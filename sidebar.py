import streamlit as st
from images import githubImage,patreonImage

def sidebar():
	st.sidebar.markdown("___")

	st.sidebar.markdown("<h3>Contact me to add a new language/framework/library/open source project or to report a mistake or to give me some feedback: </h3>",True)

	st.sidebar.markdown("<h3><a href=\"mailto:codediscovery1@gmail.com\" style=\"color: white\">CodeĐscovery</a></h3>",True)

	st.sidebar.markdown("___")

	col1,col2=st.beta_columns(2)

	with col1:
		st.sidebar.image(githubImage,use_column_width="auto")
		st.sidebar.markdown("[Github link](https://github.com/CostyRo/TimathonJune \"github\")")
	with col2:
		st.sidebar.image(patreonImage,use_column_width="auto")
		st.sidebar.markdown("[Patreon link](https://www.patreon.com \"patron\")")

	st.sidebar.markdown("___")