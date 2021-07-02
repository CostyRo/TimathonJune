import images
import streamlit as st
import functions

def open_cv():
	st.markdown("<h2>Open-Cv</h2>",True)

	st.image(images.opencvImage,use_column_width="auto")

	st.markdown("<p>Open-Cv is a great library used for computer vision, you can do so many things with it, like image recognition, face recognition, image manipulation, detecting features in images, pattern maching in images. Is also available in other languages, like C++, Java, Javascript.</p>",True)

	st.markdown("<h3>Draw a square in Open-CV:</h3>",True)

	st.code("""
import numpy as np
from cv2 import cv2 as cv
#import Open-Cv and Numpy

img=np.zeros([500,500],dtype=np.uint8)
#make a black image with 500x500 resolution

img.fill(255)
#fill the image with white

cv.rectangle(img,(100,100),(400,400),(0,0,0),-1)
#draw a fill black rectangle with starting point at (100,100) and ending point at (400,400)

cv.imshow("square",img)
#display the image

cv.waitKey(0)
#wait until a key in pressed
""")

def pygame():
	st.markdown("<h2>Pygame</h2>",True)

	st.image(images.pygameImage,use_column_width="auto")

	st.markdown("<p>Pygame is a great Python library to build 2d games, it can to be used to build simple games, like pong, breakout, space inavanders, snake or you can build some amazing platformers or some amazing adventure 2d games.</p>",True)

	st.markdown("<h3>Make a game that move a square on the screen:</h3>",True)

	st.code("""
import pygame as pg
#import pygame

pg.init()
#initialise pygame

screen=pg.display.set_mode((500,500))
#define the screen

running=True
#set a variable that store the state of the program

player=pg.Rect(235,470,30,30)
#define the player as a rectangle

#make a infinite loop to keep the game running
while running:
    #check all the events
    for event in pg.event.get():
        #if a key is pressed
        if event.type==pg.KEYDOWN:
            #if the ESC key is pressed close the game
            if event.key==pg.K_ESCAPE: running=False
            #if player press left arrow key or A key move player 10 pixels left
            elif event.key==pg.K_LEFT or event.key==pg.K_a:
                player.x-=10
            #if player press right arrow key or D key move player 10 pixels right
            elif event.key==pg.K_RIGHT or event.key==pg.K_d:
                player.x+=10
            #if player press up arrow key or W key move player 10 pixels up
            elif event.key==pg.K_UP or event.key==pg.K_w:
                player.y-=10
            #if player press down arrow key or S key move player 10 pixels down
            elif event.key==pg.K_DOWN or event.key==pg.K_s:
                player.y+=10

    screen.fill((255,255,255))
    #make the screen white

    pg.draw.rect(screen,(0,0,0),player)
    #draw the player

    pg.display.flip()
    #update the screen
""")

def streamlit():
	st.markdown("<h2>Streamlit</h2>",True)

	st.image(images.streamlitImage,use_column_width="auto")

	st.markdown("<p>Streamlit is the library used for making this website, is a good library for making small websites and for making frontend for data scrience application.</p>",True)

	st.markdown("<h3>Make a simple website:</h3>",True)

	st.code("""
import streamlit as st

st.title("A simple website")
""")	

def python():
	st.markdown("<h1>Python</h1>",True)

	st.image(images.pythonImage,use_column_width="auto")

	open_cv()

	pygame()

	streamlit()

def candcpp():
	st.markdown("<h1>C/C++</h1>",True)

	st.image(images.candcppImage,use_column_width="auto")

	st.markdown("<p>C and C++ have a powerful standard library with many algorithms and data structures.</p>",True)

	st.markdown("<p>C libraries are:</p>",True)

	st.markdown("""
* <assert.h>
* <complex.h> (C99)
* <ctype.h>
* <errno.h>
* <fenv.h> (C99)
* <float.h>
* <inttypes.h> (C99)
* <iso646.h>
* <limits.h>
* <locale.h>
* <math.h>
* <setjmp.h>
* <signal.h>
* <stdalign.h> (C11)
* <stdarg.h>
* <stdatomic.h> (C11)
* <stdbool.h> (C99)
* <stddef.h>
* <stdint.h> (C99)
* <stdio.h>
* <stdlib.h>
* <stdnoreturn.h> (C11)
* <string.h>
* <tgmath.h> (C99)
* <threads.h> (C11)
* <time.h>
* <uchar.h> (C11)
* <wchar.h>
* <wctype.h>
""")

	st.markdown("<p>C++ libraries are:</p>",True)

	st.markdown("""
* <concepts> (C++20)
* <coroutine> (C++20)
* <cstdlib>
* <csignal>
* <csetjmp>
* <cstdarg>
* <typeinfo>
* <typeindex> (C++11)
* <type_traits> (C++11)
* <bitset>
* <functional>
* <utility>
* <ctime>
* <chrono> (C++11)
* <cstddef> (C++11)
* <tuple> (C++11)
* <any> (C++17)
* <optional> (C++17)
* <variant> (C++17)
* <compare> (C++20)
* <version> (C++20)
* <source_location> (C++20)
* <stacktrace> (C++23)
* <new>
* <memory>
* <scoped_allocator> (C++11)
* <memory_resource> (C++17)
* <climits>
* <cfloat>
* <cstdint> (C++11)
* <cinttypes> (C++11)
* <limits>
* <exception>
* <stdexcept>
* <cassert>
* <system_error> (C++11)
* <cerrno>
* <cctype>
* <cwctype>
* <cstring>
* <cwchar>
* <cuchar> (C++11)
* <string>
* <string_view> (C++17)
* <charconv> (C++17)
* <format> (C++20)
* <array> (C++11)
* <vector>
* <deque>
* <list>
* <forward_list> (C++11)
* <set>
* <map>
* <unordered_set> (C++11)
* <unordered_map> (C++11)
* <stack>
* <queue>
* <span> (C++20)
* <iterator>
* <ranges> (C++20)
* <algorithm>
* <execution> (C++17)
* <cmath>
* <complex>
* <valarray>
* <random> (C++11)
* <numeric>
* <ratio> (C++11)
* <cfenv> (C++11)
* <bit> (C++20)
* <numbers> (C++20)
* <locale>
* <clocale>
* <codecvt> (C++11)(deprecated in C++17)
* <iosfwd>
* <ios>
* <istream>
* <ostream>
* <iostream>
* <fstream>
* <sstream>
* <syncstream> (C++20)
* <spanstream> (C++23)
* <strstream> (deprecated in C++98)
* <iomanip>
* <streambuf>
* <cstdio>
* <filesystem> (C++17)
* <regex> (C++11)
* <atomic> (C++11)
* <thread> (C++11)
* <stop_token> (C++20)
* <mutex> (C++11)
* <shared_mutex> (C++14)
* <future> (C++11)
* <condition_variable> (C++11)
* <semaphore> (C++20)
* <latch> (C++20)
* <barrier> (C++20)
* And all C libraries
""")

def app():
	functions.preparePage()

	python()

	candcpp()