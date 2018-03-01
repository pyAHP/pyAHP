from setuptools import setup, find_packages

setup(
    name='pyAHP',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.14.0',
        'scipy>=1.0.0'
    ],
    author='Abhinav Mishra',
    author_email='mishrabhinav96@gmail.com',
    description='Analytic Hierarchy Process solver',
    license='MIT',
    url='https://github.com/pyAHP/pyAHP',
    keywords='ahp analytic hierarchy process',
    python_requires='>=3'
)
