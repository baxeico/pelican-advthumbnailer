from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

version = '0.7.0'

setup(

    # Basic package information:
    name = 'pelican-advthumbnailer',
    version = version,
    py_modules = ('advthumbnailer',),

    # Packaging options:
    zip_safe = False,
    include_package_data = True,

    # Package dependencies:
    install_requires = ['pelican>=3.4.0', 'beautifulsoup4>=4.3.2', 'Pillow>=2.5.3'],

    # Metadata for PyPI:
    author = 'Alexandre Fonseca',
    author_email = 'alexandrejorgefonseca@gmail.com',
    license = 'Apache',
    url = 'https://github.com/AlexJF/pelican-advthumbnailer',
    download_url = 'https://github.com/AlexJF/pelican-advthumbnailer/archive/v{version}.zip'.format(version=version),
    keywords = 'pelican blog static thumbnail generation',
    description = ('A thumbnail generator for Pelican that operates by looking'
            ' at the filename of missing files to determine thumb format.'),
    long_description = long_description
)
