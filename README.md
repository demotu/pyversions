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

The examples are a [marimo](https://marimo.io) notebook in [docs/](https://github.com/demotu/pyversions/tree/master/docs). Click its name to open the **editable GitHub Pages version**. Click **Run all**, then edit and rerun cells to experiment. Download the Python file to keep your changes; browser edits do not update this repository.

- [pyversions](https://demotu.github.io/pyversions/pyversions_notebook.html) [![molab][molab-badge]](https://molab.marimo.io/github/demotu/pyversions/blob/master/docs/pyversions_notebook.py) [![marimo][marimo-badge]](https://marimo.app/github.com/demotu/pyversions/blob/master/docs/pyversions_notebook.py)

The notebook links to **Read saved outputs** in [docs/html/](https://demotu.github.io/pyversions/docs/html/). That page contains the saved environment and module version results and can be read without running Python. Both modes are hosted on this repository's GitHub Pages site independently of molab and marimo.app. The compact badges provide alternative interactive services; their molab links use the standard execution mode.

Editable Pages notebooks run Python through [WebAssembly](https://docs.marimo.io/guides/wasm/). They download their runtime and packages, and saved pages load display assets, so keep an Internet connection. GitHub Actions discovers notebooks, refreshes saved outputs and publishes the editable collection on every push to `master`. See [scripts/README.md](scripts/README.md) to update or preview the exports locally.

[molab-badge]: https://img.shields.io/badge/molab-334155?style=flat-square
[marimo-badge]: https://img.shields.io/badge/marimo-235b43?style=flat-square

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

Here is a suggestion to cite this software, with its concept DOI, which always resolves to the latest version (to cite a specific version, use its DOI listed on [Zenodo](https://doi.org/10.5281/zenodo.4599145)):

> Marcos Duarte. (2021). pyversions: A Python module to get versions of imported modules in current session. Zenodo. https://doi.org/10.5281/zenodo.4599145

And a possible BibTeX entry:

```tex
@software{duarte_pyversions,
  author       = {Marcos Duarte},
  title        = {{pyversions: A Python module to get versions of imported modules in current session}},
  year         = 2021,
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.4599145},
  url          = {https://doi.org/10.5281/zenodo.4599145}
}
```

## License

The non-software content of this project is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/), and the software code is licensed under the [MIT license](https://opensource.org/licenses/mit-license.php).
