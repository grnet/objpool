from distutils.core import setup

from objpool.version import __version__

setup(
    name='objpool',
    version=__version__,
    author='Synnefo development team',
    author_email='synnefo-devel@googlegroups.com',
    packages=['objpool'],
    scripts=[],
    url='https://github.com/grnet/objpool',
    license='LICENSE.txt',
    description='An object pooling library',
    long_description=open('README.txt').read(),
    install_requires=[],
)
