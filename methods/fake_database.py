participant_set = {
    ("1", "A"),
    ("2", "B"),
    ("3", "C"),
    ("4", "D"),
    ("5", "E"),
    ("6", "F"),
    ("7", "G"),
    ("8", "H"),
    ("9", "I"),
    ("10", "J"),
    ("11", "K"),
    ("12", "L"),
    ("13", "M")
}
is_update = False


def change_state():
    global is_update
    is_update = False


def vis_state():
    global is_update
    return is_update


def update(phone, name):
    global is_update
    global participant_set
    for i in participant_set:
        if i[0] == phone:
            return -1
        elif i[1] == name:
            return 0
    is_update = False
    participant_set.add((phone, name))
    print(participant_set)
    return 1


def delete(phone):
    global participant_set
    for i in participant_set:
        if i[0] == phone:
            participant_set.remove(i)
            return 1
    print(participant_set)
    return 0
