from cloud_ci_fixture import render_greeting


def test_greeting_strips_surrounding_whitespace():
    assert render_greeting("  Morgan\t ") == "Hello, Morgan!"
