from utils.query_rewriter import rewrite_query

history = """
user: What is TCP?
assistant: TCP is...
"""

rewritten = rewrite_query(
    "How does it ensure reliability?",
    history
)

print(rewritten)