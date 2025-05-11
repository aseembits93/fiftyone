"""Pytorch Sphinx theme.

From https://github.com/shiftlab/pytorch_sphinx_theme.

"""
from os import path

__version__ = "0.0.24+voxel51"
__version_full__ = __version__


def get_html_theme_path():
    """Return list of HTML theme paths."""
    # Compute the parent directory of the parent of this file
    cur_dir = _parent_dir_n_times(__file__, 2)
    return cur_dir


# See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
def setup(app):
    app.add_html_theme(
        "pytorch_sphinx_theme", path.abspath(path.dirname(__file__))
    )


def _parent_dir_n_times(p, n):
    for _ in range(n):
        p = p.rpartition(path.sep)[0]
        if not p:
            p = path.sep
            break
    return p
