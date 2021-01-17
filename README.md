# Architectures

[![license](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
![python version](https://img.shields.io/badge/python-3.6%2C%203.7%2C%203.8%2C%203.9-blue?logo=python)

## Introduction
Today, almost everything is managed as code including applications, infrastructure, configurations, processes, and more.  Architectures was created to allow teams to manage architecture as code using Python.

The goal for this project is to make drawing architecture diagrams with code simple and to enable the use of version control systems and standard coding practices such as pull requests, code reviews, and approvals to eliminate the toil associated with diagram creation and maintenance.

Architectures comes with support for a wide variety of cloud and on-premise providers out-of-the-box.

![azure provider](https://img.shields.io/badge/provider-Azure-orange?logo=microsoft-azure&color=0089D6)
![aws provider](https://img.shields.io/badge/provider-Amazon%20Web%20Services-orange?logo=amazon-aws&color=232F3E)
![gcp provider](https://img.shields.io/badge/provider-Google%20Cloud%20Platform-orange?logo=google-cloud&color=4285F4)
## Dependencies
Architectures works for all version of python greater than version `3.6.x`.

Architectures can be installed from PyPi using pip:
```
pip install architectures
```
The Graphviz library is also required.  To install it, simply run the following pip command in the terminal:
```
pip install graphviz
```
If you are using a MacBook for development, you may also have to install the latest version of Graphviz with Homebrew:
```
brew install graphviz
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
### Neural Network
Architectures supports the default Graphviz layout as the default.  This means that you can actually use architectures as a replacement for Graphviz to simplify your graph development.

Here is an example of a neural network using the default settings.
#### Code
```
from architectures.core import Graph, Cluster, Group, Node, Edge, Flow

with Graph("Neural Network"):
    input_layer = [Node() for i in range(3)]
    with Cluster("Hidden Layers") as hidden_layers:
        hidden_layer_1 = [Node() for i in range(4)]
        hidden_layer_2 = [Node() for i in range(4)]
    output_layer = [Node() for i in range(2)]

    Flow([input_layer, hidden_layer_1, hidden_layer_2, output_layer])
```
#### Output
!["Architecture"](assets/neural-network.png?raw=true "Architecture")

### Amazon Web Services Microservices Architecture
Architectures supports several providers to make drawing architecture diagrams simple.  It does this by wrapping services into classes than can be called to create resources in your diagram.

It also supports themes to change the look and feel of the diagram you are creating.

Here is an example that shows the use of services and themes together to create an effective diagram.

#### Code
```
from architectures.core import *
from architectures.themes import LightMode

from architectures.providers.aws.storage import SimpleStorageServiceS3
from architectures.providers.aws.network import Cloudfront, ElasticLoadBalancing
from architectures.providers.aws.compute import ElasticContainerService
from architectures.providers.aws.database import Elasticache, Aurora, Dynamodb

theme = LightMode()

with Graph("Simple Microservices Architecture", theme=theme):
    with Cluster("User Interface") as ui:
        storage = SimpleStorageServiceS3()
        cloud_front = Cloudfront()
    with Cluster("Microservices") as microservices:
        elb = ElasticLoadBalancing()
        ecs = ElasticContainerService()
    with Cluster("Data Store") as data_store:
        data_stores = [Elasticache(),Aurora(),Dynamodb()]

    Edge(cloud_front, storage, constraint="false")
    Flow([cloud_front, elb, ecs, data_stores])
```
#### Output
!["Architecture"](assets/simple-microservices-architecture.png?raw=true "Architecture")

### Azure Event Driven Serverless Architecture
Architectures also allows a tremendous amount of flexibility at over diagram look-and-feel.  Here is an example that leverages `dark mode` and keyword arguments on objects to create a clean diagram.

#### Code
```
from architectures.core import *
from architectures.themes import LightMode, DarkMode

from architectures.providers.azure.ai import CognitiveServices
from architectures.providers.azure.application import FunctionApp, EventGridDomain
from architectures.providers.azure.data import AzureCosmosDb
from architectures.providers.azure.general import Computer
from architectures.providers.azure.storage import StorageAccountBlob

theme = DarkMode()

with Graph("Event Driven Serverless Architecture", theme=theme):
    computer = Computer("Single Page Web App")
    with Cluster():
        function_get_upload_url = FunctionApp("Function (get upload url)")
        function_list_images = FunctionApp("Function (list images)")
        function_resize = FunctionApp("Function (resize & recognize image)")
        function_write_metadata = FunctionApp("Function (write metadata)")
    blob_storage = StorageAccountBlob("Blob Storage (images, thumbnails)")
    event_grid = EventGridDomain("Event Grid (async events)")
    cosmos_db = AzureCosmosDb("Cosmos DB (image metadata)")
    cognitive_services = CognitiveServices("Cognitive Services (computer vision)")

    # Flow([function_get_upload_url, function_list_images, function_resize], color="green")
    Flow([computer, [function_get_upload_url, blob_storage, function_list_images]])
    Edge([function_get_upload_url, function_resize], blob_storage)
    Edge(blob_storage, function_resize, style="dashed")
    Edge(function_resize, [cognitive_services, event_grid])
    Edge(event_grid, function_write_metadata, style="dashed")
    Edge(function_write_metadata, cosmos_db)
    Edge(function_list_images, cosmos_db, constraint="false") # This constraint setting ensures the edge does not force ranking
    Edge(function_resize, function_write_metadata, color="invis") # This ensures alignment between these two function apps
```
#### Output
!["Architecture"](assets/event-driven-serverless-architecture.png?raw=true "Architecture")