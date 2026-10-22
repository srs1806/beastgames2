import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("Original index.html length:", len(html))

# =========================================================================
# 1. FIX beastClientId ReferenceError in submitRealRating
# =========================================================================
old_rating_start = '// ================= REAL 10-STAR COMMUNITY RATING ENGINE ================='
new_client_id_decl = """// ================= REAL 10-STAR COMMUNITY RATING ENGINE =================
function getBeastClientId() {
  let id = localStorage.getItem("beast_client_id");
  if (!id) {
    id = "client_" + Date.now() + "_" + Math.random().toString(36).substring(2, 9);
    localStorage.setItem("beast_client_id", id);
  }
  return id;
}
const beastClientId = getBeastClientId();
"""

if old_rating_start in html and 'const beastClientId =' not in html:
    html = html.replace(old_rating_start, new_client_id_decl, 1)
    print("1. Added getBeastClientId() and const beastClientId definition.")
else:
    print("1. beastClientId check passed or already defined.")

# =========================================================================
# 2. FIX MOBILE LOGO: REMOVE .theme-switcher-wrapper .mode-logo:last-of-type { display: none !important; }
# =========================================================================
old_hide_last_logo = """  .theme-switcher-wrapper .mode-logo:last-of-type {
    display: none !important;
  }"""

if old_hide_last_logo in html:
    html = html.replace(old_hide_last_logo, "  /* Removed display:none on logo so it is visible in mobile */")
    print("2. Removed .theme-switcher-wrapper .mode-logo:last-of-type { display: none !important; }.")
else:
    # regex fallback
    html = re.sub(
        r'\.theme-switcher-wrapper\s+\.mode-logo:last-of-type\s*\{[^}]*display:\s*none\s*!important;[^}]*\}',
        '/* Removed display:none on logo */',
        html
    )
    print("2. Applied regex to remove display:none on logo.")

# Also remove any standalone .mode-logo:last-of-type { display: none !important; }
html = re.sub(
    r'\.mode-logo:last-of-type\s*\{[^}]*display:\s*none\s*!important;[^}]*\}',
    '/* Removed display:none on logo */',
    html
)

# =========================================================================
# 3. ENSURE MOBILE RESPONSIVENESS FOR HEADER (LOGO ON LEFT, PROFILE ON RIGHT, MODES BELOW)
# =========================================================================
mobile_header_css = """
/* ================= ENHANCED MOBILE & DESKTOP HEADER BAR ================= */
.theme-switcher-wrapper {
  width: 95% !important;
  max-width: 1100px !important;
  margin: 10px auto 26px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: space-between !important;
  gap: 16px !important;
  box-sizing: border-box !important;
}

.header-brand-left {
  display: flex !important;
  align-items: center !important;
  gap: 12px !important;
  flex-shrink: 0 !important;
  text-decoration: none !important;
}

.mode-logo {
  width: 52px !important;
  height: 52px !important;
  border-radius: 50% !important;
  object-fit: cover !important;
  border: 2px solid var(--accent, #38bdf8) !important;
  box-shadow: 0 0 16px rgba(56, 189, 248, 0.35) !important;
  display: block !important;
  visibility: visible !important;
  opacity: 1 !important;
  flex-shrink: 0 !important;
}

.header-brand-name {
  font-size: 1.1rem !important;
  font-weight: 900 !important;
  letter-spacing: 0.04em !important;
  color: var(--text) !important;
  white-space: nowrap !important;
  display: inline-block !important;
}

.theme-switcher {
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 8px !important;
  flex-wrap: nowrap !important;
}

.header-profile-btn {
  display: inline-flex !important;
  align-items: center !important;
  gap: 8px !important;
  background: var(--card) !important;
  border: 1px solid var(--card-border) !important;
  color: var(--text) !important;
  padding: 8px 16px !important;
  border-radius: 999px !important;
  cursor: pointer !important;
  font-family: inherit !important;
  font-size: 0.84rem !important;
  font-weight: 700 !important;
  flex-shrink: 0 !important;
  box-shadow: var(--card-shadow) !important;
  transition: all 0.25s ease !important;
}

.header-profile-btn:hover {
  border-color: #38bdf8 !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 4px 18px rgba(56, 189, 248, 0.3) !important;
}

/* MOBILE AUDIT: SCREENS UP TO 768px */
@media (max-width: 768px) {
  .theme-switcher-wrapper {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: wrap !important;
    justify-content: space-between !important;
    align-items: center !important;
    gap: 12px 6px !important;
    padding: 0 8px !important;
    margin: 8px auto 20px !important;
  }

  .header-brand-left {
    order: 1 !important;
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
  }

  .mode-logo {
    width: 44px !important;
    height: 44px !important;
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
  }

  .header-brand-name {
    font-size: 0.96rem !important;
    font-weight: 800 !important;
    display: inline-block !important;
  }

  .header-profile-btn {
    order: 2 !important;
    padding: 7px 12px !important;
    font-size: 0.78rem !important;
    max-width: 48% !important;
  }

  .profile-name-text {
    max-width: 76px !important;
  }

  .theme-switcher {
    order: 3 !important;
    width: 100% !important;
    display: flex !important;
    justify-content: center !important;
    gap: 6px !important;
    flex-wrap: wrap !important;
    margin-top: 4px !important;
  }

  .theme-option {
    padding: 8px 10px !important;
    font-size: 0.74rem !important;
    border-radius: 12px !important;
    flex: 1 1 calc(20% - 6px) !important;
    min-width: 54px !important;
    text-align: center !important;
  }
}

@media (max-width: 480px) {
  .mode-logo {
    width: 40px !important;
    height: 40px !important;
  }
  .header-brand-name {
    font-size: 0.88rem !important;
  }
  .header-profile-btn {
    padding: 6px 10px !important;
    font-size: 0.74rem !important;
  }
  .profile-name-text {
    max-width: 60px !important;
  }
  .theme-option {
    padding: 6px 6px !important;
    font-size: 0.7rem !important;
    min-width: 48px !important;
  }
}
"""

if '</style>' in html:
    html = html.replace('</style>', mobile_header_css + '\n</style>', 1)
    print("3. Injected enhanced mobile & desktop responsive header CSS.")

# =========================================================================
# 4. FIX LOCK GATE DISPLAY & FLIP OPENING ANIMATION FOR REGULAR USERS
# =========================================================================
# Ensure regular users always see the lock gate with subscribe button and experience the flip animation
old_init_site_func = """function initSiteAfterEnrollment() {
  // Sync saved theme mode immediately on DOM ready
  const currentSavedTheme = localStorage.getItem("beast_theme_mode") || localStorage.getItem("theme") || "dark";
  setTheme(currentSavedTheme, true);
  if (typeof updateAllCardProgress === "function") updateAllCardProgress();

  const gate = document.getElementById("gate");
  const site = document.getElementById("site");

  // Every 3 visits tracking logic
  const VISIT_COUNT_KEY = "beast_games_visit_count";
  const SESSION_UNLOCKED_KEY = "beast_games_unlocked_session";

  // Check if session is already unlocked in this browser session
  const sessionUnlocked = sessionStorage.getItem(SESSION_UNLOCKED_KEY) === "true";

  // Only increment visit count once per browser session/tab
  if (!sessionStorage.getItem("beast_games_session_counted")) {
    sessionStorage.setItem("beast_games_session_counted", "true");
    let currentVisits = parseInt(localStorage.getItem(VISIT_COUNT_KEY) || "0", 10) + 1;
    localStorage.setItem(VISIT_COUNT_KEY, currentVisits.toString());
  }

  const totalVisits = parseInt(localStorage.getItem(VISIT_COUNT_KEY) || "1", 10);
  // Appears every 3 visits: visit 1, visit 4, visit 7, ...
  const shouldShowGateThisVisit = ((totalVisits - 1) % 3 === 0);

  const intervalBadge = document.getElementById("gateIntervalBadge");
  if (intervalBadge) {
    intervalBadge.innerText = `🛡️ Community Access Gate • Checkpoint (Visit #${totalVisits} • Appears every 3 visits)`;
  }

  if (sessionUnlocked || !shouldShowGateThisVisit) {
    // Unlocked visit - directly show site without lock gate
    isSubscribedVerified = true;
    sessionStorage.setItem(SESSION_UNLOCKED_KEY, "true");
    if (gate) {
      gate.classList.add("gate-hidden");
      gate.style.setProperty("display", "none", "important");
    }
    if (site) {
      site.classList.remove("hidden");
      site.classList.add("site-active");
      site.style.setProperty("display", "block", "important");
    }
    document.body.style.overflow = "auto";
    document.documentElement.style.overflow = "auto";
  } else {
    // Checkpoint visit - show subscribe gate
    if (gate) {
      gate.classList.remove("gate-hidden");
      gate.style.setProperty("display", "flex", "important");
    }
    if (site) {
      site.classList.add("hidden");
      site.classList.remove("site-active");
      site.style.setProperty("display", "none", "important");
    }
    if (typeof runIntroAnimation === "function") {
      runIntroAnimation(() => {
        runStartupSubscriptionVerification();
      });
    } else {
      runStartupSubscriptionVerification();
    }
  }

  if (typeof initChatLiveSync === "function") {
    initChatLiveSync();
  }
}"""

new_init_site_func = """function initSiteAfterEnrollment() {
  // Sync saved theme mode immediately on DOM ready
  const currentSavedTheme = localStorage.getItem("beast_theme_mode") || localStorage.getItem("theme") || "dark";
  setTheme(currentSavedTheme, true);
  if (typeof updateAllCardProgress === "function") updateAllCardProgress();

  const gate = document.getElementById("gate");
  const site = document.getElementById("site");
  const isOwner = localStorage.getItem("beast_is_owner") === "true";

  // Check if session is already unlocked in this browser session
  const sessionUnlocked = sessionStorage.getItem("beast_games_unlocked_session") === "true";

  if (isOwner || sessionUnlocked) {
    // Directly show site for verified owner or already unlocked session
    isSubscribedVerified = true;
    if (gate) {
      gate.classList.add("gate-hidden");
      gate.style.setProperty("display", "none", "important");
    }
    if (site) {
      site.classList.remove("hidden");
      site.classList.add("site-active");
      site.style.setProperty("display", "block", "important");
    }
    document.body.style.overflow = "auto";
    document.documentElement.style.overflow = "auto";
  } else {
    // Regular visitor: showcase the Subscribe Lock Gate with Subscribe button!
    isSubscribedVerified = false;
    hasOpenedYouTubeChannel = false;
    unlockTriggered = false;
    if (gate) {
      gate.classList.remove("gate-hidden");
      gate.classList.remove("gate-flipping-out");
      gate.style.setProperty("display", "flex", "important");
    }
    if (site) {
      site.classList.add("hidden");
      site.classList.remove("site-active");
      site.classList.remove("site-flipping-in");
      site.style.setProperty("display", "none", "important");
    }
    document.body.style.overflow = "hidden";
    document.documentElement.style.overflow = "hidden";

    // Reset button to initial state
    const subBtn = document.getElementById("subscribeBtn");
    const subText = document.getElementById("subBtnText");
    const subIcon = document.getElementById("subBtnIcon");
    const subBox = document.getElementById("subVerifyingBox");
    if (subText) subText.innerText = "🔴 Subscribe on YouTube to Unlock";
    if (subIcon) subIcon.innerText = "🔥";
    if (subBtn) {
      subBtn.className = "gate-btn subscribe-btn fire-wave-btn";
      subBtn.style.pointerEvents = "auto";
      subBtn.style.background = "";
    }
    if (subBox) subBox.style.display = "none";

    runStartupSubscriptionVerification();
  }

  if (typeof initChatLiveSync === "function") {
    initChatLiveSync();
  }
}"""

if old_init_site_func in html:
    html = html.replace(old_init_site_func, new_init_site_func, 1)
    print("4. Replaced initSiteAfterEnrollment to properly show Lock Gate and enable flip transition.")
else:
    print("4. Warning: old_init_site_func not matched exactly, applying regex replace.")
    html = re.sub(
        r'function initSiteAfterEnrollment\(\)\s*\{[\s\S]*?if\s*\(typeof initChatLiveSync === "function"\)\s*\{\s*initChatLiveSync\(\);\s*\}\s*\}',
        new_init_site_func,
        html,
        count=1
    )

# =========================================================================
# 5. SIMPLIFY CHAT & ADD USER AVATAR PICKER
# =========================================================================
# Add quick avatar selector in chat composer
chat_avatar_bar = """
        <!-- User Chat Avatar Selector -->
        <div class="chat-avatar-picker-bar">
          <span class="chat-avatar-label">Your Avatar:</span>
          <div class="chat-avatar-options" id="chatAvatarOptions">
            <button type="button" class="chat-avatar-opt active" onclick="selectChatAvatar('👤')">👤</button>
            <button type="button" class="chat-avatar-opt" onclick="selectChatAvatar('🦁')">🦁</button>
            <button type="button" class="chat-avatar-opt" onclick="selectChatAvatar('⚡')">⚡</button>
            <button type="button" class="chat-avatar-opt" onclick="selectChatAvatar('🔥')">🔥</button>
            <button type="button" class="chat-avatar-opt" onclick="selectChatAvatar('🎮')">🎮</button>
            <button type="button" class="chat-avatar-opt" onclick="selectChatAvatar('🚀')">🚀</button>
            <button type="button" class="chat-avatar-opt" onclick="selectChatAvatar('🦊')">🦊</button>
            <button type="button" class="chat-avatar-opt" onclick="selectChatAvatar('🐯')">🐯</button>
          </div>
        </div>
"""

pos_chat_emojis = html.find('<div class="chat-quick-emojis">')
if pos_chat_emojis != -1 and 'chat-avatar-picker-bar' not in html:
    html = html[:pos_chat_emojis] + chat_avatar_bar + '\n    ' + html[pos_chat_emojis:]
    print("5. Added chat avatar picker bar.")

# Chat avatar CSS
chat_avatar_css = """
/* ================= CHAT AVATAR PICKER & SIMPLIFIED STYLING ================= */
.chat-avatar-picker-bar {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 8px 16px;
  background: rgba(255, 255, 255, 0.02);
  border-bottom: 1px solid var(--card-border);
  overflow-x: auto;
}

.chat-avatar-label {
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--muted);
  white-space: nowrap;
}

.chat-avatar-options {
  display: flex;
  align-items: center;
  gap: 6px;
}

.chat-avatar-opt {
  background: var(--card);
  border: 1px solid var(--card-border);
  border-radius: 50%;
  width: 32px;
  height: 32px;
  font-size: 1.1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s ease;
  padding: 0;
}

.chat-avatar-opt:hover {
  transform: scale(1.15);
  border-color: #38bdf8;
}

.chat-avatar-opt.active {
  border-color: #38bdf8;
  background: rgba(56, 189, 248, 0.2);
  box-shadow: 0 0 10px rgba(56, 189, 248, 0.4);
}

.chat-msg-avatar {
  width: 38px !important;
  height: 38px !important;
  border-radius: 50% !important;
  background: rgba(56, 189, 248, 0.12) !important;
  border: 1px solid rgba(56, 189, 248, 0.3) !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  font-size: 1.25rem !important;
  flex-shrink: 0 !important;
}

.chat-msg-item.is-creator .chat-msg-avatar {
  background: rgba(250, 204, 21, 0.15) !important;
  border-color: #facc15 !important;
  box-shadow: 0 0 12px rgba(250, 204, 21, 0.35) !important;
}
"""

if '</style>' in html:
    html = html.replace('</style>', chat_avatar_css + '\n</style>', 1)
    print("5. Injected chat avatar and simplified styling CSS.")

# JS for selectChatAvatar
avatar_js = """
let selectedChatAvatar = localStorage.getItem("beast_chat_user_avatar") || "👤";

function selectChatAvatar(emoji) {
  playBeastSound("click");
  selectedChatAvatar = emoji;
  localStorage.setItem("beast_chat_user_avatar", emoji);
  document.querySelectorAll(".chat-avatar-opt").forEach(btn => {
    btn.classList.toggle("active", btn.innerText === emoji);
  });
}
window.selectChatAvatar = selectChatAvatar;
"""

pos_chat_js = html.find('// =====================================================\n// 💬 DEDICATED LIVE CHAT ENGINE')
if pos_chat_js != -1 and 'selectChatAvatar' not in html:
    html = html[:pos_chat_js] + avatar_js + '\n' + html[pos_chat_js:]
    print("5. Injected selectChatAvatar JS.")

# In handleChatSubmit, use selectedChatAvatar:
html = html.replace(
    'avatar: ownerToken ? "👑" : "👤",',
    'avatar: ownerToken ? "👑" : (selectedChatAvatar || "👤"),'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Finished applying all fixes. New index.html length:", len(html))
