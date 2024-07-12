import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

cookies = EncryptedCookieManager(prefix='my_app_', password='jashhasusauasuosacjb_1111_ascisa')

if not cookies.ready():
    st.stop()

st.sidebar.title("Main Menu")
st.title("TEST SEND EMAIL")


