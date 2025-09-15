from myproject.main import evaluate_guess


def test_evaluate_guess_low():
    assert evaluate_guess(10, 5) == "low"


def test_evaluate_guess_high():
    assert evaluate_guess(10, 15) == "high"


def test_evaluate_guess_correct():
    assert evaluate_guess(10, 10) == "correct"
