# Fluxo de estudo

Cada etapa do [roteiro](roteiro.md) é estudada numa branch própria e entra na `main` via Pull Request.

## Nomes de branch

```
estudo/<nº da etapa>-<assunto>
```

| Prefixo | Uso | Exemplo |
|---|---|---|
| `estudo/` | Uma etapa do roteiro | `estudo/02-oauth-mtls`, `estudo/03-cob` |
| `fix/` | Correção | `fix/token-expirado` |
| `docs/` | Só documentação | `docs/fluxo-de-estudo` |

> A data não vai no nome: o Git já registra a data de cada commit.

## Ciclo de cada estudo

```bash
# 1. Partir da main atualizada
git checkout main
git pull
git checkout -b estudo/02-oauth-mtls

# 2. Estudar com commits pequenos
git add .
git commit -m "docs: anotacoes sobre mTLS"

# 3. Enviar e abrir Pull Request
git push -u origin estudo/02-oauth-mtls
gh pr create --fill

# 4. Revisar no GitHub e fazer o merge
gh pr merge --squash --delete-branch

# 5. Voltar para a main atualizada
git checkout main
git pull
```

Ao final, marcar a etapa como concluída no [roteiro](roteiro.md) (`- [x]`).

## Mensagens de commit

```
<tipo>: <o que foi feito>
```

| Tipo | Quando usar |
|---|---|
| `feat` | Código novo (exemplo, script) |
| `fix` | Correção |
| `docs` | Anotações e documentação |
| `chore` | Estrutura, configuração, dependências |

## Marcos (tags)

Ao concluir um bloco de etapas:

```bash
git tag v0.1-fundamentos
git push --tags
```

| Tag | Etapas |
|---|---|
| `v0.1-fundamentos` | 1–2 (conceitos, OAuth2 + mTLS) |
| `v0.2-cobrancas` | 3–5 (`/cob`, `/cobv`, `/loc`) |
| `v0.3-recebimentos` | 6–8 (`/pix`, `/webhook`, lote) |
| `v1.0-producao` | 9–10 (sandbox completo e produção) |

## O que é público

O repositório é público: arquivos, branches, histórico e PRs ficam visíveis.

- Credenciais e certificados (`.env`, `.p12`, `.pem`) são bloqueados pelo `.gitignore`.
- Anotações pessoais vão na pasta `privado/`, que também fica fora do Git.
