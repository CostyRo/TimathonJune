import images
import streamlit as st
import functions

def python():
	st.image(images.pythonImage,use_column_width="auto")

	st.markdown("<p>I think Python is the best programming languages for you! Python is a great language for beginners, for people who love machine learning and data science, for people who want to do web development and for people who are interesed in math.</p>",True)

def c():
	st.image(images.cImage,use_column_width="auto")

	st.markdown("<p>I think C is the best programming languages for you! C is a great lanuage to learn programming and to learn more about a computer, a great language for embedded programming and low-level programming.</p>",True)

def cpp():
	st.image(images.cppImage,use_column_width="auto")

	st.markdown("<p>I think C++ is the best programming languages for you! C++ is a great languages for competitive programming, a great language to become in nerd/geek in programming and a great language for making games.</p>",True)

def cs():
	st.image(images.csImage,use_column_width="auto")

	st.markdown("<p>I think C# is the best programming languages for you! C# is a great language for people who want to do desktop, web and mobile development and also a great language for making games.</p>",True)

def java():
	st.image(images.javaImage,use_column_width="auto")

	st.markdown("<p>I think Java is the best programming languages for you! Java is a great language for making android development and for making web development.</p>",True)

def javascript():
	st.image(images.javascriptImage,use_column_width="auto")

	st.markdown("<p>I think Javascript is the best programming languages for you! Javascript is a great language because is the language of the web, we can do web development, cross-platform mobile development and other awesome things.</p>",True)

def haskell():
	st.image(images.haskellImage,use_column_width="auto")

	st.markdown("<p>I think Haskell is the best programming languages for you! WOW! Someone who got this, you are unique, if you got this it means you are already a great programmer or you will become a great programmer who love functional programming.</p>",True)

def kotlin():
	st.image(images.kotlinImage,use_column_width="auto")

	st.markdown("<p>I think Kotlin is the best programming languages for you! Kotlin is a great language for making android development, ios development and web development, Kotlin is a new language with a lot of potential.</p>",True)

def swift():
	st.image(images.swiftImage,use_column_width="auto")

	st.markdown("<p>I think Swift is the best programming languages for you! Swift is the perfect language for Apple fans who want to do ios development.</p>",True)



def app():
	points={
		"Python": 0,
		"C": 0,
		"C++": 0,
		"C#": 0,
		"Java": 0,
		"Javascript": 0,
		"Haskell": 0,
		"Kotlin": 0,
		"Swift": 0
	}

	submit=False

	functions.preparePage()

	st.markdown("<h1>Choose the programming language which suits you best: </h1>",True)

	st.markdown("<h3>You need to answear at few questions to find the best programming languages for you. Let's begin!</h3>",True)

	with st.form(key="test"):
		st.markdown("<h2>First question:</h2>",True)

		st.markdown("<p>Are you a beginner?</p>",True)

		answear1=st.radio("",["Yes","No"],key="1")

		if answear1=="Yes": functions.modify(points,["+","+","-","-","","+","-","",""])
		else: functions.modify(points,["","","+","","","","+","",""])

		st.markdown("<h2>Second question:</h2>",True)

		st.markdown("<p>Do you like web?</p>",True)

		answear2=st.radio("",["Yes","No"],key="2")

		if answear2=="Yes": functions.modify(points,["+","-","-","+","+","+","","+",""])

		st.markdown("<h2>Third question:</h2>",True)

		st.markdown("<p>Do you like desktop apps?</p>",True)

		answear3=st.radio("",["Yes","No"],key="3")

		if answear3=="Yes": functions.modify(points,["+","+","-","-","","+","-","",""])

		st.markdown("<h2>Fourth question:</h2>",True)

		st.markdown("<p>Do you like mobile apps?</p>",True)

		answear4=st.radio("",["Yes","No"],key="4")

		if answear4=="Yes": functions.modify(points,["+","+","+","+","","","","","+"])

		st.markdown("<h2>Fifth question:</h2>",True)

		st.markdown("<p>Do you like games?</p>",True)

		answear5=st.radio("",["Yes","No"],key="5")

		if answear5=="Yes": functions.modify(points,["","","+","+","","","-","-","-"])

		st.markdown("<h2>Sixth question:</h2>",True)

		st.markdown("<p>Do you like ai/ml and/or data science?</p>",True)

		answear6=st.radio("",["Yes","No"],key="6")

		if answear6=="Yes": functions.modify(points,["+","-","+","","","+","-","",""])

		st.markdown("<h2>Seventh question:</h2>",True)

		st.markdown("<p>Do you like Computer Vision?</p>",True)

		answear7=st.radio("",["Yes","No"],key="7")

		if answear7=="Yes": functions.modify(points,["+","-","+","","+","+","","",""])

		st.markdown("<h2>Eighth question:</h2>",True)

		st.markdown("<p>Do you like graphics?</p>",True)

		answear8=st.radio("",["Yes","No"],key="8")

		if answear8=="Yes": functions.modify(points,["","+","+","+","","+","","",""])

		st.markdown("<h2>Ninth question:</h2>",True)

		st.markdown("<p>Do you like electronics?</p>",True)

		answear9=st.radio("",["Yes","No"],key="9")

		if answear9=="Yes": functions.modify(points,["","+","+","-","-","-","","-","-"])

		st.markdown("<h2>Tenth question:</h2>",True)

		st.markdown("<p>Do you like scripting?</p>",True)

		answear10=st.radio("",["Yes","No"],key="10")

		if answear10=="Yes": functions.modify(points,["+","-","","","","+","-","+",""])

		st.markdown("<h2>Eleventh question:</h2>",True)

		st.markdown("<p>Do you like math?</p>",True)

		answear11=st.radio("",["Yes","No"],key="11")

		if answear11=="Yes": functions.modify(points,["+","+","+","-","-","-","+","",""])

		st.markdown("<h2>Twelfth question:</h2>",True)

		st.markdown("<p>Do you like competitive programming?</p>",True)

		answear12=st.radio("",["Yes","No"],key="12")

		if answear12=="Yes": functions.modify(points,["","-","","-","","","+","+",""])

		st.markdown("<h2>Thirteenth question:</h2>",True)

		st.markdown("<p>Are or you want to become a nerd/geek?</p>",True)

		answear13=st.radio("",["Yes","No"],key="13")

		if answear13=="Yes": functions.modify(points,["-","+","+","-","","-","+","-","-"])
		else: functions.modify(points,["+","-","-","+","","+","-","+","+"])

		st.markdown("<h2>Fourteenth question:</h2>",True)

		st.markdown("<p>Do you want a older programming language?</p>",True)

		answear14=st.radio("",["Yes","No"],key="14")

		if answear14=="Yes": functions.modify(points,["","+","+","","","","+","-","-"])
		else: functions.modify(points,["","-","-","","","","-","+","+"])

		st.markdown("<h2>Fifteenth question:</h2>",True)

		st.markdown("<p>Do you like Apple?</p>",True)

		answear15=st.radio("",["Yes","No"],key="15")

		if answear15=="Yes": functions.modify(points,["","-","-","","-","+","-","+","+"])

		st.markdown("<h2>Sixteenth question:</h2>",True)

		st.markdown("<p>Do you like Windows?</p>",True)

		answear16=st.radio("",["Yes","No"],key="16")

		if answear16=="Yes": functions.modify(points,["","","+","","","","","","-"])

		st.markdown("<h2>Seventeenth question:</h2>",True)

		st.markdown("<p>Hard or easy way?</p>",True)

		answear17=st.radio("",["Hard","Easy"],key="17")

		if answear17=="Hard": functions.modify(points,["-","+","+","","","-","+","",""])
		else: functions.modify(points,["+","-","-","","","+","-","",""])

		st.markdown("<h2>Eighteenth question:</h2>",True)

		st.markdown("<p>Do you like oop?</p>",True)

		answear18=st.radio("",["Yes","No","What is this?"],key="18")

		if answear18=="Yes": functions.modify(points,["","-","","+","+","","-","",""])
		elif answear18=="No": functions.modify(points,["","+","","-","-","","-","",""])

		st.markdown("<h2>Nineteenth question:</h2>",True)

		st.markdown("<p>Do you like functional programming?</p>",True)

		answear19=st.radio("",["Yes","No","What is this?"],key="19")

		if answear19=="Yes": functions.modify(points,["+","-","","-","-","+","+","+","+"])
		elif answear19=="No": functions.modify(points,["-","+","","+","+","-","-","-","-"])

		st.markdown("<h2>Twentieth question:</h2>",True)

		st.markdown("<p>Hobby or you want to get a job or you want to freelance?</p>",True)

		answear20=st.radio("",["Hobby","Job","Freelance"],key="20")

		if answear20=="Hobby": functions.modify(points,["+","","","+","+","+","-","-","+"])
		elif answear20=="Job": functions.modify(points,["+","+","","-","","+","","",""])
		elif answear20=="Freelance": functions.modify(points,["+","-","-","","+","+","-","+","+"])	

		if st.form_submit_button("Submit"):
			submit=True
			points=[(k,v) for k,v in points.items()]
			points.sort(key=lambda x: x[1],reverse=True)

	if submit:
		st.markdown(f"<h1>You got {points[0][0]} with {points[0][1]} points!<h1>",True)

		exec(f"{functions.transform(points[0][0])}()")