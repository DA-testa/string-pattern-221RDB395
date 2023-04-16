# python3
# 221RDB395 Anastasija Bondare 13.grupa

def read_input():
   
    ievade = input()

    if "I" in ievade: 
        first_line = input().strip() 
        second_line = input().strip()
        

    if "F" in ievade: 
        ievade = "tests/06" 
        with open(ievade, 'r') as file: 
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

#def print_occurrences(output):
    # this function should control output, it doesn't need any return
    #print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm 
    p = len(pattern)
    t = len(text)

    count = 0

    for i in range(0,t-p+1):
        found = True
        for j in range (0, p):
            if pattern[j] != text[i+j]:
                found = False
                break
        if found:
            count += 1
    
    if not count == 0:
        print count
        


    # and return an iterable variable
    return [0]


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

