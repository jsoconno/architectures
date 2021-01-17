from architectures.core import *
from architectures.themes import LightMode

from architectures.providers.aws.storage import SimpleStorageServiceS3
from architectures.providers.aws.network import Cloudfront, ElasticLoadBalancing
from architectures.providers.aws.compute import ElasticContainerService
from architectures.providers.aws.database import Elasticache, Aurora, Dynamodb

theme = LightMode()

with Graph("Simple Microservices Architecture", theme=theme):
    with Cluster("User Interface") as ui:
        storage = SimpleStorageServiceS3("Amazon S3")
        cloud_front = Cloudfront()
    with Cluster("Microservices") as microservices:
        elb = ElasticLoadBalancing("ELB")
        ecs = ElasticContainerService("ECS")
    with Cluster("Data Store") as data_store:
        data_stores = [Elasticache(),Aurora(),Dynamodb()]

    Edge(cloud_front, storage, constraint="false")
    Flow([cloud_front, elb, ecs, data_stores])