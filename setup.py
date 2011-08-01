# -*- coding: utf-8 -*-

from os.path import join
from setuptools import setup, find_packages


name = 'dolmen.authentication'
version = '2.0a1'
readme = open('README.txt').read()
history = open(join('docs', 'HISTORY.txt')).read()

install_requires = [
    'cromlech.container',
    'grokcore.component',
    'setuptools',
    'zope.component',
    'zope.i18n',
    'zope.i18nmessageid',
    'zope.interface',
    'zope.schema',
    'zope.security',
    ]

tests_require = [
    'pytest',
    'zope.testing',
    ]

setup(name=name,
      version=version,
      description='Authentication for Cromlech applications',
      long_description=readme[readme.find('\n\n'):] + '\n' + history,
      keywords='Cromlech Dolmen User Authentication',
      author='The Dolmen Team',
      author_email='dolmen@list.dolmen-project.org',
      url='http://www.dolmen-project.org',
      download_url='http://pypi.python.org/pypi/dolmen.authentication',
      license='ZPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['dolmen'],
      include_package_data=True,
      platforms='Any',
      zip_safe=False,
      extras_require={'test': tests_require},
      install_requires=install_requires,
      tests_require=tests_require,
      classifiers=[
          'Programming Language :: Python',
          ],
      )
