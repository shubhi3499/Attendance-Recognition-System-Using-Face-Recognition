import streamlit as st
from src.components.header import header_home
from src.ui.base_layout import style_base_layout,style_background_home

def home_screen():


    #header home component 
    header_home()

    #home page background
    style_background_home()

    #will inject a style tag that will override the streamlit basic styling =>src/ui/style_base_layout
    style_base_layout()

    col1,col2 = st.columns(2)

    with col1:
        if st.button('Teacher Portal'):
            st.session_state['login_type'] = 'teacher'
            st.rerun()
    with col2:
        if st.button('Student Portal'):
            st.session_state['login_type'] = 'student'
            st.rerun()