import streamlit as st
from story_generator import generate_story
from pdf_generator import create_pdf

st.set_page_config(page_title="TinyTales", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&family=Pacifico&display=swap');

    html, body, .stApp {
        font-family: 'Quicksand', sans-serif;
        background-color: #0a1e3f !important;
        color: #ffffff !important;
    }

    h1, h2, h3, h4, h5, h6, p, label, span, div {
        color: #ffffff !important;
    }

    /* Input boxes and dropdowns */
    .stTextInput>div>div>input,
    .stTextArea textarea,
    .stSelectbox div[data-baseweb="select"],
    .stMultiSelect div[data-baseweb="select"] {
        background-color: #ffffff !important;
        color: #0a1e3f !important;
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #ffffff;
    }

    /* Dropdown menu options */
    div[data-baseweb="popover"] {
        background-color: #ffffff !important;
        color: #0a1e3f !important;
    }

    div[data-baseweb="option"] {
        background-color: #ffffff !important;
        color: #0a1e3f !important;
    }

    /* Slider styling */
    .stSlider > div {
        background-color: transparent !important;
    }

    .stSlider [role="slider"] {
        background-color: #ffffff !important;
    }

    .stSlider .css-14xtw13 {
        background-color: #ffffff !important;
    }

    .stSlider .css-1c5h2m3 {
        background-color: #4d5b76 !important;
    }

    /* FORCE button text visibility + styling */
.stButton > button {
    background-color: #ffffff !important;
    color: #0a1e3f !important;
    font-weight: bold !important;
    font-size: 1rem !important;
    border: none !important;
    padding: 0.6rem 1.4rem !important;
    border-radius: 10px !important;
    box-shadow: 2px 2px 6px rgba(0, 0, 0, 0.15) !important;
    transition: all 0.3s ease;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    text-align: center !important;
}

.stButton > button * {
    color: #0a1e3f !important;
    font-weight: bold !important;
    font-size: 1rem !important;
    text-shadow: none !important;
}

    </style>
""", unsafe_allow_html=True)


st.markdown("<h1>TinyTales <3</h1>", unsafe_allow_html=True)

st.markdown("Doomscrolling? How about reading a story based on your interests, for you and by you")

prompt = st.text_area("Story Prompt / Key Ideas", placeholder="e.g., A tiny dragon learning to fly...", height=100)

genres = st.multiselect(
    "Select Genres",
    ["Fantasy", "Adventure", "Mystery", "Fairy Tale", "Sci-Fi", "Slice of Life", "Animal Tale", "Magic Realism"]
)

tone = st.selectbox("Story Tone", ["Wholesome", "Silly", "Magical", "Emotional", "Spooky", "Adventurous"])

word_limit = st.slider("Word Limit", min_value=100, max_value=1500, step=50, value=300)

generate = st.button("Generate me a story")

if generate:
    if not prompt or not genres:
        st.warning("Please fill in the prompt and select at least one genre!")
    else:
        with st.spinner("little goblins scribbling on the pages..."):
            story_text = generate_story(prompt, genres, tone, word_limit)

        st.success("Here's your TinyTale <3")

        st.markdown("### Your thoughts in our words -")
        html_story = story_text.replace('\n', '<br>')
        st.markdown(f"<div style='line-height: 1.7; font-size: 16px;'>{html_story}</div>", unsafe_allow_html=True)


        pdf_path = create_pdf(story_text)
        with open(pdf_path, "rb") as f:
            st.download_button("Download Story as PDF", f, file_name="TinyTales_Story.pdf")

