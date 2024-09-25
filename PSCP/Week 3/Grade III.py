"""Grade III"""
def sum_score(time):
    """Sum score"""
    sum_grade = 0
    for _ in range(time):
        score = float(input())
        if 95 <= score <= 100:
            sum_grade +=  4
        elif 90 <= score < 95:
            sum_grade +=  3.5
        elif 85 <= score < 90:
            sum_grade +=  3
        elif 80 <= score < 85:
            sum_grade +=  2.5
        elif 75 <= score < 80:
            sum_grade +=  2
        elif 70 <= score < 75:
            sum_grade +=  1.5
        elif 65 <= score < 70:
            sum_grade +=  1
        elif 60 <= score < 65:
            sum_grade +=  0.5
        else:
            sum_grade +=  0
    return sum_grade
def main():
    """Grade III"""
    time = int(input())
    scores = sum_score(time)
    score = scores/time
    score = (int(score*100))/100
    print(f"{score:.2f}")

main()
