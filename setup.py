import setuptools
try:
   import pypandoc
   long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
   long_description = open('README.md').read()

setuptools.setup(
    scripts=['bin/ai-benchmark'],
    long_description_content_type="text/markdown",

    long_description=README,
    packages=setuptools.find_packages(),
)
