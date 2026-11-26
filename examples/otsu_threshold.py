"""Find a grey-level threshold that separates a dark background and a bright object."""
import numpy as np


def otsu_threshold(image):
    """Return the first threshold maximising between-class variance for a uint8 image."""
    if image.dtype != np.uint8 or image.size == 0:
        raise ValueError("Expected a non-empty uint8 image")
    counts = np.bincount(image.ravel(), minlength=256)
    lower_count = counts.cumsum()
    upper_count = image.size - lower_count
    valid = (lower_count > 0) & (upper_count > 0)
    if not valid.any():
        return int(image.flat[0])

    sums = (counts * np.arange(256)).cumsum()
    separation = np.zeros(256)
    mean_dark = sums[valid] / lower_count[valid]
    mean_light = (sums[-1] - sums[valid]) / upper_count[valid]
    separation[valid] = lower_count[valid] * upper_count[valid] * (mean_dark - mean_light) ** 2
    return int(separation.argmax())


if __name__ == "__main__":
    image = np.array([[8, 10, 12], [190, 205, 220]], dtype=np.uint8)
    threshold = otsu_threshold(image)
    mask = image > threshold
    assert mask.tolist() == [[False] * 3, [True] * 3]
    print(f"Threshold {threshold}, foreground pixels {mask.sum()}/{image.size}")
