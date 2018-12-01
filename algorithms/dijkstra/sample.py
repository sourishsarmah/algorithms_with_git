from dijkstra import Graph, dijkstra


def main():
    count = int(input("Enter no of vertices = "))
    g = Graph(count)

    edgeCount = int(input("Enter no of edges = "))
    for i in range(0, edgeCount):
        src, dest, weight = map(int, input().split())
        g.addEdge(src, dest, weight)

    src = int(input("Enter source node = "))
    dest = int(input("Enter destination node = "))
    shortest_path, distance = dijkstra(g, src, dest)
    print("Shortest Path : ")
    print(shortest_path)
    print(f"Shortest Distance = {distance}")


if __name__ == "__main__":
    main()
