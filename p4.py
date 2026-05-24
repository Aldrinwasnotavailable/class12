with open("Class12/test.txt", 'r') as file:
    for line in file:
        line = line.strip()            # Remove leading/trailing whitespace
        transformed = '#'.join(line)   # Put '#' between every character
        print(transformed + '#')       # Add final '#' at the end