import streamlit as st
from PIL import Image
import base64


import streamlit as st
from PIL import Image
import base64
from io import BytesIO 

def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url(data:image/png;base64,{encoded_image});
             background-size: cover;
             background-position: center;
             background-repeat: no-repeat;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

def home():
    set_background('images/img.png')  
    st.title("Welcome, I'm Leonard Sanya")
    
    profile_image = Image.open('images/img2.jpeg')

    # Display the image with rounded corners using CSS
    st.markdown(
        f"""
        <style>
            .profile-container {{
                display: flex;
                align-items: flex-start; /* Aligns items at the start */
            }}
            .profile-image {{
                border-radius: 50%; /* Circle shape */
                width: 100px; /* Adjust width */
                height: 100px; /* Adjust height */
                object-fit: cover; /* Cover the image */
            }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Convert the image to a base64 string
    buffered = BytesIO()
    profile_image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()

    # Create a container for the profile image
    st.markdown(
        f'<div class="profile-container"><img class="profile-image" src="data:image/jpeg;base64,{img_str}" alt="Leonard Sanya"></div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    ### Hi, I'm [Leonard Sanya]!
    """)


def bio():  
    st.title("Bio")
    st.markdown("""
    ### Hi, I'm [Leonard Sanya]!
    """)

def cv():
    set_background('images/cv_background.png') 
    st.title("Curriculum Vitae")
    with st.expander("📁 Education"):
        st.markdown("Here are some of my recent works:")
        
        # Education details
        st.subheader("February 2024 - July 2025 : AIMS - Senegal")
        st.markdown("""
        - Foundations to Machine Learning,
        - Computer Vision, 
        - Kernel Methods for Machine Learning, 
        - Optimization
        - Machine Learning Operations
        """)
        st.subheader("August 2022 - June 2023 : AIMS - Cameroon")
        st.markdown(""" 
        - Statistical Inference
        - High Dimension Data
        - Machine Learning
        - Data Analysis 
        - Data Science
        - Natural Language Processing
        - Advanced Data Science
        - Mathematical Modeling for Climate Science 
        - Machine Learning Made Easy
        - Big Data 
        - Network Science
        """)
        st.subheader("Kibabii University")
        st.markdown("""
        """)
        st.subheader("St Benedicts High School Budalangi")
        st.markdown("""
        """)

def projects():
    set_background('images/img.png')
    st.title("Projects")
    st.markdown("Here are some of my recent works:")
    st.subheader("🏠 House Price Prediction")
    st.markdown("""
    I built a machine learning model to predict house prices based on various factors like the number of rooms, location, and year built.
    - **Technologies:** Python, Scikit-Learn, Pandas, Matplotlib
    - [GitHub Repo](https://github.com/yourusername/house-price-prediction)
    """)
    st.subheader("🎥 Sentiment Analysis of IMDB Reviews")
    st.markdown("""
    A project to classify movie reviews as positive or negative using Natural Language Processing techniques.
    - **Technologies:** Python, Scikit-Learn, NLTK, Pandas
    - [GitHub Repo](https://github.com/yourusername/imdb-sentiment-analysis)
    """)

def experiences():
    st.title("Experiences")
    st.markdown("""
    ### Hi, I'm [Leonard Sanya]!
    """)

def contact():
    set_background('images/img.png') 
    st.title("Contact")
    st.markdown("Feel free to reach out to me:")
    st.write("[LinkedIn](https://www.linkedin.com/in/leonard-sanya-bb9550255/)")
    st.write("[GitHub](https://github.com/leonard-sanya)")
    st.write("Email: lsanya@aimsammi.org or leonard.sanya@aims-cameroon.org")


# Initialize session state for page navigation
if "page" not in st.session_state:
    st.session_state.page = "home"

# Sidebar for navigation buttons
with st.sidebar:
    if st.button("Home"):
        st.session_state.page = "home"
    if st.button("Bio"):
        st.session_state.page = "bio"
    if st.button("CV"):
        st.session_state.page = "cv"
    if st.button("Projects"):
        st.session_state.page = "projects"
    if st.button("Experiences"):
        st.session_state.page = "experiences"
    if st.button("Contact"):
        st.session_state.page = "contact"

# Display the selected page
if st.session_state.page == "home":
    home()
elif st.session_state.page == "projects":
    projects()
elif st.session_state.page == "skills":
    skills()
elif st.session_state.page == "contact":
    contact()
elif st.session_state.page == "cv":
    cv()
elif st.session_state.page == "experiences":
    experiences()
elif st.session_state.page == "bio":
    bio()
