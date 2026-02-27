// ══════════════════════════════════════════════════════════════
//  VHR — Firebase Configuration
//  ⚠️  SOSTITUISCI i valori sotto con le tue credenziali reali
//  Firebase Console → Impostazioni progetto → Le tue app → Config
// ══════════════════════════════════════════════════════════════

import { initializeApp } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-app.js";
import { getAuth, GoogleAuthProvider } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-auth.js";
import { getFirestore } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-firestore.js";
import { getStorage } from "https://www.gstatic.com/firebasejs/10.8.0/firebase-storage.js";

// ── INCOLLA QUI LE TUE CREDENZIALI ─────────────────────────────
const firebaseConfig = {
    apiKey: "AIzaSyC1rtY83qGXO3NV2_MOdIDHMWROH34JKoA",
    authDomain: "studio-5957048529-68f31.firebaseapp.com",
    projectId: "studio-5957048529-68f31",
    storageBucket: "studio-5957048529-68f31.firebasestorage.app",
    messagingSenderId: "5957048529",
    appId: "1:5957048529:web:31220619514035774416"
};
// ───────────────────────────────────────────────────────────────

const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
export const storage = getStorage(app);
export const googleProvider = new GoogleAuthProvider();

// ══════════════════════════════════════════════════════════════
//  STRUTTURA FIRESTORE (da SOP)
//
//  /users/{uid}
//    displayName, email, role (player|merchant|admin),
//    xp, badges[], createdAt, activeMissions[]
//
//  /missions/{id}
//    title, description, element, difficulty, xpReward,
//    price, stops[{id, title, riddleText, markerName,
//                  answer, hintText, locationName}]
//
//  /merchants/{id}
//    name, category, address, logoUrl, approved, uid
//
//  /coupons/{id}
//    merchantId, title, discount, expiresAt,
//    quantity, used, approved
//
//  /completions/{id}
//    userId, missionId, stopId, completedAt, xpEarned
// ══════════════════════════════════════════════════════════════
