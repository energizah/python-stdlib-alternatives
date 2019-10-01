# Python standard library alternatives

A collection of third-party alternatives to Python standard library modules.
### [ast](https://docs.python.org/3/library/ast.html)
- [parso](https://parso.readthedocs.io/en/latest/): Parso is a Python parser that supports error recovery and round-trip parsing for different Python versions (in multiple Python versions). Parso is also able to list multiple syntax errors in your python file. 
- [libcst](https://libcst.readthedocs.io/en/latest/): LibCST parses Python 3.7 source code as a CST tree that keeps all formatting details (comments, whitespaces, parentheses, etc). It’s useful for building automated refactoring (codemod) applications and linters. 
- [awpa](https://github.com/pyga/awpa): A working Python AST 

### [asyncio](https://docs.python.org/3/library/asyncio.html)
- [trio](https://trio.readthedocs.io/en/stable/): The Trio project’s goal is to produce a production-quality, permissively licensed, async/await-native I/O library for Python. 
- [twisted](https://twistedmatrix.com/trac/): Twisted is an event-driven networking engine written in Python and licensed under the open source ​MIT license. 

### [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html)
- [dask](https://dask.readthedocs.io/en/latest/): Dask is a flexible library for parallel computing in Python. 

### [configparser](https://docs.python.org/3/library/configparser.html)
- [toml](https://pypi.org/project/toml/): A Python library for parsing and creating TOML. 

### [ctypes](https://docs.python.org/3/library/ctypes.html)
- [cffi](https://cffi.readthedocs.io/en/latest/): C Foreign Function Interface for Python. 

### [curses](https://docs.python.org/3/library/curses.html)
- [blessed](https://github.com/jquast/blessed): Blessed is a thin, practical wrapper around terminal capabilities in Python. 
- [urwid](http://urwid.org/): Console user interface library for Python 
- [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit/): prompt_toolkit is a library for building powerful interactive command line applications in Python. 

### [dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [attrs](http://www.attrs.org/en/stable/): attrs is the Python package that will bring back the joy of writing classes by relieving you from the drudgery of implementing object protocols (aka dunder methods). 

### [datetime](https://docs.python.org/3/library/datetime.html)
- [pendulum](https://pendulum.eustace.io): Pendulum is a Python package to ease datetimes manipulation. 

### [doctest](https://docs.python.org/3/library/doctest.html)
- [pytest-sphinx](https://github.com/thisch/pytest-sphinx): A doctest plugin for pytest, which understands the sphinx-specific directives from doctest-sphinx. 

### [getopt](https://docs.python.org/3/library/getopt.html)
- [click](https://click.palletsprojects.com/en/7.x/): Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. 

### [getpass](https://docs.python.org/3/library/getpass.html)
- [click](https://click.palletsprojects.com/en/7.x/): Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. 
- [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit/): prompt_toolkit is a library for building powerful interactive command line applications in Python. 

### [glob](https://docs.python.org/3/library/glob.html)
- [pathlib](https://docs.python.org/3/library/pathlib.html): This module offers classes representing filesystem paths with semantics appropriate for different operating systems. 

### [logging](https://docs.python.org/3/library/logging.html)
- [eliot](https://eliot.readthedocs.io/en/stable/): Eliot: Logging that tells you why it happened 
- [structlog](http://www.structlog.org/en/stable/): structlog makes logging in Python less painful and more powerful by adding structure to your log entries. 

### [optparse](https://docs.python.org/3/library/optparse.html)
- [click](https://click.palletsprojects.com/en/7.x/): Click is a Python package for creating beautiful command line interfaces in a composable way with as little code as necessary. 

### [os.path](https://docs.python.org/3/library/os.path.html)
- [pathlib](https://docs.python.org/3/library/pathlib.html): This module offers classes representing filesystem paths with semantics appropriate for different operating systems. 

### [pdb](https://docs.python.org/3/library/pdb.html)
- [pudb](https://github.com/inducer/pudb): PuDB is a full-screen, console-based visual debugger for Python. 

### [re](https://docs.python.org/3/library/re.html)
- [regex](https://pypi.org/project/regex/): This regex implementation is backwards-compatible with the standard ‘re’ module, but offers additional functionality. 

### [readline](https://docs.python.org/3/library/readline.html)
- [prompt_toolkit](https://github.com/prompt-toolkit/python-prompt-toolkit/): prompt_toolkit is a library for building powerful interactive command line applications in Python. 

### [sched](https://docs.python.org/3/library/sched.html)
- [apscheduler](https://apscheduler.readthedocs.io/en/latest/): Advanced Python Scheduler (APScheduler) is a Python library that lets you schedule your Python code to be executed later, either just once or periodically. 

### [select](https://docs.python.org/3/library/select.html)
- [trio](https://trio.readthedocs.io/en/stable/): The Trio project’s goal is to produce a production-quality, permissively licensed, async/await-native I/O library for Python. 
- [twisted](https://twistedmatrix.com/trac/): Twisted is an event-driven networking engine written in Python and licensed under the open source ​MIT license. 

### [sqlite3](https://docs.python.org/3/library/sqlite3.html)
- [sqlalchemy](https://www.sqlalchemy.org/): SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. 

### [statistics](https://docs.python.org/3/library/statistics.html)
- [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html): This module contains a large number of probability distributions as well as a growing library of statistical functions. 

### [unittest](https://docs.python.org/3/library/unittest.html)
- [pytest](https://pytest.org/en/latest/): The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries. 

### [urllib.request](https://docs.python.org/3/library/urllib.request.html)
- [requests](https://python-requests.org/en/master/): Requests is an elegant and simple HTTP library for Python, built for human beings. 

### [xml](https://docs.python.org/3/library/xml.html)
- [lxml](https://pypi.org/project/lxml/): The most feature-rich and easy-to-use library for processing XML and HTML in the Python language. 

### [zipapp](https://docs.python.org/3/library/zipapp.html)
- [pex](https://github.com/pantsbuild/pex/): A library and tool for generating .pex (Python EXecutable) files 
- [shiv](https://github.com/linkedin/shiv): shiv is a command line utility for building fully self contained Python zipapps as outlined in PEP 441, but with all their dependencies included. 
