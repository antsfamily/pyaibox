def setseed(seed=None, target='numpy'):
    r"""set seed

    Set numpy / random seed.

    Parameters
    ----------
    seed : int or None, optional
        seed for random number generator (the default is None)
    target : str, optional
        - ``'numpy'``: ``np.random.seed(seed)`` (the default)
        - ``'random'``: ``random(seed)``

    """

def randperm(start, stop, n):
    r"""randperm function like matlab

    genarates diffrent random interges in range [start, stop)

    Parameters
    ----------
    start : int or list
        start sampling point

    stop : int or list
        stop sampling point

    n : int, list or None
        the number of samples (default None, (stop - start))

    Returns
    -------
    P : list
        the randomly permuted intergers. 

    see :func:`randgrid`, :func:`randperm2d`.

    """

def randperm2d(H, W, number, population=None, mask=None):
    r"""randperm 2d function

    genarates diffrent random interges in range [start, end)

    Parameters
    ----------
    H : int
        height

    W : int
        width
    number : int
        random numbers
    population : {list or numpy array(1d or 2d)}
        part of population in range(0, H*W)


    Returns
    -------
        Ph : list
            the randomly permuted intergers in height direction. 
        Pw : list
            the randomly permuted intergers in width direction. 

    see :func:`randgrid`, :func:`randperm`.
    
    """

def randgrid(start, stop, step, shake=0, n=None):
    r"""generates non-repeated uniform stepped random integers

    Generates :attr:`n` non-repeated random integers from :attr:`start` to :attr:`stop`
    with step size :attr:`step`.

    When step is 1 and shake is 0, it works similar to randperm,

    Parameters
    ----------
    start : int or list
        start sampling point
    stop : int or list
        stop sampling point
    step : int or list
        sampling stepsize
    shake : float
        the shake rate, if :attr:`shake` is 0, no shake, (default),
        if positive, add a positive shake, if negative, add a negative.
    n : int or None
        the number of samples (default None, int((stop0 - start0) / step0) * int((stop1 - start1) / step1)...).

    Returns
    -------
        for multi-dimension, return a list of lists, for 1-dimension, return a list of numbers.

    see :func:`randperm`.

    Example
    -------

    Plot sampled randperm and randgrid point.

    .. image:: ./_static/demo_randgrid.png
       :scale: 100 %
       :align: center

    The results shown in the above figure can be obtained by the following codes.

    ::

        import matplotlib.pyplot as plt

        setseed(2021)
        print(randperm(2, 40, 8), ", randperm(2, 40, 8)")
        print(randgrid(2, 40, 1, -1., 8), ", randgrid(2, 40, 1, 8, -1.)")
        print(randgrid(2, 40, 6, -1, 8), ", randgrid(2, 40, 6, 8)")
        print(randgrid(2, 40, 6, 0.5, 8), ", randgrid(2, 40, 6, 8, 0.5)")
        print(randgrid(2, 40, 6, -1, 12), ", randgrid(2, 40, 6, 12)")
        print(randgrid(2, 40, 6, 0.5, 12), ", randgrid(2, 40, 6, 12, 0.5)")

        mask = np.zeros((5, 6))
        mask[3, 4] = 0
        mask[2, 5] = 0

        Rh, Rw = randperm2d(5, 6, 4, mask=mask)

        print(Rh)
        print(Rw)

        N, H, W = 32, 512, 512

        y1 = pb.randperm(0, H, N)
        x1 = pb.randperm(0, W, N)
        print(len(y1), len(x1))

        y2 = pb.randgrid(0, H, 32, 0., N)
        x2 = pb.randgrid(0, W, 32, 0., N)
        print(len(y2), len(x2))
        print(y2, x2)

        y3, x3 = pb.randperm([0, 0], [H, W], N)
        print(len(y3), len(x3))

        y4, x4 = pb.randgrid([0, 0], [H, W], [32, 32], [0.25, 0.25], N)
        print(len(y4), len(x4))

        plt.figure()
        plt.subplot(221)
        plt.grid()
        plt.plot(x1, y1, '*')
        plt.subplot(222)
        plt.grid()
        plt.plot(x2, y2, '*')
        plt.subplot(223)
        plt.grid()
        plt.plot(x3, y3, '*')
        plt.subplot(224)
        plt.grid()
        plt.plot(x4, y4, '*')
        plt.show()

    """


