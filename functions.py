import streamlit as st
from PIL import Image
from pistonapi import PistonAPI

def showLogo():
    st.image(Image.open("images\logo.png"))

def execode(language,code):
    piston = PistonAPI()
    if language=="Bash":
        st.code(piston.execute("sh","5.1.0",code))
    elif language=="Brainfuck":
        st.code(piston.execute("bf","2.7.3",code))
    elif language=="Cjam":
        st.code(piston.execute("cjam","0.6.5",code))
    elif language=="Clojure":
        st.code(piston.execute("clj","1.10.3",code))
    elif language=="Cobol":
        st.code(piston.execute("cob","3.1.2",code))
    elif language=="Coffeescript":
        st.code(piston.execute("coffee","2.5.1",ode=code))
    elif language=="Cow":
        st.code(piston.execute("cow","1.0.0",code))
    elif language=="Crystal":
        st.code(piston.execute("cr","0.36.1",code))
    elif language=="Dart":
        st.code(piston.execute("dart","2.12.1",code))
    elif language=="Dash":
        st.code(piston.execute("dash","0.5.11",code))
    elif language=="Typescript":
        st.code(piston.execute("ts","4.2.3",code))
    elif language=="Javascript":
        st.code(piston.execute("js","15.10.0",code))
    elif language=="C#":
        st.code(piston.execute("cs","5.0.201",code))
    elif language=="Dragon":
        st.code(piston.execute("dragon","1.9.8",code))
    elif language=="Elixir":
        st.code(piston.execute("exs","1.11.3",code))
    elif language=="Emacs":
        st.code(piston.execute("el","27.1.0",code))
    elif language=="Erlang":
        st.code(piston.execute("erl","23.0.0",code))
    elif language=="Awk":
        st.code(piston.execute("awk","5.1.0",code))
    elif language=="C":
        st.code(piston.execute("c","10.2.0",code))
    elif language=="C++":
        st.code(piston.execute("c++","10.2.0",code))
    elif language=="D":
        st.code(piston.execute("d","10.2.0",code))
    elif language=="Fortran":
        st.code(piston.execute("f90","10.2.0",code))
    elif language=="Go":
        st.code(piston.execute("go","1.16.2",code))
    elif language=="Golfscript":
        st.code(piston.execute("golfscript","1.0.0",code))
    elif language=="Groovy":
        st.code(piston.execute("gvy","3.0.7",code))
    elif language=="Haskell":
        st.code(piston.execute("hs","9.0.1",code))
    elif language=="Java":
        st.code(piston.execute("java","15.0.2",code))
    elif language=="Jelly":
        st.code(piston.execute("jelly","0.1.31",code))
    elif language=="Julia":
        st.code(piston.execute("jl","1.6.1",code))
    elif language=="Kotlin":
        st.code(piston.execute("kt","1.4.31",code))
    elif language=="Lisp":
        st.code(piston.execute("cl","2.1.2",code))
    elif language=="Lolcode":
        st.code(piston.execute("lol","0.11.2",code))
    elif language=="Lua":
        st.code(piston.execute("lua","5.4.2",code))
    elif language=="Nasm":
        st.code(piston.execute("asm","2.15.5",code))
    elif language=="Nasm64":
        st.code(piston.execute("asm64","2.15.5",code))
    elif language=="Nim":
        st.code(piston.execute("nim","1.4.4",code))
    elif language=="Ocaml":
        st.code(piston.execute("ml","4.12.0",code))
    elif language=="Matlab":
        st.code(piston.execute("m","6.2.0",code))
    elif language=="Osabie":
        st.code(piston.execute("osabie","1.0.1",code))
    elif language=="Paradoc":
        st.code(piston.execute("paradoc","0.6.0",code))
    elif language=="Pascal":
        st.code(piston.execute("pp","3.2.0",code))
    elif language=="Perl":
        st.code(piston.execute("pl","5.26.1",code))
    elif language=="Php":
        st.code(piston.execute("php","8.0.2",code))
    elif language=="Ponylang":
        st.code(piston.execute("pony","0.39.0",code))
    elif language=="Prolog":
        st.code(piston.execute("plg","8.2.4",code))
    elif language=="Pure":
        st.code(piston.execute("pure","0.68.0",code))
    elif language=="Pyth":
        st.code(piston.execute("pyth","1.0.0",code))
    elif language=="Python2":
        st.code(piston.execute("py2","2.7.18",code))
    elif language=="Python":
        st.code(piston.execute("py","3.9.4",code))
    elif language=="Raku":
        st.code(piston.execute("p6","6.100.0",code))
    elif language=="Rockstar":
        st.code(piston.execute("rockstar","1.0.0",code))
    elif language=="Ruby":
        st.code(piston.execute("rb","3.0.1",code))
    elif language=="Rust":
        st.code(piston.execute("rs","1.50.0",code))
    elif language=="Scala":
        st.code(piston.execute("sc","3.0.0",code))
    elif language=="Swift":
        st.code(piston.execute("swift","5.3.3",code))
    elif language=="Vlang":
        st.code(piston.execute("v","0.1.13",code))
    elif language=="Yeethon":
        st.code(piston.execute("yeethon","3.10.0",code))
    elif language=="Zig":
        st.code(piston.execute("zig","0.8.0",code))