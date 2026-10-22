import re

with open('./index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove the floating block behind footer:
# <div style="position:fixed;bottom:20px;right:20px; ... Designed by Trendz of Shahid</div>
old_block_pattern = r'<div style="\s*position:fixed;bottom:20px;right:20px;[\s\S]*?⚡ Designed by Trendz of Shahid\s*</div>'
html = re.sub(old_block_pattern, '', html, count=1)

# 2. Add new CSS before </style>
css_to_add = '''
/* ================= STARTING INTRO LOADER ANIMATION ================= */
.intro-loader {
  position: fixed;
  inset: 0;
  z-index: 100000;
  background: radial-gradient(circle at center, #0f172a 0%, #030712 70%, #000000 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  overflow: hidden;
  transition: opacity 0.8s cubic-bezier(0.4, 0, 0.2, 1), transform 0.8s cubic-bezier(0.4, 0, 0.2, 1), visibility 0.8s;
}

.intro-loader.fade-out {
  opacity: 0;
  transform: scale(1.08);
  pointer-events: none;
  visibility: hidden;
}

.intro-bg-glow {
  position: absolute;
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(0, 229, 255, 0.22) 0%, rgba(255, 0, 100, 0.12) 45%, transparent 70%);
  filter: blur(50px);
  animation: introGlowPulse 3s ease-in-out infinite alternate;
  pointer-events: none;
}

@keyframes introGlowPulse {
  0% { transform: scale(0.9) rotate(0deg); opacity: 0.6; }
  100% { transform: scale(1.25) rotate(180deg); opacity: 1; }
}

.intro-content {
  position: relative;
  z-index: 2;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 30px 20px;
  max-width: 520px;
  width: 90%;
}

.intro-logo-container {
  position: relative;
  width: 140px;
  height: 140px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 25px;
}

.intro-logo {
  width: 110px;
  height: 110px;
  border-radius: 50%;
  object-fit: cover;
  border: 4px solid #00e5ff;
  box-shadow: 0 0 35px rgba(0, 229, 255, 0.7), 0 0 70px rgba(255, 0, 120, 0.4);
  animation: logoEntrance 1.1s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards, logoFloating 3s ease-in-out infinite 1.2s;
  z-index: 3;
}

.intro-ring-pulse {
  position: absolute;
  inset: -8px;
  border-radius: 50%;
  border: 2px dashed #00e5ff;
  animation: ringSpin 6s linear infinite;
}

.intro-ring-outer {
  position: absolute;
  inset: -18px;
  border-radius: 50%;
  border: 2px solid rgba(255, 215, 0, 0.5);
  border-top-color: transparent;
  border-bottom-color: transparent;
  animation: ringSpinRev 4s linear infinite;
}

@keyframes logoEntrance {
  0% {
    transform: scale(0.1) rotate(-180deg);
    opacity: 0;
    filter: brightness(3) blur(10px);
  }
  60% {
    transform: scale(1.18) rotate(10deg);
    opacity: 1;
    filter: brightness(1.5) blur(0);
  }
  100% {
    transform: scale(1) rotate(0deg);
    opacity: 1;
    filter: brightness(1);
  }
}

@keyframes logoFloating {
  0%, 100% { transform: translateY(0px) scale(1); }
  50% { transform: translateY(-8px) scale(1.03); }
}

@keyframes ringSpin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

@keyframes ringSpinRev {
  0% { transform: rotate(360deg); }
  100% { transform: rotate(0deg); }
}

.intro-title {
  font-size: 2rem;
  font-weight: 800;
  letter-spacing: 2px;
  background: linear-gradient(90deg, #ff0055, #ffdd00, #00e5ff, #ff0055);
  background-size: 300% 100%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: shimmerText 3s linear infinite, titleEntrance 0.8s ease-out 0.4s both;
  margin-bottom: 12px;
  text-shadow: 0 0 25px rgba(255, 215, 0, 0.5);
}

@keyframes shimmerText {
  0% { background-position: 0% 50%; }
  100% { background-position: 300% 50%; }
}

@keyframes titleEntrance {
  from {
    opacity: 0;
    transform: translateY(20px);
    letter-spacing: 6px;
  }
  to {
    opacity: 1;
    transform: translateY(0);
    letter-spacing: 2px;
  }
}

.intro-subtitle {
  color: #94a3b8;
  font-size: 0.95rem;
  margin-bottom: 22px;
  min-height: 24px;
  font-weight: 500;
  transition: all 0.3s ease;
}

.intro-progress-container {
  width: 100%;
  max-width: 380px;
  height: 8px;
  background: rgba(255, 255, 255, 0.09);
  border-radius: 999px;
  overflow: hidden;
  position: relative;
  border: 1px solid rgba(0, 229, 255, 0.3);
  box-shadow: 0 0 15px rgba(0, 229, 255, 0.2);
}

.intro-progress-bar {
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, #00e5ff, #3b82f6, #ec4899, #ffd700);
  background-size: 200% 100%;
  border-radius: 999px;
  transition: width 0.15s ease-out;
  animation: progressShine 2s linear infinite;
  box-shadow: 0 0 12px rgba(0, 229, 255, 0.8);
}

@keyframes progressShine {
  0% { background-position: 100% 0; }
  100% { background-position: -100% 0; }
}

.intro-stats {
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  max-width: 380px;
  margin-top: 10px;
  font-size: 0.85rem;
  color: #cbd5e1;
}

.intro-chip {
  background: rgba(0, 229, 255, 0.15);
  border: 1px solid rgba(0, 229, 255, 0.4);
  color: #00e5ff;
  padding: 2px 10px;
  border-radius: 20px;
  font-size: 0.75rem;
  text-transform: uppercase;
  font-weight: 600;
  letter-spacing: 1px;
}

/* ================= UPGRADED GATE & 3D FLIP ================= */
body {
  perspective: 1600px;
  padding-bottom: 50px;
}

#gate {
  position: fixed;
  inset: 0;
  background: radial-gradient(circle at center, rgba(15, 23, 42, 0.98) 0%, rgba(5, 5, 5, 0.99) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  text-align: center;
  z-index: 9999;
  padding: 20px;
  backface-visibility: hidden;
  transform-style: preserve-3d;
  transition: filter 0.5s ease;
}

.gate-card {
  background: linear-gradient(145deg, rgba(30, 41, 59, 0.88), rgba(15, 23, 42, 0.96));
  border: 1px solid rgba(0, 229, 255, 0.32);
  box-shadow: 0 25px 55px rgba(0, 0, 0, 0.85), 0 0 40px rgba(0, 229, 255, 0.25);
  border-radius: 26px;
  padding: 38px 28px;
  max-width: 440px;
  width: 100%;
  backdrop-filter: blur(20px);
  position: relative;
  overflow: hidden;
}

.gate-card::before {
  content: "";
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(0, 229, 255, 0.08) 0%, transparent 60%);
  pointer-events: none;
}

.gate-logo-box {
  position: relative;
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 8px;
}

.gate-logo {
  width: 96px;
  height: 96px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #00e5ff;
  box-shadow: 0 0 25px rgba(0, 229, 255, 0.5);
  animation: logoFloating 3s ease-in-out infinite;
}

.gate-status-pill {
  margin-top: 10px;
  background: rgba(239, 68, 68, 0.18);
  border: 1px solid rgba(239, 68, 68, 0.4);
  color: #fca5a5;
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 1px;
  text-transform: uppercase;
  padding: 4px 14px;
  border-radius: 20px;
}

.gate-status-pill.unlocked-pill {
  background: rgba(34, 197, 94, 0.2);
  border-color: rgba(34, 197, 94, 0.5);
  color: #86efac;
}

.gate-card h1 {
  font-size: 1.85rem;
  font-weight: 700;
  margin-top: 14px;
  color: #ffffff;
  text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
}

.gate-desc {
  font-size: 0.92rem;
  color: #cbd5e1;
  margin-top: 8px;
  line-height: 1.55;
}

.gate-desc strong {
  color: #00e5ff;
}

.gate-steps {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 12px;
  margin: 22px 0 16px;
}

.gate-step {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border-radius: 20px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  font-size: 0.82rem;
  font-weight: 600;
  color: #94a3b8;
  transition: all 0.3s ease;
}

.gate-step .step-num {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.72rem;
}

.gate-step.active {
  background: rgba(239, 68, 68, 0.18);
  border-color: rgba(239, 68, 68, 0.5);
  color: #f87171;
}

.gate-step.active .step-num {
  background: #ef4444;
  color: white;
}

.gate-step.completed {
  background: rgba(34, 197, 94, 0.18);
  border-color: rgba(34, 197, 94, 0.5);
  color: #4ade80;
}

.gate-step.completed .step-num {
  background: #22c55e;
  color: white;
}

.step-arrow {
  color: #64748b;
  font-weight: 700;
}

.gate-actions {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-top: 10px;
}

.gate-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 15px 22px;
  border-radius: 14px;
  font-size: 1rem;
  font-weight: 700;
  text-decoration: none;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-sizing: border-box;
  width: 100%;
  border: none;
}

.subscribe-btn {
  background: linear-gradient(135deg, #ff0000, #cc0000);
  color: white;
  box-shadow: 0 4px 20px rgba(255, 0, 0, 0.4);
  position: relative;
  overflow: hidden;
}

.subscribe-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 30px rgba(255, 0, 0, 0.6);
  filter: brightness(1.1);
}

.subscribe-btn.verified {
  background: linear-gradient(135deg, #10b981, #059669);
  box-shadow: 0 4px 20px rgba(16, 185, 129, 0.4);
}

.gate-quick-btn {
  background: transparent;
  border: none;
  color: #38bdf8;
  font-size: 0.82rem;
  font-weight: 600;
  cursor: pointer;
  padding: 4px;
  transition: color 0.2s, transform 0.2s;
}

.gate-quick-btn:hover {
  color: #7dd3fc;
  text-decoration: underline;
  transform: scale(1.02);
}

.sub-verifying-box {
  background: rgba(0, 0, 0, 0.35);
  border: 1px solid rgba(0, 229, 255, 0.25);
  border-radius: 12px;
  padding: 12px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  align-items: center;
}

.sub-spinner {
  width: 26px;
  height: 26px;
  border: 3px solid rgba(0, 229, 255, 0.2);
  border-top-color: #00e5ff;
  border-radius: 50%;
  animation: ringSpin 0.8s linear infinite;
}

.sub-verify-text {
  font-size: 0.82rem;
  color: #38bdf8;
  font-weight: 600;
}

.sub-verify-bar {
  width: 100%;
  height: 5px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 4px;
  overflow: hidden;
}

.sub-verify-fill {
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, #00e5ff, #38bdf8);
  transition: width 0.3s linear;
}

.unlock-btn {
  background: #334155;
  color: #94a3b8;
  cursor: not-allowed;
  opacity: 0.7;
}

.unlock-btn.active {
  background: linear-gradient(135deg, #00e5ff, #2563eb);
  color: white;
  cursor: pointer;
  opacity: 1;
  box-shadow: 0 4px 25px rgba(0, 229, 255, 0.5);
  transform: scale(1.02);
  animation: pulseGlow 1.8s infinite alternate;
}

@keyframes pulseGlow {
  0% { box-shadow: 0 4px 20px rgba(0, 229, 255, 0.4); transform: scale(1.01); }
  100% { box-shadow: 0 6px 35px rgba(0, 229, 255, 0.8), 0 0 20px rgba(255, 215, 0, 0.6); transform: scale(1.04); }
}

.gate-alert {
  margin-top: 14px;
  padding: 10px 14px;
  border-radius: 10px;
  font-size: 0.82rem;
  font-weight: 600;
  text-align: center;
  animation: shakeAlert 0.4s ease;
}

.gate-alert.error {
  background: rgba(239, 68, 68, 0.15);
  border: 1px solid rgba(239, 68, 68, 0.4);
  color: #fca5a5;
}

.gate-alert.success {
  background: rgba(34, 197, 94, 0.18);
  border: 1px solid rgba(34, 197, 94, 0.5);
  color: #86efac;
}

@keyframes shakeAlert {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-6px); }
  75% { transform: translateX(6px); }
}

/* 3D FLIP ANIMATIONS */
.gate-flipping-out {
  animation: gate3DFlip 1.2s cubic-bezier(0.7, 0, 0.3, 1) forwards !important;
  pointer-events: none;
}

.site-flipping-in {
  display: block !important;
  animation: site3DFlip 1.2s cubic-bezier(0.7, 0, 0.3, 1) 0.15s both !important;
  transform-origin: center center;
  backface-visibility: hidden;
}

@keyframes gate3DFlip {
  0% {
    transform: perspective(1600px) rotateY(0deg) scale(1);
    opacity: 1;
    filter: brightness(1);
  }
  50% {
    transform: perspective(1600px) rotateY(-90deg) scale(0.85);
    opacity: 0.6;
    filter: brightness(1.8) drop-shadow(0 0 50px #00e5ff);
  }
  100% {
    transform: perspective(1600px) rotateY(-180deg) scale(0.7);
    opacity: 0;
    visibility: hidden;
  }
}

@keyframes site3DFlip {
  0% {
    transform: perspective(1600px) rotateY(180deg) scale(0.7);
    opacity: 0;
    filter: brightness(2) drop-shadow(0 0 60px #ffd700);
  }
  50% {
    transform: perspective(1600px) rotateY(90deg) scale(0.85);
    opacity: 0.7;
    filter: brightness(1.5);
  }
  100% {
    transform: perspective(1600px) rotateY(0deg) scale(1);
    opacity: 1;
    filter: brightness(1);
  }
}

.unlocked-toast {
  position: fixed;
  top: 20px;
  left: 50%;
  transform: translateX(-50%) translateY(-100px);
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.95), rgba(6, 95, 70, 0.95));
  border: 1px solid rgba(52, 211, 153, 0.5);
  color: white;
  padding: 12px 24px;
  border-radius: 999px;
  font-size: 0.92rem;
  font-weight: 700;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5), 0 0 25px rgba(52, 211, 153, 0.6);
  z-index: 999999;
  display: flex;
  align-items: center;
  gap: 8px;
  transition: transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.unlocked-toast.show {
  transform: translateX(-50%) translateY(0);
}

/* ================= CREATOR BADGE & ULTRA-COMPACT FOOTER ================= */
.creator-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 999px;
  padding: 4px 12px;
  font-size: 0.75rem;
  color: var(--text);
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.25);
  white-space: nowrap;
}

.creator-badge:hover {
  border-color: rgba(0, 229, 255, 0.5);
  box-shadow: 0 0 15px rgba(0, 229, 255, 0.35);
  transform: translateY(-1px);
}

.creator-badge-logo {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  object-fit: cover;
  border: 1.5px solid #00e5ff;
  box-shadow: 0 0 8px rgba(0, 229, 255, 0.6);
  flex-shrink: 0;
}

.creator-author strong {
  color: #00e5ff;
  font-weight: 700;
}

.top-bar-creator {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-bottom: 12px;
}

.top-bar-creator .creator-badge {
  padding: 5px 15px;
  font-size: 0.8rem;
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.09), rgba(0, 229, 255, 0.06));
  border: 1px solid rgba(0, 229, 255, 0.35);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3), 0 0 15px rgba(0, 229, 255, 0.2);
}

.love-heart {
  color: #ff3366;
  font-size: 0.84rem;
  animation: heartBeat 1.4s infinite;
  display: inline-block;
}

@keyframes heartBeat {
  0%, 100% { transform: scale(1); }
  14% { transform: scale(1.25); }
  28% { transform: scale(1); }
  42% { transform: scale(1.18); }
  70% { transform: scale(1); }
}

footer {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background: rgba(10, 15, 29, 0.94);
  backdrop-filter: blur(14px);
  -webkit-backdrop-filter: blur(14px);
  border-top: 1px solid rgba(255, 255, 255, 0.12);
  color: var(--muted);
  z-index: 999;
  padding: 5px 12px;
  font-size: 0.74rem;
  box-shadow: 0 -4px 20px rgba(0, 0, 0, 0.4);
}

.footer-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 8px;
  max-width: 1400px;
  margin: 0 auto;
  width: 100%;
}

.footer-left {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-shrink: 0;
  font-size: 0.72rem;
}

.footer-links {
  display: flex;
  align-items: center;
  gap: 5px;
  flex-wrap: nowrap;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none;
  padding: 2px 0;
}

.footer-links::-webkit-scrollbar {
  display: none;
}

.footer-btn {
  padding: 4px 8px;
  border-radius: 999px;
  text-decoration: none;
  font-weight: 600;
  font-size: 0.68rem;
  color: var(--text);
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 255, 255, 0.16);
  backdrop-filter: blur(8px);
  transition: all 0.2s ease;
  white-space: nowrap;
  flex-shrink: 0;
  display: inline-flex;
  align-items: center;
  gap: 3px;
  cursor: pointer;
}

.footer-btn:hover {
  transform: translateY(-1px);
  background: linear-gradient(90deg, #00e5ff, #2563eb);
  color: white;
  border-color: #00e5ff;
}

.footer-sub-btn {
  background: linear-gradient(90deg, #dc2626, #ef4444);
  color: white;
  border-color: #f87171;
  box-shadow: 0 0 10px rgba(239, 68, 68, 0.5);
  font-weight: 700;
  animation: pulseSubTiny 2s infinite ease-in-out;
}

@keyframes pulseSubTiny {
  0%, 100% { transform: scale(1); box-shadow: 0 0 8px rgba(239, 68, 68, 0.4); }
  50% { transform: scale(1.05); box-shadow: 0 0 14px rgba(239, 68, 68, 0.85); }
}

@media (max-width: 768px) {
  footer {
    padding: 4px 8px;
  }
  .footer-container {
    flex-direction: column;
    gap: 4px;
    align-items: center;
  }
  .footer-left {
    gap: 6px;
    font-size: 0.68rem;
    flex-wrap: wrap;
    justify-content: center;
  }
  .footer-badge {
    padding: 2px 8px;
    font-size: 0.66rem;
  }
  .footer-badge .creator-badge-logo {
    width: 16px;
    height: 16px;
  }
  .footer-links {
    width: 100%;
    justify-content: center;
    gap: 4px;
    padding: 1px 0;
  }
  .footer-btn {
    padding: 3px 6px;
    font-size: 0.62rem;
  }
  body {
    padding-bottom: 60px;
  }
}

@media (min-width: 769px) {
  body {
    padding-bottom: 45px;
  }
}
'''

html = html.replace('</style>', css_to_add + '\n</style>', 1)

# 3. Add Intro Loader right after <body>
intro_markup = '''
<!-- ================= STARTING INTRO LOADER ================= -->
<div id="introLoader" class="intro-loader">
  <div class="intro-bg-glow"></div>
  <div class="intro-content">
    <div class="intro-logo-container">
      <div class="intro-ring-pulse"></div>
      <div class="intro-ring-outer"></div>
      <img
        src="https://yt3.googleusercontent.com/M1CoAorn3TEsFnY7XEoCyOU6JFkbe4kC-vLrCG5osjh7Cs6akWEeSW59xcZ7YUCfWSCMT87sUQ=s160-c-k-c0x00ffffff-no-rj"
        class="intro-logo"
        alt="Beast Games Logo"
      />
    </div>
    <h1 class="intro-title">🔥 BEAST GAMES SEASON 2 🔥</h1>
    <p class="intro-subtitle" id="introStatus">⚔️ Initializing Beast Arena...</p>
    <div class="intro-progress-container">
      <div class="intro-progress-bar" id="introProgressFill"></div>
    </div>
    <div class="intro-stats">
      <span id="introPercent">0%</span>
      <span class="intro-chip">Official Arena</span>
    </div>
  </div>
</div>
'''

html = html.replace('<body>', '<body>\n' + intro_markup, 1)

# 4. Replace #gate markup with upgraded gate card
old_gate_regex = r'<div id="gate">[\s\S]*?</div>\s*<!-- ================= WEBSITE ================= -->'

new_gate_markup = '''<!-- ================= LOCK SCREEN ================= -->
<div id="gate" class="gate-container">
  <div class="gate-card">
    <div class="gate-logo-box">
      <img
        src="https://yt3.googleusercontent.com/M1CoAorn3TEsFnY7XEoCyOU6JFkbe4kC-vLrCG5osjh7Cs6akWEeSW59xcZ7YUCfWSCMT87sUQ=s160-c-k-c0x00ffffff-no-rj"
        class="gate-logo"
        alt="Trendz of Shahid Logo"
      />
      <div class="gate-status-pill">🔒 Access Locked</div>
    </div>

    <h1>🔥 Subscribe to Unlock 🔥</h1>
    <p class="gate-desc">
      Subscribe to <strong>Trendz of Shahid</strong> on YouTube to unlock all 10 full episodes, badges, and games!
    </p>

    <!-- STEP PROGRESS -->
    <div class="gate-steps">
      <div class="gate-step active" id="step1Indicator">
        <span class="step-num">1</span>
        <span class="step-text">Subscribe</span>
      </div>
      <div class="step-arrow">→</div>
      <div class="gate-step" id="step2Indicator">
        <span class="step-num">2</span>
        <span class="step-text">Unlock</span>
      </div>
    </div>

    <!-- ACTION BUTTONS -->
    <div class="gate-actions">
      <a
        href="https://www.youtube.com/@TrendzOfShahid?sub_confirmation=1"
        target="_blank"
        rel="noopener noreferrer"
        class="gate-btn subscribe-btn"
        id="subscribeBtn"
      >
        <span>🔴</span>
        <span id="subBtnText">Subscribe Channel</span>
      </a>

      <!-- Quick instant verification button -->
      <button class="gate-quick-btn" id="quickVerifyBtn" type="button">
        ⚡ Already Subscribed? Click to Instant Verify
      </button>

      <!-- Verification progress box -->
      <div id="subVerifyingBox" class="sub-verifying-box" style="display:none;">
        <div class="sub-spinner"></div>
        <div class="sub-verify-text" id="subVerifyText">Connecting to YouTube channel...</div>
        <div class="sub-verify-bar">
          <div class="sub-verify-fill" id="subVerifyFill"></div>
        </div>
      </div>

      <button
        class="gate-btn unlock-btn"
        id="unlockBtn"
        disabled
        type="button"
      >
        🔒 I Have Subscribed
      </button>
    </div>

    <!-- Alert notice inside gate -->
    <div id="gateAlert" class="gate-alert" style="display:none;"></div>
  </div>
</div>

<!-- ================= WEBSITE ================= -->'''

assert re.search(old_gate_regex, html) is not None, "Could not find old gate markup"
html = re.sub(old_gate_regex, new_gate_markup, html, count=1)

# 5. Add "Made with love {logo} by Shahid Shaikh" in Top Bar (inside <header>)
top_badge = '''<header>
  <!-- TOP BAR CREATOR BADGE -->
  <div class="top-bar-creator">
    <div class="creator-badge">
      <span class="love-heart">❤️</span>
      <span>Made with love</span>
      <img
        src="https://yt3.googleusercontent.com/M1CoAorn3TEsFnY7XEoCyOU6JFkbe4kC-vLrCG5osjh7Cs6akWEeSW59xcZ7YUCfWSCMT87sUQ=s160-c-k-c0x00ffffff-no-rj"
        class="creator-badge-logo"
        alt="Shahid Shaikh Logo"
      />
      <span class="creator-author">by <strong class="author-name">Shahid Shaikh</strong></span>
    </div>
  </div>'''

html = html.replace('<header>', top_badge, 1)

# 6. Replace Footer with modern, compact, mobile-friendly footer with creator badge beside subscribe
old_footer_regex = r'<footer>[\s\S]*?</footer>'

new_footer_markup = '''<footer>
  <div class="footer-container">
    <div class="footer-left">
      <span>© 2026 Beast Games Season 2</span>
      <!-- FOOTER CREATOR BADGE BESIDE SUBSCRIBE -->
      <div class="creator-badge footer-badge">
        <span class="love-heart">❤️</span>
        <span>Made with love</span>
        <img
          src="https://yt3.googleusercontent.com/M1CoAorn3TEsFnY7XEoCyOU6JFkbe4kC-vLrCG5osjh7Cs6akWEeSW59xcZ7YUCfWSCMT87sUQ=s160-c-k-c0x00ffffff-no-rj"
          class="creator-badge-logo"
          alt="Shahid Shaikh Logo"
        />
        <span class="creator-author">by <strong class="author-name">Shahid Shaikh</strong></span>
      </div>
    </div>

    <div class="footer-links">
      <a class="footer-btn" href="about.html">ℹ About</a>
      <a class="footer-btn" href="privacy.html">🔐 Privacy</a>
      <a class="footer-btn" href="terms.html">📜 Terms</a>
      <a class="footer-btn" href="contact.html">📞 Contact</a>
      <a class="footer-btn" href="disclaimer.html">⚠ Disclaimer</a>
      <a
        class="footer-btn footer-sub-btn"
        href="https://www.youtube.com/@TrendzOfShahid?sub_confirmation=1"
        target="_blank"
        rel="noopener noreferrer"
      >
        🔴 Subscribe
      </a>
      <button onclick="resetGate()" class="footer-btn replay-btn" type="button" title="Replay intro animation & lock screen">
        🔄 Replay
      </button>
    </div>
  </div>
</footer>'''

assert re.search(old_footer_regex, html) is not None, "Could not find footer markup"
html = re.sub(old_footer_regex, new_footer_markup, html, count=1)

# 7. Replace JavaScript
old_js_regex = r'let subscribed = false;[\s\S]*?window\.addEventListener\(\s*"load"[\s\S]*?\}\s*\);'

new_js = '''// ================= AUDIO SYNTHESIZER =================
function playBeastSound(type) {
  try {
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    if (!AudioCtx) return;
    const ctx = new AudioCtx();
    if (ctx.state === "suspended") ctx.resume();

    if (type === "unlock") {
      const notes = [523.25, 659.25, 783.99, 1046.50, 1318.51];
      notes.forEach((freq, idx) => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = "triangle";
        osc.frequency.setValueAtTime(freq, ctx.currentTime + idx * 0.08);
        gain.gain.setValueAtTime(0.2, ctx.currentTime + idx * 0.08);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + idx * 0.08 + 0.45);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(ctx.currentTime + idx * 0.08);
        osc.stop(ctx.currentTime + idx * 0.08 + 0.5);
      });
    } else if (type === "verify") {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(440, ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(880, ctx.currentTime + 0.18);
      gain.gain.setValueAtTime(0.2, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.35);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + 0.4);
    } else if (type === "click") {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.type = "sine";
      osc.frequency.setValueAtTime(600, ctx.currentTime);
      gain.gain.setValueAtTime(0.12, ctx.currentTime);
      gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.06);
      osc.connect(gain);
      gain.connect(ctx.destination);
      osc.start();
      osc.stop(ctx.currentTime + 0.07);
    }
  } catch (err) {}
}

// ================= STARTING INTRO ANIMATION =================
function runIntroAnimation() {
  const intro = document.getElementById("introLoader");
  if (!intro) return;

  const fill = document.getElementById("introProgressFill");
  const percent = document.getElementById("introPercent");
  const status = document.getElementById("introStatus");

  const stages = [
    { p: 20, text: "⚔️ Initializing Beast Arena..." },
    { p: 50, text: "🎬 Loading 10 Episodes & Challenges..." },
    { p: 80, text: "🏆 Initializing Badges & Rewards..." },
    { p: 100, text: "⚡ Ready Challenger!" }
  ];

  let currentPercent = 0;
  const targetDuration = 1800;
  const intervalTime = 25;
  const step = 100 / (targetDuration / intervalTime);

  const timer = setInterval(() => {
    currentPercent += step + (Math.random() * 2 - 1);
    if (currentPercent >= 100) {
      currentPercent = 100;
      clearInterval(timer);
    }

    const rounded = Math.min(100, Math.floor(currentPercent));
    if (fill) fill.style.width = rounded + "%";
    if (percent) percent.innerText = rounded + "%";

    const currentStage = stages.find(s => rounded <= s.p) || stages[stages.length - 1];
    if (status && status.innerText !== currentStage.text) {
      status.innerText = currentStage.text;
    }

    if (currentPercent >= 100) {
      setTimeout(() => {
        intro.classList.add("fade-out");
        setTimeout(() => {
          intro.remove();
        }, 800);
      }, 350);
    }
  }, intervalTime);
}

// ================= SUBSCRIBE & VERIFY SYSTEM =================
let subscribed = localStorage.getItem("subscribed") === "true";
let verifying = false;
let verifyTimer = null;

const subscribeBtn = document.getElementById("subscribeBtn");
const unlockBtn = document.getElementById("unlockBtn");
const quickVerifyBtn = document.getElementById("quickVerifyBtn");
const subVerifyingBox = document.getElementById("subVerifyingBox");
const subVerifyText = document.getElementById("subVerifyText");
const subVerifyFill = document.getElementById("subVerifyFill");
const gateAlert = document.getElementById("gateAlert");
const step1Indicator = document.getElementById("step1Indicator");
const step2Indicator = document.getElementById("step2Indicator");

function showGateAlert(msg, type) {
  if (!gateAlert) return;
  gateAlert.innerText = msg;
  gateAlert.className = "gate-alert " + (type || "error");
  gateAlert.style.display = "block";
}

function markSubscriptionVerified() {
  if (verifyTimer) clearInterval(verifyTimer);
  subscribed = true;
  verifying = false;
  localStorage.setItem("subscribed", "true");
  playBeastSound("verify");
  launchConfetti();

  if (subscribeBtn) {
    subscribeBtn.classList.add("verified");
    const subText = document.getElementById("subBtnText");
    if (subText) subText.innerText = "✅ Subscription Verified (VIP)";
  }

  if (step1Indicator) {
    step1Indicator.classList.remove("active");
    step1Indicator.classList.add("completed");
    step1Indicator.innerHTML = '<span class="step-num">✓</span><span class="step-text">Subscribed</span>';
  }
  if (step2Indicator) {
    step2Indicator.classList.add("active");
  }

  if (quickVerifyBtn) {
    quickVerifyBtn.style.display = "none";
  }

  if (subVerifyingBox) {
    subVerifyingBox.style.display = "none";
  }

  if (unlockBtn) {
    unlockBtn.disabled = false;
    unlockBtn.classList.add("active");
    unlockBtn.innerHTML = "🔓 Unlock Website Now! ✨";
  }

  const pill = document.querySelector(".gate-status-pill");
  if (pill) {
    pill.classList.add("unlocked-pill");
    pill.innerText = "🔓 Ready to Unlock";
  }

  showGateAlert("🎉 Subscription verified! Click 'Unlock Website Now' to enter!", "success");
}

function startVerification(initialDelay) {
  if (subscribed) return;
  verifying = true;
  if (subVerifyingBox) subVerifyingBox.style.display = "flex";

  const subText = document.getElementById("subBtnText");
  if (subText) subText.innerText = "⏳ Verifying Subscription...";

  let remaining = initialDelay || 7;
  const total = remaining;
  if (subVerifyText) subVerifyText.innerText = "Connecting to YouTube... (" + remaining + "s)";
  if (subVerifyFill) subVerifyFill.style.width = "0%";

  if (verifyTimer) clearInterval(verifyTimer);
  verifyTimer = setInterval(() => {
    remaining--;
    const progress = Math.min(100, Math.floor(((total - remaining) / total) * 100));
    if (subVerifyFill) subVerifyFill.style.width = progress + "%";
    if (subVerifyText) subVerifyText.innerText = "Verifying with YouTube channel... (" + remaining + "s)";

    if (remaining <= 0) {
      clearInterval(verifyTimer);
      markSubscriptionVerified();
    }
  }, 1000);
}

// When returning back to tab after clicking YouTube link
window.addEventListener("focus", () => {
  if (verifying && !subscribed) {
    setTimeout(() => {
      markSubscriptionVerified();
    }, 1000);
  }
});

// ================= 3D FLIP UNLOCK TRANSITION =================
function triggerWebsiteUnlockFlip() {
  playBeastSound("unlock");
  launchConfetti();
  if (typeof launchFireworks === "function") launchFireworks();

  const gate = document.getElementById("gate");
  const site = document.getElementById("site");

  gate.classList.add("gate-flipping-out");
  site.classList.remove("hidden");
  site.classList.add("site-flipping-in");

  localStorage.setItem("unlocked", "true");

  const toast = document.createElement("div");
  toast.className = "unlocked-toast";
  toast.innerHTML = "🎉 <span>Welcome to Beast Games Season 2! All Episodes & Badges Unlocked!</span>";
  document.body.appendChild(toast);
  setTimeout(() => toast.classList.add("show"), 50);
  setTimeout(() => {
    toast.classList.remove("show");
    setTimeout(() => toast.remove(), 600);
  }, 5000);

  setTimeout(() => {
    gate.style.display = "none";
    gate.classList.remove("gate-flipping-out");
    site.classList.remove("site-flipping-in");
    window.scrollTo({ top: 0, behavior: "smooth" });
  }, 1250);
}

if (subscribeBtn) {
  subscribeBtn.addEventListener("click", () => {
    playBeastSound("click");
    startVerification(7);
  });
}

if (quickVerifyBtn) {
  quickVerifyBtn.addEventListener("click", (e) => {
    e.preventDefault();
    playBeastSound("click");
    markSubscriptionVerified();
  });
}

if (unlockBtn) {
  unlockBtn.addEventListener("click", (e) => {
    e.preventDefault();
    playBeastSound("click");
    if (!subscribed) {
      showGateAlert("⚠️ Please subscribe to @TrendzOfShahid first to unlock the website!", "error");
      if (subscribeBtn) {
        subscribeBtn.style.animation = "shakeAlert 0.4s ease";
        setTimeout(() => subscribeBtn.style.animation = "", 400);
      }
      return;
    }
    triggerWebsiteUnlockFlip();
  });
}

function resetGate() {
  localStorage.removeItem("unlocked");
  localStorage.removeItem("subscribed");
  location.reload();
}
window.resetGate = resetGate;

// ================= INITIALIZATION =================
window.addEventListener("DOMContentLoaded", () => {
  runIntroAnimation();

  const isUnlocked = localStorage.getItem("unlocked") === "true";
  const wasSubscribed = localStorage.getItem("subscribed") === "true";

  if (wasSubscribed) {
    markSubscriptionVerified();
  }

  if (isUnlocked) {
    const gate = document.getElementById("gate");
    const site = document.getElementById("site");
    if (gate) gate.style.display = "none";
    if (site) site.classList.remove("hidden");
  }
});'''

assert re.search(old_js_regex, html) is not None, "Could not find old JS block"
html = re.sub(old_js_regex, new_js, html, count=1)

with open('./index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Update successfully written! New file size:', len(html))
