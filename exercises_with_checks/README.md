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

## Hoe het werkt (voor de lesgever)

Per week zijn er drie onderdelen:

| Onderdeel | Locatie | Inhoud |
|---|---|---|
| Opgave-notebook | `exercises_with_checks/weekNN/…_opgave.ipynb` | Oefeningen met vaste variabelennamen |
| Tests | `exercises_with_checks/checks/test_weekNN_*.py` | Pytest die het notebook uitvoert en asserted |
| Workflow | `.github/workflows/checkpoints.yml` | Matrix-job: één job per week |

### Nieuwe week toevoegen

1. Maak `exercises_with_checks/weekNN/<naam>_checkpoint_opgave.ipynb` aan.
   Gebruik per oefening vaste namen voor resultaatvariabelen en vermeld ze expliciet
   in de opgavetekst. Voeg 1–2 theorievragen toe (multiple choice in een variabele).
2. Maak `exercises_with_checks/checks/test_weekNN_<naam>.py`:
   - kopieer het fixture-patroon uit `conftest.py` (registreer het notebook in `NOTEBOOKS`);
   - test per oefening: bestaat de variabele? is de waarde goed genoeg?
   - test ook het *proces* waar het kan (bv. werd er gescaled, one-hot encoded, …).
3. Voeg de week toe aan de matrix in `.github/workflows/checkpoints.yml`.

### Lokaal testen (vóór je een week uitrolt)

```bash
cd exercises_with_checks
python -m pytest checks/test_week01_knn.py -v
```

Vereist: `pytest nbformat nbclient ipykernel scikit-learn pandas numpy`.

## In de les (voorgestelde flow)

- **Vooraan de les (5 min)**: toon het checkpoint-dashboard (Actions-tab in GitHub).
  Studenten die nog niet groen zijn van vorige week, werken die eerst af.
- **Tijdens het labo**: studenten maken het checkpoint-notebook; de docent helpt
  met inhoud, niet met de oplossing (dit zijn de permanente-evaluatielabos —
  zie week0: geen externe AI-tools, alleen de AP-chatbot).
- **Einde van de les / deadline**: laatste push telt. De workflow-timestamp in
  GitHub geeft de inlevering — geen aparte inzendtool nodig.
- **Herkansing**: volgens de ECTS-afspraken kan maximaal 1 checkpoint worden ingehaald;
  zet in `checkpoints.yml` per week een deadline en markeer late pushes als "inhaal".

## Ontwerpkeuzes

- De **originele les- en oefening-notebooks** blijven onaangetast; checkpoints zijn
  aparte bestanden, zodat de lesversie en oplossingsversie behouden blijven.
- De tests draaien in GitHub Actions in een schone omgeving: studenten-code wordt
  er uitgevoerd, dus de workflow vertrouwt alleen de eigen repo (geen secrets in de job).
- Faal-boodschappen in de tests zijn leergericht geformuleerd ("normaliseren
  voorkomt vertekening…") zodat het rode kruis meteen iets leert.
