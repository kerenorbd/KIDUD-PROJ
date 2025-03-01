import itertools
import random
import math

def hamming_distance(u, v):
    return sum(x != y for x, y in zip(u, v))

def get_hamming_ball(v, t, vertices):
    return {u for u in vertices if hamming_distance(u, v) <= t}

def expected_steps(n, t):
    H2 = lambda x: -x * math.log2(x) - (1 - x) * math.log2(1 - x) if 0 < x < 1 else 0
    return 2 ** (n * (1 - H2(t / n))) * (n * math.log(2) + 0.5772156649)  # Gamma ≈ 0.5772

def simulate_hamming_graph(n, t):
    if not (0 <= t <= n and 1 <= n <= 7):
        print("Invalid input. Ensure 0 <= t <= n and 1 <= n <= 7.")
        return

    vertices = {tuple(map(int, format(i, f'0{n}b'))) for i in range(2**n)}
    covered = set()
    steps = 0

    print(f"Simulating Hamming graph with n={n}, t={t}\n")

    while covered != vertices:
        v = random.choice(list(vertices))
        new_covered = get_hamming_ball(v, t, vertices)
        covered |= new_covered
        steps += 1

        print(f"Step {steps}: Chose {v}, Covered so far: {len(covered)} / {len(vertices)}")

    exp_steps = expected_steps(n, t)
    print(f"\nGraph fully covered in {steps} steps (Expected: {exp_steps:.2f})")

if __name__ == "__main__":
    n = int(input("Enter n (1-7): "))
    t = int(input(f"Enter t (0-{n}): "))
    simulate_hamming_graph(n, t)