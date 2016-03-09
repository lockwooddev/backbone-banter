from setuptools import find_packages, setup


setup(
    name='banter',
    version='0.1.0',
    author='Carlo Smouter',
    url='https://github.com/lockwooddev/backbone-banter.git',
    packages=find_packages('src', exclude=['tests']),
    package_dir={'': 'src'},
    include_package_data=True,
    tests_require=[],
    install_requires=[],
    dependency_links=[],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
