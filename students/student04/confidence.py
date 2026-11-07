from collections import Counter
import ceaser
import string
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
    letters = [c for c in text.upper() if c in string.ascii_uppercase]

    if not letters:
        return float("inf")

    counts = Counter(letters)
    n = len(letters)

    error = 0

    for letter, frequency in ENGLISH_FREQ.items():
        expected = n * frequency / 100
        observed = counts[letter]
        error += (observed - expected) ** 2 / expected

    return error

def force_decrypt(msg):
    candidates = []
    for shift in range(26):
        decrypted = ceaser.decrypt(msg, shift)
        candidates.append({
            "text": decrypted,
            "shift": shift,
            "frequency": frequency_score(decrypted)})
    candidates.sort(key=lambda x: x["frequency"])
    return candidates[0]["shift"], candidates[0]["text"]
def force_decrypt_transposition(msg):
        candidates = []
    for shift in range(1,len(msg)):
        decrypted = ceaser.decrypt(msg, shift)
        candidates.append({
            "text": decrypted,
            "shift": shift,
            "frequency": frequency_score(decrypted)})
    candidates.sort(key=lambda x: x["frequency"])
    return candidates[0]["shift"], candidates[0]["text"]

print(force_decrypt("L DXLWW MZLE NCZDDPO ESP WLVP PLCWJ TY ESP XZCYTYR MPQZCP ESP DEZCX LCCTGPO ESP EPLX HZY ESP XLENS TY ESP WLDE XTYFEP LQEPC L"))
peint(force_decrypt_transposition("TMWEH CEUOSL TPETRU E HHIITUTU DRCISSR LYSRRTOETL ROSNG HBT AAE UE HS TLOS SEETORUWC  DAMMAECE NDD WTHOADHTLEALEONOEM AIT  ELREOIIVYLMR M ETYSHBF  YN CTE YBET"))
