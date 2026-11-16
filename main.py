import json
from datetime import datetime, timezone

import openai

client = openai.OpenAI()


def report() -> str:
    return json.dumps({"generated_at": datetime.now(timezone.utc).isoformat()})


def summarize(text: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": f"Summarize: {text}"}],
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    print(summarize(report()))
