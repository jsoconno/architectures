from architectures.core import Graph, Cluster, Group, Node, Edge, Flow

with Graph("Neural Network"):
    input_layer = [Node() for i in range(3)]
    with Cluster("Hidden Layers") as hidden_layers:
        hidden_layer_1 = [Node() for i in range(4)]
        hidden_layer_2 = [Node() for i in range(4)]
    output_layer = [Node() for i in range(2)]

    Flow([input_layer, hidden_layer_1, hidden_layer_2, output_layer])