"""Tests for the unified CLI (cli.py) — Issue #20."""

from __future__ import annotations

import sys

import cli
import pytest


class TestBuildParser:
    """Verify the argument parser is well-formed."""

    def test_parser_creation(self) -> None:
        parser = cli._build_parser()
        assert parser.prog == "sakura"


class TestGreetCommand:
    """Tests for the ``greet`` subcommand."""

    def test_default_greeting(self, capsys: pytest.CaptureFixture[str]) -> None:
        cli.run(["greet"])
        captured = capsys.readouterr()
        assert "Hello, Sakura-AI!" in captured.out
        # Ciallo kaomoji should be present (stdout is UTF-8 in tests)
        assert "Ciallo" in captured.out

    def test_custom_name(self, capsys: pytest.CaptureFixture[str]) -> None:
        cli.run(["greet", "--name", "Alice"])
        captured = capsys.readouterr()
        assert "Hello, Alice!" in captured.out

    def test_ascii_only(self, capsys: pytest.CaptureFixture[str]) -> None:
        cli.run(["greet", "--ascii-only"])
        captured = capsys.readouterr()
        assert "Hello, Sakura-AI!" in captured.out
        # The kaomoji line should NOT be printed when --ascii-only is set
        lines = captured.out.strip().split("\n")
        assert len(lines) == 1

    def test_custom_name_and_ascii_only(
        self, capsys: pytest.CaptureFixture[str]
    ) -> None:
        cli.run(["greet", "--name", "Bob", "--ascii-only"])
        captured = capsys.readouterr()
        assert "Hello, Bob!" in captured.out
        lines = captured.out.strip().split("\n")
        assert len(lines) == 1


class TestGamesCommand:
    """Tests for the ``games`` subcommand (help branch only, to avoid stdin)."""

    def test_games_help(self, capsys: pytest.CaptureFixture[str]) -> None:
        cli.run(["games", "help"])
        captured = capsys.readouterr()
        assert "Sakura-AI Mini Games" in captured.out


class TestNoCommand:
    """When no subcommand is given, the CLI should print help and exit."""

    def test_no_args_prints_help(self, capsys: pytest.CaptureFixture[str]) -> None:
        with pytest.raises(SystemExit) as exc_info:
            cli.run([])
        assert exc_info.value.code == 0
        captured = capsys.readouterr()
        assert "greet" in captured.out or "usage" in captured.out.lower()


class TestVersion:
    """--version should print version string and exit."""

    def test_version_flag(self, capsys: pytest.CaptureFixture[str]) -> None:
        with pytest.raises(SystemExit) as exc_info:
            cli.run(["--version"])
        assert exc_info.value.code == 0
        captured = capsys.readouterr()
        assert cli.__version__ in captured.out


class TestSafePrint:
    """Verify the _safe_print helper handles encoding errors gracefully."""

    def test_normal_output(self, capsys: pytest.CaptureFixture[str]) -> None:
        cli._safe_print("Hello")
        captured = capsys.readouterr()
        assert "Hello" in captured.out

    def test_unicode_fallback(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """Simulate a console that cannot encode kaomoji."""
        import io

        buf = io.BytesIO()

        class AsciiWriter:
            """Fake sys.stdout that only accepts ASCII."""

            def write(self, s: str) -> int:
                encoded = s.encode("ascii")  # raises UnicodeEncodeError on non-ASCII
                buf.write(encoded)
                return len(s)

            def flush(self) -> None:
                pass

        monkeypatch.setattr(sys, "stdout", AsciiWriter())
        # Should NOT raise, even with kaomoji
        cli._safe_print("Ciallo～(∠・ω< )⌒☆")
        output = buf.getvalue().decode("ascii")
        assert "Ciallo" in output
