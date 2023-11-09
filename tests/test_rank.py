from tabletoppy.rank import Rank


def test_rank_str_for_named_cards():
    assert str(Rank.ACE) == "A"


def test_rank_str_for_numeric_cards():
    assert str(Rank.TEN) == "10"


def test_rank_str_for_jokers():
    assert str(Rank.JOKER) == "Joker"
