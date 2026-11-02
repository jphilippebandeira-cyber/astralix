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

## 2026-11-01 (13h05 BRT, rattrapage 9h+13h)
- Test léger OK (inbox charge). PUBLIÉS sans erreur: @astralix_servicos AST_r05 (PRECO) + carrossel AST_c01 (CHECKLIST); @areiacurso ARE_r03 (LISTA) + carrossel ARE_c01 (PROMPTS). Retirés du stock (16 restants).
- MESURE @areiacurso: 30 abonnés, 33 posts; vues Reels récents 20, 12, 9, 9 (médiane ~10). @astralix_servicos 67 abonnés.
- DMs prospection et commentaires de croissance: NON faits volontairement (le bouton « Enviar mensagem » a échoué 2x il y a 20 min). Reprendre au passage de 17h avec 5 DMs max (index 7 odhosodontologia d'abord); au moindre « Ocorreu um erro » -> stop DM 24h.
- Aucun commentaire/DM entrant sur les deux comptes.
- Carrousels: format 1080x1350, crop 4:5 dans IG; Reels: crop « Original ».

## 2026-11-01 (13h20-13h35 BRT, passage 13h)
- Publication du passage 13h déjà faite à 13h05 (rattrapage) -> pas de double post.
- MESURE: @areiacurso 30 abonnés / 33 posts, Reels: ARE_r03 0 vue à +30 min, puis 20,12,9,9,17,33 (médiane ~12). @astralix_servicos 67 abonnés / 43 posts, Reels: AST_r05 0 vue à +30 min, puis 26,1,0,11,13,4 (médiane ~8). 0 vue à 30 min sur les deux = portée encore bridée.
- CONVERTIR: aucun nouveau commentaire/DM/pedido sur les deux comptes; aucune réponse aux DMs de prospection.
- CROISSANCE (sans erreur IG): @areiacurso a commenté inventormiguel (prompt fixe + exemple), pompeu.ia (photo de face pour templates Hailuo), diegoalmeida.ia (fiche de référence personnage). @astralix_servicos a commenté sebrae (PIX MEI: message fixé anti-golpe WhatsApp). Total jour: areiacurso 3, astralix 1.
- Source fiable de posts <24h: fil « Seguindo » (instagram.com/?variant=following) de @areiacurso (comptes IA suivis). Le fil d'@astralix_servicos = prospects (avocats/dentistes): pour la croissance Astralix, aller sur profils sebrae, sebraesp, etc.
- DMs prospection: toujours en pause, reprendre à 17h (5 max, index 7 odhosodontologia).

## 2026-11-01 (15h55-16h30 BRT, passage manuel demandé par JP)
- PUBLIÉS: @astralix_servicos AST_r06 (MADRUGADA), @areiacurso ARE_r04 (IA). Retirés du stock (14 restants).
- DMs: « Enviar mensagem » -> « Ocorreu um erro. Tente novamente » sur odhosodontologia (3e fois) ET belezastella (index 8). = Instagram bloque l'ouverture de nouvelles conversations sur @astralix_servicos. PAUSE DM 24h (pas avant 02/11 16h). Au retour: 1 seul essai sur index 8 belezastella; si erreur -> pause 72h et ne prospecter que via commentaires utiles.
- CONVERTIR: aucun nouveau commentaire/DM sur les deux comptes (1 like de cotedazur.travel).
- CROISSANCE: @areiacurso a commenté custodiorod (10 ganchos). Total jour: areiacurso 4, astralix 1.
- Chrome: l'ancien tabId n'existe plus après reconnexion -> toujours tabs_context_mcp(createIfEmpty) puis naviguer une 2e fois si l'onglet reste sur chrome://newtab.

## 2026-11-01 (16h20 BRT, Partenariats & Affiliés)
- Créé marketing_loop/partners.md (registre + commissions validées 20/30 % Astralixai, 40 % ebook).
- DMs entrants: aucune réponse de partenaire sur @areiacurso ni @astralix_servicos (Primary, Pedidos vides). Découvert d'anciens contacts ARE-IA (Elvizio Vanzo, Edu Sobreira, Jessica Martins...) -> listés dans partners.md, ne pas recontacter à froid.
- 9 partenaires vérifiés vidIQ (5 agences, 4 créateurs), statut a_contacter. 6e agence non trouvée (dionelbogorni = concurrent, geronimo.actis = hispanophone).
- DMs: 0 envoyé. @astralix_servicos en pause DM jusqu'au 02/11 16h. @areiacurso: profil jorgesouza.ia sans bouton « Enviar mensagem », et la recherche de destinataire dans « Nova mensagem » reste bloquée en chargement -> traité comme avertissement, arrêt. Prochain passage: 1 essai @areiacurso (gi.blanco); si échec -> pause DM 72h, prospection via commentaires utiles.
## 2026-11-01 (16h45 BRT) — tentative de contournement DM demandée par JP
- App « Instagram » sur l'ordi = web-app Chrome (com.google.Chrome.app...), accès computer-use limité à « lecture » (pas de clic/frappe) et même client web -> inutile.
- Essai voie « Nova mensagem » (direct/new) depuis @astralix_servicos: la recherche du destinataire ne charge jamais. Confirme la limite côté compte, pas côté bouton.
- Messages index 7-11 donnés à JP pour envoi manuel depuis l'app téléphone s'il le souhaite. Si JP les envoie, marquer comme faits.

## 2026-11-01 (16h45 BRT, session directe)
- SON: fond synthétique robotique SUPPRIMÉ de gen.py (piste muette). Règle: aucune musique générée par synthé. Pour les Reels, l'audio tendance ne peut être ajouté que depuis l'app mobile Instagram -> publier muet avec sous-titres forts.
- LINKEDIN (profil « are-ia ia », ARE-IA): 1 post publié (méthode des 5 prompts, lien are-ia.com) + 3 invitations (gerentes de banco / IA, Brésil). Cadence: 1 post/jour, 15 invitations/jour max, 5 commentaires utiles/jour.
- HOTMART: session déconnectée dans Chrome (page de login) -> connexion requise par JP (Claude ne saisit pas de mot de passe).
- GMAIL: aucun lead/prospect dans la boîte; à signaler à JP: « Railway Security Disclosure - Rotate Credentials ».

## 2026-11-01 (17h20-17h50 BRT, passage 17h)
- PUBLIÉ: rien (passage hors 13h/21h ; déjà 3 posts/compte aujourd'hui -> plus aucune publication avant 02/11 13h).
- MESURE: @astralix_servicos 67 abonnés / 44 posts ; AST_r06 0 vue à +1h, AST_r05 2 vues à +4h -> portée toujours bridée. @areiacurso 30 abonnés / 34 posts ; ARE_r04 14 vues à +1h, ARE_r03 17 -> légère reprise.
- CONVERTIR: aucun DM/commentaire/pedido entrant sur les deux comptes. Likes de erickschons (vérifié), leduardodias_, 0alfredinho sur nos commentaires @areiacurso. maestroprompts et michella.ia ont répondu automatiquement à nos commentaires (« enviei no direct ») : rien à faire.
- CROISSANCE @astralix_servicos: 4 commentaires (sebrae reel Empretec/franquia, contaazul « fatia » taxas maquininha, nuvemshop Black Friday FAQ, stone valuation). Suivis: contaazul, nuvemshop, sebraesp, sebraepr, sebrae. Total jour: 5 commentaires, 5 follows.
- CROISSANCE @areiacurso: 4 commentaires (hacker.prompt premissas, fabianocarvalhojr dado público, michella.ia rosto fixo, maestroprompts lacunas + 3 perguntas). Suivis: itsdavixavier, clubedasskills, willianmuller_, higgsfield.ai, openai. Total jour: 8 commentaires, 5 follows.
- Sources <24h Astralix: contaazul, nuvemshop, stone, sebrae publient tous les jours ; sebraemg n'existe pas. Astuce: shortcode commençant par DfM/DfN = <24h aujourd'hui.
- Méthode commentaire fiable: JS focus textarea -> type -> Return -> vérifier textarea vide.
- Aucune erreur Instagram pendant ce passage.

## RÈGLE PERMANENTE (01/11 17h) — FORMAT DES REELS
- gen.py est OBSOLÈTE. Utiliser EXCLUSIVEMENT marketing_loop/gen2.py et appliquer marketing_loop/FICHE_VIRALE.md (hook à t=0 sans fondu, écran réel/simulé comme preuve, changement visuel toutes les 1,5-1,8 s, durée 15-23 s, CTA « Comenta MOT » en grand dans les 3 dernières s, boucle de fin, aucun son synthétique).
- Les specs du stock specs_next.json (ancien format) doivent être RÉÉCRITS au format gen2 avant publication (écrans ChatGPT/WhatsApp, kind/msgs/stamp...). Exemples prêts: render_v2/ARE_v2_01.mp4 (@areiacurso, GUIA) et render_v2/AST_v2_01.mp4 (@astralix_servicos, ATENDENTE) -> à publier en premier (passage 13h du 02/11).

## 2026-11-02 (02h35-02h50 BRT, passage nuit)
- PUBLIÉ: rien (hors 13h/21h). Prochaine publication: 13h, render_v2/ARE_v2_01.mp4 (GUIA) et render_v2/AST_v2_01.mp4 (ATENDENTE).
- MESURE: @areiacurso 30 abonnés / 34 posts ; Reels (récent->ancien) 47, 25, 53, 18, 9, 9, 17, 33 -> ARE_r04 passé de 14 à 47, ARE_r03 de 17 à 25 : portée qui remonte. @astralix_servicos 67 abonnés / 44 posts ; Reels 2, 4, 30, 4, 2, 34 -> AST_r06 2 vues, AST_r05 4 : toujours bridé.
- CONVERTIR: DMs auto (réponses à nos commentaires) de maestroprompts, michella.ia, fabianocarvalhojr -> remerciés. ERREUR: le message pour Michela est d'abord parti chez Fabiano (liste réordonnée après envoi) -> excuse envoyée. RÈGLE: après chaque envoi, rouvrir la conversation via find() et non par coordonnées. Conta Azul = DM de bienvenue auto, pas de réponse. 0 pedido, 0 commentaire sur nos posts.
- ALERTE @areiacurso: réponse à miqueias_aurelio (post inventormiguel) -> « Não foi possível postar o comentário ». => PAUSE commentaires @areiacurso 24h (pas avant 03/11 03h). Les DMs de réponse marchent encore.
- CROISSANCE @astralix_servicos: 1 commentaire OK (contaazul DfNrBbOCeZk, juros 15% / % fixa do faturamento). Suivis: rdstation, sebraerj. À 2h30 très peu de posts <24h (sebraesp, stone, sebraerj, rdstation: aucun).
- Leads/ventes: 0.

## 2026-11-02 (17h40-18h20 BRT, rattrapage du passage 13h)
- PUBLIÉS (1/compte, 1er post du jour): @astralix_servicos render_v2/AST_v2_01.mp4 (ATENDENTE), @areiacurso render_v2/ARE_v2_01.mp4 (GUIA). Crop Original, sans erreur. => Passage 21h: PAS de nouvelle publication (écart < 5 h) ; prochaine publication 03/11 13h.
- MESURE: @astralix_servicos 67 abonnés / 45 posts ; Reels récents 5, 4, 30, 4, 2, 35 -> toujours bridé. @areiacurso 31 abonnés (+1 brans_tech) / 35 posts ; Reels 79, 31, 55, 18 -> ARE_r04 47->79 : la portée remonte bien.
- CONVERTIR: aucun commentaire/DM/pedido humain sur les deux comptes (Conta Azul et maestroprompts = messages auto). miqueias_aurelio a répondu à notre commentaire chez inventormiguel (pas de réponse : commentaires areiacurso en pause jusqu'au 03/11 03h).
- CROISSANCE @astralix_servicos: 5 commentaires OK (contaazul DfPy2pQudHN Quanto Sobra/pró-labore, contaazul DfPeLBSEZip demissão/fatos, startseuniversity DfP0rXfF5QU, lydiaemilia_ DfPeacENYrN NFS-e, sebraesc DfPEvL9Dzhk ESG). Suivi: sebraesc. Aucune erreur.
- ATTENTION: l'API /api/v1/users/web_profile_info renvoie 429 -> NE PLUS l'utiliser (risque de limitation). Trouver les posts <24h via le fil ?variant=following (balise time) ou les profils.
- @areiacurso: aucun commentaire de croissance (pause), aucun follow.
- Leads/ventes: 0.
