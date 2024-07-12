import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

from setting.config import cfg

cookies = EncryptedCookieManager(prefix='my_app_', password='jashhasusauasuosacjb_1111_ascisa')

if not cookies.ready():
    st.stop()

st.sidebar.title("Main Menu")
st.title("TEST SEND EMAIL")
# Replace with your direct link from Google Drive
image_url = 'https://drive.usercontent.google.com/download?id=13DkXSXTGEiPfbsu2arIAgG-2fMo6VJ2D&export=view'
st.image(image_url, use_column_width=True)
st.title("TEST DEPLOY")
