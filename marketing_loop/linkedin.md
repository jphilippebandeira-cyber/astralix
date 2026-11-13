# LinkedIn ARE-IA — journal (profil « are-ia ia », interface en français)

Règles: 1 post PT-BR/jour (lien are-ia.com une fois sur deux, en fin de post), 15 invitations sans note/jour max (recherche Personnes filtrée Brésil geoUrn 106057199), 5 commentaires utiles/jour. Stop au premier avertissement LinkedIn.

## Posts déjà publiés (ne pas répéter)
- 01/11: méthode des 5 étapes (contexto, pesquisa, rascunho, revisão, formato) — AVEC lien
- antérieurs: 4 partes do prompt (contexto/papel/tarefa/formato); o que nunca colar numa IA (LGPD); voz clonada 3 sinais; teste antigolpe 8 mensagens; Pix por engano/devolver; checklist plantão saúde; IA não é mágica é método; 26,5 % formés (Serasa 2026); appel afiliados 30 % Hotmart; + posts FR
- 02/11: prompt de ata de reunião (4 blocos + [A DEFINIR] + e-mail de follow-up) — SANS lien
- 03/11: prompt e-mail de cliente irritado (3 passos + [CONFIRMAR] + LGPD) — AVEC lien amostra grátis
- 06/11: prompt fórmula Excel (descrever colunas, SOMASES x SUMIFS, testar em 3 linhas, colar o erro) — SANS lien
- 07/11: prompt preparar conversa de feedback difícil (fatos x interpretações, roteiro, 3 reações prováveis, [EXEMPLO?], LGPD) — AVEC lien amostra grátis
- 07/11 (20h UTC): prompt resumo executivo de relatório longo (5 linhas, 3 números com origem, o que o relatório não responde, [VERIFICAR], LGPD) — SANS lien (prochain post: AVEC lien)

## File d'attente DOCUMENTS (PDF carrousel, marketing_loop/linkedin_docs/, généré par build.py depuis decks.json)
- D1_banco_7_prompts — PROGRAMMÉ mar. 10/11 08:00
- D3_5_erros_prompt — PROGRAMMÉ mer. 11/11 08:00
- D2_primeiro_emprego — PROGRAMMÉ ven. 13/11 08:00 (programmé le 13/11 ~02h UTC)
- D4_rh_recrutamento (10 pages, créé 13/11) — EN FILE, non programmé (créneau lun. 16/11 déjà pris).
- PROGRAMMÉS PAR UNE AUTRE SESSION (vus 13/11, ne pas répéter) : lun. 16/11 08:30 « 5 regras de LGPD para usar ChatGPT na empresa » (doc 7 p.) ; mer. 18/11 08:30 « Treinar a equipe em IA: faça a conta » (doc) ; ven. 20/11 08:30 « Trainee 2027: 3 prompts » (lien are-ia.com).
- Prochain créneau libre : mar. 17/11 ou jeu. 19/11 08:00 -> D4.
- Prochains sujets (non faits) : vendas/comercial, atendimento ao cliente, gestor de equipe 1:1, estudante TCC/estudos, analista financeiro.

## Astuces techniques
- DOCUMENT : composer > « + » > Document. L'input file n'existe pas dans le DOM : surcharger HTMLInputElement.prototype.click (capturer l'input type=file, l'attacher au body avec aria-label « captured file input », ne pas ouvrir le sélecteur), cliquer « Choisir un fichier » via JS, find « captured file input », puis file_upload depuis /mnt/user-data/outputs/. Titre (≤58 car.) > Terminé > coller la légende.
- PROGRAMMER : icône horloge à gauche de Publier ; date JJ/MM/AAAA, heure en tapant 8:00 puis clic dans la liste ; « Publication à … » confirme ; Confirmer > Programmer. Fuseau du navigateur = Brasília.
- LIMITE : compte non vérifié -> 1 post/jour (y compris programmés créés le même jour ?) et ~1 commentaire/jour. Toast « Procédez à la vérification » : la vérification d'identité LinkedIn (action JP) lèverait ces limites.
- Composer et commentaires = éditeur tiptap/ProseMirror. La frappe `type` ne marche pas: coller via JS (ClipboardEvent paste, text/html avec <p> par ligne et <p><br></p> pour les lignes vides). Pour vider: cmd+a puis Delete (Mac).
- Modale d'invitation « Ajouter une note ? » est dans un shadow DOM: bouton « Envoyer sans note » via element.shadowRoot. Liens d'invitation: aria-label « Inviter X à rejoindre votre réseau ».
- Commentaire: clic sur bouton « Commenter » du post (find), puis coller dans l'éditeur focalisé et cliquer « Commenter » voisin.

## 2026-11-02 (passage planifié)
- POST: ata de reunião (prompt prêt à copier), sans lien.
- Commentaires/messages reçus: aucun (seul message = LinkedIn Team). Post du 01/11: 37 impressions.
- INVITATIONS (15, sans note, aucun avertissement): gerentes relacionamento banco (Heraldo Francisco/Bradesco, Fabiana Paniza, Samuel Silva), analistas RH IA (Milena Azevedo, Vinicius Szajda Abbarado, Maiara Lima, Lilian Galicia), estudantes administração IA (Geovanna Carvalho, Hellen Beatriz, Pedro Gabriel Pimenta, Mirela Neves Tavares Da Silva), professores gestão IA (Thiago Soares Zezzi, Fernando Sabathé Teixeira, Alessandro Alencar), analista bancário ChatGPT (Letícia Alves, RH).
- COMMENTAIRES (5): Luiz Henrique Lobo (IA no trabalho, gargalo de revisão), Leo Candido (DeepSeek dsh-superagent, painel atenção humana), Karen Abecia (prompt foto LinkedIn), Lucíola Coelho (prompt currículo: não inventar números), Luciano Vasconcelos Filho (rinha Claude Code vs Codex: custo total + revisão).
- Mots-clés déjà utilisés: gerente de relacionamento banco IA; analista de RH IA; estudante de administração IA; professor gestão IA; analista bancário ChatGPT. Prochaine fois: gestor de equipe, coordenador financeiro, RH treinamento, gerente de agência.
- 02/11 20h50 UTC: rattrapage manuel du passage 11h23 -> quota du jour déjà fait (post, 15 invitations, 5 commentaires) : rien republié. Aucun commentaire ni message LinkedIn entrant, aucun nouvel e-mail prospect (brouillon Catia toujours en attente).

## 2026-11-03 (passage planifié 19h10 UTC)
- POST: prompt pour répondre à un e-mail de client irrité (lister le pedido real / séparer ce qui dépend de moi / réponse courte + [CONFIRMAR]), AVEC lien are-ia.com (amostra grátis) en fin de post. Publié sans erreur.
- Entrant: aucun commentaire, aucun message (seul LinkedIn Team). Post ata 02/11: 132 impressions; 72 impressions semaine. Nouvel abonné: Alexandre Masiero.
- INVITATIONS (15, sans note, aucun avertissement): gerente de agência IA (Leandro Morimoto, Gustavo Reis, Fernando Terra, Andreia Santos), coordenador financeiro IA (Raphael Fritzsons, Izadora Mendes, Lucian Simões Lira da Silva, Simone Ferreira), RH T&D IA (Kauã Stecca, Natalia Pereira, Diogo Souza, Raquel Correa Medeiros), gestor de equipe ChatGPT (Eduardo Amorim, Ellen Gonçalves, Driene Araujo).
- COMMENTAIRES (4/5): Marcio Guerra (pessimisme IA / 1 tâche répétitive), Ezio Tristão (SMART FAA, copilote), Beatriz Lanza (IA planos municipais, capacitação servidores), Rafael Celini (gargalo = formação). 5e (Wendell Pedra) REFUSÉ: toast « Vous avez atteint votre limite quotidienne de commentaires » -> ARRÊT.
- ALERTE: limite quotidienne de commentaires atteinte (compte jeune). Prochain passage: max 3 commentaires, espacés.
- Mots-clés utilisés: + gerente de agência IA; coordenador financeiro IA; RH treinamento e desenvolvimento IA; gestor de equipe ChatGPT. Prochaine fois: gerente PJ banco, analista de crédito, professor universitário IA, supervisor administrativo.
- Astuce: innerText des boutons = zero-width space -> utiliser aria-label. Commenter: find() le bouton Commenter du post, clic, puis coller dans document.activeElement et cliquer le bouton « Commenter » le plus proche.

## 2026-11-06 (passage planifié, ~04h UTC — déclenché en retard, créneau du 05/11)
- POST: prompt fórmula Excel (descrever colunas sem colar dados/LGPD, idioma SOMASES x SUMIFS e separador, testar em 3 linhas, colar mensagem de erro), SANS lien. Publié (toast « Le post a bien été publié »).
- Entrant: aucun commentaire, aucun message (seul LinkedIn Team). Post ata 02/11: 140 impressions; profil vu 314 fois cette semaine.
- INVITATIONS (15, sans note, aucun avertissement; vérifié dans « Envoyées »): gerente PJ banco IA (Wellington A., Welton Ronald S. Jr, Enrico C.), analista de crédito IA (Silas Alves, Raphaela Paturalski, Daniel Moreti, Lucas Fugimura), professor universitário administração IA (Ailton Santos, Nanachara Sperb, Patrícia Sena, Bruno Aguilar da Cunha), supervisor administrativo ChatGPT (Giovanna Ciancio, Huber Mendes, Leticia Donici), assistente de gerência banco IA (Alicia Barbosa).
- COMMENTAIRES: 1/5 — Felipe Barroso (IAGen + portfolio: « quais competências isso comprova e qual evidência falta? »). 2e (Diego Mendonca) REFUSÉ: « limite quotidienne de commentaires » -> ARRÊT.
- ALERTE: limite de commentaires atteinte dès le 2e commentaire (fenêtre glissante probable). Prochain passage: max 2 commentaires, et seulement si > 24 h depuis le dernier (06/11 ~04h UTC).
- Mots-clés utilisés: + gerente PJ banco IA; analista de crédito IA; professor universitário administração IA; supervisor administrativo ChatGPT; assistente de gerência banco IA. Prochaine fois: analista de investimentos, gerente comercial, recrutador, controller, estudante de economia.
- Astuce: la fonction JS d'invitation (aria-label « Inviter… » + bouton « Envoyer sans note » dans les shadowRoots) doit être redéfinie après chaque navigation.

## 2026-11-07 (passage planifié, ~03h UTC)
- POST: prompt pour préparer une conversation de feedback difficile (gestores), AVEC lien are-ia.com (amostra grátis) en fin de post. Vérifié dans le fil (« maintenant »).
- Entrant: aucun commentaire sur nos posts, aucun message (seul InMail sponsorisé Zenvia/CX Leaders, ignoré). Post e-mail cliente 03/11: 34 impressions; Excel 06/11: 10 impressions; ata 02/11: 141.
- INVITATIONS (15, sans note, aucun avertissement, statut « En attente » vérifié): recrutador IA (Arthur Matos, Ricardo Rodrigues, Bárbara Zimerman, Amanda Simão), analista de investimentos IA (João Paulo Leite Bezerra, Bruno Armond Freire, Maria Izabela Gomes, Rafael Lima), gerente comercial ChatGPT (Rogério Comparini Cintra, Carolina Sá, Saulo Siardo, Daniela Pereira), estudante de economia IA (Kaike Ferreira, Marcela Gamberine, Camila Oliveira).
- COMMENTAIRES: 0 — volontairement sautés: < 24 h depuis le dernier (06/11 ~04h UTC) et limite quotidienne atteinte 2 passages de suite. Prochain passage (>24 h): max 2 commentaires espacés.
- Mots-clés utilisés: + recrutador IA; analista de investimentos IA; gerente comercial ChatGPT; estudante de economia IA. Prochaine fois: controller, coordenador de RH, gerente de operações, professor de ensino técnico, analista de compliance.
- Astuce: fonction JS inviteN(n) (clic « Inviter… » + « Envoyer sans note » en shadow DOM + détection d'avertissement) à redéfinir après chaque navigation; 4 invitations par mot-clé.

## 2026-11-07 (passage planifié, ~20h30 UTC)
- POST: prompt resumo executivo de relatório longo (3 parties, origine des chiffres, [VERIFICAR], LGPD/versão corporativa), SANS lien. Toast « Le post a bien été publié ».
- Entrant: aucun commentaire sur nos posts, aucun message (seuls InMail sponsorisé CX Leaders + LinkedIn Team). Impressions: feedback 07/11 = 12, Excel 06/11 = 14, e-mail cliente 03/11 = 34. 17 vues du profil.
- INVITATIONS (15, sans note, aucun avertissement): controller IA (Gabrielle Lyra — 1 seul résultat), coordenador de RH inteligência artificial (Monique Anazário, Derek da Cruz Silva, Julia D., Arnaldo Soares), gerente de operações IA (Alex Lopes, Barbara Santiago, Bruno Alves, Bianca Villani Petrosink Aguirre), analista de compliance IA (Rafael Augusto Silva Lanaro, Bianca Dias Ferreira, Solange Schmidt, Eliel Souza), professor ensino técnico inteligência artificial (Mario Augusto Ferrari, Laís Ribeiro).
- COMMENTAIRES: 1 — Ítalo Teotônio (« Em 2027 quem não sabe IA está de fora »: dado 91 % Korn Ferry + praticar numa tarefa repetitiva + saber conferir). 2e (Maxsuel Fernando, prompt plano de estudos) REFUSÉ: « limite quotidienne de commentaires » -> ARRÊT.
- CONSTAT: la limite tombe au 2e commentaire même après > 40 h. Le compte semble plafonné à ~1 commentaire/jour -> prochain passage: 1 seul commentaire, le plus qualitatif.
- Mots-clés utilisés: + controller IA (peu de résultats); coordenador de RH inteligência artificial; gerente de operações IA; analista de compliance IA; professor ensino técnico inteligência artificial. Prochaine fois: analista financeiro IA, gerente de projetos IA, secretária executiva IA, estudante de contabilidade IA, consultor de RH ChatGPT.

## 2026-11-13 (passage planifié, ~02h UTC = 12/11 23h BRT)
- POST: « Programmé (0) » -> D2_primeiro_emprego (9 pages, titre « Primeiro emprego: 6 tarefas que a IA te ajuda a fazer ») PROGRAMMÉ ven. 13/11 08:00 (toast « Post programmé »). Légende: accroche + 6 tâches + cuidado LGPD + question + 4 hashtags, sans lien.
- MESURE (page Activité, impressions affichées): D3 5 erros (document, 11/11) = 1 ; D1 banco (document, 10/11) = aucun chiffre affiché (≈0) ; résumé exécutif (texte, 07/11) = 8 ; feedback (texte) = 16 ; Excel (texte) = 16 ; e-mail cliente = 34 ; ata = 147 ; ChatGPT 1 prompt = 37. CONSTAT: les 2 documents programmés font MOINS que les textes (0-1 vs 8-16). Hypothèse: posts programmés et/ou absence d'engagement 1re heure. À tester: publier le prochain document en direct (pas programmé) pour isoler l'effet.
- Entrant: 0 commentaire sur nos posts, 0 message (seuls LinkedIn/InMail sponsorisé). Invitations reçues: seulement une invitation à une newsletter (Fernando Terra) -> ignorée. 81 abonnés.
- INVITATIONS (15, sans note, aucun avertissement): analista financeiro IA (Raquel Perrini, Gabriel Leal, Yosaf Marques, Talita S.), gerente de projetos IA (Henrique Vidal, Paulo Henrique Rodrigues Sousa, Thamires Lacerda, Felipe José Feltrin), secretária executiva IA (Emilia Teixeira, Esmeralda L. Neves, Vânia de Oliveira, Denise Fattore), estudante de contabilidade IA (Isabel C, Renato Vinotti), consultor de RH ChatGPT (Edileide Carvalho).
- COMMENTAIRE (1): Leo Candido (Executive Top Voice, post Gemini 4 Hydrogen <7 h): méthode non-dev pour comparer 2 modèles (10 tâches réelles, 3 colonnes acertou/tempo/correção, répéter 2-3 fois). Publié, pas de toast de limite.
- Mots-clés utilisés: + analista financeiro IA; gerente de projetos IA; secretária executiva IA; estudante de contabilidade IA; consultor de RH ChatGPT. Prochaine fois: analista de marketing IA, coordenador comercial, gerente de loja, analista de dados júnior, professor de ensino médio IA.
- Astuce NOUVELLE: le paste ClipboardEvent ne marche plus dans le composer -> utiliser l'API tiptap: `el=document.querySelector('.tiptap.ProseMirror'); el.editor.commands.setContent({type:'doc',content:[{type:'paragraph',content:[texte, {type:'hardBreak'}, ...]}]}, true)` (schéma = paragraph + hardBreak seulement ; plusieurs <p> sont fusionnés). Idem pour les commentaires.
- Popup « Premium » à fermer à l'ouverture du fil (X en haut à droite).

## 2026-11-13 (passage planifié, ~23h15 UTC = 20h15 BRT)
- POST: « Programmé (3) » -> lun. 16/11, mer. 18/11, ven. 20/11 à 08:30 (créés hors de cette tâche) -> RIEN créé. D4_rh_recrutamento généré (10 p., contrôlé) et mis en file pour mar. 17/11 08:00.
- MESURE (page Activité): D2 primeiro emprego (document programmé, 13/11 08h) = 6 à +12 h ; D3 5 erros (document) = 5 ; resumo executivo (texte) = 8 ; feedback (texte) = 16 ; Excel (texte) = 16 ; ata = 147. D1 banco n'apparaît plus dans l'Activité (jamais publié ou supprimé ?). CONSTAT: documents 5-6 vs textes 8-16 -> pas d'avantage document sur ce compte.
- Entrant: 0 commentaire, 0 message ; invitation reçue = seulement newsletter Fernando Terra (ignorée). Edileide Carvalho (invitée 13/11) a consulté le profil.
- INVITATIONS (15, sans note, aucun avertissement): analista de marketing IA (Felipe Honorato, Bruna Almeida, Gabriela Dupilar), coordenador comercial IA (Silas Oliveira, Raul Medeiros, Fabio Aleixo), gerente de loja IA (Alexandre Albuquerque, Loriel Carvalho, Carlos Cavalcante), analista de dados júnior IA (Carlos Jayme, Renato Bras), professor ensino médio inteligência artificial (Rafael Ferreira, Raphael Leal, Luiz Felipe Santoro), analista de atendimento IA (Thamires Santiago).
- ⚠️ BANDEAU « Vous avez atteint votre limite de recherches mensuelles » (recherche Personnes) apparu après la 6e recherche : les résultats restent visibles en partie (profils « Utilisateur LinkedIn » masqués). Prochains passages: alternative = onglet « Réseau » > suggestions (Personnes que vous pourriez connaître) filtrées sur titres brésiliens pertinents.
- COMMENTAIRE (1): Ronie Oliveira Reyes (post Reuters/Fed sur l'impact IA sur juniors, 7 h): IA fait le 1er rascunho, le júnior confère/corrige/explique ; feedback du sênior. Publié sans toast de limite (~21 h après le précédent).
- Mots-clés utilisés: + analista de marketing IA; coordenador comercial IA; gerente de loja IA; analista de dados júnior IA; professor ensino médio IA; analista de atendimento IA.
