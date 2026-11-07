import ceaser
from collections import Counter
import string
import transposition
kworst_error = 30
kmax_gap = 8
ENGLISH_FREQ = {
    'A': 8.12, 'B': 1.49, 'C': 2.71, 'D': 4.32,
    'E': 12.02, 'F': 2.30, 'G': 2.03, 'H': 5.92,
    'I': 7.31, 'J': 0.10, 'K': 0.69, 'L': 3.98,
    'M': 2.61, 'N': 6.95, 'O': 7.68, 'P': 1.82,
    'Q': 0.11, 'R': 6.02, 'S': 6.28, 'T': 9.10,
    'U': 2.88, 'V': 1.11, 'W': 2.09, 'X': 0.17,
    'Y': 2.11, 'Z': 0.07
}

def frequency_score(text):
    text = text.lower()
    letters = [c for c in text if c in string.ascii_lowercase]
    if not letters:
        return float('-inf')
    counts = Counter(letters)
    n = len(letters)
    error = 0.0
    for letter, frequency in ENGLISH_FREQ.items():
        expected = n * frequency / 100
        observed = counts[letter]

        error += (observed - expected) ** 2 / expected
    return -error
    return error

def force_decrypt_ceaser(msg):
    candidates = []
    for shift in range(26):
        decrypted = ceaser.decrypt(msg, shift)
        candidates.append({
            "text": decrypted,
            "shift": shift,
            "frequency": frequency_score(decrypted)
        })
    candidates.sort(
        key=lambda x: x["frequency"],
        reverse=True
    )
    best = candidates[0]
    second = candidates[1]
    confident = (
        best["frequency"] > -kworst_error
        and best["frequency"] - second["frequency"] > kmax_gap
    )
    if confident:
        return best["shift"], best["text"]
    return None


def force_decrypt_transposition(msg):
    candidates = []
    for shift in range(26):
        decrypted = transposition.decrypt(msg, shift)
        candidates.append({
            "text": decrypted,
            "shift": shift,
            "frequency": frequency_score(decrypted)
        })
    candidates.sort(
        key=lambda x: x["frequency"],
        reverse=True
    )
    best = candidates[0]
    second = candidates[1]
    confident = (
        best["frequency"] > -kworst_error
        and best["frequency"] - second["frequency"] > kmax_gap
    )
    if confident:
        return best["shift"], best["text"]
    return None
