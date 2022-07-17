def snr(x, n=None, **kwargs):
    r"""computes signal-to-noise ratio

    .. math::
        {\rm SNR} = 10*{\rm log10}(\frac{P_x}{P_n})
    
    where, :math:`P_x, P_n` are the power summary of the signal and noise:

    .. math::
       P_x = \sum_{i=1}^N |x_i|^2 \\
       P_n = \sum_{i=1}^N |n_i|^2 
    
    ``snr(x, n)`` equals to matlab's ``snr(x, n)``

    Parameters
    ----------
    x : tensor
        The pure signal data.
    n : ndarray, tensor
        The noise data.
    caxis : None or int, optional
        If :attr:`x` and :attr:`n` are complex-valued but represented in real format, 
        :attr:`caxis` or :attr:`cdim` should be specified. If not, it's set to :obj:`None`, 
        which means :attr:`x` and :attr:`n` are real-valued or complex-valued in complex format.
    keepcaxis : int or None, optional
        keep the complex dimension?
    axis : int or None, optional
        Specifies the dimensions for computing SNR, if not specified, it's set to :obj:`None`, 
        which means all the dimensions.
    reduction : str, optional
        The reduce operation in batch dimension. Supported are ``'mean'``, ``'sum'`` or :obj:`None`.
        If not specified, it is set to :obj:`None`.
    
    Returns
    -----------
      : scalar
        The SNRs.

    Examples
    ----------

    ::

        import torch as th
        import pyaibox as pb
    
        pb.setseed(seed=2020, target='numpy')
        x = 10 * th.randn(5, 2, 3, 4)
        n = th.randn(5, 2, 3, 4)
        snrv = snr(x, n, caxis=1, axis=(2, 3), keepcaxis=True)
        print(snrv)
        snrv = snr(x, n, caxis=1, axis=(2, 3), keepcaxis=True, reduction='mean')
        print(snrv)
        x = pb.r2c(x, caxis=1, keepcaxis=False)
        n = pb.r2c(n, caxis=1, keepcaxis=False)
        snrv = snr(x, n, caxis=None, axis=(1, 2), reduction='mean')
        print(snrv)

        ---output
        [[19.36533589]
        [20.09428302]
        [19.29255523]
        [19.81755215]
        [17.88677726]]
        19.291300709856387
        19.291300709856387

    """

def psnr(P, G, vpeak=None, **kwargs):
    r"""Peak Signal-to-Noise Ratio

    The Peak Signal-to-Noise Ratio (PSNR) is expressed as

    .. math::
        {\rm psnrv} = 10 \log10(\frac{V_{\rm peak}^2}{\rm MSE})

    For float data, :math:`V_{\rm peak} = 1`;

    For interges, :math:`V_{\rm peak} = 2^{\rm nbits}`,
    e.g. uint8: 255, uint16: 65535 ...


    Parameters
    -----------
    P : array_like
        The data to be compared. For image, it's the reconstructed image.
    G : array_like
        Reference data array. For image, it's the original image.
    vpeak : float, int or None, optional
        The peak value. If None, computes automaticly.
    caxis : None or int, optional
        If :attr:`P` and :attr:`G` are complex-valued but represented in real format, 
        :attr:`caxis` or :attr:`cdim` should be specified. If not, it's set to :obj:`None`, 
        which means :attr:`P` and :attr:`G` are real-valued or complex-valued in complex format.
    keepcaxis : int or None, optional
        keep the complex dimension?
    axis : int or None, optional
        Specifies the dimensions for computing SNR, if not specified, it's set to :obj:`None`, 
        which means all the dimensions.
    reduction : str, optional
        The reduce operation in batch dimension. Supported are ``'mean'``, ``'sum'`` or :obj:`None`.
        If not specified, it is set to :obj:`None`.
    
    Returns
    -------
    psnrv : float
        Peak Signal to Noise Ratio value.

    Examples
    ---------

    ::

        import torch as th
        import pyaibox as pb
    
        pb.setseed(seed=2020, target='numpy')
        P = 255. * np.random.rand(5, 2, 3, 4)
        G = 255. * np.random.rand(5, 2, 3, 4)
        snrv = psnr(P, G, caxis=1, dim=(2, 3), keepcaxis=True)
        print(snrv)
        snrv = psnr(P, G, caxis=1, dim=(2, 3), keepcaxis=True, reduction='mean')
        print(snrv)
        P = pb.r2c(P, caxis=1, keepcaxis=False)
        G = pb.r2c(G, caxis=1, keepcaxis=False)
        snrv = psnr(P, G, caxis=None, dim=(1, 2), reduction='mean')
        print(snrv)

        # ---output
        [[4.93636105]
        [5.1314932 ]
        [4.65173472]
        [5.05826362]
        [5.20860623]]
        4.997291765071102
        4.997291765071102

    """


