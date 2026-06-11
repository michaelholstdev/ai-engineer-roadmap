from ai_roadmap.prompts import build_ai_analysis_prompt


def test_ai_analysis_prompt_includes_input_text():
    assert "some text" in build_ai_analysis_prompt("some text")


def test_ai_analysis_prompt_includes_required_fields():
    prompt = build_ai_analysis_prompt("some text")

    for field_name in ["summary", "sentiment", "topics", "action_items"]:
        assert field_name in prompt


def test_ai_analysis_prompt_includes_allowed_sentiments():
    prompt = build_ai_analysis_prompt("some text")

    for sentiment in ["positive", "neutral", "negative"]:
        assert sentiment in prompt


def test_ai_analysis_prompt_forbids_additional_fields():
    prompt = build_ai_analysis_prompt("Some text")

    assert "Do not include additional fields." in prompt
    assert '"additionalProperties": false' in prompt


def test_ai_analysis_prompt_rejects_markdown_and_explanations():
      prompt = build_ai_analysis_prompt("some text")

      assert "Return only valid JSON." in prompt
      assert "Do not use markdown." in prompt
      assert "Do not include explanations." in prompt
      assert "Do not wrap the JSON in code fences." in prompt
