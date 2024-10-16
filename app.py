import streamlit as st
from PIL import Image
import base64


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
    st.title("Welcome to My Portfolio!")
    
    profile_image = Image.open('images/img2.jpeg')
    st.image(profile_image, caption='Leonard Sanya')

    st.markdown("""
    ### Hi, I'm [Leonard Sanya]!
    
    """)

def bio():  
    st.title("Bio")
    st.markdown("""
    ### Hi, I'm [Leonard Sanya]!
    
    """)
def cv():
    st.title("CV")
    st.markdown("""
    ### Hi, I'm [Leonard Sanya]!
    
    """)

        # Projects Section (Collapsible)
    with st.expander("📁 Education"):
        st.markdown("Here are some of my recent works:")
        
        #1
        st.subheader("AIMS SENEGAL")
        st.markdown("""
        
        """)
        #2
        st.subheader("AIMS CAMEROON")
        st.markdown("""
        
        """)
        #3
        st.subheader("kibabii University")
        st.markdown("""
        
        """)
        #4
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
    st.title("experiences")
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


if "page" not in st.session_state:
    st.session_state.page = "home"

col1, col2, col3, col4,col5, col6= st.columns(6)

with col1:
    if st.button("Home", key="home_button"):
        st.session_state.page = "home"
with col2:
    if st.button("Bio", key="bio_button"):
        st.session_state.page = "bio"
with col3:
    if st.button("CV", key="cv_button"):
        st.session_state.page = "cv"
with col4:
    if st.button("Projects", key="project_button"):
        st.session_state.page = "project"
with col5:
    if st.button("Experiences", key="experiences_button"):
        st.session_state.page = "experiences"
with col6:
    if st.button("Contacts", key="contacts_button"):
        st.session_state.page = "contact"


if st.session_state.page == "home":
    home()
elif st.session_state.page == "projects":
    projects()
elif st.session_state.page == "skills":
    skills()
elif st.session_state.page == "contact":
    contact()
if st.session_state.page == "cv":
    cv()
elif st.session_state.page == "experiences":
    experiences()
elif st.session_state.page == "bio":
    bio()
