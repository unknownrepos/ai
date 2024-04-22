import math

# Define the game tree as a dictionary
game_tree = {
    'A': {'value': None, 'children': ['B', 'C', 'D']},
    'B': {'value': None, 'children': ['E', 'F', 'G']},
    'C': {'value': None, 'children': ['H', 'I', 'J']},
    'D': {'value': None, 'children': ['K', 'L', 'M']},
    'E': {'value': 3, 'children': []},
    'F': {'value': 12, 'children': []},
    'G': {'value': 8, 'children': []},
    'H': {'value': 2, 'children': []},
    'I': {'value': 4, 'children': []},
    'J': {'value': 6, 'children': []},
    'K': {'value': 14, 'children': []},
    'L': {'value': 5, 'children': []},
    'M': {'value': 7, 'children': []}
}

# Define the players
MAX_PLAYER = 'Max'
MIN_PLAYER = 'Min'

def minimax(node, depth, player, alpha, beta):
    if depth == 0 or not node['children']:
        return node['value']
    
    if player == MAX_PLAYER:
        max_eval = -math.inf
        for child in node['children']:
            eval = minimax(game_tree[child], depth - 1, MIN_PLAYER, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = math.inf
        for child in node['children']:
            eval = minimax(game_tree[child], depth - 1, MAX_PLAYER, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval

# Example usage
best_score = minimax(game_tree['A'], 3, MAX_PLAYER, -math.inf, math.inf)
print("Best score for Max player:", best_score)

