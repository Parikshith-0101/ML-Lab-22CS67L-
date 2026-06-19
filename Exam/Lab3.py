import matplotlib.pyplot as plt



def obj_func(x):
    return -(x**2) + 18*x + 7


def hill_climbing(start, step_size, max_iter):   # Corrected: step_size instead of stepsize
    cur = start
    cur_val = obj_func(cur)                      # Corrected: better variable naming
    path = [(cur, cur_val)]

    print("\nIteration Details:")
    print(f"Step 0 --> x = {cur:.4f}, f(x) = {cur_val:.4f}")
    # Corrected: removed extra 0 and fixed formatting

    for i in range(1, max_iter + 1):            # Corrected: include max_iter properly
        left_nbr = cur - step_size
        right_nbr = cur + step_size

        left_val = obj_func(left_nbr)
        right_val = obj_func(right_nbr)

        print(f"\nStep {i}:")
        print(f"Current x = {cur:.4f}, f(x) = {cur_val:.4f}")
        print(f"Left Neighbour x = {left_nbr:.4f}, f(x) = {left_val:.4f}")
        print(f"Right Neighbour x = {right_nbr:.4f}, f(x) = {right_val:.4f}")

        if left_val > cur_val and left_val >= right_val:
            cur = left_nbr
            cur_val = left_val
            print("Moving Left")

        elif right_val > cur_val and right_val >= left_val:
            # Corrected: used right_val >= left_val for consistency
            cur = right_nbr
            cur_val = right_val
            print("Moving Right")

        else:
            print("Local maxima reached")
            break

        path.append((cur, cur_val))

    return cur, cur_val, path


start = float(input("Enter the starting point: "))
step_size = float(input("Enter the step size: "))
max_iter = int(input("Enter the maximum iterations: "))

best_sol, best_val, path = hill_climbing(start, step_size, max_iter)

print("\nBest Solution Found:", best_sol)
print(f"Maximum value = {best_val:.4f}")