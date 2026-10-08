# 📐 00b - Matematica e Algebra per la Data Science

> Fonte Notion: https://app.notion.com/p/34612abc808d81098fead984f83a7e82 — ultima modifica 2026-04-18T08:46:51.643Z

Questo modulo raccoglie i concetti matematici e algebrici che compaiono nei moduli del corso e che spesso vengono dati per scontati. Non è un ripasso scolastico completo — è mirato ai concetti che servono davvero, spiegati con lo stesso approccio discorsivo del resto del wiki.
---
## La notazione $`\Sigma`$ (sigma)
$`\Sigma`$ (sigma maiuscola) significa semplicemente "fai la somma di tutti". È una scorciatoia per non scrivere tutti gli addendi uno per uno.
$`\sum x`$ = somma tutti i valori di x
$`\sum(xy)`$ = per ogni coppia, moltiplica x per y, poi somma tutto
$`\sum x^2`$ = eleva ogni x al quadrato, poi somma
L'unica trappola frequente: $`(\sum x)^2`$ è diverso da $`\sum x^2`$. Nel primo caso sommi prima, poi elevi al quadrato. Nel secondo elevi prima, poi sommi. Esempio concreto con x = 1, 2:
- $`(\sum x)^2 = (1+2)^2 = 9`$
- $`\sum x^2 = 1^2 + 2^2 = 5`$
---
## Media aritmetica
La media di un insieme di valori è la loro somma divisa per quanti sono. Con n valori $`x_1, x_2, ..., x_n`$:
$`\bar{x} = \frac{\sum x_i}{n}`$
Il simbolo $`\bar{x}`$ (x con la barra sopra) indica la media di x. Tornerà spesso nei calcoli di regressione e statistica.
> 🧑‍🍳 **For dummies**
> La media è il valore che "bilancia" tutti gli altri. Se hai i voti 4, 6, 8, la media è 6 — il punto in cui la somma degli scarti positivi eguaglia quella degli scarti negativi: (4-6) + (6-6) + (8-6) = -2 + 0 + 2 = 0.
---
## Scarto dalla media
Lo scarto di un valore $`x_i`$ dalla media è semplicemente $`x_i - \bar{x}`$. Misura di quanto quel punto si discosta dal valore centrale.
- Scarto positivo → il punto è sopra la media
- Scarto negativo → il punto è sotto la media
- La somma di tutti gli scarti è sempre zero: $`\sum(x_i - \bar{x}) = 0`$
Questo è il motivo per cui nei minimi quadrati si elevano al quadrato gli scarti invece di sommarli direttamente — la somma semplice si annullerebbe sempre.
---
## Perché si eleva al quadrato (e non si usa il modulo)
Quando si misura un errore o una dispersione, si potrebbero usare due approcci alternativi per rendere tutti i valori positivi:
**Il modulo** $`|x_i - \bar{x}|`$ — elimina il segno. Funziona, ma ha un problema matematico: non è derivabile in zero. La soluzione analitica dei minimi quadrati si basa sulla derivazione per trovare il minimo dell'errore — se usi il modulo non puoi ricavare i parametri con una formula diretta, servirebbero algoritmi iterativi.
**Il quadrato** $`(x_i - \bar{x})^2`$ — rende tutti i valori positivi, è sempre derivabile, e fa pesare di più gli scarti grandi. Permette la soluzione in forma chiusa che vedi nel codice.
Questo spiega il nome **minimi quadrati**: si minimizza la somma dei quadrati degli errori, non la somma degli errori assoluti.
---
## Derivata — solo l'intuizione
La derivata di una funzione in un punto misura **quanto cambia il suo valore al variare dell'input** — è la pendenza della curva in quel punto.
Perché serve nella regressione? Trovare m e b ottimali significa trovare il minimo della funzione di errore. Il minimo è dove la derivata è zero — la curva è piatta, non sale né scende. Questo è il principio su cui si basano sia i minimi quadrati (soluzione diretta) che il gradient descent (algoritmo iterativo usato nelle reti neurali).
> 💡 **For dummies**
> Immagina di essere in montagna nella nebbia e voler trovare la valle più bassa. La derivata ti dice in che direzione il terreno scende. Continui a scendere finché il terreno diventa piatto — quello è il minimo. Il gradient descent fa esattamente questo, un piccolo passo alla volta.
---
## "Lineare" — due significati distinti
Il termine "lineare" in matematica e ML ha due usi diversi che è importante non confondere.
**Lineare come forma geometrica** — una retta. Regressione lineare nel senso comune = `deg=1` = retta. È il significato operativo standard che userai nel corso, nel codice e nelle conversazioni professionali.
**Lineare nei parametri** — descrive come compaiono i coefficienti nella formula. Una formula è "lineare nei parametri" quando m e b compaiono moltiplicati per qualcosa o sommati, mai al quadrato, mai uno dentro l'altro, mai come esponenti.
Esempi:
<table header-row="true">
<tr>
<td>Formula</td>
<td>Lineare nei parametri?</td>
<td>Perché</td>
</tr>
<tr>
<td>$`Y = m \cdot X + b`$</td>
<td>✅ sì</td>
<td>m e b compaiono semplici</td>
</tr>
<tr>
<td>$`Y = m \cdot X^2 + b`$</td>
<td>✅ sì</td>
<td>X è al quadrato, non m</td>
</tr>
<tr>
<td>$`Y = m \cdot \log(X) + b`$</td>
<td>✅ sì</td>
<td>il log è su X, non su m</td>
</tr>
<tr>
<td>$`Y = X^m + b`$</td>
<td>❌ no</td>
<td>m è l'esponente</td>
</tr>
<tr>
<td>$`Y = m \cdot b \cdot X`$</td>
<td>❌ no</td>
<td>m e b si moltiplicano tra loro</td>
</tr>
<tr>
<td>$`Y = e^{m \cdot X} + b`$</td>
<td>❌ no</td>
<td>m è dentro un'esponenziale</td>
</tr>
</table>
Quando i parametri sono lineari → esiste una formula diretta → minimi quadrati.
Quando i parametri sono non lineari → servono algoritmi iterativi → gradient descent → reti neurali.
> 📌 **Regola pratica**
> Se elevi X a una costante (2, 3, 100) → lineare nei parametri, soluzione diretta.
> Se elevi X a un parametro (m, b) → non lineare, servono algoritmi iterativi.
> La distinzione "lineare nei parametri" è una precisazione teorica formale. Nel corso, "regressione lineare" significa sempre `deg=1`, retta.
---
## Varianza e scarto quadratico medio
La **varianza** misura quanto i dati sono dispersi attorno alla media. È la media dei quadrati degli scarti:
$`\sigma^2 = \frac{\sum(x_i - \bar{x})^2}{n}`$
Lo **scarto quadratico medio** (o deviazione standard) è la radice quadrata della varianza:
$`\sigma = \sqrt{\frac{\sum(x_i - \bar{x})^2}{n}}`$
Torna alla stessa unità di misura dei dati originali — più interpretabile della varianza. Un $`\sigma`$ piccolo significa dati concentrati attorno alla media, uno grande significa dati molto dispersi.
> 💡 **For dummies**
> Se le temperature di una settimana sono tutte tra 19°C e 21°C, la deviazione standard è piccola — i dati sono compatti. Se vanno da 5°C a 35°C, è grande — i dati sono sparsi. R² e SS_tot che vedi nella regressione si basano esattamente su questo concetto.
---
## Riferimenti interni
- Notazione $`\Sigma`$ → usata in [04 - Regressione lineare](04-regressione-lineare.md) nelle formule di m e b
- Derivata e minimi quadrati → usata in [04 - Regressione lineare](04-regressione-lineare.md) nella spiegazione del denominatore
- Varianza e scarto quadratico medio → usati in [02 - Statistica descrittiva](02-statistica-descrittiva.md)
