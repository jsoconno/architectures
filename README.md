# Architectures

[![license](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
![python version](https://img.shields.io/badge/python-3.6%2C3.7%2C3.8-blue?logo=python)
[![todos](https://badgen.net/https/api.tickgit.com/badgen/github.com/mingrammer/diagrams?label=todos)](https://www.tickgit.com/browse?repo=github.com/jsoconno/architectures)

![default provider](https://img.shields.io/badge/provider-Default-orange?color=C70039)
![azure provider](https://img.shields.io/badge/provider-Azure-orange?logo=microsoft-azure&color=007FFF)

<a href="https://www.buymeacoffee.com/jsoconno" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## Introduction
In a IT organization far, far away where everything is managed as code...

Including applications, infrastructure, processes, configurations, and more...

Architecture diagrams were left behind requiring architects and developers to search for the correct versions of documents stored on local servers across the organization...

Architectures was designed to help technical teams work better together to build architecture as code and overcome the evil visio diagrams grip on the universe.
## Design Goals
The overarching goal of this project is to allow for the development of architecture as code that can be stored in version control allowing teams to better collaborate and leverage standard coding practices such as pull requests, code reviews, approvals, etc to maintain architecture diagrams.

Architectures has been designed to be simple, powerful, extendable and scalable so that anyone in the technology organization can contribute to diagram development.  It is also an attempt to eliminate the toil associated with diagram creation and support a wide variety of cloud and on-premise providers out-of-the-box.

## Dependencies
Python version 3.6.x or later must be installed.

The graphviz library is also required.  To install with Python, simply run the following command in the terminal:
```
pip install graphviz
```

## Supported Objects
There are several types of supported objects in the architectures library.  These objects primarily fall into three categories:
### Containers
- **Graphs** allow users to create a base canvas to create their diagram on
- **Clusters** allow users to group **Nodes** into bounded container
- **Groups** allow users to logically group **Nodes** with no bounding container
### Components
- **Nodes** allow users to create an object that represents a service
### Connections
- **Edges** allow users to draw a line between a pair or list of **Nodes**, **Clusters**, or **Groups**
- **Flows** allow users to create a linear flow through a list of **Nodes**, **Clusters**, or **Groups**

The component objects are extended with subclasses that allow for the creation of standard service components from various providers such as Azure, GCP, and AWS.

## Examples
Coming Soon
