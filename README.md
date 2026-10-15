# Pix Estudos — Ge.Tavares

Estudo prático da API Pix do Banco Central: da especificação oficial (Bacen) até
cobranças reais em sandbox, com foco em entender o fluxo completo e operar Pix com
taxa zero via API direta do banco.

## Estrutura

| Pasta | Conteúdo |
|---|---|
| [`docs/`](docs/) | Anotações e roteiro de estudo |
| [`spec/`](spec/) | Cópia da especificação oficial ([bacen/pix-api](https://github.com/bacen/pix-api)), só para consulta |
| [`exemplos/`](exemplos/) | Código prático (sandbox Efí Bank) |

Comece pelo [roteiro](docs/roteiro.md).

## Atualizar a especificação

```bash
curl -o spec/openapi.yaml https://raw.githubusercontent.com/bacen/pix-api/master/openapi.yaml
```

## Segurança

Certificados (`.p12`, `.pem`) e credenciais (`.env`) **nunca** vão para o Git — já estão no `.gitignore`.
