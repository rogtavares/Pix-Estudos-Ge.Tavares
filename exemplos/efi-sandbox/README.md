# Exemplo: cobrança Pix no sandbox da Efí (Python)

Cria uma cobrança imediata (`/cob`), gera o QR Code (`/loc`) e consulta o status.
Etapas 2, 3 e 5 do [roteiro](../../docs/roteiro.md).

## 1. Pré-requisitos na Efí

1. Conta em https://sejaefi.com.br
2. **API → Aplicações → Nova aplicação**, com os escopos de **API Pix** em homologação
   (`cob.write`, `cob.read`, `pix.read`, `gn.pix.evp.write`...).
   Anote o `Client_Id` e o `Client_Secret` de **homologação**.
3. **API → Meus certificados → Homologação → Novo certificado** e baixe o `.p12`.

## 2. Converter o certificado

O `requests` usa PEM. Salve o `.p12` em `certs/` e converta (Git Bash):

```
openssl pkcs12 -in certs/homologacao.p12 -out certs/homologacao.pem -nodes -passin pass:
```

> `certs/*.p12` e `certs/*.pem` estão no `.gitignore` — nunca vão para o GitHub.

## 3. Ambiente Python

```
py -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
cp .env.example .env
```

Edite o `.env` com seu `Client_Id`, `Client_Secret` e o caminho do certificado.

## 4. Rodar

```
py cob.py chave             # cria chave Pix aleatória -> coloque em EFI_CHAVE_PIX
py cob.py criar 10.50       # cria cobrança, mostra Copia e Cola, salva qrcode.png
py cob.py consultar <txid>  # status: ATIVA, CONCLUIDA...
```

## O que observar

- **mTLS:** sem o certificado, nem o `/oauth/token` responde.
- **txid:** com `POST /cob` o PSP gera; com `PUT /cob/{txid}` você escolhe (26 a 35 caracteres alfanuméricos).
- **Copia e Cola:** é o BR Code (padrão EMV) — o mesmo conteúdo do QR Code.
- Em homologação o Pix **não é pago de verdade**; a cobrança fica `ATIVA`.
