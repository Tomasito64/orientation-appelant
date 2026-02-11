# Orientation Appelant

Petite interface web statique qui remplace l’usage Excel : elle permet de choisir une direction, de saisir un nom d’appelant et de cocher la thématique (Action sociale / Logement / Handicap) pour afficher automatiquement le référent correspondant.

## Contenu
- `index.html` contient toute la logique (HTML + CSS + JavaScript) et embarque la liste des directions avec leurs tranches alphabétiques et les référents.
- Les boutons thématiques se comportent comme des cases radios et la zone résultat est mise en évidence avec un fond orange clair.

## Utilisation
1. Ouvre `index.html` en local pour tester (double-clic suffit).
2. Choisis une **direction** dans la liste déroulante, puis saisis le nom de l’appelant.
3. Clique une seule thématique pour la cocher ; les autres se désactivent automatiquement.
4. Le référent s’affiche dans la zone orange si une combinaison valide est trouvée, sinon un message d’erreur apparaît.

## Déploiement GitHub Pages (gratuit)
1. Pousse `index.html` sur la branche `main`.
2. Dans les **Settings** du dépôt, sélectionne **Pages** → `main` + dossier `root`, et sauvegarde.
3. L’URL publique devient `https://Tomasito64.github.io/orientation-appelant/`.

> GitHub Pages reste gratuit pour les dépôts publics ; tu peux aussi utiliser Netlify ou Vercel si tu préfères.

## Tests
- Vérifie que la liste déroulante contient toutes les directions.
- Entre un nom dont la première lettre correspond à la plage alphabétique attendue et choisis la thématique adéquate.
- Assure-toi que la zone résultat affiche bien le référent correspondant ou affiche un message si la combinaison n’existe pas.

## Tester en local
1. Depuis la branche `V2`, ouvre `index.html` dans ton navigateur (double-clic suffit) pour un premier test rapide.
2. Pour simuler un serveur et éviter les limitations de certains navigateurs, lance :
   ```sh
   python -m http.server 8000
   ```
   depuis `C:\Users\thoma\AccTS` puis visite `http://localhost:8000/index.html`. Arrête le serveur avec `Ctrl+C` quand tu as terminé.
3. Tant que tu restes sur `V2`, aucun changement ne touche la version GitHub Pages déployée sur `main` : tu peux modifier, tester et valider ici avant de merger.

## Avancement et nettoyage
Les scripts Python et fichiers intermédiaires (`AccTS.xlsx`, `extract*.py`, `pdf_text*.txt`, etc.) servent à vérifier la source PDF mais ne sont pas nécessaires pour la page web finale : ajoute-les à `.gitignore` ou supprime-les pour garder le dépôt léger.
