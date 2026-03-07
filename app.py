import streamlit as st
from src.core.planer import TravelPlanner
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Voyager AI",
    page_icon="🌍",
    layout="wide",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,600;0,700;1,300;1,600&family=Outfit:wght@300;400;500;600&display=swap');

:root {
    --cream:  #faf7f2;
    --sand:   #f5f0e8;
    --brown:  #3d2b1f;
    --terra:  #c4622d;
    --sage:   #7a9e7e;
    --muted:  #8c7b70;
    --border: #e0d5c8;
}

*, *::before, *::after { box-sizing: border-box; }
html, body, [class*="css"], .stApp {
    font-family: 'Outfit', sans-serif !important;
    background: var(--cream) !important;
    color: var(--brown) !important;
}
#MainMenu, footer, header, .stDeployButton { visibility: hidden !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── LEFT HERO PANEL ── */
.left-panel {
    background: var(--brown);
    min-height: 100vh;
    padding: 5rem 4rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
    position: relative;
    overflow: hidden;
}
.left-panel::before {
    content: '';
    position: absolute; inset: 0;
    background:
        radial-gradient(circle at 15% 85%, rgba(196,98,45,0.3) 0%, transparent 45%),
        radial-gradient(circle at 85% 15%, rgba(122,158,126,0.12) 0%, transparent 45%);
    pointer-events: none;
}
.dot-grid {
    position: absolute; inset: 0;
    background-image: radial-gradient(rgba(255,255,255,0.05) 1px, transparent 1px);
    background-size: 30px 30px;
    pointer-events: none;
}
.live-tag {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    background: rgba(196,98,45,0.18);
    border: 1px solid rgba(196,98,45,0.35);
    color: #e8a87c;
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    padding: 0.4rem 1rem;
    border-radius: 999px;
    width: fit-content;
    margin-bottom: 2.2rem;
    position: relative; z-index: 2;
}
.live-dot {
    width: 6px; height: 6px;
    background: #e8a87c;
    border-radius: 50%;
    animation: pulse 2s infinite;
}
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.2} }

.big-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(2.8rem, 4.5vw, 5rem);
    font-weight: 300;
    line-height: 1.08;
    color: #faf7f2;
    position: relative; z-index: 2;
    margin-bottom: 1.5rem;
}
.big-title em { color: #e8a87c; font-style: italic; }

.panel-desc {
    color: rgba(250,247,242,0.48);
    font-size: 0.92rem;
    font-weight: 300;
    line-height: 1.85;
    max-width: 360px;
    position: relative; z-index: 2;
    margin-bottom: 3.5rem;
}

.stats-group {
    display: flex;
    gap: 2.5rem;
    position: relative; z-index: 2;
}
.s-item { display: flex; flex-direction: column; gap: 0.25rem; }
.s-num {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.1rem;
    font-weight: 600;
    color: #faf7f2;
    line-height: 1;
}
.s-label {
    font-size: 0.65rem;
    color: rgba(250,247,242,0.38);
    text-transform: uppercase;
    letter-spacing: 0.14em;
}
.s-sep {
    width: 1px;
    height: 38px;
    background: rgba(255,255,255,0.1);
    align-self: center;
}

/* ── RIGHT FORM PANEL ── */
.right-panel {
    background: var(--cream);
    min-height: 100vh;
    padding: 5rem 3.5rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.form-eyebrow {
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--terra);
    margin-bottom: 0.8rem;
}
.form-title {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.2rem;
    font-weight: 600;
    color: var(--brown);
    line-height: 1.15;
    margin-bottom: 0.6rem;
}
.form-hint-text {
    font-size: 0.83rem;
    color: var(--muted);
    line-height: 1.75;
    margin-bottom: 2.2rem;
}
.field-label {
    font-size: 0.68rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--brown);
    margin-bottom: 0.45rem;
    display: block;
}
.field-hint {
    font-size: 0.72rem;
    color: var(--muted);
    margin-top: 0.3rem;
    margin-bottom: 1.2rem;
}

/* ── Inputs ── */
.stTextInput > div > div > input {
    background: white !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--brown) !important;
    padding: 0.82rem 1.1rem !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.9rem !important;
    transition: border-color .2s, box-shadow .2s !important;
}
.stTextInput > div > div > input:focus {
    border-color: var(--terra) !important;
    box-shadow: 0 0 0 3px rgba(196,98,45,0.1) !important;
}
.stTextInput > div > div > input::placeholder { color: #c9b9ae !important; }
.stTextInput label { display: none !important; }

/* ── Button ── */
.stFormSubmitButton > button {
    width: 100% !important;
    background: var(--brown) !important;
    color: var(--cream) !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.9rem 2rem !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.9rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.05em !important;
    transition: all .25s ease !important;
    margin-top: 1.2rem !important;
    cursor: pointer !important;
}
.stFormSubmitButton > button:hover {
    background: var(--terra) !important;
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 24px rgba(196,98,45,0.28) !important;
}

/* ── Chips ── */
.trust-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-top: 1.8rem;
}
.chip {
    font-size: 0.7rem;
    color: var(--muted);
    background: white;
    border: 1px solid var(--border);
    padding: 0.32rem 0.75rem;
    border-radius: 999px;
}

/* ── Result ── */
.result-section {
    padding: 3.5rem 3.5rem 2rem;
}
.result-top {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding-bottom: 1.2rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 2rem;
}
.r-icon {
    width: 48px; height: 48px;
    background: linear-gradient(135deg, var(--terra) 0%, #d4834d 100%);
    border-radius: 13px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.4rem; flex-shrink: 0;
}
.r-city {
    font-family: 'Cormorant Garamond', serif;
    font-size: 1.7rem;
    font-weight: 600;
    color: var(--brown);
    line-height: 1;
}
.r-interests {
    font-size: 0.75rem;
    color: var(--muted);
    margin-top: 0.2rem;
}
.itinerary-box {
    background: white;
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 2.2rem;
    line-height: 1.95;
    font-size: 0.93rem;
    color: #4a3728;
}

/* ── Download ── */
.stDownloadButton > button {
    background: white !important;
    border: 1.5px solid var(--border) !important;
    border-radius: 10px !important;
    color: var(--brown) !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
    padding: 0.65rem 1.4rem !important;
    margin-top: 1.2rem !important;
    transition: all .2s !important;
}
.stDownloadButton > button:hover {
    border-color: var(--terra) !important;
    color: var(--terra) !important;
}

.stSpinner > div { border-top-color: var(--terra) !important; }
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 3px; }
</style>
""", unsafe_allow_html=True)

# ─── Two-Column Layout ─────────────────────────────────────────────────────────
col_left, col_right = st.columns([55, 45], gap="small")

with col_left:
    st.markdown("""
    <div class="left-panel">
        <div class="dot-grid"></div>
        <div class="live-tag"><div class="live-dot"></div>AI Travel Assistant</div>
        <div class="big-title">
            Plan your<br>next trip with<br><em>intelligence.</em>
        </div>
        <p class="panel-desc">
            A smarter way to explore the world — 
            tell us your city and passions, and we'll 
            design a perfect day just for you.
        </p>
        <div class="stats-group">
            <div class="s-item">
                <div class="s-num">10K+</div>
                <div class="s-label">Cities</div>
            </div>
            <div class="s-sep"></div>
            <div class="s-item">
                <div class="s-num">&lt;5s</div>
                <div class="s-label">Generation</div>
            </div>
            <div class="s-sep"></div>
            <div class="s-item">
                <div class="s-num">LLaMA</div>
                <div class="s-label">3.3 · 70B</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    st.markdown("""
    <div style="padding: 4.5rem 3rem 2rem;">
        <div class="form-eyebrow">Start planning</div>
        <div class="form-title">Where are you<br>headed next?</div>
        <p class="form-hint-text">Fill in your destination and interests — your personalized itinerary will be ready in seconds.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("planner_form"):
        st.markdown('<span class="field-label">🏙️ &nbsp;Destination</span>', unsafe_allow_html=True)
        city = st.text_input("city", placeholder="Paris, Tokyo, Lahore, Dubai…", label_visibility="collapsed")

        st.markdown('<span class="field-label" style="display:block;margin-top:.8rem;">🎯 &nbsp;Your Interests</span>', unsafe_allow_html=True)
        interests = st.text_input("interests", placeholder="Food, History, Art, Nature…", label_visibility="collapsed")
        st.markdown('<p class="field-hint">Separate with commas — e.g. Art, Cafes, Museums</p>', unsafe_allow_html=True)

        submitted = st.form_submit_button("Generate My Itinerary →")

    st.markdown("""
    <div class="trust-row">
        <div class="chip">🔒 Private</div>
        <div class="chip">⚡ Groq Fast</div>
        <div class="chip">🌐 Any City</div>
        <div class="chip">✈️ Free to Use</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Result ──
    if submitted:
        if city and interests:
            with st.spinner("Crafting your itinerary…"):
                try:
                    planner = TravelPlanner()
                    planner.set_city(city)
                    planner.set_interests(interests)
                    itinerary = planner.create_itineary()

                    st.markdown(f"""
                    <div class="result-section">
                        <div class="result-top">
                            <div class="r-icon">🗺️</div>
                            <div>
                                <div class="r-city">{city}</div>
                                <div class="r-interests">{interests}</div>
                            </div>
                        </div>
                        <div class="itinerary-box">
                    """, unsafe_allow_html=True)

                    st.markdown(itinerary)
                    st.markdown("</div></div>", unsafe_allow_html=True)

                    st.download_button(
                        "⬇️ Download Itinerary",
                        data=itinerary,
                        file_name=f"{city.lower().replace(' ','_')}_itinerary.txt",
                        mime="text/plain",
                    )

                except Exception as e:
                    st.error(f"Something went wrong: {str(e)}")
        else:
            st.warning("Please enter both a city and your interests.")