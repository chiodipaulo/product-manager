# Currículo por Vaga

**Uma skill de IA para analisar a aderência entre currículo, LinkedIn e vaga antes de reescrever qualquer coisa.**

Nome técnico: **ATS Architect v1**

A maioria das ferramentas começa trocando palavras. Esta skill começa verificando evidências.

Ela interpreta a descrição da vaga, identifica requisitos obrigatórios e desejáveis, compara esses requisitos com a trajetória do candidato, encontra lacunas de contexto e só reescreve o currículo depois de confirmar as informações necessárias.

> Um currículo pode esconder um bom candidato. Não pode criar a experiência que a vaga exige.

## O que a skill faz

A ATS Architect conduz um processo estruturado para:

- analisar a descrição completa da vaga;
- separar requisitos explícitos, desejáveis, inferidos e contextuais;
- identificar critérios potencialmente eliminatórios;
- extrair evidências do currículo e do LinkedIn;
- diferenciar aderência profissional de qualidade da candidatura;
- apontar experiências relevantes que estão mal comunicadas;
- detectar inconsistências, lacunas e afirmações sem sustentação;
- entrevistar o candidato antes da reescrita;
- adaptar o currículo para uma vaga específica;
- recomendar ajustes de headline, Sobre, experiências e competências no LinkedIn;
- auditar legibilidade, consistência e integridade antes do envio.

## O que ela evita

A skill foi construída para não:

- responder com dicas genéricas quando falta contexto;
- inventar experiências, métricas, ferramentas ou resultados;
- inflar senioridade ou alterar cargos históricos;
- esconder incompatibilidades importantes;
- repetir palavras-chave sem evidência;
- tratar uma nota de ATS como verdade universal;
- garantir aprovação em processos seletivos.

Contexto insuficiente não autoriza resposta genérica. Autoriza apenas coleta de contexto.

## Como funciona

### 1. Validação de contexto

Antes de analisar, a skill identifica o modo solicitado e verifica se possui as entradas mínimas.

Para adaptar um currículo a uma vaga, ela solicita:

- currículo atual;
- descrição completa da vaga;
- país da candidatura;
- idioma desejado.

O LinkedIn é recomendado, mas pode ser enviado depois.

### 2. Diagnóstico inicial

A skill apresenta:

- requisitos obrigatórios e desejáveis;
- critérios de risco;
- experiências mais aderentes;
- evidências fortes, parciais e ausentes;
- incompatibilidades;
- aderência profissional;
- qualidade atual da candidatura;
- parecer preliminar.

Ela não reescreve o currículo nesta etapa quando ainda existem lacunas relevantes.

### 3. Entrevista de evidências

A skill faz apenas perguntas que podem mudar materialmente a candidatura.

Exemplos:

- Qual métrica determinava a priorização desse produto?
- Você já construiu um Business Case com receita, custo, margem ou payback?
- Qual era o tamanho da operação ou da base afetada?
- Você apresentou essa decisão para qual nível de liderança?
- Qual foi sua responsabilidade direta no resultado informado?

### 4. Reescrita

Depois das confirmações, a skill gera uma versão adaptada para a vaga usando apenas informações sustentadas pelo candidato.

A estrutura dos bullets prioriza:

`ação + problema ou objeto + contexto ou escala + decisão ou método + resultado verificável`

### 5. Auditoria final

Antes da entrega, a skill revisa:

- fatos sem origem;
- métricas não confirmadas;
- datas e cargos;
- divergências entre currículo e LinkedIn;
- exageros de linguagem;
- repetição artificial de palavras-chave;
- requisitos ainda não atendidos;
- problemas de legibilidade do documento.

## Entregáveis

A execução completa pode gerar:

1. parecer executivo da candidatura;
2. matriz de requisitos e evidências;
3. currículo adaptado para a vaga;
4. recomendações para o LinkedIn;
5. evidências que o candidato precisa defender em entrevista;
6. riscos que a redação não consegue resolver;
7. checklist final de envio.

## Modos de uso

### Diagnóstico para uma vaga

Compara currículo e vaga, identifica aderência, riscos e lacunas.

### Otimização completa

Inclui diagnóstico, entrevista de evidências, reescrita e auditoria.

### Auditoria geral

Analisa o currículo mesmo sem uma vaga específica. Nesse modo, a skill solicita cargo, senioridade, país e idioma pretendidos.

### Auditoria final

Revisa uma versão já pronta antes da candidatura.

### Comparação entre vagas

Compara o mesmo perfil com diferentes oportunidades e mostra onde existe maior aderência verificável.

## Uso com voz ao vivo

O modo voz ao vivo é recomendado durante a entrevista de evidências.

Ele tende a funcionar melhor para recuperar:

- métricas;
- decisões;
- escopo;
- contexto de projetos;
- conflitos;
- exposição executiva;
- gestão de pessoas;
- domínio real de ferramentas.

A investigação pode acontecer por voz. A entrega final permanece em texto.

## Como instalar

1. Baixe ou clone este repositório.
2. Mantenha a estrutura de arquivos e pastas.
3. Adicione a pasta da skill ao ambiente compatível com skills.
4. Inicie uma nova conversa e anexe os materiais necessários.

Estrutura:

```text
curriculo-por-vaga/
├── SKILL.md
├── README.md
├── LICENSE.md
├── references/
│   ├── job-analysis.md
│   ├── evidence-taxonomy.md
│   ├── matching-rules.md
│   ├── resume-rewriting.md
│   ├── ats-readability.md
│   ├── linkedin-alignment.md
│   ├── integrity-rules.md
│   └── decision-rubric.md
└── templates/
    ├── diagnostic-report.md
    ├── evidence-interview.md
    ├── optimized-resume.md
    └── final-audit.md
```

## Primeiro uso

Anexe o currículo e cole a descrição completa da vaga. Depois, use:

```text
Execute o processo completo da ATS Architect.

Comece validando se há contexto suficiente. Depois, faça o diagnóstico de aderência profissional e qualidade da candidatura.

Não reescreva o currículo antes da entrevista de evidências. Não invente informações para preencher lacunas.
```

Quando a skill terminar o diagnóstico e fizer as perguntas necessárias, responda e solicite:

```text
Agora gere a versão adaptada do currículo, recomende os ajustes do LinkedIn e execute a auditoria adversarial final.
```

## Limites

A skill melhora fatores controláveis da candidatura. Ela não conhece a configuração interna de cada ATS e não controla:

- critérios não publicados;
- perguntas eliminatórias do formulário;
- volume e qualidade dos concorrentes;
- indicações internas;
- decisões de recrutadores e gestores;
- mudanças na vaga;
- políticas da empresa.

Por isso, ela não garante aprovação em triagem ou contratação.

## Licença

Este repositório é público para consulta e uso autorizado, mas o conteúdo permanece protegido por uma licença proprietária.

O acesso público não concede autorização automática para:

- redistribuir;
- revender;
- sublicenciar;
- publicar cópias;
- remover a autoria;
- utilizar a estrutura para comercializar um produto concorrente.

Consulte o arquivo [`LICENSE.md`](./LICENSE.md) antes de utilizar ou compartilhar este material.

## Autoria

Criado por **Paulo Chiodi**, fundador do Product Guru's.

Conteúdo sobre produto, inteligência artificial, negócios e carreira:

- LinkedIn: `linkedin.com/in/paulochiodi`
- Newsletter: `productgurus.substack.com`
