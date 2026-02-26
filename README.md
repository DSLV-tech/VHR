# Vercelli Hidden Runes (VHR)

![VRC VHR Banner Concept](https://user-images.githubusercontent.com/assets/banner-placeholder.png) <!-- (Sostituire possibilmente in futuro con un VHR vero logo) -->

**Vercelli Hidden Runes** è un'avventura immersiva in realtà aumentata (AR) che trasforma il centro storico della città in un'arena di gioco interattiva. Integrando le tecnologie AR (tramite *AR.js* / *Three.js*) e l'antica storia dei popoli Celtici "Libui", VHR invita i giocatori a esplorare percorsi misteriosi guidati da antiche rune, scoprire modelli 3D e risolvere enigmi intrecciati con la città vera.

Il progetto vanta cinque **Universi Narrativi**, ciascuno con la sua tematica autonoma ma accomunati dallo stesso ambiente reale:
1. **I - RUNE**: Dai Celti ai misteri Nordici.
2. **II - TAROCCHI (TARO)**: L'epoca dei Visconti e arcani rinascimentali.
3. **III - TEMPLARI (TEMP)**: La geometria sacra e l'eredità cavalleresca.
4. **IV - EGIZIO (EGY)**: Il mito della fondazione torinese che avvolge le brume padane.
5. **V - GITANI (GITA)**: Sinti, Rom e cartomanzia esoterica errante.

## 🚀 La Cella MVP

Questo repository contiene attualmente l'embrione di front-end propedeutico al lancio dell'MVP.
I file inclusi servono per stabilire la *Brand Identity*, la gestione dei *Manuali per Operatori* (SOP) e simulare gli snodi cruciali del pacchetto AR.

### File Principali 📁

* `index.html` : **Dashboard Principale**. Una vetrina elegante e centralizzata (in puro stile Garamond/Cinzel a tema VHR) creata appositamente per facilitare l'accesso allo sviluppatore ai mockup di questo archivio.
* `VHR_Brand_Identity.html` : Sistema Visivo, Linee Guida di stile, Voce del Brand e componenti modulari.
* `VHR_Mission_Cards.html` : Le UI Card delle diverse missioni interattive esplorabili e acquistabili dal giocatore filtrabili per tipologia elementare.
* `VHR_Universi_Narrativi.html` : Documento "Lore-Based" per la presentazione dettagliata dei 5 "Mondi" previsti con roadmap.
* `VHR_SOP_Collega_AI.html` : Standard Operating Procedures (SOP) dedicati al collega AI per lo scaffolding e implementazione backend Firebase + Stripe.
* `A4_Test_Print.html` : Pagina di test ingegnerizzata su layout unicamente *print-friendly* (Foglio A4) atta a posizionare agilmente le prime grafiche "Runa" e preparare il tracciamento target.

## ⚙️ Stack Tecnologico e Backend (Proposto SOP)
Lo Stack previsto per una build scalabile e in produzione è basato su tecnologie cloud native e framework agili:

- **WebAR** e visualizzazione tridimensionale guidate da `AR.js 3.x` e `Three.js` (r128+).
- **Backend / BaaS** delegato unicamente a `Firebase` (Database realtime tramite *Firestore*, *Auth* per login robusti e *Cloud Functions*).
- **Monetizzazione / Transazioni**: Integrazione `Stripe` rigorosamente protetta dalle *Cloud Functions* lato server e mai lato client.

## 🛠 Come Testare
Puoi procedere semplicemente da qualsiasi browser aggiornato aprendo l'eseguibile di ingresso:
1. Apri dal terminale o navigazione cartelle il file principale: `index.html`.
2. Dalla vetrina **Dashboard MVP** sei libero di ispezionare tutta la User Interface già costruita e testare gli stili.
3. Cliccando su "*Stampa Foglio A4*" in basso potrai procedere immediatamente al collaudo del tracciamento di AR.js sui pattern di test.

## 👥 Contributori & Copyright
Sviluppato e concettualizzato per rilancio ed esplorazione videoludica/urbanistica di Vercelli.

Licenza: `Riservata` (Proprietario: DSLV-tech e affiliati di "Vercelli Hidden Runes") 

---
*ᚢ · ᚺ · ᚱ · Vercelli · Svela i Segreti Nascosti*
