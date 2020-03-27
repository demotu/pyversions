# pyversions

Get versions of imported modules in current session: pyversions.versions()

Designed particularly to work within a Jupyter notebook.  
Call this function in a cell just after all modules/functions are imported.  
This function uses Python inspect module to get the caller's global namespace; it should work, if not, pass globals() as a parameter.

Installation
------------
```
pip install pyversions
```

Examples
--------
```python
>>> import pyversions
>>> vs = pyversions.versions()

>>> from pyversions import versions
>>> versions();  # semicolon to avoid printing information twice
```

Help
----
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

Version history
---------------
'0.0.1' :
    The first version

"""
```
