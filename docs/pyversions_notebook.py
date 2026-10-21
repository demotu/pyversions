# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "marimo",
#     "matplotlib",
#     "numpy",
#     "pyversions",
#     "scipy",
# ]
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # pyversions

    A Python module to get versions of imported modules in current session.
    [https://github.com/demotu/pyversions](https://github.com/demotu/pyversions)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Installation

    ```bash
    pip install pyversions
    ```

    Or

    ```bash
    conda install -c duartexyz pyversions
    ```

    To run this [marimo](https://marimo.io) notebook in an isolated environment with all its dependencies:

    ```bash
    uvx marimo edit --sandbox pyversions_notebook.py
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Examples

    Call `versions()` after all modules are imported; it prints information about the environment and the versions of the imported modules, and returns the same information as a list:
    """)
    return


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import scipy
    from scipy import signal

    import pyversions

    return mo, pyversions


@app.cell
def _(pyversions):
    info = pyversions.versions()
    return (info,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The returned list has the operating system, the Python version, the date, and the name and version of each module:
    """)
    return


@app.cell
def _(info):
    info
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pass a dictionary of names and modules (for example, `globals()`) to get the versions of other modules, and set `show=False` to not print:
    """)
    return


@app.cell
def _(pyversions):
    import json
    import statistics

    import numpy

    pyversions.versions(glbs={'numpy': numpy, 'statistics': statistics}, show=False)
    return


if __name__ == "__main__":
    app.run()
