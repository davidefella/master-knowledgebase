# 07 - Cumulativa e densità nel continuo

> Fonte Notion: https://app.notion.com/p/3c712abc808d8167a4d0f77157e426d5 — ultima modifica 2026-08-25T21:10:52.179Z

<table_of_contents color="gray"/>
La funzione cumulativa nel caso continuo, e il legame fra **densità** e **cumulativa**: sono la stessa informazione, e si passa dall'una all'altra con integrale e derivata.
<callout icon="💬" color="green_bg">
	**In parole semplici**
	Nel continuo la probabilità di un valore esatto è zero, quindi l'unica cosa che si può chiedere è "quanto vale da qui a lì". Due funzioni bastano a rispondere sempre.
	La prima, $`f`$, dice **quanto è concentrata** la probabilità attorno a un punto.
	La seconda, $`F`$, dice **quanto se n'è accumulata** da sinistra fino a quel punto.
	Sono due facce della stessa cosa: da una ricavi l'altra, sempre.
</callout>
---
## La probabilità di un intervallo con la cumulativa
Per un intervallo qualsiasi $`(a, b]`$ si può ragionare per differenza: prendi tutto ciò che sta fino a $`b`$ e togli ciò che sta fino ad $`a`$.
$$
P(a < x \le b) = P(x \le b) - P(x \le a) = F(b) - F(a)
$$
> Non serve calcolare l'integrale su ogni intervallo che ti interessa: se conosci $`F`$, ogni intervallo si ottiene con **una sottrazione**. È il motivo per cui la cumulativa è così comoda.
---
## Definizione della cumulativa nel continuo
$$
F(b) \;\equiv\; P(x \le b) \;=\; \int_{-\infty}^{\,b} f(x)\,dx
$$
Si integra **da meno infinito**: si accumula tutto ciò che sta a sinistra di $`b`$. Nel discreto si sommavano le $`p(a_i)`$ una a una, qui l'integrale fa la stessa cosa su un continuo di valori.
---
## Il legame: integrale in un verso, derivata nell'altro
Se $`F`$ si ottiene integrando $`f`$, allora $`f`$ si ottiene **derivando** $`F`$:
$$
f(x) = \frac{d}{dx} F(x)
$$
<table fit-page-width="true" header-row="true">
<tr>
<td>Da</td>
<td>Operazione</td>
<td>A</td>
</tr>
<tr>
<td>$`f(x)`$ — densità</td>
<td>**Integrale**</td>
<td>$`F(x)`$ — cumulativa</td>
</tr>
<tr>
<td>$`F(x)`$ — cumulativa</td>
<td>**Derivata**</td>
<td>$`f(x)`$ — densità</td>
</tr>
</table>
<callout icon="🔁" color="blue_bg">
	**Conseguenza pratica.** Le due funzioni contengono **la stessa identica informazione**. Conoscerne una significa conoscere l'altra, quindi puoi sempre partire da quella più comoda da scrivere e ricavare l'altra quando serve. Nelle prossime distribuzioni si fa esattamente questo.
</callout>
---
## Riferimenti
- Dekking et al., *A Modern Introduction to Probability and Statistics*, cap. 5 ("Continuous random variables")
