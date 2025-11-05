import streamlit as st
from PIL import Image
import base64
from pathlib import Path

# --- PAGE CONFIGURATION ---
# Use the title from your HTML file
st.set_page_config(
    page_title="Vikram Kumar | Data Science Portfolio",
    page_icon="🐍", # Python snake emoji as icon
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- IMAGE LOADING ---
# Function to load the image using PIL (Python Imaging Library)
def load_image(path):
    try:
        return Image.open(path)
    except FileNotFoundError:
        st.error(f"Error: Profile photo '{path}' not found.")
        st.info("Please make sure 'vikramPhoto.jpg' is in the same folder as this script.")
        return None
    except Exception as e:
        st.error(f"Error loading image: {e}")
        return None

# --- CUSTOM CSS ---
# This CSS mimics the style of your HTML file:
# - Animated gradient background (the "revolving snake")
# - Colors for text (blue title, yellow subtitle)
# - Styled skill "pills"
# - Styled profile photo (rounded-xl, yellow border)
CSS = """
/* 1. Animated Gradient Background (The "revolving snake" effect) */
@keyframes gradient-animation {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

[data-testid="stAppViewContainer"] > .main {
    /* Using Python-themed colors: dark, blue, and yellow/green */
    background: linear-gradient(-45deg, 
        #0a192f, /* Dark Blue */
        #000000, /* Black */
        #3572A5, /* Python Blue */
        #1a1a1a, /* Dark Gray */
        #FFD43B  /* Python Yellow */
    );
    background-size: 400% 400%;
    animation: gradient-animation 20s ease infinite;
    color: #E5E7EB; /* Default light text (Tailwind gray-200) */
}

/* 2. Make all text readable */
.stMarkdown, .stSubheader, .stTitle, p, li, .stException {
    color: #E5E7EB !important; /* Tailwind gray-200 */
    font-family: 'Inter', sans-serif;
}

/* 3. Style Header Text to match your HTML */
/* Vikram Kumar (Name) */
h1[data-testid="stTitle"] {
    color: #60A5FA !important; /* Tailwind blue-400 */
    font-size: 3rem !important;
    font-weight: 800; /* extrabold */
    letter-spacing: -0.025em; /* tracking-tight */
    padding-bottom: 1rem;
    border-bottom: 1px solid #374151; /* gray-700 */
}

/* Data Scientist | Machine Learning Engineer (Job Title) */
h2.stSubheader {
    color: #FCD34D !important; /* Tailwind yellow-400 */
    font-size: 1.25rem !important;
    font-weight: 500;
}

/* Professional Summary / Core Skills (Section Headers) */
h3 {
    font-size: 1.5rem; /* text-2xl */
    font-weight: 600; /* semibold */
    color: #F9FAFB !important; /* gray-100 */
    border-left: 4px solid #60A5FA; /* border-l-4 border-blue-400 */
    padding-left: 0.75rem; /* pl-3 */
    margin-bottom: 1rem; /* mb-4 */
    margin-top: 1rem;
}

/* Change the "Core Skills" header to use the yellow border */
h3#core-skills {
    border-left-color: #FCD34D; /* yellow-400 */
}


/* 4. Style the Profile Photo */
[data-testid="stImage"] img {
    border-radius: 0.75rem; /* rounded-xl */
    border: 4px solid #FCD34D; /* border-4 border-yellow-500 */
    box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); /* shadow-xl */
}

/* 5. Style the Skill Pills */
.skill-pill-container {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem; /* gap-2 */
}
.skill-pill {
    background-color: #2563EB; /* bg-blue-600 */
    color: white;
    font-size: 0.875rem; /* text-sm */
    font-weight: 500; /* font-medium */
    padding: 0.25rem 0.75rem; /* px-3 py-1 */
    border-radius: 9999px; /* rounded-full */
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06); /* shadow-md */
}
.skill-pill-yellow {
    background-color: #D97706; /* bg-yellow-600 */
}
"""

# Inject the custom CSS
st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)


# --- PORTFOLIO LAYOUT ---
# We use st.columns to create the left/right split
# [1, 3] ratio is like 25% width for col1 and 75% for col2
col1, col2 = st.columns([1, 3])

with col1:
    # --- LEFT SIDE: PHOTO ---
    profile_image = load_image("vikramPhoto.jpg")
    if profile_image:
        st.image(profile_image, use_column_width=True)
    
    # Caption under the photo
    st.markdown(
        "<p style='text-align: center; color: #9CA3AF; font-weight: 300;'>Data Analyst & Scientist</p>", 
        unsafe_allow_html=True
    )

with col2:
    # --- RIGHT SIDE: NAME & SUMMARY ---
    
    # Name and Job Title
    st.title("Vikram Kumar")
    st.subheader("Data Scientist | Machine Learning Engineer")
    # st.divider() is not used here because the h1 has its own border-bottom in CSS

    # Professional Summary
    st.markdown("<h3>Professional Summary</h3>", unsafe_allow_html=True)
    st.markdown(
        """
        <p style="font-size: 1.125rem; line-height: 1.75;">
        Highly motivated and detail-oriented <strong>Data Scientist</strong> with 3+ years of experience 
        transforming raw data into actionable business intelligence. 
        Proficient in <strong>Python</strong> (Pandas, NumPy, Scikit-learn, TensorFlow) and <strong>SQL</strong>, 
        with a strong focus on data visualization and storytelling. 
        Proven ability to build, train, and deploy <strong>machine learning models</strong> 
        (Classification, Regression, Time Series) to solve complex problems and 
        drive measurable results in areas such as predictive maintenance and customer segmentation. 
        Seeking to leverage analytical expertise to contribute to data-driven decision-making.
        </p>
        """, 
        unsafe_allow_html=True
    )

    # Core Skills
    st.markdown('<h3 id="core-skills">Core Skills</h3>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="skill-pill-container">
            <span class="skill-pill">Python/Pandas</span>
            <span class="skill-pill">Machine Learning</span>
            <span class="skill-pill">SQL/NoSQL</span>
            <span class="skill-pill skill-pill-yellow">Deep Learning (TensorFlow)</span>
            <span class="skill-pill skill-pill-yellow">Data Visualization (Matplotlib, Tableau)</span>
            <span class="skill-pill">Cloud (AWS/Azure)</span>
        </div>
        """,
        unsafe_allow_html=True
    )

# --- HOW TO RUN (as a helpful footer) ---
st.info("""
**How to run this app:**
1.  Save this code as `portfolio_app.py`.
2.  Make sure your photo `vikramPhoto.jpg` is in the **same folder**.
3.  Open your terminal or command prompt.
4.  Install Streamlit: `pip install streamlit pillow` (Pillow is for the image)
5.  Run the app: `streamlit run portfolio_app.py`
""")