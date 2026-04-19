processes = [1, 2, 3, 4, 5]   # process IDs
coordinator = max(processes)

print("Initial Coordinator:", coordinator)

def election(p):
    print("\nProcess", p, "starts election")

    higher = [x for x in processes if x > p]

    if not higher:
        print("Process", p, "becomes Coordinator")
        return p
    else:
        print("Process", p, "sends election to", higher)
        return election(max(higher))

# suppose coordinator (5) fails
processes.remove(4)

new_coordinator = election(2)

print("\nNew Coordinator:", new_coordinator)