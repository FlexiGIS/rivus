from distutils.core import setup
from rivus import __version__

setup(name='rivus',
      version=__version__,
      description='Does some nice optimization',
      author='Johannes Dorfner',
      #author_email='mike@stamen.com',
      #url='https://github.com/migurski/Skeletron',
      #requires=['networkx', 'StreetNames'],
      packages=['rivus'],
      scripts=['skeletron-generalize.py',
               'skeletron-hadoop-mapper.py',
               'skeletron-hadoop-reducer.py',
               'skeletron-osm-route-rels.py',
               'skeletron-osm-streets.py'],
    # download_url='https://github.com/downloads/migurski' % locals(),
      license='GPL-3')