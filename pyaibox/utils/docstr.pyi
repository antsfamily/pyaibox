def gpyi(pkgdir, autoskip=True):
            defpos = dstr.find('def ')
            compos = dstr.find('"""')
            if compos < 0:
                compos = dstr.find('r"""')

