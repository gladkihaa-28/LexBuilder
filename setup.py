from setuptools import setup, find_packages

def readme():
  with open('README.md', 'r') as f:
    return f.read()

setup(
  name='LexBuilder',
  version='1.3.0',
  author='Alexander554',
  author_email='gaa.28112008@gmail.com',
  description='Library for automatic construction of lexers',
  long_description=readme(),
  long_description_content_type='text/markdown',
  packages=find_packages(),
  install_requires=[''],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='lexbuilder python c++ lexer',
  python_requires='>=3.7'
)