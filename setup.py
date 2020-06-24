"""
estev.ao
"""
import os
import setuptools
from estev.ao import VERSION

setuptools.setup(
    name="estev.ao-cli",
    version=VERSION,
    author="Nelson Estevão",
    author_email="hello@estevao.xyz",
    description="A CLI to create shortener urls",
    url="https://github.com/nelsonmestevao/estev.ao-cli",
    packages=setuptools.find_packages(),
    install_requires=["docopt==0.6.2", "pyperclip==1.8.0", "requests==2.24.0"],
    entry_points={
        "console_scripts":
        ["estev.ao = estev.ao.cli:main", "estev = estev.ao.cli:main"]
    },
)
