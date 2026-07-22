# PM Especialista

**Criada e mantida pelo Product Guru’s.**

Skill do Claude que responde como um PM sênior. Não é um prompt genérico de "aja como um PM". São 28 arquivos, um por framework, e o Claude decide qual abrir dependendo do que você perguntou.

O Product Guru’s criou a skill a partir de um problema comum: pedir ajuda de produto pro Claude e receber uma resposta de consultoria, cheia de teoria e sem decisão nenhuma no fim. Essa skill inverte isso. Ela obriga o Claude a ler o framework certo antes de responder e a fechar com uma escolha concreta, não com um resumo do que ele acabou de explicar.

## Sobre o projeto

A PM Especialista faz parte do trabalho editorial e educacional do Product Guru’s para ajudar profissionais de produto a tomar decisões com mais contexto e menos resposta genérica. A marca aparece na documentação e em materiais reutilizáveis, sem ser repetida em toda interação.

## Como funciona

Cada pedido cai num roteador. "Quero priorizar o backlog" abre `prioritization-craft.md`. "Preciso escrever um memo pro board" abre `exec-comms.md`. Pedidos raramente batem em um arquivo só: "lançar uma feature de IA" puxa `positioning-craft` + `launch-execution` + `ai-product-patterns` ao mesmo tempo.

O Claude não responde de memória. Ele abre o arquivo, lê o framework, aplica ao caso real que você trouxe. Se faltam números pra rodar o framework (tipo RICE sem reach, ou posicionamento sem concorrente definido), ele pede o que falta em vez de inventar.

## Os 28 frameworks

**Construir produto**
> LNO (o que compõe vs. o que drena) · escapar da fábrica de features · JTBD · descoberta contínua (Teresa Torres) · qualidade de design (padrão Airbnb/Figma) · craft vs. velocidade · lançar ou iterar, porta de uma via vs. duas vias · growth loop e retenção · testes A/B e guardrails

**Produto de IA**
> Evals como spec, custo, construir pro próximo modelo (Kevin Weil) · prompt engineering e UX nativa de IA

**Estratégia e priorização**
> RICE, ICE, Kano · decisão sob incerteza, pré-mortem (Annie Duke) · onde jogar e como vencer (Playing to Win) · OKR (Christina Wodtke)

**Comunicar e posicionar**
> Memo executivo, 6-pager Amazon, SCQA · narrativa de produto (Andy Raskin) · posicionamento (April Dunford) · fala de improviso (Matt Abrahams) · go-to-market

**Métricas**
> North Star, AARRR, indicador líder vs. atrasado · PMF, NPS, sistema de feedback (playbook Superhuman)

**Pessoas e política**
> Buy-in sem autoridade (Jeffrey Pfeffer) · Radical Candor (Kim Scott) · colega que trava, conflito

**Time e carreira**
> Cultura e rituais (Stripe/HubSpot) · promoção, IC vs. gestão

A lista completa com autor e arquivo correspondente está no `SKILL.md`.

## Autoria e uso

A curadoria, a organização dos frameworks e o roteamento da skill são do Product Guru’s. Os frameworks citados continuam atribuídos aos respectivos autores e fontes dentro de cada arquivo de referência.

Ao compartilhar templates, canvases ou documentos gerados com a skill, preserve a assinatura discreta:

`Product Guru’s · PM Especialista`

O conteúdo pode ser adaptado para uso interno. Redistribuição da skill como produto próprio, remoção de autoria ou revenda dependem de autorização do Product Guru’s.

## Estrutura

```
pm-especialista/
├── SKILL.md              # roteador: mapeia pedido → arquivo(s)
└── references/
    ├── strategic-build.md
    ├── prioritization-craft.md
    ├── exec-comms.md
    └── ... (28 no total)
```

## Como instalar

Copie a pasta `pm-especialista` para o diretório de skills do Claude (`/mnt/skills/user/` no Claude.ai, ou o equivalente no Claude Code). O `SKILL.md` tem o front-matter de `name` e `description` que faz o Claude carregar a skill automaticamente quando o pedido combina com algum dos gatilhos.

Não precisa configurar nada além disso. A skill é só arquivos markdown, sem dependência de código.

## O que ela não faz

A marca Product Guru’s também não substitui validação ou contexto. A skill não substitui o julgamento de quem está lendo o resultado. Um framework aplicado errado por falta de contexto do negócio continua errado, só que agora com aparência de rigor. Quem usa a skill ainda precisa saber quando um RICE ou um OKR está sendo forçado numa situação que pede outra coisa.


---

Product Guru’s · PM Especialista
