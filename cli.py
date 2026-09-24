"""Unified command-line interface for sakura-ai-test (Issue #20).

Provides a single ``sakura`` entry point that dispatches to the greeting
module and the mini-games module via subcommands.

Usage examples::

    python cli.py greet                # default greeting
    python cli.py greet --name Alice   # greet a specific person
    python cli.py games                # interactive game menu
    python cli.py games guess          # guess-the-number
    python cli.py games hl             # higher-or-lower dice
    python cli.py --version            # show version
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence

import games

__version__ = "0.1.0"

CIALLO_GREETING = "Ciallo～(∠・ω< )⌒☆"


def _safe_print(text: str) -> None:
    """Print *text* with a graceful ASCII fallback on encoding errors."""
    try:
        print(text)
    except UnicodeEncodeError:
        # Windows GBK/cp936 等编码无法显示颜文字，降级为 ASCII
        print(text.encode("ascii", errors="replace").decode("ascii"))


def _build_parser() -> argparse.ArgumentParser:
    """Construct and return the top-level argument parser."""
    parser = argparse.ArgumentParser(
        prog="sakura",
        description="Sakura-AI Test Project — CLI",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    subparsers = parser.add_subparsers(dest="command")

    # --- greet ---------------------------------------------------------
    greet_parser = subparsers.add_parser(
        "greet",
        help="Print a greeting message",
    )
    greet_parser.add_argument(
        "--name",
        default="Sakura-AI",
        help="Name to greet (default: Sakura-AI)",
    )
    greet_parser.add_argument(
        "--ascii-only",
        action="store_true",
        help="Force pure ASCII output (skip kaomoji)",
    )

    # --- games ---------------------------------------------------------
    games_parser = subparsers.add_parser(
        "games",
        help="Play mini-games",
    )
    games_parser.add_argument(
        "game",
        nargs="?",
        default="menu",
        choices=["menu", "guess", "hl", "help"],
        help="Game to launch (default: menu)",
    )

    return parser


def cmd_greet(args: argparse.Namespace) -> None:
    """Execute the *greet* subcommand."""
    _safe_print(f"Hello, {args.name}!")
    if not args.ascii_only:
        _safe_print(CIALLO_GREETING)


def cmd_games(args: argparse.Namespace) -> None:
    """Execute the *games* subcommand by delegating to ``games.run_cli``."""
    game_argv: list[str] = [args.game] if args.game != "menu" else []
    games.run_cli(argv=game_argv)


def run(argv: Sequence[str] | None = None) -> None:
    """Parse *argv* (defaults to ``sys.argv[1:]``) and dispatch."""
    parser = _build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.command == "greet":
        cmd_greet(args)
    elif args.command == "games":
        cmd_games(args)
    else:
        # No subcommand given — print help
        parser.print_help()
        sys.exit(0)


if __name__ == "__main__":
    run()
