import subprocess
import sys
import types
from importlib import metadata

import pytest

from pyversions import versions


def _module(name, version=None):
    """A module object named `name`, with `__version__` if given."""
    mod = types.ModuleType(name)
    if version is not None:
        mod.__version__ = version
    return mod


def _modules(info):
    """Module/version pairs from the output of versions()."""
    return {m[0]: m[1] for m in info[3:]}


def test_import_does_not_need_pkg_resources():
    # pkg_resources was removed from setuptools and setuptools is not
    # installed by default in new environments
    code = "import sys; sys.modules['pkg_resources'] = None; import pyversions"
    subprocess.run([sys.executable, '-c', code], check=True)


def test_environment_information():
    info = versions(glbs={}, show=False)
    assert len(info) == 3
    assert sys.version.split()[0] in info[1]


def test_module_with_version_attribute():
    info = versions(glbs={'np': _module('numpy', '9.9.9')}, show=False)
    assert _modules(info) == {'numpy': '9.9.9'}


def test_module_without_version_attribute_uses_installed_distribution():
    info = versions(glbs={'pt': _module('pytest')}, show=False)
    assert _modules(info) == {'pytest': metadata.version('pytest')}


@pytest.mark.skipif(sys.version_info < (3, 10), reason='packages_distributions')
def test_import_name_different_from_distribution_name():
    # the import package `_pytest` is installed by the distribution `pytest`
    info = versions(glbs={'pt': _module('_pytest')}, show=False)
    assert _modules(info) == {'pytest': metadata.version('pytest')}


def test_version_that_is_not_a_string():
    info = versions(glbs={'m': _module('mymod', (1, 2))}, show=True)
    assert _modules(info) == {'mymod': '(1, 2)'}


def test_does_not_list_itself():
    info = versions(glbs={'versions': versions}, show=False)
    assert 'pyversions' not in _modules(info)


def test_columns_are_aligned(capsys):
    glbs = {'a': _module('a', '1.2.3.dev0+a.very.long.local.version'),
            'b': _module('longmodulename', '1')}
    versions(glbs=glbs, show=True)
    table = capsys.readouterr().out.split('\n\n')[1].strip().split('\n')
    assert len(table) == 3
    assert len({len(line) for line in table}) == 1


def test_caller_globals_by_default():
    info = versions(show=False)
    assert 'pytest' in _modules(info)  # imported at the top of this file


def test_module_imported_with_two_names_is_listed_once():
    numpy = _module('numpy', '9.9.9')
    info = versions(glbs={'numpy': numpy, 'np': numpy}, show=False)
    assert info[3:] == [['numpy', '9.9.9']]
