import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
name = 'nse_fno_expiry_calculator',
packages=setuptools.find_packages(),
version = '1.0.1',
include_package_data=True,
description = 'Util to calculate expiry date for FNO instruments which also considers NSE holiday calendar.',
long_description=long_description,
long_description_content_type="text/markdown",  author = 'Rakesh Ravikumar Kashyap',
author_email = 'rakesh1988@gmail.com',
url = 'https://github.com/rakesh1988/nse-fno-expiry-calculator.git',
install_requires=['pendulum'],
keywords = ['nse', 'expiry', 'nse fno', 'nse holiday', 'trading', 'stock markets'],
python_requires='>=3.6',
classifiers=[
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Software Development :: Libraries :: Python Modules'
],
)