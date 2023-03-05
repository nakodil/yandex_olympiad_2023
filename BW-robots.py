"""
Задача 3 [25 баллов]
В сервисе починки роботов очень важно соблюдать порядок. Главный механик любит, чтобы все роботы стояли друг за другом — сначала только сломанные (если они есть), а потом исправные (если они есть).
По ночам роботы всё время гуляют по ангару, и к утру порядок, установленный главным механиком, нарушается. Механик решил наказывать роботов, которые нарушают порядок, и удалять из очереди. Но роботы взбунтовались и требуют равноправия — если уж удалять из очереди, то равное количество исправных и сломанных роботов.
Сломанные роботы обозначаются буквой B (broken), исправные — буквой W (working).
Есть строка из букв B и W. Надо удалить наименьшее и равное количество сломанных и исправных роботов так, чтобы в очереди сначала стояли только сломанные, а потом только исправные. Может оказаться, что одних или других нет. Общее количество роботов в очереди не превышает 10 000.
Выведи количество удалённых роботов и очередь, которая получилась после удаления нарушивших правило роботов.
Если в очереди никого не осталось, выведи "НИКОГО НЕ ОСТАЛОСЬ".

ввод 1:
BWBWWBW

вывод 1:
2
BBWWW

ввод 2:
BWWWWW

вывод 2:
0
BWWWWW

ввод 3:
BBBBB

вывод 3:
0
BBBBB

ввод 4:
WWBB

вывод 4:
0
НИКОГО НЕ ОСТАЛОСЬ
"""


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
    while robots != sorted(robots):
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
    for i in range(len(robots) - 1, 0, -1):
        if robots[i] == "B" and robots[i + 1] == "W":
            return i


main("BWBWWBW")  # 2 BBWWW
main("BWWWWW")  # 0 BWWWWW
main("BBBBB")  # 0 BBBBB
main("WWBB")  # 4 НИКОГО НЕ ОСТАЛОСЬ
