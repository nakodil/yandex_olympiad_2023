def main(text: str):
    vowels = "ауоиэыяюеё"
    text = text.replace(" ", "")
    nums = [1 if s in vowels else -1 for s in text]
    next = shift_next(nums.copy())
    prev = shift_prev(nums.copy())
    print(min([prev, next]))


def is_alterate(word: list) -> bool:
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            return False
    return True


def shift_prev(nums: list) -> None:
    changes = 0
    for i in range(1, len(nums)):
        if is_alterate(nums):
            return changes
        if nums[i] == nums[i - 1]:
            nums[i] *= -1
            changes += 1
    return changes


def shift_next(nums: list) -> int:
    changes = 0
    for i in range(len(nums)):
        if is_alterate(nums):
            return changes
        if nums[i] == nums[i - 1]:
            changes += 1
            nums[i - 1] *= -1
    return changes


main("тру ля ля")  # 1
main("это она")	 # 3
main("мама мыла раму")	# 0
