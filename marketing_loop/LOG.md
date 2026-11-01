# Journal de la boucle marketing (ARE-IA + Astralixai)

Format de référence: titouan.ia (fond clair, cartes UI animées, sous-titres mot à mot, mot-clé à commenter, CTA jaune).
Générateur: `python3 gen.py specs.json` (Playwright + ffmpeg, 1080x1920, ~27 s).

## 2026-11-01
- @astralix_servicos: reel01 (démo salon 23h12), reel02 (3 perguntas), AST_reel04 (equipe 5 funções, mot-clé ATENDENTE).
- ARE-IA: ARE_reel01 (5 prompts em sequência, mot-clé GUIA) — à publier sur le compte ARE-IA.
- Mots-clés actifs: ATENDENTE (Astralixai -> DM: lien astralixai.com + offre test), GUIA (ARE-IA -> DM: are-ia.com/amostra puis lien d'achat).

## 2026-11-01 (02h-03h)
- Publiés: @areiacurso ARE_reel01 (GUIA). @astralix_servicos AST_reel04 (ATENDENTE).
- STOCK: marketing_loop/specs_next.json = 19 Reels prêts (ARE_r02..r11, AST_r05..r14 sauf r12). Publier dans l'ordre, 1 par compte et par passage, AVANT d'en créer de nouveaux. Légende = clé "caption". Mots-clés: ARE PROMPT, LISTA, IA, ROTINA, ERRO, GUIA, PERGUNTA, TEXTO, MAPA, COMECE ; AST PRECO, MADRUGADA, DEMO, AGENDA, ATENDENTE, FAQ, TESTE, CONTA, TOM.
- PROSPECTION DM (@astralix_servicos): marketing_loop/dms.json (80 commerces, message personnalisé). Envoyés: index 0 à 4 (base.barbearia, oscomparsasbarbearia, jrbarbeariacuritiba, barbeariapopularcwb, odonto.curitiba). Prochain: index 5. Méthode: profil > bouton « Enviar mensagem » (JS) > champ en bas à droite (1180,696) > taper > Entrée. 10 par passage max, jamais plus de 30/jour.
- Voix off: impossible (réseau bloque le téléchargement audio ElevenLabs).
- Veille: format WhatsApp viral = mauvaise conversation lue (@brunariccopolo 2M, @gabrielrupt 1,1M). Niche IA: « comandos do ChatGPT para [métier] » + Comenta MOT (@gabrielalvess.cc 9,7M).

## 2026-11-01 (02h40)
- Publié @astralix_servicos: AST_city01 (ville 3D d'agents, format theomenardi), mot-clé AGENTE -> DM: lien astralixai.com + « me diz o tipo do seu negócio ».
- Rendu 3D: marketing_loop/city (npm install three@0.160.0 ; NF=840 python3 rend.py ; ffmpeg -framerate 30 -i fr/%04d.jpg). Prochaine variante: ville ARE-IA (« cada prédio é um prompt »).
- DMs: envoyés index 0,2,3,4,5,6. ÉCHECS: index 1 oscomparsasbarbearia (« não pode receber mensagem », abandonner), index 7 odhosodontologia (raccourci clavier a intercepté, RENVOYER). Prochain: index 7.
- ATTENTION DM: si un popup « Atalhos de teclado » apparaît, Escape puis recliquer le champ.
- QG: https://claude.ai/artifact/6vHCo4jhrz2chauRuDWist (slug 2fee1949-882e-4d85-94ac-14f1f1264b13). Mettre à jour marketing_loop/hq/data.json (kpi + feito) puis republier avec publish_files (slug, base_version via get_artifact, fichier data.json seul).
- 03h15: publié ARE_r02 (PROMPT) sur @areiacurso, retiré du stock. Départements actifs: Boucle marketing (4x/j), Partenariats (15h43), AreiaPlay contenu & veille (11h37). Correctifs AreiaPlay (LGPD réservations, clubs non partenaires, marques fictives) demandés à Replit le 01/11 03h05.

## 2026-11-01 (12h40 BRT)
- MESURE: @astralix_servicos 67 abonnés, 41 posts. Vues Reels récents: AST_city01 25, AST_reel04 1, reel02 0, reel01 11 (médiane ~6). Portée quasi nulle -> suspicion de restriction de portée. @areiacurso non mesuré.
- ALERTE INSTAGRAM: API web_profile_info = 429, bouton « Enviar mensagem » = « Ocorreu um erro. Tente novamente » 2 fois (odhosodontologia). Traité comme premier avertissement -> ARRÊT de toute action IG ce passage (0 DM, 0 commentaire, 0 publication). Prochain passage: tester d'abord UNE action légère (ouvrir inbox); si erreur à nouveau, ne rien faire sur IG pendant 24h.
- Aucun nouveau commentaire/DM entrant (Primary, General, Pedidos vides de réponses). Prochain DM: index 7 (odhosodontologia).
- PRÊTS À PUBLIER: render/ARE_r03.mp4 (@areiacurso, légende specs_next.json ARE_r03), render/AST_r05.mp4 (@astralix_servicos, AST_r05). Carrosséis: carrossel/ARE_c01_1..7.jpg (mot-clé PROMPTS) et carrossel/AST_c01_1..7.jpg (mot-clé CHECKLIST, DM: astralixai.com + « me diz o tipo do seu negócio »). Une fois publiés, retirer ARE_r03/AST_r05 de specs_next.json.
- Nouveaux mots-clés: PROMPTS (ARE-IA -> are-ia.com/amostra), CHECKLIST (Astralixai).
