def pca(x, axisn=0, ncmpnts='auto99%', algo='svd'):
    r"""Principal Component Analysis (pca) on raw data

    Parameters
    ----------
    x : array
        the input data
    axisn : int, optional
        the axis of number of samples, by default 0
    ncmpnts : int or str, optional
        the number of components, by default ``'auto99%'``
    algo : str, optional
        the kind of algorithms, by default ``'svd'``

    Returns
    -------
    array
        U, S, K (if :attr:`ncmpnts` is integer)

    Examples
    --------

    .. image:: ./_static/MNISTPCA_ORIG.png
       :scale: 100 %
       :align: center

    .. image:: ./_static/MNISTPCA_K70.png
       :scale: 100 %
       :align: center

    .. image:: ./_static/MNISTPCA_K90.png
       :scale: 100 %
       :align: center

    The results shown in the above figure can be obtained by the following codes.

    ::

        import numpy as np
        import pyaibox as pb

        rootdir, dataset = '/mnt/d/DataSets/oi/dgi/mnist/official/', 'test'
        x, _ = pb.read_mnist(rootdir=rootdir, dataset=dataset, fmt='ubyte')
        print(x.shape)
        N, M2, _ = x.shape

        u, s, k = pb.pca(x, axisn=0, ncmpnts='auto90%', algo='svd')
        print(u.shape, s.shape, k)
        u = u[:, :k]
        y = x.reshape(N, -1) @ u  # N-k
        z = y @ u.T.conj()
        z = z.reshape(N, M2, M2)
        print(pb.nmse(x, z, axis=(1, 2)))
        xp = np.pad(x[:35], ((0, 0), (1, 1), (1, 1)), 'constant', constant_values=(255, 255))
        zp = np.pad(z[:35], ((0, 0), (1, 1), (1, 1)), 'constant', constant_values=(255, 255))
        plt = pb.imshow(pb.patch2tensor(xp, (5*(M2+2), 7*(M2+2)), axis=(1, 2)), titles=['Orignal'])
        plt = pb.imshow(pb.patch2tensor(zp, (5*(M2+2), 7*(M2+2)), axis=(1, 2)), titles=['Reconstructed' + '(90%)'])

        u, s, k = pb.pca(x, axisn=0, ncmpnts='auto0.7', algo='svd')
        print(u.shape, s.shape, k)
        u = u[:, :k]
        y = x.reshape(N, -1) @ u  # N-k
        z = y @ u.T.conj()
        z = z.reshape(N, M2, M2)
        print(pb.nmse(x, z, axis=(1, 2)))
        zp = np.pad(z[:35], ((0, 0), (1, 1), (1, 1)), 'constant', constant_values=(255, 255))
        plt = pb.imshow(pb.patch2tensor(zp, (5*(M2+2), 7*(M2+2)), axis=(1, 2)), titles=['Reconstructed' + '(70%)'])
        plt.show()

        u, s = pb.pca(x, axisn=0, ncmpnts=2, algo='svd')
        print(u.shape, s.shape)
        y = x.reshape(N, -1) @ u  # N-k
        z = y @ u.T.conj()
        z = z.reshape(N, M2, M2)
        print(pb.nmse(x, z, axis=(1, 2)))

    """


