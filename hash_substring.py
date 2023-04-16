# python3
# 221RDB395 Anastasija Bondare 13.grupa

def read_input():
   
    ievade = input() # Pārbaudes ievade burtiem "I" un "F"

    if "I" in ievade: # Ja ievadē burts "I"
        first_pattern = input().strip() # Ievada pirmo rindu, kas satur pattern jeb fragmentu
        second_text = input().strip() # Ievada orto rindu, kas satur text jeb tekstu
        return (first_pattern, second_text) # Atgriež abas līnijas vienā

    if "F" in ievade: 
        with open("tests/06") as file: 
            first_line = file.readline().strip()  # pattern
            second_line = file.readline().strip()  # text
        return (first_line, second_line) # Atgriež abas līnijas vienā    

    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    #return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    p = len(pattern)
    t = len(text)

    occurrences = []

    ph = hash(pattern) #pattern hash
    th = hash(text[:p]) # text hash

    for i in range(t-p+1):
        if ph == th and text[i:i+p] == pattern:
            occurrences.append(i)

        if i < t-p:
            th = hash(text[i+1:i+p+1])
    

    # and return an iterable variable
    return occurrences

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))