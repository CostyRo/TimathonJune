from PIL import Image
import streamlit as st
import frameworksstrings
import functions

def flask():
	st.markdown(frameworksstrings.flask,True)

	st.image(Image.open(frameworksstrings.flaskImageLocation),use_column_width="auto")

	st.markdown(frameworksstrings.flaskDescription,True)

def django():
	st.markdown(frameworksstrings.django,True)

	st.image(Image.open(frameworksstrings.djangoImageLocation),use_column_width="auto")

	st.markdown(frameworksstrings.djangoDescription,True)

def bottle():
	st.markdown(frameworksstrings.bottle,True)

	st.image(Image.open(frameworksstrings.bottleImageLocation),use_column_width="auto")

	st.markdown(frameworksstrings.bottleDescription,True)

def cherrypy():
	st.markdown(frameworksstrings.cherrypy,True)

	st.image(Image.open(frameworksstrings.cherrypyImageLocation),use_column_width="auto")

	st.markdown(frameworksstrings.cherrypyDescription,True)

def pythonFrameworks():
	flask()

	django()

	bottle()

	cherrypy()

def python():
	st.markdown(frameworksstrings.python,True)

	st.image(Image.open(frameworksstrings.pythonImageLocation),use_column_width="auto")

	pythonFrameworks()

def qt():
	st.markdown(frameworksstrings.qt,True)

	st.image(Image.open(frameworksstrings.qtImageLocation),use_column_width="auto")

	st.markdown(frameworksstrings.qtDescription,True)

def cpp():
	st.markdown(frameworksstrings.cpp,True)

	st.image(Image.open(frameworksstrings.cppImageLocation),use_column_width="auto")

	qt()

def dotnet():
	st.markdown(frameworksstrings.dotnet,True)

	st.image(Image.open(frameworksstrings.dotnetImageLocation),use_column_width="auto")

	st.markdown(frameworksstrings.dotnetDescription,True)

def cs():
	st.markdown(frameworksstrings.cs,True)

	st.image(Image.open(frameworksstrings.csImageLocation),use_column_width="auto")

	dotnet()

def app():
	functions.preparePage()

	python()

	cpp()

	cs()