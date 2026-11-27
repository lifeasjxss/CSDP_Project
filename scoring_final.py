# Multiply each answer by the choice's score for the same question, then calculate the sum.
def calculate_total(user_answers, choice_scores):
    total = 0
    for i in range(len(user_answers)):
        total = total + user_answers[i] * choice_scores[i]
    return total


# Convert a total into a percentage of the highest possible total.
def calculate_percentage(total, number_of_questions):
    highest_possible = 25 * number_of_questions
    percentage = round(total / highest_possible * 100)
    return percentage


# Give every choice a total score. Returns a dictionary like {"Nursing": 43}.
def score_all_choices(user_answers, scores):
    totals = {}
    for name in scores:
        if len(scores[name]) != len(user_answers):
            print("Warning: " + name + " does not have one score per question. Skipping it.")
        else:
            totals[name] = calculate_total(user_answers, scores[name])
    return totals


# Find the choice with the highest total that was not shown yet. Returns "" if none are left.
def find_best_choice(totals, already_shown):
    best_name = ""
    best_total = -1
    for name in totals:
        if name not in already_shown and totals[name] > best_total:
            best_name = name
            best_total = totals[name]
    return best_name


# Find the other choices that have the same total as this choice. Returns a list of names.
def find_tied_names(name, totals):
    tied_names = []
    for other_name in totals:
        if other_name != name and totals[other_name] == totals[name]:
            tied_names.append(other_name)
    return tied_names


# Score every choice and print the top 3 matches, plus any choice tied with the 3rd place total.
def show_results(user_answers, scores, choice_details):
    totals = score_all_choices(user_answers, scores)
    if len(totals) == 0:
        print("No results to show.")
        return

    number_of_questions = len(user_answers)
    already_shown = []
    best_total = totals[find_best_choice(totals, already_shown)]
    position = 0
    rank = 0
    last_total = -1

    print("")
    print("Your top matches:")
    print("")

    keep_going = True
    while keep_going:
        name = find_best_choice(totals, already_shown)

        if name == "":
            keep_going = False
        elif position >= 3 and totals[name] != last_total:
            keep_going = False
        else:
            position = position + 1
            if totals[name] != last_total:
                rank = position

            percentage = calculate_percentage(totals[name], number_of_questions)
            line = str(rank) + ". " + name + ": " + str(totals[name]) + " (" + str(percentage) + "%)"

            if totals[name] == best_total:
                line = line + ", the top match"

            tied_names = find_tied_names(name, totals)
            if len(tied_names) > 0:
                tied_text = ""
                for tied_name in tied_names:
                    if tied_text == "":
                        tied_text = tied_name
                    else:
                        tied_text = tied_text + ", " + tied_name
                line = line + " - tied with " + tied_text

            description = "No description found."
            if name in choice_details:
                description = choice_details[name]

            print(line)
            print("   " + description)
            print("")

            already_shown.append(name)
            last_total = totals[name]


if __name__ == "__main__":
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

    show_results(test_answers, test_scores, test_details)
