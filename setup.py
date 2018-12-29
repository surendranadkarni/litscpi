import setuptools
from litscpi.version import Version

setuptools.setup(name='litscpi',
                 version=Version('0.0.1').number,
                 description='Python Package for SCPI',
                 long_description=open('README.md').read().strip(),
                 author='Surendra Nadkarni',
                 author_email='surennadkarni@gmail.com',
                 url='https://github.com/surendranadkarni/litscpi',
                 py_modules=['litscpi'],
                 package_dir = {'': 'litscpi'},
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords='SCPI',
                 classifiers=["Development Status :: 1 - Alpha", "Topic :: Utilities"])

