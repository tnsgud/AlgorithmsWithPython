
def solution(numbers: list, hand: str):
    answer = ''

    points = {1: (0, 0), 2: (0, 1), 3: (0, 2),
              4: (1, 0), 5: (1, 1), 6: (1, 2),
              7: (2, 0), 8: (2, 1), 9: (2, 2),
              '*': (3, 0), 0: (3, 1), '#': (3, 2)}

    left = '*'
    right = '#'

    for number in numbers:
        if number in [1, 4, 7]:
            left = number
            answer += 'L'
        elif number in [3, 6, 9]:
            right = number
            answer += 'R'
        else:
            cur_point = points[number]
            left_point = points[left]
            right_point = points[right]
            left_dist = abs(cur_point[0] - left_point[0]) + abs(cur_point[1] - left_point[1])
            right_dist = abs(cur_point[0] - right_point[0]) + abs(cur_point[1] - right_point[1])

            if left_dist == right_dist:
                answer += hand[0].upper()
                left = number if hand[0] == 'l' else left
                right = number if hand[0] == 'r' else right
            elif left_dist < right_dist:
                answer += 'L'
                left = number
            else:
                answer += 'R'
                right = number

    return answer


print(solution(list(map(int, input().split(','))), input()))
