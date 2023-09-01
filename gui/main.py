import streamlit as st
from ui import Header, Footer, Sidebar, Body

# Main
def main():
    Header()

    Sidebar()
    
    Body()

    Footer()
    return

if __name__ == '__main__':
    main()