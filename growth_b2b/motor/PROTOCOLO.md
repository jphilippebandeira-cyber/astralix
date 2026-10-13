# Motor de Experimentos ARE-IA (criado 13/10/2026)

Objetivo: vendas de "O Guia Definitivo da IA". Regra-mae: nao repetir o que 99% faz (posts genericos, follows, Reels sem distribuicao). Cada dia = 1 experimento NOVO executado de ponta a ponta, medido e decidido.

## Ciclo diario (sempre nesta ordem)
1. MEDIR: atualizar resultados dos experimentos abertos em EXPERIMENTOS.csv (views, cliques, comentarios, citacoes, vendas Hotmart/site). Decidir: MATAR (sem sinal no prazo), ESCALAR (sinal) ou CONTINUAR.
2. PESQUISAR (30 min de fontes diferentes a cada dia, nunca so "dicas de marketing"): estudos de caso de growth, PR por dados, GEO/AEO (citacao em ChatGPT/Perplexity), marketplaces (Amazon, Hotmart), B2B/licencas, comunidades, eventos sazonais do Brasil (trainee, concursos, Enem, declaracao de IR, Black Friday), transcricoes de podcasts/palestras quando acessiveis, e analogias de outros setores (jogos, saude, educacao, varejo).
3. GERAR 10 ideias com estas forcas obrigatorias (2 por forca):
   - Inversao: o que faria o oposto do mercado?
   - Transplante: que tatica de outro setor funcionaria aqui?
   - Dados proprios: que numero inedito podemos produzir de graca (dados publicos)?
   - Utilidade: que ferramenta/lista as pessoas salvariam e compartilhariam?
   - Timing: que evento das proximas 4 semanas cria demanda agora?
4. PONTUAR cada ideia (ICE 1-10: impacto, confianca, facilidade) com filtros: R$0, Brasil PT-BR, sem risco de banimento, ToS e LGPD respeitados, sem spam, sem promessa de renda, precos nunca alterados.
5. EXECUTAR a melhor ideia executavel sozinho hoje, de ponta a ponta (criar o ativo + publicar/distribuir). Registrar hipotese, metrica e prazo (max 7 dias).
6. REGISTRAR em EXPERIMENTOS.csv e IDEIAS.md; commit e push.
7. RESUMO em frances ao Jean: o que foi testado, o que morreu, o que escalou, vendas.

## Ativos e links
- Site: https://are-ia.com (amostra /amostra; ferramentas /anonimizador e /politica-ia)
- Hotmart (checkout sem conta, R$149,00 com Pix): https://pay.hotmart.com/H107884362C?off=bb7j0mje  (NUNCA usar o link sem ?off=, mostra R$287,57)
- Recrutamento de afiliados (30%): https://affiliate.hotmart.com/affiliate-recruiting/view/9819D107884383
- Instagram @areiacurso, LinkedIn pagina "AREIA IA".

## Limites duros
- Nao enviar mensagens privadas oferecendo comissao a terceiros sem ok explicito do Jean (bloqueado pelo sistema em 13/10).
- No maximo 10 convites LinkedIn e 4 DMs Instagram por dia, nunca texto igual.
- Nao clicar em "Acessar pagina" no painel de afiliados Hotmart (faz logout).
- Nao alterar precos, checkout nem modo de pagamento.

## Experimento em curso: Mapa Trainee 2027 (E02) — rotina diaria obrigatoria ate 15/11
- Verificar se https://are-ia.com/trainee-2027 e os 18 dossies respondem 200 (se faltar algum, pedir ao Replit so o que falta, dados em motor/exp02_mapa_trainee/data.json, mensagens < 8000 caracteres).
- Quando o mapa estiver no ar: trocar o link da bio do Instagram para https://are-ia.com/trainee-2027 durante a temporada (manter "are-ia.com" no texto da bio).
- Publicar 1 carrossel por dia de um programa, na ordem do prazo mais proximo ainda aberto. Gerar com a data do dia: `python3 motor/exp02_mapa_trainee/carrossel.py AAAA-MM-DD slug` (saida em carrosseis/slug/1..5.png), enviar ao Mac (~/Downloads/areia9/slug/) e publicar pelo app Instagram (adicionar as imagens UMA por vez pelo botao +; o seletor so aceita 1 arquivo por vez). Legenda: prazo, salario, 1 dica, "Dossie completo gratis: link na bio", "Comenta o nome da empresa que eu te mando o dossie", fonte, hashtags #trainee #trainee2027 #processoseletivo #nomedaempresa.
- 13/10 (PRIORIDADE): Unilever fecha 14/10 — publicar o carrossel ~/Downloads/areia9/unilever/1..5.png antes do meio-dia.
- Responder por DM a quem comentar o nome de uma empresa, com o link do dossie (resposta a pedido, permitido).
- Ordem dos proximos: Hypera (20/10), PepsiCo (21/10), Indovinya (23/10), Praso (03/11), Grant Thornton (15/11), depois os sem prazo.
- A cada semana, atualizar prazos (fontes em data.json) e adicionar novos programas abertos.

## Servico "comenta o nome da empresa" (ativo desde 13/10, so a pedido)
- Comentario-servico publicado no carrossel do estudo trainee (13/10). Repetir a chamada na legenda de cada carrossel de empresa.
- Todo dia: ler comentarios dos posts trainee. Para cada pessoa que comentar um nome de empresa (ou pedir), responder no comentario ("Te mandei no direct!") e enviar DM com o link do dossie:
  "Oi, [nome]! Aqui está o dossiê da [empresa]: https://are-ia.com/trainee-2027/[slug] — prazo, salário, etapas, perguntas prováveis e 3 prompts para treinar. Boa sorte no processo! Se quiser, me conta em qual etapa você está que eu te digo o que treinar primeiro."
- Se a empresa nao estiver no mapa: "Ainda não tenho o dossiê da [empresa]; vou montar e te aviso." -> pesquisar a vaga publica, adicionar ao data.json, pedir a pagina ao Replit, e avisar a pessoa quando estiver no ar.
- Se a pessoa responder: conversa util (o que treinar primeiro). So mencionar o guia se ela perguntar por mais material ou demonstrar interesse; nunca pressionar.
- Isto e resposta a pedido: nao conta como prospeccao. Nunca enviar DM a quem nao pediu.

## E03 Mapa Certificacoes ANBIMA 2026 (publico banco)
- Quando https://are-ia.com/certificacoes-anbima-2026 estiver no ar: publicar o carrossel ~/Downloads/areia10/1..6.png (regerar com a data do dia: `cd motor/exp03_mapa_anbima && python3 carrossel.py AAAA-MM-DD`). Nao publicar no mesmo dia do carrossel trainee: alternar (trainee num dia, ANBIMA no outro) ou 2 posts com 6h de intervalo.
- Legenda: prazo 31/12/2026, o que cada certificacao vira, 4 passos, "Comenta ANBIMA que eu te mando o guia por DM", fontes, #anbima #cpa20 #cpa10 #cea #mercadofinanceiro #bancarios #certificacao.
- Quem comentar ANBIMA: DM "Oi, [nome]! Aqui está o guia: https://are-ia.com/certificacoes-anbima-2026 — transição até 31/12, formato das provas e 3 prompts de estudo. Qual certificação você tem hoje?"
- Postar tambem no LinkedIn (perfil are-ia ia) com o mesmo carrossel: publico bancario esta la.

## Proximos Mapas (mesma maquina, decidir pelo resultado de E02/E03)
- Estagios 2027 (temporada de inscricoes out-dez): mesmo formato do trainee.
- Concursos publicos com edital aberto (bancarios: BB, Caixa, BNB, BRB quando houver edital).
- Certificacoes CFP/CFA/CGA se E03 performar.
