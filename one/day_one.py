def calculate_distance(l1: list, l2: list):
    l1.sort()
    l2.sort()
    distance = 0
    for id1, id2 in zip(l1, l2):
        distance += abs(id1 - id2)

    return distance


def calculate_similarity_score(l1: list, l2: list):
    l1_dict = {v: 0 for v in l1}
    for id in l2:
        if id in l1_dict:
            l1_dict[id] += 1
    similarity_score = 0
    for id in l1:
        similarity_score += id * l1_dict[id]
    return similarity_score


def main():
    locations1, locations2 = [], []
    with open("one/input.txt") as input:
        for line in input.readlines():
            location_one, location_two = line.split()
            locations1.append(int(location_one))
            locations2.append(int(location_two))
    print(f"distance is {calculate_distance(locations1, locations2)}")
    print(f"similarity score is {calculate_similarity_score(locations1, locations2)}")


if __name__ == "__main__":
    main()
