# LinkedIn ARE-IA — journal (profil « are-ia ia », interface en français)

Règles: 1 post PT-BR/jour (lien are-ia.com une fois sur deux, en fin de post), 15 invitations sans note/jour max (recherche Personnes filtrée Brésil geoUrn 106057199), 5 commentaires utiles/jour. Stop au premier avertissement LinkedIn.

## Posts déjà publiés (ne pas répéter)
- 01/11: méthode des 5 étapes (contexto, pesquisa, rascunho, revisão, formato) — AVEC lien
- antérieurs: 4 partes do prompt (contexto/papel/tarefa/formato); o que nunca colar numa IA (LGPD); voz clonada 3 sinais; teste antigolpe 8 mensagens; Pix por engano/devolver; checklist plantão saúde; IA não é mágica é método; 26,5 % formés (Serasa 2026); appel afiliados 30 % Hotmart; + posts FR
- 02/11: prompt de ata de reunião (4 blocos + [A DEFINIR] + e-mail de follow-up) — SANS lien
- 03/11: prompt e-mail de cliente irritado (3 passos + [CONFIRMAR] + LGPD) — AVEC lien amostra grátis (prochain post: sans lien)

## Astuces techniques
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
