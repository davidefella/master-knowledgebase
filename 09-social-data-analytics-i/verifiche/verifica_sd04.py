"""Verifica per esecuzione degli esempi del capitolo 04 (SD-04, SD-05).
Esegui: python3 verifica_sd04.py  (richiede nltk + dati, scikit-learn, numpy)
"""
import math
from collections import Counter

import numpy as np
import nltk
from nltk import word_tokenize, pos_tag
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

np.set_printoptions(precision=4, suppress=True, linewidth=120)

print("=== 1. Tokenizzazione della slide 'Let's tokenize! Isn't this easy?'")
frase = "Let's tokenize! Isn't this easy?"
print("spazi       :", frase.split())
print("word_tokenize:", word_tokenize(frase))

print("\n=== 2. PoS di 'Can you help me with the can?'")
print(pos_tag(word_tokenize("Can you help me with the can?")))
try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
    print("spaCy:", [(t.text, t.tag_) for t in nlp("Can you help me with the can?")])
except Exception as e:  # spaCy facoltativo
    print("spaCy non disponibile:", e)
print("possessivi:", pos_tag(word_tokenize("This pen is mine, not my brother's")))

print("\n=== 3. Bag-of-words sulle tre frasi delle slide")
frasi = ["Jim and Pam travelled by the bus:",
         "The train was late",
         "The flight was full. Travelling by flight is expensive"]
# conteggio a mano: minuscole, solo token alfabetici (come il token_pattern di sklearn su questo testo)
tok = [[w.lower() for w in word_tokenize(f) if w.isalpha()] for f in frasi]
per_frase = [Counter(t) for t in tok]
aggregato = sum(per_frase, Counter())
print("frequenze aggregate (a mano):", dict(sorted(aggregato.items())))
cv = CountVectorizer()
bow = cv.fit_transform(frasi).toarray()
print("vocabolario:", cv.vocabulary_)
print("feature    :", list(cv.get_feature_names_out()))
print(bow)
manuale = np.array([[c[w] for w in cv.get_feature_names_out()] for c in per_frase])
print("matrice a mano == CountVectorizer:", np.array_equal(manuale, bow))
print("somma per colonna (= tabella aggregata):", dict(zip(cv.get_feature_names_out(), bow.sum(axis=0))))
print("document frequency per colonna:", dict(zip(cv.get_feature_names_out(), (bow > 0).sum(axis=0))))
print("sparsita' (zeri / celle):", (bow == 0).sum(), "/", bow.size)

print("\n=== 4. TF-IDF a mano con la formula della slide (tf = conteggio/lunghezza, idf = ln(N/df))")
docs = ["This is the first document", "This document is the second document"]
tdocs = [d.lower().split() for d in docs]
N = len(tdocs)
vocab = sorted(set(w for d in tdocs for w in d))
df = {w: sum(w in d for d in tdocs) for w in vocab}
for i, d in enumerate(tdocs):
    c = Counter(d)
    riga = {w: round(c[w] / len(d) * math.log(N / df[w]), 4) for w in vocab if c[w]}
    tf = {w: round(c[w] / len(d), 4) for w in vocab if c[w]}
    print(f"doc{i+1} tf  :", tf)
    print(f"doc{i+1} tfidf:", riga)
print("ln(2) =", round(math.log(2), 4), " log10(2) =", round(math.log10(2), 4))
print("0.20*ln2 =", round(0.2 * math.log(2), 4), "  (1/6)*ln2 =", round(math.log(2) / 6, 4))

print("\n=== 5. Stesso esempio con TfidfVectorizer: tre configurazioni")
for kw in [dict(), dict(norm=None), dict(norm=None, smooth_idf=False)]:
    v = TfidfVectorizer(**kw)
    X = v.fit_transform(docs).toarray()
    print(kw or "default (smooth_idf=True, norm='l2')", list(v.get_feature_names_out()))
    print("  idf_:", np.round(v.idf_, 4))
    print(X)
# riproduzione esatta della formula della slide con sklearn: tf relativo * (idf_ - 1) con smooth_idf=False
cvd = CountVectorizer(); C = cvd.fit_transform(docs).toarray()
v = TfidfVectorizer(norm=None, smooth_idf=False).fit(docs)
slide = C / C.sum(axis=1, keepdims=True) * (v.idf_ - 1)
print("formula slide via sklearn:", list(cvd.get_feature_names_out()))
print(slide)

print("\n=== 6. TF-IDF della slide sulle tre frasi (TfidfVectorizer(norm=None))")
v3 = TfidfVectorizer(norm=None)
X3 = v3.fit_transform(frasi).toarray()
print(X3)
print("idf_:", dict(zip(v3.get_feature_names_out(), np.round(v3.idf_, 8))))
print("ln((1+3)/(1+1))+1 =", math.log(4 / 2) + 1, " ln(4/3)+1 =", math.log(4 / 3) + 1, " ln(4/4)+1 =", math.log(1) + 1)
print("con la normalizzazione di default (l2), riga 1:", np.round(TfidfVectorizer().fit_transform(frasi).toarray()[0], 4))

print("\n=== 7. Testo dei tre porcellini: byte contro caratteri")
raw = open("Natural_Language_Processing_Text.txt", "rb").read()
txt = open("Natural_Language_Processing_Text.txt").read()
print("byte:", len(raw), " caratteri letti da open():", len(txt), " CR nel file:", raw.count(b"\r"))

print("\n=== 8. Stemming delle forme di 'to be' e dei verbi di 'travel' (contro lemmatizzazione)")
from nltk.stem import PorterStemmer, SnowballStemmer, WordNetLemmatizer
p, s, l = PorterStemmer(), SnowballStemmer("english"), WordNetLemmatizer()
forme = ["am", "is", "are", "was", "were", "travelled", "travelling", "travels"]
print("Porter  :", [p.stem(w) for w in forme])
print("Snowball:", [s.stem(w) for w in forme])
print("Lemma(v):", [l.lemmatize(w, pos="v") for w in forme])

print("\n=== 9. Tokenizzazione della slide (word_tokenize contro RegexpTokenizer)")
from nltk.tokenize import RegexpTokenizer
example = "This is an example sentence! However, it isn't a very informative one"
print(word_tokenize(example, language="english"))
print(RegexpTokenizer(r"\w+").tokenize(example))
from nltk.corpus import stopwords
sw = stopwords.words("english")
print("stopword NLTK:", len(sw), "prime 20:", sw[:20])

print("\n=== 10. WordNet: da quale senso di 'natural' viene l'antonimo 'sharp'")
from nltk.corpus import wordnet as wn
for syn in wn.synsets("natural"):
    for lem in syn.lemmas():
        if lem.antonyms():
            print(syn.name(), "|", syn.definition(), "->", lem.antonyms()[0].name())
a, b = wn.synsets("ship", "n")[0], wn.synsets("boat", "n")[0]
lcs = a.lowest_common_hypernyms(b)[0]
print("Wu-Palmer ship/boat:", a.wup_similarity(b), " LCS:", lcs.name())
