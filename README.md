jgutils: A Python Utility Module
=

This package is currently targeting Python3.7+ but it *should work with Python3.6+.

Installation
==
```bash
pip install jgutils
```

Get Files (getfiles)
==
* todo: add wild-card support
* todo: tests

File listing utility. Basic matching and sorting.

Natural Sort (naturalsort)
==
* todo: more tests

Sorting for Humans; Two Modes
```python
mylist = ['elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13', 'elm']
mode1 =  ['elm', 'elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13']
mode2 =  ['elm', 'elm0', 'elm1', 'Elm2', 'elm9', 'elm10', 'Elm11', 'Elm12', 'elm13']

mylist1 = ['e0lm', 'e1lm', 'E2lm', 'e9lm', 'e10lm', 'E12lm', 'e13lm', 'elm', 'e01lm']
mode1 =   ['e0lm', 'e1lm', 'e01lm', 'E2lm', 'e9lm', 'e10lm', 'E12lm', 'e13lm', 'elm']
mode2 =   ['elm', 'e0lm', 'e1lm', 'E2lm', 'e9lm', 'e01lm', 'e10lm', 'E12lm', 'e13lm']
```

Persistent Dictionary (persistentdict)
==
* todo: more tests

In-Memory dictionary with transparent disk-based backing.

Replace (replace)
==
Based on the built-in replace.
Accepts a list of 'old' substrings to be replaced by a single 'new' substring.

Varprint (varprint)
==
Prints the name of the variable and the value.
 
```bash
[<variable_name>]<variable_type>(<variable_length>): <variable_content>
[a] (8): some_var
```

References
==
* [Python](https://www.python.org/)
* [Python-Packaging](https://python-packaging.readthedocs.io/en/latest/) 
* [Python Packaging Tutorial](https://packaging.python.org/tutorials/packaging-projects/)
* [Python List Classifiers](https://pypi.org/pypi?%3Aaction=list_classifiers)
* [GitHub](https://github.com/jerodg/jgutils)
* [Pypi](https://pypi.org/project/jgutils/)
