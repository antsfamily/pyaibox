#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-02-23 07:01:55
# @Author  : Zhi Liu (zhiliu.mind@gmail.com)
# @Link    : http://iridescent.ink
# @Version : $1.0$


from pyaibox import listxfile


def gpyi(pkgdir, autoskip=True):

    filetype = '.py'
    dstfiletype = '.pyi'
    allfiles = listxfile(pkgdir, filetype, recursive=True)
    
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
        flag = False
        cntcomflag = -1
        for dstr in data:
            defpos = dstr.find('def ')
            if defpos == -1:
                defpos = dstr.find('class ')
            if defpos >= 0:
                cntcomflag = 0
                fpyi.write(dstr)
                continue
            compos = dstr.find('"""')
            if compos < 0:
                compos = dstr.find('r"""')
            if compos >= 0:
                cntcomflag += 1

            if (cntcomflag < 2) and (cntcomflag >= 1) :
                fpyi.write(dstr)
            elif cntcomflag == 2:
                fpyi.write(dstr)
                fpyi.write('\n')
                cntcomflag = -1

        fpy.close()
        fpyi.close()


if __name__ == '__main__':

    pkgdir = '/mnt/e/ws/github/antsfamily/torchbox/torchbox/torchbox/'
    pkgdir = '/mnt/e/ws/github/antsfamily/torchsar/torchsar/torchsar/'

    gpyi(pkgdir, autoskip=True)

