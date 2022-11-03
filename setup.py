#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2015-2030, Zhi Liu.  All rights reserved.

from os import path as os_path
import pyaibox
from setuptools import setup
from setuptools import find_packages
from Cython.Build import cythonize
from Cython.Distutils import Extension
from pyaibox.version import __version__

this_dir = os_path.abspath(os_path.dirname(__file__))

py_extensions = [
              Extension("pyaibox.misc.draw_shapes", ['pyaibox/misc/draw_shapes.py']), 
              Extension("pyaibox.misc.noising", ['pyaibox/misc/noising.py']),
              Extension("pyaibox.misc.sampling", ['pyaibox/misc/sampling.py']),
              Extension("pyaibox.misc.transform", ['pyaibox/misc/transform.py']),
              Extension("pyaibox.misc.mapping_operation", ['pyaibox/misc/mapping_operation.py']),
              Extension("pyaibox.dsp.ffts", ['pyaibox/dsp/ffts.py']),
              Extension("pyaibox.dsp.convolution", ['pyaibox/dsp/convolution.py']),
              Extension("pyaibox.dsp.correlation", ['pyaibox/dsp/correlation.py']),
              Extension("pyaibox.dsp.function_base", ['pyaibox/dsp/function_base.py']),
              Extension("pyaibox.dsp.normalsignals", ['pyaibox/dsp/normalsignals.py']),
              Extension("pyaibox.evaluation.contrast", ['pyaibox/evaluation/contrast.py']),
              Extension("pyaibox.evaluation.entropy", ['pyaibox/evaluation/entropy.py']),
              Extension("pyaibox.evaluation.error", ['pyaibox/evaluation/error.py']),
              Extension("pyaibox.evaluation.norm", ['pyaibox/evaluation/norm.py']),
              Extension("pyaibox.evaluation.snrs", ['pyaibox/evaluation/snrs.py']),
              Extension("pyaibox.utils.colormaps", ['pyaibox/utils/colormaps.py']),
              Extension("pyaibox.utils.colors", ['pyaibox/utils/colors.py']),
              Extension("pyaibox.utils.convert", ['pyaibox/utils/convert.py']),
              Extension("pyaibox.utils.file", ['pyaibox/utils/file.py']),
              Extension("pyaibox.utils.image", ['pyaibox/utils/image.py']),
              Extension("pyaibox.utils.ios", ['pyaibox/utils/ios.py']),
              Extension("pyaibox.utils.plot_show", ['pyaibox/utils/plot_show.py']),
]

c_extensions = [
              Extension("pyaibox.misc.draw_shapes", ['pyaibox/misc/draw_shapes.c']), 
              Extension("pyaibox.misc.noising", ['pyaibox/misc/noising.c']),
              Extension("pyaibox.misc.sampling", ['pyaibox/misc/sampling.c']),
              Extension("pyaibox.misc.transform", ['pyaibox/misc/transform.c']),
              Extension("pyaibox.misc.mapping_operation", ['pyaibox/misc/mapping_operation.c']),
              Extension("pyaibox.dsp.ffts", ['pyaibox/dsp/ffts.c']),
              Extension("pyaibox.dsp.convolution", ['pyaibox/dsp/convolution.c']),
              Extension("pyaibox.dsp.correlation", ['pyaibox/dsp/correlation.c']),
              Extension("pyaibox.dsp.function_base", ['pyaibox/dsp/function_base.c']),
              Extension("pyaibox.dsp.normalsignals", ['pyaibox/dsp/normalsignals.c']),
              Extension("pyaibox.evaluation.contrast", ['pyaibox/evaluation/contrast.c']),
              Extension("pyaibox.evaluation.entropy", ['pyaibox/evaluation/entropy.c']),
              Extension("pyaibox.evaluation.error", ['pyaibox/evaluation/error.c']),
              Extension("pyaibox.evaluation.norm", ['pyaibox/evaluation/norm.c']),
              Extension("pyaibox.evaluation.snrs", ['pyaibox/evaluation/snrs.c']),
              Extension("pyaibox.utils.colormaps", ['pyaibox/utils/colormaps.c']),
              Extension("pyaibox.utils.colors", ['pyaibox/utils/colors.c']),
              Extension("pyaibox.utils.convert", ['pyaibox/utils/convert.c']),
              Extension("pyaibox.utils.file", ['pyaibox/utils/file.c']),
              Extension("pyaibox.utils.image", ['pyaibox/utils/image.c']),
              Extension("pyaibox.utils.ios", ['pyaibox/utils/ios.c']),
              Extension("pyaibox.utils.plot_show", ['pyaibox/utils/plot_show.c']),
]

def read_file(filename):
    with open(os_path.join(this_dir, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
        if not line.startswith('#')]


long_description = read_file('README.md'),
long_description_content_type = "text/markdown",

try:
  cythonize(py_extensions)
  setup(name='pyaibox',
        version=pyaibox.__version__,
        description="Python Library.",
        author='Zhi Liu',
        author_email='zhiliu.mind@gmail.com',
        url='https://iridescent.ink/pyaibox/',
        download_url='https://github.com/antsfamily/pyaibox/',
        license='MIT',
        packages=find_packages(),
        install_requires=read_requirements('requirements.txt'),
        include_package_data=True,
        keywords=['Python', 'Library', 'Digital signal processing', 'Tool'],
        ext_modules=cythonize(c_extensions)
        )
except:
  setup(name='pyaibox',
        version=pyaibox.__version__,
        description="Python Library.",
        author='Zhi Liu',
        author_email='zhiliu.mind@gmail.com',
        url='https://iridescent.ink/pyaibox/',
        download_url='https://github.com/antsfamily/pyaibox/',
        license='MIT',
        packages=find_packages(),
        install_requires=read_requirements('requirements.txt'),
        include_package_data=True,
        keywords=['Python', 'Library', 'Digital signal processing', 'Tool'],
        )
