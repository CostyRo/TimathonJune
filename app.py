import streamlit as st
import functions
import const

functions.prepare()

const.PAGES[st.sidebar.radio("",list(const.PAGES.keys()))].app()