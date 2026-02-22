import json
import random
import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(page_title="Sriti KG Game", page_icon="🌟", layout="centered")


ENGLISH_WORDS = [
    {"word": "cat", "emoji": "🐱", "hint": "A pet that says meow"},
    {"word": "dog", "emoji": "🐶", "hint": "A pet that barks"},
    {"word": "sun", "emoji": "☀️", "hint": "Bright in the sky"},
    {"word": "hat", "emoji": "🎩", "hint": "You wear it on your head"},
    {"word": "car", "emoji": "🚗", "hint": "It has wheels"},
    {"word": "bus", "emoji": "🚌", "hint": "Big school ride"},
    {"word": "cup", "emoji": "☕", "hint": "You drink from it"},
    {"word": "egg", "emoji": "🥚", "hint": "Breakfast food"},
    {"word": "fish", "emoji": "🐟", "hint": "Swims in water"},
    {"word": "book", "emoji": "📘", "hint": "You read it"},
    {"word": "moon", "emoji": "🌙", "hint": "Seen at night"},
    {"word": "star", "emoji": "⭐", "hint": "Twinkles in the sky"},
    {"word": "duck", "emoji": "🦆", "hint": "Says quack"},
    {"word": "lion", "emoji": "🦁", "hint": "Big wild cat"},
    {"word": "tree", "emoji": "🌳", "hint": "Grows leaves"},
]


CSS = """
<style>
.stApp {
  background:
    radial-gradient(circle at 10% 10%, rgba(255, 184, 218, 0.35), transparent 30%),
    radial-gradient(circle at 90% 12%, rgba(146, 224, 255, 0.35), transparent 32%),
    radial-gradient(circle at 80% 88%, rgba(255, 231, 167, 0.35), transparent 30%),
    linear-gradient(180deg, #fffaf1, #f4fbff);
}
.block-container {
  padding-top: calc(2.8rem + env(safe-area-inset-top, 0px)) !important;
  padding-bottom: 1.5rem !important;
  max-width: 900px !important;
}
.main-title {
  text-align:center;
  color:#ef5f8d;
  font-size:2.1rem;
  margin-bottom:0.2rem;
  text-shadow: 0 1px 0 #fff;
}
.subtitle {
  text-align:center;
  color:#334a68;
  margin-bottom:1rem;
}
.setup-card {
  background: linear-gradient(180deg, #ffffff, #f8fbff);
  border: 2px solid #e6f0ff;
  border-radius: 16px;
  padding: 12px;
  margin: 0.6rem 0 0.8rem 0;
  box-shadow: 0 8px 16px rgba(24,39,75,0.05);
}
.setup-title {
  text-align:center;
  color:#20304a;
  font-weight:800;
  font-size:1.15rem;
  margin-bottom:0.35rem;
}
.kg-card {
  background: linear-gradient(180deg, #ffffff, #f6fbff);
  border: 2px solid #e8f0ff;
  border-radius: 18px;
  padding: 14px;
  box-shadow: 0 10px 24px rgba(24,39,75,0.08);
  backdrop-filter: blur(2px);
}
.big-question {
  text-align:center;
  font-size:2.35rem;
  font-weight:800;
  color:#20304a;
  margin: 0.4rem 0 0.7rem 0;
  text-shadow: 0 1px 0 #fff;
}
.emoji-box {
  text-align:center;
  font-size:4rem;
  line-height:1;
  margin-top:0.3rem;
}
.word-box {
  text-align:center;
  font-size:1.9rem;
  font-weight:800;
  letter-spacing:0.25rem;
  background:#fff;
  color:#20304a;
  border:2px dashed #cfe5ff;
  border-radius:14px;
  padding:0.5rem;
  margin:0.5rem 0;
  min-height: 64px;
  display:flex;
  align-items:center;
  justify-content:center;
}
.small-note {
  text-align:center;
  color:#4d647f;
  font-size:0.95rem;
}
div[data-testid="stCaptionContainer"] p,
div[data-testid="stMarkdownContainer"] p,
div[data-testid="stMarkdownContainer"] li,
label[data-testid="stWidgetLabel"] p {
  color:#334a68 !important;
}
.chooser-card {
  position: relative;
  overflow: hidden;
  border-radius: 18px;
  padding: 14px 12px;
  min-height: 140px;
  border: 2px solid #e7efff;
  box-shadow: 0 10px 22px rgba(24,39,75,0.08);
  margin-bottom: 0.5rem;
}
.chooser-card.math {
  background: linear-gradient(180deg, #fff7d6, #e9f8ff);
}
.chooser-card.english {
  background: linear-gradient(180deg, #fff0f8, #eef8ff);
}
.chooser-title {
  position: relative;
  z-index: 2;
  text-align: center;
  font-weight: 800;
  font-size: 1.35rem;
  color: #20304a;
  margin-top: 0.1rem;
}
.chooser-sub {
  position: relative;
  z-index: 2;
  text-align: center;
  color: #425c7b;
  font-size: 0.9rem;
}
.chooser-card::after {
  content:"";
  position:absolute;
  width:90px;
  height:90px;
  border-radius:50%;
  right:-12px;
  top:-18px;
  background: rgba(255,255,255,0.35);
  z-index:1;
}
.float-wrap {
  position:absolute;
  inset:0;
  pointer-events:none;
}
.float-chip {
  position:absolute;
  font-weight:800;
  opacity:0.65;
  animation: chooserFloat linear infinite;
}
.math .float-chip { color:#2ea9f5; }
.english .float-chip { color:#ef5f8d; }
@keyframes chooserFloat {
  0% { transform: translateY(18px) rotate(0deg); opacity:0; }
  20% { opacity:0.7; }
  80% { opacity:0.7; }
  100% { transform: translateY(-26px) rotate(8deg); opacity:0; }
}
div[data-baseweb="input"] input {
  background: #ffffff !important;
  color: #20304a !important;
  caret-color: #20304a !important;
  text-transform: uppercase;
  font-weight: 700;
  border-radius: 12px !important;
}
div[data-testid="stMetric"] {
  background: rgba(255,255,255,0.88);
  border: 1px solid #e7efff;
  border-radius: 14px;
  padding: 8px 10px;
  box-shadow: 0 6px 14px rgba(24,39,75,0.05);
}
div[data-testid="stMetricLabel"] {
  color:#5d7491 !important;
}
div[data-testid="stMetricValue"] {
  color:#20304a !important;
}
.stButton > button, .stFormSubmitButton > button {
  border-radius: 12px !important;
  border: 1px solid #d9e9ff !important;
  background: linear-gradient(180deg, #ffffff, #f1f8ff) !important;
  color: #20304a !important;
  font-weight: 700 !important;
  box-shadow: 0 6px 14px rgba(24,39,75,0.06);
}
.stButton > button:hover, .stFormSubmitButton > button:hover {
  border-color: #9ed4ff !important;
  box-shadow: 0 8px 18px rgba(53,183,255,0.15);
}
.stButton > button[kind="primary"], .stFormSubmitButton > button[kind="primary"] {
  background: linear-gradient(180deg, #fff0f8, #eaf7ff) !important;
}
div[data-baseweb="select"] > div {
  background: #ffffff !important;
  border-radius: 12px !important;
  border: 1px solid #d9e9ff !important;
  min-height: 44px;
  box-shadow: 0 4px 10px rgba(24,39,75,0.05);
}
div[data-baseweb="select"] * {
  color:#20304a !important;
}
div[role="listbox"] {
  background:#ffffff !important;
  border:1px solid #d9e9ff !important;
  border-radius:12px !important;
}
div[role="option"] {
  color:#20304a !important;
}
div[role="option"][aria-selected="true"] {
  background:#eef7ff !important;
}
</style>
"""


# ------------------ State helpers ------------------
def init_state():
    defaults = {
        "math_mode": "Mix (+/-)",
        "math_score": 0,
        "math_streak": 0,
        "math_feedback": "Pick or type the answer!",
        "math_feedback_kind": "info",
        "math_question": None,
        "math_input": "",
        "math_input_box": "",
        "math_input_reset_pending": False,
        "english_score": 0,
        "english_streak": 0,
        "english_feedback": "Build the word from the letters!",
        "english_feedback_kind": "info",
        "english_puzzle": None,
        "english_built_ids": [],
        "english_typed": "",
        "english_typed_box": "",
        "english_input_reset_pending": False,
        "last_math_audio_id": "",
        "last_english_audio_id": "",
        "math_feedback_speech": "",
        "math_feedback_speech_id": 0,
        "english_feedback_speech": "",
        "english_feedback_speech_id": 0,
        "selected_game": "home",
        "player_name": "Sriti",
        "player_name_input": "Sriti",
        "math_session_started": False,
        "english_session_started": False,
        "math_start_level": 1,
        "english_start_level": 1,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def render_speech_widget(text: str, widget_id: str, auto_play: bool = False, button_label: str = "🔊 Hear Question"):
    """Tiny browser speech widget for Streamlit Cloud/iPad use."""
    payload = json.dumps(text)
    auto_js = "true" if auto_play else "false"
    html = f"""
    <div style="display:flex;justify-content:center;margin:0.2rem 0 0.5rem 0;">
      <button id="speak-btn" style="
        background:#ffe7fa;border:1px solid #f8bdd8;color:#6d2a4d;
        border-radius:12px;padding:8px 14px;font-weight:700;cursor:pointer;">
        {button_label}
      </button>
    </div>
    <script>
      const text = {payload};
      const autoPlay = {auto_js};
      const widgetId = {json.dumps(widget_id)};
      const storeKey = "sriti_spoken_" + widgetId;

      function speakNow() {{
        try {{
          if (!("speechSynthesis" in window)) return;
          if (window.speechSynthesis.resume) window.speechSynthesis.resume();
          window.speechSynthesis.cancel();
          const u = new SpeechSynthesisUtterance(text);
          const voices = window.speechSynthesis.getVoices ? window.speechSynthesis.getVoices() : [];
          const preferred =
            voices.find(v => v.localService && /samantha|victoria|karen|zira|ava|susan/i.test(v.name)) ||
            voices.find(v => v.localService && /female/i.test(v.name)) ||
            voices.find(v => /samantha|victoria|karen|zira|ava|susan/i.test(v.name)) ||
            voices.find(v => /female/i.test(v.name)) ||
            voices.find(v => /^en/i.test(v.lang)) ||
            null;
          if (preferred) u.voice = preferred;
          u.lang = "en-US";
          u.rate = 0.84;
          u.pitch = 1.48;
          u.volume = 1.0;
          window.speechSynthesis.speak(u);
        }} catch (e) {{
          // no-op
        }}
      }}

      document.getElementById("speak-btn").addEventListener("click", speakNow);

      if (autoPlay) {{
        const already = sessionStorage.getItem(storeKey);
        if (!already) {{
          setTimeout(() => {{
            speakNow();
            sessionStorage.setItem(storeKey, "1");
          }}, 250);
        }}
      }}
    </script>
    """
    components.html(html, height=52)


def render_auto_speech(text: str, widget_id: str):
    """Auto-play speech once for feedback messages (no button UI)."""
    if not text:
        return
    payload = json.dumps(text)
    html = f"""
    <script>
      (function() {{
        const text = {payload};
        const key = "sriti_auto_feedback_" + {json.dumps(widget_id)};
        try {{
          if (!("speechSynthesis" in window)) return;
          if (sessionStorage.getItem(key)) return;
          setTimeout(() => {{
            try {{
              if (window.speechSynthesis.resume) window.speechSynthesis.resume();
              window.speechSynthesis.cancel();
              const u = new SpeechSynthesisUtterance(text);
              const voices = window.speechSynthesis.getVoices ? window.speechSynthesis.getVoices() : [];
              const preferred =
                voices.find(v => v.localService && /samantha|victoria|karen|zira|ava|susan/i.test(v.name)) ||
                voices.find(v => v.localService && /female/i.test(v.name)) ||
                voices.find(v => /samantha|victoria|karen|zira|ava|susan/i.test(v.name)) ||
                voices.find(v => /female/i.test(v.name)) ||
                voices.find(v => /^en/i.test(v.lang)) ||
                null;
              if (preferred) u.voice = preferred;
              u.lang = "en-US";
              u.rate = 0.86;
              u.pitch = 1.4;
              u.volume = 1.0;
              window.speechSynthesis.speak(u);
              sessionStorage.setItem(key, "1");
            }} catch (e) {{}}
          }}, 500);
        }} catch (e) {{}}
      }})();
    </script>
    """
    components.html(html, height=0)


def player_name() -> str:
    name = str(st.session_state.get("player_name", "Sriti")).strip()
    return name or "Sriti"


def commit_player_name():
    raw = str(st.session_state.get("player_name_input", st.session_state.get("player_name", "Sriti")))
    cleaned = raw.strip() or "Sriti"
    st.session_state.player_name = cleaned


def difficulty_max(score: int) -> int:
    lvl = math_level(score)
    return min(10 + (lvl - 1) * 3, 35)


def math_level(score: int) -> int:
    return max(1, (score // 4) + 1)


def english_level(score: int) -> int:
    return max(1, (score // 3) + 1)


def set_math_level(level: int):
    lvl = max(1, int(level))
    st.session_state.math_score = (lvl - 1) * 4
    st.session_state.math_streak = 0
    st.session_state.math_start_level = lvl


def set_english_level(level: int):
    lvl = max(1, int(level))
    st.session_state.english_score = (lvl - 1) * 3
    st.session_state.english_streak = 0
    st.session_state.english_start_level = lvl


def generate_math_options(correct: int) -> list[int]:
    opts = {correct}
    attempts = 0
    while len(opts) < 4 and attempts < 100:
        attempts += 1
        delta = random.randint(1, 4)
        sign = random.choice([-1, 1])
        cand = max(0, correct + sign * delta + random.randint(-1, 1))
        opts.add(cand)
    while len(opts) < 4:
        opts.add(random.randint(0, max(10, correct + 5)))
    out = list(opts)
    random.shuffle(out)
    return out[:4]


def new_math_question():
    max_n = difficulty_max(st.session_state.math_score)
    a = random.randint(0, max_n)
    b = random.randint(0, max_n)
    mode = st.session_state.math_mode

    if mode == "Add (+)":
        op = "+"
    elif mode == "Subtract (-)":
        op = "-"
    else:
        op = random.choice(["+", "-"])

    if op == "-" and b > a:
        a, b = b, a

    answer = a + b if op == "+" else a - b
    st.session_state.math_question = {
        "a": a,
        "b": b,
        "op": op,
        "answer": answer,
        "options": generate_math_options(answer),
        "locked": False,
    }
    st.session_state.math_input = ""
    st.session_state.math_input_reset_pending = True
    st.session_state.math_feedback = "Pick or type the answer!"
    st.session_state.math_feedback_kind = "info"
    st.session_state.math_feedback_speech = ""


def grade_math_answer(value: int | None):
    q = st.session_state.math_question
    if not q or q["locked"]:
        return
    if value is None:
        st.session_state.math_feedback = "Type a number or tap an option first."
        st.session_state.math_feedback_kind = "warning"
        st.session_state.math_feedback_speech = "Type a number or tap an answer first."
        st.session_state.math_feedback_speech_id += 1
        return

    q["locked"] = True
    if value == q["answer"]:
        st.session_state.math_score += 1
        st.session_state.math_streak += 1
        st.session_state.math_feedback = f"Correct! {q['a']} {q['op']} {q['b']} = {q['answer']} 🎉"
        st.session_state.math_feedback_kind = "success"
        st.session_state.math_feedback_speech = f"Great job, {player_name()}! Correct. The answer is {q['answer']}."
        st.session_state.math_feedback_speech_id += 1
        try:
            st.balloons()
        except Exception:
            pass
    else:
        st.session_state.math_streak = 0
        st.session_state.math_feedback = f"Nice try! Correct answer is {q['answer']}"
        st.session_state.math_feedback_kind = "error"
        st.session_state.math_feedback_speech = f"Nice try. The correct answer is {q['answer']}."
        st.session_state.math_feedback_speech_id += 1


def math_retry_current():
    q = st.session_state.math_question
    if not q:
        return
    q["locked"] = False
    st.session_state.math_input = ""
    st.session_state.math_input_reset_pending = True
    st.session_state.math_feedback = "Try again!"
    st.session_state.math_feedback_kind = "info"
    st.session_state.math_feedback_speech = ""


def english_new_puzzle():
    lvl = english_level(st.session_state.english_score)
    if lvl <= 2:
        pool = [w for w in ENGLISH_WORDS if len(w["word"]) == 3]
    elif lvl <= 4:
        pool = [w for w in ENGLISH_WORDS if len(w["word"]) in (3, 4)]
    else:
        pool = ENGLISH_WORDS
    item = random.choice(pool or ENGLISH_WORDS)
    letters = list(item["word"].upper())
    # Add 1-2 extra letters to make it a bit fun, but keep simple.
    alphabet = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    extra_count = 1 if lvl <= 2 else (2 if lvl <= 4 else 3)
    extras = random.sample([c for c in alphabet if c not in letters], k=min(extra_count, len([c for c in alphabet if c not in letters])))
    tiles = letters + extras
    random.shuffle(tiles)

    st.session_state.english_puzzle = {
        "word": item["word"].upper(),
        "emoji": item["emoji"],
        "hint": item["hint"],
        "tiles": [{"id": i, "ch": ch} for i, ch in enumerate(tiles)],
        "locked": False,
    }
    st.session_state.english_built_ids = []
    st.session_state.english_typed = ""
    st.session_state.english_input_reset_pending = True
    st.session_state.english_feedback = "Build the word from the letters!"
    st.session_state.english_feedback_kind = "info"
    st.session_state.english_feedback_speech = ""


def english_built_word() -> str:
    puzzle = st.session_state.english_puzzle
    if not puzzle:
        return ""
    tile_map = {tile["id"]: tile["ch"] for tile in puzzle["tiles"]}
    return "".join(tile_map[t_id] for t_id in st.session_state.english_built_ids if t_id in tile_map)


def english_add_tile(tile_id: int):
    puzzle = st.session_state.english_puzzle
    if not puzzle or puzzle["locked"]:
        return
    if tile_id in st.session_state.english_built_ids:
        return
    st.session_state.english_typed = ""
    st.session_state.english_input_reset_pending = True
    st.session_state.english_built_ids.append(tile_id)


def english_remove_last():
    puzzle = st.session_state.english_puzzle
    if not puzzle or puzzle["locked"]:
        return
    st.session_state.english_typed = ""
    st.session_state.english_input_reset_pending = True
    if st.session_state.english_built_ids:
        st.session_state.english_built_ids.pop()


def english_clear():
    puzzle = st.session_state.english_puzzle
    if not puzzle or puzzle["locked"]:
        return
    st.session_state.english_built_ids = []
    st.session_state.english_typed = ""
    st.session_state.english_input_reset_pending = True


def english_check(typed_value: str | None = None):
    puzzle = st.session_state.english_puzzle
    if not puzzle or puzzle["locked"]:
        return
    built = english_built_word()
    typed = (typed_value or "").strip().upper()
    attempt = typed if typed else built
    if not attempt:
        st.session_state.english_feedback = "Tap letters or type the word first."
        st.session_state.english_feedback_kind = "warning"
        st.session_state.english_feedback_speech = "Tap letters or type the word first."
        st.session_state.english_feedback_speech_id += 1
        return

    if attempt == puzzle["word"]:
        puzzle["locked"] = True
        st.session_state.english_score += 1
        st.session_state.english_streak += 1
        st.session_state.english_feedback = f"Correct! You spelled {puzzle['word']} 🌟"
        st.session_state.english_feedback_kind = "success"
        st.session_state.english_feedback_speech = (
            f"Excellent, {player_name()}! You spelled {puzzle['word'].lower()} correctly."
        )
        st.session_state.english_feedback_speech_id += 1
        try:
            st.balloons()
        except Exception:
            pass
    else:
        st.session_state.english_streak = 0
        st.session_state.english_feedback = "Good try! Keep going."
        st.session_state.english_feedback_kind = "error"
        st.session_state.english_feedback_speech = f"Good try. Check the letters and try again."
        st.session_state.english_feedback_speech_id += 1


def math_enter_action():
    q = st.session_state.math_question
    if not q:
        return
    if q["locked"] and st.session_state.math_feedback_kind == "success":
        new_math_question()
        st.rerun()
    if q["locked"] and st.session_state.math_feedback_kind == "error":
        math_retry_current()
        st.rerun()
    txt = str(st.session_state.get("math_input_box", st.session_state.get("math_input", ""))).strip()
    val = int(txt) if txt.isdigit() else None
    grade_math_answer(val)
    st.rerun()


def english_enter_action():
    puzzle = st.session_state.english_puzzle
    if not puzzle:
        return
    if puzzle["locked"] and st.session_state.english_feedback_kind == "success":
        english_new_puzzle()
        st.rerun()
    if st.session_state.english_feedback_kind == "error":
        english_clear()
        st.session_state.english_feedback = "Try again!"
        st.session_state.english_feedback_kind = "info"
        st.session_state.english_feedback_speech = ""
        st.rerun()
    english_check(st.session_state.get("english_typed", ""))
    st.rerun()


# ------------------ UI ------------------
init_state()
if st.session_state.math_question is None:
    new_math_question()
if st.session_state.english_puzzle is None:
    english_new_puzzle()

st.markdown(CSS, unsafe_allow_html=True)
st.markdown(f'<div class="main-title">🌟 {player_name()} KG Learning Game 🌟</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Choose a game: Math or English</div>', unsafe_allow_html=True)

if st.session_state.selected_game == "home":
    name_col1, name_col2 = st.columns([2, 1])
    with name_col1:
        entered_name = st.text_input(
            "Who is playing?",
            key="player_name_input",
            placeholder="Type name",
            help="We will use this name in the game voice and praise.",
        )
        cleaned_name = entered_name.strip() or "Sriti"
        if cleaned_name != st.session_state.get("player_name", "Sriti"):
            st.session_state.player_name = cleaned_name
    with name_col2:
        st.markdown(
            f'<div class="small-note" style="margin-top:2.2rem;">Playing: <b>{player_name().upper()}</b></div>',
            unsafe_allow_html=True,
        )
    col_math_pick, col_eng_pick = st.columns(2)
    with col_math_pick:
        st.markdown(
            """
            <div class="chooser-card math">
              <div class="float-wrap">
                <span class="float-chip" style="left:8%; top:72%; font-size:18px; animation-duration:6s;">1</span>
                <span class="float-chip" style="left:26%; top:62%; font-size:22px; animation-duration:7s;">+</span>
                <span class="float-chip" style="left:46%; top:78%; font-size:20px; animation-duration:5.8s;">4</span>
                <span class="float-chip" style="left:68%; top:66%; font-size:24px; animation-duration:7.4s;">9</span>
                <span class="float-chip" style="left:82%; top:76%; font-size:18px; animation-duration:6.6s;">-</span>
              </div>
              <div class="chooser-title">➕ Math</div>
              <div class="chooser-sub">Fun numbers & sums</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Play Math", use_container_width=True, key="pick_math"):
            commit_player_name()
            st.session_state.selected_game = "math"
            st.session_state.math_session_started = False
            st.rerun()

    with col_eng_pick:
        st.markdown(
            """
            <div class="chooser-card english">
              <div class="float-wrap">
                <span class="float-chip" style="left:8%; top:70%; font-size:17px; animation-duration:6.1s;">CAT</span>
                <span class="float-chip" style="left:36%; top:62%; font-size:16px; animation-duration:7.2s;">SUN</span>
                <span class="float-chip" style="left:62%; top:78%; font-size:17px; animation-duration:6.4s;">DOG</span>
                <span class="float-chip" style="left:78%; top:64%; font-size:16px; animation-duration:7.6s;">BOOK</span>
              </div>
              <div class="chooser-title">🔤 English</div>
              <div class="chooser-sub">Letters & spelling words</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("Play English", use_container_width=True, key="pick_english"):
            commit_player_name()
            st.session_state.selected_game = "english"
            st.session_state.english_session_started = False
            st.rerun()

game_view = "➕ Math" if st.session_state.selected_game == "math" else ("🔤 English" if st.session_state.selected_game == "english" else "")

if game_view == "➕ Math":
    top_left, top_right = st.columns([1, 2])
    with top_left:
        if st.button("← Back to Home", use_container_width=True, key="back_home_math"):
            st.session_state.selected_game = "home"
            st.session_state.math_session_started = False
            st.rerun()
    if not st.session_state.math_session_started:
        st.markdown(
            '<div class="setup-card"><div class="setup-title">Choose Math Starting Level</div></div>',
            unsafe_allow_html=True,
        )
        setup_col1, setup_col2 = st.columns(2)
        with setup_col1:
            start_lvl = st.selectbox(
                "Start Level",
                list(range(1, 11)),
                index=max(0, int(st.session_state.get("math_start_level", 1)) - 1),
                key="math_start_level_picker",
            )
        with setup_col2:
            start_mode = st.selectbox(
                "Math Type",
                ["Add (+)", "Subtract (-)", "Mix (+/-)"],
                index=["Add (+)", "Subtract (-)", "Mix (+/-)"].index(st.session_state.math_mode),
                key="math_mode_setup_picker",
            )
        st.caption("Level keeps increasing as score grows.")
        if st.button("Start Math Game", use_container_width=True, key="start_math_game"):
            st.session_state.math_mode = start_mode
            set_math_level(int(start_lvl))
            new_math_question()
            st.session_state.math_session_started = True
            st.rerun()
        st.stop()

    q = st.session_state.math_question
    st.markdown('<div class="kg-card">', unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    c1.metric("Score", st.session_state.math_score)
    c2.metric("Streak", st.session_state.math_streak)
    c3.metric("Level", math_level(st.session_state.math_score))

    st.markdown(
        f'<div class="big-question">{q["a"]} {q["op"]} {q["b"]} = ?</div>',
        unsafe_allow_html=True,
    )
    st.caption(
        f"Mode: {st.session_state.math_mode} • Level: {math_level(st.session_state.math_score)} (keeps increasing)"
    )
    math_prompt = f"What is {q['a']} {'plus' if q['op'] == '+' else 'minus'} {q['b']}?"
    math_audio_id = f"{q['a']}_{q['op']}_{q['b']}"
    auto_math = st.session_state.last_math_audio_id != math_audio_id
    render_speech_widget(math_prompt, f"math_{math_audio_id}", auto_play=auto_math, button_label="🔊 Hear Question")
    st.session_state.last_math_audio_id = math_audio_id

    st.write("Tap an option:")
    opt_cols = st.columns(2)
    for i, opt in enumerate(q["options"]):
        with opt_cols[i % 2]:
            disabled = q["locked"]
            if st.button(str(opt), key=f"math_opt_{i}_{q['a']}_{q['b']}_{q['op']}", use_container_width=True, disabled=disabled):
                grade_math_answer(opt)
                q = st.session_state.math_question

    st.write("Or type the answer:")
    if st.session_state.get("math_input_reset_pending", False) or "math_input_box" not in st.session_state:
        st.session_state.math_input_box = st.session_state.math_input
        st.session_state.math_input_reset_pending = False

    with st.form("math_type_form", clear_on_submit=False):
        in_col, sub_col = st.columns([3, 1])
        with in_col:
            raw = st.text_input(
                "Type answer",
                key="math_input_box",
                label_visibility="collapsed",
                placeholder="Type answer",
                disabled=q["locked"] and st.session_state.math_feedback_kind != "success",
            )
            st.session_state.math_input = raw
        with sub_col:
            if q["locked"] and st.session_state.math_feedback_kind == "success":
                enter_label = "NEXT ↵"
            elif q["locked"] and st.session_state.math_feedback_kind == "error":
                enter_label = "RETRY ↵"
            else:
                enter_label = "ENTER ↵"
            pressed_enter = st.form_submit_button(enter_label, use_container_width=True)
    if pressed_enter:
        math_enter_action()

    if st.session_state.math_feedback_kind == "success":
        st.success(st.session_state.math_feedback)
    elif st.session_state.math_feedback_kind == "error":
        st.error(st.session_state.math_feedback)
    elif st.session_state.math_feedback_kind == "warning":
        st.warning(st.session_state.math_feedback)
    else:
        st.info(st.session_state.math_feedback)
    if st.session_state.math_feedback_speech:
        render_auto_speech(
            st.session_state.math_feedback_speech,
            f"math_feedback_{st.session_state.math_feedback_speech_id}",
        )
        render_speech_widget(
            st.session_state.math_feedback_speech,
            f"math_feedback_replay_{st.session_state.math_feedback_speech_id}",
            auto_play=False,
            button_label="🔊 Hear Result",
        )

    st.markdown('</div>', unsafe_allow_html=True)

elif game_view == "🔤 English":
    top_left, top_right = st.columns([1, 2])
    with top_left:
        if st.button("← Back to Home", use_container_width=True, key="back_home_english"):
            st.session_state.selected_game = "home"
            st.session_state.english_session_started = False
            st.rerun()
    if not st.session_state.english_session_started:
        st.markdown(
            '<div class="setup-card"><div class="setup-title">Choose English Starting Level</div></div>',
            unsafe_allow_html=True,
        )
        start_lvl = st.selectbox(
            "Start Level",
            list(range(1, 11)),
            index=max(0, int(st.session_state.get("english_start_level", 1)) - 1),
            key="english_start_level_picker",
        )
        st.caption("Level keeps increasing as words get harder.")
        if st.button("Start English Game", use_container_width=True, key="start_english_game"):
            set_english_level(int(start_lvl))
            english_new_puzzle()
            st.session_state.english_session_started = True
            st.rerun()
        st.stop()

    puzzle = st.session_state.english_puzzle
    built = english_built_word()
    used_ids = set(st.session_state.english_built_ids)

    st.markdown('<div class="kg-card">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Score", st.session_state.english_score)
    c2.metric("Streak", st.session_state.english_streak)
    c3.metric("Level", english_level(st.session_state.english_score))

    st.markdown('<div class="emoji-box">{}</div>'.format(puzzle["emoji"]), unsafe_allow_html=True)
    st.markdown('<div class="small-note">Hint: {}</div>'.format(puzzle["hint"]), unsafe_allow_html=True)
    st.caption(
        f"English level {english_level(st.session_state.english_score)} • Word size: {len(puzzle['word'])} letters"
    )
    english_prompt = f"Spell {puzzle['word'].lower()}. Look at the picture. Hint: {puzzle['hint']}."
    english_audio_id = puzzle["word"]
    auto_english = st.session_state.last_english_audio_id != english_audio_id
    render_speech_widget(english_prompt, f"english_{english_audio_id}", auto_play=auto_english, button_label="🔊 Hear Word")
    st.session_state.last_english_audio_id = english_audio_id

    if st.session_state.get("english_input_reset_pending", False) or "english_typed_box" not in st.session_state:
        st.session_state.english_typed_box = st.session_state.english_typed
        st.session_state.english_input_reset_pending = False

    with st.form("english_type_form", clear_on_submit=False):
        typed_col, enter_col = st.columns([2, 1])
        with typed_col:
            typed_val = st.text_input(
                "Type the word",
                key="english_typed_box",
                placeholder="Type word (CAPITAL letters)",
                disabled=puzzle["locked"] and st.session_state.english_feedback_kind != "success",
            )
        with enter_col:
            if puzzle["locked"] and st.session_state.english_feedback_kind == "success":
                eng_enter_label = "NEXT ↵"
            elif st.session_state.english_feedback_kind == "error":
                eng_enter_label = "RETRY ↵"
            else:
                eng_enter_label = "ENTER ↵"
            pressed_english_enter = st.form_submit_button(eng_enter_label, use_container_width=True)

    typed_val = "".join(ch for ch in str(typed_val).upper() if ch.isalpha())
    st.session_state.english_typed = typed_val
    if pressed_english_enter:
        english_enter_action()

    slot_count = len(puzzle["word"])
    display_source = (typed_val if typed_val else built).upper()
    visible_word = display_source + ("_" * max(0, slot_count - len(display_source)))
    spaced = " ".join(list(visible_word[:slot_count]))
    st.markdown(f'<div class="word-box">{spaced}</div>', unsafe_allow_html=True)
    st.markdown('<div class="small-note">Tap letters below or type the word</div>', unsafe_allow_html=True)

    if st.session_state.english_feedback_kind == "success":
        st.success(st.session_state.english_feedback)
    elif st.session_state.english_feedback_kind == "error":
        st.error(st.session_state.english_feedback)
    elif st.session_state.english_feedback_kind == "warning":
        st.warning(st.session_state.english_feedback)
    else:
        st.info(st.session_state.english_feedback)
    if st.session_state.english_feedback_speech:
        render_auto_speech(
            st.session_state.english_feedback_speech,
            f"english_feedback_{st.session_state.english_feedback_speech_id}",
        )
        render_speech_widget(
            st.session_state.english_feedback_speech,
            f"english_feedback_replay_{st.session_state.english_feedback_speech_id}",
            auto_play=False,
            button_label="🔊 Hear Result",
        )
    if puzzle["locked"]:
        st.caption("Correct! Press NEXT.")

    tile_cols = st.columns(min(6, len(puzzle["tiles"])))
    for i, tile in enumerate(puzzle["tiles"]):
        disabled = puzzle["locked"] or (tile["id"] in used_ids)
        with tile_cols[i % len(tile_cols)]:
            if st.button(
                tile["ch"],
                key=f"eng_tile_{tile['id']}_{puzzle['word']}",
                use_container_width=True,
                disabled=disabled,
            ):
                english_add_tile(tile["id"])
                st.rerun()

    a1, a2 = st.columns(2)
    with a1:
        if st.button("Back", use_container_width=True, disabled=puzzle["locked"]):
            english_remove_last()
            st.rerun()
    with a2:
        if st.button("Clear", use_container_width=True, disabled=puzzle["locked"]):
            english_clear()
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")
st.caption("For iPad: open this app in Safari/Chrome. English uses tap-to-build letters (easy for touch screens).")

with st.expander("Show Test Checklist (for parent)", expanded=False):
    st.markdown(
        "\n".join(
            [
                "- Home opens first (no audio before choosing a game)",
                "- Enter player name and check voice uses the same name",
                "- Math: type answer -> Enter checks",
                "- Math: after correct answer, Enter again -> next question",
                "- English: type word -> Enter checks",
                "- English: after correct word, Enter again -> next word",
                "- Back to Home works in both games",
                "- Voice replay button works on Math and English",
                "- Test on iPad/phone keyboard (Enter/Go/Done)",
            ]
        )
    )
