# ASCII Kassi 2
# https://open.kattis.com/problems/asciikassi2
#
# Draws a diagonal ASCII box of side length n.

def draw_box(n):
    lines = []

    # --- Top half ---
    # Top peak
    lines.append(" " * (n + 1) + "x")

    # Upper slanted sides
    for i in range(n):
        left_spaces = n - i
        mid_spaces = 2 * i + 1
        lines.append(" " * left_spaces + "/" + " " * mid_spaces + "\\")

    # Middle line with two x's
    lines.append("x" + " " * (2 * n + 1) + "x")

    # --- Bottom half ---
    for i in range(n):
        left_spaces = i + 1
        mid_spaces = 2 * (n - i - 1) + 1
        lines.append(" " * left_spaces + "\\" + " " * mid_spaces + "/")

    # Bottom peak
    lines.append(" " * (n + 1) + "x")

    # Print result
    for L in lines:
        print(L)


draw_box(5)
