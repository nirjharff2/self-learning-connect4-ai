from board import Board

def test_vertical_win():
    b = Board()
    for i in range(4):
        b.drop_piece(5-i, 0, 1)
    assert b.winning_move(1)
    print("Vertical win test passed")

def test_horizontal_win():
    b = Board()
    for i in range(4):
        b.drop_piece(5, i, 1)
    assert b.winning_move(1)
    print("✅ Horizontal win test passed")

if __name__ == "__main__":
    test_vertical_win()
    test_horizontal_win()
