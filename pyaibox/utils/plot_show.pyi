def cplot(ca, lmod=None):
def plots(x, ydict, plotdir='./', xlabel='x', ylabel='y', title='', issave=False, isshow=True):
    def __init__(self, plotdir='./', xlabel='x', ylabel='y', title='', figname=None, issave=False, isshow=True):
    def __call__(self, x, ydict, figname=None):
def imshow(Xs, nrows=None, ncols=None, xlabels=None, ylabels=None, titles=None, figsize=None, outfile=None, **kwargs):
    r"""show images

    This function create an figure and show images in :math:`a` rows and :math:`b` columns.

    Parameters
    ----------
    Xs : array, list or tuple
        list/tuple of image arrays, if the type is not list or tuple, wrap it.
    nrows : int, optional
        show in :attr:`nrows` rows, by default None (auto computed).
    ncols : int, optional
        show in :attr:`ncols` columns, by default None (auto computed).
    xlabels : str, optional
        labels of x-axis
    ylabels : str, optional
        labels of y-axis
    titles : str, optional
        titles
    figsize : tuple, optional
        figure size, by default None
    outfile : str, optional
        save image to file, by default None (do not save).
    kwargs : 
        see :func:`matplotlib.pyplot.imshow`

    Returns
    -------
    plt
        plot handle
    """

