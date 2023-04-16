# python3
# 221RDB395 Anastasija Bondare 13.grupa

def read_input():
   
    ievade = input() # Pārbaudes ievade burtiem "I" un "F"

    if "I" in ievade: # Ja ievadē ir burts "I"
        first_pattern = input().strip() # Ievada pirmo rindu, kas satur pattern jeb fragmentu
        second_text = input().strip() # Ievada otro rindu, kas satur text jeb tekstu
        return (first_pattern, second_text) # Atgriež abas līnijas vienā

    if "F" in ievade: # Ja ievadē ir burts "F"
        with open("tests/06") as file: # Tiek atvērts fails "tests/06" un saglabāts kā file
            first_pattern = file.readline().strip()   # Nolasa pirmo rindu, kas satur pattern jeb fragmentu
            second_text = file.readline().strip()  # Nolasa otro rindu, kas satur text jeb tekstu
        return (first_pattern, second_text) # Atgriež abas līnijas vienā    

def print_occurrences(output): # Izvade
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text): # Rabin–Karp’s algoritms
    p = len(pattern)
    t = len(text)

    occurrences = []

    pattern_hash = hash(pattern) #pattern hash
    text_hash = hash(text[:p]) # text hash

    for i in range(t-p+1):
        if pattern_hash == text_hash and text[i:i+p] == pattern:
            occurrences.append(i)

        if i < t-p:
            text_hash = hash(text[i+1:i+p+1])
    
    # and return an iterable variable
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))