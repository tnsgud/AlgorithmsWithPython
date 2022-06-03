
def solution(board, moves):
    answer = 0

    bucket = []

    index = 0
    for move in moves:
        for row in board:
            if row[move - 1] != 0:
                bucket.append(row[move - 1])

                if index - 1 >= 0 and bucket[index - 1] != 0 and bucket[index - 1] == bucket[index]:
                    bucket = bucket[:index - 1]
                    index -= 1
                    answer += 2
                else:
                    index += 1

                row[move - 1] = 0
                break

    return answer
