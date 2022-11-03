def awgns(x, snrv, **kwargs):
    """adds white gaussian noise to signal

    see `Adding noise with a desired signal-to-noise ratio <https://sites.ualberta.ca/~msacchi/SNR_Def.pdf>`_ .

    Parameters
    ----------
    x : tensor
        The pure signal data.
    snrv : int or float
        The signal-to-noise ratio value in dB.
    caxis : None or int, optional
        If :attr:`x` is complex-valued but represented in real format, 
        :attr:`caxis` or :attr:`cdim` should be specified. If not, it's set to :obj:`None`, 
        which means :attr:`x` is real-valued or complex-valued in complex format.
    keepcaxis : int or None, optional
        keep the complex dimension?
    axis : int or None, optional
        Specifies the dimensions for adding noise, if not specified, it's set to :obj:`None`, 
        which means all the dimensions.
    seed : int or None, optional
        Specifies the seed for generating random noise, if not specified, it's set to :obj:`None`.
    extra : bool, optional
        If :obj:`True`, noise will also be returned.

    Returns
    -----------
    y : tensor
        The SNRs.
    
    see :func:`awgns2`.

    Examples
    ---------

    ::

        import torch as th
        import pyaibox as pb

        pb.setseed(2020)
        x = np.random.randn(5, 2, 3, 4)
        x = pb.r2c(x, caxis=1)  # 5, 3, 4
        y, n = awgns(x, 30, axis=(1, 2), seed=2022, extra=True)
        snrv = pb.snr(y, n, axis=(1, 2))
        print(snrv, 'complex-valued in complex-format')
        
        pb.setseed(2020)
        x = np.random.randn(5, 2, 3, 4)
        y, n = awgns(x, 30, caxis=1, keepcaxis=False, axis=(1, 2), seed=2022, extra=True)
        snrv = pb.snr(y, n, caxis=1, keepcaxis=False, axis=(1, 2))
        print(snrv, 'complex-valued in real-format')

        pb.setseed(2020)
        x = np.random.randn(5, 2, 3, 4)
        y, n = awgns(x, 30, caxis=None, axis=(1, 2, 3), seed=2022, extra=True)
        snrv = pb.snr(y, n, caxis=None, axis=(1, 2, 3))
        print(snrv, 'real-valued in real-format')

        pb.setseed(2020)
        x = np.random.randn(5, 2, 3, 4)
        y, n = awgns2(x, 30, caxis=1, axis=(2, 3), seed=2022, extra=True)
        snrv = pb.snr(y, n, caxis=1, axis=(1, 2), keepcaxis=False)
        print(snrv, 'real-valued in real-format, multi-channel')

        # ---output
        [29.97444457 30.06965181 29.95413251 29.99284633 29.96209985] complex-valued in complex-format
        [29.97444457 30.06965181 29.95413251 29.99284633 29.96209985] complex-valued in real-format
        [29.99399902 30.04417082 30.05313719 29.86315167 29.9423689 ] real-valued in real-format
        [29.97424739 30.07329346 29.95404992 29.98695481 29.94601035] real-valued in real-format, multi-channel
    
    """

def awgns2(x, snrv, **kwargs):
    """adds white gaussian noise to multi-channel signal

    see `Adding noise with a desired signal-to-noise ratio <https://sites.ualberta.ca/~msacchi/SNR_Def.pdf>`_ .

    Parameters
    ----------
    x : tensor
        The pure real-valued multi-channel signal data.
    snrv : int or float
        The signal-to-noise ratio value in dB.
    caxis : None or int, optional
        Specifies the channel dimension. If not specified, :attr:`x` will be treated as
        single-channel signal.
    axis : int or None, optional
        Specifies the dimensions for adding noise, if not specified, it's set to :obj:`None`, 
        which means all the dimensions.
    seed : int or None, optional
        Specifies the seed for generating random noise, if not specified, it's set to :obj:`None`.
    extra : bool, optional
        If :obj:`True`, noise will also be returned.

    Returns
    -----------
    y : tensor
        The SNRs.

    see :func:`awgns`.

    Examples
    ---------

    .. image:: ./_static/DemoNoiseAWGNS.png
       :scale: 100 %
       :align: center

    The results shown in the above figure can be obtained by the following codes.

    ::

        datafolder = pb.data_path('optical')
        xr = pb.imread(datafolder + 'Einstein256.png')
        xi = pb.imread(datafolder + 'LenaGRAY256.png')

        x = xr + 1j * xi
        x = pb.c2r(x, caxis=-1)
        print(x.shape)

        xnp15, np15 = pb.awgns2(x, snrv=15, caxis=-1, axis=(0, 1), extra=True)
        xn0, n0 = pb.awgns2(x, snrv=0, caxis=-1, axis=(0, 1), extra=True)
        xnn5, nn5 = pb.awgns2(x, snrv=-5, caxis=-1, axis=(0, 1), extra=True)

        print(pb.snr(x, np15, caxis=-1, axis=(0, 1)))
        print(pb.snr(x, n0, caxis=-1, axis=(0, 1)))
        print(pb.snr(x, nn5, caxis=-1, axis=(0, 1)))

        x = pb.abs(x, caxis=-1)
        xnp15 = pb.abs(xnp15, caxis=-1)
        xn0 = pb.abs(xn0, caxis=-1)
        xnn5 = pb.abs(xnn5, caxis=-1)

        plt = pb.imshow([x, xnp15, xn0, xnn5], titles=['original', 'noised(15dB)', 'noised(0dB)', 'noised(-5dB)'])
        plt.show()

    """

def imnoise(x, noise='awgn', snrv=30, fmt='chnllast', seed=None):
    r"""Add noise to image

    Add noise to each channel of the image.

    Parameters
    ----------
    x : tensor
        image aray
    noise : str, optional
        noise type (the default is 'awgn', which means white gaussian noise, using :func:`awgn`)
    snrv : float, optional
        Signal-to-noise ratio (the default is 30, which [default_description])
    peak : None, str or float
        Peak value in input, if None, auto detected (default), if ``'maxv'``, use the maximum value as peak value.
    fmt : str or None, optional
        for color image, :attr:`fmt` should be specified with ``'chnllast'`` or ``'chnlfirst'``, for gray image, :attr:`fmt` should be setted to :obj:`None`.

    Returns
    -------
    tensor
        Images with added noise.

    Examples
    ---------

    .. image:: ./_static/DemoIMNOISE.png
       :scale: 100 %
       :align: center

    The results shown in the above figure can be obtained by the following codes.

    ::

        datafolder = pb.data_path('optical')
        xr = pb.imread(datafolder + 'Einstein256.png')
        xi = pb.imread(datafolder + 'LenaGRAY256.png')

        x = xr + 1j * xi

        xnp15 = pb.imnoise(x, 'awgn', snrv=15)
        xn0 = pb.imnoise(x, 'awgn', snrv=0)
        xnn5 = pb.imnoise(x, 'awgn', snrv=-5)

        x = pb.abs(x, caxis=None)
        xnp15 = pb.abs(xnp15, caxis=None)
        xn0 = pb.abs(xn0, caxis=None)
        xnn5 = pb.abs(xnn5, caxis=None)

        plt = pb.imshow([x, xnp15, xn0, xnn5], titles=['original', 'noised(15dB)', 'noised(0dB)', 'noised(-5dB)'])
        plt.show()


        datafolder = pb.data_path('optical')
        xr = pb.imread(datafolder + 'Einstein256.png')
        xi = pb.imread(datafolder + 'LenaGRAY256.png')

        x = xr + 1j * xi
        x = pb.c2r(x, caxis=-1)
        print(x.shape, x.max())

        xnp15 = pb.imnoise(x, 'awgn', snrv=15)
        xn0 = pb.imnoise(x, 'awgn', snrv=0)
        xnn5 = pb.imnoise(x, 'awgn', snrv=-5)

        x = pb.abs(x, caxis=-1)
        xnp15 = pb.abs(xnp15, caxis=-1)
        xn0 = pb.abs(xn0, caxis=-1)
        xnn5 = pb.abs(xnn5, caxis=-1)

        plt = pb.imshow([x, xnp15, xn0, xnn5], titles=['original', 'noised(15dB)', 'noised(0dB)', 'noised(-5dB)'])
        plt.show()


    """

def awgn(sig, snrv=30, pmode='db', power='measured', seed=None):
    r"""AWGN Add white Gaussian noise to a signal.

    AWGN Add white Gaussian noise to a signal like matlab.

    Y = AWGN(X,snrv) adds white Gaussian noise to X.  The snrv is in dB.
    The power of X is assumed to be 0 dBW.  If X is complex, then
    AWGN adds complex noise.

    Parameters
    ----------
    sig : tensor
        Signal that will be noised.
    snrv : float, optional
        Signal Noise Ratio (the default is 30)
    pmode : str, optional
        Power mode ``'linear'``, ``'db'`` (the default is 'db')
    power : float, str, optional
        the power of signal or the method for computing power (the default is 'measured', which is sigPower = np.sum(np.abs(sig) ** 2) / np.numel(sig))
    seed : int, optional
        Seed for random number generator. (the default is None, which means different each time)
    
    Returns
    -------
    tensor
        noised data

    Raises
    ------
    IOError
        No input signal
    TypeError
        Input signal shape wrong
    """

def wgn(shape, power, pmode='dbw', dtype='real', seed=None):
    r"""WGN Generates white Gaussian noise.

    WGN Generates white Gaussian noise like matlab.

    Y = WGN((M,N),P) generates an M-by-N matrix of white Gaussian noise. P
    specifies the power of the output noise in dBW. The unit of measure for
    the output of the wgn function is Volts. For power calculations, it is
    assumed that there is a load of 1 Ohm.

    Parameters
    ----------
    shape : tuple
        Shape of noising matrix
    power : float
        P specifies the power of the output noise in dBW.
    pmode : str, optional
        Power mode of the output noise (the default is 'dbw')
    dtype : str, optional
        data type, real or complex (the default is 'real', which means real-valued)
    seed : int, optional
        Seed for random number generator. (the default is None, which means different each time)

    Returns
    -------
    tensor
        Matrix of white Gaussian noise (real or complex).
    """


