"""
setup.py
"""

from setuptools import setup, find_packages

setup(
    name="DSA",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
