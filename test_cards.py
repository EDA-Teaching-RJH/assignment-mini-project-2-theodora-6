import pytest 
from pack import open_pack, get_card
from utils import valid_name
from file_handler import save_cards, load_cards

def test_open_pack_size():
    cards = open_pack()
    assert len(cards) == 3

def test_get_card_not_none():
    card = get_card()
    assert card is not None

