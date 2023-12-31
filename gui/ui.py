import streamlit as st
from PIL import Image

# Hides Streamlit menu from UI
hide_streamlit_style = """
            <style>
            MainMenu {visibility: hidden;}
            </style>
            """

# Hides Streamlit footer from UI
ft = """
    <style>
    a:link , a:visited{
    color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
    background-color: transparent;
    text-decoration: none;
    }

    a:hover,  a:active {
    color: #0283C3; /* theme's primary color*/
    background-color: transparent;
    text-decoration: underline;
    }

    #page-container {
      position: relative;
      min-height: 0vh;
    }

    footer{
        visibility:hidden;
    }

    .footer {
    position: fixed;
    display: flex;
    justify-items: center;
    bottom: 0;
    width: 100%;
    background-color: transparent;
    color: #808080; /* theme's text color hex code at 50 percent brightness*/
    text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
    }
    </style>

    <div id="page-container">

    <div class="footer">
    <p style='font-size: 0.875em;'>Made with
    with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/>&nbsp;by <a style='display: inline; text-align: left;' href="https://github.com/andykr1k" target="_blank">Andrew Krikorian</a></p>
    </div>

    </div>
    """

# Function to create header of the web app
def Header():
    st.set_page_config(page_title="PolytopeML", layout="wide", page_icon='./assets/logo.png')

    image = Image.open('./assets/logo.png')

    img, head = st.columns([0.2,0.8])

    with img:
        st.image(image, width=150)

    with head:
        st.header("PolytopeML")
        st.caption("Studying the use of neural networks learning data from algebraic geometry, specifically the wall-chamber decomposition associated with particular spaces parameterizing plane curves and a line. There is currently limited knowledge about patterns within this type of data, so we are investigating if a neural network can accurately predict this geometric information.")
    return

# Function to create body of the web app
def Body():
    
    return

# Function to create sidebar of the web app
def Sidebar():
    with st.sidebar:

        st.header("Start Here")

    return

# Function to create footer of the web app
def Footer():
    st.write(ft, unsafe_allow_html=True)
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)
    return 