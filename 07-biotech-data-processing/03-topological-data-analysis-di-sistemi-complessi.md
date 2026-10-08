# 03 - Topological Data Analysis di sistemi complessi

> Fonte Notion: https://app.notion.com/p/3e912abc808d8119a894d5d295fe2cf7 — ultima modifica 2026-09-28T18:06:30.086Z

**Registrazione:** `BT-03` (portale, edizione 2025), durata 01:19:43. Giornata: **Day 4**.
**Materiale:** slide `TDA.pdf` ("A new paradigm for modeling and analyzing complex systems", portale e Teams, file identici); notebook `MESA_KURAMOTO.ipynb`, `MESA_KURAMOTO_persistent_entropy_persim.ipynb`, `MESA_VICSEK_persistent_entropy_final.ipynb`, `Jerne.ipynb`, `mapper_quickstart.ipynb`. A schermo anche `MESA_VICSEK.ipynb` e `mapper_tda_tutorial.ipynb`, **non tra i materiali** (codice dai fotogrammi).
**Teams 2026:** `Teams 4` (21/05/2026), sezione 11.
> **Nota sul codice.** I notebook di Teams coincidono con quelli a schermo nelle funzioni; cambiano i parametri, che il docente modifica in diretta. Come nei capitoli precedenti: funzioni dal notebook, parametri dal video. Tutto il codice è verificato per esecuzione (`mesa==0.9.0`, `ripser` 0.6, `persim` 0.3.8, `kmapper` 2.1, `giotto-tda` 0.6.2).
## Indice
1. Dall'analisi dei modelli all'analisi dei dati
2. Modellare un sistema complesso
3. Modello di Kuramoto
4. Modello di Vicsek
5. Rete idiotipica di Jerne
6. Topological Data Analysis
7. Mapper
8. Omologia persistente
9. Entropia persistente
10. Esperimenti: TDA su Kuramoto e Vicsek
11. Integrazione Teams 2026
12. Collegamento con il test finale
13. Glossario, punti incerti, materiale usato
---
## 1. Dall'analisi dei modelli all'analisi dei dati
`BT-03 @ 00:00:10`
Le lezioni precedenti hanno mostrato come **costruire** modelli di sistemi complessi (equazioni differenziali e agenti); questa si occupa di come **analizzare i dati** che i sistemi complessi producono. I sistemi complessi sono molto eterogenei, per entità e per dinamica, e la statistica classica può non bastare a descriverli. Negli ultimi vent'anni circa si è aggiunto uno strumento basato sulla **topologia**, la branca della matematica "affine alla geometria" che studia le forme e come variano: si associano **forme ai dati**. Nel corso i dati sono generati da simulazioni ad agenti (`BT-03 @ 00:01:52`).
Slide "Complex Systems – key features" (`BT-03 @ 00:03:29`):
- "Complex systems may arise and evolve through self-organization, such that they are neither completely regular nor completely random, permitting the development of emergent behavior at macroscopic scales."
- **True-concurrency**: le entità possono compiere simultaneamente due o più azioni sulla stessa risorsa. Il docente: è ciò che l'informatica prova a emulare con le astrazioni del parallelismo (i sistemi operativi); esempio biologico, le cellule immunitarie che combattono gli antigeni e intanto stimolano la produzione di cellule simili (`BT-03 @ 00:06:22`).
- **Sistema dinamico**: sistema i cui stati sono specificati da un insieme di variabili e il cui comportamento è descritto da regole predefinite; modellarlo significa identificare variabili chiave e regole.
- **Emergenza**: relazione non banale tra proprietà microscopiche e macroscopiche; le proprietà macroscopiche sono emergenti quando è difficile spiegarle da quelle microscopiche.
- **Auto-organizzazione**: processo dinamico con cui un sistema forma spontaneamente strutture o comportamenti macroscopici non banali.
In biologia l'auto-organizzazione si vede nella formazione delle strutture cellulari, nel comportamento coordinato tra organismi, nelle reti neurali e nel sistema immunitario; nelle biotecnologie servono per capire ciclo cellulare e reti di segnalazione tra proteine, dove una semplice interazione molecolare può dare risposte sistemiche (`BT-03 @ 00:07:30`).
## 2. Modellare un sistema complesso
`BT-03 @ 00:08:08`
**Requirements driven e data driven.** Il docente osserva che spesso si confondono intelligenza artificiale e machine learning. Progettare un sistema di ML parte da requisiti sui dati e sulle prestazioni (per esempio un classificatore sopra una certa accuratezza), che in pratica si traducono in un dataset di training ben fatto: il requisito vero "si enuncia nel dataset". È un cambio rispetto allo sviluppo software classico, **requirements driven**, in cui i requisiti funzionali e non funzionali costituiscono un modello del sistema (`BT-03 @ 00:10:52`). Secondo il docente farsi guidare solo dai dati è rischioso: per un sistema che identifica una patologia bisogna chiedersi anche in che contesto verrà usato, online o offline, con che tempi di risposta, con quali altri componenti interagisce. In entrambi i casi, descrivere un sistema significa **costruire modelli**.
**L'arte di modellare**, slide "The art of modeling": "model" significa "a simplified description, of a system or process, to assist representations, calculations and predictions". Una storia antica: Aristotele (origine del metodo scientifico), Roger Bacon (solo un ciclo ripetuto di osservazioni porta al modello giusto), Galileo ("Dialoghi intorno a due nuove scienze", approccio metodologico), Francis Bacon ("Novum Organum"), Cartesio (metodo sperimentale).
**Come modellare un sistema complesso**, slide "How to model a complex systems?" (`BT-03 @ 00:14:52`):
- **descriptive modeling**: si specifica lo stato del sistema a uno o più istanti;
- **rule-based modeling**: si cercano regole dinamiche che spieghino il comportamento osservato, con due famiglie:
	- **top-down**: equazioni alle differenze (tempo discreto), equazioni differenziali (tempo continuo);
	- **bottom-up**: statistiche di reti complesse (distribuzione dei gradi), automi cellulari, modelli ad agenti.
In biologia il top-down descrive la dinamica di popolazioni cellulari, il bottom-up interazioni specifiche come le simulazioni molecolari. Il docente aggiunge un terzo caso: un sistema che non è descritto né da equazioni né da regole ma **genera dati** (uno stormo, la risposta immunitaria a un farmaco, un vaccino, un patogeno). Se si parte da dati reali, come le concentrazioni di anticorpi, la domanda è: **si può generare un modello dai dati?** Sì, e la lezione presenta uno strumento "di nicchia, un po' ostico" per farlo (`BT-03 @ 00:16:04`).
Slide "Modeling of Complex Systems": *Why?* "For extracting new information from real-life emerging phenomena that otherwise can not be pinpointed out". *How?* "By combining Agent Based Modelling and Simulation and Topological Data Analysis". La TDA chiude il collegamento mancante tra osservazioni e modello (`BT-03 @ 00:18:20`). "Topologia" viene da *topos* e *logos*, lo studio dei luoghi.
Prima si costruiscono tre modelli ad agenti come **generatori di dati** (Kuramoto, Vicsek, Jerne), poi li si analizza con la TDA (`BT-03 @ 00:19:31`).
## 3. Modello di Kuramoto
`BT-03 @ 00:19:31`
Descrive l'accoppiamento di oscillatori, usato come metafora delle sincronizzazioni biologiche: ritmo circadiano, neuroni, cellule del cuore. Racconto meccanicistico del docente: metronomi su un piano comune, avviati a caso e quindi asincroni; dopo un po' oscillano tutti in sincronia. Un'ipotesi in neuroscienze è che l'**epilessia** sia un'iper-sincronizzazione del cervello, in cui tutti i neuroni oscillano insieme; in teoria per interromperla basterebbe isolare almeno un gruppo di colonne corticali, cosa tutt'altro che facile (`BT-03 @ 00:21:50`).
Slide "Modello di Kuramoto": "descrive la dinamica di un sistema di N oscillatori accoppiati, ognuno caratterizzato da una fase θi(t) al tempo t e da una frequenza propria ωi, indipendente dal tempo."
$$
\frac{d\theta_i}{dt} = \omega_i + \frac{1}{N}\sum_{j=1}^{N} K_{ij}\sin(\theta_j - \theta_i), \qquad i = 1 \dots N
$$
$`K_{ij}`$ è il **coefficiente di accoppiamento**: per i metronomi, il piano comune; per oscillatori legati da una molla, la forza della molla (`BT-03 @ 00:23:55`). Il modello si può risolvere come ODE o simulare ad agenti con MESA, come qui. Il docente precisa che in questa lezione Kuramoto serve come **generatore di dati**, non per studiarlo in sé (`BT-03 @ 00:25:04`).
**Colab** (`MESA_KURAMOTO.ipynb`, `BT-03 @ 00:25:34`): una sola classe di agenti, l'oscillatore.
```python
from mesa import Agent, Model
from mesa.time import SimultaneousActivation
from mesa.space import ContinuousSpace
import numpy as np
import matplotlib.pyplot as plt


class Oscillator(Agent):
    def __init__(self, unique_id, model, omega, phase):
        super().__init__(unique_id, model)
        self.omega = omega  # Natural frequency
        self.phase = phase  # Initial phase

    def step(self):
        # Update phase based on Kuramoto model
        coupling_strength = self.model.K / self.model.num_oscillators
        phase_diff_sum = sum(np.sin(other.phase - self.phase) for other in self.model.schedule.agents)
        self.phase += self.omega + coupling_strength * phase_diff_sum

    def advance(self):
        pass


class KuramotoModel(Model):
    def __init__(self, N, K, omega_range=(0.8, 1.2)):
        self.num_oscillators = N
        self.K = K  # Coupling constant
        self.schedule = SimultaneousActivation(self)
        self.omega_range = omega_range
        self.phases_over_time = []  # Store the phases at each time step
        self.r_over_time = []  # Store the synchronization coefficient over time

        # Create agents (oscillators) with random natural frequencies and phases
        for i in range(self.num_oscillators):
            omega = np.random.uniform(*omega_range)
            phase = np.random.uniform(0, 2 * np.pi)
            oscillator = Oscillator(i, self, omega, phase)
            self.schedule.add(oscillator)

    def step(self):
      self.schedule.step()

      # Extract phases and calculate synchronization coefficient
      phases = np.array([agent.phase for agent in self.schedule.agents])
      self.phases_over_time.append(phases)

      # Compute the synchronization coefficient (order parameter r(t))
      r = np.abs(np.mean(np.exp(1j * phases)))  # This is the magnitude of the order parameter
      self.r_over_time.append(r)
```
```python
# Parameters for the simulation
N = 100  # Number of oscillators
K = 1.0  # Coupling constant
steps = 100  # Number of time steps to run the simulation

# Run the Kuramoto model
model = KuramotoModel(N, K)
for i in range(steps):
    model.step()

# Plot the synchronization coefficient r(t) over time
plt.plot(model.r_over_time)
plt.xlabel('Time')
plt.ylabel('Synchronization Coefficient (r)')
plt.title('Synchronization Coefficient Over Time in the Kuramoto Model')
plt.grid(True)
plt.show()
```
Il modello crea N agenti con fase e frequenza casuali (frequenze uniformi in \[0.8, 1.2\]). Il **coefficiente di sincronizzazione** è il parametro d'ordine $`r(t) = \left|\frac{1}{N}\sum_j e^{i\theta_j}\right|`$, una misura globale: vale 0 per fasi sparse in modo uniforme e 1 per fasi coincidenti. Con 100 oscillatori e $`K = 1`$ il sistema si sincronizza dopo circa 15 step e da lì si comporta "come un unico grande oscillatore"; con $`K = 0.5`$ il tempo di sincronizzazione aumenta, con un punto di flesso (`BT-03 @ 00:26:44`).
Verificato per esecuzione (10 seed): con $`K = 1`$ si arriva al 95% del valore di regime in una mediana di 12 step, con $`K = 0.5`$ in 25.5 step; in entrambi i casi $`r`$ si assesta attorno a 0.87.
Il docente anticipa un risultato "controintuitivo": se $`K`$ supera una certa soglia il sistema resta caotico e non si sincronizza (`BT-03 @ 00:27:53`).
> **Correzione:** nel modello di Kuramoto, a tempo continuo, un accoppiamento più forte **aumenta** la sincronizzazione (oltre la soglia critica $`r \to 1`$ al crescere di $`K`$). Il comportamento visto nel notebook è un **artefatto numerico**: l'aggiornamento `self.phase += self.omega + ...` è un passo di Eulero con $`\Delta t = 1`$, troppo grande quando $`K`$ è grande. Verificato: con lo stesso schema, $`r`$ di regime scende da 0.87 ($`K = 1`$) a 0.60 ($`K = 3`$) e 0.29 ($`K = 10`$); integrando le stesse equazioni con $`\Delta t = 0.05`$ si ottiene $`r \approx 1.00`$ per $`K = 3, 6, 10`$.
> **Nota aggiunta:** `SimultaneousActivation` in MESA chiama prima `step()` di tutti gli agenti e poi `advance()`, per aggiornare lo stato in modo simultaneo. Qui `step()` modifica subito `self.phase` e `advance()` è vuoto: gli oscillatori usano fasi già aggiornate da altri nello stesso tick, cioè l'aggiornamento è di fatto **sequenziale**. Verificato: con aggiornamento davvero simultaneo e $`K = 0.5`$ il valore di regime è 0.97 invece di 0.87. Per la correttezza basta calcolare la nuova fase in `step()` in una variabile e assegnarla in `advance()`.
## 4. Modello di Vicsek
`BT-03 @ 00:29:06`
Introdotto in fisica statistica per particelle interagenti, si applica alla **materia attiva** in biologia: movimento di batteri o di cellule tumorali, cioè come un gruppo di elementi biologici si organizza in modo coordinato. Slide "Modello di Vicsek": "un modello matematico utilizzato per descrivere in modo semplificato (un toy model) la materia attiva. Permette di studiare il moto di particelle dotate di forze attrattive e repulsive confinate in uno spazio chiuso (bounding box)".
Descrizione del docente: particelle in una scatola, ciascuna con una forza attrattiva e repulsiva; lasciate libere, dopo un po' formano **cluster**, in un tempo che dipende dalla dimensione della scatola e dall'intensità delle forze (`BT-03 @ 00:29:46`).
**Colab** (`MESA_VICSEK.ipynb` a schermo, `MESA_VICSEK_persistent_entropy_final.ipynb` su Teams, stesso codice, `BT-03 @ 00:31:27`):
```python
import numpy as np
import matplotlib.pyplot as plt
from mesa import Agent, Model
from mesa.time import SimultaneousActivation
from mesa.space import ContinuousSpace
import warnings

# Suppress UserWarnings (like the one about placing agents at the same position)
warnings.filterwarnings("ignore", category=UserWarning)


class VicsekAgent(Agent):
    def __init__(self, unique_id, model, pos, velocity, noise):
        super().__init__(unique_id, model)
        self.pos = np.array(pos)
        self.velocity = np.array(velocity)
        self.noise = noise
        self.speed = 1.0  # Constant speed

    def step(self):
        # Find neighbors within a certain vision radius
        neighbors = self.model.space.get_neighbors(self.pos, self.model.vision, False)
        if len(neighbors) > 0:
            avg_direction = np.mean([neighbor.velocity for neighbor in neighbors], axis=0)
            avg_direction /= np.linalg.norm(avg_direction)
        else:
            avg_direction = self.velocity

        # Add noise to the direction
        angle_noise = np.random.uniform(-self.noise, self.noise)
        rotation_matrix = np.array([[np.cos(angle_noise), -np.sin(angle_noise)],
                                    [np.sin(angle_noise), np.cos(angle_noise)]])
        new_velocity = np.dot(rotation_matrix, avg_direction)
        self.velocity = new_velocity / np.linalg.norm(new_velocity)

    def advance(self):
        # Move the agent according to its velocity
        new_position = self.pos + self.velocity * self.speed
        self.model.space.move_agent(self, new_position)


class VicsekModel(Model):
    def __init__(self, N, width, height, noise, vision):
        self.positions_over_time = []  # To store positions over time
        self.num_agents = N
        self.vision = vision
        self.noise = noise

        # Create a continuous space where the agents move
        self.space = ContinuousSpace(width, height, torus=True)  # Wrap around
        self.schedule = SimultaneousActivation(self)

        # Store synchronization coefficient over time
        self.r_over_time = []

        # Create agents
        for i in range(self.num_agents):
            pos = np.random.rand(2) * [width, height]  # Random 2D position
            angle = np.random.rand() * 2 * np.pi  # Random initial direction
            velocity = np.array([np.cos(angle), np.sin(angle)])  # Unit velocity vector
            agent = VicsekAgent(i, self, pos, velocity, noise)
            self.schedule.add(agent)
            self.space.place_agent(agent, pos)

    def step(self):
        # Capture positions at each time step
        positions = np.array([agent.pos for agent in self.schedule.agents])
        self.positions_over_time.append(positions)
        self.schedule.step()

        # Compute synchronization coefficient (alignment order parameter)
        velocities = np.array([agent.velocity for agent in self.schedule.agents])
        avg_velocity = np.mean(velocities, axis=0)
        r = np.linalg.norm(avg_velocity) / self.num_agents
        self.r_over_time.append(r)
```
```python
num_agents = 100  # Number of agents
width = 50  # Width of the environment
height = 50  # Height of the environment
noise = 0.1  # Noise level
vision = 10  # Vision radius for neighbors

model = VicsekModel(num_agents, width, height, noise, vision)

# Run the model for 200 time steps
steps = 200
for i in range(steps):
    model.step()
# poi il grafico di model.r_over_time, come per Kuramoto
```
Ogni particella ha posizione, velocità, rumore; a ogni step guarda i vicini entro il raggio di visione, calcola la nuova direzione e si sposta (`step` calcola, `advance` muove: qui l'aggiornamento è davvero simultaneo). Il coefficiente di sincronizzazione, analogo a quello di Kuramoto, per il docente misura una sincronizzazione **spaziale**: le particelle si raggruppano attorno a un punto e si muovono all'unisono (`BT-03 @ 00:32:30`). Con una bounding box molto più ampia i tempi cambiano, o le particelle non si raggruppano mai perché hanno "un orizzonte infinito" rispetto alla forza di attrazione (`BT-03 @ 00:33:00`). Nel video la scatola è 50×50; il notebook di Teams ha 100×100.
> **Correzione:** il codice **non contiene forze attrattive o repulsive**. È il modello di Vicsek standard: ogni particella, a velocità costante, adotta la direzione media dei vicini entro il raggio `vision`, perturbata da un rumore angolare. Il parametro d'ordine misura quindi l'**allineamento delle velocità** (tutti nella stessa direzione), non il raggruppamento attorno a un punto; gruppi compatti possono emergere come effetto dell'allineamento, ma non sono ciò che $`r`$ misura.
> **Correzione:** nel codice `r = np.linalg.norm(avg_velocity) / self.num_agents` divide per N una media già calcolata: il parametro d'ordine di Vicsek è $`\varphi = \left|\frac{1}{N}\sum_i \mathbf{v}_i\right|`$, compreso fra 0 e 1, mentre qui $`r \le 1/N`$. Per questo il grafico a schermo ha valori fra 0.0005 e 0.0028 (`BT-03 @ 00:33:47`). Verificato: con N = 100 e scatola 50×50 o 100×100, $`\varphi`$ passa da circa 0.03-0.33 a 0.99-1.00 in 200 step (allineamento completo), mentre $`r`$ del notebook non supera 0.01. Con scatola 500×500 $`\varphi`$ resta attorno a 0.1.
## 5. Rete idiotipica di Jerne
`BT-03 @ 00:34:02`
Il terzo generatore di dati è il **sistema immunitario**, nel modello più antico e semplice: la rete idiotipica di Jerne. Slide "Sistema immunitario: rete idiotipica di Jerne": "è una teoria che descrive il sistema immunitario come una rete dinamica di anticorpi che non solo riconoscono antigeni esterni ma anche altri anticorpi attraverso gli idiotipi (le regioni variabili degli anticorpi). Questa interazione tra anticorpi crea una rete regolatoria che contribuisce all'autoregolazione del sistema immunitario." La figura mostra B-cell $`i-1`$, $`i`$, $`i+1`$ con i rispettivi anticorpi e frecce di stimolazione e soppressione.
**La dinamica** raccontata dal docente (`BT-03 @ 00:35:13`): se l'antigene è già noto, il sistema produce un anticorpo di forma complementare che si aggancia e lo sopprime, "come un puzzle". Se è nuovo, usa anticorpi che approssimano la forma complementare, ma perde la battaglia mentre l'antigene prolifera; produce allora anticorpi sempre più adatti, finché si ritrova con anticorpi che sono sia il complementare dell'antigene sia l'**immagine** dell'antigene, e combatte anche i propri anticorpi. A quel punto interrompe la produzione e **cristallizza la conoscenza** nella memoria immunitaria (`BT-03 @ 00:37:09`).
**Il modello ad agenti** (`BT-03 @ 00:37:42`): due classi di agenti.
- **Anticorpo**: idiotipo unico, riconoscibile da altri anticorpi o antigeni; può proliferare, legarsi ad antigeni o anticorpi, decadere.
- **Antigene**: molecola estranea che stimola la risposta, con un proprio idiotipo.
Interazioni: **legame anticorpo-antigene** (idiotipi complementari, stimola la proliferazione dell'anticorpo) e **legame anticorpo-anticorpo** (regola l'attività per proliferazione o soppressione). Dinamiche di sistema: **proliferazione**, **soppressione** da parte di anticorpi anti-idiotipici, **decadimento** in assenza di stimolo. Parametri: concentrazioni iniziali, tassi di legame, proliferazione, soppressione e decadimento, soglia di affinità tra idiotipi (`BT-03 @ 00:40:34`). Un modello complessivo `ImmuneSystemModel` gestisce agenti, interazioni e avanzamento, con un DataCollector. Si installa anche **Plotly**, libreria per grafici interattivi, "un'estensione di Matplotlib" (`BT-03 @ 00:42:15`).
**Colab** (`Jerne.ipynb`, `BT-03 @ 00:42:52`):
```python
from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
import random
import math
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


class AntibodyAgent(Agent):
    def __init__(self, unique_id, model, idiotype, pos):
        super().__init__(unique_id, model)
        self.idiotype = idiotype  # Idiotipo dell'anticorpo
        self.concentration = 1.0  # Concentrazione iniziale
        self.pos = pos  # Posizione iniziale sulla griglia

    def step(self):
        # Decadimento naturale
        self.concentration *= self.model.decay_rate

        # Evitare concentrazioni negative
        if self.concentration < 0:
            self.concentration = 0

        # Movimento (diffusione)
        self.move()

        # Interazioni con antigeni nello stesso cella
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        for agent in cellmates:
            if isinstance(agent, AntigenAgent):
                affinity = self.calculate_affinity(agent.idiotype)
                if random.random() < affinity:
                    # Proliferazione in risposta al legame con l'antigene
                    self.concentration += self.model.proliferation_rate

            elif isinstance(agent, AntibodyAgent) and agent != self:
                # Interazione con altri anticorpi
                affinity = self.calculate_affinity(agent.idiotype)
                if random.random() < affinity:
                    # Soppressione a causa del legame con anti-idiotipi
                    self.concentration -= self.model.suppression_rate

        # Evitare concentrazioni negative
        if self.concentration < 0:
            self.concentration = 0

        # Rimozione dell'anticorpo se la concentrazione è troppo bassa
        if self.concentration < self.model.minimum_concentration:
            self.model.grid.remove_agent(self)
            self.model.schedule.remove(self)

    def move(self):
        # L'anticorpo si muove in una posizione adiacente casuale (diffusione)
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=True)
        new_position = random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def calculate_affinity(self, other_idiotype):
        # Calcolo dell'affinità basato sulla distanza tra gli idiotipi
        affinity = math.exp(-abs(self.idiotype - other_idiotype) * self.model.affinity_scale)
        return affinity


class AntigenAgent(Agent):
    def __init__(self, unique_id, model, idiotype, pos):
        super().__init__(unique_id, model)
        self.idiotype = idiotype  # Idiotipo dell'antigene
        self.pos = pos  # Posizione sulla griglia

    def step(self):
        # Possiamo implementare una logica per gli antigeni se necessario
        pass
```
```python
class ImmuneSystemModel(Model):
    def __init__(self, N, initial_antigens, grid_width, grid_height, antigen_schedule):
        self.num_agents = N
        self.grid = MultiGrid(grid_width, grid_height, torus=True)
        self.schedule = RandomActivation(self)
        self.running = True
        self.current_step = 0  # Traccia il passo corrente per l'introduzione di antigeni

        # Parametri del modello
        self.decay_rate = 0.99  # Tasso di decadimento degli anticorpi
        self.proliferation_rate = 0.1  # Tasso di proliferazione
        self.suppression_rate = 0.05  # Tasso di soppressione
        self.minimum_concentration = 0.1  # Concentrazione minima prima della rimozione
        self.affinity_scale = 5  # Scala per il calcolo dell'affinità

        # Creare gli anticorpi iniziali
        for i in range(self.num_agents):
            idiotype = random.uniform(0, 1)
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            pos = (x, y)
            antibody = AntibodyAgent(i, self, idiotype, pos)
            self.schedule.add(antibody)
            self.grid.place_agent(antibody, pos)

        # ID unico per gli antigeni
        self.antigen_id = self.num_agents

        # Creare gli antigeni iniziali
        self.antigen_schedule = antigen_schedule  # Dizionario {step: [lista di antigeni]}
        self.add_antigens(initial_antigens)

        # Inizializzare il DataCollector
        self.datacollector = DataCollector(
            agent_reporters={"Concentration": "concentration", "Idiotype": "idiotype", "AgentType": lambda a: type(a).__name__, "x": lambda a: a.pos[0], "y": lambda a: a.pos[1]}
        )

    def add_antigens(self, antigens):
        for idiotype in antigens:
            x = random.randrange(self.grid.width)
            y = random.randrange(self.grid.height)
            pos = (x, y)
            antigen = AntigenAgent(self.antigen_id, self, idiotype, pos)
            self.schedule.add(antigen)
            self.grid.place_agent(antigen, pos)
            self.antigen_id += 1

    def step(self):
        # Controllare se ci sono antigeni da aggiungere in questo passo
        if self.current_step in self.antigen_schedule:
            new_antigens = self.antigen_schedule[self.current_step]
            self.add_antigens(new_antigens)

        self.datacollector.collect(self)
        self.schedule.step()
        self.current_step += 1


# Pianificazione degli antigeni: {passo temporale: [lista di idiotipi degli antigeni]}
antigen_schedule = {
    10: [0.3, 0.7],  # Al passo 10, introdurre due antigeni con questi idiotipi
    50: [0.1],       # Al passo 50, introdurre un antigene
    80: [0.9]        # Al passo 80, introdurre un altro antigene
}

# Parametri iniziali della simulazione
num_anticorpi = 100  # Numero di anticorpi
antigeni_iniziali = [0.5]  # Idiotipi degli antigeni iniziali
grid_width = 20
grid_height = 20

model = ImmuneSystemModel(num_anticorpi, antigeni_iniziali, grid_width, grid_height, antigen_schedule)
for i in range(100):
    model.step()
```
Il docente sottolinea i controlli sulla concentrazione, che non può essere negativa, e la pianificazione di **nuovi antigeni** in tempi successivi, per stimolazioni ripetute (`BT-03 @ 00:43:25`). Dopo 100 step si estraggono i dati del DataCollector, si tengono solo anticorpi e antigeni e si fanno due grafici Plotly: un grafico **spaziale animato** (anticorpi colorati per idiotipo, dimensione proporzionale alla concentrazione, antigeni come croci rosse) e le **serie temporali** delle concentrazioni degli anticorpi (`BT-03 @ 00:44:04`). A schermo le concentrazioni partono da 1 e scendono per quasi tutti gli anticorpi, a gradini.
Suggerimento per attività successive e per il test finale: cambiare tipo e numero di anticorpi, idiotipo dell'antigene iniziale e simili (`BT-03 @ 00:44:38`).
> **Nota aggiunta:** tre osservazioni sul modello, verificate per esecuzione (3 seed). (1) L'affinità `exp(-|id_1 - id_2| * 5)` è massima per idiotipi **uguali**: la "complementarità" è codificata come vicinanza numerica. Di conseguenza la soppressione anticorpo-anticorpo colpisce anticorpi con idiotipo simile, cioè dello stesso tipo, mentre in Jerne gli anti-idiotipi sono quelli complementari. (2) Gli antigeni non proliferano, non vengono neutralizzati e restano per sempre; le interazioni avvengono solo fra agenti nella **stessa cella** della griglia 20×20. (3) La soppressione domina: in 100 step circa 700 eventi di soppressione contro 20-30 di proliferazione. Nessun anticorpo supera la concentrazione iniziale (massimo 0.31-0.53), e ne vengono rimossi 26-34 su 100. Con il solo decadimento servirebbero 230 step per scendere sotto 0.1 ($`0.99^{100} = 0.37`$): le rimozioni in 100 step sono dovute alla soppressione. Gli anticorpi che "restano" non sono quindi quelli che hanno legato meglio l'antigene, ma quelli meno soppressi.
## 6. Topological Data Analysis
`BT-03 @ 00:45:50`
Slide "Topological Data Analysis": la sequenza di immagini che trasforma una **tazza in una ciambella**. La TDA offre strumenti matematici per esaminare dati complessi ad alta dimensione; nelle biotecnologie si applica a reti di interazione molecolari e dati genomici. Una caratteristica: la topologia **non richiede una metrica**; più precisamente alcuni algoritmi topologici si possono usare senza una metrica di riferimento, al contrario di quanto siamo abituati a fare misurando le distanze (`BT-03 @ 00:46:25`).
Da un punto di vista **omologico**, tazza e ciambella sono equivalenti perché hanno lo stesso numero di buchi (il buco della ciambella corrisponde al manico), a condizione che la trasformazione sia **continua** e preservi i buchi in ogni passaggio (`BT-03 @ 00:47:37`). Il docente anticipa che il toro ha più "buchi" di quanti se ne vedano (sezione 8). Questi concetti servono per raggruppare e confrontare dati, e anche per studiare sistemi **tempo-dipendenti**.
Slide "Applications of TDA and Input data type": sistemi immunitari, dati clinici, dati biologici, dati cosmologici e teoria delle stringhe, molti altri. Tipi di input: (time-dependent) point cloud data, (time-dependent) weighted networks, strings (`BT-03 @ 00:49:20`).
Due famiglie di algoritmi: **Mapper** e **omologia persistente**.
## 7. Mapper
`BT-03 @ 00:50:26`
Slide "TDA for data high-dimensional data analysis: Mapper", con la figura della mano:
- **Lens**: una funzione che proietta i dati ad alta dimensione in dimensione minore (PCA, t-SNE o altre proiezioni);
- **Clustering Algorithm**: DBSCAN raggruppa i punti in ogni regione della copertura;
- **Cover**: una suddivisione dello spazio proiettato in regioni sovrapposte (cubi) per costruire il grafo di Mapper.
Il racconto del docente sulla figura (`BT-03 @ 00:50:57`): (A) la scansione 3D di una mano, ogni punto rosso è un punto 3D; (B) una **funzione filtro**, per esempio la distanza dal centro della mano, che colora i punti; (C) i punti raggruppati per valore del filtro, come in un istogramma i cui bin si sovrappongono, per cui alcuni punti cadono in due bin; (D) ogni bin diventa un vertice e due bin con almeno un punto in comune sono collegati da un arco. Da una nuvola 3D fitta si passa a un **grafo** che riduce la dimensionalità ma preserva le caratteristiche geometriche.
> **Correzione:** nella descrizione a voce manca il passo di **clustering**, che la slide invece nomina. In Mapper i vertici non sono i bin: per ogni intervallo della copertura si prendono i punti la cui immagine cade nell'intervallo (la controimmagine) e li si divide in cluster (per esempio con DBSCAN); **ogni cluster** è un vertice, e due vertici sono collegati se i cluster hanno punti in comune. Senza il clustering dita e palmo nello stesso intervallo di distanza finirebbero nello stesso nodo. Nel 2026 il docente descrive il passo correttamente (sezione 11).
**Colab con giotto-tda** (`mapper_quickstart.ipynb`, `BT-03 @ 00:53:47`): il notebook di esempio di giotto-tda, con link di approfondimento. Dataset: due cerchi concentrici in 2D.
```python
!pip install giotto-tda

# Data wrangling
import numpy as np
import pandas as pd  # Not a requirement of giotto-tda, but is compatible with the gtda.mapper module

# Data viz
from gtda.plotting import plot_point_cloud

# TDA magic
from gtda.mapper import (
    CubicalCover,
    make_mapper_pipeline,
    Projection,
    plot_static_mapper_graph,
    plot_interactive_mapper_graph,
    MapperInteractivePlotter
)

# ML tools
from sklearn import datasets
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA

data, _ = datasets.make_circles(n_samples=5000, noise=0.05, factor=0.3, random_state=42)
plot_point_cloud(data)

# Define filter function – can be any scikit-learn transformer
filter_func = Projection(columns=[0, 1])
# Define cover
cover = CubicalCover(n_intervals=10, overlap_frac=0.3)
# Choose clustering algorithm – default is DBSCAN
clusterer = DBSCAN()

# Configure parallelism of clustering step
n_jobs = 1

# Initialise pipeline
pipe = make_mapper_pipeline(
    filter_func=filter_func,
    cover=cover,
    clusterer=clusterer,
    verbose=False,
    n_jobs=n_jobs,
)

fig = plot_static_mapper_graph(pipe, data)
fig.show(config={'scrollZoom': True})
```
Il grafo perde la concentricità ma ritrova le **due strutture circolari**, sa quali punti stanno in ogni nodo ed è interattivo (`BT-03 @ 00:55:31`). La concentricità si può ignorare perché in topologia conta il numero di buchi: la struttura ha due buchi, e spostando il cerchio piccolo fuori dal grande resterebbero due; conta che ci siano curve chiuse, circolari, quadrate o triangolari che siano (`BT-03 @ 00:56:10`). Alla domanda se anche i triangoli fra i nodi siano buchi, il docente risponde di no: in topologia un triangolo equivale a una **faccetta piena**, un simplesso di dimensione 2, non disegnato pieno per non appesantire il grafico (`BT-03 @ 00:57:17`).
Verificato per esecuzione (giotto-tda 0.6.2): il grafo ha 90 nodi, 228 archi e **2 componenti connesse**, una per cerchio. Il gran numero di triangoli spiega perché vanno considerati pieni: contando i cicli del solo grafo se ne troverebbero 140.
**Colab con KeplerMapper** (`mapper_tda_tutorial.ipynb`, non tra i materiali, `BT-03 @ 00:58:23`): Mapper sul dataset **Iris** (vettori di 4 caratteristiche di petali e sepali), stavolta con la libreria KeplerMapper.
```python
!pip install kmapper scikit-learn matplotlib

import kmapper as km
import sklearn
from sklearn import datasets
# [illeggibile] altri import non inquadrati: PCA, DBSCAN, networkx, matplotlib
from sklearn.decomposition import PCA
from sklearn.cluster import DBSCAN
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Load and Preprocess Data
data, labels = datasets.load_iris(return_X_y=True)
scaler = sklearn.preprocessing.MinMaxScaler()
data_scaled = scaler.fit_transform(data)

# Step 2: Initialize KeplerMapper
mapper = km.KeplerMapper(verbose=1)

# Step 3: Create Lens Function using PCA
lens = PCA(n_components=2).fit_transform(data_scaled)

# Step 4: Apply the Mapper Algorithm
graph = mapper.map(lens, data_scaled, clusterer=DBSCAN(eps=0.3, min_samples=5), cover=km.Cover(n_cubes=10, perc_overlap=0.5))

# Step 5: Visualize the Result
mapper.visualize(graph, path_html="mapper_output.html", title="Mapper Output for Iris Dataset")

# grafo statico con networkx
G = nx.Graph()
for node in graph['nodes']:   # [illeggibile] riga ricostruita
    G.add_node(node)
for node, neighbors in graph['links'].items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Draw the graph
nx.draw(G, with_labels=True, node_color='skyblue', node_size=500, edge_color='gray', font_weight='bold')
plt.show()
```
L'output HTML interattivo si può scaricare; in Colab il docente mostra il grafo statico, "meno accattivante" di giotto (`BT-03 @ 00:59:48`). Secondo il docente Mapper ha identificato automaticamente **due grandi classi di fiori** (`BT-03 @ 01:00:24`).
Verificato per esecuzione: "Created 92 edges and 36 nodes", come a schermo; il grafo ha 2 componenti: una di 12 nodi con 48 fiori tutti *setosa*, una di 24 nodi con 49 *versicolor* e 46 *virginica*.
> **Nota aggiunta:** Iris ha **tre** specie. Le due componenti del grafo separano *setosa*, linearmente separabile dalle altre, da *versicolor* + *virginica*, che si sovrappongono nello spazio delle caratteristiche. Il risultato è corretto come struttura dei dati, ma non è una classificazione delle specie.
## 8. Omologia persistente
`BT-03 @ 01:00:24`
La seconda classe di algoritmi calcola l'**omologia**, detta **omologia persistente** quando la si calcola al computer: lo strumento algebrico che quantifica il numero di buchi di un oggetto topologico e usa questi numeri per caratterizzarlo; forme con lo stesso numero di buchi sono equivalenti (`BT-03 @ 01:01:35`).
**Complessi simpliciali**, slide "Topological Space: Simplicial Complexes":
- "Simplicial Complex: is a collection of simplices – higher dimensional triangle";
- "Simplicial complex lets you to do a finite coverage of a geometrical object";
- "More formally: a simplicial complex K on a finite set V = \{v1; v2; … ; vn\} of vertices is a non-empty subset of the power set of V, so that the simplicial complex K is closed under the formation of subsets".
Simplessi fondamentali: vertice (dimensione 0), arco (1), triangolo pieno (2), tetraedro (3). Nella figura il primo esempio è corretto perché i simplessi condividono una faccia, gli altri no: per esempio un triangolo non può essere pieno se manca l'arco di base (`BT-03 @ 01:02:40`).
**Numeri di Betti**, slide "How to characterize a simplical complex": "Using HOMOLOGY. It counts the number of n-dimensional holes. Betti Number is the output of Homology and can be used for deriving equivalence classes: 'clustering'".
<table header-row="true">
<tr>
<td>Oggetto</td>
<td>$`\beta_0`$</td>
<td>$`\beta_1`$</td>
<td>$`\beta_2`$</td>
</tr>
<tr>
<td>Punto</td>
<td>1</td>
<td>0</td>
<td>0</td>
</tr>
<tr>
<td>Cerchio</td>
<td>1</td>
<td>1</td>
<td>0</td>
</tr>
<tr>
<td>Toro</td>
<td>1</td>
<td>2</td>
<td>1</td>
</tr>
</table>
Il docente: nel cerchio $`\beta_0 = 1`$ è il perimetro, la componente connessa, $`\beta_1 = 1`$ l'interno; nel toro $`\beta_1 = 2`$ sono il cerchio generatore "lungo l'orizzontale e lungo la verticale", $`\beta_2 = 1`$ il volume vuoto dentro la ciambella (`BT-03 @ 01:04:22`).
> **Nota aggiunta:** $`\beta_0`$ conta le **componenti connesse**, non i buchi: a `BT-03 @ 01:03:49` il docente dice che il vertice ha "un solo buco nella dimensione 0". In generale $`\beta_k`$ è il numero di "buchi" $`k`$-dimensionali solo per $`k \ge 1`$: $`\beta_1`$ i cicli indipendenti, $`\beta_2`$ le cavità chiuse.
**Costruire complessi simpliciali**, slide "How to build a Filtered Simplicial Complex": da **point cloud data** (punti in $`\mathbb{R}^d`$) con Vietoris-Rips, Čech o witness complex; da **reti pesate non orientate** con i clique complex; da **reti pesate orientate** con i neighborhood complex. La figura del coniglio mostra una tassellazione triangolare di una superficie (`BT-03 @ 01:05:27`).
**Vietoris-Rips** (`BT-03 @ 01:06:02`), slide "Vietoris-Rips Complexes": attorno a ogni punto si centra una sfera, le sfere si gonfiano insieme; se due sfere si intersecano si traccia un arco, se tre si intersecano "simultaneamente" un triangolo pieno, e così via. Il raggio cresce in una sola direzione, da zero; al crescere del raggio alcune strutture scompaiono, perché un'intersezione a due diventa a tre quando una terza sfera, prima lontana, le raggiunge.
> **Correzione:** la regola "tre sfere che si intersecano simultaneamente danno un triangolo" definisce il complesso di **Čech**. Nel **Vietoris-Rips** basta che le sfere si intersechino **a coppie**: un triangolo (o un simplesso di qualsiasi dimensione) viene riempito appena tutti i suoi lati ci sono. È ciò che lo rende facile da calcolare da una sola matrice delle distanze, ed è ciò che fanno `ripser` e i notebook.
**Weighted clique complex** (`BT-03 @ 01:07:08`), slide "Weighted Clique-Complexes": dalle reti pesate si cercano le **clique massimali**, sottografi completamente connessi; una clique di $`k`$ nodi corrisponde a un simplesso di dimensione $`k - 1`$, per esempio 3 nodi completamente connessi danno un triangolo pieno. Nella figura (b) le clique di tre nodi sono riempite.
**Filtrazione e barcode** (`BT-03 @ 01:08:28`). Slide "Step-by-Step construction via Persistent Homology - Filtration": "The basic aim of persistent homology is to measure the lifetime of certain topological properties of a simplicial complex (s.c.) when simplices are added to the complex or removed from it. A filtration of a complex K is a nested sequence of subcomplex: $`\emptyset = K^0 \subseteq K^1 \subseteq K^2 \subseteq \dots \subseteq K^m = K`$. We call a complex K with a filtration a filtered complex." La slide successiva mostra la costruzione passo per passo, con i numeri di Betti a ogni passo, e il **barcode**: ogni barra è la vita di una caratteristica topologica al crescere del parametro (per Vietoris-Rips, il raggio). Il docente lo chiama "rappresentazione vettoriale del processo di sviluppo delle sfere" e del numero di buchi (`BT-03 @ 01:09:05`).
## 9. Entropia persistente
`BT-03 @ 01:09:35`
I tre modelli sono tempo-dipendenti: in Vicsek cambiano le posizioni, in Kuramoto gli angoli, in Jerne le concentrazioni. Finora i punti erano fissi e variava il raggio; ma il grafo o la nuvola di punti possono evolvere nel tempo, in numero e posizione dei vertici. Lo strumento per studiare le caratteristiche topologiche in funzione del tempo è l'**entropia** (`BT-03 @ 01:10:10`). Shannon la introdusse per le comunicazioni (slide "Connecting the dots…": "I just wondered how things were put together." - Claude Shannon); il docente dice di essersi occupato lui di definirne l'analogo per gli spazi topologici, calcolato dai barcode.
Slide "Persistent Entropy" ("From topology to information theory"): "Given a filtered topological space, let F be the set of its filtration values and let J = \{0, 1, …, n\} be a set of index for the lines appearing in the whole bar-code. A line corresponding to topological noise is denoted by $`[a_j; b_j]`$, with $`j \in J`$. Instead of $`[a_j; \infty)`$, a persistent topological feature is denoted by $`[a_j; b_j = m)`$ where we set $`m = \max(F) + 1`$. The Persistent Entropy H of the topological space is calculated as follows:"
$$
H = -\sum_{j \in J} p_j \log(p_j), \qquad p_j = \frac{l_j}{L}, \quad l_j = b_j - a_j, \quad L = \sum_{j \in J} l_j
$$
Fenomenologicamente l'entropia persistente dice quanto è **ordinata** la costruzione dell'oggetto topologico (`BT-03 @ 01:11:26`).
> **Nota aggiunta:** in letteratura l'entropia persistente compare in Chintakunta, Gentimis, González-Díaz, Jiménez, Krim, "An entropy-based persistence barcode" (Pattern Recognition, 2015) e nei lavori di Merelli, Rucco et al. citati nelle referenze della slide (per esempio "Topological characterization of complex systems: using persistent entropy", Entropy 2015). Valore massimo: $`\log n`$ per $`n`$ barre di uguale lunghezza. Nei notebook la funzione `persim.persistent_entropy` per impostazione predefinita **scarta** le barre infinite invece di troncarle a $`\max(F) + 1`$ come nella slide.
## 10. Esperimenti: TDA su Kuramoto e Vicsek
`BT-03 @ 01:12:04`
Slide "Numerical experiments": TDA for Kuramoto, TDA for Vicsek, "To-do: TDA for Jerne".
**Kuramoto** (`MESA_KURAMOTO_persistent_entropy_persim.ipynb`, `BT-03 @ 01:12:41`): stesso modello della sezione 3, a schermo con $`K = 1.5`$. Per il Vietoris-Rips si installano `persim` e `ripser`; l'input sono le **differenze di fase** fra coppie di oscillatori a ogni istante (`BT-03 @ 01:13:15`).
```python
!pip install persim
!pip install ripser

import ripser
from persim.persistent_entropy import *

# Function to compute the pairwise phase differences
def compute_pairwise_differences(phases):
    N = len(phases)
    pairwise_diffs = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            pairwise_diffs[i, j] = np.abs(phases[i] - phases[j])
    return pairwise_diffs

# Function to compute persistent entropy from the pairwise differences
def compute_persistent_entropy_from_phase_diffs(phases_over_time):
    persistent_entropy_values = []

    for phases in phases_over_time:
        pairwise_diffs = compute_pairwise_differences(phases)

        # Compute Vietoris-Rips complex and persistence diagrams using persim
        diagrams = ripser.ripser(pairwise_diffs)['dgms']  # Replace this with persim

        # Compute persistent entropy from persistence diagrams using persim's function
        entropy = persistent_entropy(diagrams)

        persistent_entropy_values.append(entropy)

    return persistent_entropy_values

# Example: Compute persistent entropy based on pairwise phase differences
persistent_entropy_values_pairwise = compute_persistent_entropy_from_phase_diffs(model.phases_over_time)

# Plot the persistent entropy over time
plt.plot(persistent_entropy_values_pairwise)
plt.xlabel('Time')
plt.ylabel('Persistent Entropy (Pairwise Differences)')
plt.title('Persistent Entropy in Kuramoto Model (Pairwise Phase Differences) Over Time')
plt.show()
```
Lettura del docente (`BT-03 @ 01:13:51`): il coefficiente di sincronizzazione dice che attorno al tick 10 il sistema comincia a sincronizzarsi; l'entropia dice lo stesso, senza una sincronizzazione piena, come conferma $`r`$ che non arriva a 1. Cambiando il coefficiente di accoppiamento la sincronizzazione diventa più stabile dal tick 40 circa, e anche l'entropia persistente lo evidenzia: il sistema ha fatto una **transizione di fase** (`BT-03 @ 01:14:22`). Il punto metodologico: qui la TDA è applicata a dati generati da un modello noto e analitico, e l'entropia conferma ciò che si vede sul modello; quindi, su dati nuovi di un sistema naturale senza modello analitico, l'entropia persistente permette comunque di ottenere un **modello data driven** del sistema (`BT-03 @ 01:15:32`).
Verificato per esecuzione ($`K = 1.5`$, seed fisso): l'entropia $`H_0`$ scende da 4.14 a 3.40 al tick 10, 2.72 al tick 20 e 2.30 al tick 99; l'entropia $`H_1`$ è sempre 0 (la funzione restituisce un valore per dimensione, da cui le due curve, di cui una piatta, nel grafico a schermo). $`r`$ raggiunge il 95% del valore di regime in una mediana di 7.5 tick su 10 seed.
> **Nota aggiunta:** due osservazioni sul calcolo, verificate. (1) `ripser.ripser(pairwise_diffs)` senza `distance_matrix=True` tratta la matrice come una nuvola di 100 punti in $`\mathbb{R}^{100}`$ (ogni riga è un punto): lo segnala il warning a schermo "The input matrix is square, but the distance_matrix flag is off". In questo caso i valori di entropia coincidono con quelli ottenuti passando la matrice come matrice delle distanze, ma il flag va messo. (2) Le fasi non sono ridotte modulo $`2\pi`$: a fine simulazione vanno da circa 188 a 202 radianti. La differenza $`|\theta_i - \theta_j|`$ cresce per gli oscillatori non agganciati che derivano, e la discesa dell'entropia riflette anche questo allontanamento. Con la distanza circolare $`\min(|\Delta\theta| \bmod 2\pi,\ 2\pi - |\Delta\theta| \bmod 2\pi)`$ l'entropia $`H_0`$ resta attorno a 4.17 per tutta la simulazione.
**Vicsek** (`MESA_VICSEK_persistent_entropy_final.ipynb`, `BT-03 @ 01:16:06`): stesso modello della sezione 4 con scatola 100×100; l'input del Vietoris-Rips sono le **distanze euclidee** fra le posizioni delle particelle a ogni istante.
```python
import ripser
from persim.persistent_entropy import *

# Function to compute the pairwise Euclidean distance matrix
def compute_pairwise_distances(positions):
    N = len(positions)
    pairwise_dists = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            pairwise_dists[i, j] = np.linalg.norm(positions[i] - positions[j])
    return pairwise_dists

# Function to compute persistent entropy from the pairwise distances using persim
def compute_persistent_entropy_from_positions(positions_over_time):
    persistent_entropy_values = []

    for positions in positions_over_time:
        pairwise_dists = compute_pairwise_distances(positions)

        # Compute Vietoris-Rips complex and persistence diagrams using persim
        diagrams = ripser.ripser(pairwise_dists)['dgms']

        # Compute persistent entropy from persistence diagrams using persim's function
        entropy = persistent_entropy(diagrams)

        persistent_entropy_values.append(entropy)

    return persistent_entropy_values
```
Lettura del docente (`BT-03 @ 01:18:14`): il sistema ha una serie di **micro transizioni di fase**, tende a essere stabile ma non stabilissimo, e l'entropia amplifica le piccole oscillazioni che il coefficiente di sincronizzazione appiattisce. Si è passati da un sistema sincronizzato nelle fasi (Kuramoto) a uno sincronizzato nelle posizioni delle particelle, che potrebbero essere cellule tumorali, e anche qui l'entropia persistente dà informazioni utili. A schermo: $`H_0`$ attorno a 4.4-4.5, $`H_1`$ fra 2.2 e 2.9.
Verificato per esecuzione (seed fisso, ogni 20 tick): $`H_0`$ fra 4.27 e 4.48, $`H_1`$ fra 1.86 e 2.79, dello stesso ordine della schermata.
> **Nota aggiunta:** la griglia è toroidale, ma le distanze sono euclidee "piatte": due particelle vicine attraverso il bordo risultano lontane quasi quanto la scatola. Per una nuvola di punti su un toro la distanza corretta è quella con il minimo sulle copie traslate.
**Esercizio** (`BT-03 @ 01:19:34`): costruire la TDA per il modello di Jerne.
## 11. Integrazione Teams 2026
`Teams 4 @ 0:00:02`
Nel 2026 i contenuti di questo capitolo occupano la lezione 4 (21/05). Differenze e aggiunte rispetto al 2025.
**Introduzione** (`Teams 4 @ 0:01:03`): la lezione passa dal costruire modelli all'**analizzarli**: la matematica come strumento per capire i comportamenti emergenti. La teoria dei sistemi complessi si studia nei corsi di fisica (meccanica statistica); qui solo a livello introduttivo. Un social network come Facebook è un sistema complesso: la stessa interazione ha effetti diversi su popolazioni diverse. Il docente collega i sistemi complessi all'informatica teorica: il **vero parallelismo** dei sistemi naturali contro il parallelismo approssimato per interleaving e gli *High Dimensional Automata* (`Teams 4 @ 0:06:16`). Sul modeling suggerisce di **conciliare requirements driven e data driven**: codificare regole dalla conoscenza di dominio e imparare dal dato dà un modello più affidabile dei due approcci isolati (`Teams 4 @ 0:10:28`). Con gli agenti "si parte dal micro per scalare al macro, passando dal meso" (`Teams 4 @ 0:08:22`).
**Kuramoto** (`Teams 4 @ 0:19:46`): Kuramoto, "scienziato giapponese"; esempi biologici: cellule cardiache che si sincronizzano, e il cervello epilettico, dove ogni oscillatore è una **colonna corticale** di neuroni vicini e connessi, iper-sincronizzati in crisi. Il coefficiente di sincronizzazione è descritto come "una sorta di integrale della posizione degli oscillatori" (`Teams 4 @ 0:29:15`). Con 100 oscillatori e $`K = 0.5`$ la sincronizzazione si stabilizza dal tick 50 circa.
> **Nota aggiunta:** il parametro d'ordine è una **media** dei fasori $`e^{i\theta_j}`$, cioè il modulo del loro baricentro sul cerchio unitario. Verificato con $`K = 0.5`$: il 95% del valore di regime arriva in una mediana di 25 tick su 10 seed, ma con forte variabilità fra seed; il tick 50 dell'esecuzione in diretta è plausibile.
**Vicsek** (`Teams 4 @ 0:31:21`): il docente lo spiega con le **calamite** che si attraggono o si respingono mentre si muovono, codificate in `step` e `advance` (`Teams 4 @ 0:34:52`). Esperimenti in diretta: 100 agenti in una scatola 500×500 con raggio di visione 10, sistema "fortemente oscillante"; con 10 volte più agenti la curva diventa **monotona crescente**, il sistema si organizza in un unico gruppo; riducendo agenti e scatola "collassa subito in un unico elemento" (`Teams 4 @ 0:36:56`). Vale la correzione della sezione 4: il codice non ha forze, ma allineamento. Verificato: con scatola 500×500 e 100 agenti $`\varphi`$ resta attorno a 0.1; con 1000 agenti il valore del notebook è diviso per 1000 invece che per 100, quindi le curve dei due esperimenti non sono confrontabili in scala.
**Jerne** (`Teams 4 @ 0:40:03`): prima dell'infezione gli anticorpi sono pochi e "a riposo"; allo stimolo le cellule B producono moltissimi anticorpi, più degli antigeni, perché il sistema deve ancora imparare la forma; poi riconosce alcuni anticorpi come antigeni e ne sopprime una parte, tenendo quelli complementari (i Lego da incastrare). Gli **idiotipi** si rappresentano come **etichette binarie**: 100 e 011 sono complementari e garantiscono l'incastro (`Teams 4 @ 0:43:08`). La memoria immunitaria: a un secondo incontro il sistema produce solo gli anticorpi complementari, senza la cascata di iper-proliferazione (`Teams 4 @ 0:47:12`). A fine simulazione, "alcuni anticorpi moriranno prima, altri perdureranno" e quelli che restano costruiscono la memoria (`Teams 4 @ 0:51:25`).
> **Correzione:** il docente dice che per Jerne "non è necessaria una griglia spaziale", perché le interazioni dipendono dalla complementarità e non dalla posizione (`Teams 4 @ 0:47:12`). Nel notebook c'è una `MultiGrid` 20×20 e le interazioni avvengono **solo fra agenti nella stessa cella**: la posizione conta eccome. Inoltre nel codice gli idiotipi sono numeri reali in \[0, 1\], non stringhe binarie, e l'affinità è massima per idiotipi uguali (vedi Nota della sezione 5); la lettura "chi resta costruisce la memoria" va presa con cautela, perché nessun anticorpo aumenta la propria concentrazione.
**Mapper** (`Teams 4 @ 1:09:23`): nel 2026 il docente include il passo di **clustering** (DBSCAN "o qualsiasi altro algoritmo tipo il k-means"): ogni nodo è un insieme di punti dello stesso cluster, e due nodi sono collegati se hanno punti in comune (`Teams 4 @ 1:10:25`). Sul grafo della mano si possono fare interrogazioni e test statistici, per esempio perché il pollice è diverso dalle altre dita (`Teams 4 @ 1:12:30`). giotto-tda "va riavviata" dopo l'installazione (`Teams 4 @ 1:15:01`).
> **Correzione:** per i due cerchi concentrici il docente descrive la funzione filtro come "la distanza rispetto al centro (0, 0)" (`Teams 4 @ 1:16:20`). Nel notebook il filtro è `Projection(columns=[0, 1])`, la proiezione sugli assi $`x`$ e $`y`$: la copertura è una griglia 10×10 di quadrati sovrapposti nel piano, non una serie di anelli.
**Numeri di Betti** (`Teams 4 @ 1:25:38`): Betti "algebrista italiano"; $`\beta_0`$ conta le componenti connesse (anche punti isolati sono componenti). Il secondo ciclo del toro si vede tagliando la ciambella e svolgendola in un tubo: la sezione è un cerchio (`Teams 4 @ 1:27:47`). **Quadrato** e **stella** hanno gli stessi numeri di Betti del cerchio (1, 1, 0) e sono omologicamente equivalenti; in topologia la lunghezza dei lati e l'area dei buchi sono irrilevanti (`Teams 4 @ 1:29:49`). Sul Vietoris-Rips della slide: una componente connessa e tre buchi, $`\beta_0 = 1`$, $`\beta_1 = 3`$ (`Teams 4 @ 1:35:04`). Sul clique complex: le clique massimali si trovano con l'algoritmo di **Bron-Kerbosch**; nella figura restano un'unica componente e un solo buco, e l'informazione sta nei nodi che lo delimitano (`Teams 4 @ 1:38:10`). Per i grafi orientati si usano i **neighborhood complex** (`Teams 4 @ 1:33:00`).
**Filtrazione** (`Teams 4 @ 1:41:18`): lettura passo per passo della figura come persone che interagiscono: punti che compaiono, archi che uniscono componenti ($`\beta_0`$ scende), un triangolo vuoto ($`\beta_1 = 1`$) riempito quando tre persone parlano insieme, fino a un tetraedro vuoto ($`\beta_2 = 1`$). Le barre che arrivano alla fine sono **caratteristiche persistenti**, le altre **rumore topologico** (`Teams 4 @ 1:44:24`).
**Entropia** (`Teams 4 @ 1:45:27`): il docente mostra la *useless machine* di Shannon, "un modo meccanico per rappresentare l'assenza di informazione". L'entropia persistente riassume un barcode, difficile da interpretare, in un numero reale; il calcolo è lineare nel numero di barre. Sul Kuramoto 2026 l'entropia è massima all'inizio e si stabilizza dal tick 20 circa (`Teams 4 @ 1:50:52`); sul Vicsek dopo il tick 25 il sistema raggiunge "una posizione metastabile" (`Teams 4 @ 1:54:16`).
**Jerne con entropia** (`Teams 4 @ 1:56:19`): nel 2026 il docente mostra anche un notebook Jerne con il calcolo dell'entropia persistente sulle concentrazioni (picco massimo 6.9) e lascia come esercizio il grafico della serie temporale dell'entropia. Quel notebook **non è tra i materiali**: il `Jerne.ipynb` di Teams si ferma ai grafici Plotly.
> **Nota aggiunta:** con $`n`$ barre il valore massimo possibile dell'entropia persistente è $`\ln n`$, raggiunto quando le barre hanno tutte la stessa lunghezza. Un valore di 6.9 richiede quindi almeno $`e^{6.9} \approx 1000`$ barre.
**Domanda di uno studente** (`Teams 4 @ 1:59:45`): come si collega l'entropia al modello? Risposta: a ogni istante si associa una forma al sistema (Vietoris-Rips sulle posizioni o sugli angoli), la si riassume nel barcode e il barcode nell'entropia; il grafico entropia-tempo mostra come evolve l'ordine del sistema. L'entropia dice quanto è ordinato il processo di costruzione della forma, e quindi quanto il dataset è omogeneo o eterogeneo: un dato quantitativo con ricadute qualitative. Guardare solo l'ultimo istante non basterebbe (`Teams 4 @ 2:08:23`).
**Lezione successiva** (`Teams 4 @ 2:12:33`): un ospite presenta un simulatore ad agenti per sistemi ecologici reali, validato con dati di campo (è la lezione `Teams 5` del 22/05).
## 12. Collegamento con il test finale
<table header-row="true">
<tr>
<td>Test finale 2026</td>
<td>Dove nel capitolo</td>
</tr>
<tr>
<td>Definizione e caratteristiche di un ABMS</td>
<td>sezioni 3-5 (tre esempi di ABM come generatori di dati)</td>
</tr>
<tr>
<td>Quando ODE e quando ABMS</td>
<td>sezione 2 (top-down e bottom-up)</td>
</tr>
</table>
Il docente indica gli esperimenti sul Jerne (sezione 5) come utili "per attività successive o test finali" (`BT-03 @ 00:44:38`); la TDA non compare nella traccia 2026.
## 13. Glossario, punti incerti, materiale usato
### Glossario
- **Topological Data Analysis (TDA):** insieme di metodi che associano ai dati oggetti topologici e ne misurano la forma.
- **Mapper:** algoritmo che riassume un dataset in un grafo: filtro (lens), copertura con intervalli sovrapposti, clustering per intervallo, collegamento dei cluster che condividono punti.
- **Simplesso, complesso simpliciale:** vertice, arco, triangolo, tetraedro; collezione di simplessi chiusa rispetto alle facce.
- **Numeri di Betti:** $`\beta_0`$ componenti connesse, $`\beta_1`$ cicli indipendenti, $`\beta_2`$ cavità.
- **Vietoris-Rips, Čech:** complessi costruiti da una nuvola di punti al crescere di un raggio; il primo richiede intersezioni a coppie, il secondo intersezioni comuni.
- **Clique complex:** complesso simpliciale ottenuto riempiendo le clique di un grafo.
- **Filtrazione, barcode:** sequenza crescente di complessi; insieme degli intervalli di vita delle caratteristiche topologiche.
- **Entropia persistente:** entropia di Shannon delle lunghezze delle barre di un barcode.
- **Parametro d'ordine:** misura globale di sincronizzazione (Kuramoto) o allineamento (Vicsek), fra 0 e 1.
- **Idiotipo:** regione variabile di un anticorpo, riconoscibile da altri anticorpi.
### Punti incerti
- Valore di $`K`$ usato nella seconda esecuzione del Kuramoto con entropia (`BT-03 @ 01:14:22`): non inquadrato; il notebook di Teams salva $`K = 0.5`$, e un tempo di sincronizzazione attorno a 40 è compatibile anche con $`K = 0.25`$ \[?\].
- Import del notebook KeplerMapper non inquadrati per intero `[illeggibile]`: ricostruiti con i nomi usati nel codice.
- Nomi trascritti male e corretti nel testo: "cura moto" → Kuramoto; "vixec", "vixx" → Vicsek; "germe", "GERNE", "German" → Jerne; "vietori strips", "vittori slips", "Vitoris Reeps" → Vietoris-Rips; "per sim" → persim; "che player ma per" → KeplerMapper; "giotto", "G8TDA" → giotto-tda; "vettivo", "Betty" → Betti; "weight e the click complex" → weighted clique complex; "Nick Brude Complexis" → neighborhood complexes; "Bron kerbosh" → Bron-Kerbosch.
### Materiale usato
- `Materiale/Portale/TDA.pdf` (identico a `Materiale/Teams/IV lezione/TDA.pdf`)
- `Materiale/Teams/colab/MESA_KURAMOTO.ipynb`, `MESA_KURAMOTO_persistent_entropy_persim.ipynb`, `MESA_VICSEK_persistent_entropy_final.ipynb`, `Jerne.ipynb`, `mapper_quickstart.ipynb`
- Fotogrammi `BT-03` di `MESA_VICSEK.ipynb` e `mapper_tda_tutorial.ipynb` (non tra i materiali) e dei grafici a schermo
- Registrazione `Teams 4` (21/05/2026), trascrizione Stream
- Verifica: `verifica_bt03.py` (MESA, ripser, persim, KeplerMapper) e `verifica_mapper_giotto.py` (giotto-tda)
