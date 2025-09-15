import random
import sys


def evaluate_guess(secret: int, guess: int) -> str:
	"""Return 'low', 'high', or 'correct' comparing guess to secret."""
	if guess < secret:
		return "low"
	if guess > secret:
		return "high"
	return "correct"


def play_round(min_value: int = 1, max_value: int = 100, max_attempts: int = 7) -> None:
	"""Play a single round of the guessing game on the CLI."""
	secret = random.randint(min_value, max_value)
	print(f"I'm thinking of a number between {min_value} and {max_value}.")
	print(f"You have {max_attempts} attempts to guess it.")

	attempts = 0
	while attempts < max_attempts:
		attempts += 1
		try:
			raw = input(f"Attempt {attempts}: Enter your guess: ")
		except (EOFError, KeyboardInterrupt):
			print('\nGoodbye!')
			return

		raw = raw.strip()
		if not raw:
			print("Please enter a number.")
			attempts -= 1
			continue

		try:
			guess = int(raw)
		except ValueError:
			print("That's not a valid integer. Try again.")
			attempts -= 1
			continue

		result = evaluate_guess(secret, guess)
		if result == "correct":
			print(f"Correct! You guessed the number in {attempts} attempts.")
			return
		if result == "low":
			print("Too low.")
		else:
			print("Too high.")

	print(f"Sorry — you've used all {max_attempts} attempts. The number was {secret}.")


def main(argv=None) -> int:
	"""Command-line entry point. Returns 0 on normal exit."""
	if argv is None:
		argv = sys.argv[1:]

	# Allow optional args: min max attempts
	try:
		if len(argv) >= 1:
			min_v = int(argv[0])
		else:
			min_v = 1
		if len(argv) >= 2:
			max_v = int(argv[1])
		else:
			max_v = 100
		if len(argv) >= 3:
			attempts = int(argv[2])
		else:
			attempts = 7
	except ValueError:
		print("Usage: main.py [min max attempts]")
		return 2

	if min_v >= max_v:
		print("Minimum must be less than maximum.")
		return 2

	play_round(min_v, max_v, attempts)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
