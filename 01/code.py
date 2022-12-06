from functools import reduce

with open('input.txt') as f:
    lines = f.readlines()

    def all_calories(arr, line):
        if line == '\n':
            arr.append(0)
        else:
            arr[-1] += int(line)

        return arr

    elfs_calories = reduce(all_calories, lines, [0])
    higher_calories = max(elfs_calories)

    print(higher_calories)

    elfs_calories.sort()
    top_three_higher_calories_sum = sum(elfs_calories[-3:len(elfs_calories)])
    
    print(top_three_higher_calories_sum)
