# Runnable examples

Run these commands from the repository root. The examples use NumPy.

## Connected components

Foreground pixels belong to the same region when a path connects them along shared edges (four-neighbour connectivity). In the example mask, the lone foreground pixel in the bottom row touches the three-pixel region only at a corner, so it forms its own region. The script reports the areas in scan order: `[3, 2, 1]` pixels.

```sh
python examples/connected_components.py
```

## Otsu threshold

Find a grey-level threshold that separates a dark background and a bright object.

```sh
python examples/otsu_threshold.py
```
