from setuptools import setup
setup(
  name = 'jstn',
  version = '1.0.1',
  packages = ['jstn'],
  entry_points = {
      'console_scripts': [
          'jstn = jstn.__main__:main'
      ]
  })