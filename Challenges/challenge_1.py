import sys


def read_graph(filename):
    """ Read and parse file containing Graph information"""

    with open(filename, "r") as file:
        graph_info = file.read().split("/n")

    return graph_info


def construct_graph(filename):
    """ Construct graph based on information in the filename """
