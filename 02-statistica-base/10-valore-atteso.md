# 10 - Valore atteso

> Fonte Notion: https://app.notion.com/p/3c712abc808d81af84bcf8dfefa62ee8 — ultima modifica 2026-08-25T09:32:39.222Z

<table_of_contents color="gray"/>
Il parametro $`\mu`$ incontrato nella Gauss ha un significato generale, che vale per **qualsiasi** distribuzione.
<callout icon="💬" color="green_bg">
	**In parole semplici**
	È il valore **su cui scommetteresti**, se dovessi indovinare in anticipo come andrà a finire.
	Si calcola così: prendi tutti i risultati possibili, moltiplica ciascuno per quanto è probabile, e somma. I risultati probabili pesano tanto, quelli improbabili quasi niente.
	È una **media pesata**, dove i pesi sono le probabilità.
</callout>
---
## Tre nomi per la stessa cosa
A lezione compaiono tutti e tre, e indicano lo stesso numero:
- **valore medio**
- **valore atteso**
- **valore di aspettazione**
Si scrive con l'operatore $`E`$ e si indica con $`\mu`$.
---
## Come si costruisce
Partiamo da una variabile che può dare i valori $`a_1, a_2, \dots, a_n`$, ciascuno con la sua probabilità $`p(a_1), p(a_2), \dots, p(a_n)`$.
Si moltiplica ogni valore per la sua probabilità e si sommano tutti i contributi:
$$
a_1 \cdot p(a_1) \;+\; a_2 \cdot p(a_2) \;+\; \dots \;+\; a_n \cdot p(a_n)
$$
<table fit-page-width="true" header-row="true">
<tr>
<td>Caso</td>
<td>Formula</td>
<td>Come si legge</td>
</tr>
<tr>
<td>**Discreto**</td>
<td>$`\mu = E[a] = \sum_i a_i \cdot p(a_i)`$</td>
<td>Somma dei valori pesati per le loro probabilità</td>
</tr>
<tr>
<td>**Continuo**</td>
<td>$`\mu = E[x] = \int_{-\infty}^{+\infty} x \cdot f(x)\,dx`$</td>
<td>Stessa cosa, con l'integrale al posto della somma</td>
</tr>
</table>
> Nel continuo l'operatore integrale si applica al **prodotto** $`x \cdot f(x)`$, non alla sola densità. È la stessa struttura del caso discreto: valore per peso, poi si somma tutto.
---
## Sul dado
**Un dado singolo.** I sei risultati sono equiprobabili, quindi ciascuno pesa $`1/6`$:
$$
E = \frac{1+2+3+4+5+6}{6} = 3{,}5
$$
<callout icon="🎯" color="blue_bg">
	**Attenzione: 3,5 non è un risultato possibile.** Il valore atteso non è "il risultato che uscirà più spesso", e non deve nemmeno essere uno dei valori ammessi: è il **baricentro** della distribuzione. Confonderlo con il valore più probabile è l'errore più comune.
</callout>
**La somma di due dadi.** Usando le probabilità del modulo 04 il conto dà **7**, che qui coincide anche con il valore più probabile — ma solo perché la distribuzione è simmetrica.
**Il massimo di due dadi.** Qui la distribuzione è sbilanciata, e la differenza si vede:
$$
E = \frac{1 \cdot 1 + 2 \cdot 3 + 3 \cdot 5 + 4 \cdot 7 + 5 \cdot 9 + 6 \cdot 11}{36} = \frac{161}{36} \approx 4{,}47
$$
Il valore **più probabile** del massimo è 6, ma il valore **atteso** è circa 4,5: due domande diverse, due risposte diverse.
---
## Riferimenti
- Dekking et al., *A Modern Introduction to Probability and Statistics*, cap. 7 ("Expectation and variance")
