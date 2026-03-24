"""
Link to problem: https://www.freecodecamp.org/learn/daily-coding-challenge/2026-03-21

                    QR Decoder
Given a 6x6 matrix (array of arrays), representing a QR code, return the string of binary data in the code.

The QR code may be given in any rotation of 90 degree increments.
A correctly oriented code has a 2x2 group of 1's (orientation markers) in the bottom-left, top-left, and top-right corners.
The three 2x2 orientation markers are not part of the binary data.
The binary data is read left-to-right, top-to-bottom (like a book) when the QR code is correctly oriented.
A code will always have exactly one valid orientation.
For example, given:

[
  "110011",
  "110011",
  "000000",
  "000000",
  "110000",
  "110001"
]
or given the same code with a different orientation:

[
  "110011",
  "110011",
  "000000",
  "000000",
  "000011",
  "100011"
]
Return "000000000000000000000001", all the binary data excluding the three 2x2 orientation markers.
"""
def rotate_90(matrix):
    n = len(matrix)
    return [''.join(matrix[n-1-r][c] for r in range(n)) for c in range(n)]

def check_marker(matrix, r, c):
    return all(matrix[r+dr][c+dc] == '1' for dr in range(2) for dc in range(2))

def is_correct_orientation(matrix):
    return check_marker(matrix, 0, 0) and check_marker(matrix, 0, 4) and check_marker(matrix, 4, 0)

def decode_qr(qr_code):
    # We have 4 rotations: 90, 180, 270, 360
    for _ in range(4):
        if is_correct_orientation(qr_code):
            break
        qr_code = rotate_90(qr_code)
    skip = set()
    for dr in range(2):
        for dc in range(2):
            skip.add((dr, dc))      # top-left
            skip.add((dr, 4+dc))    # top-right
            skip.add((4+dr, dc))    # bottom-left

    result = ''
    for r in range(6):
        for c in range(6):
            if (r, c) not in skip:
                result += qr_code[r][c]
    return result


print(decode_qr(["110011", "110011", "000000", "000000", "110000", "110001"])) # should return "000000000000000000000001".
print(decode_qr(["100011", "000011", "000000", "000000", "110011", "110011"])) # should return "000000000000000000000001".
print(decode_qr(["110011", "111111", "010000", "110000", "110011", "110100"])) # should return "001101000011000000110100".
print(decode_qr(["011011", "101011", "101000", "100010", "110011", "111011"])) # should return "010001000100010101010110".
print(decode_qr(["111100", "110001", "100011", "001101", "110011", "110011"])) # should return "010000100100100101001110".
