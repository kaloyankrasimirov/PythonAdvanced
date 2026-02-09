def accommodate(*guest_groups, **available_rooms) :
    accommodation = {}
    unaccommodated_guests = 0

    rooms = sorted(available_rooms.items(), key=lambda r: (r[1], r[0]))

    for guests in guest_groups:
        is_accommodated = False

        for room_key , capacity in rooms:
            if capacity >= guests:
                room_number = room_key.split('_')[1]
                accommodation[room_number] = guests
                rooms.remove((room_key, capacity))
                is_accommodated = True
                break

        if not is_accommodated:
            unaccommodated_guests += guests

    if accommodation:
        result = [f"A total of {len(accommodation)} accommodations were completed!"]
        for room_number in sorted(accommodation.keys()):
            result.append(f"<Room {room_number} accommodates {accommodation[room_number]} guests>")
    else:
        result = ["No accommodations were completed!"]

    if unaccommodated_guests > 0:
        result.append(f"Guests with no accommodation: {unaccommodated_guests}")

    if rooms:
        result.append(f"Empty rooms: {len(rooms)}")

    return "\n".join(result).strip()


#Test input:
# print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print(accommodate(10, 9, 8, room_307=6, room_802=5))
# print(accommodate(1, 2, 4, 8, room_102=3, room_101=1, room_103=2))