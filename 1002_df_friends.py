#Lab Assignment 2:

# Example Graph
graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for i in graph[start]:
        if i not in visited:
            dfs(graph, i, visited)

print("DFS starting from A:")
dfs(graph, 'A')
print()

# Bonus:
student_name = input("Enter student name to start DFS: ").strip().upper()
if student_name in graph:
    dfs(graph, student_name)
else:
    print("Student not found in the graph.")




