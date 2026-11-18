from cloud_ci_fixture import render_greeting


def test_greeting_preserves_a_normalized_name():
    assert render_greeting("  Alice  ") == "Hello, Alice!"
