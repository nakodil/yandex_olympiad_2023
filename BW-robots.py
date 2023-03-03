def main(robots: str):
    counter, robots = remove_robots(robots)
    print(counter)
    print(robots)


def remove_robots(robots: str) -> str:
    if robots.count("B") == robots.count("W"):
        return (len(robots), "НИКОГО НЕ ОСТАЛОСЬ")
    if robots.count("B") < 2 or robots.count("W") < 2:
        return (0, robots)
   
    robots = list(robots)
    counter = 0
    while not is_ordered(robots):
        b_idx = find_B(robots)
        w_idx = find_W(robots)
        if w_idx and b_idx:
            robots.pop(b_idx)
            robots.pop(w_idx)
            counter += 2
        
    return (counter, "".join(robots))
    


def find_W(robots: list) -> None:
    for i in range(len(robots) - 1):
        if robots[i] == "W" and robots[i + 1] == "B":
            return i


def find_B(robots: list) -> None:
    idx = None
    for i in range(len(robots) - 1):
        if robots[i] == "B" and robots[i + 1] == "W":
            idx = i
    return idx


def is_ordered(robots: str):
    shifts = 0
    for i in range(len(robots) - 1):
        if robots[i] != robots[i + 1]:
            shifts += 1
    return shifts == 1


main("BWBWWBW")  # 2 BBWWW
main("BWWWWW")  # 0 BWWWWW
main("BBBBB")  # 0 BBBBB
main("WWBB")  # 4 НИКОГО НЕ ОСТАЛОСЬ
