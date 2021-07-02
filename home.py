import streamlit as st
import functions
import homestrings

def displayHomeMessage():
	st.markdown(homestrings.title,True)

	st.markdown(homestrings.message1,True)

	st.markdown(homestrings.message2,True)

	st.markdown(homestrings.message3,True)

	st.markdown(homestrings.message4,True)

	st.markdown(homestrings.message5,True)

	st.markdown(homestrings.message6,True)

def app():
	functions.preparePage()

	displayHomeMessage()