# PIPELINE REELS SANS VISAGE, AVEC VOIX (testé le 06/11/2026, 0 intervention humaine)
Résultat du test: Reel AST « POV salão 23h » 23 s, voix PT-BR + animations + sous-titres, programmé Instagram @astralix_servicos (06/11 08h05) et TikTok nexoaiii (12h30) via Metricool (brandId 6868407). Coût ≈ 40 crédits vidIQ (solde 4 500, renouvelé le 26/11).

## Étapes (tout par connecteurs, sans Chrome)
1. SCRIPT PT-BR 20-25 s (~330 caractères): hook 0-3 s, 1 problème concret, 1 solution, CTA « Comenta MOT ». Aucun chiffre non vérifié.
2. VOIX: vidiq_voiceover_generate (voiceId XrExE9yKIg1WjnnlVkGX = Matilda, voix féminine pro qui lit bien le PT) -> poll vidiq_job_poll -> audioUrl + durée. 28 crédits/1000 caractères.
3. VISUELS: 3 à 5 clips vidiq_motion_graphics (preset shorts-9-16, fond dégradé foncé, texte gros, pill « COMENTA MOT » en haut dès 0 s, icônes check/warning). Somme des durées = durée de la voix (+/- 0,5 s).
4. MONTAGE: vidiq_compose (format vertical, scenes = vidéos motion, voiceover.audioUrl, captions style shorts-tiktok). Les URL S3 expirent en 12 h.
5. PUBLICATION: Metricool createScheduledPost (blogId 6868407; instagram REEL + tiktok; media = URL du rendu compose; la vidéo est copiée vers static.metricool.com). isAiGenerated/isAigc = true (voix de synthèse: étiquette honnête).
6. MESURE: Metricool getAnalyticsDataByMetrics (reels/posts) et getScheduledPosts.

## Limites connues
- @areiacurso n'est PAS relié à Metricool (seul @astralix_servicos + TikTok nexoaiii). Publier @areiacurso reste via Chrome (ou JP relie le compte dans Metricool > Connexions).
- Pas d'écran réel avec ce pipeline: pour les formats « preuve à l'écran », prendre de vraies captures via Chrome (astralixai.com démo-chat, ChatGPT) puis les ajouter comme scènes image dans compose (il faut une URL HTTPS publique).
- Réponse aux commentaires/DM: manuelle (Chrome) tant qu'aucun automate n'est branché.
- Le visuel du 1er test n'a pas pu être relu image par image: toujours ouvrir le rendu (vidiq_get_images ne lit pas les vidéos) ou le vérifier dans Metricool avant l'heure de publication.
