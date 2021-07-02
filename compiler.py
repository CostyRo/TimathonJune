import streamlit as st
import functions
import compilerstrings

def app():
	functions.preparePage()

	st.warning(compilerstrings.uf)

	language=st.selectbox(compilerstrings.choose,compilerstrings.programmingLanguages)

	col1,col2=st.beta_columns(2)

	with col1: code=st.text_area("Write your code here: ","",250)

	with col2:
		if code=="": st.code(compilerstrings.emptyCode,language)
		else: st.code(code+"".join("⠀\n" for _ in range(13-len(code.split("\n")))),language)

	if st.button(compilerstrings.run): functions.execode(language)