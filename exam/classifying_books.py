def classify_books(*args, **kwargs):
    fiction = []
    non_fiction = []
    title_to_genre = {}

    for genre, title in args:
        title_to_genre[title] = genre

    for isbn, title in kwargs.items():
        genre = title_to_genre[title]
        if genre == "fiction":
            fiction.append((isbn, title))
        else:
            non_fiction.append((isbn, title))

    non_fiction.sort(key=lambda x: x[0], reverse=True)
    fiction.sort()

    result = []

    if fiction:
        result.append("Fiction Books:")
        for isbn, title in fiction:
            result.append(f"~~~{isbn}#{title}")

    if non_fiction:
        result.append("Non-Fiction Books:")
        for isbn, title in non_fiction:
            result.append(f"***{isbn}#{title}")

    return "\n".join(result)


#Test cases:
# print(classify_books(
#     ("fiction", "Brave New World"),
#     ("non_fiction", "The Art of War"),
#     NF3421NN="The Art of War",
#     FF1234UU="Brave New World"
# ))
# print(classify_books(
#     ("non_fiction", "The Art of War"),
#     ("fiction", "The Great Gatsby"),
#     ("non_fiction", "A Brief History of Time"),
#     ("fiction", "Brave New World"),
#     FF1234HH="The Great Gatsby",
#     NF3845UU="A Brief History of Time",
#     NF3421NN="The Art of War",
#     FF1234UU="Brave New World"
# ))
# print(classify_books(
#     ("fiction", "Brave New World"),
#     ("fiction", "The Catcher in the Rye"),
#     ("fiction", "1984"),
#     FICCITRZZ="The Catcher in the Rye",
#     FIC1984XX="1984",
#     FICBNWYYY="Brave New World"
# ))
# print(classify_books(
#     ("non_fiction", "Sapiens"),
#     ("non_fiction", "Homo Deus"),
#     ("non_fiction", "The Selfish Gene"),
#     NF123ABC="Sapiens",
#     NF987XYZ="Homo Deus",
#     NF456DEF="The Selfish Gene"
# ))
