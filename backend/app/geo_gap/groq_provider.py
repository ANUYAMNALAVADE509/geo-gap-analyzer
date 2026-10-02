import os

from groq import Groq


DEFAULT_MODEL = "openai/gpt-oss-20b"


def get_client() -> Groq:
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY environment variable is not configured."
        )

    return Groq(api_key=api_key)


def generate_response(
    prompt: str,
    model: str = DEFAULT_MODEL,
) -> str:
    client = get_client()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        temperature=0,
    )

    return response.choices[0].message.content or ""


if __name__ == "__main__":
    test_prompt = (
        "Name three types of beauty and personal care products. "
        "Return only a short list."
    )

    print("Testing Groq connection...")
    print(f"Model: {DEFAULT_MODEL}")
    print()

    answer = generate_response(test_prompt)

    print("Response:")
    print(answer)