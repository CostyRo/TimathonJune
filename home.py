import streamlit as st
import sidebar
import functions

def app():
	sidebar.sidebar()

	functions.showLogo()

	st.markdown("<h1>Explore programming languages, libraries, frameworks and open source projects.</h1>",True)

	st.markdown("<h3>CodeĐscovery give you 6 different options to find your next programming language.</h3>",True)

	st.markdown("<h3>An option is to browse to the sections with programming languages and choose the programming languages which seems best to you.</h3>",True)

	st.markdown("<h3>Other two options are to look into frameworks and libraries and find the programming language that suits you best in your area of interests.</h3>",True)

	st.markdown("<h3>Other option is to look at the open source projects and find a project where you want to contribute.</h3>",True)

	st.markdown("<h3>Exist an options where you can test a programming language to see if the programming language is for you.</h3>",True)

	st.markdown("<h3>And the last option is to respond to some questions to find your best programming language!</h3>",True)