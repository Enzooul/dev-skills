# Dev Skills

Repositório-oficina para **programação** com o Claude Code — inclusive para criar e melhorar as suas próprias skills (como as `trader-*`). Abra uma sessão (claude.ai/code ou local) com este repositório selecionado, junto com o repositório do código em que vai trabalhar, e o Claude descobre automaticamente as skills em `.claude/skills/`.

Curadoria de [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) (licença MIT, ver `LICENSE-claude-skills`), copiada do commit `27cfcd0`.

## O que tem aqui (18 skills)

| Área | Skills |
|---|---|
| Criar e avaliar skills | `write-a-skill` (cria skills com estrutura correta), `book-to-skill` (transforma livros e documentações em skills), `skill-doctor` (avalia, pelo histórico real de conversas, quais skills estão funcionando) |
| Disciplina ao programar | `karpathy-coder` (4 princípios: explicitar premissas, manter simples, mudanças cirúrgicas, metas verificáveis), `zero-hallucination-coder` (nada de APIs ou imports inventados) |
| Questionar planos | `grill-me` (interroga seu plano até tudo estar claro), `grill-with-docs` (o mesmo, confrontando com a documentação do projeto) |
| Revisão e testes | `code-reviewer`, `adversarial-reviewer` (revisão crítica de verdade), `tdd-guide` (testes primeiro) |
| Especialistas | `senior-backend`, `senior-data-engineer`, `senior-data-scientist`, `senior-prompt-engineer`, `senior-security` (modelagem de ameaças e varredura de segredos), `tech-stack-evaluator` |
| Dados e IA | `universal-scraping-architect` (raspagem e extração de dados com validação), `llm-cost-optimizer` (reduzir custo de API de IA) |

## Observações

- A skill `security-guidance` do catálogo original ficou de fora: ela funciona como um gancho (hook) automático do Claude Code e não é ativada só copiando a skill.
- Os catálogos `engineering-skills` (32) e `engineering-advanced-skills` (42) do repositório de origem têm muito mais (nuvem AWS/Azure/GCP, Docker, Kubernetes, Terraform, segurança ofensiva...). Adicione aqui só quando for usar.

## Como atualizar

Copie de novo as pastas correspondentes (`engineering/<nome>/skills/<nome>` e `engineering-team/<nome>`) do repositório de origem para `.claude/skills/`.

Só as skills foram copiadas; agentes e slash commands dos plugins originais não fazem parte deste repositório, e algumas skills citam skills "irmãs" que não estão aqui — isso não impede o funcionamento.
