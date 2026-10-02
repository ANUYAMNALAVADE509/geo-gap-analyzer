from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class GeoGapQuery:
    query_id: str
    intent: str
    template: str


QUERY_TEMPLATES: List[GeoGapQuery] = [
    GeoGapQuery(
        query_id="discovery_01",
        intent="category_discovery",
        template=(
            "What are some well-regarded {category} "
            "that customers commonly recommend?"
        ),
    ),
    GeoGapQuery(
        query_id="recommendation_01",
        intent="product_recommendation",
        template=(
            "What {category} would you recommend to a customer "
            "looking for reliable and well-reviewed options?"
        ),
    ),
    GeoGapQuery(
        query_id="recommendation_02",
        intent="product_recommendation",
        template=(
            "Which {category} have strong customer feedback "
            "and are worth considering?"
        ),
    ),
    GeoGapQuery(
        query_id="problem_01",
        intent="problem_based",
        template=(
            "I am looking for {category} with good customer "
            "satisfaction. What products should I consider?"
        ),
    ),
    GeoGapQuery(
        query_id="comparison_01",
        intent="comparison",
        template=(
            "Which {category} are commonly recommended when "
            "comparing highly rated options?"
        ),
    ),
    GeoGapQuery(
        query_id="brand_01",
        intent="brand_discovery",
        template=(
            "Which brands are commonly recommended for {category}?"
        ),
    ),
]


def build_queries(category: str) -> List[dict]:
    """
    Instantiate the fixed query templates for a category.
    """

    category = category.strip()

    if not category:
        raise ValueError("category cannot be empty")

    return [
        {
            "query_id": query.query_id,
            "intent": query.intent,
            "category": category,
            "prompt": query.template.format(category=category),
        }
        for query in QUERY_TEMPLATES
    ]


if __name__ == "__main__":
    for category in [
        "beauty products",
        "beauty and personal care products",
    ]:
        print("=" * 70)
        print(f"CATEGORY: {category}")
        print("=" * 70)

        for query in build_queries(category):
            print(f"[{query['query_id']}] {query['intent']}")
            print(query["prompt"])
            print()