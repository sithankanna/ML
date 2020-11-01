# Hyper Modern Python Packaging 
 
## Components

1. Packaging 
2. Distribution
3. Environment Management 
4. Testing
5. Enforcoing coding style 
6. CI


## Packaging, Distribution and Environment Management
* Goal is to make your functions as easy as the ones that are installed from the internet 
* Many different frameworks. Most tools have overlap in how they solve problems
* Use `wheel` as `egg` is an old build distribution format which will not be supported 
* Wheel is a new built distribution format and there are diff
    * Universal Wheel (only contains Pure Python Code that can work for Python 2 or 3)
    * Pure Python (only Python code but only has either Python 2 or Python 3)
    * Platform Wheels (only has Windows and MacOS)

[Image](assets/pyWTF_venv_diagram.png)
Diagram created by [Simone Robutti](https://chobeat.github.io/pywtf-slides/#15)


### Old method: setuptools: 
* distutils: Depricated predecassors for setuptools (Really Bad 5/5)
* setuptools: Expanded version of Setup Tools 
* Needs `setup.py` which automatically packagaes all the files in the directory with "__init__.py" 
* `MANIFEST.in` is used to list non-python files that you want to be included in the package (e.g. License file + README)
* `setup.cfg` is a config file is used - to move a lot of things from setup.py 
* `./setup.py sdist` = Creates source distribution
* `./setup.py bdist_wheel` = Creates the universal wheel 
* `./setup.py develop` or  `pip install -e` creates a simlink in your installed directory without acctually installing it. This makes the development version of your package to other projects in your computer without explicitly installing it.
* Then you need you need to upload it to `pypi` via a package called `twine`. 
* Packages listed in in `setup.py` is for the users, packages in `requirement.txt` is for developers 

## Definitions
* Module: Any Python Code (any .py file or files)
* Package is a directory of Python modules containing an additional __init__.py file
* Distribution Package (also confusingly called "package"): Sharable and installable, bundled up python code - there are source and build format
* Source Distribution: (sdist) 
* Built Distibitoon "bdist_wheel" when you intsalled 
* PyPI: Python Package Index: Repo of Python packages. *PyPIServer* can be used for interal mirror for PyPI 


## Tests 
tox.ini = To handle testing environments, runs all your tests accroding to the env specs
 (e.g. across different Python versions)



## Environment Management
* virtualenv: cli to create Virtual Env, low level tool but gives a lot control not always recommended 
* venv: Similar to venv built but for Python3 
* pipenv: Creates per project environment with pip dependecies 
* PyEnv: To juggle different Python version. Runs some shell black magic 
* For some problems containers (i.e. Docker) are better

## Poetry 
`poetry` tries to solves packaging, distribution and env management with the same framework. Still not super mature. (Possibly best option)



# Other things
* PEP stands for Python Enhancement Proposal 
* PyPI (pronounced "pai pee ai" or "pai pee" not "pai pai" which is reserved for pypy - the JIT implementation of python )
* __init__ (proniunced "dunder init dunder" or just "dunder init" )
* TOML stands for Tom's Obvious, Minimal Language. It is a data serialisation language designed to be a minimal configuration file format that's easy to read due to obvious semantics. It is an alternative to YAML and JSON. It aims to be more human friendly than JSON and simpler that YAML.
* If you use pytest with pytest cov with PyCharm's debugger, then everthing breaks. Unresolved dispute between IntelliJ and pytest developers 


# References
[venv, pyenv, pypi, pip, pipenv, pyWTF?](https://www.youtube.com/watch?v=-C8uVImkTQg)
[Lesson 8 - Python Applications Packaging with Setuptools](https://www.youtube.com/watch?v=wCGsLqHOT2I)
[Python Packaging from Init to Deploy](https://www.youtube.com/watch?v=4fzAMdLKC5k)
[Hypermodern Python](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)