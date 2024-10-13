from setuptools import setup, find_packages

setup(
    name='poke_env',
    version='0.8.1',
    packages=find_packages(),
    install_requires=[
        # This part will be read from pyproject.toml automatically by setuptools
    ],
    # Include additional project settings if needed
)
