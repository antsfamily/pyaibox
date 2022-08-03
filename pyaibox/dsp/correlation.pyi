def corr1(f, g, shape='same'):
    r"""Correlation.

    the correlation between f and g can be expressed as

    .. math::
        (f\star g)[n] = \sum_{m=-\infty}^{+\infty}{\overline{f[m]}g[m+n]} = \sum_{m=-\infty}^{+\infty}\overline{f[m-n]}g[m]
        :label: equ-1DCrossCorrelationDiscrete

    Parameters
    ----------
    f : numpy array
        data1
    g : numpy array
        daat2
    shape : str, optional
        - ``'full'``: returns the full correlation,
        - ``'same'``: returns the central part of the correlation
                that is the same size as f (default).
        - ``'valid'``: returns only those parts of the correlation
                that are computed without the zero-padded edges.
                LENGTH(y)is MAX(LENGTH(f)-MAX(0,LENGTH(g)-1),0).
    """

def cutfftcorr1(y, nfft, Nx, Nh, shape='same', axis=0, ftshift=False):
    r"""Throwaway boundary elements to get correlation results.

    Throwaway boundary elements to get correlation results.

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
        2. ``'valid'`` --> valid correlation output
        3. ``'full'`` --> full correlation output, :math:`N_x+N_h-1`
        (the default is 'same')
    axis : int
        correlation axis (the default is 0)
    ftshift : bool, optional
        whether to shift the frequencies (the default is False)

    Returns
    -------
    y : numpy array
        array with shape specified by :attr:`same`.
    """

def fftcorr1(x, h, shape='same', caxis=None, axis=0, keepcaxis=False, nfft=None, ftshift=False, eps=None):
    """Correlation using Fast Fourier Transformation

    Correlation using Fast Fourier Transformation.

    Parameters
    ----------
    x : numpy array
        data to be convolved.
    h : numpy array
        filter array, it will be expanded to the same dimensions of :attr:`x` first.
    shape : str, optional
        output shape:
        1. ``'same'`` --> same size as input x, :math:`N_x`
        2. ``'valid'`` --> valid correlation output
        3. ``'full'`` --> full correlation output, :math:`N_x+N_h-1`
        (the default is 'same')
    caxis : int or None
        If :attr:`x` is complex-valued, :attr:`caxis` is ignored. If :attr:`x` is real-valued and :attr:`caxis` is integer
        then :attr:`x` will be treated as complex-valued, in this case, :attr:`caxis` specifies the complex axis;
        otherwise (None), :attr:`x` will be treated as real-valued.
    axis : int, optional
        axis of correlation operation (the default is 0, which means the first dimension)
    keepcaxis : bool
        If :obj:`True`, the complex dimension will be keeped. Only works when :attr:`X` is complex-valued array 
        and :attr:`axis` is not :obj:`None` but represents in real format. Default is :obj:`False`.
    nfft : int, optional
        number of fft points (the default is None, :math:`2^{nextpow2(N_x+N_h-1)}`),
        note that :attr:`nfft` can not be smaller than :math:`N_x+N_h-1`.
    ftshift : bool, optional
        whether shift frequencies (the default is False)
    eps : None or float, optional
        x[abs(x)<eps] = 0 (the default is None, does nothing)

    Returns
    -------
    y : numpy array
        Correlation result array.

    """

def xcorr(A, B, shape='same', mod=None, axis=0):
    r"""Cross-correlation function estimates.


    Parameters
    ----------
    A : numpy array
        data1
    B : numpy array
        data2
    shape : str, optional
        output shape:
        1. ``'same'`` --> same size as input x, :math:`N_x`
        2. ``'valid'`` --> valid correlation output
        3. ``'full'`` --> full correlation output, :math:`N_x+N_h-1`
    mod : str, optional
        - ``'biased'``: scales the raw cross-correlation by 1/M.
        - ``'unbiased'``: scales the raw correlation by 1/(M-abs(lags)).
        - ``'coeff'``: normalizes the sequence so that the auto-correlations
                   at zero lag are identically 1.0.
        - :obj:`None`: no scaling (this is the default).
    """

def acorr(x, P, axis=0, scale=None):
    r"""computes auto-correlation using fft

    Parameters
    ----------
    x : tensor
        the input signal array
    P : int
        maxlag
    axis : int
        the auto-correlation dimension
    scale : str or None, optional
        :obj:`None`, ``'biased'`` or ``'unbiased'``, by default None
    """    

def accc(Sr, isplot=False):
    r"""Average cross correlation coefficient

    Average cross correlation coefficient (ACCC)

    .. math::
       \overline{C(\eta)}=\sum_{\eta} s^{*}(\eta) s(\eta+\Delta \eta)

    where, :math:`\eta, \Delta \eta` are azimuth time and it's increment.


    Parameters
    ----------
    Sr : numpy array
        SAR raw signal data :math:`N_a\times N_r` or range compressed data.

    Returns
    -------
    1d array
        ACCC in each range cell.
    """


