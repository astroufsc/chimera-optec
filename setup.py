from distutils.core import setup

setup(
    name='chimera-optec',
    version='0.0.1',
    packages=['chimera_optec', 'chimera_optec.instruments'],
    scripts=[],
    url='http://github.com/astroufsc/chimera-optec',
    license='GPL v2',
    author='William Schoenell',
    author_email='william@iaa.es',
    install_requires=['pyserial'],
    description='Chimera plugin for OPTEC focusers'
)
