# 22 - Valori critici e intervallo per la media

> Fonte Notion: https://app.notion.com/p/3c712abc808d81fbbd78faebc0f212b0 — ultima modifica 2026-08-25T21:11:14.126Z

<table_of_contents color="gray"/>
Nel modulo 20 l'intervallo di confidenza era una definizione. Qui si costruisce davvero, per il caso più comune: **stimare la media**.
<callout icon="💬" color="green_bg">
	**In parole semplici**
	Ho misurato l'altezza media di 100 persone e mi è venuto 172 cm. Quanto posso sbagliarmi?
	La risposta ha sempre la stessa forma: **media misurata ± un tot**. Il “tot” dipende da quanto sono sparsi i dati, da quanti ne ho, e da quanta sicurezza voglio.
</callout>
---
## Il punto di partenza
Se i dati vengono da una gaussiana, allora anche la loro media è gaussiana, ma **più stretta**:
$$
x_i \sim G(\mu, \sigma) \qquad\Longrightarrow\qquad \bar{X}_n \sim G\!\left(\mu,\; \frac{\sigma}{\sqrt{n}}\right)
$$
Standardizzando si torna alla gaussiana standard — la stessa $`z`$ del teorema del limite centrale (modulo 15):
$$
z = \frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} \;\sim\; N(0,1)
$$
---
## I valori critici
![](notion-file-block://1090cadf-c93e-47f8-9a4d-8dbd39777667/3649420a-37c6-41ca-bae3-9929eb66ff97?space_id=98012abc-808d-816f-9733-00030a2b4817&name=25-valori-critici.svg)
Si sceglie la confidenza $`\gamma`$ e si cercano i due tagli $`c_\ell`$ e $`c_u`$ che lasciano dentro quella frazione di probabilità:
$$
P(c_\ell < z < c_u) = \gamma
$$
Fuori resta $`\alpha = 1 - \gamma`$, metà per coda:
$$
P(z > c_u) = \frac{\alpha}{2} \qquad\qquad P(z < c_\ell) = \frac{\alpha}{2}
$$
Questi due numeri si chiamano **valori critici**. Per simmetria della gaussiana:
$$
c_u = z_{\alpha/2} \qquad\qquad c_\ell = -z_{\alpha/2}
$$
---
## Il valore da ricordare
<table fit-page-width="true" header-row="true">
<tr>
<td>$`\gamma`$</td>
<td>$`\alpha`$</td>
<td>$`\alpha/2`$</td>
<td>$`z_{\alpha/2}`$</td>
</tr>
<tr>
<td>**95%**</td>
<td>0,05</td>
<td>0,025</td>
<td>**1,96**</td>
</tr>
<tr>
<td>99%</td>
<td>0,01</td>
<td>0,005</td>
<td>2,58</td>
</tr>
</table>
> Il valore 1,96 è quello che si incontra ovunque: è il motivo per cui si sente dire “due sigma” come sinonimo di 95%.
---
## L'intervallo
Partendo da $`P(c_\ell < z < c_u) = \gamma`$ e isolando $`\mu`$ si arriva a:
$$
\boxed{\;\left(\;\bar{X}_n - z_{\alpha/2}\,\frac{\sigma}{\sqrt{n}}\;;\;\; \bar{X}_n + z_{\alpha/2}\,\frac{\sigma}{\sqrt{n}}\;\right)\;}
$$
Con $`\gamma = 95\%`$ diventa la formula più usata di tutta la statistica:
$$
\bar{X}_n \;\pm\; 1{,}96\,\frac{\sigma}{\sqrt{n}}
$$
<details>
<summary>I passaggi algebrici, e perché i segni si scambiano</summary>
	Si parte da:
	$$
	\gamma = P\!\left(c_\ell < \frac{\bar{X}_n - \mu}{\sigma/\sqrt{n}} < c_u\right)
	$$
	Moltiplicando tutto per $`\sigma/\sqrt{n}`$ (positivo, quindi le disuguaglianze restano):
	$$
	= P\!\left(c_\ell \frac{\sigma}{\sqrt{n}} < \bar{X}_n - \mu < c_u \frac{\sigma}{\sqrt{n}}\right)
	$$
	Sottraendo $`\bar{X}_n`$:
	$$
	= P\!\left(c_\ell \frac{\sigma}{\sqrt{n}} - \bar{X}_n < -\mu < c_u \frac{\sigma}{\sqrt{n}} - \bar{X}_n\right)
	$$
	Ora si cambia segno a tutti i membri: **le disuguaglianze si invertono**.
	$$
	= P\!\left(\bar{X}_n - c_u \frac{\sigma}{\sqrt{n}} < \mu < \bar{X}_n - c_\ell \frac{\sigma}{\sqrt{n}}\right)
	$$
	Da notare l'incrocio: l'estremo **inferiore** dell'intervallo per $`\mu`$ si costruisce con il valore critico **superiore** $`c_u`$, e viceversa. Con $`c_\ell = -c_u`$ il risultato torna simmetrico e l'incrocio non si vede più.
</details>
---
## La procedura, in tre passi
1. si porta la quantità di interesse alla forma standard, $`z \sim N(0,1)`$
2. si sceglie $`\gamma`$ e si trovano i valori critici che ritagliano quella probabilità **dentro**
3. si passa da dentro a fuori ($`\gamma \to \alpha`$) e si rovescia la disuguaglianza per isolare il parametro
<callout icon="⚠️" color="yellow_bg">
	**Attenzione a **$`\sigma`$**.** Questa formula assume di **conoscere** la deviazione standard della popolazione. Nella pratica quasi mai la si conosce, e va stimata dai dati: allora il valore critico non si legge più sulla gaussiana. Il docente qui usa il caso con $`\sigma`$ nota.
</callout>
---
## Riferimenti
- Dekking et al., *A Modern Introduction to Probability and Statistics*, cap. 23
