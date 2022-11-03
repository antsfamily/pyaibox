def gpyi(pkgdir, autoskip=True):
    """generates ``pyi`` files

    Parameters
    ----------
    pkgdir : str
        package root directory
    autoskip : bool, optional
        skip ``__init__.py``, by default True
    """    

            defpos = data[n].find('def ') if defpos == -1:
                                       ...

                defpos = data[n].find('class ') if defpos >= 0:
            compos = data[n].find('"""')
            if compos < 0:
                compos = data[n].find('r"""')

        #     if outstr[n].find('def ') > -1: #         if outstr[n].find('):') > -1:
                                     ...

            defpos1 = outstr[n].find('def ') defpos2 = outstr[n+1].find('def ')
                                          ...

            defpos2 = outstr[n+1].find('def ') clspos1 = outstr[n].find('class ')
                                                                             ...

            clspos1 = outstr[n].find('class ') clspos2 = outstr[n+1].find('class ')
                                          ...

            clspos2 = outstr[n+1].find('class ')
                # finalstr.append(' '*(startpos + 4) + 'r"""\n' + ' '*(startpos + 4) + '"""\n\n')
                finalstr.append(' '*(startpos + 4) + '...\n\n')

        for ostr in finalstr:
            fpyi.write(ostr)

        # fpyi.write(finalstr[0])
        # for n in range(1, len(finalstr)):
        #     flag = finalstr[n-1].find('class ') >= 0
        #         flagpos = max(finalstr[n].find('r"""'), finalstr[n].find('"""')) - 1
        #         fpyi.write(finalstr[n][0:flagpos] + '__doc__ = ' + finalstr[n][flagpos:])
        #     else:
        #         fpyi.write(finalstr[n])

        fpy.close()
        fpyi.close()


def rmcache(pkgdir, ext='.c'):
    """remove files

    Parameters
    ----------
    pkgdir : str
        package root directory
    ext : str, optional
        file extension
    """    


