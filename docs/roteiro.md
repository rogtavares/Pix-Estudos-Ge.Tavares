# Roteiro de estudos — API Pix

## Etapas

- [ ] 1. Conceitos: PSP, DICT, chave Pix, txid, e2eid, BR Code (EMV)
- [ ] 2. Segurança: OAuth2 (client credentials) + mTLS com certificado
- [ ] 3. `/cob` — cobrança imediata (QR Code dinâmico)
- [ ] 4. `/cobv` — cobrança com vencimento (juros, multa, desconto)
- [ ] 5. `/loc` — locations e payload do QR Code
- [ ] 6. `/pix` — consulta de Pix recebidos e devoluções
- [ ] 7. `/webhook` — notificação de pagamento
- [ ] 8. `/lotecobv` — cobranças em lote
- [ ] 9. Prática no sandbox (Efí Bank)
- [ ] 10. Produção com custo baixo/zero (API Pix direta do banco, ex.: Inter PJ)

## Endpoints principais

| Endpoint | Uso |
|---|---|
| `PUT/POST /cob` | Cria cobrança imediata (com ou sem txid informado) |
| `GET /cob/{txid}` | Consulta status da cobrança (`ATIVA`, `CONCLUIDA`, ...) |
| `PUT /cobv/{txid}` | Cria cobrança com vencimento |
| `GET /pix` / `GET /pix/{e2eid}` | Lista/consulta Pix recebidos |
| `PUT /pix/{e2eid}/devolucao/{id}` | Solicita devolução |
| `PUT /webhook/{chave}` | Configura URL de notificação para uma chave |

## Onde praticar

| Opção | Papel | Observação |
|---|---|---|
| **Efí Bank** (ex-Gerencianet) | Laboratório | Sandbox gratuito, segue o padrão Bacen quase literalmente |
| **Banco Inter PJ** | Produção | API direta do banco; Pix PJ historicamente sem tarifa |
| Mercado Pago / Asaas | Comparação | Mais simples, mas abstraem o padrão e cobram taxa |

> **Taxa zero:** em geral vem da API Pix direta do banco (PSP), não de gateways intermediários.
> Taxas mudam — sempre confirmar a tabela vigente.

## Referências

- Visualização da spec: https://bacen.github.io/pix-api/
- Regulamentação e manuais (segurança, BR Code): https://www.bcb.gov.br/estabilidadefinanceira/pix
