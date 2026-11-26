test_answers = [5, 1, 4]

test_scores = {
    "Nursing": [5, 2, 4],
    "Computer Science": [2, 1, 5],
    "Environmental Science": [3, 5, 3]
}

test_details = {
    "Nursing": "Nurses care for patients in hospitals and clinics.",
    "Computer Science": "Computer scientists design and build software.",
    "Environmental Science": "Environmental scientists study the natural world."
}

totals = {}   # creating an empty totals dictionary
for major in test_scores:    #looping through every major
    total = 0

    for i in range(len(test_answers)):
        total = total + (test_answers[i] * test_scores[major][i])

        totals[major] = total

highest_possible = 25 * len(test_answers)

sorted_scores = 25 * len(test_answers)

print("Top Machine")
print("")

first_major = ""
first_score = -1

for major in totals:
    if totals[major] > first_score:
        first_score = totals[major]
        first_major = major

first_percent = int((first_score / highest_possible) * 100)

print("1. ")
print(first_major + ": " + str(first_score) + " (" + str(first_percent) + "%)")
print("TOP MATCH")
print(test_details[first_major])
print()

second_major = ""
second_score = -1

for major in totals:
    if major != first_major and totals[major] > second_score:
        second_score = totals[major]
        second_major = major

second_percent = int((second_score / highest_possible) * 100)

print("2.")
print(second_major + ": " + str(second_score) + " (" + str(second_percent) + "%)")
print(test_details[second_major])
print()

third_major = ""
third_score = -1

for major in totals:
     if major != first_major and major != second_major:
        if totals[major] > third_score:
            third_score = totals[major]
            third_major = major

third_percent = int((third_score / highest_possible) * 100)

print("3.")
print(third_major + ": " + str(third_score) + " (" + str(third_percent) + "%)")
print(test_details[third_major])