import os
import setuptools

command = r"""
curl --silent "https://api.github.com/repos/jsoconno/architectures/releases/latest" | 
grep '"tag_name":' | 
sed -E 's/.*"v([^"]+)".*/\1/'   
"""

version = os.popen(command).read().strip()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="architectures",
    version=version,
    author="Justin O'Connor",
    author_email="jsoconno@gmail.com",
    description="Tools for creating architecture as code using Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jsoconno/architectures",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
