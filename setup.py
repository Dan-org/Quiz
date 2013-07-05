"""
Django Quiz setup.
"""

from setuptools import setup, find_packages

setup( name='django-quiz',
       version='0.1',
       description='Django app for quizzing.',
       author='Matt Easterday',
       author_email='easterday@northwestern.edu',
       packages = find_packages(),
       include_package_data = True,
       zip_safe = False,
       install_requires = ['django-yamlfield', 'django-ttag']
      )