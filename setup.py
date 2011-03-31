from setuptools import setup, find_packages

def listify(filename):
    return filter(None, open(filename, 'r').readlines())

setup(
    name = "python-smpp",
    version = "0.1",
    url = 'http://github.com/dmaclay/python-smpp',
    license = 'BSD',
    description = "Python SMPP Library",
    long_description = open('README.rst','r').read(),
    author = 'David Maclay',
    author_email = 'dev@praekeltfoundation.org',
    packages = find_packages(),
    install_requires = ['setuptools'].extend(listify('requirements.pip')),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)

