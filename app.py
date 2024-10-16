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
    I'm a passionate Data Scientist and Software Developer with experience in building machine learning models, web applications, and more.

    - 💼 Check out my projects below.
    - 🌱 I’m currently learning about new AI technologies.
    - 💬 Let's connect!
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

def skills():
    set_background('images/img.png')
    st.title("Skills")
    st.markdown("""
    - Programming: Python, JavaScript, HTML, CSS
    - Data Science: Machine Learning, NLP, Data Visualization
    - Tools: Git, Docker, Streamlit, TensorFlow, Scikit-learn
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

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("Home", key="home_button"):
        st.session_state.page = "home"
with col2:
    if st.button("Projects", key="projects_button"):
        st.session_state.page = "projects"
with col3:
    if st.button("Skills", key="skills_button"):
        st.session_state.page = "skills"
with col4:
    if st.button("Contact", key="contact_button"):
        st.session_state.page = "contact"

if st.session_state.page == "home":
    home()
elif st.session_state.page == "projects":
    projects()
elif st.session_state.page == "skills":
    skills()
elif st.session_state.page == "contact":
    contact()
