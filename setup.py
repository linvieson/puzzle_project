import setuptools

with open('README.md', 'r', encoding = 'utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'puzzle-Alina-Voronina',
    version = '0.0.1',
    author = 'Alina Voronina',
    author_email = 'alina.voronina@ucu.edu.ua',
    description = 'A paskage to validate if the combination on the board is ready for the game or not.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/linvieson/puzzle_project.git',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming language :: Python :: 3',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: Windows 10',
    ],
    python_requires = '>=3.8',
)