from GraphNode import GraphNode, Graph


def dfs_search(root_node, search_value):
    visited = set()  # Sets are faster for lookups
    stack = [root_node]  # Start with a given root node

    while len(stack) > 0:  # Repeat until the stack is empty
        current_node = stack.pop()  # Pop out a node added recently
        visited.add(current_node)  # Mark it as visited

        if current_node.value == search_value:
            return current_node

        # Check all the neighbors
        for child in current_node.children:
            # if not, hasn't been visited before, and not available in the stack yet.
            if child not in visited and child not in stack:
                stack.append(child)


def dfs_recursion_start(start_node, search_value):
    visited = set()  # Set to keep track of visited nodes
    return dfs_recursion(start_node, visited, search_value)


def dfs_recursion(node, visited, search_value):
    if node.value == search_value:
        found = True  # Don't search in other branches, if found = True
        return node

    visited.add(node)
    found = False
    result = None

    # Conditional recurse on each neighbor
    for child in node.children:
        if child not in visited:
            result = dfs_recursion(child, visited, search_value)

            # Once the match is found, no more recurse
            if found:
                break

    return result


if __name__ == '__main__':
    nodeG = GraphNode('G')
    nodeR = GraphNode('R')
    nodeA = GraphNode('A')
    nodeP = GraphNode('P')
    nodeH = GraphNode('H')
    nodeS = GraphNode('S')

    graph1 = Graph([nodeS, nodeH, nodeG, nodeP, nodeR, nodeA])
    graph1.add_edge(nodeG, nodeR)
    graph1.add_edge(nodeA, nodeR)
    graph1.add_edge(nodeA, nodeG)
    graph1.add_edge(nodeR, nodeP)
    graph1.add_edge(nodeH, nodeG)
    graph1.add_edge(nodeH, nodeP)
    graph1.add_edge(nodeS, nodeR)

    # to verify that the graph is created accurately,
    # Let's just print all the parent nodes and child nodes
    for each in graph1.nodes:
        print("Parent Node = ", each.value, end='\nchildren\n')
        for each in each.children:
            print(each.value, end=' ')
        print('\n')

    assert nodeA == dfs_search(nodeS, 'A')
    assert nodeS == dfs_search(nodeP, 'S')
    assert nodeR == dfs_search(nodeH, 'R')

    assert nodeA == dfs_recursion_start(nodeG, 'A')
    assert nodeA == dfs_recursion_start(nodeS, 'A')
    assert nodeS == dfs_recursion_start(nodeP, 'S')
    assert nodeR == dfs_recursion_start(nodeH, 'R')
