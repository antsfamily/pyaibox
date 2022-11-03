import pyaibox as pb


# pkgdir = '/mnt/e/ws/github/antsfamily/torchcs/torchcs/torchcs/'
pkgdir = '/mnt/e/ws/github/antsfamily/torchtsa/torchtsa/torchtsa/'
pkgdir = '/mnt/e/ws/github/antsfamily/torchbox/torchbox/torchbox/'
# pkgdir = '/mnt/e/ws/github/antsfamily/torchsar/torchsar/torchsar/'
# pkgdir = '/mnt/e/ws/github/antsfamily/pyaibox/pyaibox/pyaibox/'

pb.rmcache(pkgdir, ext='.c')
pb.gpyi(pkgdir, autoskip=True)

