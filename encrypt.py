def generate_key_table(keyword):
    """
    Generates the Playfair cipher key table from the given keyword.
    """
    key = keyword.replace("J", "I")  # I and J are treated as the same letter
    key_set = set(key)
    alphabet_set = set("ABCDEFGHIKLMNOPQRSTUVWXYZ")  # J is eliminated
    remaining_letters = alphabet_set - key_set
    table = [list(key)]

    for letter in remaining_letters:
        if len(table[-1]) == 5:
              table.append([])
        table[-1].append(letter)

    return table


def find_position(key_table, letter):
    """
    Finds the row and column position of the given letter in the Playfair cipher key table.
    """
    for row_idx, row in enumerate(key_table):
        if letter in row:
            col_idx = row.index(letter)
            return row_idx, col_idx


def encrypt_pair(key_table, pair):
    """
    Encrypts a pair of letters using the Playfair cipher key table.
    """
    a, b = pair
    a_row, a_col = find_position(key_table, a)
    b_row, b_col = find_position(key_table, b)

    if a_row == b_row:
        # If the letters are in the same row, take the letters to the right,
        # wrapping around to the beginning of the row if necessary.
        return key_table[a_row][(a_col + 1) % 5] + key_table[b_row][(b_col + 1) % 5]
    elif a_col == b_col:
        # If the letters are in the same column, take the letters below,
        # wrapping around to the top of the column if necessary.
        return key_table[(a_row + 1) % 5][a_col] + key_table[(b_row + 1) % 5][b_col]
    else:
        # If the letters are in different rows and columns, take the letters
        # at the intersection of their respective rows and columns.
        return key_table[a_row][b_col] + key_table[b_row][a_col]


def decrypt_pair(key_table, pair):
    """
    Decrypts a pair of letters using the Playfair cipher key table.
    """
    a, b = pair
    a_row, a_col = find_position(key_table, a)
    b_row, b_col = find_position(key_table, b)

    if a_row == b_row:
        # If the letters are in the same row, take the letters to the left,
        # wrapping around to the end of the row if necessary.
        return key_table[a_row][(a_col - 1) % 5] + key_table[b_row][(b_col - 1) % 5]
    elif a_col == b_col:
        # If the letters are in the same column, take the letters above,
        # wrapping around to the bottom of the column if necessary.
        return key_table[(a_row - 1) % 5][a_col] + key_table[(b_row - 1) % 5][b_col]
    else:
        # If the letters are in different rows and columns, take the letters
        # at the intersection of their respective rows and columns.
        return key_table[a_row][b_col] + key_table[b_row][a_col]


def playfair_cipher(keyword, source_file, destination_file, mode):
    """
    Encrypts or decrypts the contents of the source file using the Playfair cipher with the given keyword,
