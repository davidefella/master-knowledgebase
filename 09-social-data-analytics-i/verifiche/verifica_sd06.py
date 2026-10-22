"""Verifica per esecuzione degli esempi numerici del capitolo 06 (Sentiment Analysis).

Eseguire con: NLTK_ALLOW_PROXIED_URLOPEN=1 python3 verifica_sd06.py
(servono nltk con vader_lexicon, wordnet, averaged_perceptron_tagger_eng; scikit-learn; textblob)
Le sezioni marcate "NOTA AGGIUNTA" non sono esempi della lezione ma integrazioni del capitolo.
"""
import json
import math
import re
from collections import Counter

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import (classification_report, confusion_matrix,
                             precision_recall_fscore_support, precision_score,
                             roc_auc_score, roc_curve, auc)
from sklearn.naive_bayes import MultinomialNB


def titolo(s):
    print("\n" + "=" * 70 + "\n" + s + "\n" + "=" * 70)


# ---------------------------------------------------------------------------
titolo("1. Lessico: esempio slide 32 (SD-07 @ 01:08:19)")
lessico = {"like": 2, "good": 1, "worst": -3, "best": 5, "terrible": -1.5}
frase = "I did not like the movie because of its terrible plot, but the actors are the best"
tok = re.findall(r"[a-z]+", frase.lower())
trovate = [(w, lessico[w]) for w in tok if w in lessico]
print("parole trovate:", trovate)
print("somma senza negazione:", sum(v for _, v in trovate))           # +5.5

# negation detection ingenua: una negazione nelle 3 parole precedenti inverte il segno
def score_con_negazione(tokens, lex, finestra=3):
    tot = 0
    for i, w in enumerate(tokens):
        if w in lex:
            neg = any(t in {"not", "no", "never"} for t in tokens[max(0, i - finestra):i])
            tot += -lex[w] if neg else lex[w]
    return tot

print("con negation detection:", score_con_negazione(tok, lessico))   # +1.5
lessico2 = dict(lessico, terrible=-5)
print("con negazione e terrible=-5:", score_con_negazione(tok, lessico2))  # -2

# ---------------------------------------------------------------------------
titolo("2. Syntactic-pattern (Turney): step 1 sull'esempio della slide 34")
import nltk
pat = [  # tabella 3.2 di Liu: (primo, secondo, vincolo sul terzo)
    ({"JJ"}, {"NN", "NNS"}, None),
    ({"RB", "RBR", "RBS"}, {"JJ"}, {"NN", "NNS"}),
    ({"JJ"}, {"JJ"}, {"NN", "NNS"}),
    ({"NN", "NNS"}, {"JJ"}, {"NN", "NNS"}),
    ({"RB", "RBR", "RBS"}, {"VB", "VBD", "VBN", "VBG"}, None),
]

def estrai_bigrammi(frase):
    tags = nltk.pos_tag(nltk.word_tokenize(frase))
    out = []
    for i in range(len(tags) - 1):
        (w1, t1), (w2, t2) = tags[i], tags[i + 1]
        t3 = tags[i + 2][1] if i + 2 < len(tags) else None
        for k, (a, b, vietato3) in enumerate(pat, 1):
            if t1 in a and t2 in b and (vietato3 is None or t3 not in vietato3):
                out.append((f"{w1} {w2}", f"pattern {k}"))
    return tags, out

for f in ["This piano produces beautiful sounds",
          "This is an interesting book",
          "The movie plot was unpredictable",
          "This is a very interesting book"]:
    tags, out = estrai_bigrammi(f)
    print(f, "->", tags, "->", out)

# ---------------------------------------------------------------------------
titolo("3. NOTA AGGIUNTA: PMI e average SO con conteggi di hit inventati")
N = 1_000_000          # documenti indicizzati (ipotetico)
hits = {"excellent": 20_000, "poor": 25_000}
frasi = {  # hits(frase NEAR excellent), hits(frase NEAR poor), hits(frase)
    "beautiful sounds": (300, 60, 2_000),
    "unpredictable plot": (90, 40, 800),
    "small viewfinder": (30, 70, 900),
}

def pmi(h12, h1, h2, n=N):
    return math.log2((h12 / n) / ((h1 / n) * (h2 / n)))

so_tot = []
for fr, (ne, npoor, hf) in frasi.items():
    so_pmi = pmi(ne, hf, hits["excellent"]) - pmi(npoor, hf, hits["poor"])
    so_eq3 = math.log2((ne * hits["poor"]) / (npoor * hits["excellent"]))
    so_tot.append(so_pmi)
    print(f"{fr:20s} SO via PMI = {so_pmi:+.4f}   SO via eq.(3) = {so_eq3:+.4f}")
avg = sum(so_tot) / len(so_tot)
print(f"average SO = {avg:+.4f} -> {'positive' if avg > 0 else 'negative'}")

# ---------------------------------------------------------------------------
titolo("4. NOTA AGGIUNTA: Bayes e Multinomial Naive Bayes a mano vs sklearn")
# Teorema di Bayes con numeri giocattolo
P_h, P_D_h, P_D = 0.56, 0.10, 0.07
print("P(h|D) = P(D|h)P(h)/P(D) =", round(P_D_h * P_h / P_D, 4))

train = [("it's a good car", "pos"), ("this car is great", "pos"),
         ("i like my new iphone", "pos"), ("it's a bad car", "neg"),
         ("i do not like this camera", "neg"), ("terrible plot bad actors", "neg")]
test = "a good camera but bad battery"
vec = CountVectorizer(token_pattern=r"[a-z']+")
X = vec.fit_transform([t for t, _ in train])
y = [c for _, c in train]
V = vec.get_feature_names_out()
classi = sorted(set(y))
# a mano, smoothing di Laplace alpha=1
xt = vec.transform([test]).toarray()[0]
logpost = {}
for c in classi:
    righe = [i for i, yy in enumerate(y) if yy == c]
    cnt = np.asarray(X[righe].sum(axis=0)).ravel()
    prior = len(righe) / len(y)
    lik = (cnt + 1) / (cnt.sum() + len(V))
    logpost[c] = math.log(prior) + float((xt * np.log(lik)).sum())
z = np.logaddexp.reduce(list(logpost.values()))
mano = {c: math.exp(v - z) for c, v in logpost.items()}
nb = MultinomialNB(alpha=1.0).fit(X, y)
sk = dict(zip(nb.classes_, nb.predict_proba(vec.transform([test]))[0]))
print("parole del test nel vocabolario:", [w for w, n in zip(V, xt) if n])
print("posterior a mano:", {k: round(v, 4) for k, v in mano.items()})
print("posterior sklearn:", {k: round(v, 4) for k, v in sk.items()})
print("predizione:", nb.predict(vec.transform([test]))[0])

# ---------------------------------------------------------------------------
titolo("5. Metriche a 2 classi dalla confusion matrix del notebook (SD-08 @ 00:39:44)")
TN, FP, FN, TP = 6411, 2320, 2321, 8946   # classe 1 = positiva
y_true = np.array([0] * (TN + FP) + [1] * (FN + TP))
y_pred = np.array([0] * TN + [1] * FP + [0] * FN + [1] * TP)
print(confusion_matrix(y_true, y_pred))
P_pos, R_pos = TP / (TP + FP), TP / (TP + FN)
P_neg, R_neg = TN / (TN + FN), TN / (TN + FP)
acc = (TP + TN) / (TP + TN + FP + FN)
F_pos = 2 * P_pos * R_pos / (P_pos + R_pos)
F_neg = 2 * P_neg * R_neg / (P_neg + R_neg)
P_avg, R_avg = (P_pos + P_neg) / 2, (R_pos + R_neg) / 2
F_slide = 2 * P_avg * R_avg / (P_avg + R_avg)
print(f"P_pos={P_pos:.4f} R_pos={R_pos:.4f} F_pos={F_pos:.4f}")
print(f"P_neg={P_neg:.4f} R_neg={R_neg:.4f} F_neg={F_neg:.4f}")
print(f"accuracy={acc:.4f}")
print(f"P_avg={P_avg:.4f} R_avg={R_avg:.4f} F (formula slide 47)={F_slide:.6f}  "
      f"F macro sklearn (media degli F)={(F_pos + F_neg) / 2:.6f}")
print(classification_report(y_true, y_pred, digits=4))

# ---------------------------------------------------------------------------
titolo("6. Micro vs macro precision: esempio slide 49 (SD-08 @ 00:09:11)")
manuale_macro = (0.5 + 0.1 + 0.5 + 0.5) / 4
manuale_micro = (1 + 10 + 1 + 1) / (2 + 100 + 2 + 2)
print("macro =", manuale_macro, " micro =", round(manuale_micro, 4))
# ricostruzione con etichette: i FP di ogni classe sono item di un'altra classe
yt, yp = [], []
def add(true, pred, n):
    yt.extend([true] * n); yp.extend([pred] * n)
add("A", "A", 1); add("B", "A", 1)
add("B", "B", 10); add("C", "B", 90)
add("C", "C", 1); add("D", "C", 1)
add("D", "D", 1); add("A", "D", 1)
lab = ["A", "B", "C", "D"]
p, r, f, s = precision_recall_fscore_support(yt, yp, labels=lab, zero_division=0)
print("precision per classe:", dict(zip(lab, p.round(3))))
print("sklearn macro:", precision_score(yt, yp, labels=lab, average="macro"))
print("sklearn micro:", round(precision_score(yt, yp, labels=lab, average="micro"), 4))

# ---------------------------------------------------------------------------
titolo("7. NOTA AGGIUNTA: ROC/AUC su 8 punteggi giocattolo")
yt8 = [0, 0, 1, 1, 0, 1, 1, 0]
sc8 = [0.1, 0.4, 0.35, 0.8, 0.2, 0.9, 0.6, 0.55]
fpr, tpr, thr = roc_curve(yt8, sc8)
print("FPR:", fpr.round(2), "\nTPR:", tpr.round(2), "\nsoglie:", thr)
print("AUC =", auc(fpr, tpr), "=", roc_auc_score(yt8, sc8))
coppie = [(a, b) for a, ya in zip(sc8, yt8) for b, yb in zip(sc8, yt8) if ya == 1 and yb == 0]
print("frazione di coppie (pos,neg) ordinate bene:", sum(a > b for a, b in coppie) / len(coppie))

# ---------------------------------------------------------------------------
titolo("8. Preprocessing del notebook su frasi di prova (funzioni copiate dal notebook)")
contractions = json.load(open("assets/contractions.json"))["contractions"] \
    if __import__("os").path.exists("assets/contractions.json") else {"can't": "cannot", "don't": "do not"}

def emoji(tweet):
    tweet = re.sub(r'(:\s?\)|:-\)|\(\s?:|\(-:|:\'\)|:o|:O|:0)', ' positiveemoji ', tweet)
    tweet = re.sub(r'(:\s?D|:-D|x-?D|X-?D)', ' positiveemoji ', tweet)
    tweet = re.sub(r'(<3|:\*)', ' positiveemoji ', tweet)
    tweet = re.sub(r'(;-?\)|;-?D|\(-?;|@-\))', ' positiveemoji ', tweet)
    tweet = re.sub(r'(:\s?\(|:-\(|\)\s?:|\)-:|:-/|:-\|)', ' negetiveemoji ', tweet)
    tweet = re.sub(r'(:,\(|:\'\(|:"\()', ' negetiveemoji ', tweet)
    return tweet

def process_tweet(tweet):
    tweet = tweet.lower()
    tweet = re.sub(r'@[^\s]+', '', tweet)
    tweet = re.sub(r'((www\.[^\s]+)|(https?://[^\s]+))', ' ', tweet)
    tweet = re.sub(r'\d+', " ", str(tweet))
    tweet = re.sub(r'&quot;', " ", tweet)
    tweet = emoji(tweet)
    tweet = re.sub(r'\b[a-zA-Z]\b', "", str(tweet))
    for word in tweet.split():
        if word.lower() in contractions:
            tweet = tweet.replace(word, contractions[word.lower()])
    tweet = re.sub(r'[^\w\s]', " ", str(tweet))
    tweet = re.sub(r'(.)\1+', r'\1\1', tweet)
    tweet = re.sub(r'\s+', " ", str(tweet))
    return tweet

for t in ["I don't like Pepsi :(", "I can't wait!! :D", "Sooooo coooool XD",
          "@john check http://x.co it's great :)", "I'm not happy :-("]:
    print(repr(t), "->", repr(process_tweet(t)))

# ---------------------------------------------------------------------------
titolo("9. NOTA AGGIUNTA: VADER e TextBlob sulle frasi delle slide")
from nltk.sentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
sia = SentimentIntensityAnalyzer()
for f in ["I did not like the movie because of its terrible plot, but the actors are the best",
          "What a great car! It stopped working in two days",
          "Can anyone tell me where I can find a good Nokia phone?",
          "If someone makes a reliable car, I will buy it.",
          "I bought the mattress a week ago and a valley has formed.",
          "I think it is raining now.",
          "must think about positive "]:
    tb = TextBlob(f).sentiment
    print(f"{f!r}\n   VADER {sia.polarity_scores(f)}  TextBlob polarity={tb.polarity:.3f} subjectivity={tb.subjectivity:.3f}")
