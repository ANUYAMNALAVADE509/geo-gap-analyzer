from app.geo_gap.query_templates import build_queries
from app.geo_gap.groq_provider import generate_response, DEFAULT_MODEL
from app.geo_gap.response_schema import LLMResponse
from app.geo_gap.response_store import save_responses


def run_category(category: str):
    queries = build_queries(category)

    responses = []

    for query in queries:
        print("=" * 80)
        print(f"Query ID: {query['query_id']}")
        print(f"Intent: {query['intent']}")
        print(f"Prompt: {query['prompt']}")
        print()

        response_text = generate_response(
            query["prompt"],
            model=DEFAULT_MODEL,
        )

        print("LLM Response:")
        print(response_text)
        print()

        response = LLMResponse(
            provider="groq",
            model=DEFAULT_MODEL,
            category=category,
            query_id=query["query_id"],
            intent=query["intent"],
            prompt=query["prompt"],
            response_text=response_text,
            product_mentions=[],
        )

        responses.append(response)

    return responses


if __name__ == "__main__":
    category = "beauty products"

    print(f"Running Geo-Gap queries for: {category}")
    print(f"Model: {DEFAULT_MODEL}")
    print()

    results = run_category(category)

    output_path = save_responses(
        results,
        "beauty_products_groq.jsonl",
    )

    print("=" * 80)
    print(f"Completed {len(results)} queries.")
    print(f"Saved responses to: {output_path}")