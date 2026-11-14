"""Analyze clothing images with a locally running Ollama model."""

from pathlib import Path

from ollama import ResponseError, chat

from clothing_attributes import ClothingAttributes

MODEL_NAME = "qwen2.5vl:7b"
NUM_PREDICT = 1024
print(f"\n num_predict: {NUM_PREDICT} \n ")
IMAGE_PATH = Path(
    r"C:\Users\Eho\Desktop\Images & Videos\A47500020-front-pdp-ld-79808908.jpg"
)


def analyze_clothing_image(image_path: Path) -> ClothingAttributes:
    """Analyze one local clothing image with the locally running Qwen model."""
    if not image_path.is_file():
        raise FileNotFoundError(f"Image file was not found: {image_path}")

    prompt = """
Analyze the single clothing item in this image and return only structured JSON.

Rules:
- Describe the garment, not the person wearing it.
- Use concise lowercase values.
- Use "unknown" when an attribute cannot be determined reliably.
- Evaluate each season independently and include every season in which the item
  is reasonably suitable, not only the best season.
- For ordinary medium-weight clothing, include spring or winter when the item
  could reasonably be layered or worn in cool weather; do not omit a plausible
  season just because another season is a better match.
- Select seasons only from: spring, summer, autumn, winter.
- List weather conditions conservatively.
"""

    try:
        response = chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                    "images": [str(image_path)],
                }
            ],
            format=ClothingAttributes.model_json_schema(),
            think=False,
            options={"temperature": 0, "num_predict": NUM_PREDICT},
        )
    except ResponseError as error:
        raise RuntimeError(
            f"Ollama could not analyze the image with {MODEL_NAME!r}. "
            f"HTTP {error.status_code}: {error.error}"
        ) from error

    if not response.message.content:
        raise RuntimeError(
            "The model returned no final JSON content. "
            f"done_reason={response.done_reason!r}; "
            f"thinking_length={len(response.message.thinking or '')}."
        )

    try:
        clothing_attributes = ClothingAttributes.model_validate_json(
            response.message.content
        )
    except ValueError as error:
        raise RuntimeError(
            "The model returned invalid or truncated JSON. "
            f"done_reason={response.done_reason!r}; "
            f"response_length={len(response.message.content)}."
        ) from error

    prompt_tokens = response.prompt_eval_count
    generated_tokens = response.eval_count
    print(
        "Token usage: "
        f"prompt={prompt_tokens}, "
        f"generated={generated_tokens}, "
        f"total={prompt_tokens + generated_tokens}"
    )

    return clothing_attributes


if __name__ == "__main__":
    attributes = analyze_clothing_image(IMAGE_PATH)
    print(attributes.model_dump_json(indent=2))
