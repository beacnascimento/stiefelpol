from setuptools import setup

setup(
    name='stiefelpol',
    version='0.0.1',
    description='A library for generating random polygons in the plane',
    author='Beatriz Nascimento',
    author_email='b247403@dac.unicamp.br',
    url='https://github.com/beacnascimento/stiefelpol',
    license='MIT',
    packages=['stiefelpol', 'stiefelpol.utils'],
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
    ],
)
