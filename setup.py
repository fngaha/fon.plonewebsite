from setuptools import setup, find_packages
import os

version = '0.1'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='fon.plonewebsite',
      version=version,
      description="A very basic FON's Plone 4.x website",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='Web Python Zope Plone ngaha',
      author='Franck NGAHA',
      author_email='franck.o.ngaha@gmail.com',
      url='https://github.com/fngaha/fon.plonewebsite',
      license='gpl3',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['fon'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.dexterity [grok]',
          'plone.namedfile [blobs]',
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': [
              'plone.app.testing',
           ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
