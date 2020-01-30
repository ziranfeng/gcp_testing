#!/usr/bin/env python

from setuptools import find_packages, setup

tests_require = [
    'coverage~=4.0.1',
    'freezegun~=0.3.10',
    'pylib_spark==2.0.0',
    'pytest==3.7.2',
    'pytest-cov~=2.5.1',
    'pytest-pep8~=1.0.6'
]

setup(
    name='framework',
    version='0.0.1',
    description='GCP DataScience Project End to End Testing',
    author='Ziran Feng',
    author_email='ziran.feng01@gmail.com',
    package_dir={'framework': 'framework'},
    package_data={'': ['resources/*']},
    packages=find_packages(exclude=['tests', '*.tests', '*.tests.*']),
    python_requires='==3.6.*',
    install_requires=[
        'beautifulsoup4>=4.8.0',
        'geopy>=1.20.0',
        'hyperopt>=0.1.1',
        'ipython>=5.1.0',
        'keras>=2.2.4',
        'matplotlib>=2.0.0',
        'numpy>=1.16.4',
        'pandas>=0.23.0',
        'patsy>=0.4',
        'plotly>=4.0.0',
        'pyarrow>=0.10.0',
        'pytz',
        'scikit-learn>=0.15',
        'scipy>=0.14',
        'tensorflow>=1.14.0',
        'timezonefinder>=4.1.0',
        'tsfresh>=0.10.0'
    ],
    tests_require=tests_require,
    extras_require={
        'test': tests_require,
        'docs': [
            'docutils==0.12',
            'Sphinx==1.2.3',
            'sphinx_py3doc_enhanced_theme==0.1.1',
        ]
    }
)
