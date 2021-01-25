import setuptools
import json
import requests
import re

def get_release_data(user, repo, field=None, regex_pattern=None, group_number=0):
    """
    Extract data from the latest release.
    """
    response = requests.get(f"https://api.github.com/repos/{user}/{repo}/releases/latest")
    release_data_dict = json.loads(response.text)

    if field:
        field_value = release_data_dict[field]
        if regex_pattern is None:
            output = field_value
        else:
            output = re.search(regex_pattern, field_value).group(group_number)
    else:
        output = release_data_dict

    return output

version = get_release_data(user="jsoconno", repo="architectures", field="tag_name", regex_pattern="[0-9]*\.[0-9]*\.[0-9]*")

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
