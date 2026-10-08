# 06 - Dal discreto al continuo

> Fonte Notion: https://app.notion.com/p/3c612abc808d814bb619d13e36decdb5 — ultima modifica 2026-08-25T21:10:45.612Z

<table_of_contents color="gray"/>
Finora tutti i valori erano **elencabili**: le facce di un dado, le somme da 2 a 12, il numero di risposte esatte. Qui si passa al caso in cui i valori possibili sono infiniti e non elencabili, e la probabilità cambia forma.
<callout icon="💬" color="green_bg">
	**In parole semplici**
	Finora i risultati si potevano elencare a uno a uno: 1, 2, 3... Ma se misuri un'altezza, un tempo o una temperatura, i valori possibili sono infiniti e non li puoi elencare nemmeno volendo.
	Succede allora una cosa che all'inizio suona strana: la probabilità di ottenere **esattamente** un certo valore diventa **zero**. Non perché sia impossibile, ma perché "esattamente" non ha più senso quando i decimali non finiscono mai.
	L'unica domanda che resta sensata è: **il valore cade dentro questo intervallo?** Questo capitolo spiega perché, e cosa si usa al posto delle probabilità di prima.
</callout>
---
## Il caso discreto: i valori sono noti
Nel discreto il campione è fatto di valori separati:
$$
\text{sample} = \{a_1,\ a_2,\ a_3,\ a_4,\ \dots\}
$$
Sai in anticipo **quali** valori possono uscire, e a ciascuno puoi assegnare la sua $`p(a_i)`$.
---
## Il caso continuo: un intervallo
Ora il valore può cadere ovunque dentro un intervallo fra $`A`$ e $`B`$: una lunghezza, un tempo, una temperatura.
Proviamo a fare la stessa domanda di prima. Qual è la probabilità che la misura valga esattamente **6,28**?
<callout icon="🔍" color="blue_bg">
	Ma "6,28" cosa vuol dire davvero? Vale anche **6,280**? E **6,2801**? E **6,28000004**?
	Più decimali pretendi, meno casi restano validi, e più la probabilità scende. Continuando all'infinito, il numero a cui tende è **zero**.
</callout>
$$
P(x = \text{un valore esatto}) = 0
$$
Non è un cavillo da matematici: significa che nel continuo la funzione $`p(a)`$ del modulo precedente **non serve più**, perché varrebbe zero dappertutto. Ha senso una sola domanda: **qual è la probabilità che il valore cada in un intervallo?**
---
## La densità f(x)
Al posto di $`p(a)`$ subentra una nuova funzione, $`f(x)`$, e la definizione diventa:
$$
P(a \le x \le b) = \int_a^b f(x)\,dx
$$
L'integrale è la versione continua della somma: nel discreto si sommavano le $`p(a_i)`$ una per una, qui si "somma" $`f(x)`$ lungo tutto l'intervallo da $`a`$ a $`b`$. E l'intervallo $`(a,b)`$ può essere uno qualsiasi.
![](notion-file-block://2de3a6fe-5774-401a-a2bd-787b49cc52c9/d1b00264-d06c-403f-87fa-92daa8f32c04?space_id=98012abc-808d-816f-9733-00030a2b4817&name=densita-continua.svg)
---
## Perché si chiama densità e non probabilità
Prendiamo una fascia molto stretta attorno ad $`a`$, larga $`2\varepsilon`$ con $`\varepsilon`$ piccolo:
$$
P(a - \varepsilon \le x \le a + \varepsilon) = \int_{a-\varepsilon}^{a+\varepsilon} f(x)\,dx \;\simeq\; 2\varepsilon \cdot f(a)
$$
Se la fascia è abbastanza stretta, la curva lì sopra è quasi piatta e l'area sotto è quella di un rettangolino: **base per altezza**, cioè $`2\varepsilon`$ per $`f(a)`$.
> **Da qui si vede tutto.** La probabilità non è $`f(a)`$: è $`f(a)`$ **moltiplicata per un'ampiezza**. Da sola $`f(a)`$ è una probabilità per unità di $`x`$ — una *densità*, esattamente come la densità di un materiale è massa per unità di volume e diventa una massa solo quando la moltiplichi per un volume.
E si vede anche perché il singolo punto ha probabilità zero: facendo tendere $`\varepsilon`$ a zero, la base del rettangolino si annulla e con essa l'area.
<callout icon="⚠️" color="yellow_bg">
	Conseguenza pratica: $`f(x)`$** può tranquillamente superare 1**, cosa impossibile per una probabilità. Se l'intervallo su cui è concentrata è stretto, la densità lì dentro può essere alta quanto serve. Ciò che non può mai superare 1 è l'**area**.
</callout>
---
## Le corrispondenze
<table fit-page-width="true" header-row="true">
<tr>
<td></td>
<td>Caso discreto</td>
<td>Caso continuo</td>
</tr>
<tr>
<td>**I valori**</td>
<td>Elencabili: $`a_1, a_2, a_3 \dots`$</td>
<td>Tutti quelli di un intervallo</td>
</tr>
<tr>
<td>**La funzione**</td>
<td>$`p(a)`$ — una probabilità</td>
<td>$`f(x)`$ — una densità</td>
</tr>
<tr>
<td>**Un singolo valore**</td>
<td>$`p(a)`$, può essere diverso da zero</td>
<td>Sempre 0</td>
</tr>
<tr>
<td>**Come si sommano**</td>
<td>Somma: $`\sum`$</td>
<td>Integrale: $`\int`$</td>
</tr>
<tr>
<td>**Il totale fa 1**</td>
<td>$`\sum_i p(a_i) = 1`$</td>
<td>$`\int f(x)\,dx = 1`$</td>
</tr>
<tr>
<td>**Si legge come**</td>
<td>Altezza dei punti</td>
<td>Area sotto la curva</td>
</tr>
</table>
**In una riga:** nel discreto la probabilità è un'altezza, nel continuo è un'area.
---
## Riferimenti
- Dekking et al., *A Modern Introduction to Probability and Statistics*, cap. 5 ("Continuous random variables")
