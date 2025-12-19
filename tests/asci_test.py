from src.kattis.ASCII import draw_box


def test_draw_box_returns_value():
    assert draw_box(1) is not None
    assert draw_box(5) is not None
