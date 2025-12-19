from src.kattis.aaawa import final_rank


def test_final_rank():
    T = 4
    P = 3
    F = 2

    teams = [
        "AAP",
        "PPP",
        "APP",
        "AAA"
    ]

    chants = [
        (1, "Aaaw"),
        (2, "yaaaay"),
        (3, "yaaay"),
        (4, "yaaaay")
    ]

    expected_rank = final_rank(T, P, F, teams, chants)
    assert isinstance(expected_rank, int)
