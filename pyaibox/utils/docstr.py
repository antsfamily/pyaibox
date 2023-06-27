#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @file      : docstr.py
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

import os
import re
from pyaibox.utils.file import listxfile
from pyaibox.base.baseops import strfind


def gpyi(pkgdir, autoskip=True):
    r"""generates ``pyi`` files

    Parameters
    ----------
    pkgdir : str
        package root directory
    autoskip : bool, optional
        skip ``__init__.py``, by default True
    """    

    filetype = '.py'
    dstfiletype = '.pyi'
    allfiles = listxfile(pkgdir, exts=filetype, recursive=True)
    
    dstfiles = []
    for file in allfiles:
        if autoskip:
            if (file.find('__init__.py') >= 0) or (file.find('version.py') >=0):
                pass
            else:
                dstfiles.append(file)
        else:
            dstfiles.append(file)
            
    for pyfile in dstfiles:
        pyifile = pyfile[:-len(filetype)] + dstfiletype

        fpy = open(pyfile, "r")
        fpyi = open(pyifile, "w")
        data = fpy.readlines()
        cntcomflag = -1
        outstr = []
        for n in range(len(data)):
            defpos = data[n].find('def' + ' ')
            if defpos == -1:
                defpos = data[n].find('class' + ' ')
            if defpos >= 0:
                cntcomflag = 0
                if data[n].find('):') > -1:
                    outstr.append(data[n])
                else:
                    for k in range(len(data[n+1])):
                        if data[n+1][k] != ' ':
                            break
                    outstr.append(data[n][:-1] + data[n+1][k-1:])
                continue
            compos = data[n].find('"' + '"' + '"')
            if compos < 0:
                compos = data[n].find('r"' + '"' + '"')
            if compos >= 0:
                cntcomflag += 1

            if cntcomflag == 1:
                outstr.append(data[n])
            elif cntcomflag == 2:
                outstr.append(data[n] + '\n')
                cntcomflag = -1
        outstr.append('\n')

        if len(outstr) == 0:
            continue

        finalstr = []
        outstr.append('ENDFLAG')
        N = len(outstr)
        for n in range(0, N-1):
            defpos1 = outstr[n].find('def' + ' ')
            defpos2 = outstr[n+1].find('def' + ' ')
            clspos1 = outstr[n].find('class' + ' ')
            clspos2 = outstr[n+1].find('class' + ' ')

            finalstr.append(outstr[n])

            startpos = -1 if (defpos1<0 and clspos1<0) else max(defpos1, clspos1)
            endpos = -1 if (defpos2<0 and clspos2<0) else max(defpos2, clspos2)
            if (startpos>=0 and endpos>=0) or (startpos>=0 and outstr[n+2]=='ENDFLAG'):
                finalstr.append(' '*(startpos + 4) + '...\n\n')

        for ostr in finalstr:
            fpyi.write(ostr)

        fpy.close()
        fpyi.close()

    return 0

def rmcache(pkgdir, exts='.c'):
    r"""remove cache files

    Parameters
    ----------
    pkgdir : str
        package root directory
    ext : str, optional
        file extension
    """

    if exts == '.py':
        raise TypeError("danger!")

    allcfiles = listxfile(pkgdir, exts=exts, recursive=True)
    for file in allcfiles:
        os.remove(file)

    return 0


def dltccmmt(pkgdir, startflag='/*', endflag='*/'):
    """delete block comment in c file

    Parameters
    ----------
    pkgdir : str
        the rootdir
    startflag : str
        start flag of block comment
    endflag : str
        end flag of block comment
    """
    endflaglen = len(endflag)
    allcfiles = listxfile(pkgdir, exts='.c', recursive=True)
    for file in allcfiles:
        output = ''
        with open(file, "r") as f:
            data = f.read()
            f.close()

            starts = strfind(data, startflag)
            ends = strfind(data, endflag)
            Nstarts, Nends = len(starts), len(ends)
            if Nstarts != Nends:
                raise ValueError('Error block comment format!')
            if Nstarts == 0:
                output = data
            else:
                output = data[:starts[0]] + data[ends[0]+endflaglen:starts[1]]
                for i in range(1, Nstarts):
                    output += data[ends[i-1]+endflaglen:starts[i]]
                output += data[ends[-1]+endflaglen:]
        with open(file, "w") as f:
            f.write(output)
            f.close()

    return 0


if __name__ == '__main__':

    pkgdir = '/mnt/e/ws/github/antsfamily/torchcs/torchcs/torchcs/'
    # pkgdir = '/mnt/e/ws/github/antsfamily/pysparse/pysparse/pysparse/'

    dltccmmt(pkgdir)
    # gpyi(pkgdir, autoskip=True)

