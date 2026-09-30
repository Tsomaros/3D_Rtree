# 3D R-Tree

A Python implementation of a simple **3D R-Tree** for indexing and querying points in a combined spatial-temporal space.

Each point is represented by three coordinates:
- **X** – spatial coordinate
- **Y** – spatial coordinate
- **T** – temporal coordinate

The tree maintains bounding boxes for its nodes and supports range queries over all three dimensions.

## Features
- 3D point representation using `(x, y, t)`
- R-Tree-style hierarchical node structure
- Bounding-box management for nodes
- Best-fit child selection during insertion
- 3D spatial-temporal range queries
- Intersection-based pruning during searches
- Simple Python implementation with no external dependencies

## How It Works

### Point Insertion
Points are inserted using:

```python
rtree.insert(Point(x, y, t))
```

When a node contains children, the implementation selects the child whose bounding box provides the best fit for the new point. Leaf nodes store the actual points and expand their bounding boxes when new points are inserted.

### Range Search
The tree supports queries over a 3D range:

```python
results = rtree.search(
    min_x, min_y, min_t,
    max_x, max_y, max_t
)
```

Only nodes whose bounding boxes intersect the query range are traversed, reducing unnecessary point checks.

## Example
```python
from 3D_Rtree import Point, RTree

rtree = RTree()
rtree.insert(Point(1, 2, 3))
rtree.insert(Point(4, 5, 6))
rtree.insert(Point(7, 8, 9))

results = rtree.search(0, 0, 0, 5, 5, 7)

for point in results:
    print(point)
```

Example output:
```text
Point(1, 2, 3)
Point(4, 5, 6)
```

## Project Structure
```text
3D_Rtree/
├── 3D_Rtree.py      # R-Tree implementation and example usage
└── 3D-Rtree.docx    # Project documentation
```

## Running the Project
The project uses only Python's standard library, so no additional packages are required.

```bash
git clone https://github.com/Tsomaros/3D_Rtree.git
cd 3D_Rtree
python 3D_Rtree.py
```

## Main Classes
### `Point`
Represents a point in 3D spatial-temporal space: `Point(x, y, t)`.

### `Node`
Represents a tree node and maintains minimum/maximum X, Y, and T coordinates, stored points, and child nodes.

### `RTree`
The main data structure providing `insert(point)` and `search(min_x, min_y, min_t, max_x, max_y, max_t)`.

## Applications
A 3D spatial-temporal index can be useful for spatiotemporal data indexing, moving-object data, GIS, trajectory and event queries, and location-based time-series data.

## License
This project does not currently specify a license.