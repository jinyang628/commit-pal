GIT_COMMIT_MESSAGE_SYSTEM_PROMPT = (
    """You are a helpful assistant that generates clear and concise git commit messages."""
)

GIT_COMMIT_MESSAGE_USER_PROMPT = """
Given the following git diff, generate a commit message that follows these rules:
{style_config}

Here's the diff to analyze:
{diff}

You should only output the commit message, nothing else.
"""
