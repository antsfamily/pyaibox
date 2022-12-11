#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : convert.py
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

import re
import hashlib
from ast import literal_eval


def str2hash(s, hmode='sha256', enc='utf-8', tohex=True):
    r"""convert a string to hash code

    Parameters
    ----------
    s : str
        the input.
    hmode : str or hash function, optional
        must either be a hash algorithm name as a str, a hash constructor, or a callable that returns a hash object.
         ``'sha1'``, ``'sha224'``, ``'sha256'``, ``'sha384'``, ``'sha512'``, ``'md5'``, ..., 
        see `hashlib <https://docs.python.org/3/library/hashlib.html?highlight=new#module-hashlib>`_ , by default 'sha256'
    enc : str, optional
        encoding type, by default 'utf-8'.
    tohex : bool, optional
        return hex code?, by default :obj:`True`.

    Returns
    -------
    str or object
        hash code hex string or hash object.
    """
    
    hmode = eval('hashlib.' + hmode) if type(hmode) is str else hmode
    digesth = hmode(s.encode(enc))
    if tohex:
        return digesth.hexdigest()
    else:
        return digesth

def file2hash(file, hmode='sha256', tohex=True):
    r"""convert contents of a file to hash code

    Parameters
    ----------
    file : str
        the input file path string.
    hmode : str or hash function, optional
        must either be a hash algorithm name as a str, a hash constructor, or a callable that returns a hash object.
         ``'sha1'``, ``'sha224'``, ``'sha256'``, ``'sha384'``, ``'sha512'``, ``'md5'``, ..., 
        see `hashlib <https://docs.python.org/3/library/hashlib.html?highlight=new#module-hashlib>`_ , by default 'sha256'
    tohex : bool, optional
        return hex code?, by default :obj:`True`.

    Returns
    -------
    str or object
        hash code hex string or hash object
    """

    with open(file, "rb") as f:
        hmode = eval('hashlib.' + hmode) if type(hmode) is str else hmode
        digesth = hmode(f.read())
    if tohex:
        return digesth.hexdigest()
    else:
        return digesth

def dict2str(ddict, indent='  ', linebreak='\n', nindent=0):
    r"""dump dict object to str

    Parameters
    ----------
    ddict : dict
        The dict object to be converted
    indent : str, optional
        The dict identifier, by default ``'  '``
    linebreak : str, optional
        The line break character, by default '\n'
    nindent : int, optional
        the number of initial indent characters, by default 0

    Returns
    -------
    str
        The converted string.
    """
    
    dstr = ''
    for k, v in ddict.items():
        dstr += indent * nindent
        dstr += k + ': '
        if type(v) is dict:
            dstr += linebreak
            nindent += 1
            dstr += dict2str(v, indent=indent, nindent=nindent)
            nindent = 0
        elif v is None:
            dstr += 'Null' + linebreak
        else:
            dstr += str(v) + linebreak
    return dstr


def str2list(s):
    r"""Converts string with ``[`` and ``]`` to list

    Parameters
    ----------
    s : str
        The string.

    Examples
    --------

    ::

        s = '[0, [[[[1], 2.], 33], 4], [5, [6, 2.E-3]], 7, [8]], 1e-3'
        print(str2list(s))

        # ---output
        ([0, [[[[1], 2.0], 33], 4], [5, [6, 0.002]], 7, [8]], 0.001)


    """
    # left = [i.start() for i in re.finditer(r'\[', s)]
    # print(left)
    # right = [i.start() for i in re.finditer(r'\]', s)]
    # print(right)

    # nlevel = -1
    # for l in left:
    #     nlevel += 1
    #     if l > right[0]:
    #         break
    # right[0:nlevel - 1] = right[0:nlevel - 1][::-1]
    # right.insert(0, right.pop())
    # print(right)

    return literal_eval(s)

def str2num(s, tfunc=None):
    r"""Extracts numbers in a string.

    Parameters
    ----------
    s : str
        The string.
    tfunc : None, optional
        formating function, such as ``int``, ``float`` or ``'auto'``.

    Returns
    -------
    list
        The number list.

    Examples
    --------

    ::

        print(str2num(s, int))
        print(str2num(s, float))
        print(str2num(s, 'auto'))

        print(2**(str2num('int8', int)[0]))
        print(str2num('int', int) == [])
        
        # ---output
        [0, 1, 2, 33, 4, 5, 6, 0, 7, 8, 0]
        [0.0, 1.0, 2.0, 33.0, 4.0, 5.0, 6.0, 0.002, 7.0, 8.0, 0.001]
        [0, 1, 2.0, 33, 4, 5, 6, 0.002, 7, 8, 0.001]
        256
        True
    """
    numstr = re.findall(r'-?\d+\.?\d*e*E?[-+]?\d*', s)
    if tfunc is None:
        return numstr
    else:
        if tfunc == 'auto':
            numlist = []
            for num in numstr:
                if num.find('.') > -1 or num.find('e') > -1:
                    numlist.append(float(num))
                else:
                    numlist.append(int(float(num)))
            return numlist
        else:
            return [tfunc(float(i)) for i in numstr]


def str2sec(x, sep=':'):
    r"""Extracts second in a time string.
        
        ``hh:mm:ss``  -->  ``hh*3600 + mm*60 + ss``

    Parameters
    ----------
    s : str
        The string or string list/tuple.
    sep : str
        The separator between hour, minute and seconds, default is ``':'``.

    Returns
    -------
    y : int
        The seconds.

    Examples
    --------

    ::

        print(str2sec('1:00:0'))
        print(str2sec('1:10:0'))
        print(str2sec('1:10:6'))
        print(str2sec('1:10:30'))
        
        # ---output
        3600
        4200
        4206
        4230
    """
    if type(x) is str:
        h, m, s = x.strip().split(sep)
        return int(h) * 3600 + int(m) * 60 + int(s)
    
    if (type(x) is list) or (type(x) is tuple):
        y = []
        for xi in x:
            h, m, s = xi.strip().split(sep)
            y.append(int(h) * 3600 + int(m) * 60 + int(s))
        return y


def int2bstr(n, nbytes, endian='<', signed=True):
    r"""converts integer to bytes string

    Parameters
    ----------
    n : int
        the input integer
    nbytes : int
        the number of bytes
    endian : str, optional
        byte order, supported are little endian: ``'<'`` (the default), big endian: ``'>'``.
    signed : bool, optional
        signed or unsigned, by default True

    Returns
    -------
    bstr
        The integer in binary string format.

    Examples
    --------

    ::

        n = -123

        bs = int2bstr(n, 4, '<', signed=True)
        print(bs)
        print(hex(n))
        print(bstr2int(bs, '<'))

        bs = int2bstr(n, 4, '>', signed=True)
        print(bs)
        print(hex(n))
        print(bstr2int(bs, '>'))

        # ---output
        b'\x85\xff\xff\xff'
        -0x7b
        -123
        b'\xff\xff\xff\x85'
        -0x7b
        -123

    """    

    if endian.lower() in ['<', 'little', 'l', 'lit']:
        endian = 'little'
    if endian.lower() in ['>', 'big', 'b', 'bigger']:
        endian = 'big'

    return n.to_bytes(nbytes, endian, signed=signed)


def bstr2int(b, endian='<', signed=True):
    r"""convert binary string data to integer

    Parameters
    ----------
    b : bstr
        an integer in binary format
    endian : str, optional
        The order of the bytes, supported are little endian: ``'<'`` (the default), big endian: ``'>'``.
    signed : bool, optional
        signed or unsigned, by default True
    
    Returns
    -------
    int
        The integer in decimal.

    Examples
    --------

    ::

        n = -123

        bs = int2bstr(n, 4, '<', signed=True)
        print(bs)
        print(hex(n))
        print(bstr2int(bs, '<'))

        bs = int2bstr(n, 4, '>', signed=True)
        print(bs)
        print(hex(n))
        print(bstr2int(bs, '>'))

        # ---output
        b'\x85\xff\xff\xff'
        -0x7b
        -123
        b'\xff\xff\xff\x85'
        -0x7b
        -123

    """

    if endian.lower() in ['<', 'little', 'l', 'lit']:
        endian = 'little'
    if endian.lower() in ['>', 'big', 'b', 'bigger']:
        endian = 'big'

    return int.from_bytes(b, endian, signed=signed)


if __name__ == '__main__':

    s = '[0, [[[[1], 2.], 33], 4], [5, [6, 2.E-3]], 7, [8]], 1e-3'

    print(str2list(s))

    print(str2num(s, int))
    print(str2num(s, float))
    print(str2num(s, 'auto'))

    print(2**(str2num('int8', int)[0]))
    print(str2num('int', int) == [])

    print(str2sec('1:00:0'))
    print(str2sec('1:10:0'))
    print(str2sec('1:10:6'))
    print(str2sec('1:10:30'))

    n = -123

    bs = int2bstr(n, 4, '<', signed=True)
    print(bs)
    print(hex(n))
    print(bstr2int(bs, '<'))

    bs = int2bstr(n, 4, '>', signed=True)
    print(bs)
    print(hex(n))
    print(bstr2int(bs, '>'))

    print(str2hash('123456ABCDEFG', 'md5'), 'md5')
    print(file2hash('deploy.sh', 'md5'), 'md5')