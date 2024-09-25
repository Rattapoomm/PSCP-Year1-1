'''alm'''
def almost_mean():
    '''ccc'''
    student_ids = []
    scores = []

    num_students = int(input())
    for _ in range(num_students):
        temp = input().split()
        student_ids.append(temp[0])
        scores.append(float(temp[1]))

    score_sum = sum(scores)
    mean = score_sum / num_students
    sorted_scores = sorted(scores)

    index_score = 0
    while True:
        if sorted_scores[index_score] >= mean:
            index_score -= 1
            break
        index_score += 1

    for i, score in enumerate(scores):
        if score == sorted_scores[index_score]:
            print("\t".join([student_ids[i], str(score)]))

almost_mean()
