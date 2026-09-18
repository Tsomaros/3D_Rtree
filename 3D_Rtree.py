class Point:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.t = t

    def __str__(self):
        return f'Point({self.x}, {self.y}, {self.t})'


class Node:
    def __init__(self, min_x, min_y, min_t, max_x, max_y, max_t, data=None, children=None):
        self.min_x = min_x
        self.min_y = min_y
        self.min_t = min_t
        self.max_x = max_x
        self.max_y = max_y
        self.max_t = max_t
        self.data = data or []
        self.children = children or []

    def insert(self, point):
        #  If the node has no children, the point is added to the node's data
        if len(self.children) == 0:
            self.data.append(point)
            self._expand_bounds(point)

        # If the node has children, the method finds the best-fit child node for the point, and inserts the point
        # into that node.
        else:
            child = self._get_best_fit(point)
            child.insert(point)

    #  searches for all points that fall within a given 3D range and returns a list of Point objects.
    def search(self, min_x, min_y, min_t, max_x, max_y, max_t):
        results = []
        if self._intersects(min_x, min_y, min_t, max_x, max_y, max_t):
            if len(self.children) == 0:
                results += [p for p in self.data if
                            min_x <= p.x <= max_x and min_y <= p.y <= max_y and min_t <= p.t <= max_t]
            else:
                for child in self.children:
                    results += child.search(min_x, min_y, min_t, max_x, max_y, max_t)
        return results

    # find the best-fit child node for the point
    def _get_best_fit(self, point):
        best_fit = None
        min_diff = float('inf')
        for child in self.children:
            diff = child.get_bounding_box_difference(point)
            if diff < min_diff:
                best_fit = child
                min_diff = diff
        return best_fit

    # calculates the bounding box difference between the point and the node
    def get_bounding_box_difference(self, point):
        return abs(self.min_x - point.x) + abs(self.max_x - point.x) + abs(self.min_y - point.y) + abs(
            self.max_y - point.y) + abs(self.min_t - point.t) + abs(self.max_t - point.t)

    # Expand the bounds of the node to include the point
    def _expand_bounds(self, point):
        self.min_x = min(self.min_x, point.x)
        self.min_y = min(self.min_y, point.y)
        self.min_t = min(self.min_t, point.t)
        self.max_x = max(self.max_x, point.x)
        self.max_y = max(self.max_y, point.y)
        self.max_t = max(self.max_t, point.t)

    # check if a 3D spatial-temporal range intersects with another 3D range
    def _intersects(self, min_x, min_y, min_t, max_x, max_y, max_t):
        return self.min_x <= max_x and self.min_y <= max_y and self.min_t <= max_t and self.max_x >= min_x and self.max_y >= min_y and self.max_t >= min_t


class RTree:
    def __init__(self, max_children=4):
        self.root = None
        self.max_children = max_children

    #  takes a Point object and inserts it into the R-tree
    def insert(self, point):
        if self.root is None:
            self.root = Node(point.x, point.y, point.t, point.x, point.y, point.t, data=[point])
        else:
            self.root.insert(point)

    # calls the search method of the root node
    def search(self, min_x, min_y, min_t, max_x, max_y, max_t):
        if self.root is None:
            return []
        else:
            return self.root.search(min_x, min_y, min_t, max_x, max_y, max_t)


def main():
    rtree = RTree()

    # # Define the points
    p1 = Point(1, 2, 3)
    p2 = Point(4, 5, 6)
    p3 = Point(7, 8, 9)
    p4 = Point(10, 11, 12)
    p5 = Point(13, 14, 15)

    # Insert the points into the rtree
    rtree.insert(p1)
    rtree.insert(p2)
    rtree.insert(p3)
    rtree.insert(p4)
    rtree.insert(p5)

    # Query the tree for points within a spatial-temporal range

    results1 = rtree.search(0, 1, 2, 10, 10, 10)
    # Print the results
    print("Output1:")
    for result in results1:
        print(result)

    results2 = rtree.search(3, 3, 3, 11, 11, 12)
    # Print the results
    print("\nOutput2:")
    for result in results2:
        print(result)

    results3 = rtree.search(2, 3, 4, 6, 7, 8)
    # Print the results
    print("\nOutput3")
    for result in results3:
        print(result)


if __name__ == "__main__":
    main()
