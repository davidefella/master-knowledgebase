# 12 - Variabili congiunte

> Fonte Notion: https://app.notion.com/p/3c712abc808d814d8efcd727315a12a8 — ultima modifica 2026-08-25T10:09:27.137Z

<table_of_contents color="gray"/>
Finora abbiamo guardato **una statistica alla volta**. Ma sullo stesso esperimento se ne possono calcolare più di una, e le due possono essere legate fra loro.
<callout icon="💬" color="green_bg">
	**In parole semplici**
	Lancio due dadi. Sullo **stesso** lancio posso chiedermi due cose diverse: quanto fa la somma, e qual è il numero più alto uscito.
	Ogni lancio produce quindi una **coppia** di numeri. Studiare la coppia insieme, invece che una alla volta, è quello che si chiama distribuzione **congiunta**.
</callout>
---
## Due statistiche sullo stesso evento
Un lancio di due dadi è un unico evento. Su di esso definiamo:
- $`\Sigma`$ — la **somma** dei due dadi
- $`M`$ — il **massimo** dei due dadi
Sono due funzioni diverse calcolate sullo stesso risultato. Ogni lancio genera quindi la coppia $`(\Sigma, M)`$.
**Esempio.** Esce $`(3, 5)`$: allora $`\Sigma = 8`$ e $`M = 5`$. La coppia osservata è $`(8, 5)`$.
La tavola della somma è già nel modulo 04. Questa è quella del massimo:
<table fit-page-width="true" header-row="true">
<tr>
<td>dado 1 / dado 2</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
</tr>
<tr>
<td>**1**</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
</tr>
<tr>
<td>**2**</td>
<td>2</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
</tr>
<tr>
<td>**3**</td>
<td>3</td>
<td>3</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
</tr>
<tr>
<td>**4**</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>5</td>
<td>6</td>
</tr>
<tr>
<td>**5**</td>
<td>5</td>
<td>5</td>
<td>5</td>
<td>5</td>
<td>5</td>
<td>6</td>
</tr>
<tr>
<td>**6**</td>
<td>6</td>
<td>6</td>
<td>6</td>
<td>6</td>
<td>6</td>
<td>6</td>
</tr>
</table>
> Righe e colonne sono i due dadi; la cella è il valore della statistica su quel lancio.
---
## La probabilità congiunta
La domanda diventa: qual è la probabilità che **contemporaneamente** la somma valga $`a`$ **e** il massimo valga $`b`$?
$$
p(a, b) \;=\; P(\Sigma = a,\; M = b)
$$
La virgola dentro la parentesi è una **E logica**: i due eventi devono verificarsi insieme, sullo stesso lancio.
Si conta come sempre: quanti dei 36 lanci danno quella coppia.
<table fit-page-width="true" header-row="true">
<tr>
<td>Σ / M</td>
<td>1</td>
<td>2</td>
<td>3</td>
<td>4</td>
<td>5</td>
<td>6</td>
</tr>
<tr>
<td>**2**</td>
<td>1</td>
<td>·</td>
<td>·</td>
<td>·</td>
<td>·</td>
<td>·</td>
</tr>
<tr>
<td>**3**</td>
<td>·</td>
<td>2</td>
<td>·</td>
<td>·</td>
<td>·</td>
<td>·</td>
</tr>
<tr>
<td>**4**</td>
<td>·</td>
<td>1</td>
<td>2</td>
<td>·</td>
<td>·</td>
<td>·</td>
</tr>
<tr>
<td>**5**</td>
<td>·</td>
<td>·</td>
<td>2</td>
<td>2</td>
<td>·</td>
<td>·</td>
</tr>
<tr>
<td>**6**</td>
<td>·</td>
<td>·</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>·</td>
</tr>
<tr>
<td>**7**</td>
<td>·</td>
<td>·</td>
<td>·</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td>**8**</td>
<td>·</td>
<td>·</td>
<td>·</td>
<td>1</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td>**9**</td>
<td>·</td>
<td>·</td>
<td>·</td>
<td>·</td>
<td>2</td>
<td>2</td>
</tr>
<tr>
<td>**10**</td>
<td>·</td>
<td>·</td>
<td>·</td>
<td>·</td>
<td>1</td>
<td>2</td>
</tr>
<tr>
<td>**11**</td>
<td>·</td>
<td>·</td>
<td>·</td>
<td>·</td>
<td>·</td>
<td>2</td>
</tr>
<tr>
<td>**12**</td>
<td>·</td>
<td>·</td>
<td>·</td>
<td>·</td>
<td>·</td>
<td>1</td>
</tr>
</table>
> I numeri sono **conteggi su 36**: la cella "2" vale $`2/36`$. Il punto indica una casella impossibile. Sommando tutte le celle si ottiene 36, cioè probabilità totale 1.
**Prima cella.** $`P(\Sigma = 2, M = 1) = 1/36`$: l'unico lancio con somma 2 è $`(1,1)`$, e lì il massimo è 1.
---
## Perché tante caselle sono a zero
È il punto interessante della tavola: le due statistiche **non sono libere di variare indipendentemente**. Fissato il massimo $`b`$, l'altro dado può valere da 1 a $`b`$, quindi:
$$
b + 1 \;\le\; \Sigma \;\le\; 2b
$$
Esempio: se $`M = 3`$, la somma può essere solo 4, 5 o 6. Tutte le altre combinazioni sono impossibili, e infatti nella tavola i valori si dispongono lungo una fascia diagonale.
<callout icon="⚠️" color="yellow_bg">
	**\[integrazione\] Le righe e le colonne hanno un senso.** Sommando una **riga** intera si ottiene la probabilità di quel valore della somma, indipendentemente dal massimo: la riga $`\Sigma = 7`$ dà $`2+2+2 = 6`$ su 36, esattamente il valore del modulo 04. Allo stesso modo, sommando una **colonna** si ritrova la distribuzione del massimo. La tavola congiunta contiene quindi entrambe le distribuzioni separate.
</callout>
---
## Il caso continuo
La struttura non cambia, cambia solo il linguaggio: al posto della probabilità di una coppia di valori si ha una **densità a due variabili**.
<table fit-page-width="true" header-row="true">
<tr>
<td>Caso</td>
<td>Oggetto</td>
<td>Normalizzazione</td>
</tr>
<tr>
<td>**Discreto**</td>
<td>$`p(a, b) = P(\Sigma = a, M = b)`$</td>
<td>$`\sum_a \sum_b p(a,b) = 1`$</td>
</tr>
<tr>
<td>**Continuo**</td>
<td>$`f(x, y)`$</td>
<td>$`\int\!\!\int f(x,y)\,dx\,dy = 1`$</td>
</tr>
</table>
Nel continuo $`f(x,y)`$ non è una probabilità ma una densità: la probabilità si ottiene integrando su una **regione** del piano, non su un punto. È la stessa distinzione già vista nel modulo 07, con una dimensione in più.
---
## Riferimenti
- Dekking et al., *A Modern Introduction to Probability and Statistics*, cap. 9 ("Joint distributions and independence")
