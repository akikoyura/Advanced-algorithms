import sys

from Graph import Graph


def dijkstra(graph, source):
    # Declare and initialize a result, unvisited, and path
    result = {source: 0}

    for node in graph.nodes:
        if node != source:
            result[node] = sys.maxsize

    unvisited = set(graph.nodes)

    path = {}

    # As long as unvisited is non-empty?
    while unvisited:
        min_node = None
        # 1. Find the unvisited node having the smallest known distance from the source node.
        for node in unvisited:
            if node in result:
                if min_node is None:
                    min_node = node
                elif result[node] < result[min_node]:
                    min_node = node

        if min_node is None:
            break

        # know the distance of min_node
        current_distance = result[min_node]

        # 2. For the current node, find all the unvisited neighbors.
        # For this, you have calculated the distance of each unvisited neighbor.
        for neighbor in graph.neighbors[min_node]:
            if neighbor in unvisited:
                distance = current_distance + graph.distances[(min_node, neighbor)]
                # 3. If the calculated distance of the unvisited neighbor is less than the already known distance
                # in the result dictionary, update the shortest distance in the result dictionary.
                if (neighbor not in result) or (distance < result[neighbor]):
                    result[neighbor] = distance

                # 4. If there is an update in the result dictionary, you need to update
                # the path dictionary as well for the same key.
                path[neighbor] = min_node

        # 5. Remove the current node from the unvisited set.
        unvisited.remove(min_node)

    return result


if __name__ == '__main__':
    # Test 1
    testGraph = Graph()
    for node in ['A', 'B', 'C', 'D', 'E']:
        testGraph.add_node(node)

    testGraph.add_edge('A', 'B', 3)
    testGraph.add_edge('A', 'D', 2)
    testGraph.add_edge('B', 'D', 4)
    testGraph.add_edge('B', 'E', 6)
    testGraph.add_edge('B', 'C', 1)
    testGraph.add_edge('C', 'E', 2)
    testGraph.add_edge('E', 'D', 1)

    print(dijkstra(testGraph, 'A'))  # {'A': 0, 'D': 2, 'B': 3, 'E': 3, 'C': 4}

    # Test 2
    graph = Graph()
    for node in ['A', 'B', 'C']:
        graph.add_node(node)

    graph.add_edge('A', 'B', 5)
    graph.add_edge('B', 'C', 5)
    graph.add_edge('A', 'C', 10)

    print(dijkstra(graph, 'A'))  # {'A': 0, 'C': 10, 'B': 5}

    # Test 3
    graph = Graph()
    for node in ['A', 'B', 'C', 'D', 'E', 'F']:
        graph.add_node(node)

    graph.add_edge('A', 'B', 5)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('D', 'C', 1)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('A', 'D', 2)
    graph.add_edge('B', 'F', 2)
    graph.add_edge('C', 'F', 3)
    graph.add_edge('E', 'F', 2)
    graph.add_edge('C', 'E', 1)

    print(dijkstra(graph, 'A'))  # {'A': 0, 'C': 3, 'B': 5, 'E': 4, 'D': 2, 'F': 6}
