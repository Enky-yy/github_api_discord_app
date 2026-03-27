import matplotlib.pyplot as plt
import numpy as np

def get_color(count):
    if count == 0:
        return "#161b22"
    elif count < 5:
        return "#0e4429"
    elif count < 10:
        return "#006d32"
    elif count < 20:
        return "#26a641"
    else:
        return "#39d353"


def generate_heatmap(weeks, filename="heatmap.png"):
    grid = []

    for week in weeks:
        row = [day["contributionCount"] for day in week["contributionDays"]]
        row = row + [0] * (7 - len(row))
        grid.append(row)

    grid = np.array(grid).T  # shape → (7, ~53)

    rows, cols = grid.shape

    fig, ax = plt.subplots(figsize=(cols*0.25, rows *0.25))
    fig.patch.set_facecolor("#0d1117")
    ax.set_facecolor("#0d1117")

    # draw squares manually
    for y in range(rows):
        for x in range(cols):
            color = get_color(grid[y][x])
            rect = plt.Rectangle(
                (x, y),
                0.8, 0.8,   # square size
                color=color
            )
            ax.add_patch(rect)

    # spacing and layout
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)

    ax.set_xticks([])
    ax.set_yticks([])

    # remove borders
    for spine in ax.spines.values():
        spine.set_visible(False)

    plt.gca().invert_yaxis()

    plt.savefig(
        filename,
        bbox_inches='tight',
        facecolor=fig.get_facecolor(),
        dpi=200
    )

    plt.close()
    return filename