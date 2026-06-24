from logic_utils import check_guess
from app import get_range_for_difficulty, update_score


def test_winning_guess():
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"


def test_too_high_says_go_lower():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High" and "LOWER" in message


def test_too_low_says_go_higher():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low" and "HIGHER" in message


def test_check_guess_both_ints():
    outcome, _ = check_guess(42, 42)
    assert outcome == "Win"


def test_hard_range_is_larger_than_normal():
    _, hard_high = get_range_for_difficulty("Hard")
    _, normal_high = get_range_for_difficulty("Normal")
    assert hard_high > normal_high


def test_win_score_increases():
    new_score = update_score(0, "Win", 1)
    assert new_score > 0
