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

def test_card_has_attributes():
    card = get_card()
    assert hasattr(card, "name")
    assert hasattr(card, "rarity")

def test_valid_name():
    assert valid_name("Jinx")
    assert valid_name("Vi")

def test_invalid_name():
    assert not valid_name("Jinx123")
    assert not valid_name("123")

def test_empty_name():
    assert not valid_name("")

def test_save_and_load():
    cards = open_pack()
    save_cards(cards)

    loaded = load_cards()
    assert len(loaded) > 0

def test_multiple_packs():
    for i in range(5):
        cards = open_pack()
        assert len(cards) == 3