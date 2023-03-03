# Задача с олимпиады яндекса по информатике, март 2023


def count_changes(text: str) -> int:
    text = text.replace(" ", "")
    vowels = "ауоиэыяюеё"
    nums = [1 if s in vowels else -1 for s in text]
    changes = 0
    for i in range(len(nums)):
        if nums[i] == nums[i - 1]:
            changes += 1
            nums[i - 1] *= -1
    return changes


print(count_changes("тру ля ля"))  # 1
print(count_changes("это она"))	 # 3
print(count_changes("мама мыла раму"))  # 0
