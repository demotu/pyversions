# [pyversions](https://pypi.org/project/pyversions/)

[![PyPI version](https://badge.fury.io/py/pyversions.svg)](https://badge.fury.io/py/pyversions)
[![DOI](https://zenodo.org/badge/250615934.svg)](https://zenodo.org/badge/latestdoi/250615934)

Get versions of imported modules in current session: pyversions.versions()

Designed particularly to work within a Jupyter or [marimo](https://marimo.io) notebook.  
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

More examples are in a [marimo](https://marimo.io) notebook in the [docs](https://github.com/demotu/pyversions/tree/master/docs) directory. Run it in your browser, no installation needed:

| Notebook | molab | marimo.app |
|---|---|---|
| [pyversions](https://molab.marimo.io/github/demotu/pyversions/blob/master/docs/pyversions_notebook.py) | [![Open in molab](https://marimo.io/molab-shield.svg)](https://molab.marimo.io/github/demotu/pyversions/blob/master/docs/pyversions_notebook.py/wasm) | [![Open with marimo](https://marimo.io/shield.svg)](https://marimo.app/github.com/demotu/pyversions/blob/master/docs/pyversions_notebook.py) |

The notebook name links to a static preview with the outputs; the badges run the notebook in your browser with [WebAssembly](https://docs.marimo.io/guides/wasm/).

Or run it locally:

```bash
uvx marimo edit --sandbox docs/pyversions_notebook.py
```

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
Designed particularly to work within a Jupyter or marimo notebook.
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

[In a marimo notebook](https://github.com/demotu/pyversions/blob/master/docs/pyversions_notebook.py)

Version history
---------------
'0.0.4' :
    Use importlib.metadata (pkg_resources was removed from setuptools)
    Find the distribution of modules whose import name is different
    Fix the alignment of the columns and versions that are not strings
    A module imported with different names is listed once
'0.0.3' :
    Docs

"""
```

## How to cite this work

Here is a suggestion to cite this GitHub repository:

> Marcos Duarte. (2021). pyversions: A Python module to get versions of imported modules in current session (Version v0.0.3). Zenodo. http://doi.org/10.5281/zenodo.4599146

And a possible BibTeX entry:

```tex
@software{marcos_duarte_2021_4599146,
  author       = {Marcos Duarte},
  title        = {{pyversions: A Python module to get versions of 
                   imported modules in current session}},
  month        = mar,
  year         = 2021,
  publisher    = {Zenodo},
  version      = {v0.0.3},
  doi          = {10.5281/zenodo.4599146},
  url          = {https://doi.org/10.5281/zenodo.4599146}
}
```

## License

The non-software content of this project is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/), and the software code is licensed under the [MIT license](https://opensource.org/licenses/mit-license.php).
