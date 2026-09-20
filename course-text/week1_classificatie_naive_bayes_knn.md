# Week 1 — Classificatie deel 1: Naive Bayes en KNN

## Herhaling ML-basisbegrippen

- **Classificatie** vs **clustering**; **supervised** (begeleid) vs **unsupervised** (onbegeleid).
- **Underfitting / overfitting**.
- **Train/test/validation data**, **cross-validatie**.

## Naive Bayes

### Conditionele (voorwaardelijke) kans

- $P(A|B)$: de kans op A als B al is gebeurd.
- Definitie: $P(A|B) = \dfrac{P(A \& B)}{P(B)}$
- Voorbeeld: kans op twee keer zes gooien = $1/36 = P(A\&B)$; kans op één keer zes = $1/6 = P(B)$; dus $P(A|B) = \frac{1/36}{1/6} = \frac{1}{6}$.

### Regel van Bayes

$$P(A|B) = \frac{P(B|A)\,P(A)}{P(B)}$$

- In ML-context: B = data/feiten, A = het classificatielabel dat we willen toekennen. We willen dus $P(\text{label} \mid \text{data})$ berekenen.

### Spamfilter voorbeeld

Gegeven: $P(\text{moneytransfer} \mid \text{spam}) = 0.4$, $P(\text{moneytransfer} \mid \neg\text{spam}) = 0.0001$, $P(\text{spam}) = 0.45$.

$$P(\text{spam} \mid \text{mt}) = \frac{P(\text{mt} \mid \text{spam})\,P(\text{spam})}{P(\text{mt}\mid\text{spam})P(\text{spam}) + P(\text{mt}\mid\neg\text{spam})P(\neg\text{spam})}$$

De classifier kiest het label met de grootste kans (hier: spam).

### Meerdere woorden screenen

Met meerdere tokens ($mo$=moneytransfer, $ug$=uganda, $ap$=AP Hogeschool):

$$P(\neg mo \& ug \& ap \mid \text{spam}) = P(\neg mo \mid \text{spam})\,P(ug \mid \text{spam})\,P(ap \mid \text{spam})\cdots$$

- Idem voor $\neg$spam; kies uiteindelijk het label met de grootste teller (noemer hoeft niet uitgerekend te worden).

### Waarom "naief"?

- De kansen van woorden samen en apart zijn niet onafhankelijk — ze beïnvloeden elkaar in werkelijkheid.
- In de praktijk werkt de classifier vrij goed, dus we negeren dit.

### Laplace-smoothing (uit notebook)

Als $P(x_i \mid y=k) = 0$ voor een label, wordt het hele product 0. Oplossing: tel een klein getal $\delta$ op:

$$P(x_i \mid y=k) = \frac{\delta + \#(x_i, y=k)}{\sum_j (\delta + \#(x_j, y=k))}$$

$\delta$ wordt bepaald in functie van de documentgrootte en kan met cross-validatie worden geschat.

### Implementatie (sklearn)

```python
from sklearn.naive_bayes import BernoulliNB
clf = BernoulliNB()
clf.fit(X, Y)
clf.predict(X[2:3])
```

Let op de `.fit`/`.predict`-structuur — dit komt overal terug.

## K-Nearest Neighbours (KNN)

### Basisidee

- Gelijkaardige dingen zijn "dicht bij elkaar".
- Algoritme:
  1. Kies K (aantal buren).
  2. Voor een nieuw punt: bereken de K dichtste datapunten.
  3. Het meest voorkomende label van die K punten is de voorspelling.

### Eigenschappen en aandachtspunten

- Supervised; zowel binary als multiclass.
- Werkt enkel als er een notie van "afstand" is:
  - enkel numerieke data → **normaliseren is verplicht!**
  - of zelf een metriek definiëren voor categorische data (bv. vogelvluchtafstand tussen steden).
- K moet op voorhand gekozen worden.
- Training kost nauwelijks tijd, maar classificatie is traag (veel afstanden berekenen).

- Visueel (k=5): vindt het algoritme 4 × rood en 1 × groen, dan is de voorspelling rood.

### Implementatie (sklearn)

```python
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X_train, y_train)
predictions = knn.predict(X_test)
```

## Belangrijk bij implementatie (Week 1)

- **Normaliseer** je features vóór KNN — afstanden zijn anders vertekend.
- Kies K via cross-validatie, niet "op het gevoel" - hier komen we later nog op terug.
- Gebruik `.fit`/`.predict` via scikit-learn in plaats van zelf te implementeren, tenzij de oefening het vraagt.
- Check dat categorische features een bruikbare metriek hebben of one-hot encoded worden. Op One-Hot encoding komen we later nog terug.

## Kernpunten

- Naive Bayes: Bayes' regel + aanname van onafhankelijke features (Laplace-smoothing tegen nulkansen).
- KNN: lazy learner — geen training, trage predictie, afstandsgebaseerd.
- Beide zijn supervised classifiers; beide vereisen goede datavoorbereiding.