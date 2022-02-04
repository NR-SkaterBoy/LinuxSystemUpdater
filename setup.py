from setuptools import setup

# Setup
with open("./README.md", "r", encoding="utf-8") as readme_file:
    long_des = readme_file.read()

setup(
    name="Linux System Update",
    version="0.0.1",
    description="You can update your system with it moreover it can save your time",
    long_description=long_des,
    long_description_content_type="text/markdown",
    author="NR-SkaterBoy",
    author_email="nr.rick.dev@gmail.com",
    license="MIT",
    packages=["lsu"],
    package_dir={"lsu": "bash/"}
)