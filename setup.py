from setuptools import setup

# Setup
with open("./README.md", "r", encoding="utf-8") as readme_file:
    long_des = readme_file.read()

setup(
    name='Linux System Updater',
    version='1.0',
    author='SkaterBoy',
    author_email="nr.rick.dev@gmail.com",
    packages=["lsu"],
    setup_requires=['setuptools'],
)