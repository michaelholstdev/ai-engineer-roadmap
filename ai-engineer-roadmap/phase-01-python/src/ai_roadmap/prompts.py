import json
import textwrap


def build_ai_analysis_prompt(text: str) -> str:
    schema = {
        "type": "object",
        "properties": {
            "summary": {"type": "string"},
            "sentiment": {
                "type": "string",
                "enum": ["positive", "neutral", "negative"],
            },
            "topics": {
                "type": "array",
                "items": {"type": "string"},
            },
            "action_items": {
                "type": "array",
                "items": {"type": "string"},
            },
        },
        "required": ["summary", "sentiment", "topics", "action_items"],
        "additionalProperties": False,
    }
    json_schema = json.dumps(schema, indent=2)
    prompt = f"""Analyze the following text.
        Return only valid JSON.
        Do not use markdown.
        Do not include explanations.
        Do not wrap the JSON in code fences.

        Schema:
        ---
        {json_schema}
        ---

        Do not include additional fields.

        Text:
        ---
        {text}
        ---
        """
    return textwrap.dedent(prompt)
