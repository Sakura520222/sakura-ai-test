from cloud_ci_fixture import render_greeting


def test_greeting_trims_surrounding_whitespace():
    assert render_greeting("  Ada  ") == "Hello, Ada!"
