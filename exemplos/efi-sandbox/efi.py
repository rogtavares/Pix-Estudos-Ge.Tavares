"""Cliente mínimo da API Pix da Efí (homologação).

Autenticação em duas camadas, como exige o padrão Bacen:
  1. mTLS: o certificado (.pem) vai em TODA requisição (parâmetro `cert`).
  2. OAuth2 client_credentials: troca Client_Id/Secret por um access_token.
"""
import os

import requests
from dotenv import load_dotenv

load_dotenv()

_faltando = [v for v in ("EFI_CLIENT_ID", "EFI_CLIENT_SECRET", "EFI_CERT_PEM") if not os.getenv(v)]
if _faltando:
    raise SystemExit(f"Faltam no .env: {', '.join(_faltando)} (copie .env.example para .env)")

BASE_URL = os.getenv("EFI_BASE_URL", "https://pix-h.api.efipay.com.br")
CLIENT_ID = os.environ["EFI_CLIENT_ID"]
CLIENT_SECRET = os.environ["EFI_CLIENT_SECRET"]
CERT = os.environ["EFI_CERT_PEM"]
CHAVE_PIX = os.getenv("EFI_CHAVE_PIX", "")


def obter_token():
    resp = requests.post(
        f"{BASE_URL}/oauth/token",
        auth=(CLIENT_ID, CLIENT_SECRET),
        json={"grant_type": "client_credentials"},
        cert=CERT,
    )
    resp.raise_for_status()
    return resp.json()["access_token"]


class Efi:
    def __init__(self):
        self.session = requests.Session()
        self.session.cert = CERT
        self.session.headers["Authorization"] = f"Bearer {obter_token()}"

    def _req(self, metodo, caminho, **kwargs):
        resp = self.session.request(metodo, f"{BASE_URL}{caminho}", **kwargs)
        if not resp.ok:
            raise RuntimeError(f"{resp.status_code} {metodo} {caminho}: {resp.text}")
        return resp.json() if resp.content else {}

    # --- Chave Pix (endpoint próprio da Efí, fora da spec Bacen) ---
    def criar_chave_aleatoria(self):
        return self._req("POST", "/v2/gn/evp")

    # --- /cob: cobrança imediata (spec Bacen) ---
    def criar_cob(self, valor, chave, descricao="Estudo Pix", expiracao=3600):
        corpo = {
            "calendario": {"expiracao": expiracao},
            "valor": {"original": f"{valor:.2f}"},
            "chave": chave,
            "solicitacaoPagador": descricao,
        }
        # POST /cob: o PSP gera o txid. Com PUT /cob/{txid} você escolhe o txid.
        return self._req("POST", "/v2/cob", json=corpo)

    def consultar_cob(self, txid):
        return self._req("GET", f"/v2/cob/{txid}")

    # --- /loc: payload do QR Code ---
    def qrcode(self, loc_id):
        return self._req("GET", f"/v2/loc/{loc_id}/qrcode")
