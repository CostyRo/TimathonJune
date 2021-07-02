import streamlit as st
import functions
from PIL import Image

def python():
	st.markdown("<h1>Python</h1>",True)

	st.image(Image.open("images\python.png"),use_column_width="auto")

	st.markdown("<p>Python is a great programming language which is a good starting language for beginners, it is used for many tasks, like artificial intelligence/machine learning, data science, computer vision, web/mobile/desktop development, statistics, scripting, web scraping. Python is used from teaching kids to programming to develop large applications and machine learning models.</p>",True)

	st.markdown("<p>It is a interpreted, high-level, modular, object-oriented, functional, imperative, dynamic typing programming language. Python have a grabage-colector and you don't worry about memory. Because is a interpreted and dynamic typing programming language python is a very slow programming language. You can speed up your python code using Cython/Jython or writing some functions in C/C++.</p>",True)

	st.markdown("<p>Python was released in February 1991 by Guido van Rossum. Python 2.0 was released on 16 October 2000 and Python 3.0 was released on 4 December 2008. End of life of Python 2.7 was initially set at 2015 then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3. Python was named after BBC TV show Monty Python's Flying Circus and it has nothing to do with snakes.</p>",True)

	st.markdown("<p>Python have a very friendly syntax, beginners are very confortable with this syntax, it doesn't have curly brackets, use indentation instead and also doesn't have semicolons because is an interpreted language. Python heywords are and, as, assert, break, class, continue, def, del, elif, else, except, False, finally, for, from, global, if, import, in, is, lambda, None, nonlocal, not, or, pass, raise, return, True, try, while, with, yield.</p>",True)

	st.markdown("<h2>Some Python code</h2>",True)

	st.markdown("<p>Here is a hello world Python program:</p>",True)

	st.code("print(\"Hello World!\")")

	st.markdown("<p>Here is a function that open a link in your browser:</p>",True)

	st.code("""
def openTab(link):
    import webbrowser
    webbrowser.open(link)
""")

	st.markdown("<p>Here is a function that spam a custom message:</p>",True)

	st.code("""
def spamFunction(text):
    import pyautogui
    import time

    time.sleep(5)

    while True:
        time.sleep(0.1)
        pyautogui.typewrite(test)
        pyautogui.press("enter")
""")

	st.markdown("<h2>Python special features</h2>",True)

	st.markdown("<h3>Decorators</h3>",True)

	st.markdown("<p>Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it. But before diving deep into decorators let us understand some concepts that will come in handy in learning the decorators.</p>",True)

	st.code("""
def start_and_stop(func):
    def wrapper(*args,**kwargs):
        print("start")
        var=func(*args,**kwargs)
        print("stop")
        return var
    return wrapper

@start_and_stop
def helloPeople(people):
    print(f"Hello {people}!")

if __name__=="__main__":
    helloPeople(input())
#this we will print "start" then result of the function and then "stop"
""")

	st.markdown("<h3>Generators</h3>",True)

	st.markdown("<p>Introduced with PEP 255, generator functions are a special kind of function that return a lazy iterator. These are objects that you can loop over like a list. However, unlike lists, lazy iterators do not store their contents in memory.</p>",True)

	st.code("""
def perfect_squares_generator(n):
    for i in range(n):
        yield n**2
#function that creat a generator

for i in perfect_squares_generator(50):
    print(i)
#loop the genrator, a element of a generator is available in memory only when element is evaluated

for i in [i**2 for i in range(50)]:
    print(i)
#loop a list comprehension, all elements are vailable in memory from start to finish

for i in (i**2 for i in range(50)):
    print(i)
#loop a generator expression, same as the first example
""")

	st.markdown("<h2>Python tutorials</h2>",True)

	st.video("https://youtu.be/rfscVS0vtbw")

	st.video("https://youtu.be/HGOBQPFzWKo")

	st.video("https://youtu.be/sxTmJE4k0ho")

def c():
	st.markdown("<h1>C</h1>",True)

	st.image(Image.open("images\c.png"),use_column_width="auto")

	st.markdown("<p>C is a great programming language which is hard for begginers, but it offer a good understanding of how memory works and how a computer works, it is used for embedded programming and for operatings systems.</p>",True)

	st.markdown("<p>It is a compliled, low-level, imperative, static typing programming language. In C you can manage memory very well by hand to make your programs more efficient. C is also a very fast programming language, being one of the fastest and it is one of the most important languages ever.</p>",True)

	st.markdown("<p>C was a successor of B prgramming language, it was released in 1972 by Dennis Ritchie. During the 1980s, C gradually gained popularity. It has become one of the most widely used programming languages, with C compilers from various vendors available for the majority of existing computer architectures and operating systems. It was designed to be compiled to provide low-level access to memory and language constructs that map efficiently to machine instructions, all with minimal runtime support. Despite its low-level capabilities, the language was designed to encourage cross-platform programming.</p>",True)

	st.markdown("<p>C don't have a beginner-friendly syntax, it have curly brackets and semicolons and you need to specify the type of your variables. C don't have such many keywords, the keywords are auto, break, case, char, const, continue, default, do, double, else, enum, extern, float, for, goto, if, int, long, register, return, short, signed, sizeof, static, struct, switch, typedef, union, unsigned, void, volatile, while.</p>",True)

	st.markdown("<h2>Some C code</h2>",True)

	st.markdown("<p>Here is a hello world C program:</p>",True)

	st.code("""
#include <stdio.h>

int main() 
{
   printf("Hello World!");
   return 0;
}
""","c")

	st.markdown("<p>Here is a function that calculate nth fibonacci number recursively:</p>",True)

	st.code("""
int fibonacci(int n)
{
    if(n==0) return 0;
    else if(n==1) return 1;

    return fibonacci(n-1)+fibonacci(n-2);
}
""","c")

	st.markdown("<p>Here is a function that calculate greatest common factor of two numbers:</p>",True)

	st.code("""
int cmmdc(int a,int b)
{
    int r=a%b;
    while(r!=0)
    {
        a=b;
        b=r;
        r=a%b;
    }
    return b;
}
""","c")

	st.markdown("<h2>C special features</h2>",True)

	st.markdown("<h3>Preprocessor</h3>",True)

	st.markdown("<p>The C preprocessor is the macro preprocessor for the C, Objective-C and C++ computer programming languages. The preprocessor provides the ability for the inclusion of header files, macro expansions, conditional compilation, and line control.In many C implementations, it is a separate program invoked by the compiler as the first part of translation.The language of preprocessor directives is only weakly related to the grammar of C, and so is sometimes used to process other kinds of text files.</p>",True)

	st.code("""
#include <stdio.h>

#define PI 3.14
//wherever there is a PI it will be replaced by 3,14

int main()
{
    printf("%.2f",PI);
    return 0;
}
""","c")

	st.markdown("<h3>Pointers</h3>",True)

	st.markdown("<p>Pointers are a data type which stores a memory adress. Pointers are used in many cases of daily use of C. With pointers you can modify the value of a variable without touching the variable value.</p>",True)

	st.code("""
#include <stdio.h>

int main()
{
    int var=5;
    int* pointer=&var;
    //declare a pointer to variable var

    printf("%d",var);

    *pointer+=1;
    //increase the value of the location pointed by the pointer

    printf("%d",var);
    //now the value is changed

    return 0;
}
""","c")

	st.markdown("<h2>C tutorials</h2>",True)

	st.video("https://youtu.be/KJgsSFOSQv0")

	st.video("https://youtu.be/zuegQmMdy8M")

def cpp():
	st.markdown("<h1>C++</h1>",True)

	st.image(Image.open("images\c++.png"),use_column_width="auto")

	st.markdown("<p>C++ is a great programming language which is hard for begginers because derive from C, but it offer a good understanding of how memory works and how a computer works, it is used for embedded programming, operatings systems and AAA games.</p>",True)

	st.markdown("<p>It is a compliled, low-level, imperative, object-oriented, functional, static typing programming language. In C++ you can manage memory very well by hand to make your programs more efficient. C++ is also a very fast programming language, being one of the fastest and it is also one of the most important languages ever.</p>",True)

	st.markdown("<p>C++ was released in 1985 by Bjarne Stroustrup as an extension of the C programming language, or \"C with Classes\" The C++ programming language was initially standardized in 1998 as ISO/IEC 14882:1998, which was then amended by the C++03, C++11, C++14, and C++17 standards. The current C++20 standard supersedes these with new features and an enlarged standard library. Before the initial standardization in 1998, C++ was developed by Danish computer scientist Bjarne Stroustrup at Bell Labs since 1979 as an extension of the C language; he wanted an efficient and flexible language similar to C that also provided high-level features for program organization.</p>",True)

	st.markdown("<p>C++, like C, don't have a beginner-friendly syntax, it have curly brackets and semicolons and you need to specify the type of your variables. C++ don have a lot of keywords, compared to C. Newer version of C++ have additional keywords.</p>",True)

	st.markdown("<h2>Some C++ code</h2>",True)

	st.warning("In this moment C++ syntax highlighting doesn't work, if you know how to solve this problem comment your solution here: https://discuss.streamlit.io/t/c-markdown-syntax-highlighting-doesnt-work/14106/5 !")

	st.markdown("<p>Here is a hello world C++ program:</p>",True)

	st.code("""
#include <iostream>

int main() 
{
   std::cout<<"Hello World!";
   return 0;
}
""","c")

	st.markdown("<p>Here is a simple implementation of a hash table in c++:</p>",True)

	st.code("""
class HashTable{
private:
  std::list<int> *table;
  int total_elements;
  int getHash(int key)
  {
    return key%total_elements;
  }
public:
  HashTable(int n)
  {
    total_elements=n;
    table=new std::list<int>[total_elements];
  }
  void insertElement(int key)
  {
    table[getHash(key)].push_back(key);
  }
  void removeElement(int key)
  {
    int x=getHash(key);
    std::list<int>::iterator i;
    for(i=table[x].begin();i!=table[x].end();i++)
    {
      if(*i==key)
        break;
    }
    if(i!=table[x].end())
      table[x].erase(i);
  }
  void printAll()
  {
    for(int i=0;i<total_elements;i++)
    {
      cout <<"Index "<<i<<": ";
      for(int j : table[i])
        std::cout<<j<<" => ";
      std::cout<std::<endl;
    }
  }
};
""","c")

	st.markdown("<p>Here is a simple program with a vector in c++:</p>",True)

	st.code("""
#include <iostream>
#include <vector>
 
int main()
{
    std::vector<int> v={7,5,16,8};
 
    v.push_back(25);
    v.push_back(13);
 
    std::cout<<"v={";
    for(int n : v)
    {
        std::cout<<n<<",";
    }
    std::cout<<"};";

    v.pop_back();
    v.pop_back();

    std::cout<<"v={";
    for(int n : v)
    {
        std::cout<<n<<",";
    }
    std::cout<<"};";
}
""","c")

	st.markdown("<h2>C++ special features</h2>",True)

	st.markdown("<h3>STL</h3>",True)

	st.markdown("<p>The Standard Template Library (STL) is a set of C++ template classes to provide common programming data structures and functions such as lists, stacks, arrays, etc. It is a library of container classes, algorithms, and iterators. It is a generalized library and so, its components are parameterized. A working knowledge of template classes is a prerequisite for working with STL.</p>",True)

	st.code("""
#include <iostream>
#include <vector>
 
int main()
{
    std::vector<int> v={7,5,16,8};
 
    v.push_back(25);
    v.push_back(13);
 
    std::cout<<"v={";
    for(int n : v)
    {
        std::cout<<n<<",";
    }
    std::cout<<"};";

    v.pop_back();
    v.pop_back();

    std::cout<<"v={";
    for(int n : v)
    {
        std::cout<<n<<",";
    }
    std::cout<<"};";
    //code that use a stl vector
}
""","c")

	st.markdown("<h3>Namespaces</h3>",True)

	st.markdown("<p>Namespaces provide a method for preventing name conflicts in large projects. Symbols declared inside a namespace block are placed in a named scope that prevents them from being mistaken for identically-named symbols in other scopes. Multiple namespace blocks with the same name are allowed. All declarations within those blocks are declared in the named scope.</p>",True)

	st.code("""
#include <iostream>

namespace ns1
{
    int x=100;
}

namespace ns2 
{
    int x=1000;
}
  
int main()
{
    std::cout<<ns1::x<<std::endl;
    //this will be 100
  
    std::cout<<ns2::x<<std::endl;
    //this will be 1000

    return 0;
}
""","c")

	st.markdown("<h2>C++ tutorials</h2>",True)

	st.video("https://youtu.be/vLnPwxZdW4Y")

	st.video("https://youtu.be/P2jVybFyh3A")

def cs():
	st.markdown("<h1>C#</h1>",True)

	st.image(Image.open("images\c#.png"),use_column_width="auto")

	st.markdown("<p>C# is a very used programming language in this days, it is used fro many things, like game development with Unity, desktop application development and web development with .NET framework or web devlopement direct in web assembly with Blazor.</p>",True)

	st.markdown("<p>C# is a compiled, general-purpose, multi-paradigm programming language encompassing static typing, strong typing, lexically scoped, imperative, declarative, functional, generic, object-oriented(class-based), and component-oriented programming disciplines.</p>",True)

	st.markdown("<p>C# was developed around 2000 by Microsoft as part of its .NET initiative and later approved as an international standard by Ecma (ECMA-334) in 2002 and ISO (ISO/IEC 23270) in 2003. It was designed by Anders Hejlsberg, and its development team is currently led by Mads Torgersen, being one of the programming languages designed for the Common Language Infrastructure (CLI). During the development of the .NET Framework, the class libraries were originally written using a managed code compiler system called \"Simple Managed C\" (SMC). In January 1999, Anders Hejlsberg formed a team to build a new language at the time called Cool, which stood for \"C-like Object Oriented Language\". Microsoft had considered keeping the name \"Cool\" as the final name of the language, but chose not to do so for trademark reasons. By the time the .NET project was publicly announced at the July 2000 Professional Developers Conference, the language had been renamed C#, and the class libraries and ASP.NET runtime had been ported to C#.</p>",True)

	st.markdown("<p>C# syntax is very similar with C or C++ syntax, it have only some diference, like in C# indices of an array are in a single set of square brackets.</p>",True)

	st.markdown("<h2>Some C# code</h2>",True)

	st.warning("Unfortunately C# syntax highlighting doesn't work as well! 😔")

	st.markdown("<p>Here is a hello world C# program:</p>",True)

	st.code("""
using System;

namespace myApp
{
    class Program
    {
        static void Main()
        {
            Console.WriteLine("Hello World!");
        }
    }
}
""","c")

	st.markdown("<p>Implement a bogosort in C#:</p>",True)

	st.code("""
static bool isSorted(int[] a)
{
    int i = a.Length - 1;
    if (i <= 0) return true;
    if ((i & 1) > 0) { if (a[i] < a[i - 1]) return false; i--; }
    for (int ai = a[i]; i > 0; i -= 2)
        if (ai < (ai = a[i - 1]) || ai < (ai = a[i - 2])) return false;
    return a[0] <= a[1];
}

static int bogoSort(int[] arr)
{
    while(!isSorted(arr))
    {
        Random random=new Random();
        arr=arr.OrderBy(x=>random.Next()).ToArray();
    }
    return arr
}
""","c")

	st.markdown("<p>Function that solve a second degree equation:</p>",True)

	st.code("""
static int ecuationSolver(int a, int b, int c)
{
    float delta=b*b-4*a*c;
    if(delta>0)
    {
    	float x1=(-b+Math.Sqrt(delta))/2a;
    	float x2=(-b-Math.Sqrt(delta))/2a;
        float[] arr={x1,x2};
    }
    else if(delta==0)
    {
        float x1=-b/2a
        float[] arr={x1,x1};
    }
    else
    {
        float[] arr={null,null};
    }
    return arr;
}
""","c")

	st.markdown("<h2>C# special features</h2>",True)

	st.markdown("<h3>Huh? There is something special in C#?</h3>",True)

	st.markdown("<h2>C# tutorials</h2>",True)

	st.video("https://youtu.be/GhQdlIFylQ8")

def kotlin():
	st.markdown("<h1>Kotlin</h1>",True)

	st.image(Image.open("images\kotlin.png"),use_column_width="auto")

	st.markdown("<p>Kotlin is a programming language which is designed to replace java for android development. Google make kotlin official language for android developement since 2017. Kotlin community grow fast and now kotlin support many other things, like ios app development, desktop development and web development.</p>",True)

	st.markdown("<p>Kotlin is a cross-platform, statically typed, general-purpose programming language with type inference. Kotlin is designed to interoperate fully with Java, and the JVM version of Kotlin's standard library depends on the Java Class Library, but type inference allows its syntax to be more concise.</p>",True)

	st.markdown("<p>In July 2011, JetBrains unveiled Project Kotlin, a new language for the JVM, which had been under development for a year. JetBrains lead Dmitry Jemerov said that most languages did not have the features they were looking for, with the exception of Scala. However, he cited the slow compilation time of Scala as a deficiency. One of the stated goals of Kotlin is to compile as quickly as Java. In February 2012, JetBrains open sourced the project under the Apache 2 license. The name comes from Kotlin Island, near St. Petersburg. Andrey Breslav mentioned that the team decided to name it after an island, just like Java was named after the Indonesian island of Java.</p>",True)

	st.markdown("<p>Kotlin syntax is similar with Java syntax, but is more friendly, and not as much verbose. Kotlin have hard and soft keywords, hard keywords are as, break, class, continue, do, else, false, for, fun, if,in,interface,is,null,object,package,return,super,this,throw,true,try, typealias, typeof, val, var, when, while.</p>",True)

	st.markdown("<h2>Some Kotlin code</h2>",True)

	st.warning("Unfortunately Kotlin syntax highlighting doesn't work as well! 😔")

	st.markdown("<p>Here is a hello world Kotlin program:</p>",True)

	st.code("fun main()=println(\"Hello World!\")"," ")

	st.markdown("<p>Kotlin WTF moment:</p>",True)

	st.code("""
fun main()
{
    val l1=listOf("a")
    val l2=listOf("a")
    var x=(l1==l2)//=>true
    println(x)

    val a1=arrayOf("a")
    val a2=arrayOf("a")
    var y=(a1==a2)//=>false
    println(y)
}
"""," ")

	st.markdown("<p>Solution to \"Cat years, Dog years\" from codewars:</p>",True)

	st.code("""
package solution
fun calculateYears(years: Int)=arrayOf(years,if(years==1) 15 else if(years==2) 24 else 24+(years-2)*4,if(years==1) 15 else if(years==2) 24 else 24+(years-2)*5);
"""," ")

	st.markdown("<h2>Kotlin special features</h2>",True)

	st.markdown("<h3>Data classes</h3>",True)

	st.markdown("<p>Classes that are use just for storing data, like a C struct, you don't need to make getters and setters for this, like in Java.</p>",True)

	st.code("""
data class ChessPiece(val col: Int,val row: Int,val player: ChessPlayer,
val rank: ChessRank,val resID: Int,val wasPlayed: Boolean=false){}
"""," ")

	st.markdown("<h3>Null Safety</h3>",True)

	st.markdown("<p>Kotlin aims at eliminating the risk of NullPointerException. It distinguishes between nullable and non-nullable references as a part of its type system. In Kotlin, all variables are non-nullable by default. So, we cannot assign a null value to a variable because it’ll throw a compilation error. To define a nullable variable, we must append a question mark(?) to the type declaration. We can call a method or access a property on a non-nullable variable. However, in the case of nullable variables, we need to handle the null case explicitly. Otherwise, it will throw a compilation error since Kotlin knows that the variable contains null references.</p>",True)

	st.code("""
var str="string"
str=null//you can't do that
var str1:String?="string"
star=null//you can do this
var str2:String?="null"
val len=str2.length//compile error, because is a string that accept null type
"""," ")

	st.markdown("<h2>Kotlin tutorials</h2>",True)

	st.video("https://youtu.be/F9UC9DY-vIU")

	st.video("https://youtu.be/5flXf8nuq60")

def haskell():
	st.markdown("<h1>Haskell</h1>",True)

	st.image(Image.open("images\haskell.png"),use_column_width="auto")

	st.markdown("<p>Haskell is a great programming language to learn functional programming, it is don't used so much in development.</p>",True)

	st.markdown("<p>Haskell is a general-purpose, statically typed, purely functional programming language with type inference and lazy evaluation. Designed for teaching, research and industrial application, Haskell has pioneered a number of advanced programming language features such as type classes, which enable type-safe operator overloading. Haskell's main implementation is the Glasgow Haskell Compiler(GHC). It is named after logician Haskell Curry.</p>",True)

	st.markdown("<p>Following the release of Miranda by Research Software Ltd. in 1985, interest in lazy functional languages grew. By 1987, more than a dozen non-strict, purely functional programming languages existed. Miranda was the most widely used, but it was proprietary software. At the conference on Functional Programming Languages and Computer Architecture(FPCA '87) in Portland, Oregon, there was a strong consensus that a committee be formed to define an open standard for such languages. The committee's purpose was to consolidate existing functional languages into a common one to serve as a basis for future research in functional-language design.</p>",True)

	st.markdown("<p>Pattern matching consists of specifying patterns to which some data should conform and then checking to see if it does and deconstructing the data according to those patterns. When defining functions, you can define separate function bodies for different patterns. This leads to really neat code that's simple and readable. You can pattern match on any data type — numbers, characters, lists, tuples, etc.</p>",True)

	st.markdown("<h2>Some Haskell code</h2>",True)

	st.markdown("<p>Here is a hello world Haskell program:</p>",True)

	st.code("""
main=putStrLn "Hello World!"
""","")

	st.markdown("<p>Solution to \"String repeat\" from codewars:</p>",True)

	st.code("""
module StringRepeat where

repeatStr :: Int -> String -> String
repeatStr 1 string=string
repeatStr n string=string ++ repeatStr (n-1) string
""","")

	st.markdown("<p>Bmi calculator in haskell:</p>",True)

	st.code("""
calculate :: Float -> Float -> Float
calculate w h=w/(h*h)

bmi :: Float -> Float -> String  
bmi w h =
  if (calculate w h)<=18.5 then "Underweight"
  else if (calculate w h)<=25.0 then "Normal"
  else if (calculate w h)<= 30.0 then "Overweight"
  else "Obese"
""","")

	st.markdown("<h2>Haskell special features</h2>",True)

	st.markdown("<h3>Recursion is powerful</h3>",True)

	st.markdown("<p>Haskell doesn't have loops, so you are forced to use recursion, in Haskell recursion is optimized against recursion in other programming languages. If you use Haskell you are one more reason to learn or to improve your recursion skill.</p>",True)

	st.code("""
factorial :: Integer -> Integer
factorial 0=1
factorial n=n*factorial (n-1)
""","")

	st.markdown("<h3>Lazy evaluation</h3>",True)

	st.markdown("<p>Haskell is a lazy programming language, it evaluate a expression or calculate something only when it needs to do, like generators from Python.</p>",True)

	st.code("""
main=do
  n<-readLn
  if even n
  then print (countDigits (product [1..n]))
  else return ()

countDigits :: Natural -> Int
countDigits n=if n<10 then 1 else 1+countDigits (n `quot` 10)

{-
$ echo 100000 | time ./compute  
456574
./compute  19.79s user 0.11s system 99% cpu 19.901 total

$ echo 100001 | time ./compute
./compute  0.00s user 0.00s system 90% cpu 0.001 total
you can see how haskell do calculation only when n is even, when n is odd it do nothing
-}
""","")

	st.markdown("<h2>Haskell tutorials</h2>",True)

	st.video("https://youtu.be/02_H3LjqMr8")

def app():
	functions.preparePage()

	python()

	c()

	cpp()

	cs()

	kotlin()

	haskell()