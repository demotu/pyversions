"""Get versions of all imported modules in current session: pyversions.versions()
"""

__author__ = "Marcos Duarte, https://github.com/BMClab/"
__version__ = "0.0.3"
__license__ = "MIT"

import sys
import platform
import types
import datetime
import inspect
import pkg_resources


def versions(glbs=None, show=True):
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
    '0.0.3' :
        Docs

    """
    if glbs is None:
        glbs = inspect.currentframe().f_back.f_globals
        # inspect.stack()[1][0].f_globals  # slow

    # get the imported modules
    # sys.modules is an option but it shows all modules which have been loaded,
    # not only the modules in the current jupyter notebook session
    # sys.modules is used in https://github.com/fbrundu/py_session
    def imp_mod(glbs):
        """ Yield imported modules"""
        for value in glbs.values():
            if isinstance(value, types.ModuleType):
                ver = value.__version__ if hasattr(value, '__version__') else None
                yield [value.__name__.split('.')[0], ver]
            elif isinstance(value, types.FunctionType):
                ver = value.__version__ if hasattr(value, '__version__') else None
                yield [value.__module__.split('.')[0], ver]

    # modules to ignore
    ignore = ['platform', 'json', 'pyvers']
    imp = [m for m in imp_mod(glbs) if m[0] not in ignore]
    mod = [['Module', 'Version']]
    # modules which already have __version__ (not necessarily in pip/conda)
    mod.extend([m for m in imp if m[1] is not None])
    # modules with and without __version__
    imp_v = [i[0] for i in imp if i[1] is not None]
    imp = [i[0] for i in imp if i[1] is None]
    # Some packages have different imported names vs. system/pip names or
    # are not found; add them manually as a dictionary:
    #others = {'PIL': 'Pillow', 'sklearn': 'scikit-learn'}
    others = {}
    imp.extend([others[key] for key in others if key in glbs.keys()])
    # get the ipython version if it's running interactively
    # get_ipython() returns None if no InteractiveShell instance is registered
    if 'get_ipython' in glbs.keys() and callable(glbs['get_ipython']) and glbs['get_ipython']():
        imp.append('ipython')
        # if '_Jupyter' in glbs.keys() and glbs['_Jupyter'] is glbs['get_ipython']():
        #     imp.extend(['notebook'])
        imp.extend(['notebook', 'jupyterlab'])  # just a guess
    imp = list(set(imp))
    # get other installed modules
    mod.extend([[m.project_name, m.version] for m in pkg_resources.working_set
                if m.project_name in imp and m.project_name not in imp_v])
    # or get list of installed modules from pip
    # pip = !pip freeze
    # mod.extend([m.split('==') for m in pip if m.split('==')[0] in imp])
    # Add PyQt5 if imported:
    if 'PyQt5' in glbs.keys() or 'QWidget' in glbs.keys():
        try:
            from PyQt5 import QtCore, Qt
            mod.extend([['PyQt', Qt.PYQT_VERSION_STR], ['Qt PyQt5', QtCore.QT_VERSION_STR]])
        except ImportError:
            pass
    mod[1:] = sorted(mod[1:], key=lambda x: x[0].lower())
    # environment information, force line width under 80 chars
    ver = sys.version.replace('| ', '').replace('\n', '')
    nbits = '64' if sys.maxsize > 2 ** 32 else '32'
    info = ['{} {} {}-bit {}'.format(platform.system(), platform.release(),
                                     nbits, platform.version()),
            '{} {}'.format(platform.python_implementation(), ver),
            datetime.datetime.now().strftime("%b %d %Y, %H:%M:%S")]

    if show:
        print(*info, sep='\n', end='\n\n')
        width = max([[len(m) + 4, len(d) + 4] for m, d in mod])
        lis = ['{0:<{w0}}{1:>{w1}}'.format(n, v, w0=str(width[0]),
                                           w1=str(width[1])) for n, v in mod]
        print(*lis, sep='\n')

    info.extend(mod[1:])

    return info


def _repr_html_(mod):

    html = "<table>"
    html += "<tr><th>Module</th><th>Version</th></tr>"
    for name, version in mod:
        html += "<tr><td>%s</td><td>%s</td></tr>" % (name, version)

    html += "<tr><td colspan='2'>%s</td></tr>" % \
            datetime.datetime.now().strftime("%b %d %Y, %H:%M:%S")
    html += "</table>"

    return html


if __name__ == "__main__":
    versions()
