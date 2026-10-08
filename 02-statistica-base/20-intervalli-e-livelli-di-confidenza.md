# 20 - Intervalli e livelli di confidenza

> Fonte Notion: https://app.notion.com/p/3c712abc808d81399209dd9e8cde671c — ultima modifica 2026-08-25T21:11:06.698Z

<table_of_contents color="gray"/>
Una stima da sola non basta: serve dire **quanto stretta** è, e con quanta fiducia.
<callout icon="💬" color="green_bg">
	**In parole semplici**
	I sondaggi elettorali dicono "il 41%, con un margine di errore del 2% e un livello di confidenza del 95%".
	L'intervallo è 39–43. Il 95% dice: se ripetessimo il sondaggio tante volte, 95 volte su 100 l'intervallo costruito così conterrebbe il vero valore.
</callout>
---
## La costruzione
Dalla variabile $`X`$ si estrae un campione $`\{x_i\}_n`$. La distribuzione ha un parametro (o più) da stimare, ad esempio $`\theta = (\mu, \sigma^2)`$.
Si costruiscono **due funzioni dei dati** — non del parametro, che non conosciamo:
$$
L_n = g(x_i) \qquad\qquad U_n = f(x_i)
$$
e si chiede che l'intervallo fra le due contenga il parametro vero con probabilità $`\gamma`$:
$$
\boxed{\;P\big(L_n < \theta < U_n\big) = \gamma\;}
$$
<table fit-page-width="true" header-row="true">
<tr>
<td>Oggetto</td>
<td>Nome</td>
</tr>
<tr>
<td>$`\gamma \in [0, 1]`$, scritto come $`100 \times \gamma\ \%`$</td>
<td>**livello di confidenza** (confidence level)</td>
</tr>
<tr>
<td>$`(L_n,\, U_n)`$</td>
<td>**intervallo di confidenza** (confidence interval)</td>
</tr>
</table>
---
## Che cosa significa davvero
![](notion-file-block://e164bbc4-56f0-484c-8f15-43cff446227f/4ddfdf01-9739-4d05-9c2c-abda6e717488?space_id=98012abc-808d-816f-9733-00030a2b4817&name=23-confidenza.svg)
<callout icon="⚠️" color="yellow_bg">
	**L'errore classico.** "C'è il 90% di probabilità che $`\theta`$ stia nel mio intervallo" **non** è la lettura corretta.
	$`\theta`$ è un numero fisso: o ci sta o non ci sta. La cosa che varia è **l'intervallo**, perché dipende dai dati che ho pescato. Il 90% descrive la **procedura**: applicata tante volte, azzecca 9 volte su 10.
</callout>
---
## Il legame con $`\alpha`$
Il complemento del livello di confidenza si chiama $`\alpha`$:
$$
\gamma = 1 - \alpha
$$
Con $`\gamma = 0{,}95`$ si ha $`\alpha = 0{,}05`$. Questo $`\alpha`$ è la stessa quantità che regola i test di ipotesi — le due cose sono due facce dello stesso conto.
---
## Un avvertimento del docente
<callout icon="🎯" color="blue_bg">
	**Non sempre è possibile definire **$`L_n(x_i)`$** e **$`U_n(x_i)`$**.**
	Costruire l'intervallo richiede di sapere come si distribuisce la stima. Quando la distribuzione non è nota o non è trattabile, la formula chiusa non esiste e servono altre strade.
</callout>
---
## Riferimenti
- Dekking et al., *A Modern Introduction to Probability and Statistics*, cap. 23
