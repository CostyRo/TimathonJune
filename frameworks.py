from PIL import Image
import streamlit as st
import sidebar
import functions

def flask():
	st.markdown("<h2>Flask</h2>",True)

	st.image(Image.open("images\$flask.png"),use_column_width="auto")

	st.markdown("<p>Flask is another well-known and best Python framework that comes under the Micro framework category and comes with the BSD license. It is inspired by the Sinatra Ruby framework. It needs the Werkzeug WSGI toolkit and the Jinja2 template, and ToscaWidgets is an example of a WSGI framework. Dash developers can utilize Flask as a web framework. Thanks to the functionality, restful request dispatching, request handling, modular, and lightweight frontend design of Flask, it is promptly adaptable. ORMs deliver an advanced abstraction on an interactive database that lets a developer transcribe code in place of SQL to read, create, delete, and update tools and data in the database. Flask is a framework of Python language that allows the users to build a genuine web app foundation and database tables from where they can use any source of extensions needed.</p>",True)

def django():
	st.markdown("<h2>Django</h2>",True)

	st.image(Image.open("images\django.png"),use_column_width="auto")

	st.markdown("<p>The Django framework is one of the most used Python frameworks for developing large-scale web applications and websites. It tends to follow the MVC architecture minutely enough to be known as an MVC framework. One major reason for its popularity is, it is open source and free to use a full-stack Python framework, also available in maintenance mode, and asyncio library, including a variety of built-in features rather than just offering individual libraries for your projects. Python language with the Django framework is based on the \"Don’t Repeat Yourself\" (DRY) functionality. Django Python web development framework uses its ORM (Object Relational Mapper) for mapping objects to multi-database tables which allows the code to work across multiple databases and template engines to make it easier to migrate from one database to the other. Despite the fact that Django Python frameworks provide a range of inbuilt libraries and database support - MySQL, SQLite, PostgreSQL, and Oracle, it also supports other databases and templating systems via third-party adapters, drivers, and content management systems.</p>",True)

def bottle():
	st.markdown("<h2>Bottle</h2>",True)

	st.image(Image.open("images\$bottle.png"),use_column_width="auto")

	st.markdown("<p>Bottle is one of the best Python web framework, which falls under the class of small-scale frameworks. Originally, it was developed for building web APIs. Also, Bottle tries to execute everything in a single source document. It has no other dependencies than Python Standard Library. The out-of-the-box functionalities include templating, utilities, directing, and some fundamental abstraction over the WSGI standard. Like Flask, you will be coding significantly closer to the metal than with a full-stack framework. Bottle enables developers to work closer to the hardware. It not only builds simplistic personal-use apps but an apt place for learning Python frameworks and prototyping. For example, Bottle has been used by Netflix for its web interfaces.</p>",True)

def cherrypy():
	st.markdown("<h2>CherryPy</h2>",True)

	st.image(Image.open("images\cherrypy.png"),use_column_width="auto")

	st.markdown("<p>CherryPy is an open-source, minimalist web framework. It makes building Python web applications no different than building any other object-oriented program. CherryPy is created to be extensible. The framework even offers mechanisms for hook points and extensions.For example, a CherryPy-powered web app is a standalone Python application that embeds its own multi-threaded web server. With its own web server, the extension points include functions outside the request-response cycle, thus adding to the level of CherryPy’s extensibility.</p>",True)

def python():
	st.markdown("<h1>Python</h1>",True)

	st.image(Image.open("images\python.png"),use_column_width="auto")

	flask()

	django()

	bottle()

	cherrypy()

def qt():
	st.markdown("<h2>Qt</h2>",True)

	st.image(Image.open("images\qt.png"),use_column_width="auto")

	st.markdown("<p>QT is one of the best choices for developers wanting to build graphical programs that could run on Windows, Linux, and macOS. Built in C++, it is, actually, an open-source widget toolkit. Apart from desktop platforms, QT applications can also run on Android or embedded systems with little to no changes. If you are not into graphical applications and, instead, like the terminal and console interfaces even then QT can also be of immense use. With it, developers can conveniently build non-GUI programs such as command-line tools and consoles for servers.</p>",True)

def cpp():
	st.markdown("<h1>C++</h1>",True)

	st.image(Image.open("images\c++.png"),use_column_width="auto")

	qt()

def dotnet():
	st.markdown("<h2>.NET</h2>",True)

	st.image(Image.open("images\dotnet.png"),use_column_width="auto")

	st.markdown("<p>The .NET framework is a software development framework from Microsoft. It provides a controlled programming environment where software can be developed, installed and executed on Windows-based operating systems. .NET is central to Microsoft’s over-arching development strategy and is the organization’s competition to Java. It is so central to development on Windows platforms, the term’s usage depends on context. For example, it’s common to simply talk generally about a \".NET developer\" as a programmer who works in a Microsoft development environment. On the other hand, when writing code, the developer references what specific version of the Framework is being worked with - .NET 2.0, which came out in 2005, is much different than .NET 4.0, which was shipped in 2010.Even though the term is written as \".NET\", it is not an acronym. It is pronounced as \"dot net\" and is sometimes written as dotnet or dot-net.</p>",True)

def cs():
	st.markdown("<h1>C#</h1>",True)

	st.image(Image.open("images\c#.png"),use_column_width="auto")

	dotnet()

def app():
	sidebar.sidebar()

	functions.showLogo()

	python()

	cpp()

	cs()