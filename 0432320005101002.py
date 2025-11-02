import heapq

'''
heapq is a Python module that provides a priority queue implementation using a min-heap.
It allows you to always pop the element with the lowest priority value efficiently (in O(log n) time).
'''

'''
def a_star_search(graph, start, goal, heuristic):
This defines a function called a_star_search with:
graph: a dictionary showing nodes and their neighbors with edge costs.
start: the node where the search begins.
goal: the node we want to reach.
heuristic: a dictionary (or function) giving each node a heuristic value — an estimate of how close it is to the goal.
'''

def a_star_search(graph, start, goal, heuristic):
    # Priority queue stores (f_score, current_node, path, g_cost)
    pq = []
    heapq.heappush(pq, (heuristic[start], start, [start], 0))  # f = g + h, here g=0 for start

    visited = set()  # Track visited nodes

    while pq:  # Continue while queue not empty
        (f, current, path, g) = heapq.heappop(pq)
        print(f"Visiting: {current} (f={f}, g={g}, h={heuristic[current]})")

        if current == goal:  # Goal reached
            return path, g  # Return both path and total cost
            #f(goal)=g(goal)+h(goal)=g(goal)+0=g(goal)

        if current in visited:
            continue
        visited.add(current)

        for neighbor, cost in graph[current].items():  # Each neighbor with travel cost
            if neighbor not in visited:
                g_new = g + cost  # Actual cost so far
                f_new = g_new + heuristic[neighbor]  # Total estimated cost
                heapq.heappush(pq, (f_new, neighbor, path + [neighbor], g_new))

    return None, float('inf')  # No path found


# ---- Example usage ----

# Step 1: Define a weighted graph (edges have costs)
graph = {
    'A': {'B': 6, 'F': 3},
    'B': {'A': 6, 'C': 3, 'D': 2},
    'C': {'B': 3, 'D': 1, 'E': 5},
    'D': {'B': 2, 'C': 1, 'E': 8},
    'E': {'C': 5, 'D': 8, 'I': 5, 'J': 5},
    'F': {'A': 3, 'G': 1, 'H': 7},
    'G': {'F': 1, 'I': 3},
    'H': {'F': 7, 'I': 2},
    'I': {'E': 5, 'G': 3, 'H': 2, 'J': 3},
    'J': {'E': 5, 'I': 3}
}

# Step 2: Define heuristic values (estimated cost to goal 'F')
# Typically Euclidean or straight-line distance to goal
heuristic = {
    'A': 10,
    'B': 8,
    'C': 5,
    'D': 7,
    'E': 3,
    'F': 6,
    'G': 5,
    'H': 3,
    'I': 1,
    'J': 0
}

# Step 3: Call the function
path, total_cost = a_star_search(graph, 'A', 'J', heuristic)

# Step 4: Print the result
print("Path found:", path)
print("Total cost:", total_cost)



