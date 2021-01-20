import glob
import os
import pytest

from architectures.core import Graph, Cluster, Group, Node, Edge, Flow
from architectures.core import wrap_text

from architectures.themes import Default


@pytest.mark.parametrize("test_input, expected", [
    ("short name", "short name"),
    ("little longer name", " little longer\nname"),
    ("an even longer name than that", " an even longer\nname than that")
])
def test_wrap_text(test_input, expected):
    assert wrap_text(test_input) == expected


class TestGraph:
    @classmethod
    def setup_class(cls):
        cls.default_graphname = "my-architecture"
        cls.default_ext = ".png"
        cls.default_filename = cls.default_graphname + cls.default_ext
    
    @classmethod
    def teardown_class(cls):
        for graph_image in glob.glob(f"*{cls.default_ext}"):
            os.remove(graph_image)

    def test_default_filename(self):
        with Graph(show=False):
            Node("A")
        assert os.path.exists(self.default_filename)

    def test_custom_filename(self):
        graph_name = "Custom Name"
        with Graph(graph_name, show=False):
            Node("A")
        expected_filename = "-".join(graph_name.split()).lower() + self.default_ext
        assert os.path.exists(expected_filename)

    def test_default_ext(self):
        graph_name = "test_ext"
        with Graph(graph_name, show=False):
            Node("A")
        assert self.default_ext in glob.glob(graph_name + self.default_ext)[0]

    def test_default_theme(self):
        graph_name = "test_theme"
        theme = Default()
        with Graph(graph_name, theme=theme, show=False) as graph:
            Node("A")
        assert isinstance(graph.theme, Default)

    def test_theme_override(self):
        graph_name = "test_theme_override"
        theme = Default(graph_attr_overrides={"rankdir":"LR"})
        with Graph(graph_name, theme=theme) as graph:
            Node("A")
        assert graph.theme.graph_attrs["rankdir"] == "LR"


class TestCluster:
    @classmethod
    def setup_class(cls):
        cls.default_graphname = "my-architecture"
        cls.default_ext = ".png"
        cls.default_filename = cls.default_graphname + cls.default_ext
    
    @classmethod
    def teardown_class(cls):
        for graph_image in glob.glob(f"*{cls.default_ext}"):
            os.remove(graph_image)

    def test_cluster_graph_context(self):
        with pytest.raises(EnvironmentError):
            Cluster("A")


class TestNode:
    @classmethod
    def setup_class(cls):
        cls.default_graphname = "my-architecture"
        cls.default_ext = ".png"
        cls.default_filename = cls.default_graphname + cls.default_ext

    @classmethod
    def teardown_class(cls):
        for graph_image in glob.glob(f"*{cls.default_ext}"):
            os.remove(graph_image)

    def test_node_graph_context(self):
        with pytest.raises(EnvironmentError):
            Node("A")


class TestEdge:
    @classmethod
    def setup_class(cls):
        cls.default_graphname = "my-architecture"
        cls.default_ext = ".png"
        cls.default_filename = cls.default_graphname + cls.default_ext

    @classmethod
    def teardown_class(cls):
        for graph_image in glob.glob(f"*{cls.default_ext}"):
            os.remove(graph_image)

    def test_node_to_node(self):
        with Graph(show=False):
            node_a = Node("A")
            node_b = Node("B")
            with Cluster() as cluster_a:
                node_c = Node("C")
                node_d = Node("D")
            with Cluster() as cluster_b:
                node_e = Node("E")

            Edge(node_a, node_b)  # node to node
            Edge(node_b, node_c)  # node to node within cluster
            Edge(node_c, node_d)  # node to node within the same cluster
            Edge(node_d, node_e)  # node to node within different clusters

            with pytest.raises(TypeError):
                Edge(node_a, "node_b")

            with pytest.raises(TypeError):
                Edge("node_a", node_b)

    def test_node_to_nodes(self):
        with Graph(show=False):
            node_a = Node("A")
            with Cluster() as cluster_a:
                node_b = Node("B")
            with Cluster() as cluster_b:
                node_c = Node("C")

            Edge(node_a, [node_b, node_c])  # node to list of nodes
            Edge([node_a, node_b], node_c)  # list of nodes to node

            with pytest.raises(TypeError):
                Edge(node_a, [node_b, "node_c"])

            with pytest.raises(TypeError):
                Edge([node_a, "node_b"], node_c)
    
    def test_node_to_cluster(self):
        with Graph(show=False):
            node_a = Node("A")
            with Cluster() as cluster_a:
                node_b = Node("B")
            with Cluster() as cluster_b:
                Node("C")
            with Cluster() as cluster_c:
                Node("D")

            Edge(node_a, cluster_a)  # node to cluster
            Edge(node_b, cluster_b)  # node within cluster to cluster
            Edge(node_a, [cluster_b, cluster_c])  # node to list of clusters
            
    def test_cluster_to_cluster(self):
        with Graph(show=False):
            with Cluster() as cluster_a:
                Node("A")
            with Cluster() as cluster_b:
                Node("B")

            Edge(cluster_a, cluster_b)  # cluster to cluster
            Edge(cluster_b, cluster_a)

            with pytest.raises(TypeError):
                Edge(cluster_a, "cluster_b")

            with pytest.raises(TypeError):
                Edge("cluster_a", cluster_b)

    def test_cluster_to_clusters(self):
        with Graph(show=False):
            with Cluster() as cluster_a:
                Node("A")
            with Cluster() as cluster_b:
                Node("B")
            with Cluster() as cluster_c:
                Node("C")

            Edge(cluster_a, [cluster_b, cluster_c])  # cluster to list of clusters
            Edge([cluster_a, cluster_b], cluster_c)

            with pytest.raises(TypeError):
                Edge(cluster_a, [cluster_b, "cluster_c"])

            with pytest.raises(TypeError):
                Edge([cluster_a, "cluster_b"], cluster_c)

    def test_cluster_to_node(self):
        with Graph(show=False):
            with Cluster() as cluster_a:
                Node("A")
            with Cluster() as cluster_b:
                node_b = Node("B")
            node_c = Node("C")
            
            Edge(cluster_a, node_b)  # cluster to node within cluster
            Edge(cluster_b, node_c)  # cluster to node

 
class TestFlow:
    @classmethod
    def setup_class(cls):
        cls.default_graphname = "my-architecture"
        cls.default_ext = ".png"
        cls.default_filename = cls.default_graphname + cls.default_ext
        
    @classmethod
    def teardown_class(cls):
        for graph_image in glob.glob(f"*{cls.default_ext}"):
            os.remove(graph_image)

    def test_flow_between_nodes(self):
        with Graph(show=False):
            node_a = Node("A")
            node_b = Node("B")
      
            Flow([node_a, node_b])

    def test_flow_between_clusters(self):
        with Graph(show=False):
            with Cluster() as cluster_a:
                Node("A")
            with Cluster() as cluster_b:
                Node("B")
         
            Flow([cluster_a, cluster_b])

    def test_flow_between_nodes_and_clusters(self):
        with Graph(show=False):
            with Cluster() as cluster_a:
                Node("A")
            with Cluster() as cluster_b:
                Node("B")
            node_c = Node("C")
        
            Flow([cluster_a, cluster_b, node_c])

    def test_flow_num_arguments(self):
        with Graph(show=False):
            node_a = Node("A")
            
            with pytest.raises(Exception):
                Flow([node_a])

# TO-DO
class TestGroup:
    @classmethod
    def setup_class(cls):
        cls.default_graphname = "my-architecture"
        cls.default_ext = ".png"
        cls.default_filename = cls.default_graphname + cls.default_ext
    
    @classmethod
    def teardown_class(cls):
        for graph_image in glob.glob(f"*{cls.default_ext}"):
            os.remove(graph_image)

