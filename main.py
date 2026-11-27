import choice_leader
import score_leader
import quiz
import scoring

choices_details = choice_loader.load_choices("data/choices.txt")
questions, scores = score_loader.load_questions_and_scores("data/questions.txt")
answers = quiz.ask_all_questions(questions)
scoring.show_results(answers, scored, choice_details)
