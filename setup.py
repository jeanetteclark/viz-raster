from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    author='Robyn Thiessen-Bock, Juliet Cohen',
    author_email='thiessenbock@nceas.ucsb.edu, jcohen@nceas.ucsb.edu',
    name='pdgraster',
    version='0.9.2',
    description='Rasterization to GeoTiff and web-based tiles for the PDG '
                'Visualization pipeline',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/PermafrostDiscoveryGateway/viz-raster',
    packages=['pdgraster'],
    install_requires=[
        'numpy >= 1.2, < 2',
        'shapely >= 2, < 3',
        'geopandas >= 0.12.2, < 1',
        'coloraide >= 0.10, < 1',
        'Pillow >= 9, < 10',
        'morecantile >= 3.1, < 4',
        'Rtree >= 0.9, < 1',
        'rasterio >= 1.2, < 2',
        'pydantic == 1.10.9',
        'pdgstaging @ git+https://github.com/PermafrostDiscoveryGateway/viz-staging.git#egg=pdgstaging',
        'colormaps == 0.4.0'
    ],
    python_requires='>=3.9, <4',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    license='Apache Software License 2.0',
)
