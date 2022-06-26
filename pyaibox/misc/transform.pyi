def standardization(X, mean=None, std=None, axis=None, extra=False):
    r"""standardization

    .. math::
        \bar{X} = \frac{X-\mu}{\sigma}


    Args:
        X (ndarray): data to be normalized,
        mean (list or None, optional): mean value (the default is None, which means auto computed)
        std (list or None, optional): standard deviation (the default is None, which means auto computed)
        axis (list, tuple or int, optional): specify the axis for computing mean and standard deviation (the default is None, which means all elements)
        extra (bool, optional): if True, also return the mean and std (the default is False, which means just return the standardized data)

    Returns:
        (ndarray): Standardized/Normalized ndarray.
    """

def scale(X, st=[0, 1], sf=None, istrunc=True, extra=False):
    r"""
    Scale data.

    .. math::
        x \in [a, b] \rightarrow y \in [c, d]

    .. math::
        y = (d-c)*(x-a) / (b-a) + c.

    Args:
        X (ndarray): The data to be scaled.
        st (tuple, list, optional): Specifies the range of data after beening scaled. Default [0, 1].
        sf (tuple, list, optional): Specifies the range of data. Default [min(X), max(X)].
        istrunc (bool): Specifies wether to truncate the data to [a, b], For example,
            If sf == [a, b] and 'istrunc' is true,
            then X[X < a] == a and X[X > b] == b.
        extra (bool): If ``True``, also return :attr:`st` and :attr:`sf`.

    Returns:
        out (ndarray): Scaled data ndarray.
        st, sf (list or tuple): If :attr:`extra` is true, also be returned

    Raises:
        Exception: Description
    """

def quantization(X, idrange=None, odrange=[0, 31], odtype='auto', extra=False):
    r"""
    Quantize data.

    .. math::
        {\bm X} \in [a, b] \rightarrow y \in [c, d]

    .. math::
        {\bm Y} = \lfloor (d-c) (X-a) / (b-a) + c \rfloor.

    Args:
        X (ndarray): The data to be quantized with shape :math:`{\bm X} \in {\mathbb R}^{N_a×N_r}`, or :math:`{\bm X} \in {\mathbb C}^{N_a×N_r}`.
        idrange (tuple, list, optional): Specifies the range of data. Default :math:`[{\rm min}(X), {\rm max}(X)]`.
        odrange (tuple, list, optional): Specifies the range of data after beening quantized. Default [0, 31].
        odtype (str or None, optional): output data type, supportted are ``'auto'`` (auto infer, default), or numpy ndarray's dtype string.
            If the type of :attr:`odtype` is not string(such as None), the type of output data is the same with input.
        extra (bool): If ``True``, also return :attr:`idrange` and :attr:`odrange`.

    Returns:
        (ndarray): Quantized data ndarray, if the input is complex, will return a ndarray with shape :math:`{\bm Y} \in {\mathbb R}^{N_a×N_r×2}`.
        idrange, odrange (list or tuple): If :attr:`extra` is true, also be returned

    Raises:
        Exception: :attr:`idrange` and :attr:`odrange` should be (tulpe) or (list)
    """

def db20(x):
def ct2rt(x, axis=0):
    r"""Converts a complex-valued tensor to a real-valued tensor

    Converts a complex-valued tensor :math:`{\bf x}` to a real-valued tensor with FFT and conjugate symmetry.


    Parameters
    ----------
    x : Tensor
        The input tensor :math:`{\bf x}\in {\mathbb C}^{H×W}`.
    axis : int
        The axis for excuting FFT.

    Returns
    -------
    Tensor
        The output tensor :math:`{\bf y}\in {\mathbb R}^{2H×W}` ( :attr:`axis` = 0 ), :math:`{\bf y}\in {\mathbb R}^{H×2W}` ( :attr:`axis` = 1 )
    """

def rt2ct(y, axis=0):
    r"""Converts a real-valued tensor to a complex-valued tensor

    Converts a real-valued tensor :math:`{\bf y}` to a complex-valued tensor with FFT and conjugate symmetry.


    Parameters
    ----------
    y : Tensor
        The input tensor :math:`{\bf y}\in {\mathbb C}^{2H×W}`.
    axis : int
        The axis for excuting FFT.

    Returns
    -------
    Tensor
        The output tensor :math:`{\bf x}\in {\mathbb R}^{H×W}` ( :attr:`axis` = 0 ), :math:`{\bf x}\in {\mathbb R}^{H×W}` ( :attr:`axis` = 1 )
    """

