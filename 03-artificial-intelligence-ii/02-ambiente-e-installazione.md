# 02 - Ambiente e installazione
> Fonte Notion: https://app.notion.com/p/3d612abc808d8199b27cce0ec1128474 — ultima modifica 2026-09-15T10:04:33.454Z

> Giornata 1, sezioni 6–16 · video `TF-01`
**Allegati:** `docker-compose.yml`, `docker/README.md`, `day-01-appunti.pdf`
---
## 6. Requisiti di sistema e canali di installazione `TF-01 @ 00:16:00`
L'installazione dipende dalla macchina. Il docente lavora su **Linux**; su Mac la procedura è la stessa, su Windows può differire. Su Linux e su Mac Python è già presente; su Windows va installato, e serve anche il redistribuibile C++ — a partire da Windows 7 dovrebbe già essere presente — oppure si può usare **WSL2**, che è un ambiente Linux dentro Windows.
Sul Mac, osserva il docente, al momento conviene usare la CPU: con i nuovi processori Apple Silicon il supporto non è ancora completo. Trattandosi però di un progetto open source, esiste un repository a cui collaborano in molti per usare la GPU di Apple.
**Pagina ****`tensorflow.org/install`**** mostrata a schermo ****`TF-01 @ 00:18:52`****:**
La pagina elenca i sistemi a 64 bit su cui TensorFlow è testato e supportato: Python 3.8–3.11, Ubuntu 16.04 o successivi, Windows 7 o successivi (con redistribuibile C++), macOS 10.12.6 Sierra o successivi senza supporto GPU, e WSL2 da Windows 10 19044 in su, con GPU in fase sperimentale.
### Download a package
La pagina indica di installare TensorFlow con il gestore di pacchetti `pip`, avvertendo che i pacchetti di TensorFlow 2 richiedono una versione di `pip` \>19.0 (o \>20.3 su macOS), e che sono disponibili pacchetti ufficiali per Ubuntu, Windows e macOS.
```bash
# Requires the latest pip
$ pip install --upgrade pip

# Current stable release for CPU and GPU
$ pip install tensorflow

# Or try the preview build (unstable)
$ pip install tf-nightly
```
### Run a TensorFlow container
Le immagini Docker di TensorFlow sono già configurate per eseguirlo; un container gira in un ambiente virtuale ed è il modo più semplice per predisporre il supporto GPU.
```bash
$ docker pull tensorflow/tensorflow:latest  # Download latest stable image
$ docker run -it -p 8888:8888 tensorflow/tensorflow:latest-jupyter  # Start Jupyter server
```
### Google Colab
Nessuna installazione necessaria: i tutorial si eseguono direttamente nel browser con Colaboratory, un progetto di ricerca Google per diffondere formazione e ricerca sul machine learning; è un ambiente Jupyter che non richiede setup e gira interamente nel cloud.
**Dagli appunti del corso (****`appunti.pdf`****, pagina 2) ****`TF-01 @ 00:16:55`****:**
Gli appunti rimandano alla guida ufficiale di installazione di TensorFlow per le istruzioni dettagliate in base a sistema operativo e hardware, e per una installazione base su CPU indicano di usare nel terminale il comando riportato sotto.
```bash
python3 -m pip install tensorflow-cpu
```
Per installare invece TensorFlow con supporto GPU, gli appunti indicano un comando diverso.
*(il blocco di codice successivo è sotto il bordo inferiore della finestra in tutti i frame disponibili — \[illeggibile\])*
---
## 7. Installazione locale: virtualenv e VS Code `TF-01 @ 00:19:00`
Il docente usa **VS Code**, ma precisa che va bene qualunque editor. Dà un consiglio didattico esplicito: in questa fase conviene usare VS Code **senza** i plugin di completamento automatico basati su AI, perché lo scopo è capire la sintassi di TensorFlow; generare codice senza averne capito il significato non serve. Una volta acquisita familiarità con la sintassi, si potrà passare agli assistenti.
Il docente lavora su **Ubuntu**. Su Windows, dopo aver installato Python, si può usare PowerShell per verificarne la versione. Lui usa **Python 3.10**, ma vanno bene anche 3.9 o 3.11; indica 3.10 solo per coerenza, così che il codice della lezione sia riutilizzabile.
La regola che segue sempre: **non installare TensorFlow nel Python globale**, ma creare un ambiente separato per la sessione di lavoro.
```bash
python3 -m pip install virtualenv
python3 -m virtualenv venv
```
**Output nel terminale integrato ****`TF-01 @ 00:22:00`****:**
```javascript
Requirement already satisfied: filelock<4,>=3.12.2 in /usr/local/lib/python3.10/dist-packages (from virtualenv) (3.12.2)
10-06-2025 python3 -m virtualenv venv
created virtual environment CPython3.10.12.final.0-64 in 301ms
  creator CPython3Posix(dest=/home/louis/Documents/TEACHING/INCLASS2025/10-06-2025/venv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/louis/.local/share/virtualenv)
    added seed packages: pip==25.1.1, setuptools==80.4.0, wheel==0.45.1
  activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
```
**Attivazione dell'ambiente.** Su Linux si usa `source venv/bin/activate`; su Windows quel comando può non funzionare. La via consigliata, indipendente dal sistema operativo, è passare da VS Code: installare l'estensione **Python** dal marketplace, premere `F1` e cercare **"Python: Select Interpreter"**, quindi scegliere il virtualenv appena creato. Da quel momento anche i nuovi terminali aperti dentro VS Code attivano l'ambiente automaticamente.
La cartella di lavoro della lezione è `10-06-2025/`, e contiene `.vscode/`, `colab/`, `docker/`, `venv/`, `appunti.md`, `appunti.pdf` e `main.py`.
---
## 8. Verifica dell'installazione e della GPU `TF-01 @ 00:24:00`
Per il pacchetto CPU si usa il comando visto negli appunti; il download è di circa 500 megabyte, ma se il pacchetto è già nella cache di pip non serve riscaricarlo.
**Verifica della versione (dagli appunti, pagina 3) ****`TF-01 @ 00:25:18`****:**
```bash
python3 -c "import tensorflow; print(tensorflow.__version__)"
```
Gli appunti spiegano che il comando stampa la versione di TensorFlow installata, che su Windows può essere necessario usare `py3` al posto di `python3`, e che in alternativa si può scaricare da Docker Hub un'immagine TensorFlow già pronta.
Il docente ottiene la versione **2.19**, accompagnata dai warning CUDA di cui parlerà più avanti.
**Verifica della scheda grafica ****`TF-01 @ 00:26:00`****.** Se si ha una GPU NVIDIA e il driver è installato, `nvidia-smi` restituisce la versione del driver:
```javascript
Tue Jun 10 16:29:10 2025
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.163.01              Driver Version: 550.163.01      CUDA Version: 12.4    |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 2060        Off |   00000000:01:00.0  On |                  N/A |
| N/A   62C    P8              2W /   80W |      71MiB /   6144MiB |     12%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
```
La macchina del docente monta dunque una **GeForce RTX 2060 da 6 GB**, driver **550.163.01**, **CUDA 12.4**. Precisa di usare la versione 550 e non l'ultima disponibile perché la sua è una scheda vecchia e con i driver più recenti a volte ha problemi.
**Riferimenti indicati negli appunti (****`appunti.pdf`****, sezione "references") ****`TF-01 @ 00:28:37`****:**
Gli appunti riportano la procedura per installare Docker con GPU NVIDIA in tre passi — driver NVIDIA (su Ubuntu si cerca fra i driver aggiuntivi e se ne seleziona uno di NVIDIA), installazione di Docker per la propria distribuzione Linux ([https://docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/)) e installazione del NVIDIA Container Toolkit ([https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)) — e rimandano inoltre alle competizioni Kaggle ([https://www.kaggle.com/competitions](https://www.kaggle.com/competitions)).
---
## 9. Jupyter dentro l'ambiente virtuale `TF-01 @ 00:27:00`
Durante il corso si userà **Jupyter Notebook**, per due ragioni: è facile condividere il codice, ed è più comodo di scrivere un file `.py` e lanciarlo con `python nomefile`.
Jupyter viene installato **dentro il virtualenv**. L'elenco dei pacchetti installati compare nel terminale `TF-01 @ 00:28:00` e comprende, fra gli altri, `jupyter-1.1.1`, `jupyterlab-4.4.3`, `notebook-7.4.3`, `ipykernel-6.29.5`, `ipython-8.37.0`, `matplotlib-inline-0.1.7`, `nbconvert-7.16.6`, `nbformat-5.10.4`, `tornado-6.5.1`.
Il docente crea la cartella `notebooks/` e dentro il notebook `dayone.ipynb` `TF-01 @ 00:28:44`. Alla prima apertura VS Code mostra "Detecting Kernels": bisogna **selezionare il kernel**, esattamente come si era fatto con l'interprete, scegliendo il percorso del virtualenv.
**Prime celle del notebook ****`TF-01 @ 00:44:02`** — kernel `venv (Python 3.10.12)`:
Cella `[1]`:
```python
import tensorflow as tf
```
Output (5.9 s):
```javascript
2025-06-10 16:32:05.142385: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:467] Unable to register cuFFT
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
E0000 00:00:1749565925.224822  371691 cuda_dnn.cc:8579] Unable to register cuDNN factory: Attempting to register fa[illeggibile]
E0000 00:00:1749565925.256681  371691 cuda_blas.cc:1407] Unable to register cuBLAS factory: Attempting to register [illeggibile]
W0000 00:00:1749565925.431822  371691 computation_placer.cc:177] computation placer already registered. Please chec[illeggibile]
2025-06-10 16:32:05.454348: I tensorflow/core/platform/cpu_feature_guard.cc:210] This TensorFlow binary is optimize[illeggibile]
[...] enable the following instructions: AVX2 FMA, in other operations, rebuild TensorFlow with the appropriate compil[illeggibile]
```
*(le righe sono tagliate dal bordo destro della finestra)*
Cella `[2]`:
```python
tf.__version__
```
```javascript
'2.19.0'
```
Cella `[3]`:
```python
tf.config.list_physical_devices()
```
```javascript
[PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU'), ...
```
Il docente ricorda che le celle si eseguono con **`Shift`****+****`Invio`**.
---
## 10. Pluggable devices e i warning CUDA `TF-01 @ 00:30:00`
Per usare la GPU non basta il driver della scheda: serve anche **CUDA**. Il comando `pip install tensorflow` porta con sé le dipendenze CUDA, ma i warning che compaiono all'import indicano che qualcosa non viene registrato.
Il docente spiega che cosa sia **cuDNN**: è una libreria di CUDA scritta in C++ che implementa le reti neurali **a basso livello** — chi volesse scrivere le proprie reti direttamente in C++ userebbe quella libreria.
Con `tf.config.list_physical_devices()` `TF-01 @ 00:31:30` il docente verifica quali dispositivi TensorFlow riesca effettivamente a vedere.
**Pagina ****`tensorflow.org/install/gpu_plugins`**** mostrata a schermo ****`TF-01 @ 00:30:00`****–****`TF-01 @ 00:36:27`****:**
La pagina avverte che riguarda i dispositivi GPU non NVIDIA (per NVIDIA si rimanda alla guida di installazione con pip) e descrive l'architettura a *pluggable device* di TensorFlow: il supporto a nuovi dispositivi viene aggiunto come pacchetti plug-in separati, installati accanto al pacchetto ufficiale. Il meccanismo non richiede modifiche specifiche nel codice di TensorFlow perché si appoggia a API C stabili per comunicare con il binario; sono gli sviluppatori dei plug-in a mantenere repository e pacchetti propri e a farsi carico del test dei loro dispositivi.
### Use device plugins
Per usare un dispositivo come se fosse nativo basta installare il pacchetto plug-in corrispondente. L'esempio mostra l'installazione e l'uso del plug-in di un dispositivo dimostrativo, la *Awesome Processing Unit (APU)*, che per semplicità implementa un solo kernel personalizzato, quello per la ReLU.
<empty-block/>
```bash
# Install the APU example plug-in package
$ pip install tensorflow-apu-0.0.1-cp36-cp36m-linux_x86_64.whl
...
Successfully installed tensorflow-apu-0.0.1
```
Installato il plug-in, si verifica che il dispositivo sia visibile e si esegue un'operazione sulla nuova APU.
```python
import tensorflow as tf   # TensorFlow registers PluggableDevices here.
tf.config.list_physical_devices()  # APU device is visible to TensorFlow.
[PhysicalDevice(name='/physical_device:CPU:0', device_type='CPU'), PhysicalDevice(name='/physical_device:AP[illeggibile]

a = tf.random.normal(shape=[5], dtype=tf.float32)  # Runs on CPU.
b =  tf.nn.relu(a)         # Runs on APU.

with tf.device("/APU:0"):  # Users can also use 'with tf.device' syntax.
  c = tf.nn.relu(a)        # Runs on APU.

with tf.device("/CPU:0"):
  c = tf.nn.relu(a)        # Runs on CPU.

@tf.function  # Defining a tf.function
def run():
  d = tf.random.uniform(shape=[100], dtype=tf.float32)  # Runs on CPU.
  e = tf.nn.relu(d)        # Runs on APU.

run()  # PluggableDevices also work with tf.function and graph mode.
```
### Available devices
La pagina elenca due plug-in disponibili: **Metal** per le GPU macOS, che funziona con TF 2.5 o successivi, con una guida introduttiva e il rimando all'Apple Developer Forum per domande e feedback; e **DirectML** per Windows e WSL, in anteprima, che funziona con il pacchetto `tensorflow-cpu` dalla versione 2.10 in su ed è distribuito come wheel su PyPI.
---
## 11. L'alternativa Docker: perché e come `TF-01 @ 00:32:00`
Il caso d'uso è preciso: si ha una GPU NVIDIA, ma installando TensorFlow con pip compaiono i warning e l'addestramento fallisce perché cuDNN non viene registrato. L'alternativa è **Docker**.
Il docente definisce che cosa sia un container. Un'immagine Docker è un ambiente separato, come una macchina virtuale — ma con una differenza di progetto importante: mentre una macchina virtuale (VirtualBox, VMware) è pensata per ospitare un intero sistema con molti programmi, la virtualizzazione Docker **è pensata per un singolo processo**. Un container con TensorFlow lancia soltanto Python.
Il vantaggio pratico riguarda la **condivisione del lavoro**: senza container, per far girare il proprio codice su un'altra macchina bisogna dire all'altra persona di installare Python 3.10, poi TensorFlow in una certa versione, poi Jupyter in un'altra. Con Docker tutti questi requisiti si dichiarano una volta nella definizione dell'immagine, e vengono installati automaticamente. Il risultato è un **ambiente omogeneo**: tutti hanno le stesse versioni. Il docente sottolinea perché conta: alcune parti della sintassi sono **deprecate**, e il funzionamento dipende dalla versione.
---
## 12. I tre prerequisiti per la GPU in container `TF-01 @ 00:35:30`
Per usare la GPU dentro un container servono tre cose, nell'ordine.
**1. Verificare e installare il driver NVIDIA.** Prima si verifica di avere davvero una scheda NVIDIA: il comando restituisce l'informazione che la VGA è una GeForce prodotta da NVIDIA. Poi si installa il driver. Su Ubuntu esiste un'interfaccia grafica dedicata: cercando "driver" nelle impostazioni si apre l'elenco dei driver disponibili (*Additional Drivers*). Il docente sceglie la versione **550** invece dell'ultima perché la sua scheda è vecchia e con la più recente ha avuto problemi.
**2. Installare Docker.** Su Ubuntu è una sequenza di comandi; su Windows è un software da scaricare, **Docker Desktop**. Si verifica dal terminale con `docker version`.
**3. Installare il NVIDIA Container Toolkit.** Questa è la parte che il docente spiega con più cura, perché è quella che risolve il problema di fondo: Docker, di per sé, ha accesso soltanto alla virtualizzazione della CPU e **non vede gli altri componenti hardware**. Perché dentro il container si sappia che esiste una scheda grafica utilizzabile, serve il Container Toolkit. Anche questa è una sequenza di comandi, ma richiede tempo e cambia a seconda della versione di Ubuntu; il docente lo ha installato in anticipo. Alla fine è necessario un **riavvio**.
---
## 13. `docker-compose.yml` e avvio del container `TF-01 @ 00:40:00`
Il file `docker-compose.yml` è l'*entry point* per lanciare il container. È scritto in **YAML**: si definisce la sezione dei servizi, il nome del servizio (`jupyter`) e l'immagine da usare.
**Scelta dell'immagine ****`TF-01 @ 00:41:00`****.** Per vedere quali immagini siano disponibili si va su **Docker Hub** e si cerca `tensorflow`. Il docente nota che le ultime immagini *nightly jupyter* sono state pubblicate due ore prima. Osserva anche la dimensione: le immagini vanno dai 500-700 megabyte, ma quelle **GPU sono decisamente più pesanti**. Con `docker image ls` elenca le immagini già presenti in locale: c'è una `tensorflow/tensorflow` `2.16.1-gpu-jupyter` da 7.69 GB. L'immagine `2.19.0` che gli serve pesa circa 3 GB compressa.
Nel file l'immagine passa da `2.12.0` a **`2.19.0`**, per farla combaciare con la versione di TensorFlow usata in locale.
**Il file completo ****`TF-01 @ 00:47:34`** (`docker/docker-compose.yml`, 9 righe):
```yaml
# Pin the image tag to match the TensorFlow version you teach; see:
# https://hub.docker.com/r/tensorflow/tensorflow/tags
services:
  jupyter:
    image: tensorflow/tensorflow:2.19.0-gpu-jupyter
    runtime: nvidia
    environment:
      - NVIDIA_VISIBLE_DEVICES=all
      - NVIDIA_DRIVER_CAPABILITIES=all
    ports:
      - "8888:8888"
    volumes:
      - ../:/workspace
    working_dir: /workspace
```
> **Divergenza, e riguarda proprio il problema che il docente pone a voce.** La versione mostrata a schermo (`TF-01 @ 00:47:34`) si ferma a `- 8888:8888`: non ha ne' `volumes` ne' `working_dir`. A `TF-01 @ 00:51:30` il docente avverte che i file creati dentro il container si perdono quando il container viene cancellato e che «bisogna definire una cartella in cui mettere i propri file» — ma non la aggiunge. Il file distribuito su Teams la contiene gia'. Vedi `day-01-divergenze.md` §6.
Il docente spiega riga per riga le tre cose che servono per la GPU:
- `runtime: nvidia` — indica il runtime da usare;
- `NVIDIA_VISIBLE_DEVICES=all` — dice al container che può vedere **tutti** i dispositivi NVIDIA;
- `NVIDIA_DRIVER_CAPABILITIES=all` — le capacità del driver.
L'ultima parte, la mappatura delle porte, è necessaria perché **Jupyter è un web server**: la porta `8888` del container va esposta sulla `8888` dell'host. Il docente aggiunge che in VS Code, avendo installato l'estensione **Jupyter**, non ha più bisogno di aprire il browser: è la stessa cosa che aveva fatto con "Select Kernel".
**Comandi usati dal terminale integrato** (prompt `venv→ docker`):
```bash
docker ls
docker compose -f docker-compose.yml up
docker compose up
docker compose down
docker container ls
```
---
## 14. L'errore `nvidia-container-runtime` e la configurazione con `nvidia-ctk` `TF-01 @ 00:45:00`
Al primo `docker compose up` il container non parte. L'errore, letto a schermo `TF-01 @ 00:49:19`:
```javascript
Attaching to jupyter-1
Gracefully stopping... (press Ctrl+C again to force)
Error response from daemon: failed to create task for container: failed to create shim task: OCI runtime create failed: unable to retrieve OCI runtime error (open /run/containerd/io.containerd.runtime.v2.task/moby/7e32a6149de1fa2ccbb4b2bf47f6eb40df75a378650d0e526214db582aba601c/log.json: no such file or directory): exec: "nvidia-container-runtime": executable file not found in $PATH: unknown
```
La diagnosi del docente: **non basta installare il Container Toolkit, bisogna anche configurarlo**, perché il runtime deve sapere che esiste. Nel suo caso il container era stato aggiornato e la configurazione precedente non era più valida.
**Documentazione NVIDIA Container Toolkit 1.17.7 mostrata a schermo ****`TF-01 @ 00:46:00`****, ****`TF-01 @ 00:50:22`****.** L'indice della pagina distingue i gestori di pacchetti: `apt` per Ubuntu/Debian, `dnf` per RHEL/CentOS, Fedora, Amazon Linux, `zypper` per OpenSUSE e SLE. La parte visibile a schermo è quella `zypper`:
La documentazione propone come passo opzionale di abilitare il repository dei pacchetti sperimentali,
```bash
$ sudo zypper modifyrepo --enable nvidia-container-toolkit-experimental
```
e poi, come secondo passo, di installare i pacchetti del NVIDIA Container Toolkit.
```bash
$ sudo zypper --gpg-auto-import-keys install -y nvidia-container-toolkit
```
### Configuration — Prerequisites
I prerequisiti indicati sono due: avere installato un container engine supportato (Docker, Containerd, CRI-O, Podman) e avere installato il NVIDIA Container Toolkit.
### Configuring Docker
Il primo passo è configurare il container runtime con il comando `nvidia-ctk`.
```bash
$ sudo nvidia-ctk runtime configure --runtime=docker
```
La documentazione spiega che `nvidia-ctk` modifica il file `/etc/docker/daemon.json` sull'host, aggiornandolo perché Docker possa usare l'NVIDIA Container Runtime; il secondo passo è riavviare il demone Docker.
```bash
$ sudo systemctl restart docker
```
### Rootless mode
Per configurare il container runtime con Docker in modalità rootless la documentazione indica questi passi.
```bash
nvidia-ctk runtime configure --runtime=docker --config=$HOME/.config/docker/daemon.json
$ systemctl --user restart docker
$ sudo nvidia-ctk config --set nvidia-container-cli.no-cgroups --in-place
```
Il docente esegue la configurazione e il riavvio del demone, e a quel punto il container parte. Sottolinea il punto operativo: il comando `nvidia-ctk` **crea il file di configurazione** ed è possibile verificarne il contenuto.
---
## 15. Jupyter nel container e il tutorial Fashion MNIST `TF-01 @ 00:50:00`
All'avvio il container stampa molto output; quello che interessa è **l'URL con cui accedere a Jupyter**. Aprendolo nel browser si trova già una copia del notebook e una cartella con i **tutorial di TensorFlow**.
Il docente apre `classification.ipynb` all'indirizzo `127.0.0.1:8888/notebooks/tensorflow-tutorials/classification.ipynb` — kernel `Python 3 (ipykernel)`, stato "Not Trusted".
Il notebook si intitola **"Basic classification: Classify images of clothing"** e presenta una guida che addestra una rete neurale a classificare immagini di capi di abbigliamento, come scarpe da ginnastica e camicie; avverte che non è un problema se non si capiscono tutti i dettagli, perché è una panoramica rapida di un programma TensorFlow completo, con le spiegazioni date via via, e precisa che usa `tf.keras`, l'API di alto livello per costruire e addestrare modelli.
Cella `[1]`:
```python
# TensorFlow and tf.keras
import tensorflow as tf

# Helper libraries
import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__)
```
Output: i soliti messaggi CUDA, seguiti da `2.19.0`.
La sezione **"Import the Fashion MNIST dataset"** spiega che la guida usa il dataset Fashion MNIST, composto da 70.000 immagini in scala di grigi suddivise in 10 categorie, che ritraggono singoli capi di abbigliamento a bassa risoluzione (28 per 28 pixel), come mostrato nell'immagine.
**Diagramma a schermo:** una griglia di immagini in scala di grigi che mostra il campione del dataset Fashion-MNIST (capi di abbigliamento a bassa risoluzione).
**Avvertenza operativa sulla persistenza ****`TF-01 @ 00:51:30`****.** Il docente insiste su un punto: i file creati dentro il container **si perdono quando il container viene cancellato**. Occorre quindi definire una cartella condivisa in cui mettere i propri file, per conservarli.
**Il problema che resta aperto ****`TF-01 @ 00:52:00`****–****`TF-01 @ 00:54:30`****.** Dentro il notebook la GPU non viene trovata. Per capire dove sia il problema il docente entra nel container:
```bash
docker container ls
docker exec -it <nome-container> nvidia-smi
```
Il container **vede** la GPU. Quindi il problema non è né Jupyter né Docker: è TensorFlow che non riesce a usarla, probabilmente per una **incompatibilità fra la versione di CUDA** e quella richiesta. Il docente propone come possibile rimedio di scendere a CUDA 11, dice che condividerà il file e che eventuali problemi si rivedranno insieme.
**Arresto dei container ****`TF-01 @ 00:55:19`****:**
```javascript
jupyter-1  | Skipping registering GPU devices...
jupyter-1  | [I 2025-06-10 14:55:26.368 ServerApp] Saving file at /tensorflow-tutorials/classification.ipynb
jupyter-1  | [I 2025-06-10 14:56:21.465 ServerApp] Saving file at /dayone.ipynb
Gracefully stopping... (press Ctrl+C again to force)
[+] Stopping 1/1
 ✔ Container docker-jupyter-1  Stopped                    1.3s
^C
venv→ docker docker compose down
[+] Running 2/2
 ✔ Container docker-jupyter-1  Removed                    0.0s
 ✔ Network docker_default      Removed                    0.2s
```
---
## 16. Le alternative online: Kaggle e Google Colab `TF-01 @ 00:55:00`
Se non si dispone di una macchina potente, restano le piattaforme online.
**Kaggle** ospita competizioni di machine learning e mette a disposizione una GPU. Il docente segnala che ci sono competizioni pensate per imparare, e che l'ambiente non è specifico di TensorFlow: per le altre librerie potrebbe essere necessario installarle.
**Google Colab** è la piattaforma che si userà. Serve un account Google. Il vantaggio rispetto a Kaggle è diretto: poiché **TensorFlow è sviluppato da Google**, su Colab è già installato, mentre su Kaggle l'ambiente potrebbe richiedere un `pip install`.
---
## File allegati
Il `docker-compose.yml` ufficiale, che a differenza di quello mostrato a lezione contiene `volumes` e `working_dir` — cioè la soluzione al problema della persistenza dei file che il docente pone a voce a `TF-01 @ 00:51:30` senza risolverlo a schermo.
<file src="notion-file-block://143ac29b-cb47-431b-8460-3e6e8b77a9a8/22331ce3-f667-42cb-9bd7-765db3c031f1?space_id=98012abc-808d-816f-9733-00030a2b4817&name=docker-compose.yml"></file>
<file src="notion-file-block://8d970b53-8480-4dac-a9fd-cca4c58be9bf/a9a5969a-481e-4786-9d8e-d73796953ca2?space_id=98012abc-808d-816f-9733-00030a2b4817&name=docker-README.md"></file>
