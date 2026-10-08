# Verifica per esecuzione — giornata 1, capitolo API tensori

Il capitolo 4 del manuale ricostruisce `10-06-2025.ipynb`, il notebook che il docente
ha costruito dal vivo e che non e' mai stato distribuito. Le celle sono state
estratte dal manuale, assemblate in `giornata-01-tensori-ricostruito.ipynb` ed
eseguite con TensorFlow 2.21 su CPU.

## Esito

| | |
|---|---|
| Celle di codice | 42 |
| Eseguite senza errori | 38 / 38 |
| Errori attesi corrispondenti | 4 / 4 |
| Celle non ricostruibili | 1 |

I 4 errori attesi sono quelli che il docente dimostra apposta e devono fallire:

- `InvalidArgumentError` sul reshape di dimensione incompatibile (sez. 28)
- `AttributeError` su `assign` applicato a una costante (sez. 30)
- `InvalidArgumentError` su `matmul` fra matrici incompatibili (sez. 31)
- `InvalidArgumentError` su `sqrt` applicata a un `int32` (sez. 32)

Che girino tutte le altre e falliscano esattamente queste quattro e' la conferma
che la trascrizione del codice regge: un errore di trascrizione avrebbe prodotto
un fallimento in piu' o in meno.

## L'unica lacuna

La cella che definisce `mm` (sez. 31) non e' leggibile in nessun frame. A
`TF-02 @ 00:49:00` il docente la sta ancora scrivendo e la cella e' vuota; al
frame successivo, `00:49:49`, la vista e' gia' scrollata sul traceback dell'errore.
Il contenuto e' caduto nei 49 secondi fra i due.

Il manuale l'aveva **scartata in silenzio** invece di marcarla: ora e' segnata
`[illeggibile]` con la nota di cosa si deduce (mm non e' quadrata) e il punto del
video da riguardare.

Nel notebook la cella e' presente come segnaposto commentato, con un valore
arbitrario che permette al resto di girare. **Non e' il valore usato a lezione.**

## Nota di metodo

Il primo tentativo di esecuzione dava 25 celle fallite su 41. Era un difetto dello
script che genera il notebook: le righe venivano scritte senza `\n` finale, e al
caricamento tutte le righe di una cella si concatenavano in una sola. Il formato
`.ipynb` vuole che ogni elemento di `source` termini con il newline, tranne
l'ultimo. Da correggere in `scripts/` prima di generare i notebook delle altre
giornate.
