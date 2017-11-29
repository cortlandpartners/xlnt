from setuptools import setup, find_packages

setup(
    name='xlnt',
    version='0.1',
    description='Automate Excel.',
    author='Aaron Fisher',
    packages=find_packages(exclude=['docs', 'tests']),
    install_requires=[
        'xlwings >= 0.10.2',
        'scipy >= 0.18.1',
        'python-dateutil >= 2.6.0',
        'setuptools >= 34.3.3',
        'sphinx_rtd_theme >= 0.2.4'
    ]
)
