def conv1(f, g, shape='same', axis=0):
    r"""Convolution

    The convoltuion between f and g can be expressed as

    .. math::
       \begin{aligned}
       (f*g)[n] &= \sum_{m=-\infty}^{+\infty}f[m]g[n-m] \\
                &= \sum_{m=-\infty}^{+\infty}f[n-m]g[m]
       \end{aligned}
       :label: equ-1DConvDiscrete

    Parameters
    ----------
    f : numpy array
        data to be filtered, can be 2d matrix
    g : numpy array
        convolution kernel
    shape : str, optional
        - ``'full'``: returns the full convolution,
        - ``'same'``: returns the central part of the convolution
                that is the same size as x (default).
        - ``'valid'``: returns only those parts of the convolution
                that are computed without the zero-padded edges.
                LENGTH(y)is MAX(LENGTH(x)-MAX(0,LENGTH(g)-1),0).
    shape : int, optional
        convolution axis (the default is 0).
    """

def cutfftconv1(y, nfft, Nx, Nh, shape='same', axis=0, ftshift=False):
    r"""Throwaway boundary elements to get convolution results.

    Throwaway boundary elements to get convolution results.

    Parameters
    ----------
    y : numpy array
        array after ``iff``.
    nfft : int
        number of fft points.
    Nx : int
        signal length
    Nh : int
        filter length
    shape : str
        output shape:
        1. ``'same'`` --> same size as input x, :math:`N_x`
        2. ``'valid'`` --> valid convolution output
        3. ``'full'`` --> full convolution output, :math:`N_x+N_h-1`
        (the default is 'same')
    axis : int
        convolution axis (the default is 0)
    ftshift : bool, optional
        whether to shift the frequencies (the default is False)

    Returns
    -------
    y : numpy array
        array with shape specified by :attr:`same`.
    """

def fftconv1(x, h, shape='same', caxis=None, axis=0, keepcaxis=False, nfft=None, ftshift=False, eps=None):
    """Convolution using Fast Fourier Transformation

    Convolution using Fast Fourier Transformation.

    Parameters
    ----------
    x : numpy array
        data to be convolved.
    h : numpy array
        filter array, it will be expanded to the same dimensions of :attr:`x` first.
    shape : str, optional
        output shape:
        1. ``'same'`` --> same size as input x, :math:`N_x`
        2. ``'valid'`` --> valid convolution output
        3. ``'full'`` --> full convolution output, :math:`N_x+N_h-1`
        (the default is 'same')
    caxis : int or None
        If :attr:`X` is complex-valued, :attr:`caxis` is ignored. If :attr:`X` is real-valued and :attr:`caxis` is integer
        then :attr:`X` will be treated as complex-valued, in this case, :attr:`caxis` specifies the complex axis;
        otherwise (None), :attr:`X` will be treated as real-valued.
    axis : int, optional
        axis of convolution operation (the default is 0, which means the first dimension)
    keepcaxis : bool
        If :obj:`True`, the complex dimension will be keeped. Only works when :attr:`X` is complex-valued array 
        and :attr:`axis` is not :obj:`None` but represents in real format. Default is :obj:`False`.
    nfft : int, optional
        number of fft points (the default is :math:`2^{nextpow2(N_x+N_h-1)}`),
        note that :attr:`nfft` can not be smaller than :math:`N_x+N_h-1`.
    ftshift : bool, optional
        whether shift frequencies (the default is False)
    eps : None or float, optional
        x[abs(x)<eps] = 0 (the default is None, does nothing)

    Returns
    -------
    y : numpy array
        Convolution result array.

    """


