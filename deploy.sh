# 0. edit ~/.pypirc
gedit ~/.pypirc

if false ; then
[distutils]
index-servers=pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username =
password =
fi

python setup.py sdist

python setup.py build_ext --inplace

# 1. generate whl
python setup.py bdist_wheel --universal

# 2. convert to manylinux
auditwheel repair pyaibox-1.0-cp36-cp36m-linux_x86_64.whl
auditwheel repair pyaibox-1.0-cp37-cp37m-linux_x86_64.whl

# 3. upload to pypi
twine upload dist/*

# https://stackoverflow.com/questions/59451069/binary-wheel-cant-be-uploaded-on-pypi-using-twine
