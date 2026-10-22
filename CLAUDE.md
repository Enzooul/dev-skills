# Dev Skills

Este repositório é a oficina de **programação**, inclusive para criar e melhorar as skills do usuário (como as `trader-*`). Normalmente é aberta junto com o repositório do código em que se vai trabalhar. As skills ficam em `.claude/skills/`.

## Como responder

- O usuário escreve em **português do Brasil**: responda sempre em português, mesmo que a skill esteja escrita em inglês. Termos técnicos podem ficar em inglês quando não houver tradução comum, com uma explicação curta na primeira vez.
- O usuário tem conhecimento **intermediário**: comece com uma explicação curta do que vai ser feito e por quê, depois entregue o trabalho principal. Textos claros, completos e didáticos.
- Em estratégias e planos, seja o mais avançado e completo possível.
- **Não invente informações.** Se um dado não puder ser verificado (preço, número, fato, fonte), diga que não sabe ou que está no limite do seu conhecimento.

## Como escolher a skill

- Os pedidos chegam em português; as descrições das skills estão em inglês. Use o mapa abaixo para traduzir o pedido na skill certa.
- Se o pedido não bater claramente com uma skill, comece pelo **roteador** indicado no mapa: ele escolhe a especialista.
- Diga ao usuário, em uma linha, qual skill está usando e por quê.

## Arquivos gerados

Sessões na nuvem são apagadas ao terminar. Quando uma skill gerar um arquivo que valha guardar (relatório, plano, contexto), salve-o dentro deste repositório e ofereça fazer commit.

## Mapa de pedidos

| Pedido em português | Skill |
|---|---|
| "cria uma skill", "melhora essa skill" | `write-a-skill` |
| "transforma esse livro/documentação numa skill" | `book-to-skill` |
| "minhas skills estão funcionando?" | `skill-doctor` |
| "questiona meu plano", "me sabatina" | `grill-me` (com documentação do projeto: `grill-with-docs`) |
| tarefa de código importante ou que mexe em código existente | `zero-hallucination-coder` |
| "estou complicando demais?", "antes de commitar" | `karpathy-coder` |
| "revisa meu código" | `code-reviewer`; revisão bem crítica: `adversarial-reviewer` |
| "escreve testes", "TDD" | `tdd-guide` |
| "API", "banco de dados", "backend" | `senior-backend` |
| "pipeline de dados", "ETL" | `senior-data-engineer` |
| "modelo estatístico", "machine learning", "experimento" | `senior-data-scientist` |
| "melhora esse prompt", "avalia respostas da IA" | `senior-prompt-engineer` |
| "segurança", "tem senha/chave exposta?" | `senior-security` |
| "qual tecnologia usar?", "comparar frameworks" | `tech-stack-evaluator` |
| "raspar dados de um site", "extrair dados" | `universal-scraping-architect` |
| "custo da API de IA está alto" | `llm-cost-optimizer` |
