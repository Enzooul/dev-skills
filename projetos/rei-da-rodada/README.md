# Rei da Rodada

Jogo de futebol brasileiro para navegador que junta duas ideias:

- **Fantasy de rodada** (no estilo dos fantasy games do campeonato brasileiro): orçamento de M$ 100, 6 formações, capitão ×1,5, scouts, valorização de jogadores, situação Provável/Dúvida/Lesionado/Suspenso, suspensão por cartões, campeonato de 20 clubes em 38 rodadas e liga contra 9 rivais controlados pelo computador.
- **Carreira de desenhar o passe** (no estilo de jogos como Score Hero): você arrasta o dedo/mouse a partir da bola e o traço vira o caminho exato da bola. Termine em um companheiro para passar ou dentro do gol para chutar. Marcadores correm para cortar, o goleiro sai na bola, e menos toques dão mais estrelas. São 40 fases.

**A ligação entre os modos:** o craque que você cria na carreira entra no mercado do fantasy. Gols, assistências e finalizações dele nas fases viram scouts na próxima rodada (até 3 de cada), e cada estrela nova rende M$ 0,50 no caixa.

## Como jogar

Abra `index.html` no navegador. Não precisa instalar nada. O progresso fica salvo no próprio navegador (localStorage).

> O arquivo segue o formato de Artifact do claude.ai (sem `<!doctype>`/`<html>`/`<body>`, que são adicionados na publicação). Os navegadores abrem ele normalmente assim mesmo.

## Avisos

- Clubes, jogadores e técnicos são **fictícios**, gerados com semente fixa (os mesmos em toda visita).
- A tabela de pontos é **própria deste jogo**. Não é a tabela oficial de nenhum produto.
- Não há ligação com nenhuma liga, clube ou marca real.

## Estrutura do código (tudo em `index.html`)

| Parte | O que faz |
|---|---|
| `CLUBES`, `gerarElencos()` | 20 clubes e 360 jogadores com rating, preço e média iniciais |
| `CALENDARIO` | Pontos corridos pelo método do círculo (19 de ida + 19 de volta) |
| `jogarRodada()` | Simula os jogos com distribuição de Poisson, distribui scouts, atualiza tabela, preços, situação e liga |
| `escalarAuto()` | Escalação automática (usada pelo botão e pelos rivais) |
| `gerarFase()`, `atualizar()`, `desenhar()` | O jogo de desenhar o passe em `<canvas>` |
| `terminar()` | Estrelas, bônus e scouts do craque para o fantasy |
