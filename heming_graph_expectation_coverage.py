import itertools
import random
import math
import matplotlib.pyplot as plt
from scipy.special import comb


def hamming_distance(u, v):
    return sum(x != y for x, y in zip(u, v))


def get_hamming_ball(v, t, vertices):
    return {u for u in vertices if hamming_distance(u, v) <= t}


def ball_size(n, t):
    return sum(comb(n, i, exact=True) for i in range(t + 1))


def expected_steps(n, t):
    B_t = ball_size(n, t)
    return (2 ** n) / B_t * (n * math.log(2) + 0.5772156649)  # Using math.euler_gamma for better precision


def simulate_hamming_graph(n, t):
    vertices = {tuple(map(int, format(i, f'0{n}b'))) for i in range(2 ** n)}
    covered = set()
    steps = 0

    while covered != vertices:
        v = random.choice(list(vertices))
        new_covered = get_hamming_ball(v, t, vertices)
        covered |= new_covered
        steps += 1

    return steps


if __name__ == "__main__":
    n = int(input("Enter n (1-7): "))
    t = int(input(f"Enter t (0-{n}): "))

    if not (0 <= t <= n and 1 <= n <= 7):
        print("Invalid input. Ensure 0 <= t <= n and 1 <= n <= 7.")
    else:
        runs = 100  # Reduced to 100 iterations
        results = [simulate_hamming_graph(n, t) for _ in range(runs)]
        expected = expected_steps(n, t)

        plt.figure(figsize=(10, 6))
        plt.scatter(range(runs), results, color='blue', alpha=0.6, label='Simulated Runs')
        plt.axhline(expected, color='red', linestyle='dashed', linewidth=2, label=f'Expected ({expected:.2f})')
        plt.xlabel("Simulation Run Number")
        plt.ylabel("Steps to Cover Graph")
        plt.title(f"Simulation Results (n={n}, t={t}, {runs} runs)")
        plt.legend()
        plt.savefig("hamming_graph_simulation.png")  # Save the plot as an image file
        print("Graph saved as 'hamming_graph_simulation.png'")
