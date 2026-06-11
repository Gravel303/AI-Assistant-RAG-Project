
from utils.flashcard_generator import (
    generate_flashcards
)

sample_text = """
TCP provides reliable communication.
UDP is connectionless.
"""

print(
    generate_flashcards(
        sample_text
    )
)