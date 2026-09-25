# Checkpoints — hoe gebruik je dit in de les?

Automatische checkpoints per week: studenten vullen een opgave-notebook in en pushen het;
GitHub Actions voert het uit en controleert of het juist is. Resultaat is zichtbaar als
✅/❌ bij de commit in GitHub.

## Hoe het werkt (voor de student)

1. Open het checkpoint-notebook van de week, bv.
   `exercises_with_checks/week01/knn_checkpoint_opgave.ipynb`.
2. Vul alle cellen in. **Let op de gevraagde variabelennamen** (`accuracy_iris`,
   `mse_mall`, `antwoord_normaliseren`, …) — daarnaar wordt door de automatische
   controle gezocht. Verkeerde naam = checkpoint faalt.
3. Sla het notebook op **met alle cellen uitgevoerd** en push het naar je repo.
4. GitHub Actions draait automatisch (bij elke push die iets in
   `exercises_with_checks/` wijzigt). Na ±1–2 min zie je een groene vink (alle
   checks geslaagd) of een rood kruis (klik erop voor de details: welke oefening faalt en waarom).
5. Je mag zo vaak pushen als je wil tot alles groen is.
