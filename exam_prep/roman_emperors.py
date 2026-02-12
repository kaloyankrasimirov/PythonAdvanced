def list_roman_emperors(*args, **kwargs):
    successful = []
    unsuccessful = []

    for name, status in args:
        years = kwargs[name]

        if status:
            successful.append((name, years))
        else:
            unsuccessful.append((name, years))

    successful.sort(key=lambda x: (-x[1], x[0]))
    unsuccessful.sort(key=lambda x: (x[1], x[0]))

    result = [f"Total number of emperors: {len(args)}"]

    if successful:
        result.append("Successful emperors:")
        for name, years in successful:
            result.append(f"****{name}: {years}")

    if unsuccessful:
        result.append("Unsuccessful emperors:")
        for name, years in unsuccessful:
            result.append(f"****{name}: {years}")

    return "\n".join(result)


#test cases:
print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14,))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False),
                          ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14,
                          Caligula=4, Pertinax=4, Vespasian=19,))
print(list_roman_emperors(("Augustus", True), ("Trajan", True),
                          ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))