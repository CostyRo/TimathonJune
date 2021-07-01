import streamlit as st
import sidebar
import functions


def app():
	sidebar.sidebar()

	functions.showLogo()

	st.warning("Unfortunately most of the syntaxs highlighting don't work😔")

	language=st.selectbox("Choose the programming languageuage:",["Bash","Brainfuck","Cjam","Clojure","Cobol","Coffeescript","Cow","Crystal","Dart","Dash","Typescript","Javascript","C#","Dragon","Elixir","Emacs","Erlanguage","Awk","C","C++","D","Fortran","Go","Golfscript","Groovy","Haskell","Java","Jelly","Julia","Kotlin","Lisp","Lolcode","Lua","Nasm","Nasm64","Nim","Ocaml","Matlab","Osabie","Paradoc","Pascal","Perl","Php","Ponylanguage","Prolog","Pure","Pyth","Python2","Python","Raku","Rockstar","Ruby","Rust","Scala","Swift","V","Yeethon","Zig"])

	col1,col2=st.beta_columns(2)

	with col1:
		code=st.text_area("Write your code here: ","",250)

	with col2:
		if code=="":
			st.code("""
⠀
⠀
⠀
⠀
⠀
⠀
⠀
⠀
⠀
⠀
⠀
⠀
""",language)
		else:
			st.code(code+"".join("⠀\n" for _ in range(13-len(code.split("\n")))),language)

	if st.button("▶️ Press to run the code"):
		functions.execode(language)