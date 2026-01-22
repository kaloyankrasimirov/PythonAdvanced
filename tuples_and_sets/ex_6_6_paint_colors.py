from collections import deque

colors_string = deque(input().split())
main_colors = ["red", "yellow", "blue"]
secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

collected_colors = []

while colors_string:
    first_substring = colors_string.popleft()
    last_string = colors_string.pop() if colors_string else ""

    for color in (first_substring + last_string, last_string + first_substring):
        if color in main_colors or color in secondary_colors:
            collected_colors.append(color)
            break
    else:
        if len(first_substring) > 1:
            colors_string.insert(len(colors_string) // 2, first_substring[:-1])
        if len(last_string) > 1:
            colors_string.insert(len(colors_string) // 2, last_string[:-1])

for color in collected_colors:
    if color in secondary_colors:
        for el in secondary_colors[color]:
            if el not in collected_colors:
                collected_colors.remove(color)
                break

print(collected_colors)