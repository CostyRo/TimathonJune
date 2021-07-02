import images
import streamlit as st
import frameworksstrings
import functions

def flask():
	st.markdown(frameworksstrings.flask,True)

	st.image(images.flaskImage,use_column_width="auto")

	st.markdown(frameworksstrings.flaskDescription,True)

def django():
	st.markdown(frameworksstrings.django,True)

	st.image(images.djangoImage,use_column_width="auto")

	st.markdown(frameworksstrings.djangoDescription,True)

def bottle():
	st.markdown(frameworksstrings.bottle,True)

	st.image(images.bottleImage,use_column_width="auto")

	st.markdown(frameworksstrings.bottleDescription,True)

def cherrypy():
	st.markdown(frameworksstrings.cherrypy,True)

	st.image(images.cherrypyImage,use_column_width="auto")

	st.markdown(frameworksstrings.cherrypyDescription,True)

def pythonFrameworks():
	flask()

	django()

	bottle()

	cherrypy()

def python():
	st.markdown(frameworksstrings.python,True)

	st.image(images.pythonImage,use_column_width="auto")

	pythonFrameworks()

def qt():
	st.markdown(frameworksstrings.qt,True)

	st.image(images.qtImage,use_column_width="auto")

	st.markdown(frameworksstrings.qtDescription,True)

def cpp():
	st.markdown(frameworksstrings.cpp,True)

	st.image(images.cppImage,use_column_width="auto")

	qt()

def dotnet():
	st.markdown(frameworksstrings.dotnet,True)

	st.image(images.dotnetImage,use_column_width="auto")

	st.markdown(frameworksstrings.dotnetDescription,True)

def cs():
	st.markdown(frameworksstrings.cs,True)

	st.image(images.csImage,use_column_width="auto")

	dotnet()

def app():
	functions.preparePage()

	python()

	cpp()

	cs()