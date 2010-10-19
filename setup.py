from setuptools import setup, find_packages

setup(
    name = "python-smpp",
    version = "0.1",
    url = 'http://github.com/dmaclay/python-smpp',
    license = 'BSD',
    description = "Python SMPP Library",
    author = 'David Maclay',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = [],
)

