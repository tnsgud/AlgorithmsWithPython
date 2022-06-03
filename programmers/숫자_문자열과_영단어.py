
def solution(s: str):
    answer = 0

    dictionary = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }

    for key in dictionary.keys():
        for i in range(s.count(key)):
            index = s.find(key)
            s = s[:index] + str(dictionary[key]) + s[index+len(key):]

    answer = s

    return answer


print(solution(input()))
