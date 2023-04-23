from tabletoppy.rank import Rank


def test_rank_str_for_named_cards():
    assert "A" == str(Rank.ACE)


def test_rank_str_for_numeric_cards():
    assert "10" == str(Rank.TEN)


def test_rank_str_for_jokers():
    assert "Joker" == str(Rank.JOKER)
