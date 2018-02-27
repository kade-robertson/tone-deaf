from setuptools import setup, find_packages

import tone_deaf

long_desc = ""
try:
    import pypandoc
    long_desc = pypandoc.convert('README.md', 'rst', extra_args = ('--eol', 'lf'))
except(IOError, ImportError):
    long_desc = open('README.md').read()

setup(
    name = "tone-deaf",
    version = "0.2.0",
    description = "An interpreter for the tone-deaf programming language.",
    long_description = long_desc,
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ],
    entry_points = {
        'console_scripts': [
            'tone-deaf = tone_deaf:main'
        ]
    },
    keywords = "tone deaf esoteric programming language interpreter",
    author = "Kade Robertson",
    author_email = "kade@kaderobertson.pw",
    url = "https://github.com/kade-robertson/tone-deaf",
    license = "MIT",
    packages = find_packages(),
    install_requires = [],
    python_requires = '>=3.4, <4'
)
