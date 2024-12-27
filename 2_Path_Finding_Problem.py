from collections import deque

# BFS and DFS Pathfinding
def uninformed_path_finder(cities, roads, start_city, goal_city, strategy):
    if strategy.lower() == 'bfs':
        return bfs_path_finder(roads, start_city, goal_city)
    elif strategy.lower() == 'dfs':
        return dfs_path_finder(roads, start_city, goal_city)
    else:
        raise ValueError("Invalid strategy. Choose 'bfs' or 'dfs'.")

def bfs_path_finder(roads, start_city, goal_city):
    queue = deque([(start_city, [start_city], 0)])  # (current city, path, cost)
    visited = set()

    while queue:
        current_city, path, cost = queue.popleft()
        
        if current_city in visited:
            continue
        visited.add(current_city)

        # Goal check
        if current_city == goal_city:
            return path, cost

        # Explore neighbors
        for neighbor, distance in roads.get(current_city, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor], cost + 1))
    
    return None, float('inf')  # If no path is found

def dfs_path_finder(roads, start_city, goal_city):
    stack = [(start_city, [start_city], 0)]  # (current city, path, cost)
    visited = set()

    while stack:
        current_city, path, cost = stack.pop()
        
        if current_city in visited:
            continue
        visited.add(current_city)

        # Goal check
        if current_city == goal_city:
            return path, cost

        # Explore neighbors
        for neighbor, distance in roads.get(current_city, []):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor], cost + 1))
    
    return None, float('inf')  # If no path is found

# Input Data
cities = ['Addis Ababa', 'Bahir Dar', 'Gondar', 'Hawassa', 'Mekelle']
roads = {
    'Addis Ababa': [('Bahir Dar', 510), ('Hawassa', 275)],
    'Bahir Dar': [('Addis Ababa', 510), ('Gondar', 180)],
    'Gondar': [('Bahir Dar', 180), ('Mekelle', 300)],
    'Hawassa': [('Addis Ababa', 275)],
    'Mekelle': [('Gondar', 300)]
}

# Start and goal cities
start_city = input('Insert Start City: ')
goal_city = input('Insert Goal City: ')

# Call BFS
path, cost = uninformed_path_finder(cities, roads, start_city, goal_city, strategy='bfs')
print(f"BFS Result: Path - {path}, Cost (steps) - {cost}")

# Call DFS
path, cost = uninformed_path_finder(cities, roads, start_city, goal_city, strategy='dfs')
print(f"DFS Result: Path - {path}, Cost (steps) - {cost}")
