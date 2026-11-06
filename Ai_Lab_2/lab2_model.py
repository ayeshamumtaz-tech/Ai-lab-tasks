
def control_mode(temperature, occupied, previous_mode):
    if not occupied:
        target = "ECO"
    elif temperature > 26:
        target = "COOL"
    elif temperature < 20:
        target = "WARM"
    else:
        target = "IDLE"
    if target == previous_mode:
        command = "NO COMMAND"
    else:
        command = "SEND COMMAND"
    return target, command

previous_mode = None
tests = [
    ("Repeated percept", 29, True),
    ("Repeated percept", 29, True),
    ("Lower boundary", 20, True),
    ("Upper boundary", 26, True),
    ("Mode transition", 19, True),
    ("Empty room", 29, False)
]
for name, temperature, occupied in tests:
    target, command = control_mode(temperature, occupied, previous_mode)
    print(name)
    print("Previous mode:", previous_mode)
    print("Percept:", "Temperature =", temperature, "Occupied =", occupied)
    print("Target mode:", target)
    print("Command:", command)
    print()
    previous_mode = target
