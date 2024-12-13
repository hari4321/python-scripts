"""
This program prints a diamond shaped pattern in the console
"""

def print_diamond_pattern(n):
    """Prints a diamond pattern with n rows."""
    # Top half of the diamond
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    
    # Bottom half of the diamond
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

# Example usage
if __name__ == "__main__":
    rows = 5  # Number of rows for the diamond
    print_diamond_pattern(rows)
