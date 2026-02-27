README — Marker AR per VHR
==========================

Il file `marker-uruz.patt` è il pattern AR.js per la runa ᚢ (Uruz).

Per generarlo correttamente:

1. Stampa la pagina A4_Test_Print.html con la runa ᚢ (già configurata)
2. Vai su: https://jeromeetienne.github.io/AR.js/three.js/examples/marker-training/examples/train-marker.html
3. Carica l'immagine della runa stampata (screenshot della parte centrale)
4. Scarica il file .patt generato
5. Salva come: assets/markers/marker-uruz.patt

NOTA: Per testing desktop, AR.js usa automaticamente il marker Hiro standard
(incluso nella libreria) — non serve nessun marker fisico per testare
il flusso completo sul PC.

Per i marker fisici delle singole tappe:
- Tappa 1 — ᚢ (Uruz)    → marker-uruz.patt
- Tappa 2 — ᚷ (Gebo)    → marker-gebo.patt
- Tappa 3 — ᚺ (Hagalaz) → marker-hagalaz.patt
- Tappa 4 — ᚱ (Raido)   → marker-raido.patt
- Tappa 5 — ᛖ (Ehwaz)   → marker-ehwaz.patt
- Tappa 6 — ᛚ (Laguz)   → marker-laguz.patt

Usa A4_Test_Print.html per stampare ogni runa separatamente.
Il bordo nero spesso è FONDAMENTALE per il riconoscimento AR.
