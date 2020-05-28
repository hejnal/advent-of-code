import re
def extract_ints(a_string):
    return tuple(map(int, re.findall(r'-?\d+', a_string)))

with open('input.txt') as f:
    inputs = [extract_ints(line) for line in f]
for i in range(15000):
    points = [(p[0] + i * p[2], p[1] + i * p[3]) for p in inputs]
    min_pos, max_pos = zip(*((min(coord), max(coord)) for coord in tuple(zip(*points))))
    size = (max_pos[0] - min_pos[0] + 1, max_pos[1] - min_pos[1] + 1)
    if size[1] <= 10:
        print(i)
        local_points = [tuple(map(sub, point, min_pos)) for point in points]
        text = [['.' for x in range(size[0])] for y in range(size[1])]
        for p in local_points:
            text[p[1]][p[0]] = '#'
        for line in text:
            print(''.join(line))