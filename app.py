import streamlit as st
import compiler
import frameworks
import home
import libraries
import opensource
import proglangs
import test

PAGES={
	"Home": home,
	"Programming languages": proglangs,
	"Libraries": libraries,
	"Frameworks": frameworks,
	"Open source projects": opensource,
	"Compiler": compiler,
	"Choose your programming language": test
}

st.set_page_config("CodeĐscovery","images\icon.png")

st.markdown("<style>p{font-family: Verdana,sans-serif;font-size: 1.25rem;}h1,h2,h3{font-family: \"Times New Roman\",serif;}h1{font-size: 2.25rem;}h2{font-size: 2rem;}h3{font-size: 1.75rem;}</style>",True)

st.sidebar.markdown("___")

st.sidebar.markdown("<h1>Go to:</h1>",True)

PAGES[st.sidebar.radio("",list(PAGES.keys()))].app()