# ROSEVOMIT: a name generator

This is a personal project to teach myself some programming basics. If you've stumbled across this project in search of an actually functional name generator, I highly recommend checking out [faker](https://github.com/joke2k/faker).

This program's documentation is currently spread out between this README and the [wiki](https://github.com/AlexLemna/rosevomit/wiki).

New to coding? You and me both, buddy. If you've viewing this on GitHub, you probably see this README underneath a bunch of files and folders. The file structure should be something like this:

````text
+ /core/
+   Data/              <-- ROSEVOMIT's data
+       (a bunch of data files)
+   Logic/             <-- ROSEVOMIT's modules
+       __init__.py
+       LogicController.py
+       rlRandomName.py
+       rlRepeatFunction.py
+   __init__.py
+   rosevomit.py       <-- ROSEVOMIT's main program
+ /docs/
+ .gitignore           <-- a file Git needs
+ __init__.py          <-- a file Python needs
+ LICENSE
+ README.md            <-- the file you're reading now
+ requirements.txt
+ setup.py
````

Don't freak out - it can look intimidating, but you can see that there's only a few places you actually need to look if you want to see Rosevomit's code: the `Data` folder, the `Logic` folder, and the `rosevomit.py` file.
