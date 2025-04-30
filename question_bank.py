# ---------------------------------------
#  Question Bank
#    Sarim Naveed
# ---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("What is the chemical symbol for carbon monoxide", "CO"),
        ("Who came up with the Theory Of Relativity", "Einstein"),
        ("What force keeps planets in orbit around the Sun?", "Gravity"),
        ("What is the powerhouse of the cell?", "Mitochondria"),
        ("What is the process by which plants make their own food", "Photosynthesis"),
        ("What is the Earth's natural satellite?", "The Moon"),
        ("What is the largest planet in our solar system?", "Jupiter"),
        ("What is the process where a liquid turns into a gas?", "Evaporation"),
        ("What is the primary gas that makes up Earth's atmosphere?", "Nitrogen"),
        ("What is the process by which animals take in Oxygen and release Carbon Dioxide?", "Respiration")
    ],
}

hints = {
    "Science": [
        ("What is the chemical symbol for water?", "Imagine it's atomic structure and simplify it"),
        ("What is the chemical symbol for carbon monoxide", "It's Carbon Dioxide, but has one less Oxygen atom in it"),
        ("Who came up with the Theory Of Relativity", "Second name only"),
        ("What force keeps planets in orbit around the Sun?", "Newton gave it this name after a apple fell on his head"),
        ("What is the powerhouse of the cell?", "Google the spellings"),
        ("What is the process by which plants make their own food", "Google the spellings"),
        ("What is the Earth's natural satellite?", "There's a 'The' at the start"),
        ("What is the largest planet in our solar system?", "Skill issue"),
        ("What is the process where a liquid turns into a gas?", "Google the spellings"),
        ("What is the primary gas that makes up Earth's atmosphere?", "The full name not the chemical name"),
        ("What is the process by which animals take in Oxygen and release Carbon Dioxide?", "Google the spellings")
    ],
    # Repeat for other categories as needed.
}


# ---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    # ------------------------

    return random.choice(questions[category])

    # ------------------------


# ---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    # ------------------------
    if player_answer == correct_answer:
        return True

    return False

    # ------------------------


# ---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    # ------------------------
    question_list = questions[category]
    index = -1

    for qs in question_list:
        index += 1
        if question == qs[0]:
            del questions[category][index]

    # ------------------------


# ---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    # ------------------------
    print("Please input an answer right next to the question.")
    answer = input(f"{question}: ")
    return answer

    # ------------------------


# ---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    # ------------------------
    question_list = questions[category]
    index = -1

    for qs in question_list:
        index += 1
        if question == qs[0]:
            return hints[category][index][1]

    # ------------------------


# ---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    # ------------------------
    print(f"Here was the correct answer: {correct_answer}")

    # ------------------------

# ---------------------------------------
