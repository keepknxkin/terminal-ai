import os
import sys
from openai import OpenAI

client = OpenAI()

query = " ".join(sys.argv[1:])

response = client.responses.create(
    model="gpt-4.1-mini",
    input=f"""
Convert the user's request into ONE shell command.

Rules:
- Return ONLY the command
- No explanation
- No markdown
- Assume Windows PowerShell or CMD

Request:
{query}
"""
)

print(response.output_text.strip())
