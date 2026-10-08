# 15 - Grandi numeri e limite centrale

> Fonte Notion: https://app.notion.com/p/3c712abc808d81f09556cc6195146dc4 — ultima modifica 2026-08-25T21:10:55.706Z

<table_of_contents color="gray"/>
Due risultati che spiegano **perché raccogliere più dati serve** — e sono la ragione per cui la Gauss salta fuori dappertutto.
<callout icon="💬" color="green_bg">
	**In parole semplici**
	**Legge dei grandi numeri**: più dati raccogli, più la loro media si incolla al valore vero.
	**Teorema del limite centrale**: e non solo si avvicina — lo fa sbagliando in modo gaussiano, qualunque sia il fenomeno di partenza.
</callout>
---
## Il punto di partenza
Da una variabile $`X`$ con valore atteso $`\mu`$ estraggo $`n`$ osservazioni $`x_1, x_2, \dots, x_n`$ e ne faccio la media:
$$
\bar{X}_n = \frac{x_1 + x_2 + \dots + x_n}{n}
$$
Questa media è una **stima** di $`\mu`$: è il numero che calcolo dai dati per indovinare quello vero, che non conosco.
La sua varianza si restringe al crescere di $`n`$:
$$
\mathrm{Var}(\bar{X}_n) = \frac{\sigma^2}{n}
$$
> È il fatto chiave: la media di tanti dati **balla meno** dei singoli dati. Con 100 osservazioni oscilla dieci volte meno che con una sola.
---
## Legge dei grandi numeri
![](notion-file-block://56b92e61-efa8-4df0-a6fc-ac55dced332d/0720871b-47ca-4c2e-8753-5217c0b3d727?space_id=98012abc-808d-816f-9733-00030a2b4817&name=18-grandi-numeri.svg)
In formula: fissato uno scarto $`\varepsilon`$ piccolo a piacere, la probabilità che la media dei dati sia lontana da $`\mu`$ più di $`\varepsilon`$ tende a zero.
$$
\lim_{n \to \infty} P\big(|\bar{X}_n - \mu| > \varepsilon\big) = 0
$$
<callout icon="🎯" color="blue_bg">
	Vale **qualunque sia la pdf** di partenza. Non serve che i dati siano gaussiani: possono essere esponenziali, uniformi, qualsiasi cosa.
</callout>
<details>
<summary>Perché è vero — la disuguaglianza di Čebyšëv</summary>
	Čebyšëv mette un tetto alla probabilità di allontanarsi dal valore atteso, usando solo la varianza:
	$$
	P\big(|Y - E[Y]| \ge a\big) \;\le\; \frac{1}{a^2}\,\mathrm{Var}(Y)
	$$
	La dimostrazione parte dalla definizione di varianza e butta via dei pezzi positivi:
	$$
	\mathrm{Var}(Y) = \int_{-\infty}^{+\infty} (y-\mu)^2 f(y)\,dy \;\ge\; \int_{|y-\mu| \ge a} (y-\mu)^2 f(y)\,dy \;\ge\; a^2 \!\!\int_{|y-\mu| \ge a} \!\! f(y)\,dy = a^2\, P(|Y-\mu| \ge a)
	$$
	Il primo passaggio restringe l'integrale a una parte del dominio; il secondo sostituisce $`(y-\mu)^2`$ con $`a^2`$, che lì dentro è più piccolo.
	Applicandolo a $`\bar{X}_n`$ con $`a = \varepsilon`$:
	$$
	P\big(|\bar{X}_n - \mu| > \varepsilon\big) \;\le\; \frac{1}{\varepsilon^2}\,\mathrm{Var}(\bar{X}_n) = \frac{1}{\varepsilon^2}\cdot\frac{\sigma^2}{n} \;\xrightarrow[n \to \infty]{}\; 0
	$$
</details>
---
## Teorema del limite centrale
La legge dei grandi numeri dice **dove** finisce la media. Il limite centrale dice **con che forma** ci arriva.
Si prende lo scarto $`\bar{X}_n - \mu`$ e lo si riscala in modo che non si schiacci a zero:
$$
Z_n = \sqrt{n}\;\frac{\bar{X}_n - \mu}{\sigma}
$$
Per $`n`$ grande:
$$
Z_n \;\longrightarrow\; \text{Gauss}(\mu = 0,\; \sigma = 1) = N(0,1)
$$
<callout icon="🎯" color="blue_bg">
	Anche qui: **non importa da quale distribuzione vengono i dati**. Questo è il motivo per cui la gaussiana compare ovunque — non perché la natura sia gaussiana, ma perché le **medie** lo diventano.
</callout>
<details>
<summary>Perché c'è quel √n</summary>
	Senza riscalare, $`\bar{X}_n - \mu`$ tende a zero (è la legge dei grandi numeri) e non si vedrebbe più nulla. La sua deviazione standard vale $`\sigma/\sqrt{n}`$: dividendo per quella, cioè moltiplicando per $`\sqrt{n}/\sigma`$, si ottiene una quantità che resta di dimensione fissa e la cui forma si può osservare. Il risultato è sempre la stessa: una gaussiana standard.
</details>
---
## I due risultati in una riga
<table fit-page-width="true" header-row="true">
<tr>
<td></td>
<td>Cosa dice</td>
</tr>
<tr>
<td>**Grandi numeri**</td>
<td>la media aritmetica $`\bar{X}_n`$ tende al valore atteso $`\mu`$</td>
</tr>
<tr>
<td>**Limite centrale**</td>
<td>$`Z_n = \sqrt{n}\,(\bar{X}_n - \mu)/\sigma`$ tende a $`N(0,1)`$</td>
</tr>
</table>
---
## Riferimenti
- Dekking et al., *A Modern Introduction to Probability and Statistics*, cap. 13 ("The law of large numbers") e cap. 14 ("The central limit theorem")
