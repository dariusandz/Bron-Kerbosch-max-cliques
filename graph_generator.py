from string import ascii_uppercase
from node import Node
from random import randint
import json

def find_node_by_name(nodes, str):
    for node in nodes:
        if node.name == str:
            return node


def read_file_as_dict(filename):
    with open(filename) as f:
        dictionary = json.load(f)
    return dictionary

def get_random_neighbor_names(count):
    if (count > 28):
        return list(map(chr, range(0, count)))
    else:
        return list(ascii_uppercase[:count])


def get_random_neighbors(nodes, node_name):
    neighbor_names = get_random_neighbor_names(len(nodes))
    neighbor_names.remove(node_name)
    neighbor_count = randint(0, len(nodes) - 1)
    neighbors = []
    for name in range(neighbor_count):
        index = randint(0, len(neighbor_names)-1)
        rand_name = neighbor_names[index]
        neighbor_names.remove(rand_name)
        neighbor = find_node_by_name(nodes, rand_name)
        neighbors.append(neighbor)

    return neighbors


def random_graph(vertices):
    node_names = get_random_neighbor_names(vertices)
    all_nodes = []
    for name in node_names:
        all_nodes.append(Node(name))

    for node in all_nodes:
        node_neighbors = get_random_neighbors(all_nodes, node.name)
        node.neighbors = node_neighbors

    return all_nodes


def read_graph(filename):
    graph = read_file_as_dict(filename)

    all_nodes = []
    for key in graph:
        all_nodes.append(Node(key))

    for node in all_nodes:
        node_neighbors = []
        for neighbor in graph[node.name]:
            node_neighbor = find_node_by_name(all_nodes, neighbor)
            node_neighbors.append(node_neighbor)
        node.neighbors = node_neighbors

    return all_nodes
