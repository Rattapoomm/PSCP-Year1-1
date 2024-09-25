"""_"""
def calculate_scores(total_scores, highest_scores):
    """_"""
    lowest_scores = total_scores - (highest_scores * 2)
    if lowest_scores < 0:
        lowest_scores = 0
    if highest_scores - lowest_scores > 2:
        print("Surprising")
    else:
        print("Not surprising")
calculate_scores(float(input()), float(input()))
