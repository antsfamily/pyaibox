def db2mag(db):
    r"""Converts decibel values to magnitudes

    .. math::
       {\rm mag} = 10^{db / 20}

    Parameters
    ----------
    db : int, float, tuple, list, ndarray
        The decibel values.

    Returns
    -------
     int, float, tuple, list, ndarray
        The magnitudes of inputs with the same type.
    """

def mag2db(mag):
    r"""Converts decibel values to magnitudes

    .. math::
       {\rm db} = 20*{\rm log10}{\rm mag}

    Parameters
    ----------
    mag : int, float, tuple, list, ndarray
        The magnitude values.

    Returns
    -------
     int, float, tuple, list, ndarray
        The decibel of inputs with the same type.
    """

def fnab(n):
    """gives the closest two integer number factor of a number

    Parameters
    ----------
    n : int or float
        the number

    Returns
    -------
    a : int
    b : int
        the factor number

    Examples
    --------

    ::

        print(fnab(5))
        print(fnab(6))
        print(fnab(7))
        print(fnab(8))
        print(fnab(9))

        # ---output
        (2, 3)
        (2, 3)
        (2, 4)
        (2, 4)
        (3, 3)

    """    

def ebeo(a, b, op='+'):
    r"""element by element operation

    Element by element operation.

    Parameters
    ----------
    a : list, tuple or ndarray
        The first list/tuple/ndarray.
    b : list, tuple or ndarray
        The second list/tuple/ndarray.
    op : str, optional
        Supported operations are:
        - ``'+'`` or ``'add'`` for addition (default)
        - ``'-'`` or ``'sub'`` for substraction
        - ``'*'`` or ``'mul'`` for multiplication
        - ``'/'`` or ``'div'`` for division
        - ``'**'`` or ``pow`` for power
        - ``'<'``, or ``'lt'`` for less than
        - ``'<='``, or ``'le'`` for less than or equal to
        - ``'>'``, or ``'gt'`` for greater than
        - ``'>='``, or ``'ge'`` for greater than or equal to
        - ``'&'`` for bitwise and
        - ``'|'`` for bitwise or
        - ``'^'`` for bitwise xor
        - function for custom operation.

    Raises
    ------
    TypeError
        If the specified operator not in the above list, raise a TypeError.
    """

def nextpow2(x):
    r"""get the next higher power of 2.

    Given an number :math:`x`, returns the first p such that :math:`2^p >=|x|`. 

    Args:
        x (int or float): an number.

    Returns:
        int: Next higher power of 2.

    Examples:

        ::

            print(prevpow2(-5), nextpow2(-5))
            print(prevpow2(5), nextpow2(5))
            print(prevpow2(0.3), nextpow2(0.3))
            print(prevpow2(7.3), nextpow2(7.3))
            print(prevpow2(-3.5), nextpow2(-3.5))

            # output
            2 3
            2 3
            -2 -1
            2 3
            1 2

    """

def prevpow2(x):
    r"""get the previous lower power of 2.

    Given an number :math:`x`, returns the first p such that :math:`2^p <=|x|`. 

    Args:
        x (int or float): an number.

    Returns:
        int: Next higher power of 2.

    Examples:

        ::

            print(prevpow2(-5), nextpow2(-5))
            print(prevpow2(5), nextpow2(5))
            print(prevpow2(0.3), nextpow2(0.3))
            print(prevpow2(7.3), nextpow2(7.3))
            print(prevpow2(-3.5), nextpow2(-3.5))

            # output
            2 3
            2 3
            -2 -1
            2 3
            1 2

    """

def r2c(X, caxis=-1, keepcaxis=False):
    r"""convert real-valued array to complex-valued array

    Convert real-valued array (the size of :attr:`axis` -th dimension is 2) to complex-valued array

    Args:
        X (numpy array): real-valued array.
        caxis (int, optional): the complex axis. Defaults to -1.
        keepcaxis (bool, optional): keepcaxis? default is False.

    Returns:
        numpy array: complex-valued array

    Examples:

        ::

            import numpy as np

            np.random.seed(2020)

            Xreal = np.random.randint(0, 30, (3, 2, 4))
            Xcplx = r2c(Xreal, caxis=1)
            Yreal = c2r(Xcplx, caxis=0, keepcaxis=True)

            print(Xreal, Xreal.shape, 'Xreal')
            print(Xcplx, Xcplx.shape, 'Xcplx')
            print(Yreal, Yreal.shape, 'Yreal')
            print(np.sum(Yreal[0] - Xcplx.real), np.sum(Yreal[1] - Xcplx.imag), 'Error')

            # output
            [[[ 0  8  3 22]
            [ 3 27 29  3]]

            [[ 7 24 29 16]
            [ 0 24 10  9]]

            [[19 11 23 18]
            [ 3  6  5 16]]] (3, 2, 4) Xreal

            [[[ 0. +3.j  8.+27.j  3.+29.j 22. +3.j]]

            [[ 7. +0.j 24.+24.j 29.+10.j 16. +9.j]]

            [[19. +3.j 11. +6.j 23. +5.j 18.+16.j]]] (3, 1, 4) Xcplx

            [[[[ 0.  8.  3. 22.]]

            [[ 7. 24. 29. 16.]]

            [[19. 11. 23. 18.]]]


            [[[ 3. 27. 29.  3.]]

            [[ 0. 24. 10.  9.]]

            [[ 3.  6.  5. 16.]]]] (2, 3, 1, 4) Yreal

            0.0 0.0, Error
    """

def c2r(X, caxis=-1, keepcaxis=True):
    r"""convert complex-valued array to real-valued array

    Args:
        X (numpy array): complex-valued array
        caxis (int, optional): complex axis for real-valued array. Defaults to -1.
        keepcaxis (bool, optional): keepcaxis? default is True.

    Returns:
        numpy array: real-valued array

    Examples:

        ::

            import numpy as np

            np.random.seed(2020)

            Xreal = np.random.randint(0, 30, (3, 2, 4))
            Xcplx = r2c(Xreal, caxis=1)
            Yreal = c2r(Xcplx, caxis=0, keepcaxis=True)

            print(Xreal, Xreal.shape, 'Xreal')
            print(Xcplx, Xcplx.shape, 'Xcplx')
            print(Yreal, Yreal.shape, 'Yreal')
            print(np.sum(Yreal[0] - Xcplx.real), np.sum(Yreal[1] - Xcplx.imag), 'Error')

            # output
            [[[ 0  8  3 22]
            [ 3 27 29  3]]

            [[ 7 24 29 16]
            [ 0 24 10  9]]

            [[19 11 23 18]
            [ 3  6  5 16]]] (3, 2, 4) Xreal

            [[[ 0. +3.j  8.+27.j  3.+29.j 22. +3.j]]

            [[ 7. +0.j 24.+24.j 29.+10.j 16. +9.j]]

            [[19. +3.j 11. +6.j 23. +5.j 18.+16.j]]] (3, 1, 4) Xcplx

            [[[[ 0.  8.  3. 22.]]

            [[ 7. 24. 29. 16.]]

            [[19. 11. 23. 18.]]]


            [[[ 3. 27. 29.  3.]]

            [[ 0. 24. 10.  9.]]

            [[ 3.  6.  5. 16.]]]] (2, 3, 1, 4) Yreal

            0.0 0.0, Error
    """

def conj(X, caxis=None):
    r"""conjugates a array

    Both complex and real representation are supported.

    Parameters
    ----------
    X : array
        input
    caxis : int or None
        If :attr:`X` is complex-valued, :attr:`cdim` is ignored. If :attr:`X` is real-valued and :attr:`cdim` is integer
        then :attr:`X` will be treated as complex-valued, in this case, :attr:`cdim` specifies the complex axis;
        otherwise (None), :attr:`X` will be treated as real-valued

    Returns
    -------
    array
         the inputs's conjugate matrix.

    Examples
    ---------

    ::

        np.random.seed(2020)
        X = np.random.rand(2, 3, 3)

        print('---conj')
        print(conj(X, caxis=0))
        print(conj(X[0] + 1j * X[1]))

        # ---output
        ---conj
        [[[ 0.98627683  0.87339195  0.50974552]
        [ 0.27183571  0.33691873  0.21695427]
        [ 0.27647714  0.34331559  0.86215894]]

        [[-0.15669967 -0.14088724 -0.75708028]
        [-0.73632492 -0.35566309 -0.34109302]
        [-0.66680305 -0.21710064 -0.56142698]]]
        [[0.98627683-0.15669967j 0.87339195-0.14088724j 0.50974552-0.75708028j]
        [0.27183571-0.73632492j 0.33691873-0.35566309j 0.21695427-0.34109302j]
        [0.27647714-0.66680305j 0.34331559-0.21710064j 0.86215894-0.56142698j]]

    """

def real(X, caxis=None, keepcaxis=False):
    r"""obtain real part of a array

    Both complex and real representation are supported.

    Parameters
    ----------
    X : array
        input
    caxis : int or None
        If :attr:`X` is complex-valued, :attr:`cdim` is ignored. If :attr:`X` is real-valued and :attr:`cdim` is integer
        then :attr:`X` will be treated as complex-valued, in this case, :attr:`cdim` specifies the complex axis;
        otherwise (None), :attr:`X` will be treated as real-valued
    keepcaxis : bool, optional
        keep complex-dimension?

    Returns
    -------
    array
         the inputs's real part array.

    Examples
    ---------

    ::

        np.random.seed(2020)
        X = np.random.rand(2, 3, 3)

        print('---real')
        print(real(X, caxis=0))
        print(real(X[0] + 1j * X[1]))

        # ---output
        ---real
        [[0.98627683 0.87339195 0.50974552]
        [0.27183571 0.33691873 0.21695427]
        [0.27647714 0.34331559 0.86215894]]
        [[0.98627683 0.87339195 0.50974552]
        [0.27183571 0.33691873 0.21695427]
        [0.27647714 0.34331559 0.86215894]]
    """

def imag(X, caxis=None, keepcaxis=False):
    r"""obtain imaginary part of a array

    Both complex and real representation are supported.

    Parameters
    ----------
    X : array
        input
    caxis : int or None
        If :attr:`X` is complex-valued, :attr:`cdim` is ignored. If :attr:`X` is real-valued and :attr:`cdim` is integer
        then :attr:`X` will be treated as complex-valued, in this case, :attr:`cdim` specifies the complex axis;
        otherwise (None), :attr:`X` will be treated as real-valued
    keepcaxis : bool, optional
        keep complex-dimension?

    Returns
    -------
    array
         the inputs's imaginary part array.

    Examples
    ---------

    ::

        np.random.seed(2020)
        X = np.random.rand(2, 3, 3)

        print('---imag')
        print(imag(X, caxis=0))
        print(imag(X[0] + 1j * X[1]))

        # ---output
        ---imag
        [[0.15669967 0.14088724 0.75708028]
        [0.73632492 0.35566309 0.34109302]
        [0.66680305 0.21710064 0.56142698]]
        [[0.15669967 0.14088724 0.75708028]
        [0.73632492 0.35566309 0.34109302]
        [0.66680305 0.21710064 0.56142698]]

    """

def abs(X, caxis=None, keepcaxis=False):
    r"""obtain amplitude of a array

    Both complex and real representation are supported.

    .. math::
       {\rm abs}({\bf X}) = |{\bf x}| = \sqrt{u^2 + v^2}, x\in {\bf X}

    where, :math:`u, v` are the real and imaginary part of x, respectively.

    Parameters
    ----------
    X : array
        input
    caxis : int or None
        If :attr:`X` is complex-valued, :attr:`cdim` is ignored. If :attr:`X` is real-valued and :attr:`cdim` is integer
        then :attr:`X` will be treated as complex-valued, in this case, :attr:`cdim` specifies the complex axis;
        otherwise (None), :attr:`X` will be treated as real-valued
    keepcaxis : bool, optional
        keep complex-dimension?

    Returns
    -------
    array
         the inputs's amplitude.
   
    Examples
    ---------

    ::

        np.random.seed(2020)
        X = np.random.rand(2, 3, 3)

        print('---abs')
        print(abs(X, caxis=0))
        print(abs(X[0] + 1j * X[1]))

        # ---output
        ---abs
        [[0.99864747 0.88468226 0.91269439]
        [0.78490066 0.48990863 0.40424448]
        [0.72184896 0.40619981 1.02884318]]
        [[0.99864747 0.88468226 0.91269439]
        [0.78490066 0.48990863 0.40424448]
        [0.72184896 0.40619981 1.02884318]]

    """

def pow(X, caxis=None, keepcaxis=False):
    r"""obtain power of a array

    Both complex and real representation are supported.

    .. math::
       {\rm pow}({\bf X}) = |{\bf x}| = u^2 + v^2, x\in {\bf X}

    where, :math:`u, v` are the real and imaginary part of x, respectively.

    Parameters
    ----------
    X : array
        input
    caxis : int or None
        If :attr:`X` is complex-valued, :attr:`cdim` is ignored. If :attr:`X` is real-valued and :attr:`cdim` is integer
        then :attr:`X` will be treated as complex-valued, in this case, :attr:`cdim` specifies the complex axis;
        otherwise (None), :attr:`X` will be treated as real-valued
    keepcaxis : bool, optional
        keep complex-dimension?

    Returns
    -------
    array
         the inputs's power.
   
    Examples
    ---------

    ::

        np.random.seed(2020)
        X = np.random.rand(2, 3, 3)

        print('---pow')
        print(pow(X, caxis=0))
        print(pow(X[0] + 1j * X[1]))

        # ---output
        ---pow
        [[0.99729677 0.78266271 0.83301105]
        [0.61606904 0.24001046 0.1634136 ]
        [0.52106592 0.16499828 1.05851829]]
        [[0.99729677 0.78266271 0.83301105]
        [0.61606904 0.24001046 0.1634136 ]
        [0.52106592 0.16499828 1.05851829]]

    """


