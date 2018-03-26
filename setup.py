from setuptools import setup, Extension, find_packages
from sysconfig import get_paths


# boost_python_lib = '/usr/local/boost_1_65_1/stage/lib/'
python_include = get_paths()['include']

compile_args = ['-g', '-std=c++1z', '-stdlib=libc++', ]
link_args = []  # ['-mmacosx-version-min=10.12']

extension = Extension(name='machina.src.core',
                      sources=['machina/src/core.cpp'],
                      include_dirs=[python_include],
                      # library_dirs=[boost_python_lib],
                      libraries=['boost_python3'],
                      extra_compile_args=compile_args,
                      extra_link_args=link_args,
                      language='c++')


setup(name='Machina',
      version='0.0.1',
      author='Zi Wang',
      author_email='guzzii316@gmail.com',
      packages=find_packages(),
      install_requires=['matplotlib', 'seaborn', 'pandas', 'numpy'],
      license='Use as you wish. No guarantees whatsoever.',
      ext_modules=[extension])
