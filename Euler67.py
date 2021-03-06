# -*- coding: utf-8 -*-
"""
Maximum path sum II
Problem 67
By starting at the top of the triangle below and moving to adjacent numbers on 
the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 
'Save Link/Target As...'), a 15K text file containing a triangle with 
one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to
try every route to solve this problem, as there are 299 altogether! If you could
check one trillion (10^12) routes every second it would take over twenty billion 
years to check them all. There is an efficient algorithm to solve it. ;o)

Answer: 7273
Ricky Kwok, rickyk9487@gmail.com, 2014-10-25
"""

def get_max_path(tri_array, depth):
    """ Returns the maximum path for each node by computing the maximum
        path of each of the two children starting from bottom up. """
    max_path = [0]*len(tri_array)
    max_path[depth*(depth-1)/2:depth*(depth+1)/2] = tri_array[depth*(depth-1)/2:depth*(depth+1)/2]
    for r in range(depth-1, 0, -1):
        for c in range(r):
            # Iterates from the bottom-most row, left to rigth
            max_child = max(max_path[r*(r+1)/2+c],max_path[r*(r+1)/2+c+1])
            max_path[r*(r-1)/2+c] = tri_array[r*(r-1)/2+c] + max_child
    return max(max_path)

def triangle_to_array(triangle):
    """ Converts the string provided into an array of ints."""
    nodes = list(triangle.split("\n"))
    depth, row, tri_array  = 100, 0, []
    for node in nodes:
        integer, col  = node.split(" "), 0
        row += 1
        for elt in integer:
            elt = int(elt)
            tri_array.append(elt)
            col += 1
    return get_max_path(tri_array, depth)

def main():
    """ Opens file containing heap and stores the triangle as text."""
    f = open("p067_triangle.txt")
    triangle = f.read()
    f.close()
    print triangle_to_array(triangle)
        
if __name__ == "__main__":
    main()