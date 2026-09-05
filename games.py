"""Interactive mini-games CLI for sakura-ai-test (Issue #18).

Implements the "新玩法" request from Issue #18 as a small collection of
terminal games: guess-the-number and a higher-or-lower dice game.

Run standalone (the greeting entrypoint ``main.py`` stays untouched)::

    python games.py            # interactive menu (default)
    python games.py guess      # guess-the-number
    python games.py hl         # higher-or-lower dice
    python games.py help       # command help

All game output is ASCII by default. The Ciallo kaomoji is only printed
on victory, with an ASCII fallback for consoles that cannot encode it
(e.g. Windows GBK/cp936), following this repository's conventions.
"""

from __future__ import annotations

import random
import sys
from collections.abc import Callable

InputFunc = Callable[[str], str]
OutputFunc = Callable[[str], None]

# 庆祝用语：胜利时输出 Ciallo 颜文字，GBK 等控制台降级为 ASCII
CIALLO_GREETING = "Ciallo～(∠・ω< )⌒☆"

GUESS_LOW = 1
GUESS_HIGH = 100
GUESS_MAX_ATTEMPTS = 7

HL_ROUNDS = 5
HL_DICE_SIDES = 6

_QUIT_WORDS = ("q", "quit", "exit")

HELP_TEXT = """\
Sakura-AI Mini Games

Usage:
  python games.py            interactive menu (default)
  python games.py guess      guess-the-number (1-100, 7 attempts)
  python games.py hl         higher-or-lower dice (5 rounds)
  python games.py help       show this help

In-game commands:
  q / quit / exit            abort the current game or leave the menu
""".rstrip()


def roll_dice(sides: int = HL_DICE_SIDES, rng: random.Random | None = None) -> int:
    """Roll one die with the given number of sides."""
    generator = rng if rng is not None else random.Random()
    return generator.randint(1, sides)


def _celebrate(output_func: OutputFunc) -> None:
    """Print the Ciallo kaomoji, degrading to ASCII on encoding errors."""
    try:
        output_func(CIALLO_GREETING)
    except UnicodeEncodeError:
        # 部分控制台编码（如 Windows 的 GBK/cp936）无法表示颜文字，降级为 ASCII 输出
        output_func("Ciallo~")


def play_number_guess(
    input_func: InputFunc = input,
    output_func: OutputFunc = print,
    rng: random.Random | None = None,
    low: int = GUESS_LOW,
    high: int = GUESS_HIGH,
    max_attempts: int = GUESS_MAX_ATTEMPTS,
) -> bool:
    """Run one guess-the-number game. Returns True when the player wins."""
    generator = rng if rng is not None else random.Random()
    answer = generator.randint(low, high)
    output_func(
        f"Guess my number between {low} and {high}! You have {max_attempts} attempts."
    )
    attempts_used = 0
    while attempts_used < max_attempts:
        prompt = f"Attempt {attempts_used + 1}/{max_attempts} > "
        try:
            raw = input_func(prompt)
        except EOFError:
            output_func("No more input, game over.")
            return False
        if raw is None:
            output_func("No more input, game over.")
            return False
        text = raw.strip()
        if text.lower() in _QUIT_WORDS:
            output_func("Game aborted.")
            return False
        try:
            guess = int(text)
        except ValueError:
            # 非数字输入不消耗尝试次数
            output_func("Please enter a whole number (or 'q' to quit).")
            continue
        if not low <= guess <= high:
            # 超出范围的输入同样不消耗尝试次数
            output_func(f"Please guess a number between {low} and {high}.")
            continue
        attempts_used += 1
        if guess < answer:
            output_func("Too low!")
        elif guess > answer:
            output_func("Too high!")
        else:
            unit = "attempt" if attempts_used == 1 else "attempts"
            output_func(f"Correct! You got it in {attempts_used} {unit}.")
            _celebrate(output_func)
            return True
    output_func(f"Out of attempts! The number was {answer}.")
    output_func("Better luck next time!")
    return False


def _ask_hl_choice(
    input_func: InputFunc,
    output_func: OutputFunc,
    prompt: str,
) -> str | None:
    """Ask for an h/l/q choice, re-prompting on invalid input.

    Returns None when the input stream is closed.
    """
    while True:
        try:
            raw = input_func(prompt)
        except EOFError:
            return None
        if raw is None:
            return None
        choice = raw.strip().lower()
        if choice in ("h", "l") or choice in _QUIT_WORDS:
            return choice
        output_func("Please answer 'h' or 'l' (or 'q' to quit).")


def play_higher_lower(
    input_func: InputFunc = input,
    output_func: OutputFunc = print,
    rng: random.Random | None = None,
    rounds: int = HL_ROUNDS,
    sides: int = HL_DICE_SIDES,
) -> bool:
    """Run one higher-or-lower dice game. Returns True when the player wins."""
    generator = rng if rng is not None else random.Random()
    score = 0
    needed = rounds // 2 + 1
    current = roll_dice(sides, generator)
    output_func(f"Higher or lower! Dice: 1-{sides}, rounds: {rounds}.")
    output_func(
        f"Guess if the next roll is higher (h) or lower (l); q quits. "
        f"Score {needed}+ to win."
    )
    for round_no in range(1, rounds + 1):
        prompt = f"Round {round_no}/{rounds} -- roll: {current}. Higher or lower? (h/l/q) "
        choice = _ask_hl_choice(input_func, output_func, prompt)
        if choice is None:
            output_func("No more input, game over.")
            return False
        if choice == "q":
            output_func(f"Quit after {round_no - 1} round(s). Final score: {score}/{rounds}.")
            return False
        nxt = roll_dice(sides, generator)
        while nxt == current:
            # 平局没有意义，自动重掷直到点数不同
            output_func("Tie! Rerolling...")
            nxt = roll_dice(sides, generator)
        if (nxt > current and choice == "h") or (nxt < current and choice == "l"):
            score += 1
            output_func(f"Correct! It was {nxt}. Score: {score}")
        else:
            output_func(f"Wrong! It was {nxt}. Score: {score}")
        current = nxt
    output_func(f"Game over! Final score: {score}/{rounds}.")
    if score >= needed:
        output_func("You win!")
        _celebrate(output_func)
        return True
    output_func("Better luck next time!")
    return False


def show_menu(
    input_func: InputFunc = input,
    output_func: OutputFunc = print,
    rng: random.Random | None = None,
) -> None:
    """Show the game menu and run the chosen game until the player quits."""
    output_func("=== Sakura-AI Mini Games ===")
    output_func("[1] Guess the number (1-100, 7 attempts)")
    output_func("[2] Higher or lower (dice, 5 rounds)")
    output_func("[0] Quit")
    while True:
        try:
            raw = input_func("Select a game: ")
        except EOFError:
            return
        if raw is None:
            return
        choice = raw.strip().lower()
        if choice in ("", "0") or choice in _QUIT_WORDS:
            output_func("Bye!")
            return
        if choice in ("1", "guess", "g"):
            play_number_guess(input_func, output_func, rng)
        elif choice in ("2", "hl", "higher-lower"):
            play_higher_lower(input_func, output_func, rng)
        else:
            output_func(f"Invalid choice: {choice!r}. Please enter 1, 2 or 0.")
            continue
        output_func("Back to menu -- [1] guess [2] higher/lower [0] quit")


def run_cli(
    argv: list[str] | None = None,
    input_func: InputFunc = input,
    output_func: OutputFunc = print,
    rng: random.Random | None = None,
) -> None:
    """Entry point of the mini-games CLI (defaults to the interactive menu)."""
    args = list(sys.argv[1:] if argv is None else argv)
    command = args[0].strip().lower() if args else "menu"
    if command in ("guess", "number", "guess-number"):
        play_number_guess(input_func, output_func, rng)
    elif command in ("hl", "higher-lower", "higherlower", "dice"):
        play_higher_lower(input_func, output_func, rng)
    elif command in ("help", "-h", "--help"):
        output_func(HELP_TEXT)
    elif command == "menu":
        show_menu(input_func, output_func, rng)
    else:
        output_func(f"Unknown command: {command!r} -- starting the menu instead.")
        show_menu(input_func, output_func, rng)


if __name__ == "__main__":
    run_cli()
