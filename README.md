# ML\_algo\_cursus

Oefeningen en labs voor het vak **Machine Learning Algorithms (AP, 2e jaar)**.

## Bronnen

* Hands-On Machine Learning – Aurélien Géron
* Artificial Intelligence: A Modern Approach – Russell & Norvig

***

# ✅ Werken met de devcontainer (aanbevolen)

Deze repo gebruikt een **Dev Container** zodat je niets lokaal hoeft te installeren.

## Stap 1 – Open in VS Code

1. Open de folder in VS Code
2. Installeer de extensie: **Dev Containers**
3. Klik op:  
   **"Reopen in Container"**

De omgeving wordt automatisch opgebouwd.

***

## Stap 2 – Werken met notebooks

* Open een `.ipynb` bestand
* Kies de Python kernel (in de container)
* Run cellen

Je hoeft **geen Jupyter server zelf te starten**

***

## ✅ Extra packages installeren (optioneel)

De container start **minimal en snel**.  
Heb je extra libraries nodig, installeer ze on-demand:

### Deep learning

```bash
uv pip install -r requirements-dl.txt
```

### NLP

```bash
uv pip install -r requirements-nlp.txt
```

### Extra ML tools

```bash
uv pip install -r requirements-advanced.txt
```

***

## ✅ Waarom deze aanpak

* Snelle startup (geen zware installs)
* Minder fouten bij setup
* Flexibel: installeer enkel wat je nodig hebt

***

# ⚠️ Problemen oplossen

## OpenCV error (cv2)

Indien je een fout krijgt zoals:
`libGL.so.1 not found`

Voer uit in de container:

```bash
apt-get update && apt-get install -y libgl1
```

***

## Build errors (zeldzaam)

* Herbouw container:
  ```
  Rebuild Container
  ```
* Verwijder eventueel oude containers


# 🧪 Oefeningen

## Fork de repository

1. **Fork** deze repository naar je eigen GitHub-account via de **Fork**-knop rechtsboven.
2. **Clone** jouw fork naar je lokale machine.
3. Werk de oefeningen uit in de notebooks en **commit & push** je oplossingen naar jouw fork.

## Automatische feedback (via GitHub Actions)

Na elke push wordt er via **GitHub Actions** automatisch een testbestand gedraaid.  
Dit is **geen formeel examen** of officiële evaluatie, maar een **hulpmiddel** om je te begeleiden — vooral als je deelneemt aan het oefeningenmoment.

- De tests controleren of je oplossingen correct zijn.
- Je krijgt feedback in de **Actions**-tab van jouw fork op GitHub.
- Gebruik deze feedback om je code te verbeteren.

> ⚠️ **Experimentele opzet**  
> Dit systeem wordt stap voor stap uitgerold en kan nog wijzigen. Laat gerust weten als je problemen tegenkomt of suggesties hebt.
***