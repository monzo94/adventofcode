from collections import deque


def parse_connections(list):
    """Given a list of connections, returns a dictionary with the list of nodes connected to each key"""
    graph = {}
    for con in list:
        node, other = con.split(' <-> ')
        graph[int(node)] = [int(x) for x in other.split(', ')]
    return graph


def bfs(graph, origin=0):
    """Return a set of nodes reachable from the origin"""
    seen = set()
    queue = deque()

    seen.add(origin)
    queue.append(origin)

    while queue:
        node = queue.popleft()
        for other in graph[node]:
            if other not in seen:
                seen.add(other)
                queue.append(other)

    return seen


def bfs_groups(graph):
    """Returns the total number of groups, a group being a connected component of the graph"""
    seen = set()
    groups = 0

    for node in graph:
        if node not in seen:
            seen.update(bfs(graph, node))
            groups += 1

    return groups


def main():
    with open("input") as f:
        connection_list = [line.strip() for line in f]

    graph = parse_connections(connection_list)
    print("Part 1:", len(bfs(graph)))
    print("Part 2:", bfs_groups(graph))


if __name__ == "__main__":
    main()
