# 04 - Epidemiologia computazionale

> Fonte Notion: https://app.notion.com/p/3e912abc808d81c988f1e0df96d41f2e — ultima modifica 2026-09-28T18:15:18.888Z

**Registrazione:** `BT-04` (portale, edizione 2025), durata 01:17:24. Giornata: **Day 5** (slide "Epidemiologia computazionale, Matteo Rucco - Day 5").
**Materiale:** nessun PDF delle slide (testo e formule dai fotogrammi); notebook `SIR_ABMS.ipynb`, `SIR_Network.ipynb` e, non mostrato a lezione, `Epidemiology.ipynb`.
**Teams 2026:** `Teams 6` (25/05/2026) fino a `0:57:41`; poi la lettura della traccia del test finale (vedi **Assessment**). Sezione 10.
> **Nota sul codice.** `SIR_ABMS.ipynb` e `SIR_Network.ipynb` coincidono con quelli a schermo. Tutto il codice è verificato per esecuzione (`mesa==0.9.0`; per `SIR_Network` serve `EoN` 1.2, vedi sezione 8). Le celle di visualizzazione con Bokeh e Panel sono riassunte, non riportate per intero.
## Indice
1. Che cos'è l'epidemiologia computazionale
2. Un po' di storia
3. Epidemiologo e clinico, dinamica dell'infezione
4. Il modello di Kermack e McKendrick (SIR)
5. L'epidemiologia come scienza complessa
6. Dati e big data
7. SIR ad agenti con MESA (`SIR_ABMS.ipynb`)
8. SIR su grafo (`SIR_Network.ipynb`)
9. Esercizio in tabella
10. Integrazione Teams 2026
11. Dal materiale ufficiale: `Epidemiology.ipynb`
12. Collegamento con il test finale
13. Glossario, punti incerti, materiale usato
---
## 1. Che cos'è l'epidemiologia computazionale
`BT-04 @ 00:00:09`
Uno strumento digitale di modellistica per studiare le malattie e prevederne la diffusione: combina scienza, tecnologia e matematica. Il SIR, visto finora come esempio di tecnica di modellazione, qui è il punto di partenza per il percorso inverso: dall'epidemiologia agli strumenti (`BT-04 @ 00:00:41`). L'obiettivo è fornire strumenti per **prevenire e gestire le epidemie**; applicazioni pratiche: simulare l'impatto di una campagna vaccinale, prevedere il picco per preparare il sistema sanitario e i policy maker (`BT-04 @ 00:02:19`).
Evoluzione: dalle analisi manuali alle simulazioni, grazie alla matematica e alla capacità di acquisire dati quasi in tempo reale su scala nazionale; in passato gli epidemiologi lavoravano isolati su aree ristrette (`BT-04 @ 00:02:54`). Durante la pandemia di COVID-19 questi strumenti sono stati molto usati; il docente cita il gruppo di epidemiologia computazionale della **Fondazione Bruno Kessler** di Trento, diretto da Stefano Merler (`BT-04 @ 00:04:34`).
Slide "Epidemiologia è interdisciplinare" (`BT-04 @ 00:05:37`), "un'orchestra scientifica":
- *Salute pubblica*: per l'enfasi sulla prevenzione delle malattie;
- *Medicina clinica*: per l'enfasi sulla classificazione e diagnosi delle malattie (numeratori);
- *Fisiopatologia*: per comprendere i meccanismi biologici di base (storia naturale);
- *Scienze sociali*: per il contesto sociale in cui le malattie si manifestano (determinanti sociali);
- *Statistica \[+ Matematica + Fisica + ...\]*: per quantificare la frequenza delle malattie e le relazioni con gli antecedenti.
Esempi del docente dal COVID-19: i clinici dicono se e come una patologia è curabile; le scienze sociali, con la fisica che simula la dinamica in aria delle particelle respiratorie, hanno portato alle linee guida sul distanziamento (`BT-04 @ 00:06:50`); epidemiologi e sociologi hanno studiato l'effetto del lockdown sulla salute mentale, e il docente suggerisce gli interventi di Paolo Crepet (`BT-04 @ 00:07:54`). Nessuna disciplina è la più importante: dipende dal punto di osservazione.
## 2. Un po' di storia
`BT-04 @ 00:09:41`
Slide "Parziale vista sulla cronologia delle malattie infettive" (una linea del tempo dal Medioevo a oggi). Dati citati: le malattie infettive causano circa 13 milioni di morti l'anno; sei malattie (polmonite, tubercolosi, malattie diarroiche, malaria, morbillo e HIV/AIDS) sono responsabili di metà delle morti premature, soprattutto bambini e giovani adulti; la malaria avrebbe causato tra 650 000 e 1,4 milioni di morti nel solo 2010, con statistiche poco aggiornate perché colpisce paesi con sistemi poco strutturati (`BT-04 @ 00:10:15`). Eventi chiave: la peste nera (popolazione europea ridotta del 30-50%), la spagnola, la vaccinazione obbligatoria contro il vaiolo, il miglioramento delle norme igieniche. La lezione principale: **rispondere rapidamente e in modo coordinato**; aspettare che l'epidemia scompaia da sola è l'errore peggiore (`BT-04 @ 00:11:17`).
Definizioni (`BT-04 @ 00:11:50`):
- **epidemia**: casi di malattia in una comunità o regione in quantità e rapidità ben oltre l'atteso; dal greco *epi* (su) e *demos* (popolo);
- **pandemia**: epidemia che interessa gran parte del mondo (H1N1 nel 2009);
- **endemia**: nuove infezioni che si verificano costantemente nella popolazione.
Le epidemie avrebbero influito su eventi storici: pestilenze romane e medievali, caduta della dinastia Han nel III secolo, sconfitta degli Aztechi nel 1500 per il vaiolo; la pandemia del 1918 fece più morti della prima guerra mondiale; negli ultimi 50 anni HIV, SARS, malattie simil-influenzali, COVID-19 (`BT-04 @ 00:12:29`).
**Storia dei modelli** (`BT-04 @ 00:19:22`):
- Daniel **Bernoulli**, 1760: primo modello matematico in epidemiologia, sulla variolazione e l'aspettativa di vita nella popolazione francese;
- John **Snow**, 1854: analisi sistematica dei dati di un'epidemia di colera a Londra, attribuita a una fonte d'acqua contaminata. Il docente sottolinea l'importanza di cercare le **cause**, non solo di misurare le velocità di diffusione (`BT-04 @ 00:20:38`);
- Ronald **Ross**, 1911: il vettore della malaria (le zanzare *Anopheles gambiae*) e un modello spaziale della diffusione; risultato: la malaria si controlla riducendo le zanzare sotto una soglia, primo esempio di **soglia epidemica** (`BT-04 @ 00:21:17`);
- **Kermack e McKendrick**, 1927: il primo modello epidemico generale, il SIR.
> **Correzione:** il docente definisce la variolazione come "la diffusione del variolo" (`BT-04 @ 00:20:00`), e nel 2026 come "il processo di sviluppo del variolo". La **variolazione** era l'inoculazione deliberata di materiale di pustole di vaiolo in una persona sana, per provocare una forma lieve e l'immunità; Bernoulli stimò che generalizzarla avrebbe allungato la speranza di vita.
> **Correzione:** Ross **scoprì** la trasmissione della malaria attraverso le zanzare nel **1897** (premio Nobel per la medicina nel 1902); nel 1911 pubblicò il modello matematico (nella seconda edizione di *The Prevention of Malaria*). Il docente data la scoperta al 1911 (`BT-04 @ 00:21:17`) e dice "riducendo la popolazione della malaria": la soglia riguarda la popolazione di **zanzare**, come dice lui stesso nel 2026.
Perché i modelli: in epidemiologia gli esperimenti fisici controllati sono spesso impossibili per ragioni **etiche** e pratiche. Alla domanda del docente uno studente risponde che per studiare la diffusione di un virus bisognerebbe inocularlo nelle persone; il docente aggiunge il rischio che l'infezione sfugga al controllo, con costi sociali ed economici a carico del sistema sanitario pubblico (`BT-04 @ 00:18:48`).
## 3. Epidemiologo e clinico, dinamica dell'infezione
`BT-04 @ 00:13:03`
Epidemiologo e clinico lavorano insieme con obiettivi diversi: il clinico studia il **paziente** e il trattamento individuale (un malato di COVID-19 in terapia intensiva), l'epidemiologo la **popolazione** e la diffusione su larga scala (l'impatto di un lockdown). Senza i dati clinici gli epidemiologi non modellano con precisione (`BT-04 @ 00:13:33`).
Slide "Confronto epidemiologo vs clinico" (da Keeling & Rohani, *Modeling Infectious Diseases*, 2008): dal tempo di infezione il **patogeno** cresce fino a un picco, poi cala mentre sale la **risposta immunitaria**; il docente la collega al modello di Jerne (capitolo 03), con una risposta in media più ampia della carica del patogeno (`BT-04 @ 00:14:41`). Sotto, la "coarse graining of the dynamics" su due assi: **stato medico** (incubazione, malattia) e **stato di infezione** (suscettibile, latente, infettivo, guarito). Da suscettibili, dopo il contatto con un infetto si entra in uno stato latente o di incubazione, poi infettivo, da cui si guarisce o, nei casi estremi, si muore (`BT-04 @ 00:15:53`).
## 4. Il modello di Kermack e McKendrick (SIR)
`BT-04 @ 00:17:07`
Slide "Kermack & McKendrick model" (Kermack & McKendrick, Proc. Roy. Soc. A 1927; Keeling & Rohani 2008): tre compartimenti, suscettibili $`S`$, infettivi $`I`$, guariti $`R`$.
$$
\frac{dS}{dt} = -k\beta\frac{I}{N}S, \qquad \frac{dI}{dt} = k\beta\frac{I}{N}S - \mu I, \qquad \frac{dR}{dt} = \mu I, \qquad S + I + R = N
$$
Il "movimento" tra compartimenti non è fisico ma una **transizione di stato** (`BT-04 @ 00:22:42`). Dal modello si ricavano quando arriva il picco e l'impatto delle vaccinazioni. Il docente lo presenta come il primo modello epidemico generale, basato sull'ipotesi di **azione di massa** (`BT-04 @ 00:21:49`).
> **Nota aggiunta:** nella slide $`k`$ è il numero di contatti per unità di tempo, $`\beta`$ la probabilità di trasmissione per contatto, $`\mu`$ il tasso di guarigione (l'inverso della durata media dell'infezione). Il prodotto $`k\beta`$ è quello che altrove nel corso è indicato con $`\beta`$, e $`\mu`$ con $`\gamma`$.
**Limiti** (`BT-04 @ 00:23:45`): alla domanda del docente su cosa si trascura, la risposta è che il modello non contiene la **struttura sociale** né le **mutazioni** del virus.
**Dove intervenire** (`BT-04 @ 00:24:18`): se un policy maker potesse agire su un solo compartimento? Due approcci: **preventivo**, sui suscettibili (renderli meno suscettibili, per esempio con la vaccinazione), e **curativo/di contenimento**, sugli infetti (ridurre la trasmissione, anche con la mascherina). L'esito di lungo periodo è simile, ridurre il numero totale di infetti, ma cambia il momento: a epidemia già al picco conviene intervenire prima sugli infetti, all'inizio prima sui suscettibili (`BT-04 @ 00:27:27`).
Slide successiva: dati della rete francese **Sentinelles** ([sentiweb.fr](http://sentiweb.fr)) del 1988, con il modello applicato a una serie settimanale di casi; secondo il docente mostra un segnale d'allarme che era già presente (`BT-04 @ 00:27:58`).
**Il picco** (`BT-04 @ 00:47:08`). Slide "Quando avverrà il picco nel modello SIR?": in una popolazione di $`N`$ persone le coppie possibili sono $`N(N-1)/2`$; per un rischio serve un contatto tra un sano e un infetto ($`S_0 I_0`$ coppie); il contatto va moltiplicato per la contagiosità $`\alpha`$ e per gli $`N`$ individui:
$$
\text{Numero medio giornaliero di infezioni} = \frac{2\alpha}{N-1}\,S_0 I_0, \qquad \beta = \frac{2\alpha}{N-1}
$$
"Il numero di infetti fa diminuire il numero S(t) delle persone sane e fa aumentare la popolazione I, quest'ultima però diminuisce se le persone guariscono, o muoiono o vengono isolate." Il picco dipende da un numero $`\gamma`$ misurato quotidianamente, che "dipende da quanto si sta facendo per isolare la popolazione, a farla guarire, a morire le persone ci pensano da sole". Da qui le tre formule a tempo discreto:
$$
S(t+1) = S(t) - \beta S(t) I(t), \qquad I(t+1) = I(t) + \beta S(t) I(t) - \gamma I(t), \qquad R(t+1) = R(t) + \gamma I(t)
$$
"Affinché ci sia un'epidemia il numero degli infetti in un certo giorno (t+1) deve aumentare rispetto al giorno precedente t cioè il numero $`\beta S(t) - \gamma > 0`$, equivalente a dire che $`\frac{\beta}{\gamma}S(t) > 1`$."
Il docente: il picco si ha quando $`dI/dt = 0`$, cioè nuovi casi uguali ai guariti, quando $`S`$ scende sotto una **soglia critica** legata a $`\gamma`$ e $`\beta`$; il picco è influenzato da interventi esterni. Poi l'**immunità di gregge**: quando una porzione sufficiente della popolazione è immune, per vaccinazione o guarigione, "$`R_0`$ scende sotto 1" e l'epidemia si ferma prima del picco naturale (`BT-04 @ 00:50:27`).
> **Nota aggiunta:** il fattore $`2\alpha/(N-1)`$ si ottiene supponendo che ogni giorno avvengano $`N`$ contatti tra coppie scelte a caso: la probabilità che una coppia sia sano-infetto è $`S I / [N(N-1)/2]`$, e moltiplicando per $`\alpha`$ e per $`N`$ si ha $`2\alpha S I/(N-1)`$. È l'ipotesi implicita nel "moltiplichiamo per tutti gli N individui".
> **Correzione:** nella slide la seconda equazione è scritta $`I(t+1) = I(t) + \beta S(t)I(t) - \gamma I(t) = I(t)\cdot[\beta S(t) - \gamma]`$. Il raccoglimento corretto è $`I(t)\cdot[1 + \beta S(t) - \gamma]`$. La condizione di crescita della slide resta giusta, perché $`I(t+1) - I(t) = I(t)[\beta S(t) - \gamma]`$.
> **Correzione:** $`R_0`$ è una costante della malattia nella popolazione tutta suscettibile e non "scende sotto 1". Con l'immunità a scendere sotto 1 è il **numero di riproduzione effettivo** $`R_t = R_0 \cdot S/N`$; la soglia di immunità di gregge è $`1 - 1/R_0`$ della popolazione immune (verificato nella sezione 11: 0.75 per $`R_0 = 4`$).
## 5. L'epidemiologia come scienza complessa
`BT-04 @ 00:29:43`
Oltre alla multidisciplinarità, tre assi di complessità, riassunti nella slide "L'epidemiologia è una scienza complessa", che parte in basso a sinistra dai modelli compartimentali a **mescolamento omogeneo**:
**1. Il patogeno** (`BT-04 @ 00:30:15`): *pathogen polymorphism, evolution, interaction with other pathogens*, "multi strain, evolution". Il SIR vale per patogeni che non cambiano; il virus del COVID-19 ha mostrato varianti e "resistenze". Resistenza agli antibiotici per uso eccessivo e inappropriato; HIV e influenza mutano rapidamente, per questo il vaccino antinfluenzale cambia ogni anno; adattamenti ambientali: i batteri della tubercolosi resistono nei polmoni per anni in forma silente; per il COVID-19 sono serviti vaccini per le varianti Delta e Omicron. "Una partita a scacchi": ogni nostra mossa genera una risposta evolutiva (`BT-04 @ 00:33:01`).
**2. L'ospite** (`BT-04 @ 00:33:38`): *host immunological & genetical profile, microbiome*, "population structure". Storia clinica (comorbidità, malattie croniche), genetica (alcuni individui sono resistenti all'HIV per mutazioni del gene CCR5), stili di vita (fumatori e sedentari più vulnerabili alle infezioni respiratorie), scelte (il rifiuto dei vaccini accelera la diffusione), adattamenti culturali (in Giappone la mascherina si usa anche fuori dalle epidemie).
**3. La struttura sociale** (`BT-04 @ 00:35:24`): *host demography, behaviour* e i luoghi (ospedale, scuola, casa, lavoro); modelli di rete, metapopolazione e ad agenti. Chi entra in contatto con chi, quanto spesso, dove; densità abitativa bassa (nord Europa) contro alta. Gli **hub**, persone o luoghi con molti contatti (scuole, aeroporti), hanno un impatto sproporzionato; gli eventi **super spreader**; le disuguaglianze (lavoratori essenziali più esposti, accesso ineguale a cure e vaccini). Interventi mirati come il **contact tracing** usano la conoscenza delle reti; conoscere in anticipo un evento super spreader può suggerire il numero massimo di partecipanti in funzione del luogo (`BT-04 @ 00:37:46`). "Come un terremoto ha bisogno della terra per propagarsi, una patologia ha bisogno di una rete di relazioni sociali."
**Le assunzioni del SIR** (`BT-04 @ 00:40:13`), indicate dal docente come possibile domanda del test finale: la popolazione è **omogenea**, senza hub preferenziali di diffusione; al tempo zero tutti hanno la stessa probabilità di essere suscettibili, e poi di infettarsi. Il SIR non va buttato: funziona bene sotto queste assunzioni, e con patogeni variabili, ospiti eterogenei e reti sociali servono modelli più complessi (`BT-04 @ 00:39:29`).
**Oltre i compartimenti** (`BT-04 @ 01:01:19`), slide "Da modelli compartimentali a strutture più complesse": i compartimenti sono sottopopolazioni simili e ben mescolate, descritte da ODE; hanno avuto enorme successo nell'ultimo secolo perché facili da estendere, veloci da costruire e risolvibili analiticamente o numericamente, ma assumono omogeneità. Estensioni:
- **modelli stratificati**: sottogruppi per età, professione, area geografica. Per questo il docente ha messo l'età negli agenti della sezione 7: un'estensione da implementare sono probabilità di transizione dipendenti dall'età (`BT-04 @ 01:03:05`);
- **modelli a rete**: nodi persone, archi contatti;
- **modelli dinamici adattativi**: comportamenti che cambiano nel tempo (distanziamento, mascherine), anche il cambiamento climatico.
Riferimenti citati: Newman (2003) e Brauer (2008).
## 6. Dati e big data
`BT-04 @ 00:28:37`
Slide "Epidemiologia: come dare senso ai dati": **forecasting** (durata, picco, casi), **nowcasting** (misurare e analizzare il modello rispetto a dati appena passati o immediatamente futuri), comprensione medica e biologica (fattori che influenzano la trasmissione), **analisi di scenari futuri** (vaccinazione, intervento farmacologico, quarantena, limitazione degli spostamenti). Strumenti: Python, R, Google Colab.
Slide "Dalla complessità ai big data" (`BT-04 @ 00:42:27`): un *quad chart* delle quattro V applicate all'epidemiologia (**varietà, velocità, volume, veridicità**), con fonti come HealthMap, ProMED-mail, dati di sequenziamento, reti sociali sintetiche, demografia, Twitter, Google Flu Trends, dati meteo e di vegetazione (NDVI). Perché il calcolo è diventato centrale (`BT-04 @ 00:43:07`):
- i modelli sono sempre più complessi: il SIR si risolve a mano, i modelli accoppiati o con spostamenti di popolazione no;
- i **modelli a rete** sono sempre più accettati: più naturali dei compartimenti, ma più costosi in calcolo e dati. Il docente cita un modello della popolazione degli Stati Uniti con 34 insiemi di dati pubblici e commerciali, oltre 100 GB in input, circa 300 milioni di persone e 100 milioni di località, che richiede il cloud (`BT-04 @ 00:44:43`);
- più parametri non noti (la probabilità di trasmissione all'inizio di una nuova malattia) da stimare con inferenza statistica e bayesiana.
Strumenti di sorveglianza citati: **Google Flu Trends** e il sistema per le influenze stagionali della Fondazione ISI di Torino (Alessandro Vespignani) (`BT-04 @ 00:45:58`).
> **Nota aggiunta:** Google Flu Trends è stato **chiuso nel 2015**, dopo che le sue stime avevano sovrastimato di molto i picchi influenzali (in particolare nella stagione 2012-2013). Nel 2026 il docente lo descrive ancora come piattaforma operativa (`Teams 6 @ 0:40:31`).
## 7. SIR ad agenti con MESA (`SIR_ABMS.ipynb`)
`BT-04 @ 00:51:05`
Estensione del SIR: invece di gruppi omogenei, ogni individuo è un agente che interagisce secondo regole, con una componente spaziale. Oltre a MESA si installano **Bokeh** e `jupyter_bokeh` per grafici interattivi (`BT-04 @ 00:51:39`).
```python
!pip install mesa==0.9.0
!pip install bokeh
!pip install jupyter_bokeh

import time, enum
import numpy as np
import pandas as pd
import pylab as plt
from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
# + import di bokeh e panel per i grafici interattivi


class State(enum.IntEnum):
    SUSCEPTIBLE = 0
    INFECTED = 1
    REMOVED = 2


class MyAgent(Agent):
    """ An agent in an epidemic model."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.age = self.random.normalvariate(20,40)
        self.state = State.SUSCEPTIBLE
        self.infection_time = 0

    def move(self):
        """Move the agent"""

        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def status(self):
        """Check infection status"""

        if self.state == State.INFECTED:
            drate = self.model.death_rate
            alive = np.random.choice([0,1], p=[drate,1-drate])
            if alive == 0:
                self.model.schedule.remove(self)
            t = self.model.schedule.time-self.infection_time
            if t >= self.recovery_time:
                self.state = State.REMOVED

    def contact(self):
        """Find close contacts and infect"""

        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        if len(cellmates) > 1:
            for other in cellmates:
                if self.random.random() > model.ptrans:
                    continue
                if self.state is State.INFECTED and other.state is State.SUSCEPTIBLE:
                    other.state = State.INFECTED
                    other.infection_time = self.model.schedule.time
                    other.recovery_time = model.get_recovery_time()

    def step(self):
        self.status()
        self.move()
        self.contact()
```
La classe `State` mappa etichette numeriche e testuali: 0 suscettibile, 1 infetto, 2 rimosso, cioè guarito (`BT-04 @ 00:52:58`). A ogni step l'agente verifica lo stato (se infetto da abbastanza tempo passa a rimosso), si muove su una cella del vicinato di Moore e cerca contatti (`BT-04 @ 00:54:05`).
```python
class GridInfectionModel(Model):
    """A model for infection spread."""

    def __init__(self, N=10, width=10, height=10, ptrans=0.5,
                 progression_period=3, progression_sd=2, death_rate=0.0193, recovery_days=21,
                 recovery_sd=7):

        self.num_agents = N
        self.initial_outbreak_size = 1
        self.recovery_days = recovery_days
        self.recovery_sd = recovery_sd
        self.ptrans = ptrans
        self.death_rate = death_rate
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True
        self.dead_agents = []
        # Create agents
        for i in range(self.num_agents):
            a = MyAgent(i, self)
            self.schedule.add(a)
            # Add the agent to a random grid cell
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            self.grid.place_agent(a, (x, y))
            #make some agents infected at start
            infected = np.random.choice([0,1], p=[0.98,0.02])
            if infected == 1:
                a.state = State.INFECTED
                a.recovery_time = self.get_recovery_time()

        self.datacollector = DataCollector(
            agent_reporters={"State": "state"})

    def get_recovery_time(self):
        return int(self.random.normalvariate(self.recovery_days,self.recovery_sd))

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()


def get_column_data(model):
    #pivot the model dataframe to get states count at each step
    agent_state = model.datacollector.get_agent_vars_dataframe()
    X = pd.pivot_table(agent_state.reset_index(),index='Step',columns='State',aggfunc=np.size,fill_value=0)
    labels = ['Susceptible','Infected','Removed']
    X.columns = labels[:len(X.columns)]
    return X


pop=300
steps=100
model = GridInfectionModel(pop, 20, 20, ptrans=0.5)
for i in range(steps):
    model.step()
print (get_column_data(model))
```
Il modello posiziona gli agenti su una griglia toroidale 20×20, infetta all'inizio circa il 2% di loro, e il DataCollector registra lo stato di ogni agente; `get_column_data` conta suscettibili, infetti e rimossi a ogni step (`BT-04 @ 00:56:16`). Con 300 agenti per 100 step la tabella inizia con 295 suscettibili e 5 infetti; alla fine "rimangono pochissimi suscettibili, non abbiamo più malati e tutti sono stati recuperati" (`BT-04 @ 00:57:34`). Seguono il grafico delle tre serie, una mappa della griglia colorata per stato e un'animazione Bokeh di 100 step, in cui a un certo punto le celle di infetti sono quasi la totalità (`BT-04 @ 00:58:59`).
Seconda esecuzione, con animazione:
```python
steps=100
pop=400
model = GridInfectionModel(pop, 20, 20, ptrans=0.25, death_rate=0.01)
for i in range(steps):
    model.step()
    # aggiornamento dei pannelli Bokeh (serie temporali e griglia), pausa di 0.5 s

def compute_max_infections(model):
    X=get_column_data(model)
    try:
        return X.Infected.max()
    except:
        return 0

print("Maximum number of infected people " +str(compute_max_infections(model) ))
```
Con 400 persone, griglia 20×20, probabilità di trasmissione del 25% e "probabilità di sparire dalla popolazione dello 0,01 per cento", il picco a schermo è di 243 infetti (`BT-04 @ 01:00:12`). Cambiando la dimensione della griglia o le probabilità il picco cambia.
Verificato per esecuzione (20 seed): con 300 agenti e `ptrans=0.5` il picco ha mediana 192 (157-220); con 400 agenti, `ptrans=0.25`, `death_rate=0.01` mediana 243 (222-273), come a schermo; il notebook salvato riporta 262.
> **Correzione:** il docente descrive l'età come "una distribuzione normale con media 30, fra i 20 e i 40 anni" (`BT-04 @ 00:53:33`). `normalvariate(20, 40)` è una normale con **media 20 e deviazione standard 40**: verificato, circa un terzo delle età è negativo. L'età comunque non è usata nel modello.
> **Correzione:** secondo il docente `possible_steps` sono le celle "libere" e il contagio avviene verso "i vicini nelle celle limitrofe" (`BT-04 @ 00:54:37`, `00:55:42`). `get_neighborhood` restituisce tutte le 8 celle, occupate o no, e `contact` agisce solo sugli agenti nella **stessa cella** (`get_cell_list_contents([self.pos])`).
> **Correzione:** a fine simulazione non "sono tutti recuperati": `death_rate` è una probabilità di morte **per step** di infezione. Con 0.0193 per circa 21 giorni di malattia muore circa un terzo degli infetti ($`1 - 0.9807^{21} \approx 0.34`$). Verificato: nella prima esecuzione muoiono in mediana 97 agenti su 300 (nel notebook salvato restano 1 suscettibile e 186 rimossi: 113 agenti mancano). I morti escono dallo scheduler e quindi dai conteggi, per cui le tre curve non sommano a N. Nella seconda esecuzione `death_rate=0.01` è l'**1%** per step, non lo 0,01% (circa il 19% degli infetti muore; verificato, mediana 73 morti su 400).
> **Nota aggiunta:** altri dettagli del codice. L'agente morto viene tolto dallo scheduler ma **non dalla griglia**: resta come "fantasma" nella cella, può essere ricontato tra i `cellmates` e anche "infettato". In `contact` il test `random() > ptrans` è fatto per ogni coinquilino, compreso l'agente stesso, e usa la variabile globale `model` invece di `self.model`: funziona solo perché nel notebook il modello si chiama `model`. I parametri `progression_period` e `progression_sd` non sono usati.
## 8. SIR su grafo (`SIR_Network.ipynb`)
`BT-04 @ 01:04:10`
Nell'epidemiologia su rete la diffusione avviene su una rete di contatto $`G = (V, E)`$ non orientata: ogni nodo è un individuo o un sottogruppo, ogni arco un contatto (`BT-04 @ 01:04:47`). Slide "Estensione con grafo":
- "Il grafo di contatto G = (V,E) è definito su una popolazione V = \{a, b, c, d\}.
- I colori dei nodi bianco, nero e grigio rappresentano rispettivamente gli stati Suscettibile, Infetto e Recuperato.
- Inizialmente, solo il nodo a è infetto e tutti gli altri nodi sono suscettibili.
- Viene mostrato un possibile risultato a t = 1, in cui il nodo c viene infettato, mentre il nodo a si riprende.
- Il nodo a cerca di infettare in modo indipendente entrambi i suoi vicini b e c, ma solo il nodo c viene infettato, questo è indicato dal bordo pieno (a,c).
- La probabilità di ottenere questo risultato è $`(1 - \beta((a,b),1))\,\beta((a,c),1)`$."
Qui $`\beta`$ è la stessa quantità del SIR, la velocità di diffusione, ora per arco (`BT-04 @ 01:10:59`).
**Come costruire il grafo** (`BT-04 @ 01:06:30`): dipende dal fenomeno. Per le relazioni fisiche si può collegare due persone se la loro distanza è sotto una soglia (nella stessa stanza); per i contatti su Facebook la vicinanza spaziale non vale e servono altri criteri (amicizie, like). La scelta cambia la **topologia** (connettività) e quindi la diffusione. Esempio: incrociando i dati social si può dedurre che due utenti hanno partecipato allo stesso evento super spreader, cioè sono stati in contatto a loro insaputa: analisi multimodale dei dati per costruire il grafo (`BT-04 @ 01:09:20`).
**Colab** (`BT-04 @ 01:11:35`): si installano **NetworkX**, per i grafi, ndlib, **EoN** (*Epidemics on Networks*) e graphviz per la visualizzazione. NetworkX offre molte topologie (Barabási, grafi casuali); qui un grafo **Watts-Strogatz** (`BT-04 @ 01:13:09`).
```python
!pip install networkx
!pip install mesa==0.9.0
!pip install bokeh
!pip install ndlib
!pip install EoN
!pip install jupyter_bokeh
!apt install libgraphviz-dev
!pip install pygraphviz

import time, enum, math
import numpy as np
import pandas as pd
import pylab as plt
import networkx as nx
import EoN
import random

g=nx.watts_strogatz_graph(n=100, k=4, p=0.6)
plt.figure(figsize=(40,40))

E = g.number_of_edges()
#initializing random weights
w = [random.random() for i in range(E)]
s = max(w)
w = [ i/s for i in w ] #normalizing
k = 0
for i, j in g.edges():
    g[i][j]['weight'] = w[k]
    k+=1

gamma = 0.2
beta = 1.2
r_0 = beta/gamma
print(r_0)
N = 100 # population size
I0 = 1   # intial n° of infected individuals
R0 = 0
S0 = N - I0 -R0
pos = nx.spring_layout(g)
nx_kwargs = {"pos": pos, "alpha": 0.7} #optional arguments to be passed on to the
#networkx plotting command.
print("doing Gillespie simulation")
sim = EoN.Gillespie_SIR(g, tau = beta, gamma=gamma, rho = I0/N, transmission_weight="weight", return_full_data=True)
print("done with simulation, now plotting")
for i in range(0,5,1):
    sim.display(time = i,  **nx_kwargs)
    plt.axis('off')
    plt.title("Iteration {}".format(i))
    plt.draw()
```
(Celle di disegno commentate nel notebook omesse.) Output: istantanee del grafo a tempi diversi, a sinistra, e le serie temporali S, I, R, a destra (`BT-04 @ 01:13:54`). Il docente: esempio minimale, arricchibile cambiando topologia e dinamica; **non utile ai fini del test finale**, ma i grafi sono strumenti utili per chi si occuperà di epidemiologia computazionale (`BT-04 @ 01:14:29`).
Verificato per esecuzione: il grafo ha 100 nodi e 200 archi (grado medio 4), `r_0` stampato 6.0. Su 200 simulazioni l'epidemia si esaurisce subito (5 casi o meno) nel 14% dei casi; altrimenti raggiunge in media 96 nodi su 100.
> **Nota aggiunta:** in `EoN.Gillespie_SIR` il parametro `tau` è un **tasso di trasmissione per arco** (qui moltiplicato per il peso), non il $`\beta`$ del SIR a mescolamento omogeneo, e `rho` è la frazione iniziale di infetti. Su una rete $`\beta/\gamma`$ non è il numero di riproduzione: la probabilità che un infetto contagi un vicino prima di guarire è $`\tau w/(\tau w + \gamma)`$ (0.857 per peso 1, 0.75 per peso 0.5), e $`R_0`$ dipende anche dalla struttura dei gradi.
> **Nota aggiunta:** con `EoN` 2.0 la chiamata con `transmission_weight="weight"` va in errore (`TypeError: unhashable type: 'numpy.ndarray'`); funziona con `EoN==1.2`.
## 9. Esercizio in tabella
`BT-04 @ 01:15:04`
Un esercizio sul SIR, da risolvere con le equazioni (a tempo discreto) o con gli agenti, per calcolare e tracciare S, I, R al variare di $`\beta`$ e $`\gamma`$. Slide "Esercizio": "Prendete N=1200 e un intervallo di 7 giorni, supponiamo che l'epidemia abbia un indice di contagiosità dello 0,15 (cioè si ammali il 15% delle persone venute a contatto). Supponiamo inoltre che γ = 0,80 per la prima settimana e poi aumenta a 0,95 per la settimana successive. Riempire la seguente tabella per la settimana 1" (colonne Giorno, β, S(t), I(t), R(t)). "Esercizio - continua": la stessa tabella per la settimana 2; "Riportare su un grafico i valori ottenuti ogni giorno per le tre popolazioni nelle due settimane. Vedere se si tratta di diffusione con picco, quali osservazioni fate?"
Il docente suggerisce di completare la tabella giorno per giorno, identificare il picco, discutere strategie per appiattire la curva, per esempio intervenendo su $`\beta`$ (distanziamento sociale). Non è fondamentale per il test finale (`BT-04 @ 01:16:48`).
> **Nota aggiunta:** la traccia non dà le condizioni iniziali. Con le formule della sezione 4 si ha $`\beta = 2 \cdot 0.15 / 1199 = 2.50 \cdot 10^{-4}`$ e $`\beta N = 0.30`$; al giorno 1 $`\frac{\beta}{\gamma}S = 0.375 < 1`$, quindi **non c'è picco**: gli infetti calano dal primo giorno. Verificato con $`I_0 = 1`$: $`I`$ passa a 0.5, 0.25, ... e a fine seconda settimana $`R \approx 1.6`$; con $`I_0 = 10`$: $`I`$ scende a 4.98, 2.47, ... e $`R`$ finale $`\approx 15.9`$. Con $`\gamma`$ così alti (guarigione in poco più di un giorno) l'epidemia si estingue; per vedere un picco serve $`\beta S > \gamma`$, cioè una contagiosità ben più alta o un $`\gamma`$ più basso.
## 10. Integrazione Teams 2026
`Teams 6 @ 0:00:03`
Nel 2026 l'epidemiologia è la prima parte dell'ultima lezione (25/05). Stessi contenuti e slide del 2025, con queste aggiunte.
**COVID-19** (`Teams 6 @ 0:02:04`): alla domanda su come l'epidemiologia computazionale sia stata usata, gli studenti rispondono ricostruire i focolai a ritroso e monitorare $`R_0`$ per area; il docente: la **root cause analysis** richiede una rappresentazione a grafo dei siti per individuare gli hub di trasmissione; i dati dei tamponi sono sottostimati e non si generalizzano con semplici fattori di scala, per via di dinamiche complesse (contatti di prossimità, lavoratori essenziali in lockdown) che si simulano al computer (`Teams 6 @ 0:04:07`).
**Il SIR basta per il COVID?** (`Teams 6 @ 0:05:09`): no. Uno studente nota che il SIR non prevede reinfezioni, mentre ci sono state più ondate; il docente aggiunge che non prevede una **causa esterna** di trasmissione, come il salto di specie dagli animali all'uomo: servono **modelli accoppiati** (epidemiologia veterinaria e umana) che lavorano a scale spaziali e temporali diverse, da sincronizzare (`Teams 6 @ 0:06:10`).
**Trasmissione indiretta** (`Teams 6 @ 0:08:13`): a una domanda sul contagio tramite oggetti (soldi, superfici), il docente spiega che il SIR assume un'interazione **aspaziale e atomica**: al contatto la trasmissione avviene, indipendentemente da tempo e distanza di esposizione. Modelli più evoluti stabiliscono tempi minimi di esposizione e tipo di interazione (per le malattie sessualmente trasmissibili un contatto intimo) o mezzi diversi (soldi, acqua stagnante), anche con modelli di crescita della concentrazione del virus. In un modello semplice si può alzare la probabilità di trasmissione, ma bisogna sempre dare un'**interpretazione semantica** ai parametri: nel COVID, per esempio, la probabilità che due persone siano state a meno di un metro; va adattata alla densità (alta in un luogo affollato, bassa nel nord della Scandinavia) e validata rispetto al fenomeno reale. "Un modello è un'astrazione" (`Teams 6 @ 0:12:22`).
**Dove intervenire** (`Teams 6 @ 0:26:59`): risposte degli studenti sugli infetti (la diffusione parte da lì), sui guariti (evitare ricontagi, che però nel SIR non esistono) e sui suscettibili. Il docente: prevenzione e contenimento sono due estremi dello spettro; la scelta ottimizza costi sociali e pressione sanitaria e richiede modelli più complessi (`Teams 6 @ 0:30:15`).
**Dove funziona il SIR** (`Teams 6 @ 0:31:15`): in **sistemi isolati**, senza flussi in ingresso o uscita, come un college americano in cui quasi tutta la popolazione convive: l'esempio di una patologia seguita per 5 settimane in un college (vedi sezione 11).
**Strumenti** (`Teams 6 @ 0:32:15`): R è storicamente l'ambiente più usato in ambito biomedico e dagli epidemiologi esperti; Python lo ha quasi eguagliato e molte librerie sono portate da uno all'altro. Modelli di previsione con **transformer** e *physics-informed machine learning*; dataset "non più sotto il terabyte"; nell'analisi: analisi stocastica delle fluttuazioni, strutture dati di consenso riutilizzabili tra geografie, rimozione dei bias, rapporto segnale/rumore, risoluzione spaziale con dati GIS, armonizzazione di fonti diverse, **incertezza** epistemica e di modello; dati di sequenziamento high-throughput e dei social media (`Teams 6 @ 0:40:31`). Il docente collega la malaria all'intervento dell'ospite della lezione 5, Andrea De Antoni (`Teams 6 @ 0:15:31`).
**Modelli su grafo** (`Teams 6 @ 0:48:49`): un nodo infetto trasmette solo ai vicini e gli archi possono avere pesi (probabilità di trasmissione). Esempio: una scuola, dove la probabilità fra studenti è più alta che fra studenti e docenti. I modelli a grafo servono per focolai locali e **interventi mirati**, invece di interventi sull'intera popolazione di un compartimento. Un grafo si rappresenta con una **matrice di adiacenza** (1 o 0, oppure un peso in \[0, 1\]) (`Teams 6 @ 0:55:37`). Il picco nel grafico di EoN è calcolato automaticamente.
> **Correzione:** nel 2026 il docente dice che in EoN "$`R_0`$ è calcolato come la proporzione $`I_0`$ su $`N`$" (`Teams 6 @ 0:56:41`). Nel codice `rho = I0/N` è la **frazione iniziale di infetti**; la variabile `r_0` è `beta/gamma` (e su rete non è il numero di riproduzione, vedi sezione 8).
> **Correzione:** il riferimento a "von Neumann del 2003 e Brower del 2008" (`Teams 6 @ 0:46:46`; nel 2025 "Neumann e Brouwer") va letto come Mark **Newman** (2003) e Fred **Brauer** (2008).
Dopo la pausa (`Teams 6 @ 1:07:19`) la lezione passa alla traccia del test finale: vedi **Assessment**.
## 11. Dal materiale ufficiale: `Epidemiology.ipynb`
Dal materiale ufficiale, non mostrato a lezione. È il SIR della "Freshman Plague" dell'Olin College (circa 90 nuovi studenti l'anno, di cui almeno uno porta un'infezione), probabilmente l'esempio del college citato nel 2026; il link alla fonte nel notebook è malformato (`https://https://...`).
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

N = 350. #Total number of individuals, N
I0, R0 = 1., 0 #Initial number of infected and recovered individuals
S0 = N - I0 - R0 #Susceptible individuals to infection initially is deduced
beta, gamma = 0.4, 0.1 #Contact rate and mean recovery rate
tmax = 160 #A grid of time points (in days)
Nt = 160
t = np.linspace(0, tmax, Nt+1)

def derivative(X, t):
    S, I, R = X
    dotS = -beta * S * I / N
    dotI = beta * S * I / N - gamma * I
    dotR = gamma * I
    return np.array([dotS, dotI, dotR])

X0 = S0, I0, R0 #Initial conditions vector
res = integrate.odeint(derivative, X0, t)
S, I, R = res.T
Seuil = 1 - 1 / (beta/gamma)

def Euler(func, X0, t):
    dt = t[1] - t[0]
    nt = len(t)
    X  = np.zeros([nt, len(X0)])
    X[0] = X0
    for i in range(nt-1):
        X[i+1] = X[i] + func(X[i], t[i]) * dt
    return X

Xe = Euler(derivative, X0, t)
# grafici: odeint, Eulero, confronto
```
(Import non usati, `numba` e `ipywidgets`, omessi.) `Seuil` ("soglia") è la soglia di immunità di gregge $`1 - 1/R_0`$ con $`R_0 = \beta/\gamma = 4`$.
Verificato per esecuzione: `Seuil` = 0.75; con `odeint` il picco è di 141.3 infetti al giorno 24, e alla fine risulta infettato il 98% della popolazione (S finale 6.9), in accordo con l'equazione della dimensione finale $`z = 1 - e^{-R_0 z}`$ ($`z = 0.980`$). Al picco $`S = 82.5`$, vicino alla soglia $`N\gamma/\beta = 87.5`$ (con passo di un giorno il campionamento non coglie esattamente l'istante). Eulero con passo 1 giorno dà un picco di 148.6 al giorno 26, con uno scarto massimo di 24.8 infetti da `odeint`.
> **Nota aggiunta:** la cella con `Nt = 100` prima di chiamare `Euler` non ha effetto, perché `t` è già stato calcolato con `Nt = 160`. Nei grafici l'asse del tempo è etichettato in secondi, ma l'unità sono i giorni.
## 12. Collegamento con il test finale
<table header-row="true">
<tr>
<td>Test finale 2026</td>
<td>Dove nel capitolo</td>
</tr>
<tr>
<td>Studi possibili con l'epidemiologia computazionale</td>
<td>sezioni 1, 6 (forecasting, nowcasting, scenari), 10</td>
</tr>
<tr>
<td>Elementi di complessità dell'epidemiologia</td>
<td>sezione 5 (patogeno, ospite, struttura sociale), 10</td>
</tr>
<tr>
<td>Assunzioni del SIR (indicate a voce come possibile domanda)</td>
<td>sezione 5 (`BT-04 @ 00:40:13`)</td>
</tr>
</table>
Il SIR su grafo e l'esercizio in tabella sono "non fondamentali" per il test (`BT-04 @ 01:14:29`, `01:16:48`).
## 13. Glossario, punti incerti, materiale usato
### Glossario
- **Epidemia, pandemia, endemia:** diffusione oltre l'atteso in una regione; epidemia su scala mondiale; infezioni costanti nella popolazione.
- **SIR:** modello compartimentale suscettibili-infetti-guariti (Kermack e McKendrick, 1927).
- **Soglia epidemica:** condizione $`\frac{\beta}{\gamma}S > 1`$ perché gli infetti crescano.
- $`R_0`$**, **$`R_t`$**:** numero medio di contagi di un infetto in una popolazione tutta suscettibile; lo stesso numero nella popolazione attuale.
- **Immunità di gregge:** quota di immuni $`1 - 1/R_0`$ oltre la quale $`R_t < 1`$.
- **Forecasting, nowcasting:** previsione a lungo termine; stima della situazione attuale o immediatamente futura.
- **Hub, super spreader:** nodi o eventi con molti contatti e impatto sproporzionato sulla diffusione.
- **Contact tracing:** ricostruzione dei contatti per interrompere le catene di trasmissione.
- **Watts-Strogatz:** modello di rete "small world" con clustering alto e cammini brevi.
- **Algoritmo di Gillespie:** simulazione stocastica esatta di processi a tempo continuo, usata da EoN.
### Punti incerti
- Chi abbia costruito il modello degli Stati Uniti con 34 dataset e 300 milioni di persone (`BT-04 @ 00:44:43`): il docente dice "io ho provato a estenderlo" \[?\].
- Nomi trascritti male e corretti nel testo: "Merler" → Stefano Merler; "Paolo Crepè" → Paolo Crepet; "che armac e mack kendrick", "Kermic-McHenry" → Kermack e McKendrick; "Anopheles gambia" → *Anopheles gambiae*; "Neumann e Brouwer" → Newman e Brauer; "VATS e STROGATS" → Watts-Strogatz; "network hicks" → NetworkX; "ION" → EoN; "modello di germ" → Jerne.
### Materiale usato
- Fotogrammi `BT-04` delle slide (`00:09:20`, `00:11:26`, `00:17:01`, `00:25:08`, `00:27:58`, `00:29:34`, `00:41:41`, `00:46:26`, `00:48:54`, `00:50:19`, `01:11:22`, `01:15:36`, `01:16:40`)
- `Materiale/Teams/colab/SIR_ABMS.ipynb`, `SIR_Network.ipynb`, `Epidemiology.ipynb`
- `Materiale/Teams/Test_Finale_BDP_26.pdf`
- Registrazione `Teams 6` (25/05/2026) fino a `0:57:41`, trascrizione Stream
- Verifica: `verifica_bt04.py` (MESA 0.9, SciPy) e `verifica_bt04_network.py` (EoN 1.2)
