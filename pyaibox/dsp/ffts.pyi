def freq(n, fs, norm=False, shift=False):
    r"""Return the sample frequencies

    Return the sample frequencies.

    Given a window length `n` and a sample rate `fs`, if shift is ``True``::

      f = [-n/2, ..., n/2] / (d*n)

    Given a window length `n` and a sample rate `fs`, if shift is ``False``::

      f = [0, 1, ..., n] / (d*n)

    If :attr:`norm` is ``True``, :math:`d = 1`, else :math:`d = 1/f_s`.

    Parameters
    ----------
    n : int
        Number of samples.
    fs : float
        Sampling rate.
    norm : bool
        Normalize the frequencies.
    shift : bool
        Does shift the zero frequency to center.

    Returns
    -------
    numpy array
        frequency array with size :math:`n×1`.
    """

def fftfreq(n, fs, norm=False, shift=False):
    r"""Return the Discrete Fourier Transform sample frequencies

    Return the Discrete Fourier Transform sample frequencies.

    Given a window length `n` and a sample rate `fs`, if shift is ``True``::

      f = [-n/2, ..., -1,     0, 1, ...,   n/2-1] / (d*n)   if n is even
      f = [-(n-1)/2, ..., -1, 0, 1, ..., (n-1)/2] / (d*n)   if n is odd

    Given a window length `n` and a sample rate `fs`, if shift is ``False``::

      f = [0, 1, ...,   n/2-1,     -n/2, ..., -1] / (d*n)   if n is even
      f = [0, 1, ..., (n-1)/2, -(n-1)/2, ..., -1] / (d*n)   if n is odd

    where :math:`d = 1/f_s`, if :attr:`norm` is ``True``, :math:`d = 1`, else :math:`d = 1/f_s`.

    Parameters
    ----------
    fs : float
        Sampling rate.
    n : int
        Number of samples.
    norm : bool
        Normalize the frequencies.
    shift : bool
        Does shift the zero frequency to center.

    Returns
    -------
    numpy array
        frequency array with size :math:`n×1`.
    """

def fftshift(x, **kwargs):
    r"""Shift the zero-frequency component to the center of the spectrum.

    This function swaps half-spaces for all axes listed (defaults to all).
    Note that ``y[0]`` is the Nyquist component only if ``len(x)`` is even.

    Parameters
    ----------
    x : numpy array
        The input array.
    axis : int, optional
        Axes over which to shift. (Default is None, which shifts all axes.)

    Returns
    -------
    y : numpy array
        The shifted array.

    See Also
    --------
    ifftshift : The inverse of :func:`fftshift`.

    """

def ifftshift(x, **kwargs):
    r"""Shift the zero-frequency component back.

    The inverse of :func:`fftshift`. Although identical for even-length `x`, the
    functions differ by one sample for odd-length `x`.

    Parameters
    ----------
    x : numpy array
        The input array.
    axis : int, optional
        Axes over which to shift. (Default is None, which shifts all axes.)

    Returns
    -------
    y : numpy array
        The shifted array.

    See Also
    --------
    fftshift : The inverse of `ifftshift`.

    Examples
    --------

    ::

        x = [1, 2, 3, 4, 5, 6]
        y = np.fft.ifftshift(x)
        print(y)
        y = pb.ifftshift(x)
        print(y)

        x = [1, 2, 3, 4, 5, 6, 7]
        y = np.fft.ifftshift(x)
        print(y)
        y = pb.ifftshift(x)
        print(y)

        axis = (0, 1)  # axis = 0, axis = 1
        x = [[1, 2, 3, 4, 5, 6], [0, 2, 3, 4, 5, 6]]
        y = np.fft.ifftshift(x, axis)
        print(y)
        y = pb.ifftshift(x, axis)
        print(y)


        x = [[1, 2, 3, 4, 5, 6, 7], [0, 2, 3, 4, 5, 6, 7]]
        y = np.fft.ifftshift(x, axis)
        print(y)
        y = pb.ifftshift(x, axis)
        print(y)

    """

def padfft(X, nfft=None, axis=0, shift=False):
    r"""PADFT Pad array for doing FFT or IFFT

    PADFT Pad array for doing FFT or IFFT

    Parameters
    ----------
    X : ndarray
        Data to be padded.
    nfft : int or None
        the number of fft point.
    axis : int, optional
        Padding dimension. (the default is 0)
    shift : bool, optional
        Whether to shift the frequency (the default is False)
    """

def fft(x, n=None, norm=None, shift=False, **kwargs):
    r"""FFT in pyaibox

    FFT in pyaibox, both real and complex valued tensors are supported.

    Parameters
    ----------
    x : array
        When :attr:`x` is complex, it can be either in real-representation format or complex-representation format.
    n : int, optional
        The number of fft points (the default is None --> equals to signal dimension)
    caxis : int or None
        If :attr:`X` is complex-valued, :attr:`caxis` is ignored. If :attr:`X` is real-valued and :attr:`caxis` is integer
        then :attr:`X` will be treated as complex-valued, in this case, :attr:`caxis` specifies the complex axis;
        otherwise (None), :attr:`X` will be treated as real-valued.
    axis : int, optional
        axis of fft operation (the default is 0, which means the first dimension)
    keepcaxis : bool
        If :obj:`True`, the complex dimension will be keeped. Only works when :attr:`X` is complex-valued array 
        and :attr:`axis` is not :obj:`None` but represents in real format. Default is :obj:`False`.
    norm : None or str, optional
        Normalization mode. For the forward transform (fft()), these correspond to:
        - :obj:`None` - no normalization (default)
        - "ortho" - normalize by ``1/sqrt(n)`` (making the FFT orthonormal)
    shift : bool, optional
        shift the zero frequency to center (the default is False)

    Returns
    -------
    y : array
        fft results array with the same type as :attr:`x`

    see also :func:`ifft`, :func:`fftfreq`, :func:`freq`.

    Examples
    ---------

    .. image:: ./_static/FFTIFFTdemo.png
       :scale: 100 %
       :align: center

    The results shown in the above figure can be obtained by the following codes.

    ::

        import numpy as np
        import pyaibox as pb
        import matplotlib.pyplot as plt

        shift = True
        frq = [10, 10]
        amp = [0.8, 0.6]
        Fs = 80
        Ts = 2.
        Ns = int(Fs * Ts)

        t = np.linspace(-Ts / 2., Ts / 2., Ns).reshape(Ns, 1)
        f = pb.freq(Ns, Fs, shift=shift)
        f = pb.fftfreq(Ns, Fs, norm=False, shift=shift)

        # ---complex vector in real representation format
        x = amp[0] * np.cos(2. * np.pi * frq[0] * t) + 1j * amp[1] * np.sin(2. * np.pi * frq[1] * t)

        # ---do fft
        Xc = pb.fft(x, n=Ns, caxis=None, axis=0, keepcaxis=False, shift=shift)

        # ~~~get real and imaginary part
        xreal = pb.real(x, caxis=None, keepcaxis=False)
        ximag = pb.imag(x, caxis=None, keepcaxis=False)
        Xreal = pb.real(Xc, caxis=None, keepcaxis=False)
        Ximag = pb.imag(Xc, caxis=None, keepcaxis=False)

        # ---do ifft
        x̂ = pb.ifft(Xc, n=Ns, caxis=None, axis=0, keepcaxis=False, shift=shift)
        
        # ~~~get real and imaginary part
        x̂real = pb.real(x̂, caxis=None, keepcaxis=False)
        x̂imag = pb.imag(x̂, caxis=None, keepcaxis=False)

        plt.figure()
        plt.subplot(131)
        plt.grid()
        plt.plot(t, xreal)
        plt.plot(t, ximag)
        plt.legend(['real', 'imag'])
        plt.title('signal in time domain')
        plt.subplot(132)
        plt.grid()
        plt.plot(f, Xreal)
        plt.plot(f, Ximag)
        plt.legend(['real', 'imag'])
        plt.title('signal in frequency domain')
        plt.subplot(133)
        plt.grid()
        plt.plot(t, x̂real)
        plt.plot(t, x̂imag)
        plt.legend(['real', 'imag'])
        plt.title('reconstructed signal')
        plt.show()

        # ---complex vector in real representation format
        x = pb.c2r(x, caxis=-1)

        # ---do fft
        Xc = pb.fft(x, n=Ns, caxis=-1, axis=0, keepcaxis=False, shift=shift)

        # ~~~get real and imaginary part
        xreal = pb.real(x, caxis=-1, keepcaxis=False)
        ximag = pb.imag(x, caxis=-1, keepcaxis=False)
        Xreal = pb.real(Xc, caxis=-1, keepcaxis=False)
        Ximag = pb.imag(Xc, caxis=-1, keepcaxis=False)

        # ---do ifft
        x̂ = pb.ifft(Xc, n=Ns, caxis=-1, axis=0, keepcaxis=False, shift=shift)
        
        # ~~~get real and imaginary part
        x̂real = pb.real(x̂, caxis=-1, keepcaxis=False)
        x̂imag = pb.imag(x̂, caxis=-1, keepcaxis=False)

        plt.figure()
        plt.subplot(131)
        plt.grid()
        plt.plot(t, xreal)
        plt.plot(t, ximag)
        plt.legend(['real', 'imag'])
        plt.title('signal in time domain')
        plt.subplot(132)
        plt.grid()
        plt.plot(f, Xreal)
        plt.plot(f, Ximag)
        plt.legend(['real', 'imag'])
        plt.title('signal in frequency domain')
        plt.subplot(133)
        plt.grid()
        plt.plot(t, x̂real)
        plt.plot(t, x̂imag)
        plt.legend(['real', 'imag'])
        plt.title('reconstructed signal')
        plt.show()

    """

def ifft(x, n=None, norm=None, shift=False, **kwargs):
    r"""IFFT in pyaibox

    IFFT in pyaibox, both real and complex valued tensors are supported.

    Parameters
    ----------
    x : array
        When :attr:`x` is complex, it can be either in real-representation format or complex-representation format.
    n : int, optional
        The number of ifft points (the default is None --> equals to signal dimension)
    caxis : int or None
        If :attr:`X` is complex-valued, :attr:`caxis` is ignored. If :attr:`X` is real-valued and :attr:`caxis` is integer
        then :attr:`X` will be treated as complex-valued, in this case, :attr:`caxis` specifies the complex axis;
        otherwise (None), :attr:`X` will be treated as real-valued.
    axis : int, optional
        axis of fft operation (the default is 0, which means the first dimension)
    keepcaxis : bool
        If :obj:`True`, the complex dimension will be keeped. Only works when :attr:`X` is complex-valued array 
        and :attr:`axis` is not :obj:`None` but represents in real format. Default is :obj:`False`.
    norm : bool, optional
        Normalization mode. For the backward transform (ifft()), these correspond to:
        - :obj:`None` - no normalization (default)
        - "ortho" - normalize by 1``/sqrt(n)`` (making the IFFT orthonormal)
    shift : bool, optional
        shift the zero frequency to center (the default is False)

    Returns
    -------
    y : array
        ifft results array with the same type as :attr:`x`

    see also :func:`fft`, :func:`fftfreq`, :func:`freq`. see :func:`fft` for examples. 

    """

def fft2(img):
    r"""
    Improved 2D fft
    """

def fftx(x, n=None):
    ...

def ffty(x, n=None):
    ...

def ifftx(x, n=None):
    ...

def iffty(x, n=None):
    ...


