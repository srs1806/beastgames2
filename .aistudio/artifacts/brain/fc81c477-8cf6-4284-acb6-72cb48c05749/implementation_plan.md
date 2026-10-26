# Google Gemini AI 3D Celebration & Milestone Engine Plan

Architectural blueprint for integrating server-side Google Gemini AI (`gemini-3.8-flash`) to generate unique, personalized celebrations for viewers at key episode milestones (3, 5, 8, and the Grand 10-Episode Champion celebration). The celebration triggers strictly upon closing the video player, adapts fluidly across all mobile and desktop screen sizes with responsive 3D miniature depth, and automatically resets on the user's next visit.

## User Review & Critical Decisions

> [!IMPORTANT]
> The following core behaviors were confirmed by the user:

- **AI-Powered Personalization**: Real Gemini AI generation (`gemini-3.8-flash`) via server-side `/api/ai/celebrate` that crafts unique, tailored victory speeches, tactical ratings, and survival praises for each viewer's registered username and avatar.
- **Milestone Tier Celebrations**: Triggers at milestone badges:
  - **3 Episodes**: Bronze Survivor badge celebration with custom AI commentary.
  - **5 Episodes**: Silver Tactician badge celebration with custom AI commentary.
  - **8 Episodes**: Gold Eliminator badge celebration with custom AI commentary.
  - **10 Episodes**: Grand 3D Champion Celebration with 3D Gold Panther Trophy, AI Survival Assessment, and $5,000,000 Championship Certificate.
- **Strict Exit Trigger**: The celebration **only** fires when the user closes/exits the video player (`closeVideoPlayer()`), never during playback.
- **Device-Sustainable 3D Miniature Card**: Uses fluid CSS clamping (`clamp()`), stereoscopic 3D perspective (`perspective: 1400px; transform-style: preserve-3d`), dynamic viewport units (`dvh` / `vw`), and touch-friendly scaling for phones, tablets, and desktops.
- **Next-Visit Fresh Reset**: If a user previously completed all 10 episodes and celebrated, their next visit opens cleanly without repeating the celebration, resetting watched episodes to 0 so they can start fresh.

---

## 1. System Architecture & Execution Flow

```
┌─────────────────────────────────────────────────────────────┐
│                 USER WATCHES IN VIDEO THEATER               │
│  (Marks Episode 3, 5, 8, or 10 as completed)                │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│               USER CLOSES VIDEO PLAYER (EXIT)               │
│  • Halts video & audio stream immediately                   │
│  • Checks for uncelebrated milestone (3, 5, 8, or 10)       │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│       SERVER-SIDE GEMINI API CALL (/api/ai/celebrate)       │
│  • Model: 'gemini-3.8-flash'                                │
│  • Input: Username, Avatar, Milestone (3, 5, 8, or 10)      │
│  • Output: Unique personalized AI commentary & tactical IQ  │
│  • Graceful fallback to localized templates if offline      │
└──────────────────────────────┬──────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────┐
│         RESPONSIVE 3D MINIATURE CELEBRATION MODAL           │
│  • Fluid card scaling: clamp(300px, 90vw, 520px)            │
│  • 3D rotating trophy / badge with gold & neon particle rays│
│  • Animated AI commentary with typing effect                │
│  • Fireworks, confetti cannons, and audio fanfare           │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Server-Side Gemini API Implementation (`server.ts`)

- Expose a secure server-side endpoint `POST /api/ai/celebrate`.
- Uses `@google/genai` with `gemini-3.8-flash` and `User-Agent: 'aistudio-build'`.
- System instruction prompts the model in the high-energy, electrifying voice of the official Beast Games referee and analyst.
- Returns structured JSON:
  ```json
  {
    "title": "ULTIMATE SURVIVOR",
    "badgeTitle": "Grand Champion",
    "tacticalIq": "99.8%",
    "commentary": "Personalized speech generated dynamically for [Username]..."
  }
  ```

---

## 3. Responsive 3D Miniature Frontend Experience (`index.html`)

- **3D Stereoscopic Stage**:
  - `perspective: 1400px; transform-style: preserve-3d;`
  - Floating 3D Gold Panther Trophy (for 10 episodes) or 3D Holographic Medallion (for 3, 5, 8).
  - Concentric rotating neon laser rings in gold (`#facc15`) and cyan (`#38bdf8`).
- **Device Sustainability**:
  - Height fits within `max-height: 90dvh` with internal scroll if needed on ultra-compact phones.
  - Width scales smoothly via `width: min(92vw, 480px)`.
- **Milestone Tracking**:
  - Tracks `beast_celebrated_milestones` array in `localStorage` so each milestone (3, 5, 8, 10) is celebrated once per cycle.
  - On the user's next visit after completing all 10 episodes, the cycle resets automatically.
