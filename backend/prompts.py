def summary_prompt(text: str, style: str) -> str:
    return f"""You are a helpful assistant that summarizes text.

Write a {style} summary of the text below.
Use simple English. Do not add information that is not in the text.

TEXT:
{text}
"""