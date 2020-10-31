n = input()
scores = list(map(int, input().split(' ')))
min_score = scores[0]
max_score = scores[0]
min_score_counter = 0
max_score_counter = 0

for score in scores:
    if score > max_score:
        max_score = score
        max_score_counter += 1
    elif score < min_score:
        min_score = score
        min_score_counter += 1

print('{} {}'.format(max_score_counter, min_score_counter))