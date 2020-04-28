#!/bin/python

def is_valid_triangle(edges):
    assert len(edges) == 3, "input should have 3 edges"

    if edges[0] + edges[1] > edges[2] and edges[0] + edges[2] > edges[1] and edges[1] + edges[2] > edges[0]:
        return True
    else:
        return False

def main():
    response = is_valid_triangle([5, 10, 25])
    assert response == False, "it should be 0"

    response = is_valid_triangle([4, 5, 7])
    assert response == True, "it should be 1"

    # part 1
    num_triangles = 0

    with open("input.txt", "r") as f:
        while True:
            line = f.readline()

            if line == "\n" or line == "":
                break

            edges = list(map(lambda x: int(x), line.strip().split()))
            num_triangles = num_triangles + (1 if is_valid_triangle(edges) else 0)

    print("Part1: Total number of triangles is: {}".format(num_triangles))


    # part 2
    num_triangles = 0
    processed_edges = []

    with open("input.txt", "r") as f:
        while True:
            line = f.readline()

            processed_edges.append(list(map(lambda x: int(x), line.strip().split())))

            if line == "\n" or line == "":
                break

            if (len(processed_edges) % 3 == 0):

                edges_first = [processed_edges[0][0], processed_edges[1][0], processed_edges[2][0]]
                edges_second = [processed_edges[0][1], processed_edges[1][1], processed_edges[2][1]]
                edges_third = [processed_edges[0][2], processed_edges[1][2], processed_edges[2][2]]
                
                num_triangles = num_triangles + (1 if is_valid_triangle(edges_first) else 0)
                num_triangles = num_triangles + (1 if is_valid_triangle(edges_second) else 0)
                num_triangles = num_triangles + (1 if is_valid_triangle(edges_third) else 0)

                processed_edges = []

    print("Part2: Total number of triangles is: {}".format(num_triangles))

if __name__ == "__main__":
    main()