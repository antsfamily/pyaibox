def gpyi(pkgdir, autoskip=True):
            defpos = dstr.find('def ')
                defpos = dstr.find('class ')
            compos = dstr.find('"""')
            if compos < 0:
                compos = dstr.find('r"""')

