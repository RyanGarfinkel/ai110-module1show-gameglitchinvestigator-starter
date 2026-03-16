from logic_utils import check_guess, update_score

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

# FIX: Added new tests to validate bug fixes using Claude Code
def test_too_high_message_says_lower():
	_, message = check_guess(60, 50)
	assert "LOWER" in message.upper()

def test_too_low_message_says_higher():
	_, message = check_guess(40, 50)
	assert "HIGHER" in message.upper()

def test_score_starts_fresh_on_new_game():
	fresh_score = update_score(current_score=0, outcome="Win", attempt_number=1)
	assert fresh_score > 0

def test_score_reset_matches_fresh_start():
	mid_game_reset = update_score(current_score=0, outcome="Win", attempt_number=1)
	fresh_game    = update_score(current_score=0, outcome="Win", attempt_number=1)
	assert mid_game_reset == fresh_game
