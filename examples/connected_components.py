"""Count foreground regions using horizontal and vertical pixel neighbours."""
from collections import deque

import numpy as np


def component_areas(mask):
    """Return each region's area in scan order using a four-neighbour flood fill."""
    remaining = np.array(mask, dtype=bool, copy=True)
    height, width = remaining.shape
    areas = []
    for row, col in np.ndindex(remaining.shape):
        if not remaining[row, col]:
            continue
        remaining[row, col] = False
        queue = deque([(row, col)])
        area = 0
        while queue:
            y, x = queue.popleft()
            area += 1
            for ny, nx in ((y-1, x), (y+1, x), (y, x-1), (y, x+1)):
                if 0 <= ny < height and 0 <= nx < width and remaining[ny, nx]:
                    remaining[ny, nx] = False
                    queue.append((ny, nx))
        areas.append(area)
    return areas


if __name__ == "__main__":
    areas = component_areas([[1, 1, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0]])
    assert areas == [3, 2, 1]  # Diagonally touching pixels belong to separate regions.
    print("Region areas in pixels:", areas)
