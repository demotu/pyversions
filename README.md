# [pyversions](https://pypi.org/project/pyversions/)

Get versions of imported modules in current session: pyversions.versions()

Designed particularly to work within a Jupyter notebook.  
Call this function in a cell just after all modules/functions are imported.  
This function uses Python inspect module to get the caller's global namespace; it should work, if not, pass globals() as a parameter.

## Installation

```bash
pip install pyversions
```

Or

```bash
conda install -c duartexyz pyversions
```

## Examples

```python
>>> import pyversions
>>> vs = pyversions.versions()

>>> from pyversions import versions
>>> versions();  # semicolon to avoid printing information twice
```

- [In a Jupyter notebook](https://github.com/demotu/pyversions/blob/master/docs/pyversions.ipynb)

## Help

```python
"""
Get versions of imported modules in current session: pyversions.versions()

Parameters
----------
glbs : globals(), optional (default=None)
    Get all the imported modules from the passed globals() namespace.
show : bool, optional (default=True)
    Whether to print information about environment and imported modules.

Returns
-------
info : list of strings
    list of strings with information about the current environment and
    imported modules.

Notes
-----
Designed particularly to work within a Jupyter notebook.
Call this function in a cell just after all modules/functions are imported.
This function uses Python inspect module to get the caller's global
namespace; it should work, if not, pass globals() as a parameter.

Based on https://stackoverflow.com/questions/40428931

Examples
--------
>>> import pyversions
>>> vs = pyversions.versions()

>>> from pyversions import versions
>>> versions();  # semicolon to avoid printing information twice

[In a Jupyter notebook](https://github.com/demotu/pyversions/blob/master/docs/pyversions.ipynb)  

Version history
---------------
'0.0.1' :
    The first version

"""
```

## How to cite this work

Here is a suggestion to cite this GitHub repository:

> Duarte, M. (2020) pyversions: A Python module to get versions of imported modules in current session. GitHub repository, <https://github.com/demotu/pyversions>.

And a possible BibTeX entry:

```tex
@misc{Duarte2020,  
    author = {Duarte, M.},
    title = {pyversions: A Python module to get versions of imported modules in current session},  
    year = {2020},  
    publisher = {GitHub},  
    journal = {GitHub repository},  
    howpublished = {\url{https://github.com/demotu/pyversions}}  
}
```

## License

The non-software content of this project is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/), and the software code is licensed under the [MIT license](https://opensource.org/licenses/mit-license.php).
