import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

from app.setting.config import cfg

cookies = EncryptedCookieManager(prefix='my_app_', password='jashhasusauasuosacjb_1111_ascisa')

if not cookies.ready():
    st.stop()

st.sidebar.title("Main Menu")
st.title("TEST SEND EMAIL")
st.text("Alo anh Nhân ơi vip ko kkk")
st.image(cfg.IMAGE_AVATAR, use_column_width=True)

