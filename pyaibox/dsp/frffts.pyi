def frfft(x, n=None, caxis=None, axis=0, keepcaxis=False, norm=None, shift=False):
    r"""Fractional FFT in pyaibox

    Fractional FFT in pyaibox, both real and complex valued tensors are supported.

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

def frifft(x, n=None, caxis=None, axis=0, keepcaxis=False, norm=None, shift=False):
    r"""Fractional IFFT in pyaibox

    Fractional IFFT in pyaibox, both real and complex valued tensors are supported.

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


