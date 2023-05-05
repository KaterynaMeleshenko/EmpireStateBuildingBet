import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import HTML

np.random.seed(21)


def random_walk():
    """Generate and return a list of 100 results of dice rollings where the first element is always 0 and
    others are according to the rules:
    - if rolled number is 1 or 2, the element is 1 point less than the previous element, but not less than 0;
    - if rolled number is 3, 4, or 5, the element is 1 point more than the previous element.
    - if rolled number is 6, the die is thrown again and the element is equel to the rolled number.
    """
    random_walk = [0]

    for x in range(100):
        step = random_walk[-1]
        dice = np.random.randint(1, 7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1, 7)

        # Implementing clumsiness
        if np.random.rand() <= 0.001:
            step = 0

        random_walk.append(step)

    return random_walk


def all_walks(iteration_number=100):
    """Generate and return a transposed list of 100 values lists.

    Keyword argument:
    iteration_number -- number of 100 values lists in the final list (default 100)
    """
    all_walks = []

    for i in range(iteration_number):
        walk = random_walk()
        all_walks.append(walk)

    np_aw = np.array(all_walks)
    np_aw_transposed = np.transpose(np_aw)

    return np_aw_transposed


def walk_results(iteration_number=100):
    """Find final steps of generated walks.

    Keyword argument:
    iteration_number -- number of final steps (default 100)
    """
    final_steps = all_walks(iteration_number)[-1, :]

    return final_steps


# Fixing bin edges
HIST_BINS = np.linspace(0, 160, 80)

# Histogram our data with numpy
data = walk_results(1000)
n, _ = np.histogram(data, HIST_BINS)


def prepare_animation(bar_container):
    def animate(frame_number):
        # Simulating new data coming in
        data = walk_results(1000)
        n, _ = np.histogram(data, HIST_BINS)
        for count, rect in zip(n, bar_container.patches):
            rect.set_height(count)
        return bar_container.patches

    return animate


fig, ax = plt.subplots()
_, _, bar_container = ax.hist(
    data, HIST_BINS, lw=1, ec="#9e6a97", fc="#756597", alpha=0.5
)

# Setting safe limit to ensure that all data is visible.
ax.set_ylim(top=80)

ani = animation.FuncAnimation(
    fig, prepare_animation(bar_container), 100, repeat=False, blit=True
)

plt.title("Distribution of Results")
plt.xlabel("Steps")
plt.ylabel("Frequency")

HTML(ani.to_jshtml(default_mode="loop"))
