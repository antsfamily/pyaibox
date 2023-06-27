def sinc_table(Nq, Ns):
    ...

def sinc_interp(xin, r=1.0):
    ...

def interp(x, xp, yp, mod='sinc'):
    """interpolation

    interpolation

    Parameters
    ----------
    x : array_like
        The x-coordinates of the interpolated values.

    xp : 1-D sequence of floats
        The x-coordinates of the data points, must be increasing if argument
        `period` is not specified. Otherwise, `xp` is internally sorted after
        normalizing the periodic boundaries with ``xp = xp % period``.

    yp : 1-D sequence of float or complex
        The y-coordinates of the data points, same length as `xp`.

    mod : str, optional
        ``'sinc'`` : sinc interpolation (the default is 'sinc')

    Returns
    -------
    y : float or complex (corresponding to fp) or ndarray
        The interpolated values, same shape as `x`.

    """

def sinc(x):
    ...


