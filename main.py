def print_cstep_pattern():
    """Prints the word 'CSTEP' in a pattern form using a block style."""
    C = [
        " CCC ",
        "C    ",
        "C    ",
        "C    ",
        " CCC "
    ]
    S = [
        " SSSS ",
        "S     ",
        " SSS  ",
        "    S ",
        " SSSS "
    ]
    T = [
        "TTTTTTT",
        "   T   ",
        "   T   ",
        "   T   ",
        "   T   "
    ]
    E = [
        "EEEEE ",
        "E     ",
        "EEE   ",
        "E     ",
        "EEEEE "
    ]
    P = [
        "PPPP  ",
        "P   P ",
        "PPPP  ",
        "P     ",
        "P     "
    ]

    # Print the word "CSTEP" in the pattern
    for i in range(5):
        print(C[i] + " " + S[i] + " " + T[i] + " " + E[i] + " " + P[i])

# Example usage
if __name__ == "__main__":
    print_cstep_pattern()
