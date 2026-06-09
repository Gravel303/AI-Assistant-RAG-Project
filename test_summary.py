from utils.summary_generator import (
    generate_summary
)

sample_text = """
TCP provides reliable communication.
UDP is connectionless.
"""

print(
    generate_summary(
        sample_text
    )
)