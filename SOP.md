# Vercellae Hidden Runes (VHR) — V2 Architecture SOP

Questo documento rappresenta la **Standard Operating Procedure (Procedura Operativa Standard)** aggiornata per lo sviluppo, l'avvio e la manutenzione della piattaforma *Vercellae Hidden Runes*.

Il progetto è stato migrato da un'architettura statica Vanilla HTML/JS ad una moderna **Single Page Application (SPA)** basata su framework **Next.js (App Router)** e **React**.

---

## Struttura del Progetto

Il cuore dell'applicativo si trova all'interno della cartella `vhr-web`. Non vi è più bisogno di usare script Python o Live Server per avviare l'app dalla cartella radice (i vecchi file HTML prototipo sono stati archiviati nella cartella `legacy_vhr_v1` a scopo di storico).

```text
VHR/
├── vhr-web/                 <-- La vera applicazione Next.js
│   ├── src/
│   │   ├── app/             <-- Rotte (Login, Register, Dashboard, AR Scanner)
│   │   ├── components/ui/   <-- Componenti React riutilizzabili (Pulsanti, Navbar)
│   │   ├── contexts/        <-- Provider di stato globale (Es: AuthContext per Firebase)
│   │   └── lib/             <-- Configurazione SDK (Es: firebase.ts)
│   ├── public/              <-- Assets asincroni (Immagini, CSS PWA)
│   ├── tailwind.config.ts   <-- Variabili CSS Brand VHR (Oro, Inchiostro, Pergamena)
│   └── package.json         <-- Definizioni pacchetto e script NodeJS
└── legacy_vhr_v1/           <-- Archivi storici del prototipo V1 in HTML (da ignorare per lo sviluppo)
```

---

## 1. Avviare l'Applicazione in Locale

Per testare e sviluppare il progetto sul proprio computer, Next.js offre un server di sviluppo ultra-reattivo (Hot Module Reloading) che ricarica automaticamente la pagina quando si salva una modifica al codice sorgente TypeScript/React.

**Prima esecuzione (se si clona il progetto su un nuovo PC):**
1. Aprire il terminale e spostarsi nella cartella web: `cd vhr-web`
2. Installare le dipendenze: `npm install`

**Avvio Quotidiano (Fase di Sviluppo):**
1. Aprire il terminale e spostarsi nella cartella web: `cd VHR/vhr-web`
2. Digitare: `npm run dev`
3. Il server partirà. Aprire il browser all'indirizzo `http://localhost:3000`.

---

## 2. Piattaforma Database: Firebase

L'intera applicazione dipende dall'infrastruttura Cloud database e Auth fornita dal progetto "studio-5957048529" di Firebase. La sua configurazione vitale (`config.apiKey`) è salvata e definita nel file `src/lib/firebase.ts`.
Il client React interroga istantaneamente Firebase per conoscere il Ruolo dell'utente connesso e per aggiornare in tempo reale Coupons, Merchants e Missioni.

### Ruoli di Sicurezza:
Il sistema riconosce tre strati di navigazione tramite l' `AuthContext`:
- **Player (Default):** Qualsiasi utente (Google o Email) accederà alla `/dashboard` del giocatore.
- **Merchant (Commerciante):** Un utente approvato che riceve un flag `roles_merchant` dall'amministratore verrà renderizzato sulla pagina dedicata `/merchant/dashboard`.
- **Admin (Guardiano):** Ha i super-poteri per approvare commercianti, creare missioni, visionare i log tramite la vista `/admin`.

---

## 3. Deployment Pubblico (Vercel)

Trattandosi di un'applicazione Next.js, lo standard architetturale prevede l'uso di [Vercel](https://vercel.com/) per l'hosting. Il deploy è interamente automatizzato.

1. Creare un account gratuito su **Vercel** usando Google o GitHub.
2. Caricare l'intera cartella `/VHR` su una Repository privata di **GitHub**.
3. Sulla Dashboard di Vercel, cliccare *"Add New Project"* e importare il container GitHub.
4. **ATTENZIONE:** Configurare il `Root Directory` in Vercel specificando `vhr-web`.
5. Vercel costruirà, ottimizzerà e pubblicherà automaticamente l'applicazione in tutto il mondo all'URL generato (es: `vercellae-hidden-runes.vercel.app`), dotando il server di certificato SSL universale necessario per le fotocamere AR.

Ogni `git push origin main` al codice aggiornerà contestualmente la piattaforma e i server Cloud.

---

## 4. Scansione AR e Realtà Aumentata (A-Frame)

La logica della camera (`<ArScanner>`) risiede sotto `src/app/scanner/page.tsx` ed è isolata per non andare in conflitto con l'albero virtuale (Virtual DOM) di React. 
Eventuali aggiornamenti alla UI del sensore vanno manipolati esclusivamente dentro il wrapper di montaggio (useRef, useEffect) evitando stili globali che romperebbero il posizionamento z-index estremo nativo della webcam di ARJS.
I pattern visivi `*.patt` e le primitive vettoriali non vanno compilate ma vanno servite libere (raw) dentro `vhr-web/public/assets/`.
