n = int(input())
series = list(map(int, input().split()))
count = 0
give_away_left = 0
for i in range(1, n):
    start = series[i - 1]
    end = series[i]
    difference = start - end
    give_away_left += abs(difference)
    if abs(difference) <= 1:
        continue
    if difference < 0:
        for j in range(i, -1, -1):
            count_2 = 0
            start_2 = series[j]
            end_2 = series[j - 1]
            if abs(end_2 - start_2) <= 1:
                continue
            if start_2 - end_2 - 2 == 0:
                count_2 = start_2 - end_2 - 1
            else:
                count_2 = start_2 - end_2 - 2
            series[j - 1] += count_2
            series[j] -= count_2
            count += count_2
    else:
        if start - end - 2 == 0:
            series[i] += start - end - 1
            series[i - 1] -= start - end - 1
            count += start - end - 1
        else:
            series[i] += start - end - 2
            series[i - 1] -= start - end - 2
            count += start - end - 2


print(count)
# for j in range(i - 2, -1, -1):
#     if abs(series[j] - end) <= 1:
#         count += (i - j)
#         series[j] += 1
#         if abs(series[j] - end) <= 1:
#             continue
