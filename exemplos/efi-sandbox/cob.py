"""Cobrança imediata (/cob) no sandbox da Efí.

Uso:
  py cob.py chave             -> cria uma chave Pix aleatória de homologação
  py cob.py criar 10.50       -> cria cobrança e salva o QR Code em qrcode.png
  py cob.py consultar <txid>  -> mostra o status da cobrança
"""
import base64
import json
import sys

from efi import CHAVE_PIX, Efi


def mostrar(dados):
    print(json.dumps(dados, indent=2, ensure_ascii=False))


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return

    comando = sys.argv[1]
    efi = Efi()

    if comando == "chave":
        mostrar(efi.criar_chave_aleatoria())
        print("\nCopie a chave acima para EFI_CHAVE_PIX no arquivo .env")

    elif comando == "criar":
        if not CHAVE_PIX:
            sys.exit("Defina EFI_CHAVE_PIX no .env (rode: py cob.py chave)")
        valor = float(sys.argv[2]) if len(sys.argv) > 2 else 1.00
        cob = efi.criar_cob(valor, CHAVE_PIX)
        mostrar(cob)

        qr = efi.qrcode(cob["loc"]["id"])
        imagem = qr["imagemQrcode"].split(",", 1)[1]
        with open("qrcode.png", "wb") as f:
            f.write(base64.b64decode(imagem))

        print(f"\ntxid: {cob['txid']}")
        print(f"Pix Copia e Cola:\n{qr['qrcode']}")
        print("\nQR Code salvo em qrcode.png")

    elif comando == "consultar":
        mostrar(efi.consultar_cob(sys.argv[2]))

    else:
        print(__doc__)


if __name__ == "__main__":
    main()
