def read_mnist(rootdir, dataset='test', fmt='ubyte'):
    r"""read mnist dataset

    The data can be downloaded from http://yann.lecun.com/exdb/mnist/

    Parameters
    ----------
    rootdir : str
        root directory path string of mnist dataset 
    dataset : str, optional
        dataset to be read, ``'test'`` or ``'train'``, by default ``'test'``.
    fmt : str, optional
        the dataset formation, ``'ubyte'`` (original) or ``'image'``, by default ``'ubyte'``.

    Returns
    -------
    list or tuple
        X : array
            image data
        Y : array
            label data
    
    Examples
    --------

    Read and show digital MNIST images

    .. image:: ./_static/mnist.png
       :scale: 100 %
       :align: center

    The results shown in the above figure can be obtained by the following codes.

    ::

        import pyaibox as pb

        rootdir = '/mnt/d/DataSets/oi/dgi/mnist/pics/'
        dataset = 'test'
        X, Y = pb.read_mnist(rootdir=rootdir, dataset=dataset, fmt='image')
        print(X.shape, Y.shape)

        rootdir = '/mnt/d/DataSets/oi/dgi/mnist/official/'
        dataset = 'train'
        X, Y = pb.read_mnist(rootdir=rootdir, dataset=dataset, fmt='ubyte')
        print(X.shape, Y.shape)
        plt = pb.imshow([X[i] for i in range(0, 32)])
        plt.show()

        dataset = 'test'
        X, Y = pb.read_mnist(rootdir=rootdir, dataset=dataset, fmt='ubyte')
        print(X.shape, Y.shape)
        plt = pb.imshow([X[i] for i in range(0, 32)])
        plt.show()

        # output
        (10000, 28, 28) (10000,)
        (60000, 28, 28) (60000,)
        (10000, 28, 28) (10000,)


    Read and show Fasion MNIST images

    .. image:: ./_static/fashionmnist.png
       :scale: 100 %
       :align: center

    The results shown in the above figure can be obtained by the following codes.

    ::

        import pyaibox as pb

        rootdir = '/mnt/d/DataSets/oi/dgi/fashionmnist/official/'
        dataset = 'train'
        X, Y = pb.read_mnist(rootdir=rootdir, dataset=dataset, fmt='ubyte')
        print(X.shape, Y.shape)

        plt = pb.imshow([X[i] for i in range(0, 32)])
        plt.show()

        dataset = 'test'
        X, Y = pb.read_mnist(rootdir=rootdir, dataset=dataset, fmt='ubyte')
        print(X.shape, Y.shape)

        plt = pb.imshow([X[i] for i in range(0, 32)])
        plt.show()

    """


