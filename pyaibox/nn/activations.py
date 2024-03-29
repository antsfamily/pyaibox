#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : activations.py
# @author    : Zhi Liu
# @email     : zhiliu.mind@gmail.com
# @homepage  : http://iridescent.ink
# @date      : Sun Nov 11 2019
# @version   : 0.0
# @license   : The GNU General Public License (GPL) v3.0
# @note      : 
# 
# The GNU General Public License (GPL) v3.0
# Copyright (C) 2013- Zhi Liu
#
# This file is part of pyaibox.
#
# pyaibox is free software: you can redistribute it and/or modify it under the 
# terms of the GNU General Public License as published by the Free Software Foundation, 
# either version 3 of the License, or (at your option) any later version.
#
# pyaibox is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with pyaibox. 
# If not, see <https://www.gnu.org/licenses/>. 
#

import numpy as np


def linear(x):
    r"""linear activation

    .. math::
       y = x

    Parameters
    ----------
    x : lists or array
        inputs

    Returns
    -------
    array
        outputs
    """

    return x


def sigmoid(x):
    r"""sigmoid function

    .. math::
        y = \frac{e^x}{e^x + 1}

    Parameters
    ----------
    x : lists or array
        inputs

    Returns
    -------
    array
        outputs
    """

    ex = np.exp(x)

    return ex / (ex + 1)


def tanh(x):
    r"""tanh function

    .. math::
        y = {\rm tanh}(x) = {{e^{2x} - 1} \over {e^{2x} + 1}}.

    Parameters
    ----------
    x : lists or array
        inputs

    Returns
    -------
    array
        outputs
    """

    # e2x = np.exp(2 * x)
    # return (e2x - 1) / (e2x + 1)

    return np.tanh(x)


def softplus(x):
    r"""softplus function

    .. math::
       {\rm log}(e^x + 1)

    Parameters
    ----------
    x : lists or array
        inputs

    Returns
    -------
    array
        outputs
    """

    return np.log(np.exp(x) + 1)


def softsign(x):
    r"""softsign function

    .. math::
       \frac{x} {({\rm abs}(x) + 1)}

    Parameters
    ----------
    x : lists or array
        inputs

    Returns
    -------
    array
        outputs
    """

    return x / (np.abs(x) + 1)


def elu(x):
    r"""Computes exponential linear element-wise.

    .. math::
        y = \left\{ {\begin{array}{*{20}{c}}{x,\;\;\;\;\;\;\;\;\;x \ge 0}\\{{e^x} - 1,\;\;\;x < 0}\end{array}} \right..

    See  `Fast and Accurate Deep Network Learning by Exponential Linear Units (ELUs) <http://arxiv.org/abs/1511.07289>`_  

    Parameters
    ----------
    x : lists or array
        inputs

    Returns
    -------
    array
        outputs
    """

    return np.where(x < 0, np.exp(x) - 1, x)


def relu(x):
    r"""Computes rectified linear

    .. math::
       {\rm max}(x, 0)

    Parameters
    ----------
    x : lists or array
        inputs

    Returns
    -------
    array
        outputs
    """

    # x[x < 0] = 0
    # return x
    return np.where(x > 0, x, 0)


def relu6(x):
    r"""Computes Rectified Linear 6

    .. math::
       {\rm min}({\rm max}(x, 0), 6)

    `Convolutional Deep Belief Networks on CIFAR-10. A. Krizhevsky <http://www.cs.utoronto.ca/~kriz/conv-cifar10-aug2010.pdf>`_  

    Parameters
    ----------
    x : lists or array
        inputs

    Returns
    -------
    array
        outputs
    """
    maxx = np.where(x > 0, x, 0)
    return np.where(maxx < 6, maxx, 6)


def selu(x):
    r"""Computes scaled exponential linear

    .. math::
        y = \lambda \left\{ {\begin{array}{*{20}{c}}{x, x \ge 0}\\{\alpha ({e^x} - 1), x < 0}\end{array}} \right.
    
    where, :math:`\alpha = 1.6732632423543772848170429916717` , :math:`\lambda = 1.0507009873554804934193349852946`, 
    See `Self-Normalizing Neural Networks <https://arxiv.org/abs/1706.02515>`_

    Parameters
    ----------
    x : lists or array
        inputs

    Returns
    -------
    array
        outputs
    """

    alpha = 1.6732632423543772848170429916717
    scale = 1.0507009873554804934193349852946

    return np.where(x < 0, scale * alpha * (np.exp(x) - 1), scale * x)


def crelu(x):
    r"""Computes Concatenated ReLU.

    Concatenates a ReLU which selects only the positive part of the activation
    with a ReLU which selects only the *negative* part of the activation.
    Note that as a result this non-linearity doubles the depth of the activations.
    Source: `Understanding and Improving Convolutional Neural Networks via
    Concatenated Rectified Linear Units. W. Shang, et
    al. <https://arxiv.org/abs/1603.05201>`_

    Parameters
    ----------
    x : lists or array
        inputs

    Returns
    -------
    array
        outputs
    """

    return x


def leaky_relu(x, alpha=0.2):
    r"""Compute the Leaky ReLU activation function. 

    .. math::
        y = \left\{ {\begin{array}{ccc}{x, x \ge 0}\\{\alpha x, x < 0}\end{array}} \right.

    `Rectifier Nonlinearities Improve Neural Network Acoustic Models <http://web.stanford.edu/~awni/papers/relu_hybrid_icml2013_final.pdf>`_  

    Parameters
    ----------
    x : lists or array
        inputs
    alpha : float
        :math:`\alpha`

    Returns
    -------
    array
        outputs
    """

    return np.where(x < 0, alpha * x, x)


def swish(x, beta=1.0):
    r"""Swish function

    .. math::
       y = x\cdot {\rm sigmoid}(\beta x) = {e^{(\beta x)} \over {e^{(\beta x)} + 1}} \cdot x

    See `"Searching for Activation Functions" (Ramachandran et al. 2017) <https://arxiv.org/abs/1710.05941>`_  

    Parameters
    ----------
    x : lists or array
        inputs
    beta : float
        :math:`\beta`

    Returns
    -------
    array
        outputs
    """

    ex = np.exp(beta * x)

    return (ex / (ex + 1)) * x


if __name__ == '__main__':

    import matplotlib.pyplot as plt

    colors = ['k', 'm', 'b', 'g', 'c', 'r',
              '-.m', '-.b', '-.g', '-.c', '-.r']
    activations = ['linear', 'tanh', 'sigmoid', 'softplus', 'softsign',
                   'elu', 'relu', 'selu', 'relu6', 'leaky_relu', 'swish']
    # 'elu', 'relu', 'selu', 'crelu', 'relu6', 'leaky_relu']
    x = np.linspace(-10, 10, 200)

    # for activation in activations:
    #     print("---show activation: " + activation + "---")
    #     y = globals()[activation](x)
    #     plt.figure()
    #     plt.plot(x, y, 'r')
    #     plt.title(activation + ' activation')
    #     plt.xlabel('x')
    #     plt.ylabel('y')
    #     plt.grid()
    #     plt.show()

    plt.figure()
    for activation, color in zip(activations, colors):
        print("---show activation: " + activation + "---")
        y = globals()[activation](x)
        plt.plot(x, y, color)
    plt.title('activation')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.legend(activations)
    plt.show()