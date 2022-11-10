def better_than_average(class_points, your_points):
    count = 0
    for element in class_points:
        count += 1
    peer_points = (sum(class_points)) / count
    if peer_points < your_points:
        return True
    return False

print(better_than_average([7, 8, 9, 10], 90))