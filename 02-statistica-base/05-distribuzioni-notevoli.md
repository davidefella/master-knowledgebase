# 05 - Distribuzioni notevoli

> Fonte Notion: https://app.notion.com/p/3c612abc808d81f4b2c1c8a5af7d9daa — ultima modifica 2026-08-25T21:10:43.853Z

<table_of_contents color="gray"/>
Alcune situazioni ricorrono così spesso che la loro distribuzione ha un nome proprio. Il docente ne presenta tre: **Bernoulli**, **Binomiale**, **Geometrica**.
<callout icon="💬" color="green_bg">
	**In parole semplici**
	Ci sono situazioni che ricapitano di continuo, e per cui qualcuno ha già fatto il conto una volta per tutte. Qui ne vedi tre, e la differenza fra loro sta tutta nella domanda che fai:
	- **una prova sola: va o non va?** → Bernoulli
	- **tante prove: quante vanno a buon fine?** → Binomiale
	- **quante prove devo fare prima che vada bene?** → Geometrica
	L'esempio che le tiene insieme è un test a crocette a cui rispondi tirando a indovinare.
</callout>
---
## Bernoulli — Ber(p)
Il caso più semplice possibile: **un solo tentativo, due soli esiti**.
$$
P(e = 1) = p \qquad P(e = 0) = 1 - p
$$
Si chiama 1 il successo e 0 l'insuccesso, ma sono etichette: testa/croce, risposta giusta/sbagliata, clic/non clic.
> **È il mattone.** Da sola dice poco: serve perché le altre due distribuzioni si costruiscono **ripetendo** prove di Bernoulli.
---
## L'esempio del test a risposta multipla
Un test di **10 domande**, ciascuna con **4 opzioni** e una sola giusta. Rispondi completamente a caso: su ogni domanda hai probabilità $`p = 1/4`$ di indovinare.
Ogni domanda è una Bernoulli: chiamiamo $`R_i = 1`$ se la $`i`$-esima risposta è giusta, $`R_i = 0`$ se è sbagliata. Il numero totale di risposte esatte è
$$
X = R_1 + R_2 + \dots + R_{10}
$$
e può valere da 0 a 10.
### Nessuna risposta giusta
Serve che **tutte** e dieci siano sbagliate. Le domande sono indipendenti, quindi le probabilità si moltiplicano:
$$
P(X = 0) = \underbrace{\tfrac{3}{4} \times \tfrac{3}{4} \times \dots \times \tfrac{3}{4}}_{10 \text{ volte}} = \left(\tfrac{3}{4}\right)^{10} \approx 5{,}6\%
$$
### Esattamente una risposta giusta
Una giusta e nove sbagliate: $`\tfrac{1}{4} \cdot \left(\tfrac{3}{4}\right)^{9}`$. Ma **quale** sia quella giusta non è stabilito: può essere una qualsiasi delle 10 domande, e sono 10 casi distinti che vanno sommati.
$$
P(X = 1) = 10 \cdot \tfrac{1}{4} \cdot \left(\tfrac{3}{4}\right)^{9} \approx 18{,}8\%
$$
### Il caso generale
$$
P(X = k) = C_{10,k} \cdot \left(\tfrac{1}{4}\right)^{k} \cdot \left(\tfrac{3}{4}\right)^{10-k}
$$
<callout icon="🧱" color="blue_bg">
	**La formula ha tre pezzi, e ognuno risponde a una domanda diversa.**
	- $`\left(\tfrac{1}{4}\right)^{k}`$ → le $`k`$ risposte giuste
	- $`\left(\tfrac{3}{4}\right)^{10-k}`$ → le rimanenti sbagliate
	- $`C_{10,k}`$ → **in quanti modi diversi** le giuste possono disporsi fra le dieci domande
</callout>
---
## Il coefficiente binomiale
Risponde a: *in quanti modi posso scegliere *$`k`$* oggetti fra *$`n`$*, senza che conti l'ordine?*
**Sul test**, in quanti modi 3 risposte giuste possono distribuirsi fra 10 domande:
$$
C_{10,3} = \frac{10 \cdot 9 \cdot 8}{3 \cdot 2 \cdot 1} = 120
$$
Sopra si moltiplicano tanti fattori decrescenti quanti sono gli oggetti da scegliere; sotto si divide perché l'ordine non conta. Nel caso generale:
$$
C_{n,k} = \frac{n \cdot (n-1) \cdot (n-2) \cdots (n-k+1)}{1 \cdot 2 \cdot 3 \cdots k} = \frac{n!}{k!\,(n-k)!}
$$
dove il **fattoriale** è il prodotto di tutti gli interi fino a quel numero:
$$
n! \equiv 1 \cdot 2 \cdot 3 \cdots (n-1) \cdot n \qquad \text{ad esempio} \qquad 3! = 1 \cdot 2 \cdot 3 = 6
$$
---
## Binomiale — Bin(n, p)
Generalizza l'esempio del test: $`n`$** prove indipendenti**, ciascuna di Bernoulli con probabilità $`p`$, e si conta **quanti successi** si ottengono in tutto.
$$
P(k) = C_{n,k} \cdot p^{k} \cdot (1-p)^{\,n-k}
$$
con $`p`$ = probabilità di successo e $`1-p`$ = probabilità di insuccesso su una singola prova.
**Il test a risposta multipla è esattamente** $`\text{Bin}(10,\ 1/4)`$:
<table fit-page-width="true" header-row="true">
<tr>
<td>Risposte esatte $`k`$</td>
<td>0</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td>Probabilità</td>
<td>5,6%</td>
<td>18,8%</td>
<td>**28,2%**</td>
<td>25,0%</td>
</tr>
</table>
> Il risultato più probabile rispondendo a caso è **2 risposte esatte su 10**. E la probabilità di non azzeccarne nemmeno una è solo del 5,6%: indovinarne qualcuna per caso è la norma, non l'eccezione.
---
## Geometrica — Geo(p)
Cambia la domanda: non "quanti successi su $`n`$ prove", ma **"quanti tentativi devo fare prima di riuscire?"**
$$
P(k) = (1-p)^{\,k-1} \cdot p
$$
dove $`k`$ è il numero di tentativi fino al primo successo, quello riuscito compreso. La formula si legge da sinistra: $`k-1`$ fallimenti di fila, e poi il successo.
**Con** $`p = 1/4`$:
<table fit-page-width="true" header-row="true">
<tr>
<td>Tentativi $`k`$</td>
<td>1</td>
<td>2</td>
<td>3</td>
</tr>
<tr>
<td>Probabilità</td>
<td>25,0%</td>
<td>18,8%</td>
<td>14,1%</td>
</tr>
</table>
> È sempre decrescente: il caso più probabile è riuscire subito. Ogni tentativo in più richiede un fallimento in più, che moltiplica per un numero minore di 1.
---
## Quale usare
<table fit-page-width="true" header-row="true">
<tr>
<td>La domanda</td>
<td>Distribuzione</td>
<td>Cosa conta</td>
</tr>
<tr>
<td>"Va bene o no?", una volta sola</td>
<td>**Bernoulli** $`(p)`$</td>
<td>L'esito di una singola prova: 0 o 1</td>
</tr>
<tr>
<td>"Su $`n`$ prove, quanti successi?"</td>
<td>**Binomiale** $`(n, p)`$</td>
<td>Il numero di successi, da 0 a $`n`$</td>
</tr>
<tr>
<td>"Quanto devo aspettare per il primo successo?"</td>
<td>**Geometrica** $`(p)`$</td>
<td>Il numero di tentativi, da 1 in su</td>
</tr>
</table>
> Il numero di prove è **fissato** nella binomiale e **variabile** nella geometrica: nella prima sai quante prove farai e ti chiedi il risultato, nella seconda sai il risultato che vuoi e ti chiedi quante prove serviranno.
---
## Riferimenti
- Dekking et al., *A Modern Introduction to Probability and Statistics*, cap. 4 ("Discrete random variables")
