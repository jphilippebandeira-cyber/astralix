# Audit AreiaPlay.club — 1er novembre 2026

Périmètre : code Replit « Cross Platform Connect » (replId 049ab091-0d26-44ea-8f53-9348326ca3f0), consulté **en lecture seule** (list_app_files / read_app_file uniquement ; aucun update ni publish). Site public https://areiaplay.club et son API publique, recherche de marché web.

Légende : **[FAIT]** = vérifié dans le code, sur le site ou dans une source citée. **[HYPOTHÈSE]** = estimation, recommandation ou point non confirmé.

Limite de l'audit : les 3 questions envoyées à l'agent Replit (`ask_question`, en pt-BR) sont toutes revenues avec `phase: paused` et une réponse vide. L'agent Replit est en pause, probablement faute de crédits ou parce qu'il attend une action du propriétaire. Toutes les conclusions viennent donc de la lecture directe du code et du site. `lib/api-spec/openapi.yaml` dépasse 100 Ko et n'a pas pu être lu : les routes ont été déduites de `artifacts/api-server/src/routes/`. Il n'y a pas de dossier `docs/` à la racine. La documentation trouvée se limite à `replit.md`, `export/LEIA-ME*.md|txt` et aux slides `artifacts/areiaplay-pitch`.

---

## 1. Produit : ce qui existe réellement

### 1.1 Architecture [FAIT]
- Monorepo pnpm : API Express 5 + PostgreSQL/Drizzle (`artifacts/api-server`), site React/Vite (`artifacts/areiaplay-web`), app Expo (`artifacts/areiaplay`), deck investisseurs (`artifacts/areiaplay-pitch`), contrat OpenAPI vers des hooks générés par Orval.
- Connexion via Clerk, e-mails via Resend, IA via l'intégration OpenAI de Replit (modèle `gpt-5.4` dans `routes/me.ts`).
- L'app mobile est **seulement une PWA**. La page /instalar le dit : « ainda não há download na App Store ou no Google Play ». Un export Xcode existe (`export/AreiaPlay-iOS-Xcode-2026-09-30.zip`, route `xcode-export.ts`), mais rien n'est publié dans les stores.
- Un pack de migration hors Replit est prêt (`export/LEIA-ME-MIGRACAO-2026-09-02.md`), avec notamment une piste IONOS VPS.
- Marque : demande INPI n° 944164811, classe NCL 41, déposée le 19/06/2026 **au nom de la personne physique Catia Sintinella** (CPF), avec l'e-mail jpbandeira@lighthumanhotels.com. Source : `attached_assets/Pasted-Pedido-de-Registro-de-Marca…txt`. L'opérateur indiqué en pied de page est **AREIAPLAY LTDA, CNPJ 68.827.180/0001-13**.
- Prompt d'origine (`attached_assets/Pasted--Atue-como-um-Engenheiro…txt`) : produit pensé comme « Circuito Open » premium pour les cadres de Faria Lima/Itaim. Il prévoyait une **licence annuelle obligatoire** et des **inscriptions à R$150 par PIX**.

### 1.2 Fonctionnalités : état réel

| Module | Dans le code | En production (API publique, 01/11/2026) |
|---|---|---|
| **Passaporte / licence** | `player_passports` : ID `AP-AAAA-NNNNN`, expiration +1 an **créée automatiquement et gratuitement** au premier enregistrement (`routes/me.ts`). Aucun paiement de licence n'existe. Multi-sport, photo, club déclaré, historique, titres. | **3 passeports**, tous de la famille : Jean Philippe Sintinella Bandeira, Catia Sintinella, Catarina Parra. 0 point au classement. |
| **Tournois** | Table `official_tournaments` : capacité de 4 à 64 duplas, statuts open/closed/completed. Moteur de tableaux et de points (`tournamentEngine.ts`, `tournamentPoints.ts`, nombreux tests). Inscription en dupla avec invitation du partenaire par e-mail. Admin tournois. | **1 tournoi**, « Open tennis », beach tennis, São Paulo, **sans date**, statut `open`. La page /torneios affiche « Nenhum torneio encontrado ». |
| **Inscriptions / paiements** | **Bloqués dans le code** : `TOURNAMENT_REGISTRATIONS_PAUSED = true` (`lib/tournamentRegistrationPolicy.ts`). Le checkout renvoie un **lien Mercado Pago fixe et public** (`https://mpago.la/2bAiXVN`) de **R$130 par inscription de dupla** (`TOURNAMENT_SIGNUP_AMOUNT_CENTS = 13_000`). Le commentaire du code précise que ce lien « não identifica a inscrição » : la confirmation du paiement est **manuelle (admin)**. | Fermé. Le bandeau « pausados » apparaît sur toutes les pages. |
| **Ranking** | Points sur les tournois officiels terminés uniquement (victoire +3, nul ou défaite 0). Classement par sport et par niveau. | Vide, à part 3 « Atleta Demonstração ». Le site précise qu'il n'est homologué par aucune fédération. |
| **Matchs amicaux** | Invitations (`friendly_invitations`) et résultats confirmés par l'adversaire via un token SHA-256 (`friendly_match_reports`). Ils ne comptent pas pour le classement. | Actif, mais sans notification push ni e-mail (/como-funciona). |
| **Réservation de courts** | `POST /bookings` **sans authentification ni paiement**. Le créneau est vérifié par club, date et heure, **pas par court** : un club de 10 courts n'accepte qu'une réservation par heure. Une **commission de 10 % est calculée et enregistrée, mais jamais encaissée**. E-mails de confirmation. | 2 réservations de test (juin 2026). |
| **Clubs** | Catalogue de **65 clubs** (38 à SP, 5 RJ, 3 SC, etc.), dont 15 « featured ». **63 ont `bookingEnabled = true`**. Coordonnées approximatives (centroïde de la ville). Le champ `consent` vaut false par défaut. Côté club : inscription, connexion, tableau de bord, licenciés, publication. | La page /clubes affiche « 0 locais » au rendu, alors que la meta annonce 65. Le site reconnaît que certains contacts sont « ilustrativos ». |
| **Fédérations** | Annuaire en lecture seule. | **77 entrées** (31 beach tennis, 30 vôlei de praia, 16 futevôlei). |
| **Liste d'attente LGPD** | Consentement obligatoire (formulaire et API). | `{"total":1,"players":1,"clubs":0}` |
| **Oráculo da Areia (IA)** | 1) `POST /api/openai/oraculo`, public (web et app). 2) `POST /me/performance-analysis` : coaching JSON sur les vraies métriques, **réservé aux adultes de 18 ans et plus**, limité à 4 appels par minute et par utilisateur. Les appels sont facturés en crédits Replit. | En ligne. Sans données, l'analyse reste générique. |
| **Diário adulto / carte à collectionner** | Journal d'entraînement, carte partageable par token. | Pour les adultes ayant un passeport. |
| **Júnior** | Module mineurs avec compte géré par un responsable légal et consentement (`junior.ts`, `junior-safety.ts`). | La vitrine publique n'utilise que des données de démo. |
| **Parceiros / cupons** | Seed de 12 marques avec codes de réduction (Adidas, Nike, Wilson, HEAD, Oakley, Olympikus…). | La page /parceiros précise « marcas e cupons são exemplos de demonstração ». **L'API publique `/api/partners` renvoie pourtant les 12 marques comme `active: true`.** |
| **Embaixadores** | Candidatures (professeurs, créateurs), rémunération « à combiner ». | Mis en avant sur la page d'accueil. |
| **Campagnes e-mail** | Envoi validé par un opérateur, pixel d'ouverture, désinscription LGPD, audience limitée aux clubs consentants et à la liste d'attente. | Outil interne. |

### 1.3 Pourquoi les paiements sont « pausados » [FAIT + HYPOTHÈSE]
- **[FAIT]** Un flag codé en dur bloque l'inscription, l'acceptation de l'invitation et le checkout. La slide « Financeiro » (`areiaplay-pitch/src/pages/slides/Financeiro.tsx`) donne trois raisons :
  1. le checkout reste fermé « até o anúncio » ;
  2. chaque paiement exige une **validation manuelle** par l'admin ;
  3. la **répartition automatique** entre arène, prize money et plateforme **n'existe pas**.
- **[FAIT]** Techniquement, le lien Mercado Pago est unique pour tout le monde. Il ne transmet aucun `external_reference` et aucun webhook ne remonte. Le système ne peut donc pas savoir **qui** a payé.
- **[HYPOTHÈSE]** Les raisons non techniques sont probablement : aucun tournoi daté avec une arène signée, pas de règlement ni de politique de remboursement, pas d'émission de NFS-e, et seulement 3 utilisateurs. Ouvrir les paiements maintenant n'apporterait rien.

**Ce qu'il faut pour rouvrir [HYPOTHÈSE, liste de tâches]** :
1. Un tournoi daté, en accord écrit avec Calçadão JK ou Posto 011 : prix, nombre de courts, horaires, prize money.
2. Le règlement et la page de l'événement : catégories, format, droit de rétractation de 7 jours (art. 49 du CDC pour la vente en ligne), politique d'annulation.
3. Un paiement identifié : Mercado Pago Checkout Pro avec `external_reference = signupId` et un webhook qui passe `paymentStatus` à `paid`. À défaut, une étape intermédiaire : un **lien Mercado Pago par tournoi** et un rapprochement manuel quotidien (acceptable jusqu'à environ 30 duplas).
4. L'émission de NFS-e par AREIAPLAY LTDA, vérifiée avec le comptable.
5. Passer le flag à `false` (modification de code : à faire par Jean-Philippe, hors de cet audit en lecture seule).

### 1.4 Modèle économique prévu, d'après le code et le deck [FAIT]
- Licence/passeport : **gratuit**, confirmé par le site et le code. La « licence obligatoire payante » du prompt d'origine a été abandonnée.
- Inscription aux tournois : **R$130 par dupla**, via Mercado Pago (en pause).
- Réservations : **commission de 10 %**, prévue dans le schéma mais non encaissée.
- Clubs : aucune formule d'abonnement dans le code. Le deck vend de la « visibilidade » et la possibilité de « sediar uma etapa ».
- Partenaires et marques : seulement une maquette de démonstration.
- Ambassadeurs : programme de rémunération à négocier au cas par cas.

### 1.5 Risques à corriger AVANT toute acquisition

| # | Risque | Gravité | Preuve |
|---|---|---|---|
| 1 | **`GET /api/bookings` est public et renvoie `playerName` et `playerEmail`**, sans authentification. C'est une fuite de données personnelles au sens de la LGPD. | Critique | `routes/bookings.ts` : aucun `requireAuth`. Constaté sur https://areiaplay.club/api/bookings (2 réservations, champs e-mail présents). |
| 2 | 63 clubs du catalogue acceptent des « réservations » alors qu'ils n'ont **jamais donné leur accord** (`consent` false par défaut, `source = catalog`, contacts parfois « ilustrativos »). Un joueur peut croire qu'il a réservé. Risques : publicité trompeuse au regard du CDC et usage des noms et images des clubs. | Élevée | `schema/clubs.ts`, `/api/clubs`, mention sur /clubes. |
| 3 | `/api/partners` publie 12 grandes marques avec des codes promo `active: true`, sans aucun contrat. | Élevée (marques de tiers) | `/api/partners`, alors que /parceiros affiche une mention de démo. |
| 4 | Le titulaire de la marque INPI (Catia, personne physique) n'est pas l'opérateur (AREIAPLAY LTDA). | Moyenne | Fichier INPI et pied de page du site. Prévoir un contrat de licence ou une cession de la marque à la société. |
| 5 | Module Júnior : les données de mineurs relèvent de l'art. 14 de la LGPD. | Moyenne | `junior*.ts`. Le garder en aperçu et ne faire aucun marketing auprès des mineurs. |
| 6 | Le tournoi « Open tennis » n'a pas de date et les listes s'affichent vides côté HTML, ce qui nuit au SEO et à la crédibilité. | Faible | API et pages /torneios, /jogadores, /clubes. |
| 7 | Réservation vérifiée par club et non par court. | Faible (produit) | `routes/bookings.ts`. |

---

## 2. Site public : ce qui est visible

| Page | Contenu [FAIT, WebFetch le 01/11/2026] |
|---|---|
| `/` | « Encontre atletas. Explore torneios. Acompanhe o ranking. » Bandeau sur la pause des inscriptions et paiements. Cartes Passaporte, Torneios, Atletas, Ranking. Blocs Embaixadores, Clubes, « Investidores (modelo em construção) » et PWA. **Aucun chiffre** affiché. Pied de page : CNPJ, Instagram **@areiaplayclub**, mention INPI, lieux Calçadão JK et Posto 011. |
| `/torneios` | **Vide** (« Nenhum torneio encontrado »). Mentions : inscriptions en pause, frais selon le règlement, passeport et licence requis pour les deux joueurs. |
| `/ranking` | **Vide**, 3 athlètes de démonstration. Barème +3/0/0. Pas d'homologation. |
| `/jogadores` | **Vide** au rendu. |
| `/clubes` | Meta : « 65 locais em 18 cidades ». Rendu : **0 locais**. Contacts parfois « ilustrativos ». |
| `/como-funciona` | 4 étapes. Disponible : passeport, recherche, classement, amicaux. En pause : inscriptions, invitations, paiements. Tout est gratuit. |
| `/faq` | 19 questions. Plusieurs réponses n'apparaissent pas dans le HTML (rendu JavaScript). |
| `/instalar` | PWA uniquement, pas d'app dans les stores. |
| `/parceiros` | Mention « Prévia ilustrativa ». Aucune marque affichée. |
| `/oraculo` | Oracle IA public. |

Constat : le site est **soigné et juridiquement prudent dans ses textes**, mais il est **vide de contenu réel** : 0 tournoi daté, 0 athlète classé, 1 inscrit en liste d'attente. Le principal problème n'est pas technique. Il manque **un premier événement réel**.

---

## 3. Marché : Brésil 2025-2026

### 3.1 Chiffres vérifiés [FAIT, sources]
- **Beach tennis, pratiquants** : 400 000 en 2021, puis **1,1 million en 2022** (+175 %), selon les données de la CBT. Marché estimé à **US$140 millions (environ R$738 millions)** par le CEO de Heroe's. Le Brésil a versé 65 % du prize money du circuit international en 2022. Chaque tournoi de l'Arena Nacional (SP) réunit environ 850 inscrits, dont 95 % en double. https://maquinadoesporte.com.br/beach-tennis/beach-tennis-atrai-elite-ao-pais-e-ve-aumento-de-175-no-numero-de-praticantes-em-um-ano/
- **Le Brésil est n° 1 mondial en tournois ITF de beach tennis** : 180 en 2025 (l'Italie est deuxième). L'**État de São Paulo seul en compte 45, contre 49 pour les États-Unis**. Aucune estimation fiable du nombre de pratiquants n'existe (« variam numa faixa ampla »). https://braziljournal.com/beach-tennis-um-mercado-sem-dono (07/09/2026)
- **FPT, bilan 2025** : plus de 440 événements dans l'État de SP, 270 tournois ouverts, **114 tournois de beach tennis**, partenariat de 4 ans avec Playpiso. https://www.portaltela.com/esporte/outros-esportes/2026/01/13/federacao-paulista-anuncia-parceria-estrategica-e-faz-balanco-de-2025/
- **Prix de la fédération (benchmark de prix direct)** : FPT 2025, anuité de **R$270 par an**. Inscription aux tournois G2 : **R$135 / R$195 / R$220 par athlète** selon la catégorie, R$190 à R$275 pour les athlètes non à jour de leur anuité. Inscriptions **via LetzPlay ou Tenisintegrado**, paiement par **PIX ou boleto**. https://www.tenispaulista.com.br/wp-content/uploads/2025/02/REGULAMENTO-BEACH-TENNIS-2025.pdf
  - Conséquence : les **R$130 par dupla** prévus par AreiaPlay (R$65 par athlète) coûtent **environ la moitié** d'une inscription FPT, et sans anuité.
- **Futevôlei** : plus de « 1 000 complexos » de beach sports estimés à São Paulo (estimation d'un organisateur). Le circuit Estação Open accueille environ 400 athlètes par étape (9 à 10 catégories). Étape de Praia Grande 2025 : environ 13 000 spectateurs sur 3 jours. Cours à SP : **R$250 à R$300 par mois** pour 2 séances par semaine. https://timesbrasil.com.br/esportes/crescimento-futevolei-brasil-negocios/ (20/10/2026)
- **Futevôlei 2025** : tendance qualitative uniquement. Multiplication des courts de sable dans les salles de sport et les condominiums, écoles pour enfants. https://www.itatiaia.com.br/porlucasmachado/esportes-em-alta-para-2025-padel-futevolei-hyrox-e-triathlon
- **Vôlei de praia amateur** : **aucun chiffre fiable trouvé** pour le nombre de pratiquants. Le CBV publie le circuit professionnel, pas les données amateurs.
- **Nordeste** : aucun chiffre agrégé. Exemple qualitatif : le futevôlei figure parmi les sports les plus pratiqués à Salvador (https://www.bnews.com.br/noticias/esporte/bnews-summer-futevolei-se-consolida-como-um-dos-esportes-mais-praticados-em-salvador.html, article non lu en entier).
- **Arènes sur Wellhub/TotalPass** : de nombreuses arènes de beach tennis sont partenaires (ex. https://wellhub.com/pt-br/search/partners/arena-sports-campinas-campinas/, https://www.gympass.com/negocios/arena-btg-by-sollis-itaim, https://totalpass.com/br/academias/academia-de-beach-tennis/). Ce sont des **listes publiques d'établissements**, utiles pour une prospection B2B manuelle.

### 3.2 Concurrents

| Acteur | Ce que c'est | Prix / modèle | Forces / faiblesses |
|---|---|---|---|
| **LetzPlay** (ex-Lptennis) | App de tournois, classements, réservations et gestion de clubs (plus de 40 graphiques). Plateforme d'inscription officielle de la FPT. | App gratuite pour le joueur. Revenus côté B2B (clubs, ligues, fédérations) ; tarifs non publiés. | Effet de réseau grâce aux fédérations. **Note de 2,8/5 (221 avis)** sur l'App Store BR : déconnexions, lenteurs, résultats non mis à jour. https://apps.apple.com/BR/app/id1262006308 |
| **Tenisintegrado** | Inscriptions FPT (citées dans le règlement). | Modèle fédération. | Institutionnel. |
| **Torneio Já** | « Gerenciador de torneios » de beach tennis, très présent en Santa Catarina (règlements hébergés sur painel.torneioja.com.br). | Tarif organisateur non publié. | Niche régionale. https://www.torneioja.com.br/ |
| **Playtomic** | Leader mondial de la réservation et de la gestion de clubs : plus de 6 700 clubs, plus de 4 millions d'utilisateurs, 63 pays. | SaaS Playtomic Manager + paiements intégrés. Prix sur devis. | Centré sur le padel et le tennis. **Le beach tennis n'apparaît pas sur la page Manager.** https://playtomic.com/pt/playtomic-manager |
| **Meu Ranking, Bora Pro Play, Play da Galera, Placar Playzim** | Petites apps de classement, de matchs ou de score. | Freemium. | Faible notoriété. https://apps.apple.com/us/app/meu-ranking/id1483076354, https://apps.apple.com/app/id6470311831 |
| **CBT / FPT / fédérations d'État** | Circuits officiels, anuités, classements homologués. | Anuité + inscriptions. | Légitimité. AreiaPlay ne peut pas et ne doit pas se présenter comme « officiel ». |
| **Wellhub / TotalPass** | Agrégateurs qui envoient des abonnés vers les arènes. | Rémunération des arènes par check-in. | Montre que les arènes acceptent des intermédiaires qui leur apportent du flux. |

**Ce qui fonctionne pour eux en acquisition [FAIT + HYPOTHÈSE]** :
- [FAIT] LetzPlay et Tenisintegrado gagnent par **l'obligation fédérale** : pour jouer un tournoi FPT, il faut passer par eux.
- [FAIT] Les circuits (Estação Open, Arena Nacional) acquièrent par **l'événement lui-même** : 400 à 850 inscrits par étape, du public, des sponsors.
- [HYPOTHÈSE] Les acteurs régionaux comme Torneio Já gagnent via les **organisateurs** : chaque organisateur apporte toute sa base d'athlètes.

**Conclusion** : on n'acquiert pas des athlètes sur une plateforme vide. On les acquiert **par des tournois et par des organisateurs**. Le positionnement possible pour AreiaPlay : « torneio amador simples, PIX, sem baixar app, sem anuidade, R$65 por atleta », face à des concurrents perçus comme lents ou institutionnels.

---

## 4. Recommandations : légales, sans budget publicitaire, sans visage

### 4.0 Préalables (semaine 1) [HYPOTHÈSE, actions de code à faire par Jean-Philippe]
1. Protéger `GET /api/bookings` (authentification + filtre sur l'utilisateur ou le club), puis vérifier si des données ont été exposées. Les 2 réservations sont des tests de la famille : un risque faible, mais à documenter.
2. Passer `bookingEnabled = false` pour tous les clubs sans consentement explicite. Afficher « Perfil não verificado — informações públicas » et un bouton « Sou o dono / remover meu clube ».
3. Vider ou désactiver `/api/partners` tant qu'aucun contrat n'est signé.
4. Supprimer ou dater le tournoi « Open tennis ».
5. Régulariser la marque : licence d'usage ou cession de Catia vers AREIAPLAY LTDA, à faire valider par un avocat.

### 4.1 Les 3 sources de revenus les plus rapides
1. **Les étapes propres « Circuito AreiaPlay » au Calçadão JK et au Posto 011** (revenu en 2 à 4 semaines).
   - [FAIT] Tout est déjà codé : passeport, inscription en dupla, moteur de tableaux de 4 à 64, points, page tournoi. Il manque le paiement identifié et un accord avec l'arène.
   - [HYPOTHÈSE] Exemple d'économie : 16 duplas × R$130 = **R$2 080 bruts par étape**, moins la location des courts, les balles, l'arbitrage et les prix. Monter en prix (R$160 à R$180 par dupla) reste moins cher que la FPT (R$270 à R$440 pour une dupla G2).
   - Formats rapides : torneio relâmpago de 4 heures, « Rei e Rainha da Quadra », mixte du jeudi soir.
2. **« Torneio Chave-na-Mão » pour les arènes et organisateurs (B2B)** (revenu en 1 à 3 semaines).
   - AreiaPlay héberge le tournoi de l'arène : page, inscriptions, tableaux, classement et WhatsApp.
   - [HYPOTHÈSE] Prix : **R$8 à R$12 par athlète inscrit** ou un **forfait de R$290 à R$490 par événement**. Ce modèle ne demande pas de base d'utilisateurs propre : c'est l'arène qui apporte ses joueurs.
   - Chaque tournoi crée de nouveaux passeports, donc alimente l'acquisition.
3. **Abonnement « Arena Fundadora » avec Astralix** (revenu récurrent dès le mois 1).
   - Contenu : profil vérifié et mis en avant sur AreiaPlay, 1 tournoi par mois hébergé, assistant WhatsApp Astra (réservations, inscriptions, FAQ).
   - [HYPOTHÈSE] Prix : **R$197 à R$397 par mois**, avec un tarif fondateur bloqué pendant 12 mois pour les 10 premières arènes.

À **ne pas** lancer maintenant :
- la licence payante (3 utilisateurs, et une anuité FPT déjà en place) ;
- la commission de 10 % sur les réservations (pas de flux de paiement, clubs non consentants) ;
- la vente de coupons de marques (aucun contrat).

### 4.2 Plan d'acquisition (90 jours, sans pub, sans visage)

**Clubs et arènes (B2B d'abord) :**
- **S1-S2** : signer **1 étape datée** avec Calçadão JK ou Posto 011 (relation déjà existante).
- **S1-S4** : constituer manuellement une liste de **50 arènes de SP** à partir de sources publiques (sites, Google Maps, listes Wellhub/TotalPass). Aucun scraping de profils personnels, conformément à la préférence de `replit.md`. Seulement des données d'entreprise.
- Contact B2B : un e-mail ou un DM Instagram à la page de l'entreprise, avec opt-out (intérêt légitime au sens de la LGPD). Aucun envoi massif sur WhatsApp : c'est contraire aux règles de WhatsApp Business.
- Offre : « primeiro torneio grátis no AreiaPlay ». Objectif : **5 arènes clientes à J+60**.
- **Organisateurs de tournois** : repérer les organisateurs indépendants publics (Instagram des circuits, règlements publiés). Proposer la plateforme gratuitement pour le premier tournoi, puis R$8 à R$12 par athlète.
- **Professeurs, via le programme Embaixadores déjà en ligne** : commission de R$10 à R$15 par dupla inscrite grâce au code du professeur. Il faut un suivi par code. Le professeur amène ses élèves, c'est le levier le plus efficace sur ce marché.

**Athlètes :**
- Chaque dupla inscrite invite son partenaire : la boucle d'invitation est **déjà codée** (e-mail au partenaire).
- Carte à collectionner partageable (déjà codée) : à publier en story après chaque match. Viralité organique.
- Classement publié chaque lundi (visuel) et « dupla da semana » (avec consentement des joueurs).
- SEO : faire rendre côté serveur les pages /onde-jogar/[cidade] et /torneios. Les pages existent (`OndeJogarCidade.tsx`) mais s'affichent vides.

**Instagram @areiaplayclub :**
- 1 Reel par jour, 3 stories par jour, sans visage.
- Comptes séparés de @areiacurso (ARE-IA) et de @astralix_servicos. Cela respecte la règle du PLAN_MAITRE : ne jamais mélanger les comptes.

### 4.3 Dix idées de Reels (sans visage)
1. **« Quanto custa jogar um torneio de beach tennis em SP? »** Tableau animé FPT (R$135 à R$220 par athlète + R$270 d'anuité) vs AreiaPlay (R$65 par athlète, sans anuité). Faits sourcés.
2. **« O Brasil tem mais torneios ITF que os EUA, e só SP quase empata. »** Infographie (180 / 49 / 45, source Brazil Journal).
3. **Le tableau qui se remplit** : timelapse d'écran du tableau de 16 duplas jusqu'à la finale (`tournamentEngine`).
4. **« Pergunte ao Oráculo »** : capture d'écran d'une analyse IA réelle, puis 3 conseils d'entraînement en sous-titres.
5. **POV pieds dans le sable** : caméra au sol, balle et filet, texto « 4 tipos de parceiro de dupla ». Humour.
6. **Drone ou plan fixe d'une arène au coucher du soleil (Posto 011)**, avec l'annonce de l'étape et un compte à rebours.
7. **« 3 erros que fazem você perder no saque »** : animation 2D du court, flèches, voix off IA.
8. **Mains seules** : remplir son passeport en 30 secondes sur le téléphone (enregistrement d'écran + mains).
9. **Classement de la semaine** : motion graphics des 5 premiers, en n'affichant que les noms des athlètes qui ont donné leur accord.
10. **« Arena, pare de responder WhatsApp às 23h »** : démo d'écran d'Astra qui réserve un court et inscrit une dupla. Reel B2B pour les propriétaires d'arènes.

Règles : aucune promesse de gain, aucune fausse rareté, mention « ranking interno, não homologado » sur les Reels liés au classement, et autorisation d'image des arènes et joueurs filmés.

### 4.4 Intégrations
**AreiaPlay × Astralix (assistant WhatsApp pour les arènes)** [HYPOTHÈSE, conception] :
- **Canal** : uniquement la WhatsApp Business Platform officielle (Cloud API), opt-in de l'athlète, modèles de messages approuvés.
- **Réservation de courts** : Astra collecte le sport, la date, l'heure et la durée, puis appelle `POST /api/bookings`. Avant cela, il faut **ajouter l'authentification, la gestion par court et la confirmation par le club** (aujourd'hui l'enregistrement est simplement déclaratif). Rappel automatique 2 heures avant.
- **Inscriptions** : Astra envoie le lien `/torneios/:id`, vérifie que le passeport existe, relance le partenaire qui n'a pas accepté et renvoie le lien de paiement. Une fois le webhook Mercado Pago en place, il confirme le paiement.
- **Après le match** : Astra demande le score et fait confirmer le résultat amical par l'adversaire (mécanisme token déjà codé).
- **Oráculo via WhatsApp** : « manda 'análise' », puis appel de `/me/performance-analysis` (pour les adultes uniquement).
- **Offre commerciale** : Astra sert de produit d'entrée (arène cliente) et AreiaPlay de réseau (visibilité et tournois) : c'est l'abonnement « Arena Fundadora » du point 4.1-3.

**AreiaPlay × ebook ARE-IA (Guia Definitivo de IA, are-ia.com)** :
- [FAIT] D'après PLAN_MAITRE.md, le guide coûte R$149,99 à R$249,99 en PIX, avec 0 vente constatée.
- [HYPOTHÈSE] Créer un **bonus « IA para donos de arena »** (prompts pour l'agenda, les réponses WhatsApp, les règlements de tournoi, les posts), offert aux arènes clientes Astra/AreiaPlay et vendu seul aux autres.
- Côté athlètes, garder les marques séparées : un simple lien « como usamos IA no Oráculo » vers are-ia.com, sans pousser la vente aux joueurs.
- Vérifier la raison sociale : le plan indique « AREAIPLAY LTDA » pour ARE-IA, le site « AREIAPLAY LTDA ».

### 4.5 Tâches quotidiennes pour un agent automatique [HYPOTHÈSE]
1. **07h** : santé du site et de l'API (/, /api/healthz, /api/tournaments) et vérification que `/api/bookings` n'expose plus d'e-mails.
2. **Rapport KPI** : nouveaux passeports, liste d'attente, candidatures ambassadeurs, inscriptions, paiements en attente de rapprochement (lecture admin).
3. **Rapprochement Mercado Pago** : comparer les paiements reçus aux inscriptions `checkout_open` et proposer la validation à l'admin (sans valider soi-même).
4. **Veille du calendrier public** : FPT, CBT, ITF (événements publics uniquement, sans données personnelles), pour en tirer des idées de contenu et des dates à éviter.
5. **Production d'un Reel par jour** (format 4.3) avec légende pt-BR, envoyé **en brouillon** pour validation avant publication.
6. **Pipeline B2B** : mettre à jour un CSV de 50 arènes, rédiger 5 relances personnalisées par jour (envoi par JP), noter les réponses.
7. **Préparer des réponses aux DM et commentaires** Instagram, publiées après validation humaine.
8. **Classement du lundi** : générer le visuel du top 5 à partir de l'API (athlètes consentants uniquement).
9. **LGPD** : vérifier les demandes sur /dados et les désinscriptions, et alerter si le délai approche.
10. **Veille concurrentielle hebdomadaire** : nouveaux avis négatifs sur LetzPlay et sujets de plainte, pour nourrir les angles de contenu.

L'agent ne publie, n'envoie et ne paie jamais rien sans l'accord de JP, et ne poste jamais de contenu AreiaPlay sur @astralix_servicos ou @areiacurso.

---

## 5. Résumé (15 lignes max)
1. Le produit est techniquement avancé : passeport, tournois en dupla avec tableaux de 4 à 64, classement, amicaux confirmés, réservations, 77 fédérations, Oráculo IA (gpt-5.4), mais en PWA seulement.
2. En production il est vide : 3 passeports (tous de la famille), 1 tournoi sans date, 1 inscrit en liste d'attente, 2 réservations de test.
3. La licence est gratuite. Les seuls revenus codés sont R$130 par dupla (Mercado Pago) et une commission de 10 % sur les réservations, jamais encaissée.
4. Les paiements sont « pausados » à cause d'un flag codé en dur. Le lien Mercado Pago est fixe et n'identifie pas le payeur (confirmation manuelle), il n'y a pas de répartition arène/plateforme, ni de tournoi daté.
5. Urgence LGPD : `GET /api/bookings` est public et expose les e-mails des joueurs.
6. Autres risques : 63 clubs « réservables » sans consentement, 12 grandes marques actives dans `/api/partners` sans contrat, marque INPI au nom de Catia et non de la LTDA.
7. Marché : 1,1 million de pratiquants de beach tennis (CBT, 2022), Brésil n° 1 mondial ITF (180 tournois en 2025), FPT à 114 tournois de beach tennis en 2025, plus de 1 000 complexes de beach sports estimés à SP.
8. Benchmark FPT : anuité R$270 et R$135 à R$220 par athlète. AreiaPlay à R$65 par athlète, sans anuité, se positionne comme le tournoi amateur accessible.
9. Concurrents : LetzPlay (inscriptions FPT, 2,8/5), Tenisintegrado, Torneio Já (SC), Playtomic (padel, pas de beach tennis). L'acquisition passe par les événements et les organisateurs.
10. Revenus rapides : (a) étapes propres au Calçadão JK / Posto 011, (b) « Torneio chave-na-mão » pour arènes à R$8-12 par athlète, (c) abonnement Arena Fundadora + Astra à R$197-397 par mois.
11. Acquisition : d'abord le B2B (1 étape signée, 50 arènes en prospection manuelle, ambassadeurs professeurs rémunérés par code), puis la boucle d'invitation des duplas et 1 Reel par jour sans visage.
12. Astra devient la porte d'entrée WhatsApp officielle (réservation, inscription, relance du partenaire, résultat) ; l'ebook ARE-IA fournit un bonus « IA para donos de arena ».
13. Les questions à l'agent Replit n'ont pas abouti (agent en pause) et `openapi.yaml` (plus de 100 Ko) n'a pas été lu.
