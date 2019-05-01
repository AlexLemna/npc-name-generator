# ROSEVOMIT: a name generator

This is a personal project to teach myself some programming basics. If you've stumbled across this project in search of an actually functional name generator, I highly recommend checking out [faker](https://github.com/joke2k/faker).

This program's documentation is currently spread out between this README, the `_docs_Sphinx` folder, and the [wiki](https://github.com/AlexLemna/rosevomit/wiki).

New to coding? You and me both, buddy. If you've viewing this on GitHub, you probably see this README underneath a bunch of files and folders. Those files and folders probably look something like this:

````
+ _docs_Sphinx/        <-- my (attempts at) documentation
+ Data/                <-- ROSEVOMIT's data
+ Logic/               <-- ROSEVOMIT's modules
+ .gitignore           <-- a file Git needs
+ __init__.py          <-- a file Python needs
+ LICENSE              <-- a file I need
+ README.md            <-- the file you're reading now
+ requirements.txt     <-- a file Python needs (kinda)
+ rosevomit.py         <-- ROSEVOMIT's actual code
+ setup.py             <-- A file Python needs (kinda)
````
Don't freak out - it can look intimidating, but you can see that there's only a few places you actually need to look if you want to see Rosevomit's code: the `Data` folder, the `Logic` folder, and the `rosevomit.py` file.

Hopefully, any questions you might have about Rosevomit's code can be answered either in the [wiki](https://github.com/AlexLemna/rosevomit/wiki) or in `_docs_Sphinx`. Both are works in progress - the wiki is mostly focused on what Rosevomit down the road, while Sphinx is mostly focused on documenting what exists right now. Sphinx, by the way, is [a tool](http://www.sphinx-doc.org/en/master/index.html) commonly used by Python programmers to document their projects and is totally separate from Rosevomit. I haven't done much with it yet, but if you want to look around here's a quick overview of the contents:

*EDIT: I'll be getting rid of Sphinx shortly, at least for the time being. While it's a powerful tool, I'm not sure how to use it yet and I want to focus on one thing at a time.*

````
+ _docs_Sphinx/
    +-- build/      <-- the documentation Sphinx builds
    +-- source/     <-- what Sphinx uses to document stuff
        +-- _static/
        +-- _templates/
        +-- conf.py
        +-- index.rst
    +-- make.bat
    +-- Makefile
````
