# 01 - Matematica in biologia: ODE, Eulero e odeint

> Fonte Notion: https://app.notion.com/p/3e912abc808d81c29186c6a36952a493 — ultima modifica 2026-09-28T17:51:39.664Z

**Registrazione:** `BT-01` (portale, edizione 2025), durata 01:27:44. Giornata: **Day 2** del corso (titolo della slide "Mathematics in Biology, Matteo Rucco - Day 2").
**Materiale:** slide `Math_in_biology.pdf`; notebook `Lotka_Volterra.ipynb` (a schermo `Lotka-Volterra.ipynb`) e `Zombie_invasion.ipynb`.
> La registrazione parte a discorso iniziato ("Quando parlo di sistemi complessi..."): la parte iniziale della lezione non c'è. I rimandi all'"incontro precedente" e a "l'altro giorno" riguardano il Day 1, non registrato.
> **Nota sul codice.** Il notebook `Lotka_Volterra.ipynb` di Teams è la versione dell'edizione 2026, con i parametri cambiati in diretta dal docente (`Teams 2 @ 1:38:51`): le funzioni coincidono con il video 2025, i valori no (dettagli nelle Divergenze). In questo capitolo le funzioni vengono dal notebook, i valori dei parametri dal video, perché sono quelli che producono i grafici mostrati e commentati. La sezione 13 integra le lezioni Teams 2026.
## Indice
1. Sistemi complessi e perché si modella
2. La matematica nella biologia: una panoramica
3. Il filo comune: le equazioni differenziali
4. Risolvere un'ODE: metodo di Eulero e `odeint`
5. Primo esempio in Python: dy/dt = a·y
6. Il modello preda-predatore di Lotka-Volterra
7. Esercizi e sensitivity analysis
8. Modelli compartimentali: il SIR
9. L'invasione degli zombie
10. Esercizio finale
11. Collegamento con il test finale
12. Glossario, punti incerti, materiale usato
13. Integrazione Teams 2026: i quattro casi di studio
---
## 1. Sistemi complessi e perché si modella
`BT-01 @ 00:00:09`
Il concetto di **sistema complesso** viene dalla fisica, in particolare dalla meccanica statistica. Un sistema complesso è composto da molti **agenti** (attori), raggruppabili per classi; ogni classe ha un proprio comportamento. Il comportamento globale **non è prevedibile** guardando il singolo agente: bisogna osservare il comportamento collettivo e le interazioni. Ogni interazione può cambiare lo stato interno dell'agente che agisce, ma anche quello degli agenti vicini e dell'**ambiente**.
L'ambiente, nella teoria dei sistemi complessi, è l'insieme di ciò in cui vivono gli agenti, con le sue caratteristiche: concentrazioni di sostanze chimiche se si modellano reazioni, caratteristiche geografiche o orografiche se si modella uno spazio tridimensionale.
I modelli (matematici, combinatori, computazionali) servono a rappresentare e comprendere questi sistemi e a produrre previsioni e spiegazioni difficili da ottenere con poche osservazioni dirette o con esperimenti vincolati da assunzioni.
`BT-01 @ 00:02:06` Uno strumento di simulazione permette di **variare le condizioni iniziali** e osservare l'output di ogni esperimento. Esempio del docente: la caduta di un grave si può sperimentare in laboratorio variando forma, dimensione e peso e annotando i tempi, ma far cadere un oggetto di decine di tonnellate richiede strumentazione non disponibile. Un modello matematico implementato al computer permette di eseguire l'esperimento in digitale e, se il modello è abbastanza fedele alla realtà, di **anticipare esperimenti impegnativi o impossibili** dal vivo.
`BT-01 @ 00:04:04` Programma della lezione: esempi di applicazione della matematica alla biologia; poi un metodo pratico per risolvere le **equazioni differenziali**, lo strumento che permette di studiare o approssimare nel tempo il tasso di crescita di una quantità, sia con librerie già pronte sia scrivendo la routine di integrazione; infine l'applicazione a casi di studio.
## 2. La matematica nella biologia: una panoramica
`BT-01 @ 00:05:15`
Slide "What Kind of Biology?":
- Population of organisms - i.e., animals
- Spread of Disease - i.e., Flu, vaccines
- How muscles work - even the heart
- Diabetes - insulin and glucose
- Patterns in natures - zebra stripes, leopard spots
- Brain electrical behavior - sight, sound
- Organism growth - embryos
- Genetics …..and much more
Esempi citati a voce:
- **Dinamiche di popolazione:** come cresce una popolazione di insetti in una stagione, con certe risorse. In Biocentis, l'azienda del docente, uno degli strumenti più usati è la risoluzione di equazioni differenziali ordinarie, stocastiche e con ritardo per studiare ereditarietà e sviluppo di popolazioni di insetti.
- **Epidemiologia:** il termine **R0**, sentito spesso durante l'ultima pandemia, quantifica la "pressione" di un'epidemia sulla popolazione, cioè la velocità di diffusione. Si riprende nel SIR (sezione 8).
- **Biofisica muscolare:** modelli meccanicistici del movimento dei muscoli, cuore compreso. Gli sportivi professionisti hanno équipe mediche con biomatematici che costruiscono modelli personalizzati sull'anatomia dell'atleta, per la preparazione atletica e per accelerare le cure.
- **Diabete e regolazione del glucosio:** modelli della dinamica di insulina e glucosio, usati nel follow-up della terapia e nella prevenzione. Il docente cita il progetto europeo **Presidium**, che sviluppa modelli fisici che informano modelli di machine learning per prevenire il diabete di tipo 2.
- **Pattern in natura:** foglie, conchiglie, strisce delle zebre, macchie dei leopardi non sono casuali ma seguono pattern.
> **Correzione:** a voce il docente dice che le conchiglie "seguono la formula aurea". Molte conchiglie (per esempio il nautilus) crescono secondo una spirale logaritmica, ma il loro rapporto di crescita in generale non è il rapporto aureo.
- **Neuroscienze:** studi recenti hanno usato modelli matematici per approssimare i segnali elettrici del cervello (il docente cita ricercatori del San Raffaele e di Barcellona \[?\]). Il docente ricorda il Nobel a **John Hopfield**: la rete di Hopfield è uno dei modelli di riferimento per lo studio delle colonne corticali e per ipotizzare la dinamica delle crisi epilettiche.
> **Correzione:** il docente parla di "premio Nobel per l'intelligenza artificiale". Il premio è il **Nobel per la Fisica 2024**, assegnato a Hopfield e Hinton per i contributi alle reti neurali artificiali; non esiste un Nobel per l'intelligenza artificiale.
`BT-01 @ 00:11:33` Ogni campo ha sfide e modelli specifici. La tendenza recente è la **personalizzazione** dei modelli, al servizio della cosiddetta medicina personalizzata.
### 2.1 Diffusione di un contagio: modello esponenziale e logistico
`BT-01 @ 00:12:09`
Slide "Spread of Disease": "A quale ritmo si diffonde nella popolazione il contagio durante un'epidemia? E quale frazione della popolazione viene contagiata?"
$$
\frac{dN_C}{dt} = C \cdot N_C, \qquad C = E \cdot p
$$
"Può essere riscritta come"
$$
\frac{dN_C}{dt} = C \cdot N_C \cdot \left(1 - \frac{N_C}{P}\right)
$$
Il modello è volutamente ipersemplificato ma abbastanza veritiero. Descrive il contagio in una popolazione che **circola liberamente**, come una popolazione non ancora informata all'inizio di una pandemia; quando i comportamenti cambiano, per scelta o per imposizione, il modello non si applica più senza correttivi.
Lettura dal grafico: all'inizio gli infetti sono pochi, ognuno ne contagia alcuni, che a loro volta ne contagiano altri. È un **processo a catena**, che produce una crescita esponenziale dei contagiati.
- $`N_C`$: totale dei contagiati dall'inizio dell'epidemia; la prima equazione ne descrive la variazione nel tempo (una derivata).
- $`C`$: **tasso di contagio**, la rapidità di diffusione. Con passo temporale $`\Delta t`$ di un giorno, l'equazione esprime l'aumento percentuale giornaliero dei contagiati.
- $`C = E \cdot p`$: $`E`$ è il numero medio di persone con cui un infetto viene in contatto ogni giorno, $`p`$ la probabilità che un singolo contatto produca un contagio.
`BT-01 @ 00:15:46` Il modello esponenziale vale solo nelle **prime fasi**. Quando una frazione significativa della popolazione è contagiata, o quando si introducono misure di contenimento, il ritmo di diffusione si riduce. Il docente usa l'analogia di una bottiglia che si riempie: all'inizio il liquido si espande liberamente, poi lo spazio disponibile si restringe. La terza equazione (**logistica**) introduce esplicitamente questo limite tramite la popolazione totale $`P`$.
Domanda posta alla classe `BT-01 @ 00:17:29`: quando prima e terza equazione coincidono? Quando il termine fra parentesi vale 1, cioè quando $`N_C/P \ll 1`$: vale all'inizio della diffusione. Nel caso limite opposto, $`N_C = P`$, il fattore fra parentesi si annulla, la derivata è zero e non sono possibili altri contagi: tutti sono stati contagiati.
Grafico della slide ("modelli per la diffusione di un contagio in una popolazione", asse y $`N_C/P`$, frazione della popolazione già contagiata, asse x giorni): curva tratteggiata esponenziale, curva continua logistica, punto di **flesso** evidenziato. Nella simulazione del docente la logistica si discosta in modo significativo dall'esponenziale dopo circa 30 giorni; dopo circa 40 giorni metà della popolazione è contagiata. Il flesso cade a $`N_C/P = 0.5`$: da lì la diffusione rallenta, perché la popolazione si avvia a saturazione.
`BT-01 @ 00:21:13` Messaggio per un decisore pubblico: conviene intervenire **prima del punto di flesso**. Nella realtà però è difficile, all'inizio di un contagio, capire se il modello giusto è questo: servirebbero osservatori che monitorano costantemente la salute della popolazione. Spesso, per mancanza di monitoraggio quotidiano, le misure arrivano ben oltre il flesso, e si cerca allora di evitare la saturazione trasformando la curva in una "campana" che torni a zero.
> **Nota aggiunta:** la logistica descrive i contagiati **cumulati**. La sua derivata, cioè i nuovi contagi per unità di tempo, ha la forma a campana, con il massimo proprio nel punto di flesso della logistica.
### 2.2 Come nuota una sogliola
`BT-01 @ 00:23:28`
Slide "How do soles swim?": Physics of Fluids; F(x,t) = sole force; u = fluid velocity; p = pressure.
$$
\mu \Delta \mathbf{u} = \nabla p - \mathbf{F}(\mathbf{x},t), \qquad \nabla \cdot \mathbf{u} = 0
$$
Le sogliole oscillano l'intero corpo, non solo coda o pinne. Per approssimarne il moto si usano strumenti presi in prestito dalla fisica dei fluidi: il termine $`\mathbf{F}(\mathbf{x},t)`$, combinato con velocità del fluido e pressione, spiega come il pesce si muove nell'acqua.
Perché interessa: le tecnologie artificiali prendono spunto dalla natura. Secondo il docente, le pinne per l'immersione con autorespiratore (ARA) approssimano il moto delle sogliole e i produttori sanno risolvere queste equazioni. Le pinne da apnea, dice, sono più rigide, perché l'apneista deve fare meno movimenti possibile; chi ha le bombole può permettersi pinneggiate più frequenti con pinne più elastiche.
> **Nota aggiunta:** le due equazioni della slide sono le equazioni di Stokes per un fluido incomprimibile (la seconda è il vincolo di incomprimibilità).
### 2.3 Pattern in natura
`BT-01 @ 00:26:54`
Slide "Patterns in Nature": "Chemicals that react and diffuse in animal skin make visible patterns"; "C(x,t) concentration at time t location x".
$$
\frac{\partial C}{\partial t} = F(C) + D \nabla^2 C
$$
A sinistra tre immagini reali (due pesci e un fico d'India), a destra le analoghe generate al computer. I modelli usati per generarle studiano **propagazione, diffusione e tasso di crescita della concentrazione di sostanze chimiche** in funzione di posizione e tempo. Servono a capire perché si formano certi pattern e, soprattutto, a **classificare un tessuto come sano**: un pattern che si discosta da quello sano segnala un tessuto patologico.
Esempio applicativo: il monitoraggio degli **impollinatori**. Gli insetti catturati con trappole vengono studiati attraverso i pattern delle ali, che dipendono dalla salubrità dell'ambiente in cui vivono; da lì si deduce se i fiori con cui interagiscono sono in buona salute.
### 2.4 Sviluppo dell'embrione
`BT-01 @ 00:29:25`
Slide "Embryo Development - genes": "Young embryos form a body axis early on. Why? How? Chemicals cause cells to move."
Lo sviluppo embrionale è regolato da segnali chimici che guidano il movimento delle cellule e la formazione degli assi corporei. Un modello di riferimento serve a diagnosticare il prima possibile eventuali patologie e a riprodurre i primi stadi della **morfogenesi**.
Aneddoto del docente `BT-01 @ 00:30:39`: anni fa ha sviluppato con l'Istituto Ortopedico Rizzoli di Bologna un simulatore del **rimodellamento osseo**. L'osso non è statico: le sue cellule lavorano continuamente per erodere, deporre e calcificare nuovo materiale osseo, e anche questa dinamica si descrive con equazioni differenziali.
> **Correzione:** il docente attribuisce le tre funzioni, "rispettivamente", a osteoblasti, osteoclasti e osteoni. Sono gli **osteoclasti** a riassorbire (erodere) l'osso e gli **osteoblasti** a deporre nuova matrice; l'**osteone** non è una cellula ma l'unità strutturale dell'osso compatto.
`BT-01 @ 00:31:56` Nello sviluppo umano una struttura lineare, la **striscia primitiva**, compare circa 14 giorni dopo la fecondazione. Segna il passaggio dalla simmetria radiale a quella **bilaterale** (destra e sinistra) e fornisce informazioni spaziali antero-posteriori e dorso-ventrali; il processo si chiama **gastrulazione**, e da lì originano i vari tipi di cellule. Se il biologo osserva una striscia primitiva che non introduce una simmetria bilaterale, può capire da subito che l'embrione sarà con alta probabilità portatore di patologie. Secondo il docente, i primi a formalizzare matematicamente lo sviluppo della striscia primitiva furono due studiosi, nel 1991 (nomi non chiari nell'audio \[?\]); i loro modelli sono diventati riferimento nei software con cui i biologi valutano lo stato di salute dell'embrione, per esempio prima di un impianto.
Slide "Models Reproduce Experiments for streak development": n = cell density; u = chemical.
$$
\frac{\partial n}{\partial t} = \nabla \cdot \left(D_n \nabla n - n\,g(u)\,\nabla u\right) + f_1(u,n)
$$
$$
\frac{\partial u}{\partial t} = \nabla^2 u + f_2(u,n)
$$
Didascalia della figura (Figure 8): "Development of a nodal-like structure at the anterior portion of the developing 'streak'. The highest point of cell density moves from posterior to anterior, creating a bulbous-type structure reminiscent of Hensen's node. This structure is subsequently retained during regression."
Le due equazioni descrivono l'evoluzione nel tempo della densità cellulare e della concentrazione chimica. Sono modelli costruiti **a partire da osservazioni sperimentali** che permettono poi esperimenti predittivi: fondamentali per l'ideazione di nuovi farmaci.
### 2.5 Stimolo e risposta: il sistema visivo e il neurone
`BT-01 @ 00:36:19`
Slide "Some Biology is 'Stimulus/Response'": "A stimulus I causes an output u"; "Sometimes get an output even if there is no stimulus (I=0) (i.e., people who talk to you even when you don't talk to them)". Schema: Stimulus I → Model → Output u.
Fin qui si sono visti fenomeni di crescita spontanea; ma un fenomeno biologico si può vedere anche come **risposta a uno stimolo**. Esempio: il **sistema visivo**, governato da segnali elettrici neuronali che si attivano in risposta agli stimoli visivi. Si può modellare il tasso di attivazione elettrica dei neuroni in funzione dell'angolo dello stimolo, oltre che di altre variabili come la frequenza dell'onda luminosa, l'intensità della luce ambiente, i meccanismi di memoria (slide "Visual System": "The electrical firing rate of your visual system neurons changes with stimulus angle!").
Slide "Each neuron can be modeled.": "Ions move across membrane"; "Voltage V changes in time". Riquadro "Hodgkin-Huxley model of electrical activity in the squid giant axon":
$$
C_m \frac{dV}{dt} = -g_{Na} m^3 h (V - V_{Na}) - g_k n^4 (V - V_k) - g_L (V - V_L) + I_a(t)
$$
$$
\frac{dm}{dt} = \frac{m_\infty(V) - m}{\tau_m(V)}, \quad \frac{dh}{dt} = \frac{h_\infty(V) - h}{\tau_h(V)}, \quad \frac{dn}{dt} = \frac{n_\infty(V) - n}{\tau_n(V)}
$$
Il modello di **Hodgkin-Huxley** è uno dei riferimenti per la dinamica dei neuroni: ogni neurone è rappresentato dalla variazione del potenziale elettrico; gli ioni che attraversano la membrana generano segnali elettrici descrivibili matematicamente, e si possono simulare la trasmissione dei segnali e i processi cognitivi che ne derivano.
Slide "Models of Visual System Orientation Patterns": "Activity a(r,t) at time t, position r in your brain." La mappa colorata illustra i pattern di attivazione della corteccia durante la visione, per orientamento dello stimolo.
$$
\frac{\partial}{\partial t} a(\mathbf{r},t) = -\alpha\, a(\mathbf{r},t) + \nu \int_\Omega w_{lat}(\mathbf{r}-\mathbf{r}')\,\sigma[a(\mathbf{r}',t)]\,d\mathbf{r}'
$$
### 2.6 Diabete
`BT-01 @ 00:40:23`
Slide "Diabetes": "An increase in glucose (sugar) causes pancreas cells to make insulin. Calcium plays a key role." Figure: anatomia dell'apparato digerente, sezione del pancreas, parte esocrina (cellule acinose) ed endocrina (isole di Langerhans).
I modelli sviluppati nel progetto citato descrivono la dinamica della glicemia e permettono di **simulare l'effetto delle terapie farmacologiche**, così da personalizzare l'intervento sulla fisiologia del singolo paziente.
## 3. Il filo comune: le equazioni differenziali
`BT-01 @ 00:41:30`
Domanda alla classe: cosa hanno in comune tutti questi modelli? Studiano fenomeni che **evolvono nel tempo**, e il tempo compare dentro le **equazioni differenziali**. I modelli visti hanno assunzioni forti (per esempio l'assenza di ritardi e di reazioni ad altri stimoli), ma lo strumento dominante è quello.
Il docente però non vuole che si esca dalla lezione pensando che l'equazione differenziale sia l'unico strumento. Slide "Lot's of different kinds of math models":
<table header-row="true">
<tr>
<td>Tipo</td>
<td>Forma</td>
</tr>
<tr>
<td>Functional</td>
<td>$`u = F(I)`$</td>
</tr>
<tr>
<td>Ordinary Differential Equation (ODE)</td>
<td>$`\frac{du}{dt} = F(u) + I(t)`$</td>
</tr>
<tr>
<td>Partial Differential Equation (PDE)</td>
<td>$`\frac{\partial u}{\partial t} = D\frac{\partial^2 u}{\partial x^2} + F(u) + I(x,t)`$</td>
</tr>
<tr>
<td>Map</td>
<td>$`u_{n+1} = F(u_n) + I_n`$</td>
</tr>
<tr>
<td>Filter</td>
<td>$`u(t) = \int F(t-s)\,I(s)\,ds`$</td>
</tr>
</table>
Si sceglie il modello in base a cosa si deve descrivere:
- dipendenza dallo **spazio**: non le ODE, ma altri strumenti (le PDE);
- **tempo discreto**: equazioni di ricorsione (le mappe);
- quantità che superano o scendono sotto una soglia, o che si **accumulano** nel tempo: integrali. Un integrale singolo è l'area sotto una curva, quindi la quantità di materia accumulata nel tempo.
Alcuni modelli sono semplici e predittivi, altri complessi e descrittivi. Il focus del corso resta sulle **equazioni differenziali ordinarie**, almeno fino all'introduzione della simulazione ad agenti.
## 4. Risolvere un'ODE: metodo di Eulero e `odeint`
`BT-01 @ 00:45:06`
Due metodi principali: il **metodo di Eulero** e la funzione **`odeint`** del pacchetto `scipy.integrate`. Si usa Python perché è open source e gira su Google Colab (accessibile con un account Gmail), ma il concetto vale in ogni linguaggio.
Scelta didattica del docente `BT-01 @ 00:46:45`: introdurre Eulero ha più valore che imparare a usare una libreria di terze parti senza sapere cosa fa. Meglio capire prima cosa fa la libreria, magari riscrivendone il codice, e poi adottarla: la libreria reimplementa lo stesso codice, ma in modo più stabile ed efficiente.
### 4.1 Il metodo di Eulero
`BT-01 @ 00:47:49`
Eulero è un algoritmo numerico semplice per risolvere ODE: approssima la soluzione con una serie di valori calcolati lungo l'intervallo di interesse (**orizzonte temporale**). È utile quando non esiste una soluzione analitica e servono metodi iterativi.
Slide "Methods to solve differential equation: Euler or ODEINT", riquadro "Euler Method":
"The most basic way of sovling an ODE numerically is Euler Method. Remember the definition of the derivative is"
$$
\frac{dy}{dt} = \lim_{\Delta t \to 0} \frac{y(t+\Delta t) - y(t)}{\Delta t}.
$$
"Thus we can approximate dy/dt with a small time step Δt as"
$$
\frac{dy}{dt} \simeq \frac{y(t+\Delta t) - y(t)}{\Delta t} = f(y,t).
$$
"This brings us to an update equation"
$$
y(t+\Delta t) = y(t) + f(y,t)\,\Delta t
$$
"starting from an initial condition $`y(t_0) = y_0`$."
Il ragionamento: se $`\Delta t`$ è abbastanza piccolo, il limite si può togliere e resta il rapporto incrementale; isolando $`y(t+\Delta t)`$ si ottiene la regola di aggiornamento. La condizione iniziale $`y_0`$ è una quantità nota. "Non dovete memorizzarlo", dice il docente: conta la slide successiva, cioè il codice.
### 4.2 `odeint` di SciPy
`BT-01 @ 00:50:45`
In fondo alla slide c'è il link "Precooked ODEINT in Python-scipy" alla documentazione ufficiale (SciPy 1.14.1 a schermo). Come si legge la pagina: `odeint` prende alcuni parametri obbligatori, in particolare la funzione da integrare (`func`), la condizione iniziale `y0` e il vettore dei tempi `t`, e altri con valore di default; sotto la firma c'è la spiegazione di ogni parametro e dell'output. Alcuni parametri si scelgono da un dizionario di valori ammessi.
Esempio della documentazione `BT-01 @ 00:52:22`, il pendolo con attrito:
```python
import numpy as np

def pend(y, t, b, c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

b = 0.25
c = 5.0
y0 = [np.pi - 0.1, 0.0]
t = np.linspace(0, 10, 101)

from scipy.integrate import odeint
sol = odeint(pend, y0, t, args=(b, c))
```
La funzione `pend` riceve lo stato `y` (qui la coppia $`\theta`$, $`\omega`$), il tempo e i parametri `b` e `c`. Le condizioni iniziali sono $`\theta(0) = \pi - 0.1`$ (pendolo quasi verticale) e $`\omega(0) = 0`$. A `odeint` si passano la funzione, le condizioni iniziali, il vettore dei tempi e i parametri tramite `args`. Poiché il sistema ha due equazioni, `sol` contiene due serie temporali, una per $`\theta`$ e una per $`\omega`$ (array di shape `(101, 2)`).
> **Nota aggiunta:** `odeint` è un'interfaccia alla routine LSODA della libreria Fortran ODEPACK, a passo adattivo, che passa automaticamente fra metodi per problemi stiff e non stiff. La documentazione di SciPy raccomanda `solve_ivp` per il codice nuovo; per gli esercizi del corso si usa `odeint`.
### 4.3 Pregi e limiti di Eulero
`BT-01 @ 00:54:09`
Per usare Eulero bisogna implementare la routine, ma è semplicissimo. Il metodo è **meno preciso** di altri metodi di integrazione come Runge-Kutta o `odeint`: se serve una soluzione molto precisa, Eulero non fa per voi.
Può avere problemi di **stabilità** quando il passo $`\Delta t`$ è grande: matematicamente l'approssimazione del rapporto incrementale non vale più, anche se il codice continua a girare, e i risultati possono **divergere rapidamente** dalla soluzione reale. Esempio: una serie la cui dinamica vera cambia su scala giornaliera ma osservata su scala mensile. In quei casi il docente sconsiglia Eulero e suggerisce metodi più impegnativi da implementare ma più stabili e precisi, in particolare **Runge-Kutta del quarto ordine**.
### 4.4 Implementazione in Python
`BT-01 @ 00:56:25`
Slide "Euler method in python", "Import the main libraries" e "Define the Euler method":
```python
# As usual, import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
```
```python
def euler(f, y0, dt, n, *args):
    """f: righthand side of ODE dy/dt=f(y,t)
        y0: initial condition y(0)=y0
        dt: time step
        n: iteratons
        args: parameter for f(y,t,*args)"""
    d = np.array([y0]).size  ## state dimension
    y = np.zeros((n+1, d))
    y[0] = y0
    t = 0
    for k in range(n):
        y[k+1] = y[k] + f(y[k], t, *args)*dt
        t = t + dt
    return y
```
Come la spiega il docente, riga per riga:
- parametri: l'equazione da integrare, la condizione iniziale, il passo di integrazione, il numero di iterazioni ed eventuali parametri di `f`;
- righe 7-8: calcolano la dimensione dello stato e preparano l'array delle soluzioni, di $`n+1`$ righe;
- riga 9: `y[0]` riceve la condizione iniziale, il "seme" scelto da chi esegue il codice;
- `t = 0` è il contatore del tempo;
- il ciclo esegue `n` iterazioni: a ogni passo il nuovo valore è la soluzione al passo precedente più la funzione valutata in quel punto, moltiplicata per $`\Delta t`$; poi il tempo avanza di $`\Delta t`$, così che alla chiamata successiva `f` venga valutata all'istante successivo;
- alla fine si restituisce il vettore `y`.
Nel notebook la stessa funzione ha i commenti come righe `#` al posto della docstring; il corpo è identico.
## 5. Primo esempio in Python: dy/dt = a·y
`BT-01 @ 00:59:46`
Slide "Euler method in python", "Define the system we want to solve" ed "Execute the solver: initial conditions and the functions are needed":
```python
def first(y, t, a):
    """first-order linear ODE dy/dt = a*y"""
    return a*y
```
```python
dt = 0.1
n = 100
y = euler(first, 1, dt, n, 1)
plt.plot(np.arange(0,n+1)*dt, y)
plt.xlabel("t"); plt.ylabel("y(t)");
```
Si studia $`dy/dt = a\,y`$ con condizione iniziale $`y(0) = 1`$, passo 0.1, cento passi. Il risultato, un vettore di 101 valori, si visualizza con matplotlib: è una **curva di crescita** (grafico "Graphical representation of the differential equation", da 1.00 a circa 2.7 su $`t \in [0, 10]`$). Accanto: "Add some 'print' to debug the computation"; "How does the slope change when we use different values of y0 and/or alpha?"; "Colab!".
> **Correzione:** a voce e nel codice della slide $`a = 1`$, ma il grafico accanto corrisponde ad $`a = 0.1`$. Verificato per esecuzione: con $`a = 1`$ Eulero arriva a $`y(10) \approx 13\,781`$ (soluzione esatta $`e^{10} \approx 22\,026`$), con $`a = 0.1`$ a $`y(10) \approx 2.705`$ (esatta $`e \approx 2.718`$), che è la curva mostrata. Anche la demo in Colab usa $`a = 0.1`$.
### 5.1 In Colab
`BT-01 @ 01:01:31`
Il notebook contiene due esempi: questo e, più avanti, il preda-predatore risolto sia con Eulero sia con `odeint`. Il docente condivide l'accesso al notebook ed esegue le celle: import, definizione di `euler`, definizione di `first`.
Cella degli import (identica in tutti i notebook della lezione):
```python
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numba
from scipy import integrate

import random
import matplotlib.cm as cm

import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed
from IPython.display import display
```
```python
#Define the system to solve: it is a first-order linear ODE dy/dt = alpha*y
def first(y, t, alpha):
  return alpha*y
```
La prima esecuzione riproduce il grafico della slide ($`dt = 0.1`$, $`n = 100`$; dal grafico, $`\alpha = 0.1`$ e $`y_0 = 1`$: la cella non è inquadrata per intero).
`BT-01 @ 01:02:44` Confronto a parità di condizione iniziale ($`y_0 = 1`$), variando $`\alpha`$ (valori del video):
```python
#variare del grafico al variare di y
dt = 0.1 #time step
n = 100 #number of iterations
#modificando i valori di alpha la curva si appiattisce di più verso l'asse x
alpha = 0.1
y0 = 1
y = euler(first, y0 , dt, n, alpha)
y2 = euler(first, y0 , dt, n, alpha + 0.1)
y3 = euler(first, y0 , dt, n, alpha + 0.2)
#possible solution
plt.plot(np.arange(0,n+1)*dt, y)
plt.plot(np.arange(0,n+1)*dt, y2)
plt.plot(np.arange(0,n+1)*dt, y3)

plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Graphical representation of the differential equation with different y");
plt.show()
```
Passando da $`\alpha = 0.1`$ a $`0.3`$ cambia completamente il fondo scala: $`y(10)`$ va da circa 2.7 a circa 19.2 (verificato: 2.705, 7.245, 19.219).
Esercizio 1 del notebook (cella di testo): "Add some 'print' to debug how values evolve"; "How does the slope change with different y0 and alpha values?". Il docente invita a sperimentare variando passo, parametro $`a`$ e forma dell'equazione.
`BT-01 @ 01:03:52` Punto della situazione (slide "Conclusion"): "There will be more math in biology and medicine in your lifetime." "Unlike other science the math models are being discovered right now!" L'unione di matematica e biologia è recente ma costante: le nuove tecnologie generano nuovi dati e fanno capire meglio i meccanismi biologici, il che richiede nuovi modelli. Molti fenomeni e modelli restano da esplorare.
## 6. Il modello preda-predatore di Lotka-Volterra
`BT-01 @ 01:05:35`
Due modelli "capisaldo" della matematica in biologia; il primo è il **Lotka-Volterra**, della famiglia dei modelli preda-predatore: un sistema di equazioni differenziali che descrive la dinamica di due popolazioni in relazione di predazione. Lo hanno formulato Alfred Lotka e Vito Volterra; il docente sottolinea il ruolo pionieristico della scuola matematica italiana.
Slide "Let's code Lotka-Volterra!": Predator-Prey; X = hare population; Y = lynx population.
$$
\frac{dx}{dt} = a x - b x y, \qquad \frac{dy}{dt} = -c y + p x y
$$
- $`x`$: prede (lepri), $`y`$: predatori (linci).
- $`a`$: tasso di crescita delle prede in assenza di predatori; $`b`$: tasso con cui i predatori catturano le prede.
- $`p`$ (a volte $`\gamma`$): incremento dei predatori per ogni preda catturata; $`c`$: mortalità dei predatori in assenza di prede.
In assenza di predatori la popolazione delle prede cresce come $`a x`$; in loro presenza diminuisce, perché il modello **assume che le due specie interagiscano sempre**. Esistono varianti con componente spaziale: se prede e predatori sono inizialmente molto lontani, le due equazioni si comportano come disaccoppiate. Il modello si può estendere con termini di accoppiamento, per esempio una terza equazione se la preda è a sua volta predatore di un'altra specie.
`BT-01 @ 01:09:12` Comportamento: **oscillazioni periodiche** interdipendenti. Quando le prede aumentano, i predatori seguono; la crescita dei predatori porta al calo (o al collasso) delle prede, e quindi al declino dei predatori, che non si predano fra loro: il modello non cattura il cannibalismo. Il modello è semplice ma affidabile, fondamentale per le dinamiche ecologiche e la stabilità degli ecosistemi, ma idealizzato: considera solo l'interazione preda-predatore, senza malattie, migrazioni o altre specie, e le oscillazioni non rappresentano accuratamente popolazioni reali.
Il grafico della slide ("odeint method", Hare e Lynx su 30 giorni) mostra le oscillazioni delle due popolazioni, con le lepri che partono da 4.
### 6.1 Il codice
`BT-01 @ 01:11:01`
Nel notebook il modello è risolto due volte, con `odeint` e con Eulero, "a fini didattici". Impostazioni (valori del video; slide $`a, b, c, p`$ = codice `alpha`, `beta`, `delta`, `gamma`):
```python
alpha = 1. #mortality rate due to predators
beta = 1.
delta = 1.
gamma = 1.
#aumentando la quantità di linci o lepri aumenta l'intervallo di risalita
x0 = 4. #quantità iniziali di lepre
y0 = 2. #quantità iniziali di lince

#modello preda predatore
def derivative(X, t, alpha, beta, delta, gamma):
    x, y = X #x vettore che inizialmente avrà x0 e y0
    dotx = x * (alpha - beta * y) #derivata di x rispetto al tempo è dotx
    doty = y * (-delta + gamma * x)
    return np.array([dotx, doty])
```
Quattro parametri per i tassi di crescita e decrescita, condizioni iniziali di esempio (quattro lepri e due linci), e la funzione che restituisce le due derivate: `X` contiene lo stato corrente, da cui si estraggono $`x`$ e $`y`$.
> **Correzione:** il commento `#mortality rate due to predators` su `alpha` è sbagliato. In `dotx = x * (alpha - beta * y)` il parametro `alpha` è il **tasso di crescita delle prede** in assenza di predatori, come dice il docente a voce; l'effetto dei predatori sulle prede è `beta`.
Soluzione con `odeint` `BT-01 @ 01:12:11`, su 1000 istanti fra 0 e 30:
```python
Nt = 1000
tmax = 30. #tempo massimo
t = np.linspace(0.,tmax, Nt) #vettore che va da 0 a 30 gg e conterrà 1000 campionamenti
X0 = [x0, y0]
#odeint metodo di derivazione di shipy
res = integrate.odeint(derivative, X0, t, args = (alpha, beta, delta, gamma)) #funzione da integrare, vettore iniziale,
# vettore di punti nel tempo su cui fare il calcolo, e gli argomenti cioò i paramentri
x, y = res.T #trasposta di res (risultato dell'integrale)

plt.figure()
plt.grid()
plt.title("odeint method")
plt.plot(t, x, 'xb', label = 'Hare')
plt.plot(t, y, '+r', label = "Lynx")
plt.xlabel('Time t, [days]')
plt.ylabel('Population')
plt.legend()

plt.show()
```
> **Correzione:** il commento `#odeint metodo di derivazione di shipy` è impreciso: `odeint` **integra** il sistema (calcola $`x(t)`$ e $`y(t)`$ a partire dalle derivate), e la libreria è SciPy.
Verifica per esecuzione: con questi valori le due popolazioni oscillano con picchi delle lepri intorno a $`t \approx 8.2`$, $`16.6`$, $`25.0`$ e massimi di circa 4.4, come nel grafico a schermo. La quantità $`V = x - \ln x + y - \ln y`$, che per questi parametri è costante lungo le soluzioni esatte, resta 3.9206 dall'inizio alla fine: `odeint` conserva le orbite chiuse.
Il docente suggerisce, studiando, di variare le quantità iniziali e l'orizzonte temporale.
### 6.2 Effetto di un parametro: variare beta
`BT-01 @ 01:12:47`
Per quantificare l'importanza dei parametri esistono diversi metodi. Il primo è **euristico**: si fissa un intervallo di valori per un parametro e si osserva come varia il modello tenendo fermo tutto il resto.
```python
betas = np.arange(0.9, 1.4, 0.1)

nums=np.random.random((10,len(betas)))
colors = cm.rainbow(np.linspace(0, 1, nums.shape[0]))  # generate the colors for each data set

fig, ax = plt.subplots(2,1)

#ciclo for in cui cambiamo il valore di beta mantendo fissati gli altri
for beta, i in zip(betas, range(len(betas))):
    res = integrate.odeint(derivative, X0, t, args = (alpha,beta, delta, gamma))
    ax[0].plot(t, res[:,0], color = colors[i],  linestyle = '-', label = r"$\beta = $" + "{0:.2f}".format(beta))
    ax[1].plot(t, res[:,1], color = colors[i], linestyle = '-', label = r" $\beta = $" + "{0:.2f}".format(beta))
    ax[0].legend()
    ax[1].legend()

ax[0].grid()
ax[1].grid()
ax[0].set_xlabel('Time t, [days]')
ax[0].set_ylabel('Hare')
ax[1].set_xlabel('Time t, [days]')
ax[1].set_ylabel('Lynx');
```
Due grafici (lepri sopra, linci sotto) per $`\beta`$ = 0.90, 1.00, 1.10, 1.20, 1.30: all'aumentare di $`\beta`$ i picchi si spostano in avanti nel tempo, quelli delle lepri si alzano e quelli delle linci si abbassano (verificato: massimo delle lepri da 4.28 a 4.83, delle linci da 4.76 a 3.72, terzo picco delle lepri da $`t \approx 24.7`$ a $`26.2`$).
### 6.3 Il ritratto di fase
`BT-01 @ 01:13:59`
Cella di testo del notebook: "**Phase portrait** The phase portrait is a geometrical representation of the trajectories of a dynamical system in the phase space (axes corresponding to the state variables x and y). It is a tool for visualizing and analyzing the behavior of dynamic systems. Particularly, in case of oscillatory systems like Lotka-Volterra equations."
```python
#questo tipo di grafico indica che dato che ci sono delle curve chiuse il fenomeno ha delle centricità
#fondamentale per lo studio di sistemi dinamici o sistemi tempo-dipendenti
plt.figure()
IC = np.linspace(1.0, 6.0, 21) # initial conditions for deer population (prey)
for deer in IC:
    X0 = [deer, 1.0]
    Xs = integrate.odeint(derivative, X0, t, args = (alpha, beta, delta, gamma))
    plt.plot(Xs[:,0], Xs[:,1], "-", label = "$x_0 =$"+str(X0[0]))
plt.xlabel("Hare")
plt.ylabel("Lynx")
plt.legend()
plt.title("Hare vs Lynx");
```
Il grafico mette, per ogni istante, il numero di lepri contro il numero di linci, per 21 condizioni iniziali diverse ($`x_0`$ da 1.0 a 6.0, linci iniziali 1.0). Qualunque sia la condizione iniziale, la traiettoria è una **curva chiusa**: il sistema è periodico e **non caotico**. Secondo il docente, con ulteriori analisi della dinamica si arriva a identificare la classe del sistema.
> **Nota aggiunta:** il ciclo `for beta, i in zip(...)` della cella precedente lascia la variabile globale `beta` al suo ultimo valore, 1.3. Il ritratto di fase e la soluzione con Eulero che seguono sono quindi calcolati con $`\beta = 1.3`$, non con $`\beta = 1`$ come nelle impostazioni; per questo il centro delle orbite a schermo è a $`y \approx 0.77`$ ($`= \alpha/\beta`$) invece che a 1. La verifica per esecuzione riproduce i grafici a schermo solo con $`\beta = 1.3`$. È un effetto tipico dei notebook, dove l'ordine di esecuzione delle celle cambia lo stato.
### 6.4 Soluzione con Eulero
`BT-01 @ 01:15:02`
```python
def Euler(func, X0, t, alpha, beta, delta, gamma):
    """
    Euler solver.
    """
    dt = t[1] - t[0]
    nt = len(t)
    X  = np.zeros([nt, len(X0)])
    X[0] = X0
    for i in range(nt-1):
        X[i+1] = X[i] + func(X[i], t[i], alpha,  beta, delta, gamma) * dt
    return X
```
Rispetto a `euler` della sezione 4.4, questa versione riceve direttamente il vettore dei tempi `t` e ne ricava passo e numero di iterazioni.
```python
Xe = Euler(derivative, X0, t, alpha, beta, delta, gamma)
plt.figure()
plt.title("Euler method")
plt.plot(t, Xe[:, 0], 'xb', label = 'Hare')
plt.plot(t, Xe[:, 1], '+r', label = "Lynx")
plt.grid()
plt.xlabel("Time, $t$ [s]")
plt.ylabel('Population')
plt.ylim([0.,3.])
plt.legend(loc = "best")

plt.show()
```
```python
plt.figure()
plt.plot(Xe[:, 0], Xe[:, 1], "-")
plt.xlabel("Hare")
plt.ylabel("Lynx")
plt.grid()
plt.title("Phase plane : Hare vs Lynx (Euler)");
```
> **Nota aggiunta:** anche `X0` viene dal ciclo del ritratto di fase, che lo lascia a `[6.0, 1.0]`: la soluzione con Eulero a schermo parte da 6 lepri e 1 lince, non da 4 e 2.
Il docente fa il diagramma di fase anche della soluzione con Eulero e conclude che "anche questo è un sistema chiuso", a conferma di aver identificato correttamente la classe del sistema.
> **Correzione:** il ritratto di fase ottenuto con Eulero a schermo **non è chiuso**: è una spirale che si allarga a ogni giro (massimi delle lepri circa 7.1 e poi 8.6, delle linci 4.8, 5.7, 7.0). Verificato per esecuzione: partendo da (6, 1) con $`\beta = 1.3`$ si ottengono esattamente questi massimi, e la quantità che il sistema esatto conserva, $`V = x - \ln x + \beta y - \ln y`$, cresce da 5.51 a 8.84 in 30 giorni, mentre con `odeint` resta 5.51. Il sistema è periodico; la spirale è l'**errore numerico** di Eulero esplicito, che su orbite chiuse accumula energia a ogni ciclo. È esattamente il limite di precisione di cui il docente parla alla sezione 4.3, e il confronto fra i due grafici è la risposta al primo punto dell'Esercizio 2.
## 7. Esercizi e sensitivity analysis
`BT-01 @ 01:15:02`
Cella di testo del notebook, "Exercise 2":
- "Draw comparisons between the two methods: odeint vs Euler"
- "Change the parameters, observe and document the results."
- "Perform sensitivity analysis with the Saltelli Lib (SALIB) library" (link a `salib.readthedocs.io`)
Il docente non si aspetta che gli esercizi gli vengano inviati, ma li consiglia perché **aiutano ad affrontare la prova finale**.
`BT-01 @ 01:15:37` Sull'ultimo punto: la **sensitivity analysis** permette di identificare e quantificare l'importanza dei parametri di un modello. Il Lotka-Volterra ha quattro parametri: sono tutti ugualmente importanti o qualcuno conta più degli altri? La libreria **SALib** implementa diversi metodi di sensitivity analysis ed è ben documentata; il tema va oltre il corso, ma secondo il docente chi vuole costruire o studiare modelli non può farne a meno.
Esempio mostrato dalla documentazione di SALib ("Another Example"), la parabola:
$$
f(x) = a + b x^2
$$
"The parameters a and b will be subject to the sensitivity analysis, but x will be not." La pagina mostra la media di $`y`$ con l'intervallo di previsione al 95% e gli indici di Sobol del primo ordine di $`a`$ e $`b`$ in funzione di $`x`$. Lettura: a $`x = 0`$ la variabilità di $`y`$ è spiegata al 100% da $`a`$, perché il contributo di $`b x^2`$ si annulla; al crescere di $`|x|`$ cresce il peso di $`b`$ e diminuisce quello di $`a`$. La sensitivity analysis quantifica come piccole oscillazioni dello spazio degli input, dei parametri o di entrambi si ripercuotono sull'output.
`BT-01 @ 01:18:59` Sull'esame: **la sensitivity analysis non sarà argomento pratico d'esame**, perché non viene trattata in modo estensivo; ci potrebbe però essere una domanda su come si studia e si caratterizza un modello. Nel notebook ci sono i diagrammi di fase e altri strumenti; una domanda possibile è come quantificare l'importanza dei parametri.
## 8. Modelli compartimentali: il SIR
`BT-01 @ 01:19:30`
Un modello che completa il primissimo modello di diffusione di un'epidemia visto a inizio lezione. In epidemiologia si usano i **modelli compartimentali**: dividono la popolazione in gruppi distinti (**compartimenti**), ciascuno corrispondente a uno stato della malattia. Il modello base è il **SIR**.
Slide "SIR the first compartmental model":
- **S**usceptibles S: individui che possono contrarre la malattia
- **I**nfected I: attualmente infetti, capaci di trasmetterla
- **R**ecovered R: guariti e immuni; in questa versione **non possono reinfettarsi**
$$
\frac{ds}{dt} = -b\,s(t)\,i(t), \qquad \frac{di}{dt} = b\,s(t)\,i(t) - k\,i(t), \qquad \frac{dr}{dt} = k\,i(t)
$$
Grafico: $`s(t)`$ scende da 1 a circa 0.42, $`r(t)`$ sale fino a circa 0.58, $`i(t)`$ ha un piccolo picco intorno al giorno 75, su 150 giorni.
Tre equazioni per tre popolazioni che si influenzano: i suscettibili diminuiscono all'aumentare degli infetti, perché chi si infetta viene tolto dai suscettibili e aggiunto agli infetti; lo stesso "travaso" avviene fra infetti e guariti. Per questo si dice che il SIR rappresenta il **flusso di individui fra compartimenti** nel tempo.
`BT-01 @ 01:22:12` L'andamento si studia tramite il **numero di riproduzione di base **$`R_0`$, il numero medio di nuovi casi generati da ogni infetto: se $`R_0 > 1`$ la malattia tende a diffondersi, se $`R_0 < 1`$ la diffusione rallenta. Il SIR serve a prevedere le epidemie, stimare quando si raggiungerà il **picco di infezione** e aiutare i decisori a ideare strategie di contenimento.
> **Nota aggiunta:** con la notazione della slide, e popolazioni normalizzate, $`R_0 = b\,s(0)/k`$: il rapporto fra il tasso di contagio e quello di guarigione.
L'espansione più naturale è il **SEIR**, che aggiunge il compartimento degli **esposti** fra suscettibili e infetti. Il docente lo motiva così: per non assumere una relazione uno a uno fra suscettibile e infetto, perché non tutti quelli che entrano in contatto con un malato si ammalano (per esempio per immunità innata).
> **Correzione:** nel SEIR il compartimento E (esposti) contiene individui **già infettati ma non ancora contagiosi**, nel periodo di latenza; tutti passano poi a I con un certo tasso. Chi entra in contatto con un malato senza infettarsi resta fra i suscettibili: questo aspetto è già nel tasso di contagio, non nel compartimento E.
## 9. L'invasione degli zombie
`BT-01 @ 01:24:34`
I modelli compartimentali non servono solo per le patologie. In letteratura, per rendere l'apprendimento più coinvolgente, si usa lo stesso schema per un'**invasione di zombie**: la matematica è la stessa, cambia l'interpretazione.
Slide "Let's code the zombie invasion model: a compartmental model". Schema: Π → Susceptible; Susceptible → Zombie ($`\beta ZS`$); Zombie → Removed ($`\alpha SZ`$); Removed → Zombie ($`\zeta R`$); Susceptible → Removed ($`\delta S`$).
$$
\frac{dS}{dt} = \Pi - \beta S Z - \delta S, \qquad \frac{dZ}{dt} = \beta S Z + \zeta R - \alpha Z S, \qquad \frac{dR}{dt} = \delta S + \alpha Z S - \zeta R
$$
$$
X = \begin{pmatrix} S \\ Z \\ R \end{pmatrix}, \qquad \dot{X} = \begin{pmatrix} \Pi - \beta S Z - \delta S \\ \beta S Z + \zeta R - \alpha Z S \\ \delta S + \alpha Z S - \zeta R \end{pmatrix} = F(X)
$$
- Π: birth rate (assumed constant)
- δ: natural mortality rate
- ζ: resurrection rate into zombie after death
- β: rate of becoming a zombie after contact with a zombie Z
- α: total destruction rate of a zombie \[illeggibile, riga tagliata dal bordo dello schermo; testo ricostruito dal commento `#destruction rate` del notebook\]
> **Correzione:** a voce il docente descrive il terzo compartimento come quelli "infettati dagli zombie che poi, grazie a qualche magia, ritornano sani". Nel modello R sono i **rimossi**: morti per cause naturali ($`\delta S`$) e zombie distrutti ($`\alpha Z S`$); il flusso $`\zeta R`$ li riporta in vita **come zombie**, non come sani ("resurrection rate into zombie after death").
### 9.1 Il codice
`BT-01 @ 01:25:33`
Il notebook `Zombie_invasion.ipynb` (a schermo "Data ultima modifica: 8 novembre") coincide con quello distribuito.
```python
!pip install SALib
```
Segue la stessa cella di import dei notebook precedenti, con in più una seconda riga `from scipy import integrate`.
"Numerical values for SIR-based apocalypse zombie":
```python
Pi =  0. #birth rate
delta = 1.e-4 #natural death rate
beta = 9.5e-3 #contact rate
zeta = 1.e-4 #resurrection rate
alpha = 1.e-4 #destruction rate

S0 = 1000 #initial population
Z0, R0 = 0, 0
X0 = S0, Z0, R0
tmax = 10
Nt = 160
t = np.linspace(0, tmax, Nt+1) #time grid
```
"Coding the model":
```python
def derivative(X, t, Pi, delta, beta, zeta, alpha):
    S, Z, R = X
    dotS = Pi - beta * S * Z - delta * S
    dotZ = beta * S * Z + zeta * R - alpha * Z * S
    dotR = delta * S + alpha * Z * S - zeta * R
    return np.array([dotS, dotZ, dotR])
```
Si definisce il sistema per le tre popolazioni e lo si integra, con `odeint` e con Eulero. Più equazioni e più parametri: il docente invita a giocare con i parametri e osservare quanto rapidamente cambiano le curve; ci sono situazioni limite in cui, per esempio, la popolazione non si riprende mai.
```python
#questa volta ho 3 curve non 2 come nel caso della lince e lepre
#ho la seria temporale per le persone non zombee, gli zombee e quelle che recuperano uscendo dallo stadio zombee
X = integrate.odeint(derivative, X0, t, args = (Pi, delta, beta, zeta, alpha))
S, Z, R = X.T #X.T order 3 x (Nt+1)

plt.figure()
plt.grid()
plt.title("SIR model")
plt.plot(t, S, 'orange', label='Susceptible')
plt.plot(t, Z, 'r', label='Zombie')
plt.plot(t, R, 'g', label='Removed')
plt.xlabel('Time t, [days]')
plt.ylabel('Population')
plt.legend()

plt.show();
```
> **Nota aggiunta:** con $`Z_0 = R_0 = 0`$ gli zombie compaiono lo stesso: la mortalità naturale $`\delta S`$ alimenta R e la resurrezione $`\zeta R`$ alimenta Z, poi il contagio $`\beta S Z`$ fa il resto. Verificato per esecuzione: gli zombie superano i suscettibili intorno a $`t \approx 2.4`$ giorni e a $`t = 10`$ sono circa 989 su 1000.
"Testing with different initial conditions":
```python
R0 = 0.01 * S0
X0 = S0, Z0, R0
Pi = 8
X = integrate.odeint(derivative, X0, t, args =(Pi, delta, beta, zeta, alpha))
S, Z, R = X.T #X.T order 3 x (Nt+1)

plt.figure()
plt.grid()
plt.title("Zombie model")
plt.plot(t, S, 'orange', label='Susceptible')
plt.plot(t, Z, 'r', label='Zombie')
plt.plot(t, R, 'g', label='Removed')
plt.xlabel('Time t, [days]')
plt.ylabel('Population')
plt.legend()

plt.show();
```
"Solve with Euler":
```python
def Euler(func, X0, t, Pi, delta, beta, zeta, alpha):
    """
    Euler solver.
    """
    dt = t[1] - t[0]
    nt = len(t)
    X  = np.zeros([nt, len(X0)])
    X[0] = X0
    for i in range(nt-1):
        X[i+1] = X[i] + func(X[i], t[i], Pi, delta, beta, zeta, alpha) * dt
    return X
```
```python
Xe = Euler(derivative, X0, t, Pi, delta, beta, zeta, alpha)

plt.figure()
plt.grid()
plt.title("Zombie model with explicit Euler")
plt.plot(t, Xe[:,0], 'orange', label='Susceptible')
plt.plot(t, Xe[:,1], 'r', label='Zombie')
plt.plot(t, Xe[:,2], 'g', label='Removed')
plt.xlabel('Time t, [days]')
plt.ylabel('Population')
plt.legend()
```
`R0` qui è la condizione iniziale dei rimossi, non il numero di riproduzione di base.
### 9.2 Bonus: SALib
`BT-01 @ 01:26:11`
La "bonus track" è un esempio d'uso di SALib, sulla funzione di test di Ishigami:
```python
from SALib.sample import saltelli
from SALib.analyze import sobol
from SALib.test_functions import Ishigami
import numpy as np

# Define the model inputs
# il prblema ha 3 variabili le x sono le var da studiare.
# bounds sono li estremi dei vettori
problem = {
    'num_vars': 3,
    'names': ['x1', 'x2', 'x3'],
    'bounds': [[-3.14159265359, 3.14159265359],
               [-3.14159265359, 3.14159265359],
               [-3.14159265359, 3.14159265359]]
}

# Generate samples: 1024 campionamenti per le 3 variaibli
param_values = saltelli.sample(problem, 1024)

# Run model (example): chiediamo valutazione di yshiami passando vettore di vettori
Y = Ishigami.evaluate(param_values)

# Perform analysis
Si = sobol.analyze(problem, Y, print_to_console=True)

# Print the first-order sensitivity indices
print(Si['S1'])
```
A lezione la cella fallisce con `ModuleNotFoundError: No module named 'SALib'`, perché la cella `!pip install SALib` non era stata eseguita; il docente dice di averla aggiunta nella nuova versione del notebook, così l'errore non si ripresenta.
Verificato per esecuzione (SALib installato): indici del primo ordine S1 ≈ 0.317, 0.444, 0.012 e totali ST ≈ 0.556, 0.442, 0.245, come nell'output salvato nel notebook. $`x_3`$ ha effetto quasi nullo da solo ma un indice totale di 0.245: agisce solo in interazione con $`x_1`$ (S2 per la coppia $`x_1, x_3`$ ≈ 0.24 nell'output del notebook).
> **Nota aggiunta:** `1024` è il numero base $`N`$ di campioni; lo schema di Saltelli con indici del secondo ordine genera $`N(2D+2) = 1024 \cdot 8 = 8192`$ valutazioni del modello (verificato: `param_values.shape` = `(8192, 3)`). Nelle versioni recenti di SALib `saltelli.sample` è deprecato a favore di `SALib.sample.sobol` (lo segnala un warning nell'output del notebook).
## 10. Esercizio finale
`BT-01 @ 01:26:43`
Ultima slide, "Exercises: pick one model among LK or zombie and":
- Draw comparisons between the two methods: odeint vs Euler
- Change the parameters, observe and document the results.
- Automatize by sensitivity analysis with the Saltelli lib
"Assignment ([https://salib.readthedocs.io/en/latest/user_guide/getting-started.html#installing-salib](https://salib.readthedocs.io/en/latest/user_guide/getting-started.html#installing-salib)) – hint for colab use `!pip install SALib` and not `pip install SALib`"
Non è obbligatorio. Si può partire dal codice fornito e arricchirlo con la sensitivity analysis, ma quest'ultima parte non è fondamentale: per il docente conta che si impari a usare `odeint` e l'integrazione con Eulero.
## 11. Collegamento con il test finale
<table header-row="true">
<tr>
<td>Test finale 2026</td>
<td>Dove nel capitolo</td>
</tr>
<tr>
<td>T2: definizione di ODE</td>
<td>sezioni 3 e 4 (tabella dei tipi di modello, definizione del metodo di Eulero)</td>
</tr>
<tr>
<td>T4: quando usare ODE e quando ABMS</td>
<td>sezione 3 (le ODE modellano l'evoluzione nel tempo di quantità aggregate); il confronto con gli ABMS è nel capitolo 02</td>
</tr>
<tr>
<td>T5-T6: epidemiologia computazionale</td>
<td>sezioni 2.1 e 8 (logistica, SIR, $`R_0`$, SEIR); il resto nel capitolo 04</td>
</tr>
<tr>
<td>Esercizio pratico 2: Gompertz con Eulero o `odeint`</td>
<td>sezioni 4.4, 5 e 6: la funzione `euler` e il pattern `derivative`  • `integrate.odeint` si applicano direttamente a $`dT/dt = r\,T \ln(K/T)`$</td>
</tr>
<tr>
<td>Domanda possibile: come caratterizzare un modello</td>
<td>sezioni 6.2, 6.3 e 7 (variazione euristica dei parametri, ritratto di fase, sensitivity analysis)</td>
</tr>
</table>
## 12. Glossario, punti incerti, materiale usato
### Glossario
- **Sistema complesso:** sistema di molti agenti in interazione il cui comportamento globale non si deduce da quello del singolo.
- **ODE (equazione differenziale ordinaria):** equazione che lega una funzione di una sola variabile (qui il tempo) alle sue derivate.
- **PDE (equazione differenziale alle derivate parziali):** come sopra, con più variabili indipendenti (tempo e spazio).
- **Orizzonte temporale:** intervallo di tempo su cui si integra.
- **Metodo di Eulero (esplicito):** $`y_{k+1} = y_k + f(y_k, t_k)\,\Delta t`$.
- **`odeint`****:** integratore di ODE di `scipy.integrate`.
- **Ritratto (diagramma) di fase:** traiettorie del sistema nello spazio delle variabili di stato.
- **Sensitivity analysis:** quantificazione dell'effetto dei parametri o degli input sull'output; indici di Sobol del primo ordine (S1) e totali (ST).
- **Modello compartimentale:** modello che divide la popolazione in compartimenti e ne descrive i flussi.
- $`R_0`$**:** numero medio di nuovi casi generati da un infetto in una popolazione interamente suscettibile.
- **Curva logistica, punto di flesso:** crescita che satura; il flesso è il punto di massima velocità di crescita.
### Punti incerti e nomi corretti
- Nome del progetto europeo sul diabete: "Presidium", confermato in `Teams 2 @ 1:25:08`.
- `[?]` ricercatori citati per le neuroscienze (San Raffaele, Barcellona), `BT-01 @ 00:10:24`.
- `[?]` autori della prima formalizzazione della striscia primitiva, 1991, `BT-01 @ 00:33:37`.
- `[illeggibile]` definizione di α nella slide zombie, riga tagliata, `BT-01 @ 01:25:29`.
- Nomi trascritti male e corretti nel testo: Biosentis → Biocentis; Hoffield, opfield → Hopfield; "modello di qual meno... in asli" → Hodgkin-Huxley; "gastrula azione" → gastrulazione; "o dint", "ODE e INT", "the int" → `odeint`; "eurero" → Eulero; "rung cut" → Runge-Kutta; "lot cavol terra", "lott cover terra" → Lotka-Volterra; "Saltelli Lib", "Saltelli" → SALib; "foglie", "soglia", "le pesce" → sogliole.
### Materiale usato
- `Materiale/Portale/Math_in_biology.pdf` (identico a `Materiale/Teams/II lezione/Math_in_biology.pdf`)
- `Materiale/Teams/colab/Lotka_Volterra.ipynb` (funzioni; parametri presi dal video, vedi Divergenze)
- `Materiale/Teams/colab/Zombie_invasion.ipynb`
- Pagina `scipy.integrate.odeint` (SciPy 1.14.1) e SALib "Basics", mostrate a schermo
- Registrazioni `Teams 1`, `Teams 2` e `Teams 3` fino a 0:31 (18-20/05/2026), trascrizione Stream; notebook `01`-`04` del canale Teams
## 13. Integrazione Teams 2026: i quattro casi di studio
`Teams 2 @ 0:00:27`
Nell'edizione 2026 la lezione 2 (19/05/2026) completa i quattro casi di studio introdotti nella lezione 1 (capitolo 00, sezione 7) e poi riprende le slide "Mathematics in Biology" di questo capitolo. I notebook sono sul canale Teams del corso. Il codice qui sotto è preso dai notebook; il commento è quello del docente in aula, riassunto.
### 13.1 Crescita batterica con Eulero (`01_eulero_crescita_batterica.ipynb`)
`Teams 1 @ 1:12:17`
Metodo di Eulero generico per una ODE scalare, con il vettore dei tempi come input (a differenza di `euler` della sezione 4.4, che riceve passo e numero di iterazioni):
```python
def eulero_esplicito(f, y0, t):
    """
    Metodo di Eulero esplicito per una ODE del tipo dy/dt = f(y, t).

    Parametri
    ---------
    f  : funzione che restituisce dy/dt
    y0 : valore iniziale
    t  : array dei tempi

    Ritorna
    -------
    y : array con la soluzione approssimata
    """
    y = np.zeros(len(t))      # vettore soluzione
    y[0] = y0                # condizione iniziale

    for i in range(len(t) - 1):
        dt = t[i+1] - t[i]   # passo temporale
        y[i+1] = y[i] + dt * f(y[i], t[i])

    return y
```
Crescita esponenziale $`dN/dt = rN`$ confrontata con la soluzione analitica $`N_0 e^{rt}`$:
```python
# Parametri biologici
N0 = 1e5      # cellule/mL iniziali
r = 0.8       # 1/h, tasso di crescita
T = 8         # ore totali

# Griglia temporale
# Prova poi a cambiare dt in 1.0, 0.5, 0.1 e osserva l'errore.
dt = 0.25
t = np.arange(0, T + dt, dt)

# Definizione della ODE
def crescita_esponenziale(N, t):
    return r * N

# Soluzione numerica con Eulero
N_euler = eulero_esplicito(crescita_esponenziale, N0, t)

# Soluzione analitica esatta
N_esatta = N0 * np.exp(r * t)

plt.plot(t, N_euler, 'o-', label='Eulero')
plt.plot(t, N_esatta, '-', label='Soluzione analitica')
plt.xlabel('Tempo [h]')
plt.ylabel('Cellule/mL')
plt.title('Crescita esponenziale batterica')
plt.legend()
plt.show()

errore_finale = abs(N_euler[-1] - N_esatta[-1]) / N_esatta[-1] * 100
print(f"Errore relativo finale: {errore_finale:.2f}%")
```
Verificato per esecuzione: errore relativo finale **43.20%** con $`\Delta t = 0.25`$ h. È un errore grande perché $`r\,\Delta t = 0.2`$ non è piccolo: Eulero moltiplica a ogni passo per $`1 + r\Delta t = 1.2`$, mentre la soluzione esatta per $`e^{0.2} \approx 1.221`$.
Crescita logistica $`dN/dt = rN(1 - N/K)`$ con $`N_0 = 10^5`$, $`r = 0.9`$ h⁻¹, $`K = 10^9`$ cellule/mL, 24 ore a $`\Delta t = 0.1`$:
```python
def crescita_logistica(N, t):
    return r * N * (1 - N / K)

N_log = eulero_esplicito(crescita_logistica, N0, t)
```
Verificato: valore finale $`1.00 \cdot 10^9`$ cellule/mL, cioè la capacità $`K`$.
Domande guidate del notebook: cosa succede con $`\Delta t`$ = 2 ore; perché Eulero può diventare instabile; quale passo usare per una crescita molto rapida. Mini-progetto: aggiungere una fase di morte cellulare dopo 16 ore.
> **Nota aggiunta:** questo notebook è quello che il docente indica come riferimento per l'esercizio di Gompertz del test finale (`Teams 6 @ 1:13:48`): basta sostituire la funzione con `r * T * np.log(K / T)`.
### 13.2 Bioreattore batch, Eulero contro odeint (`02_eulero_vs_odeint_bioreattore_batch.ipynb`)
`Teams 2 @ 0:06:54`
Cinetica di Monod: $`\mu(S) = \mu_{max}\,S/(K_s + S)`$, con $`dX/dt = \mu(S)X`$ e $`dS/dt = -\frac{1}{Y_{X/S}}\mu(S)X`$. Biomassa $`X`$ e glucosio $`S`$ in g/L.
```python
def eulero_sistema(f, y0, t, params):
    """
    Metodo di Eulero per sistemi di ODE.
    y0 può contenere più variabili, ad esempio [X0, S0].
    """
    y = np.zeros((len(t), len(y0)))
    y[0, :] = y0

    for i in range(len(t) - 1):
        dt = t[i+1] - t[i]
        y[i+1, :] = y[i, :] + dt * np.array(f(y[i, :], t[i], params))

        # Vincolo biologico: substrato e biomassa non possono diventare negativi
        y[i+1, :] = np.maximum(y[i+1, :], 0)

    return y
```
```python
params = {
    'mu_max': 0.55,  # 1/h
    'Ks': 0.2,       # g/L
    'Yxs': 0.45      # g biomassa / g substrato
}

y0 = [0.05, 20.0]   # X0, S0
T = 30              # ore
dt = 0.1
t = np.arange(0, T + dt, dt)

def bioreattore_batch(y, t, p):
    X, S = y
    mu = p['mu_max'] * S / (p['Ks'] + S + 1e-12)
    dXdt = mu * X
    dSdt = -(1 / p['Yxs']) * mu * X
    return [dXdt, dSdt]

sol_euler = eulero_sistema(bioreattore_batch, y0, t, params)
X_e, S_e = sol_euler[:, 0], sol_euler[:, 1]

# odeint richiede una funzione con firma f(y, t, params)
sol_odeint = odeint(bioreattore_batch, y0, t, args=(params,))
X_o, S_o = sol_odeint[:, 0], sol_odeint[:, 1]
```
Il docente commenta la firma `f(y, t, p)`: `y` è il vettore dello stato, per convenzione la variabile da integrare, inizializzata con `y0`; `t` lo spazio dei tempi; `p` il dizionario dei parametri (`Teams 2 @ 0:12:23`). Il substrato cala perché viene consumato, la biomassa cresce. Il sistema è ideale: nessuno scambio con l'esterno e nessuna perdita.
Poi l'effetto del passo: lo stesso sistema integrato con $`\Delta t`$ = 1, 0.5, 0.25, 0.1, 0.05 e confronto dell'errore **finale** su $`X`$ fra Eulero e `odeint` (cella "Esercizio 2"). Output verificato:
<table header-row="true">
<tr>
<td>dt \[h\]</td>
<td>errore finale su X \[g/L\]</td>
</tr>
<tr>
<td>1.0</td>
<td>0.0565</td>
</tr>
<tr>
<td>0.5</td>
<td>0.7071</td>
</tr>
<tr>
<td>0.25</td>
<td>0.0779</td>
</tr>
<tr>
<td>0.1</td>
<td>0.0959</td>
</tr>
<tr>
<td>0.05</td>
<td>0.0226</td>
</tr>
</table>
Il docente legge il grafico così: l'errore è massimo intorno a 0.5, e "tanto più sono fitti i punti di osservazione, tanto più il sistema aumenta la sua instabilità" (`Teams 2 @ 0:17:52`); aumentando il passo a 1 "ci aspettiamo che i sistemi ritornino a coincidere" (`Teams 2 @ 0:19:36`). Su domanda di uno studente conferma che l'instabilità si presenterebbe quando $`\Delta t`$ scende sotto una soglia (`Teams 2 @ 0:22:07`).
> **Correzione:** per Eulero esplicito vale il contrario: l'errore **diminuisce** al diminuire del passo (è un metodo del primo ordine). Il grafico del notebook inganna perché misura l'errore solo all'**ultimo istante**, $`t = 30`$ h, quando il substrato è esaurito e tutte e due le soluzioni sono ferme vicino allo stesso valore di equilibrio, $`X_0 + Y_{X/S} S_0 = 9.05`$ g/L. Verificato: l'errore **massimo** lungo la traiettoria cala in modo regolare con il passo (5.20, 3.75, 2.25, 0.99, 0.51 g/L per dt = 1, 0.5, 0.25, 0.1, 0.05). Le differenze residue all'istante finale vengono dal vincolo `np.maximum(..., 0)`: quando Eulero porta $`S`$ sotto zero, lo riporta a zero, e così crea un po' di substrato dal nulla (verificato: $`X`$ finale con Eulero fra 9.07 e 9.76, sempre sopra 9.05).
Domande del notebook (`Teams 2 @ 0:20:38`): in quale intervallo la biomassa cresce più velocemente; quando si esaurisce il substrato; perché `odeint` è più comodo per sistemi accoppiati e potenzialmente rigidi. Il docente suggerisce una risposta parziale: `odeint` passa i parametri in modo agnostico rispetto al loro numero (`Teams 2 @ 0:21:04`). Mini-progetto: aggiungere il prodotto $`dP/dt = \alpha\,\mu X`$.
> **Nota aggiunta:** la risposta principale alla terza domanda è che `odeint` ha **passo adattivo** e passa automaticamente a un metodo per problemi stiff (LSODA), mentre Eulero a passo fisso diventa instabile se il passo supera il limite imposto dalla dinamica più rapida. Il docente lo dice a fine lezione, rispondendo a uno studente: `odeint` usa il vettore dei tempi solo come punti in cui restituire la soluzione e sceglie da sé il passo interno per contenere l'errore (`Teams 2 @ 0:46:37`).
### 13.3 Farmacodinamica con odeint (`03_odeint_farmacodinamica_biotech.ipynb`)
`Teams 2 @ 0:21:59`
Popolazione cellulare (tumorale o microbica) trattata con un farmaco: crescita logistica, uccisione dose-dipendente, decadimento del farmaco.
$$
\frac{dN}{dt} = rN\left(1-\frac{N}{K}\right) - k_{kill}\frac{C}{EC_{50}+C}N, \qquad \frac{dC}{dt} = -k_{deg}C
$$
```python
params = {
    'r': 0.04,        # 1/h, crescita cellulare
    'K': 1e7,         # cellule, carrying capacity
    'k_kill': 0.20,   # 1/h, massimo effetto di killing
    'EC50': 2.0,      # uM, concentrazione a metà effetto
    'k_deg': 0.03     # 1/h, degradazione del farmaco
}

N0 = 1e5
T = 120
t = np.linspace(0, T, 600)

def modello_farmaco(y, t, p):
    N, C = y
    effetto = C / (p['EC50'] + C + 1e-12)
    dNdt = p['r'] * N * (1 - N / p['K']) - p['k_kill'] * effetto * N
    dCdt = -p['k_deg'] * C
    return [dNdt, dCdt]
```
Esperimenti del notebook: dosi iniziali 0, 0.5, 2, 5, 10 µM con asse $`y`$ logaritmico; area sotto la curva (AUC) delle cellule vive con la regola dei trapezi, "minore AUC = maggiore efficacia"; dosi ripetute ogni 24 ore, gestite come eventi discreti fra un'integrazione e la successiva:
```python
def simula_dosi_ripetute(dose, intervallo=24, n_dosi=5, T=120):
    tempi_totali = []
    stati_totali = []

    stato = np.array([N0, 0.0])
    t_inizio = 0

    for j in range(n_dosi):
        # somministrazione istantanea
        stato[1] += dose

        t_fine = min(t_inizio + intervallo, T)
        t_segmento = np.linspace(t_inizio, t_fine, 100)
        sol = odeint(modello_farmaco, stato, t_segmento, args=(params,))

        tempi_totali.extend(t_segmento)
        stati_totali.extend(sol)

        stato = sol[-1, :]
        t_inizio = t_fine

    return np.array(tempi_totali), np.array(stati_totali)
```
Commento del docente: con tutte le dosi da 0.5 a 10 µM le cellule vive calano ma poi **ricominciano a crescere**, perché il farmaco degrada; una singola somministrazione non basta, come nella pratica (antipiretici ogni 6-8 ore). Con cinque dosi ogni 24 ore la concentrazione si accumula e le cellule calano di più (`Teams 2 @ 0:27:06`, `0:33:16`). Sulla domanda "a parità di dose totale, meglio una dose singola o dosi ripetute?" il docente osserva che nella pratica è incompleta: servirebbero effetti indesiderati e costi-benefici, che il modello ideale ignora (`Teams 2 @ 0:35:12`).
> **Nota aggiunta:** la cella dell'AUC usa `np.trapz`, deprecata in NumPy 2.0 e assente nelle versioni recenti (verificato: `AttributeError` con NumPy 2.4). In quel caso si usa `np.trapezoid`, che ha la stessa firma.
### 13.4 Fed-batch e proteina ricombinante (`04_odeint_fed_batch_proteina_ricombinante.ipynb`)
`Teams 2 @ 0:37:18`
Quattro variabili: biomassa $`X`$, substrato $`S`$, prodotto $`P`$ (g/L) e volume $`V`$ (L). L'alimentazione porta substrato concentrato e aumenta il volume, diluendo le concentrazioni.
```python
params = {
    'mu_max': 0.45,   # 1/h
    'Ks': 0.1,        # g/L
    'Yxs': 0.5,       # gX/gS
    'alpha': 0.08,    # gP/gX, produzione associata alla crescita
    'beta': 0.002,    # gP/(gX h), produzione non associata alla crescita
    'Sf': 300.0,      # g/L, substrato nel feed
    'F0': 0.03,       # L/h, flusso base
    't_feed': 8.0,    # h, inizio alimentazione
    't_ind': 12.0     # h, induzione produzione
}

def feed_rate(t, p):
    """Flusso di alimentazione: nullo prima di t_feed, poi costante."""
    return p['F0'] if t >= p['t_feed'] else 0.0

def induzione(t, p):
    """Fattore di induzione: 0 prima di t_ind, 1 dopo t_ind."""
    return 1.0 if t >= p['t_ind'] else 0.0

def fed_batch(y, t, p):
    X, S, P, V = y
    F = feed_rate(t, p)
    D = F / max(V, 1e-12)  # tasso di diluizione

    mu = p['mu_max'] * S / (p['Ks'] + S + 1e-12)
    I = induzione(t, p)

    dXdt = mu * X - D * X
    dSdt = D * (p['Sf'] - S) - (1 / p['Yxs']) * mu * X
    dPdt = I * (p['alpha'] * mu * X + p['beta'] * X) - D * P
    dVdt = F

    return [dXdt, dSdt, dPdt, dVdt]
```
Simulazione con `odeint` su 40 ore (800 punti), $`y_0 = (0.1, 20, 0, 1)`$. Verificato: prodotto finale 8.012 g/L, volume finale 1.960 L, prodotto totale 15.704 g. Il docente osserva che, rispetto ai casi precedenti, ci sono più punti di discontinuità (inizio del feed e dell'induzione) e che dopo circa 12 ore la crescita della biomassa rallenta (`Teams 2 @ 0:39:53`).
Screening del tempo di induzione su 6, 8, 10, 12, 16, 20, 24 ore: verificato, il massimo del prodotto totale è a **6 h** (17.394 g).
> **Correzione:** il docente dice che il volume "è proporzionale alla presenza di biomassa e prodotto" (`Teams 2 @ 0:41:01`). Nel modello $`dV/dt = F`$: il volume dipende solo dal flusso di alimentazione, costante a 1 L fino a $`t_{feed} = 8`$ h e poi crescente in modo lineare (da 1 a 1.96 L).
> **Correzione:** il docente legge il risultato dello screening come "introdurre il feed e aggiungere substrato a sei ore" (`Teams 2 @ 0:41:30`). Lo screening varia `t_ind`, il **tempo di induzione** della produzione, non l'inizio del feed (fisso a 8 h). Inoltre 6 h è il **primo valore** della griglia: verificato, anticipando l'induzione a 4 h si ottengono 17.467 g e a 2 h 17.497 g. Con questi parametri il prodotto totale cresce anticipando l'induzione, e l'ottimo non è dentro l'intervallo esplorato.
Confronto finale con Eulero a passi 0.5, 0.2, 0.05 h: tutte le curve di Eulero si discostano da `odeint` ed "esplodono"; il docente lo attribuisce alla non linearità del sistema dopo circa 12 ore (`Teams 2 @ 0:43:05`).
> **Nota aggiunta:** verificato per esecuzione, l'esplosione è anche un **errore di conservazione della massa**. Con $`K_s = 0.1`$ g/L, quando il substrato è quasi esaurito la dinamica di $`S`$ è molto rapida (problema stiff): Eulero porta $`S`$ sotto zero, `np.maximum` lo riporta a zero e così crea substrato dal nulla a ogni passo. A 40 ore Eulero dà $`X`$ = 3207, 3420, 1468 g/L per dt = 0.5, 0.2, 0.05, e ancora 166 g/L con dt = 0.01, mentre `odeint` dà 78.6 g/L. Il valore di `odeint` è coerente col bilancio di massa: $`(20 + 0.03 \cdot 32 \cdot 300) \cdot 0.5 / 1.96 \approx 78.6`$ g/L.
Domande del notebook: quale tempo di induzione massimizza il prodotto; cosa succede aumentando `F0`; perché il volume è una variabile di stato e non un parametro; quale metodo usare con molte variabili e parametri incerti. Mini-progetto: heatmap del prodotto totale al variare di `t_ind` e `F0`.
### 13.5 Differenze rispetto al 2025 nella parte "Mathematics in Biology"
`Teams 2 @ 1:00:05`
Nella seconda parte della lezione 2 il docente ripercorre le stesse slide di questo capitolo (contagio, sogliole, pattern, embrione, stimolo-risposta, visione, diabete, Eulero), con poche aggiunte:
- **contagio** (`Teams 2 @ 1:08:45`): la simulazione della slide usa $`C = 0.2`$ al giorno, costante; in modelli più complessi anche $`C`$ può variare nel tempo. Al flesso la derivata seconda cambia segno.
- **pattern** (`Teams 2 @ 1:12:36`): la dipendenza dallo spazio porta alle PDE; nel corso lo spazio sarà trattato non con le PDE ma con la **simulazione ad agenti**.
- **diabete** (`Teams 2 @ 1:25:08`): il progetto europeo si chiama **Presidium** (conferma il nome sentito nel 2025), terminato da pochi mesi, e usa il *physics-informed machine learning*, che inserisce equazioni differenziali nella struttura delle reti neurali per vincolarne l'addestramento.
- **Eulero** (`Teams 2 @ 1:28:46`): il docente aggiunge che anche un passo troppo piccolo produrrebbe "accumuli locali eccessivi" e quindi instabilità.
- **Colab** (`Teams 2 @ 1:35:11`): le librerie installate con `!pip install` vanno reinstallate a ogni sessione, perché il runtime è una macchina virtuale che si spegne; per i dati persistenti si collega Google Drive.
- **esempio **$`dy/dt = a\,y`$ (`Teams 2 @ 1:38:51`): il docente prova in diretta $`\alpha`$ = 0.8, 1.6 e 160 e cambia le condizioni iniziali. Sono i valori rimasti nel notebook `Lotka_Volterra.ipynb` di Teams (vedi nota sul codice in testa al capitolo e Divergenze).
- **Lotka-Volterra** (`Teams 2 @ 1:40:55`): introdotto a fine lezione, codice rimandato alla lezione 3; "negli anni '20", da Lotka e Volterra in modo indipendente.
> **Correzione:** sul passo di Eulero (`Teams 2 @ 1:29:11`) l'errore di troncamento globale di Eulero decresce linearmente con il passo; l'arrotondamento pesa solo con passi estremamente piccoli, molto lontani da quelli usati nel corso. Nella pratica, ridurre il passo rende Eulero più accurato e più stabile, non meno.
> **Correzione:** nel 2026 il docente descrive i parametri del Lotka-Volterra come "c il tasso di incremento dei predatori per ogni preda catturata" e "p il tasso di mortalità dei predatori" (`Teams 2 @ 1:42:23`). Nella slide $`dy/dt = -cy + pxy`$: $`c`$ è la mortalità dei predatori (il termine negativo), $`p`$ l'incremento per preda catturata.
### 13.6 Lotka-Volterra, SIR, zombie e SALib in Colab (edizione 2026)
`Teams 3 @ 0:00:02`
Nel 2026 la parte in Colab di questo capitolo occupa la prima mezz'ora della lezione 3 (20/05), prima degli agenti. Il docente ripercorre gli stessi notebook della sezione 6 e 9 (`Lotka_Volterra.ipynb`, `Zombie_invasion.ipynb`), con queste aggiunte:
- **Lotka-Volterra** (`Teams 3 @ 0:03:11`): se $`x = 0`$ la prima equazione resta a zero e i predatori decrescono in modo esponenziale; se $`y = 0`$ le prede crescono in modo esponenziale, "salvo moderarla con termini sottrattivi". Il ritratto di fase è una **curva chiusa** per ogni condizione iniziale, segno di periodicità, confermata dalla distanza costante tra i massimi della serie temporale (`Teams 3 @ 0:07:24`).
- **Esercizio** (`Teams 3 @ 0:09:32`): confrontare Eulero e `odeint` per capire quale sia più affidabile, e automatizzare la variazione dei quattro parametri, per esempio con una griglia di valori.
- **SIR** (`Teams 3 @ 0:12:46`): modello compartimentale capostipite, di cui gli altri modelli epidemiologici sono estensioni; non modella la reinfezione. Parametri: tasso di trasmissione ($`\beta`$) e tasso di guarigione ($`\gamma`$); se $`R_0 > 1`$ la malattia si diffonde, se $`R_0 < 1`$ la diffusione rallenta. Applicazioni: stima del picco, valutazione di vaccinazione e isolamento. Prima estensione: **SEIR**, con il compartimento degli esposti per il periodo di incubazione (`Teams 3 @ 0:16:54`).
- **Zombie** (`Teams 3 @ 0:17:54`): stessa formulazione del SIR, ma i rimossi possono tornare allo stadio precedente.
- **SALib** (`Teams 3 @ 0:19:38`): "Saltelli" è il nome di uno statistico; invece della forza bruta su tutte le combinazioni si campiona lo spazio dei parametri in modo più efficiente. Sulla funzione di Ishigami (tre input in $`[-\pi, \pi]`$, 1024 campioni base) il docente indica $`x_1`$ come variabile più impattante (`Teams 3 @ 0:24:50`). Il collegamento col SIR: una sola parametrizzazione non dice quali dei 5 parametri pesano di più, serve una valutazione statistica su molte combinazioni (`Teams 3 @ 0:25:52`).
- **Domanda di uno studente** (`Teams 3 @ 0:41:43`): perché non usare le derivate parziali per l'effetto marginale di ogni variabile? Risposta del docente: perché si vuole una valutazione **olistica**, sull'intero sistema e non su un solo elemento.
> **Nota aggiunta:** le derivate parziali danno una sensitività **locale**, valida attorno a un punto dello spazio dei parametri. Gli indici di Sobol sono **globali**: scompongono la varianza dell'output su tutto il dominio degli input e catturano anche le interazioni (l'indice totale di $`x_3`$ nella funzione di Ishigami, 0.245 con S1 ≈ 0.012, è un esempio di effetto che esiste solo in interazione).
> **Correzione:** il docente dice che SALib usa "metodi bayesiani" per capire quanto allontanarsi da un valore del parametro (`Teams 3 @ 0:20:38`). Lo schema di Saltelli usato nel notebook campiona con sequenze quasi-casuali (di Sobol) e gli indici si stimano con la **scomposizione della varianza**: non c'è inferenza bayesiana.
> **Correzione:** a `Teams 3 @ 0:24:50` la variabile più importante è descritta come quella "che, seppur perturbata, poco aumenta l'impatto sull'uscita". È il contrario: la variabile più importante è quella le cui variazioni spiegano la quota maggiore della varianza dell'output. Nota inoltre che $`x_1`$ è la prima per indice **totale** (ST ≈ 0.556), mentre per indice del **primo ordine** la prima è $`x_2`$ (S1 ≈ 0.444 contro 0.317), vedi sezione 9.2.
> **Nota aggiunta:** a `Teams 3 @ 0:14:51` la trascrizione rende la definizione di $`R_0`$ come "B per K" \[?\]. Nel SIR base $`R_0 = \beta / \gamma`$ (tasso di trasmissione diviso tasso di guarigione, con $`\beta`$ normalizzato sulla popolazione).
**Esercizio preliminare all'assignment** (`Teams 3 @ 0:29:05`): scegliere Lotka-Volterra o il SIR applicato agli zombie, risolverlo con `odeint` e con Eulero variando i parametri e documentando i risultati; poi la sensitivity analysis con SALib. Segue mezz'ora di esercitazione libera con il docente collegato (`Teams 3 @ 0:31:28`), poi gli agenti (capitolo 02).
