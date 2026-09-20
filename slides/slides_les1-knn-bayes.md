---
marp: true
theme: ap-theme
paginate: true
---

<!-- _class: title-slide -->

# Week 1
## Classificatie met Naive Bayes, KNN

---

## Herhalen

---

## Wat weten jullie hier nog over ?

• Classificatie
• Clustering
• Supervised (begeleid) vs unsupervised (onbegeleid)
• Underfitting, overfitting
• Train/test/validation data
• Cross validatie

---

## Naive Bayes

Een eerste classifier

---

## Conditionele kans = voorwaardelijke kans

• : de kans op A als B al is gebeurd – voorwaardelijke kans
• Definitie:
௉ሺ஺ & ஻ሻ
௉ሺ஻ሻ
• Voorbeeld:
• Kans op 2 keer zes gooien = 1/36 = P(A en B)
• Kans op 1 keer zes gooien = 1/6 = P(B)
• Dus de kans om 2 keer zes te gooien als je al eens 6 hebt gegooid =
ଵ/ଷ଺
ଵ/଺
ଵ
଺

---

## Regel van Bayes

• Regel van Bayes
• 𝑃𝐴𝐵ൌ
௉𝐵𝐴௉ሺ஺ሻ
௉ሺ஻ሻ
• In de context van Machine
Learning, is
• B : data, feiten
• A : een classificatielabel dat we willen toekennen
• Dus: we willen
𝑃label  dataሻberekenen
• : de kans op A als B al is gebeurd – voorwaardelijke kans
• De kans kan ook worden uitgewerkt als:
• Deze laatste heb je in de praktijk nodig om dingen uit te rekenen

---

## Ham of spam ?

---

## Classificatie met een Naive Bayes filter (1)

• We willen een spam filter bouwen. De filter heeft als doel om e-mails te controleren op tekst, en dan te labelen als ‘spam’ of ‘geen spam’.
• We hebben volgende gegevens:
• We weten uit vorige spam emails dat 40% van de spam emails het woord ‘moneytransfer’ bevatten
• We weten dat in echte emails slechts in 0.01% van de gevallen dat woord bevatten
• We weten ook dat circa 45% van alle emails spam is

---

## Moneytransfer -> Spam ?

•
•
•
• Bayes:
௉
௉ሺ௦ሻ
௉
௉௦ା௉
௉ሺ൓௦ሻ
• De classifier kiest het label met de grootste kans, in ons geval spam
• In Python: demo

---

## Meerdere woorden screenen

• 𝑃𝑚𝑜𝑛𝑒𝑦𝑡𝑟𝑎𝑛𝑠𝑓𝑒𝑟 𝑠𝑝𝑎𝑚ሻൌ
0.4
• 𝑃𝑚𝑜𝑛𝑒𝑦𝑡𝑟𝑎𝑛𝑠𝑓𝑒𝑟 ൓𝑠𝑝𝑎𝑚ሻൌ
0.0001
• 𝑃𝑢𝑔𝑎𝑛𝑑𝑎 𝑠𝑝𝑎𝑚ሻൌ0.1
• 𝑃𝑢𝑔𝑎𝑛𝑑𝑎 ൓𝑠𝑝𝑎𝑚ሻൌ0.05
• 𝑃ሺ𝑠𝑝𝑎𝑚ሻൌ0.45
• 𝑃𝐴𝑃 𝐻𝑜𝑔𝑒𝑠𝑐ℎ𝑜𝑜𝑙 𝑠𝑝𝑎𝑚ሻൌ
0.001
• 𝑃𝐴𝑃 𝐻𝑜𝑔𝑒𝑠𝑐ℎ𝑜𝑜𝑙 ൓𝑠𝑝𝑎𝑚ሻൌ
0.3
• Wat is de kans op spam als de email niet ‘moneytransfer’, maar wel ‘uganda’ en ‘AP
Hogeschool’ bevat ?

---

## Meerdere datapunten

• 𝑃𝑠𝑝𝑎𝑚  ൓𝑚𝑜 & 𝑢𝑔 & 𝑎𝑝ሻൌ
௉൓௠௢ & ௨௚ & ௔௣  ௦௣௔௠ሻ௉ሺ௦௣௔௠ሻ
⋯
• ൌ ௉൓𝑚𝑜𝑠𝑝𝑎𝑚௉𝑢𝑔𝑠𝑝𝑎𝑚௉𝑎𝑝𝑠𝑝𝑎𝑚௉ሺ௦௣௔௠ሻ
⋯
• Ik kan nu ook kijken naar geen spam:
• ௉൓𝑚𝑜൓𝑠𝑝𝑎𝑚௉𝑢𝑔൓𝑠𝑝𝑎𝑚௉𝑎𝑝൓𝑠𝑝𝑎𝑚௉ሺ൓௦௣௔௠ሻ
⋯
• Uiteindelijk kies ik het label met de grootste teller: code demo
Dit hoef ik niet uit te rekenen

![](images/Slides_ML_Algorithms_les1_p11_img001.png)

![](images/Slides_ML_Algorithms_les1_p11_img002.png)

Dit is ‘naief’ !

---

## Naive Bayes Classifier

• Waarom ‘naief’ ?
• De kansen van woorden samen en woorden apart zijn niet onafhankelijk, eigenlijk beïnvloeden ze elkaar
• In de praktijk werkt deze classifier vrij goed, dus we ‘negeren’ dit
• Volgende stap: het trainen van de data flexibeler maken: de essentie van Machine
Learning!
• Dit gaan we doen in het Labo

---

## K-nearest neighbours

- KNN

---

## Wat bepaalt de prijs van een huis ?

---

## Wat bepaalt de prijs van een huis ?

?

---

## Wat bepaalt de prijs van een huis ?

Locatie, locatie en nog eens locatie 350k 320k 370k 315kc
? 340k

---

## Wat bepaalt de prijs van een huis ?

Locatie, locatie en nog eens locatie 350k 320k 370k 315k 339k

![](images/Slides_ML_Algorithms_les1_p17_img001.jpeg)

![](images/Slides_ML_Algorithms_les1_p17_img002.jpeg)

340k

---

## KNN

• Basisidee:
• Gelijkaardige dingen zijn ‘dicht bij elkaar’
• Het algoritme:
• Kies K, het aantal ‘buren’ om rekening mee te houden
• Voor een nieuw punt:
• Bereken de K dichtste datapunten bij het nieuwe punt
• Het meest voorkomende label van de K datapunten, is het voorspelde label voor een nieuw punt

---

## KNN

• Supervised learning algoritme
• Kan zowel binary als multiclass classifier zijn
• Werkt enkel als er een notie van ‘afstand’ is tussen datapunten
• Ofwel enkel numerieke data
• Let op normaliseren !!
• Ofwel zelf een metriek gedefinieerd voor categorische data: een functie die voor elke 2 items van een lijst een afstand teruggeeft. Een metriek voor een kolom met steden zou bijvoorbeeld de afstand in vogelvlucht tussen die steden kunnen zijn
• Je moet op voorhand weten wat het aantal k is. Hier gaan we dieper op in tijdens het labo.
• Training kost nauwelijks tijd, maar classificatie is traag (omdat veel afstanden moeten worden berekend)

---

## KNN visueel, voor data met 2 kolommen

![](images/Slides_ML_Algorithms_les1_p20_img001.jpeg)

• In het voorbeeld hier links is k = 5
• Het algoritme vindt 4 rood en 1 groen label
• het voorspelde label is rood voor het nieuwe datapunt

---

## Implementatie met python en sklearn

• Optie 1: zelf implementeren -> labo
• Optie 2: scikit-learn library gebruiken (sklearn)
