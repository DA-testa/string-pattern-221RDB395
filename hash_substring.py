# python3
# 221RDB395 Anastasija Bondare 13.grupa

def read_input():
   
    ievade = input() # Pārbaudes ievade burtiem "I" un "F".

    if "I" in ievade: # Ja ievadē ir burts "I"
        first_pattern = input().strip() # Ievada pirmo rindu, kas satur pattern jeb fragmentu.
        second_text = input().strip() # Ievada otro rindu, kas satur text jeb tekstu.
        return (first_pattern, second_text) # Atgriež abas līnijas vienā.

    if "F" in ievade: # Ja ievadē ir burts "F"
        with open("tests/06") as file: # Tiek atvērts fails "tests/06" un saglabāts kā file.
            first_pattern = file.readline().strip()   # Nolasa pirmo rindu, kas satur pattern jeb fragmentu.
            second_text = file.readline().strip()  # Nolasa otro rindu, kas satur text jeb tekstu.
        return (first_pattern, second_text) # Atgriež abas līnijas vienā.   

def print_occurrences(output): # Izvade.
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text): # Rabin–Karp’s algoritms.
    
    pattern_length = len(pattern) # Nosaka fragmenta garumu.
    text_length = len(text) # Nosaka teksta garumu.

    list_of_symbols = [] # Tiek izveidots saraksts, kas glabās sakristās vērtības - simbolus, ciparus,burtus.

    pattern_hash = hash(pattern) # Tiek piešķirta vērtība jeb atslēga katram pattern_hash. 
    text_hash = hash(text[: pattern_length]) # Tiek samazinināta vai pielīdzināta text_length ar pattern_length,
    # lai varētu pēc tam piešķirt text_hash atslēgu jeb vērtību

    for i in range(text_length - pattern_length + 1): # Iziet cauri virknēm, meklējot sakritības
        if text[i : i + pattern_length] == pattern and pattern_hash == text_hash: # Pārbauda, vai teksta virkne, kas sākas i pozīcijā un beidzās i + pattern_length sakrīt ar pattern
        #  un pārbauda, vai pattern_hash vērtība sakrīt ar text_hash vērtību  
            list_of_symbols.append(i) # Ja abi apgalvojumi sakrīt, tad pievieno sarakstam i-tās pozīcijas vērtības klāt

        if text_length-pattern_length > i: # Ja atlikušā virknes garums ir lielāks par i,
            text_hash = hash(text[i + 1 : i + pattern_length + 1]) # tad izveido jaunu text_hash vērtību, kas atspoguļo virkni no sākuma i+1 līdz beigām pattern_length + 1 
    
    return list_of_symbols # Atgriež visu sarakstu ar visām sakristajām vērtībām

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
