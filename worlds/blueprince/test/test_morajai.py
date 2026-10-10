
from ..morajai_randomizer import *

def test_rotateRow():
    board = list("012345678")
    i = 0
    expected = list("201345678")
    rotateRow(board, i, "")
    assert board == expected

def test_applyRed():
    board = list("000008888")
    expected = list("111110000")
    applyRed(board, 0, "1")
    assert board == expected

def test_swap():
    board = list("012345678")
    a, b = 0, 8
    expected = list("812345670")
    swap(board, a, b)
    assert board == expected

def test_swapAcross():
    board = list("012345678")
    i = 0
    expected = list("812345670")
    swapAcross(board, i, "")
    assert board == expected

def test_applyBlue():
    board = list("000040030")
    i = 7
    expected = list("000030040")
    applyBlue(board, i, "")
    assert board == expected

def test_shiftUp():
    board = list("012345678")
    i = 3
    expected = list("312045678")
    shiftUp(board, i, "")
    assert board == expected

def test_shiftDown():
    board = list("000678123")
    i = 3
    expected = list("000178623")
    shiftDown(board, i, "")
    assert board == expected

def test_rotateAround():
    board = list("012345678")
    i = 0
    expected = list("032415678")
    rotateAround(board, i, "")
    assert board == expected

def test_applyOrange():
    board = list("010101010")
    i = 4
    expected = list("010111010")
    applyOrange(board, i, "")
    assert board == expected

def test_invertColors():
    board = list("010101010")
    i = 4
    expected = list("000010000")
    invertColors(board, i, "1", "0")
    assert board == expected

def test_is_unsolvable_state():
    board = list("012345670")
    target = list("8888")
    expected = True
    result = is_unsolvable_state(board, target)
    assert result == expected

def test_is_solved():
    board = list("101000101")
    target = list("1111")
    expected = True
    result = is_solved(board, target)
    assert result == expected

