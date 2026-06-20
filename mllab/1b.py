def objective(x):
    return -(x - 5) ** 2 + 25
def hill_climbing(start):
    current = start
    while True:
        left = current - 1
        right = current + 1
        if objective(left) > objective(current):
            current = left
        elif objective(right) > objective(current):
            current = right
        else:
            return current, objective(current)
start_state = 0
best_state, best_value = hill_climbing(start_state)
print("Start State:", start_state)
print("Best State:", best_state)
print("Maximum Value:", best_value)