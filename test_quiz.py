from utils.quiz_generator import (
    generate_quiz
)

sample_text = """
TCP provides reliable communication.
UDP is connectionless.
"""

print(
    generate_quiz(
        sample_text
    )
)