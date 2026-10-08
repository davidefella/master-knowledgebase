# 04 - Regressione lineare

> Fonte Notion: https://app.notion.com/p/33212abc808d81b0ae4dc6b8a81f59ad — ultima modifica 2026-04-21T23:03:32.142Z

<table_of_contents color="gray"/>
### Introduzione
La **regressione** è una tecnica statistica che cerca di trovare la curva che meglio approssima la relazione tra una variabile in input (X) e una in output (Y), così da poter fare previsioni su valori nuovi. La forma più semplice è la **regressione lineare**, che usa una retta. Quando la relazione non è lineare si usano curve di grado superiore — parabole, cubiche e così via — ed è ciò che si chiama **regressione polinomiale**.
Il prerequisito fondamentale è che la struttura della curva scelta rispecchi la struttura reale del fenomeno. L'andamento dei contagi nella fase iniziale di una pandemia era esponenziale: una retta non poteva catturarlo, sottostimava i valori alti e sovrastimava quelli bassi. Scegliere il modello giusto significa prima capire che tipo di andamento hanno i dati nel mondo reale.
In questo modulo trattiamo la regressione lineare — caso `deg=1` — che è il punto di partenza concettuale per tutto il resto.
> 📌 **Nota terminologica: "lineare" ha due significati**
> Nel linguaggio comune e nel corso, **regressione lineare = retta = ****`deg=1`**. È il significato operativo standard che userai in esame, nel codice e nelle conversazioni professionali.
> Esiste però una distinzione formale che si trova nei testi accademici: "lineare" può riferirsi non alla forma della curva, ma al modo in cui compaiono i parametri nella formula. In $`Y = m \cdot X^2 + b`$ la curva è una parabola, ma m e b compaiono ancora moltiplicati o sommati — mai al quadrato, mai uno dentro l'altro. Questo si chiama "lineare nei parametri" e spiega perché anche `deg=2` viene risolto con gli stessi minimi quadrati.
> In pratica: quando leggi "regressione lineare" in un contesto normale, intendi `deg=1`. Quando trovi la frase "lineare nei parametri" in un testo formale, intende che i coefficienti si trovano con metodi lineari indipendentemente dal grado della curva.
La regressione lineare cerca di descrivere la relazione tra due variabili numeriche, una in input (X) e una in output (Y), attraverso una *retta*. Dato un insieme di osservazioni, l'obiettivo è trovare la retta che meglio approssima l'andamento dei dati, così da poter fare previsioni su nuovi valori di X.
La regressione lineare è storicamente il primo e più semplice esempio di **modello predittivo supervisionato**: riceve in input dati storici già etichettati (coppie X, Y note) e impara una relazione che poi applica a dati nuovi. Questa struttura, imparare dai dati passati, predire quelli futuri, è la stessa di tutti i modelli ML, dai più semplici ai più complessi.
Concetti fondamentali che troveremo spesso nel corso: 
- **Parametri del modello** — in regressione lineare sono solo due: $`m`$ e $`b`$. In una rete neurale sono milioni. Il concetto è lo stesso: valori numerici che il modello "aggiusta" durante il training.
- **Funzione di perdita (loss function)** — la "differenza tra valori reali e predetti" che minimizziamo con i minimi quadrati è la prima loss function. In ML si chiama MSE (Mean Squared Error). Ogni modello ha la sua, ma l'idea è sempre: definisci una misura dell'errore, minimizzala.
- **Training e ottimizzazione** — trovare $`m`$ e $`b`$ ottimali *è* il training. Qui si risolve con una formula diretta; in modelli più complessi si usa gradient descent, ma il principio è identico.
- **Valutazione su dati nuovi** — il train/test split nel codice scikit-learn non è un dettaglio tecnico: è il principio cardine del ML. Non basta che il modello funzioni sui dati con cui ha imparato, deve generalizzare a dati mai visti.
- **Feature e target** — X si chiama *feature* (variabile in input), Y si chiama *target* (variabile da predire). Questa nomenclatura attraversa tutto il ML.
Supponi di avere i dati di 100 appartamenti: per ciascuno sai quanti metri quadri ha e a quanto è stato venduto. Se li metti su un grafico (asse X = mq, asse Y = prezzo), vedi che i punti formano più o meno una nuvola allungata in diagonale: più è grande, più costa.
La regressione lineare traccia la retta che "passa nel mezzo" di quella nuvola nel modo più preciso possibile. Una volta trovata quella retta, puoi usarla per rispondere a domande come: *"quanto costerà un appartamento di 95 mq che non ho mai visto?"* — lo leggi direttamente dalla retta." Lineare" significa proprio che il modello assume che la relazione tra X e Y sia descrivibile da una retta — non da una curva o da una forma più complessa.
### **Dove si colloca rispetto agli altri modelli?**
La regressione lineare predice un **numero continuo** (prezzo, temperatura, PIL) a partire da uno o più valori numerici in input. Questo tipo di problema si chiama **regressione**. Esistono però problemi completamente diversi che la regressione lineare non può affrontare:
- **Classificazione: ***"questa email è spam o no?"*, *"questo tumore è maligno o benigno?"* — l'output non è un numero continuo ma una categoria. Servono altri modelli: regressione logistica, SVM, reti neurali.
- **Riconoscimento di immagini:** mostri 1000 foto di gatti e cani etichettate, e vuoi che il modello classifichi la foto numero 1001. Qui l'input è una matrice di pixel, la relazione non è lineare, e la complessità è ordini di grandezza superiore. Servono reti neurali convoluzionali (CNN).
- **Relazioni non lineari** — se la relazione tra X e Y non è una retta (es. crescita esponenziale, andamento a U), la regressione lineare produce previsioni scadenti. Servono regressione polinomiale, alberi decisionali, o modelli più sofisticati.
### **Limiti della regressione lineare**
- ***Serve una tendenza lineare nei dati.*** La regressione produce sempre una retta, ma quella retta è utile solo se nei dati c'è una tendenza approssimativamente costante: al crescere di X, Y tende sistematicamente a salire o scendere. Il prerequisito non è che la crescita sia forte, ma che sia *presente e proporzionale*. Se i dati non hanno nessuna direzione chiara, l'R² sarà vicino a 0. Relazioni a U, a campana, o cicliche non sono adatte. Se i dati non hanno nessuna direzione chiara, per esempio il peso corporeo in funzione del mese dell'anno, la retta risultante sarà quasi piatta e l'R² vicino a 0: il modello esiste, ma non dice nulla di utile.
- ***Estrapolazione: la retta va all'infinito*.** La retta può essere proiettata su qualunque valore di X, anche molto lontano dai dati con cui è stata costruita. Questo si chiama **estrapolazione**, ed è sempre rischioso: il modello non sa nulla di crisi, saturazione o inversioni di tendenza, vede solo la pendenza storica e la prolunga. *Esempio*: una regressione sul PIL mondiale produce una retta con pendenza positiva che, proiettata in avanti, dà un PIL crescente all'infinito. Usare la retta *all'interno* dell'intervallo dei dati osservati (**interpolazione**) è invece molto più affidabile.
- ***È un punto di partenza, non di arrivo.*** Per fenomeni reali complessi la regressione lineare semplice è raramente sufficiente da sola, ma è la base concettuale di modelli più sofisticati. In contesti ben delimitati — relazione mq→prezzo in un quartiere omogeneo, consumo→costo energetico — funziona sorprendentemente bene.
La regressione lineare, come qualsiasi modello supervisionato, ha un prerequisito implicito: **ci deve essere una relazione reale tra X e Y nel mondo reale**. Il modello non "capisce" niente, impara a riconoscere pattern nei dati storici ma se il pattern non esiste, non c'è niente da imparare.
Supponi di voler predire il numero vincente al bingo raccogliendo dati per 365 giorni. Il modello troverà comunque una retta, un R² e dei coefficienti, ma saranno numeri privi di senso, perché il bingo è per definizione casuale. Non esiste nessuna variabile X che influenzi l'estrazione. Hai sprecato 365 giorni. Il termine tecnico è **correlazione**: X e Y devono essere correlati, cioè al variare di uno deve tendere a variare anche l'altro in modo sistematico. Senza correlazione reale, qualsiasi modello, lineare o no, produce solo rumore con un'interfaccia scientifica sopra.
---
### Il modello
Immagina che un tassista abbia una tariffa fissa di salita (intercetta $`b`$) e un costo per ogni chilometro percorso (pendenza $`m`$). Se sali e non ti muovi, paghi solo $`b`$. Per ogni km in più, il contatore sale di $`m`$. La retta $`Y = mX + b`$ è esattamente questo: un punto di partenza fisso più una crescita costante. L'obiettivo del modello è trovare *quel tassista preciso* — cioè i valori di $`m`$ e $`b`$ — che descriva meglio i dati osservati.
```javascript
Y = mX + b
```
Dove:
- $`Y`$ = output predetto (variabile dipendente)
- $`X`$ = feature in input (variabile indipendente)
- $`m`$ = pendenza (*slope*) — quanto Y cambia per ogni unità di X. Il termine *slope* viene dalla geometria analitica anglosassone (letteralmente "inclinazione") ed è il nome standard in statistica, ML e nelle librerie Python come NumPy e scikit-learn. In italiano si dice indifferentemente *pendenza* o *coefficiente angolare*.
- $`b`$ = intercetta — valore di Y quando X = 0
#### **Come si trovano m e b?**
Hai un insieme di punti sul piano. Potresti tracciare infinite rette che li attraversano in modo più o meno preciso. Come scegli quella "*giusta*"? Per ogni retta candidata, misura quanto sbaglia su ciascun punto (distanza verticale tra il punto reale e la retta), combina tutti questi errori in un unico numero, e scegli la retta che lo minimizza. Il metodo dei minimi quadrati fa esattamente questo — e le formule per $`m`$ e $`b`$ nella sezione seguente sono la soluzione matematica chiusa a quel problema di minimizzazione.
---
## Formule per m e b (metodo dei minimi quadrati)
$`m = \frac{n\sum(xy) - \sum x \sum y}{n\sum x^2 - (\sum x)^2}`$
$`b = \frac{\sum y - m\sum x}{n}`$
<empty-block/>
> $`\sum`$ (sigma maiuscola) significa semplicemente "fai la somma di tutti". $`\sum x`$ = "somma tutti gli x". $`\sum(xy)`$ = "per ogni coppia, moltiplica x per y, poi somma tutto". $`\sum x^2`$ = "eleva ogni x al quadrato, poi somma". L'unica trappola: $`(\sum x)^2`$ è diverso da $`\sum x^2`$ — nel primo caso sommi prima, poi elevi; nel secondo elevi prima, poi sommi. Come $`(1+2)^2 = 9`$ vs $`1^2 + 2^2 = 5`$.
> **Come si leggono:** $`\sum(xy)`$ significa "moltiplica ogni coppia x,y e somma tutto". $`\sum x^2`$ significa "eleva ogni x al quadrato e somma". $`(\sum x)^2`$ significa "prima somma tutti gli x, poi eleva al quadrato" — diverso da $`\sum x^2`$! In parole: **sono combinazioni di somme che trovano la retta che minimizza l'errore totale**.
> **Come si leggono le formule di slope e intercetta:** $`n`$ è il numero di osservazioni, $`\sum(xy)`$ è la somma dei prodotti tra x e y, $`\sum x^2`$ è la somma dei quadrati di x. L'idea è: trovare la retta che minimizza la distanza tra i punti reali e quelli predetti. La formula dell'intercetta $`b`$ segue direttamente una volta noto $`m`$.
> **Attenzione all'overflow:** la formula diretta con `int32` o `int64` può causare overflow sui prodotti \$sum x\^2\$. Convertire sempre in `float64` prima di calcolare.
---
## Esempio concreto: dataset investimenti reale
Invece di dati simulati, usiamo un dataset reale: acquisti mensili di ETF su un conto Fineco, da marzo 2024 a marzo 2026.
L'obiettivo è stimare il **capitale investito cumulativo** in funzione del tempo. Due scelte di rappresentazione:
**Perché il cumulativo e non il singolo acquisto?** I singoli acquisti variano molto mese per mese (357€ a marzo 2024, 94€ a luglio 2024) — messi su un grafico sembrano rumore senza tendenza. Il cumulativo somma tutti gli acquisti progressivamente e mostra la crescita totale nel tempo, che è quasi lineare perché ogni mese si aggiunge qualcosa.
**Perché il mese progressivo e non la data?** La regressione lineare lavora con numeri. Marzo 2024 diventa 0, aprile 2024 diventa 1, maggio 2024 diventa 2, e così via. È una trasformazione puramente tecnica per rendere le date numericamente trattabili.
X = mese progressivo (0 = marzo 2024, 24 = marzo 2026)
Y = capitale investito cumulativo in EUR
```python
import numpy as np
import pandas as pd

# Caricamento e preparazione
df = pd.read_csv('investments.csv')
df['Data'] = pd.to_datetime(df['Data'])

# Filtra solo acquisti ETF
etf = df[df['Categoria'].str.contains('ETF|XTR2')].copy()
etf['Importo_abs'] = etf['Importo'].abs()
etf = etf.sort_values('Data')
etf['Cumulativo'] = etf['Importo_abs'].cumsum()

# Converti data in mese progressivo
ref = etf['Data'].min()  # marzo 2024 = mese 0
etf['Mese'] = ((etf['Data'].dt.year - ref.year) * 12 +
               (etf['Data'].dt.month - ref.month)).astype(float)

X = etf['Mese'].values.astype(np.float64)
Y = etf['Cumulativo'].values.astype(np.float64)

# Regressione lineare (forma stabile)
x_mean, y_mean = np.mean(X), np.mean(Y)
m = np.sum((X - x_mean) * (Y - y_mean)) / np.sum((X - x_mean) ** 2)
b = y_mean - m * x_mean

print(f"Equazione: Capitale = {m:.2f} * mese + {b:.2f}")
# Equazione: Capitale = 200.20 * mese + 367.13

# Predizioni future (estrapolazione)
for mesi in [24, 36, 48]:
    print(f"Predizione a {mesi} mesi: {m * mesi + b:.0f} EUR")
# Predizione a 24 mesi: 5172 EUR
# Predizione a 36 mesi: 7574 EUR
# Predizione a 48 mesi: 9977 EUR

# R²
predicted = m * X + b
ss_res = np.sum((Y - predicted) ** 2)
ss_tot = np.sum((Y - y_mean) ** 2)
r2 = 1 - ss_res / ss_tot
print(f"R² = {r2:.4f}")
# R² = 0.9883
```
Per capire da dove vengono **m**, **b** e **R²**, usiamo 5 punti rappresentativi del dataset (mese → capitale cumulativo):
- *Mese 0* → 357€
- *Mese 3* → 990€
- *Mese 6* → 1.467€
- *Mese 12* → 2.276€
- *Mese 24* → 5.221€.
**Step 1: calcola le medie**
$`\bar{X} = (0+3+6+12+24)/5 = 9`$
$`\bar{Y} = (357+990+1467+2276+5221)/5 = 2062`$
**Step 2: calcola m (pendenza)**
L'idea è misurare se X e Y si muovono insieme. Per ogni punto $`i`$, calcola di quanto $`X_i`$ (il mese di quel punto) si discosta da $`\bar{X}`$ (la media di tutti i mesi) e di quanto $`Y_i`$ (il capitale di quel punto) si discosta da $`\bar{Y}`$ (la media di tutti i capitali), poi moltiplica i due scarti.
<table header-row="true">
<tr>
<td>$`X_{mese,i}`$</td>
<td>$`Y_{capitale,i}`$</td>
<td>$`X_{mese,i} - \bar{X}_{mese}`$</td>
<td>$`Y_{capitale,i} - \bar{Y}_{capitale}`$</td>
<td>prodotto</td>
</tr>
<tr>
<td>0</td>
<td>357</td>
<td>0 - 9 = **-9**</td>
<td>357 - 2062 = **-1.705**</td>
<td>-9 × -1.705 = **+15.345**</td>
</tr>
<tr>
<td>3</td>
<td>990</td>
<td>3 - 9 = **-6**</td>
<td>990 - 2062 = **-1.072**</td>
<td>-6 × -1.072 = **+6.432**</td>
</tr>
<tr>
<td>6</td>
<td>1.467</td>
<td>6 - 9 = **-3**</td>
<td>1467 - 2062 = **-595**</td>
<td>-3 × -595 = **+1.785**</td>
</tr>
<tr>
<td>12</td>
<td>2.276</td>
<td>12 - 9 = **+3**</td>
<td>2276 - 2062 = **+214**</td>
<td>+3 × +214 = **+642**</td>
</tr>
<tr>
<td>24</td>
<td>5.221</td>
<td>24 - 9 = **+15**</td>
<td>5221 - 2062 = **+3.159**</td>
<td>+15 × +3.159 = **+47.385**</td>
</tr>
</table>
Tutti i prodotti sono positivi: quando $`X_i`$ è sotto la media anche $`Y_i`$ è sotto (negativo × negativo = positivo), quando $`X_i`$ è sopra la media anche $`Y_i`$ è sopra (positivo × positivo = positivo). Questo conferma che $`X`$ e $`Y`$ crescono insieme.
Numeratore = 15.345 + 6.432 + 1.785 + 642 + 47.385 = **71.589**
Il denominatore è la somma degli scarti di X **elevati al quadrato**. Perché al quadrato e non semplicemente il modulo (\|scarto\|)? Due motivi:
Il modulo renderebbe tutti i valori positivi ma ha un problema matematico: non è derivabile in zero. La soluzione analitica dei minimi quadrati si basa sulla derivazione per trovare il minimo dell'errore — se usi il modulo non puoi ricavare m e b con una formula diretta, servirebbero algoritmi iterativi. Il quadrato invece è sempre derivabile e permette la soluzione in forma chiusa che vedi nel codice.
Inoltre elevando al quadrato gli scarti grandi pesano molto più di quelli piccoli, il che rende il denominatore una misura robusta della dispersione di X. Serve a rispondere a questa domanda: 71.589 è un numeratore grande o piccolo? Dipende da quanto sono distanziati i punti di X. Se i mesi fossero stati ravvicinati (0, 1, 2, 3, 4) invece che sparsi (0, 3, 6, 12, 24), il numeratore sarebbe uscito molto più piccolo anche a parità di relazione reale tra X e Y. Dividendo per la dispersione di X, stai normalizzando: m diventa una misura stabile di quanto Y cresce per ogni unità di X, indipendente da quanto sono spaziati i dati.
$`(-9)^2 + (-6)^2 + (-3)^2 + (3)^2 + (15)^2 = 81+36+9+9+225 = 360`$
$`m = 71.589 / 360 = 198.86`$ €/mese — ogni mese in più corrisponde mediamente a \~199€ di capitale in più.
**Step 3 — calcola b (intercetta)**
$`b = \bar{Y} - m \cdot \bar{X} = 2062 - 198.86 \times 9 = 272`$ € — valore stimato della retta al mese 0, vicino al primo acquisto reale (357€).
**Step 4 — calcola R²**
$`SS_{tot}`$ (tot = totale) è l'errore di partenza: quanto sbaglieresti se non avessi nessun modello e usassi sempre la media come previsione. Per ogni punto, calcoli la distanza dal valore reale alla media di Y (2.062€), la elevi al quadrato, e sommi tutto. Con i 5 punti: $`SS_{tot} = 14.435.311`$.
$`SS_{res}`$ (res = residuo, cioè "rimasto") è l'errore che rimane dopo aver usato la retta. Per ogni punto, calcoli la distanza dal valore reale al valore che la retta prevede, la elevi al quadrato, e sommi tutto. Con i 5 punti: $`SS_{res} = 199.242`$.
$`R^2 = 1 - SS_{res}/SS_{tot} = 1 - 199.242/14.435.311 = 0.986`$
SS_res è piccolissimo rispetto a SS_tot: la retta ha quasi azzerato l'errore di partenza. R² = 0.986 significa che il 98.6% dell'errore originale è stato eliminato dalla retta — ha senso per un PAC mensile quasi costante.
> 📈 **Lettura dei risultati**
> La pendenza $`m = 200.20`$ EUR/mese significa che ogni mese viene investito in media \~200€. L'intercetta $`b = 367.13`$ è il capitale stimato al mese 0 — leggermente superiore a zero perché i primi acquisti erano più alti della media.
> R² = 0.9883 è molto alto: il 98.8% della variazione del capitale cumulativo è spiegata dall'avanzare del tempo. Ha senso: un PAC mensile costante è quasi per definizione una relazione lineare.
> Le predizioni a 36 e 48 mesi (\~7.574€ e \~9.977€) sono **estrapolazione**: vanno oltre il range dei dati (mese 0→24). Assumono che il ritmo di investimento rimanga costante — il modello non sa nulla di eventuali cambiamenti futuri nel piano di accumulo.
---
## Implementazione con NumPy
```python
	import numpy as np
import matplotlib.pyplot as plt

# Dataset simulato: prezzi case in funzione dei mq
np.random.seed(42)
square_footage = np.random.randint(1000, 3000, size=100).astype(np.float64)
house_prices = square_footage * 150 + np.random.normal(0, 5000, size=100)

# Calcolo slope e intercetta (forma stabile numericamente)
x_mean = np.mean(square_footage)
y_mean = np.mean(house_prices)

m = np.sum((square_footage - x_mean) * (house_prices - y_mean)) / \
    np.sum((square_footage - x_mean) ** 2)
b = y_mean - m * x_mean

print(f"Best Fit: Price = {m:.2f} * sqft + {b:.2f}")
# Best Fit: Price = 149.50 * sqft + 978.06

# Predizione
predicted = m * square_footage + b
sqft_new = 2000
print(f"Predizione per {sqft_new} sqft: ${m * sqft_new + b:.2f}")
```
---
## np.polyfit e overfitting
`np.polyfit(X, Y, deg)` trova i coefficienti del polinomio di grado `deg` che meglio approssima i dati. Con `deg=1` è equivalente alla regressione lineare manuale, ma più stabile numericamente perché usa decomposizione QR internamente.
```python
X = np.array([0, 3, 6, 12, 24], dtype=np.float64)
Y = np.array([357, 990, 1467, 2276, 5221], dtype=np.float64)

m, b = np.polyfit(X, Y, 1)  # deg=1 = lineare
predicted_Y = np.polyval([m, b], X)
print(f"Capitale = {m:.2f} * mese + {b:.2f}")
```
**Cosa succede aumentando deg?** Con `deg=2` trovi una parabola, con `deg=3` una cubica. Gradi più alti seguono i dati di training con precisione crescente, ma portano a **overfitting**: la curva memorizza i singoli punti invece di catturare la tendenza generale, e fallisce su dati nuovi.
```python
import matplotlib.pyplot as plt

X_plot = np.linspace(0, 30, 200)  # esteso oltre il training per vedere l'estrapolazione

for deg in [1, 2, 4]:
    coeffs = np.polyfit(X, Y, deg)
    Y_fit = np.polyval(coeffs, X_plot)
    plt.plot(X_plot, Y_fit, label=f'deg={deg}')

plt.scatter(X, Y, color='black', zorder=5, label='dati reali')
plt.axvline(x=24, color='gray', linestyle='--', label='fine training data')
plt.ylim(-2000, 12000)
plt.legend()
plt.title('polyfit: deg crescente → overfitting')
plt.xlabel('Mese')
plt.ylabel('Capitale €')
plt.show()
```
> ⚠️ **Overfitting con deg alto**
> Con `deg=4` su soli 5 punti, il polinomio passa esattamente per tutti i punti (R²=1 sul training set) ma oltre il mese 24 esplode — può dare valori negativi o astronomici. Il modello ha memorizzato i dati invece di imparare la tendenza: perfetto sui dati visti, inutile su quelli nuovi.
> La regola pratica: `deg` deve essere molto inferiore al numero di punti. Con 31 punti come nel dataset completo, `deg=1` o `deg=2` sono ragionevoli; `deg=10` sarebbe già sospetto.
$`R^2`$ (coefficiente di determinazione) misura quanto bene la retta trovata segue l'andamento reale dei dati. Va da 0 a 1.
Partiamo da zero: se non hai nessun modello e devi comunque dare una previsione per ogni dato, la scelta più ragionevole è usare la **media** di Y. $`SS_{tot}`$ (sum of squares total) è la somma dei quadrati delle distanze tra ogni punto reale e quella media (misura quanto i dati sono sparsi attorno alla media, cioè quanta "incertezza" c'è di partenza)
Ora aggiungi il modello (la retta). $`SS_{res}`$ (sum of squares residuals, cioè "degli scarti rimasti") è la somma dei quadrati delle distanze tra ogni punto reale e la retta, misura quanta incertezza *rimane ancora* dopo che il modello ha fatto il suo lavoro.
$`R^2 = 1 - SS_{res}/SS_{tot}`$ confronta questi due numeri: se il modello è perfetto, $`SS_{res} = 0`$ e $`R^2 = 1`$. Se il modello non migliora nulla rispetto alla media, $`SS_{res} = SS_{tot}`$ e $`R^2 = 0`$. Un $`R^2 = 0.78`$ significa che il modello ha ridotto l'incertezza di partenza del 78% — il restante 22% è errore che la retta non riesce a catturare.
$`R^2 = 1 - \frac{SS_{res}}{SS_{tot}}`$
```python
from sklearn.metrics import r2_score

r2 = r2_score(Y, predicted_Y)
print(f"R² Score: {r2:.2f}")  # 1.00 su dataset lineare perfetto
```
---
## Riferimenti
- [NumPy — polyfit](https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html)
- [scikit-learn — LinearRegression](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)
- [scikit-learn — r2_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html)
- [Dataset assicurazioni — Kaggle](https://www.kaggle.com/code/fehimenuruysal/medical-cost-multiple-regression)
