from setuptools import setup, find_namespace_packages

setup(
    name='bennet-observer',
    version='0.1',
    packages=find_namespace_packages(include=['bennet.observer', 'bennet.observer.*']),
    namespace_packages=['bennet'],
    author='Zoltán Benke',
    author_email='benke.zoltan.71@gmail.com',
    url='https://bennet.hu',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
