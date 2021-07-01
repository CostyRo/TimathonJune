import streamlit as st
import sidebar
import functions

def app():
	sidebar.sidebar()

	functions.showLogo()

	st.markdown("<h1>Here you can see a list with amazing open source projects you can contribute!</h1>",True)

	st.markdown("<h2>Python</h2>",True)

	st.markdown("""
* [Animation engine for explanatory math videos](https://github.com/3b1b/manim "Animation engine for explanatory math videos")
* [A computer algebra system written in pure Python](https://github.com/sympy/sympy "A computer algebra system written in pure Python")
* [Turn (almost) any Python command line program into a full GUI application with one line](https://github.com/chriskiehl/Gooey "Turn (almost) any Python command line program into a full GUI application with one line")
* [Magenta: Music and Art Generation with Machine Intelligence](https://github.com/magenta/magenta "Magenta: Music and Art Generation with Machine Intelligence")
* [⏬ Dumb downloader that scrapes the web](https://github.com/soimort/you-get "⏬ Dumb downloader that scrapes the web")
* [Terminal session recorder 📹](https://github.com/asciinema/asciinema "Terminal session recorder 📹")
* [Tool to scan for secret files on HTTP servers](https://github.com/hannob/snallygaster "Tool to scan for secret files on HTTP servers")
* [Just a really simple, insecure and incomplete implementation of a blockchain for a cryptocurrency made in Python as educational material. In other words, a simple Bitcoin clone.](https://github.com/cosme12/SimpleCoin "Just a really simple, insecure and incomplete implementation of a blockchain for a cryptocurrency made in Python as educational material. In other words, a simple Bitcoin clone.")
* [Magnificent app which corrects your previous console command.](https://github.com/nvbn/thefuck "Magnificent app which corrects your previous console command.")
""")

	st.markdown("<h2>C</h2>",True)

	st.markdown("""
* [The official Vim repository](https://github.com/vim/vim "The official Vim repository")
* [A text editor in less than 1000 LOC with syntax highlight and search.](https://github.com/antirez/kilo "A text editor in less than 1000 LOC with syntax highlight and search.")
* [Gravity Programming Language](https://github.com/marcobambini/gravity "Gravity Programming Language")
* [LeetCode in pure C](https://github.com/begeekmyfriend/leetcode "LeetCode in pure C")
* [A fast and lightweight IDE](https://github.com/geany/geany "A fast and lightweight IDE")
* [A self-contained cryptographic library for Python](https://github.com/Legrandin/pycryptodome "A self-contained cryptographic library for Python")
* [Go 3D Game Engine](https://github.com/g3n/engine "Go 3D Game Engine")
* [A cross-platform, open-source, pure C game engine for mobile game.](https://github.com/scottcgi/Mojoc "A cross-platform, open-source, pure C game engine for mobile game.")
* [Improved Quake III Arena engine](https://github.com/ec-/Quake3e "Improved Quake III Arena engine")
* [Real-Time ASCII Art Rendering Library](https://github.com/symisc/ascii_art "Real-Time ASCII Art Rendering Library")
""")

	st.markdown("<h2>C++</h2>",True)

	st.markdown("""
* [Godot Engine – Multi-platform 2D and 3D game engine](https://github.com/godotengine/godot "Godot Engine – Multi-platform 2D and 3D game engine")
* [A small 2d c++ game framework](https://github.com/NoelFB/blah "A small 2d c++ game framework")
""")

	st.markdown("<h2>C#</h2>",True)

	st.markdown("""
* [📚 📈 Plug-and-play class-library project of standard Data Structures and Algorithms in C#](https://github.com/aalhour/C-Sharp-Algorithms "📚 📈 Plug-and-play class-library project of standard Data Structures and Algorithms in C#")
* [C# .NET - Arduino library supporting simultaneous serial ASCII, Firmata and I2C communication](https://github.com/SolidSoils/Arduino "C# .NET - Arduino library supporting simultaneous serial ASCII, Firmata and I2C communication")
* [Short C# code snippets for all your development needs](https://github.com/30-seconds/30-seconds-of-csharp "Short C# code snippets for all your development needs")
* [Fast C# CSV parser](https://github.com/nreco/csv "Fast C# CSV parser")
* [Unity Graphics - Including Scriptable Render Pipeline](https://github.com/Unity-Technologies/Graphics "Unity Graphics - Including Scriptable Render Pipeline")
* [Bitmap & tilemap generation from a single example with the help of ideas from quantum mechanics](https://github.com/mxgmn/WaveFunctionCollapse "Bitmap & tilemap generation from a single example with the help of ideas from quantum mechanics")
""")

	st.markdown("<h2>Kotlin</h2>",True)

	st.markdown("""
* [A memory leak detection library for Android.](https://github.com/square/leakcanary "A memory leak detection library for Android.")
* [Free and open source manga reader for Android.](https://github.com/tachiyomiorg/tachiyomi "Free and open source manga reader for Android.")
* [Library support for Kotlin coroutines](https://github.com/Kotlin/kotlinx.coroutines "Library support for Kotlin coroutines")
* [🗡️ Android Pokedex using Hilt, Motion, Coroutines, Flow, Jetpack (Room, ViewModel) based on MVVM architecture.](https://github.com/skydoves/Pokedex "🗡️ Android Pokedex using Hilt, Motion, Coroutines, Flow, Jetpack (Room, ViewModel) based on MVVM architecture.")
* [A lightweight Android browser with modern navigation](https://github.com/anthonycr/Lightning-Browser "A lightweight Android browser with modern navigation")
* [Image Picker for Android 🤖](https://github.com/esafirm/android-image-picker "Image Picker for Android 🤖")
* [All Algorithms implemented in Kotlin](https://github.com/TheAlgorithms/Kotlin "All Algorithms implemented in Kotlin")
* [🧩 Kotlin coding puzzle and solutions](https://github.com/igorwojda/kotlin-coding-challenges "🧩 Kotlin coding puzzle and solutions")
* [Kotlin mathematics extensions library](https://github.com/mipt-npm/kmath "Kotlin mathematics extensions library")
* [Pure Kotlin CSV Reader/Writer](https://github.com/doyaaaaaken/kotlin-csv "Pure Kotlin CSV Reader/Writer")
""")

	st.markdown("<h2>Haskell</h2>",True)

	st.markdown("""
* [A friendly programming language from the future](https://github.com/unisonweb/unison "A friendly programming language from the future")
* [🚗 Parse and generate Rocket League replays.](https://github.com/tfausak/rattletrap "🚗 Parse and generate Rocket League replays.")
""")

	st.markdown("<h2>Java</h2>",True)

	st.markdown("""
* [Render After Effects animations natively on Android and iOS, Web, and React Native](https://github.com/airbnb/lottie-android "Render After Effects animations natively on Android and iOS, Web, and React Native")
* [MockNeat - the modern faker lib.](https://github.com/nomemory/mockneat "MockNeat - the modern faker lib.")
""")

	st.markdown("<h2>Javascript</h2>",True)

	st.markdown("""
* [📝 Minimalistic Vue-powered static site generator](https://github.com/vuejs/vuepress "📝 Minimalistic Vue-powered static site generator")
* [Prettier is an opinionated code formatter.](https://github.com/prettier/prettier "Prettier is an opinionated code formatter.")
* [📝A simple and elegant markdown editor, available for Linux, macOS and Windows.](https://github.com/marktext/marktext "📝A simple and elegant markdown editor, available for Linux, macOS and Windows.")
* [📊 A highly interactive data-driven visualization grammar for statistical charts.](https://github.com/antvis/g2 "📊 A highly interactive data-driven visualization grammar for statistical charts.")
* [🎨 Classic MS Paint, ＲＥＶＩＶＥＤ + ✨Extras](https://github.com/1j01/jspaint "🎨 Classic MS Paint, ＲＥＶＩＶＥＤ + ✨Extras")
* [High-performance Toolkit for WebGL-based Data Visualization](https://github.com/visgl/luma.gl "High-performance Toolkit for WebGL-based Data Visualization")
* [Chance - Random generator helper for JavaScript](https://github.com/chancejs/chancejs "Chance - Random generator helper for JavaScript")
* [An open source code editor for the web, written in JavaScript, HTML and CSS.](https://github.com/adobe/brackets "An open source code editor for the web, written in JavaScript, HTML and CSS.")
* [Fast, easy and reliable testing for anything that runs in a browser.](https://github.com/cypress-io/cypress "Fast, easy and reliable testing for anything that runs in a browser.")
* [A markdown parser and compiler. Built for speed.](https://github.com/markedjs/marked "A markdown parser and compiler. Built for speed.")
""")

	st.markdown("<h2>Typescript</h2>",True)

	st.markdown("""
* [Visual Studio Code](https://github.com/microsoft/vscode "Visual Studio Code")
* [JavaScript drag and drop, resizing and multi-touch gestures with inertia and snapping for modern browsers (and also IE9+)](https://github.com/taye/interact.js "JavaScript drag and drop, resizing and multi-touch gestures with inertia and snapping for modern browsers (and also IE9+)")
* [🎥 Create videos programmatically in React](https://github.com/remotion-dev/remotion "")
* [Icons for Visual Studio Code](https://github.com/vscode-icons/vscode-icons "Icons for Visual Studio Code")
* [Stories for VSCode](https://github.com/ide-stories/vscode-stories "Stories for VSCode")
* [COVID-19 global data (from JHU CSSE for now) as-a-service](https://github.com/mathdroid/covid-19-api "COVID-19 global data (from JHU CSSE for now) as-a-service")
* [Simple yet powerful framework for building command-line apps.](https://github.com/cacjs/cac "Simple yet powerful framework for building command-line apps.")
* [An SVG loader component for ReactJS](https://github.com/gilbarbara/react-inlinesvg "An SVG loader component for ReactJS")
* [MyCrypto is an open-source tool that allows you to manage your Ethereum accounts privately and securely. Developed by and for the community since 2015, we’re focused on building awesome products that put the power in people’s hands.](https://github.com/MyCryptoHQ/MyCrypto "MyCrypto is an open-source tool that allows you to manage your Ethereum accounts privately and securely. Developed by and for the community since 2015, we’re focused on building awesome products that put the power in people’s hands.")
* [📘A super fast dictionary for Chrome/Firefox](https://github.com/wtetsu/mouse-dictionary "📘A super fast dictionary for Chrome/Firefox")
""")

	st.markdown("<h2>Rust</h2>",True)

	st.markdown("""
* [A secure JavaScript and TypeScript runtime](https://github.com/denoland/deno "A secure JavaScript and TypeScript runtime")
* [A cat(1) clone with wings.](https://github.com/sharkdp/bat "A cat(1) clone with wings.")
* [Lightning Fast, Ultra Relevant, and Typo-Tolerant Search Engine](https://github.com/meilisearch/MeiliSearch "Lightning Fast, Ultra Relevant, and Typo-Tolerant Search Engine")
* [An interactive cheatsheet tool for the command-line](https://github.com/denisidoro/navi "An interactive cheatsheet tool for the command-line")
* [Spotify for the terminal written in Rust 🚀](https://github.com/Rigellute/spotify-tui "Spotify for the terminal written in Rust 🚀")
* [A Flash Player emulator written in Rust](https://github.com/ruffle-rs/ruffle "A Flash Player emulator written in Rust")
* [A work-in-progress, open-source, multi-player city simulation game.](https://github.com/citybound/citybound "A work-in-progress, open-source, multi-player city simulation game.")
* [A bunch of lints to catch common mistakes and improve your Rust code](https://github.com/rust-lang/rust-clippy "A bunch of lints to catch common mistakes and improve your Rust code")
* [📬 Easily and securely share files from the command line. A fully featured Firefox Send client.](https://github.com/timvisee/ffsend "📬 Easily and securely share files from the command line. A fully featured Firefox Send client.")
* [Count your code, quickly.](https://github.com/XAMPPRocky/tokei "Count your code, quickly.")
""")

	st.markdown("<h2>Go</h2>",True)

	st.markdown("""
* [Official Go implementation of the Ethereum protocol](https://github.com/ethereum/go-ethereum "Official Go implementation of the Ethereum protocol")
* [Delve is a debugger for the Go programming language.](https://github.com/go-delve/delve "Delve is a debugger for the Go programming language.")
* [Arbitrary-precision fixed-point decimal numbers in go](https://github.com/shopspring/decimal "Arbitrary-precision fixed-point decimal numbers in go")
* [Console progress bar for Golang](https://github.com/cheggaaa/pb "Console progress bar for Golang")
* [A cryptocurrency trading bot and framework supporting multiple exchanges written in Golang.](https://github.com/thrasher-corp/gocryptotrader "A cryptocurrency trading bot and framework supporting multiple exchanges written in Golang.")
* [📊 Code City metaphor for visualizing Go source code in 3D](https://github.com/rodrigo-brito/gocity "📊 Code City metaphor for visualizing Go source code in 3D")
* [Mergo: merging Go structs and maps since 2013.](https://github.com/imdario/mergo "Mergo: merging Go structs and maps since 2013.")
* [WhatsApp Web API](https://github.com/Rhymen/go-whatsapp "WhatsApp Web API")
* [🍕 Enjoy a slice! A utility library for dealing with slices and maps that focuses on type safety and performance.](https://github.com/elliotchance/pie "🍕 Enjoy a slice! A utility library for dealing with slices and maps that focuses on type safety and performance.")
* [A Go wrapper for the Spotify Web API](https://github.com/zmb3/spotify "A Go wrapper for the Spotify Web API")
""")