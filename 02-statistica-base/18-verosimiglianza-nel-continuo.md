# 18 - Verosimiglianza nel continuo

> Fonte Notion: https://app.notion.com/p/3c712abc808d81048105ff2c2aaf9305 — ultima modifica 2026-08-25T14:02:54.234Z

<table_of_contents color="gray"/>
Il metodo funziona anche quando i dati sono numeri continui — altezze, tempi, temperature — ma serve una piccola furbizia.
<callout icon="💬" color="green_bg">
	**In parole semplici**
	Se misuro un'altezza e ottengo 1,7523 m, qual è la probabilità di ottenere **esattamente** quel valore? Zero: ci sono infiniti numeri reali.
	La soluzione è quella che usiamo già senza accorgercene: nessuno misura "esattamente", si misura sempre con una tolleranza. E la probabilità di cadere dentro quella tolleranza non è zero.
</callout>
---
## Il problema
Si parte come prima: dai dati $`x_1, x_2, \dots, x_n`$ si vorrebbe scrivere
$$
L = P(X_1 = x_1,\; X_2 = x_2,\; \dots,\; X_n = x_n)
$$
Ma nel continuo $`P(X = x)`$ **non è definita**: come visto nel modulo 07, la probabilità di un singolo punto vale zero. La formula darebbe $`0 \times 0 \times \dots = 0`$ per qualsiasi parametro, e non distinguerebbe nulla.
---
## La soluzione: una finestrella
![](notion-file-block://51673f03-1544-4535-8f14-d93c7f9a12c1/773df0a8-ef6c-4649-855a-61194a904d99?space_id=98012abc-808d-816f-9733-00030a2b4817&name=21-likelihood-continuo.svg)
Al posto del punto si prende un intervallino di semiampiezza $`\varepsilon`$ attorno a ciascun dato:
$$
L = P(x_1 - \varepsilon \le X_1 \le x_1 + \varepsilon)\cdot P(x_2 - \varepsilon \le X_2 \le x_2 + \varepsilon)\cdots P(x_n - \varepsilon \le X_n \le x_n + \varepsilon)
$$
Ogni fattore ora è un numero diverso da zero, ed è un integrale della densità:
$$
P(x_i - \varepsilon \le X \le x_i + \varepsilon) = \int_{x_i - \varepsilon}^{x_i + \varepsilon} f(x)\,dx
$$
<callout icon="🎯" color="blue_bg">
	Nota del docente: **per quanto piccolo si prenda **$`\varepsilon`$**, l'intervallo resta "popolato"**. Non serve che sia grande, serve solo che non sia un punto.
	E poiché $`\varepsilon`$ è lo stesso per tutti i dati, moltiplica la verosimiglianza per una costante: sposta la curva in su o in giù, ma non sposta il punto di massimo. Sparisce dal risultato.
</callout>
---
## Il vettore dei parametri
Finora c'era un parametro solo. In generale una distribuzione ne ha più d'uno, e si raccolgono in un vettore:
$$
\theta = (p_1,\, p_2,\, p_3,\, \dots,\, p_m)
$$
<table fit-page-width="true" header-row="true">
<tr>
<td>Distribuzione</td>
<td>Parametri</td>
</tr>
<tr>
<td>Geometrica (fumatrici / non fumatrici)</td>
<td>$`\theta = (p)`$ — uno solo</td>
</tr>
<tr>
<td>Esponenziale</td>
<td>$`\theta = (\lambda)`$</td>
</tr>
<tr>
<td>Gauss</td>
<td>$`\theta = (\mu, \sigma)`$ — due</td>
</tr>
</table>
La verosimiglianza diventa allora $`L(\theta)`$, e il metodo non cambia: si cerca il $`\theta`$ che la rende massima. Con un parametro si annulla una derivata, con $`m`$ parametri se ne annullano $`m`$.
---
## Lo schema, una volta per tutte
<table fit-page-width="true" header-row="true">
<tr>
<td>Passo</td>
<td>Discreto</td>
</tr>
<tr>
<td>Contributo di un dato</td>
<td>$`P(x_i)`$</td>
</tr>
<tr>
<td>Verosimiglianza</td>
<td>prodotto dei contributi di tutti i dati</td>
</tr>
<tr>
<td>Stima</td>
<td>il $`\theta`$ che massimizza $`L(\theta)`$</td>
</tr>
</table>
---
## Riferimenti
- Dekking et al., *A Modern Introduction to Probability and Statistics*, cap. 21
