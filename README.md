# Hello World
<!-- To Do

0. Setup Python in the this mac
1. Do Hypermodern Python Tutorial 
2. Setup Pre-commit hooks
3. 


 -->



 # venv, pyenv, pypi, pip, pipenv, pyWTF

 1. Stick to the "beaten" path 

 2. Most tools have overlap in how they solve problems


3. Problems you want to solve

1. Packaging 
2. Distribution
3. Environment Management 
4. Testing
5. Enforcoing coding style 



Goal is to make your functions as easy as the ones that are installed from the internet 



egg files are bad
wheel feel are better



Packaging, Distribution and Environment Management 









The old 
Distutils: Depricated predecassors for setuptools (Really Bad 5/5)
Setuptools: Expanded version of Setup Tools 

Needs: setup.py which automatically packagaes all the files in the directory with "__init__.py" 
Manifest.in is used to list non-python files that you want to be included in the package 

python setup.py sdist
then you need you need to upload it to pypi via a package called twine 

Packaging Application with Setup Tools

python setup.py develop 
makes the development version of your package to other projects in your computer without explicitly installing it. This is done by creating a symbolic link 

[Lesson 8 - Python Applications Packaging with Setuptools](https://www.youtube.com/watch?v=wCGsLqHOT2I)




Definition

* Module: Any Python Code (any .py file or files)
* Package is a directory of Python modules containing an additional __init__.py file
* Distribution Package (also confusingly called "package"): Sharable and installable, bundled up python code - there are source and build format
* Source Distribution: (sdist) 
* Built Distibitoon "bdist_wheel" when you intsalled 

* Egg is an old built distribution format which will not be supported distribution 



Wheel is a new built distribution forma
* Universal Wheel (only contains Pure Python Code that can work for P)
* Pure Python (only Python code but only has either Python 2 or Python 3)
* Platform Wheels (only has Windows and MacOS)


PyPI (pronounced "pai pee ai" or "pai pee" not "pai pai" which is reserved for pypy - the JIT implementation of python )
* Python Package Index: Repo of Python 
* PyPIServer for interal setup for 

"Setup Tools" 
setup.cfg is a config file is used - to move a lot of things from setup.py 
MANFISET. - Lisencse and readme but not code/data
README = used as an index page on, also can be used as a pyPI 
You can tell what licese


__init__ (proniunced "dunder init dunder" or just "dunder init" )


./setup.py sdist = Creates source distribution
./setup.py bdist_wheel = Creates the universal wheel 

"./setup.py develop" or  "pip install -e" creates a simlink in your installed directory without acctually installing it 


Tests 
tox.ini = Test runner that runne


package in setup.py is for the users, packages in requirment.txt is for developers 


wheel, twine, tox (Test Runner)



Tox creates virtual environments and runs things in the virtual environemtne 
So your CI can run the package in every environment 


Viitrual Env vs PyEnv 


[Python Packaging from Init to Deploy](https://www.youtube.com/watch?v=4fzAMdLKC5k)


pip = distribution 

virtualenv: Cli to create Virtual Env, low level tool but gives a lot control not always recommended 

venv: Similar to venv built for Python3 

pipenv: Creates per project environment with dependecies 

PyEnv: To juggle different Python version. Runs some shell black magic 

For some problems containers are better

poetry: tries to solves packaging, distribution and env management with the same framework. Still not super mature. (Possibly best option)

tox: to handle testing environments, runs all your tests accroding to the env specs

If you use pytest with pytest cov with PyCharm's debugger, then everthing breaks. Unresolved dispute 


[venv, pyenv, pypi, pip, pipenv, pyWTF?]()
https://www.youtube.com/watch?v=-C8uVImkTQg


[Image](assets/pyWTF_venv_diagram)


Reference: Simone Robutti

https://chobeat.github.io/pywtf-slides/#15



What is PEP

PEP stands for Python Enhancement Proposal 







TOML stands for Tom's Obvious, Minimal Language. It is a data serialisation language designed to be a minimal configuration file format that's easy to read due to obvious semantics. It is an alternative to YAML and JSON. It aims to be more human friendly than JSON and simpler that YAML.
