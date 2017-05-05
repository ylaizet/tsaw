from distutils.core import setup

tsaw_version = open("tsaw/VERSION").read().strip()
tsaw_download_url = 'https://github.com/ylaizet/tswa/archive/%s.tar.gz' % tsaw_version

setup(
    name = 'tsaw',
    packages = ['tsaw'],
    version = tsaw_version,
    description = 'TSAW : Torrent Server API Wrapper.',
    long_description=open('README.md').read(),
    author = "Yec'han Laizet",
    author_email = 'y.laizet@bordeaux.unicancer.fr',
    url = 'https://github.com/ylaizet/tsaw',
    download_url = tsaw_download_url,
    license = "GPL3",
    keywords = ['api', 'sequencer', 'Torrent server'],
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ]
)
