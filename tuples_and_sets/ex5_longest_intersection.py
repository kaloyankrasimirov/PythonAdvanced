def create_set(range_str):
    start, end = range_str.split(",")
    return set(range(int(start), int(end) +1))

longest_intersection = set()

for _ in range(int(input())):
    first_range, second_range = input().split("-")
    first_set = create_set(first_range)
    second_set = create_set(second_range)

    curr_intersection = first_set & second_set

    if len(curr_intersection) > len(longest_intersection):
        longest_intersection = curr_intersection

print(f"Longest intersection is {list(longest_intersection)} with length {len(longest_intersection)}")