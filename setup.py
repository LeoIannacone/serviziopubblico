from distutils.core import setup

setup(
    name="Servizio Pubblico",
    version="0.2",
    author="Leo Iannacone",
    author_email="l3on@ubuntu.com",
    description=("Un semplice script scaricare le puntate di Servizio Pubblico"),
    license="GPLv3",
    keywords="video download",
    url="https://github.com/LeoIannacone/serviziopubblico",
    #long_description=read('README.md'),

    scripts=['serviziopubblico/serviziopubblico'],

    data_files=[
        ('share/serviziopubblico', ['README.md', ]), # 'Changelog', 'Authors']),
        ('share/man/man1', ['man/serviziopubblico.1']),
    ],
)
