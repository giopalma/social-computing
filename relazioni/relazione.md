---
title: "Relazione primo progetto di Social Computing"
author: 
- "Andrea Gritti (152206)"
- "Anna Sacchet (153005)"
- "Giovanni Palma (152336)"
- "Paola Sagliocca (151861)"
geometry: margin=3cm
output: pdf_document
---

# Introduzione
In questa prima esperienza di laboratorio, il nostro gruppo ha avuto l’occasione di prendere dimestichezza con il linguaggio di programmazione Python e di accedere alle API di Twitter, oltre che di effettuare analisi su grafi e reti grazie, alle librerie: Tweepy, utilizzata per i primi 3 punti del progetto, e NetworkX, per i rimanenti 7 punti. Al centro della nostra analisi vi è il noto social network Twitter: un  social finalizzato alla comunicazione e alla divulgazione di informazioni tramite lo scambio di messaggi di testo di al massimo 280 caratteri che prendono il nome di “tweet”, e per cui si contano oltre 500 milioni di iscritti e 330 milioni di utenti attivi in tutto il mondo, motivo per cui gli oltre 5780 tweet al secondo lo rendono uno dei più grandi database al mondo da cui poter estrapolare qualsiasi tipo di informazione. 

## Tweepy
Tweepy è una libreria Python per l'accesso alle API di Twitter. Consente agli sviluppatori di integrare facilmente le funzionalità di Twitter nelle proprie applicazioni Python. Con Tweepy è possibile eseguire operazioni quali la lettura e la scrittura di messaggi Twitter, la ricerca di tweet, ricavare i followers di un utente ed altro. Per utilizzare la libreria Tweepy è, dunque, necessario aver accesso agli strumenti da sviluppatore Twitter indispensabili per estrarre i dati pubblicati sulla piattaforma. Ogni componente del gruppo ha dovuto creare dapprima un account Twitter e in seguito un account Twitter Developers che fornisce all'utente le credenziali d’accesso alle API, tra cui il bearer token. Installata la libreria ed importata all'interno del progetto, è possibile utilizzare la funzione `tweepy.Client()`, autenticandoci tramite `BEARER_TOKEN`, creeremo un oggetto `Client` che fungerà da interfaccia per le API di Twitter.

## NetworkX
NetworkX è una libreria Python che fornisce strumenti per la creazione e la manipolazione di reti complesse. Può essere utilizzata per creare e analizzare grafi, ovvero rappresentazioni matematiche di reti formate da un insieme di punti ( vertici o nodi ) e un insieme di linee ( archi ) che uniscono coppie di nodi.
NetworkX può essere utilizzato per modellare e studiare un'ampia gamma di sistemi complessi, tra cui reti sociali, biologiche e tecnologiche. È uno strumento potente per comprendere la struttura e la dinamica dei sistemi complessi e può aiutare i ricercatori e gli analisti a comprendere meglio le relazioni tra i vari elementi di una rete. Nel nostro caso utilizzeremo NetworkX per analizzare i followers di un utente, @KevinRoitero, analizzeremo le relazioni di following tra essi e infine andremo a svolgere varie misurazioni sul grafo risultate.

# Svolgimento
## Raccolta dati :
### Punto 1
 Prima di iniziare abbiamo definito due funzioni: una per salvare dati  JSON in locale e l’altra,invece, per leggere file JSON da locale.  
 A questo punto abbiamo potuto finalmente iniziare il nostro progetto! Per il primo punto ci è stato richiesto di utilizzare la libreria Tweepy e scaricare tutti i follower del profilo Twitter con username @KevinRoitero, scaricando per ciascuno di essi : attributi di default, descrizione del profilo, metriche pubbliche dell’account (followers_count, following_count, tweet_count, listed_count) e lo stato di protezione dell’account, e infine salvare il risultato in una unica serializzazione JSON. Per fare ciò abbiamo creato una funzione `get_parsed_users_followers(id)` che sfrutteremo anche nei punti successivi e che, specificato l’id dell’utente di interesse, ci restituisce, grazie alla funzione `client.get_users_followers` di Tweepy, un dizionario di tutti i suoi followers con salvate tutte le informazioni richieste nella consegna del punto 1. In questo passaggio, inoltre, per aggirare il limite imposto da twitter di 100 risultati abbiamo usato il Paginator di Tweepy che ci ha permesso di paginarli creando pagine da 100 ciascuno. Abbiamo, quindi, fornito come parametro l’id di @kevinRoitero e salvato tutte le informazioni scaricate in un JSON utilizzando la funzione da noi definita nei primi passi.

### Punto 2
 Andando avanti con il progetto, per ciascuno dei follower di @KevinRoitero siamo riusciti a risalire al numero di tweet pubblicati da ogni profilo durante l’ultima settimana utilizzando la funzione `client.get_recent_tweets_count` di Tweepy, la quale, però, ci forniva per ogni utente solamente il conteggio rispettivo al singolo giorno e quindi abbiamo dovuto prendere, per ogni utente, i diversi risultati giorno per giorno e sommarli tutti quanti per trovare il numero di tweet totale dei sette giorni. Dopo aver aggiunto questi risultati sotto la dicitura di “last_week_tweets_count” ai dati salvati relativi alla lista di follower di KevinRoitero, abbiamo serializzato il tutto nel JSON creato in precedenza.

### Punto 3
 Seguendo il punto 3, abbiamo preso in considerazione all’interno della lista di follower di @KevinRoitero solamente gli utenti che avessero profilo non protetto e almeno un follower, e scaricato per ognuno di essi 1000 follower utilizzando ancora la funzione da noi in precedenza definita `get_parsed_users_follower(id)` , salvando quindi per ciascuno le stesse informazioni del punto 1 e aggiungendo poi il risultato sotto la dicitura “followers” nel JSON fatto in precedenza.  
 Per scaricare tutte le informazioni ci sono volute più di due ore e per questo motivo abbiamo salvato il JSON risultante e aperto tramite funzione read_json.  

 ## Creazione dei grafi :
 ### Punto 4
 Arrivati al punto 4 abbiamo messo da parte la libreria Tweepy e iniziato a lavorare con Networkx, ovvero una libreria open source che si occupa della creazione e manipolazione di grafi, e che noi utilizzeremo per analizzare i dati appena ottenuti ed estrapolati da Twitter e per effettuarci delle misurazioni al fine di fare una analisi delle cerchie sociali del profilo di Kevin Roitero. 
Una volta scaricata e importata la libreria abbiamo costruito un grafo che avesse come nodi gli id di Kevin Roitero e dei suoi follower, e come attributi (username, descrizione, numero di follower) gli stessi dei profili twitter presi in considerazione, tutto ciò utilizzando la funzione `Graph.add_node`. Abbiamo quindi effettuato un check basandoci sulle informazioni di cui disponiamo dal JSON ottenuto al punto 3 per verificare le relazioni di following tra i profili e, qualora due profili fossero coinvolti in tale relazione, sono stati legati da degli archi grazie alla funzione `Graph.add_edge`.
In questo modo si è andato a creare un grafo diretto, ovvero un grafo in cui gli archi sono caratterizzati da una direzione e, di conseguenza, in cui  il grado dei nodi si misura sia in archi entranti (In-degree) che in archi uscenti (Out-Degree).

### Punto 5
 Al punto seguente, tuttavia, ci è stato richiesto di trasformare il grafo da diretto a indiretto, pertanto abbiamo utilizzato la apposita funzione `Graph.to_undirected()` andando, in questo modo, a creare un grafo non orientato in cui non vi è più la distinzione tra archi entranti ed archi uscenti, e tale per cui vi siano 2 rappresentazioni equivalenti per lo stesso arco, essendo, esso, per l’appunto, non direzionato. 
Dopodiché, dato che il nostro obiettivo era quello di ampliare il grafo già ottenuto aggiungendo nodi e archi fino ad ottenere il doppio dei nodi rispetto al grafo di partenza seguendo il metodo del “Preferential Attachment”, abbiamo utilizzato la funzione di Networkx chiamata `barabasi_albert_graph` per far sì che i nuovi nodi si colleghino tramite archi agli altri nuovi nodi proporzionalmente al grado di questi ultimi.
Essenza dell’algoritmo dell’ “Attaccamento Preferenziale”, è, infatti, proprio questa tendenza dei nodi a collegarsi a nodi a loro volta già molto collegati e connessi e che quindi dispongono di un alto grado: meccanismo, questo, studiato dall'omonimo ricercatore Albert Laszlo Barabasi, il quale scorse proprio in questo algoritmo l'origine del fenomeno, molto frequente nel mondo reale, delle reti “scale-free”, ovvero quelle reti in cui, tracciando i gradi dei nodi sull’asse x e la probabilità di avere quei gradi nella rete sull’asse y, troviamo che la distribuzione dei gradi risultante su una scala log-log sarà una linea retta (distribuzione “power law”), e in cui possiamo notare la presenza di una stragrande maggioranza di nodi con basso grado e, invece, una piccola cerchia di nodi con un grado di collegamenti che supera la media(Hub).  


## Visualizzazione dei grafi
### Punto 6 RIV. FUNZIONE PER LAYOUT
Una volta riusciti a creare i due grafi richiesti, uno diretto e l'altro indiretto, andremo a visualizzarli graficamente testando sia le funzionalità della libreria Pyvis per ottenere una visualizzazione interattiva, che quelle della libreria NetworkX per la versione statica.  
Per quanto riguarda la prima modalità è bastato usare per entrambi i grafi la funzione `pyvis.network.Network` mentre per la visualizzazione senza animazioni abbiamo visualizzato il grafo usando la funzione `.draw_networkx` e impostando opportunamente i parametri di visualizzazione anche grazie alla libreria matplotlib pyplot.

## Misurazioni
### Punto 7
Per ciascuno dei due grafi abbiamo identificato
