# Rei da Rodada

Fantasy do **Brasileirão Série A 2026** para navegador, com **liga entre amigos** e um modo carreira de "desenhar o passe".

## O que tem

- **20 clubes e 556 jogadores reais** da Série A 2026, mais um técnico por clube (sem nome).
- **Preço e qualidade pelo valor de mercado:** quanto mais valioso o jogador, mais caro e melhor no jogo (escala logarítmica: € 30 mi ≈ M$ 20; € 100 mil ≈ M$ 1,8).
- **Força dos clubes** pelo valor total do elenco (Palmeiras e Flamengo no topo; Remo e Chapecoense na base).
- **Fantasy:** M$ 100, 6 formações, capitão ×1,5, scouts, valorização, situação (Provável, Dúvida, Reserva, Lesionado, Suspenso), suspensão por cartões, 38 rodadas simuladas.
- **Liga com amigos (página publicada no claude.ai):** cada pessoa monta o próprio time, todos veem o ranking e os times uns dos outros, e o dono da liga fecha as rodadas. A rodada é simulada uma vez e vale igual para todos.
- **Carreira:** você desenha o caminho da bola para passar e chutar (40 fases). O craque criado entra no seu mercado e pontua com o que fez nas fases.
- **Modo solo:** fora do claude.ai (abrindo o arquivo direto), o jogo roda contra 9 rivais do computador, salvo no navegador.

## Como convidar os amigos

1. Abra a página publicada uma vez (isso cria a liga).
2. No menu **Compartilhar** da página, convide cada amigo **por e-mail como Editor**. Pelas regras da plataforma, só quem é dono, Editor convidado por e-mail ou (em planos de equipe) membro da organização com acesso de Colaborador consegue salvar dados. Quem só recebe o link apenas assiste.
3. Cada amigo abre o link, dá nome ao time e escala.
4. Você (dono) clica em **Fechar rodada** quando todos tiverem escalado.

## Fontes dos dados

- Elencos, posições, idades e valores de mercado: **Transfermarkt**, consultado em 24/10/2026 (`dados/elencos_tm.json`).
- **Bahia e Chapecoense:** o Transfermarkt bloqueou o acesso automático; os elencos vieram da Wikipédia em português (atualizados lá em 21/03/2026 e 13/10/2026). Sem valor individual verificado, o preço deles é **estimado** pela mediana da posição, e o mercado mostra "valor estimado". O mesmo vale para ~35 jogadores sem valor publicado no Transfermarkt.
- Cores dos clubes só como identificação. Nenhum escudo ou marca oficial é usado.
- Elencos mudam a cada janela de transferências: para atualizar, rode de novo `dados/parse.py` e `dados/gerar.py` com as páginas novas e substitua `dados.js`.

## Limitações conhecidas

- Os jogos e scouts são **simulados** a partir da força dos elencos. Não são os resultados reais das partidas.
- Técnicos não têm nome (os dados de técnicos não foram coletados).

## Arquivos

| Arquivo | O que é |
|---|---|
| `index.html` | O jogo (formato de Artifact do claude.ai) |
| `dados.js` | Clubes e jogadores, gerado por `dados/gerar.py` |
| `dados/parse.py` | Extrai os elencos das páginas salvas do Transfermarkt |
| `dados/wiki.py` | Elencos de Bahia e Chapecoense (Wikipédia) |
| `dados/gerar.py` | Junta tudo e gera `dados.js` |
