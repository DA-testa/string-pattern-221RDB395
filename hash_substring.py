# python3


def read_input():
   
    ievade = input()

    if "I" in ievade: 
        first_line = input().strip() 
        second_line = input().strip()
        

    if "F" in ievade: 
        ievade = "tests/06" 
        with open(ievade) as file: 
            first_line = file.readline().strip()  # pattern
            second_line = file.readline().strip()  # text
               

    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow
    # after input type choice
    # read two lines 
    # first line is pattern 
    # second line is text in which to look for pattern 
    
    # return both lines in one return
    
    # this is the sample return, notice the rstrip function
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    p = len(pattern)
    t = len(text)

    occurences = []

    ph = hash(pattern) #pattern hash
    th = hash(text[:p]) # text hash

    for i in range(t-p+1):
        if ph == th and text[i:i+p] == pattern:
            occurences.append(i)

        if i < t-p:
            th = hash(text[i+1:i+p+1])
    

    # and return an iterable variable
    return occurences

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))