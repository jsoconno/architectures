from architectures import Graph, Cluster, Setting

with Graph():
    with Cluster("test") as one:
        one.node('1', 'test 1')

        with Cluster("test") as two:
            two.node('2', 'test 2')