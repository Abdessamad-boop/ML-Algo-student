"""Checkpoint-tests week 1: KNN &amp; Naive Bayes."""
import numpy as np
import pandas as pd
import pytest


# ---------- Oefening 1: eigen KNN ----------
def test_oef1_knn_classifier_werkt(week01):
    KNNClassifier = week01.get("KNNClassifier")
    assert KNNClassifier is not None, "KNNClassifier is niet gedefinieerd"
    rng = np.random.RandomState(0)
    X = rng.randn(30, 2)
    y = (X[:, 0] + X[:, 1] > 0).astype(int)
    knn = KNNClassifier(k=3)
    knn.fit(X[:20], y[:20])
    preds = knn.predict(X[20:])
    assert preds is not None and len(preds) == 10
    # Met een simpel lineair separabel probleem moet eigen KNN > 0.7 halen
    assert np.mean(np.asarray(preds) == y[20:]) >= 0.7, "Eigen KNN voorspelt te slecht"


def test_oef1_knn_meerderheid_1buren(week01):
    KNNClassifier = week01.get("KNNClassifier")
    knn = KNNClassifier(k=1)
    X = np.array([[0.0], [10.0]])
    y = np.array([0, 1])
    knn.fit(X, y)
    assert list(knn.predict(np.array([[1.0], [9.0]]))) == [0, 1]


# ---------- Oefening 2: iris ----------
def test_oef2_accuracy_iris(week01):
    acc = week01.get("accuracy_iris")
    assert acc is not None, "variabele 'accuracy_iris' ontbreekt"
    assert isinstance(acc, (int, float)) or hasattr(acc, "item")
    acc = float(acc)
    assert 0.85 <= acc <= 1.0, f"accuracy_iris={acc} is te laag (verwacht >= 0.85)"


def test_oef2_predicties_iris(week01):
    y_pred = week01.get("y_pred_iris")
    assert y_pred is not None, "variabele 'y_pred_iris' ontbreekt"
    assert len(np.asarray(y_pred)) >= 25, "te weinig test-voorspellingen (test_size=0.25 van 150 = 38)"


# ---------- Theorievragen ----------
def test_theorie_normaliseren(week01):
    antw = week01.get("antwoord_normaliseren")
    assert antw is not None, "variabele 'antwoord_normaliseren' ontbreekt"
    assert str(antw).strip().upper() == "B", "Fout: normaliseren voorkomt vertekening van afstanden door schaalverschillen"


def test_theorie_k_kiezen(week01):
    antw = week01.get("antwoord_k_kiezen")
    assert antw is not None, "variabele 'antwoord_k_kiezen' ontbreekt"
    assert str(antw).strip().upper() == "C", "Fout: K kies je via cross-validatie"


# ---------- Oefening 3: Mall customers ----------
def test_oef3_mse_mall(week01):
    mse = week01.get("mse_mall")
    assert mse is not None, "variabele 'mse_mall' ontbreekt"
    assert float(mse) < 2500, f"mse_mall={mse} is te hoog (doel: < 2500)"


def test_oef3_one_hot_gebruikt(week01):
    """De features moeten 'Gender' via one-hot encoding bevatten (bv. kolomnamen met 'gender')."""
    df = week01.get("X_mall")
    if df is None:
        pytest.skip("optioneel: sla features op in 'X_mall' als extra controle")
    cols = " ".join(map(str, df.columns)).lower()
    assert "gender" in cols, "one-hot encoding van Gender lijkt te ontbreken (kolomnamen met 'gender' verwacht)"
    assert "Gender" not in map(str, df.columns), "Gender staat er nog als ruwe categorische kolom in i.p.v. one-hot"


# ---------- Oefening 4: Bayes-formule ----------
def test_oef4_bayes_function_exists(week01):
    """Controleer dat de bayes()-functie bestaat en correct rekent."""
    bayes = week01.get("bayes")
    assert bayes is not None, "functie 'bayes' is niet gedefinieerd"
    # Test met gekende waarden: P(spam|money) = 0.4*0.45 / (0.4*0.45 + 0.01*0.55) = 0.97035...
    result = bayes(0.4, 0.01, 0.45)
    assert abs(result - 0.97035) < 0.01, f"bayes(0.4, 0.01, 0.45) geeft {result}, verwacht ~0.97035"


def test_oef4_spam_given_money(week01):
    spam_given_money = week01.get("spam_given_money")
    assert spam_given_money is not None, "variabele 'spam_given_money' ontbreekt"
    assert abs(float(spam_given_money) - 0.97035) < 0.01, f"spam_given_money={spam_given_money}, verwacht ~0.97035"


def test_oef4_bayes_classifier_spam_exists(week01):
    """Controleer dat bayes_classifier_spam() bestaat."""
    bcs = week01.get("bayes_classifier_spam")
    assert bcs is not None, "functie 'bayes_classifier_spam' is niet gedefinieerd"
    given_money = [0.4, 0.00001]
    uganda = [0.1, 0.05]
    ap_hogeschool = [0.001, 0.3]
    cond = [given_money, uganda, ap_hogeschool]
    result = bcs(cond, 0.45, [1, 1, 0])
    assert result == "SPAM", f"bayes_classifier_spam(...) geeft '{result}', verwacht 'SPAM'"


def test_oef4_is_spam(week01):
    is_spam = week01.get("is_spam")
    assert is_spam is not None, "variabele 'is_spam' ontbreekt"
    assert str(is_spam).strip().upper() == "SPAM", f"is_spam={is_spam}, verwacht 'SPAM'"


# ---------- Oefening 6: NaiveBayesianClassifier ----------
def test_oef6_naive_bayesian_classifier_exists(week01):
    NaiveBayesianClassifier = week01.get("NaiveBayesianClassifier")
    assert NaiveBayesianClassifier is not None, "class 'NaiveBayesianClassifier' is niet gedefinieerd"
    inst = NaiveBayesianClassifier()
    assert hasattr(inst, "train"), "NaiveBayesianClassifier mist een 'train' methode"
    assert hasattr(inst, "classify"), "NaiveBayesianClassifier mist een 'classify' methode"
