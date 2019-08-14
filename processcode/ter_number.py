def statics_ter(filename):
    with open (filename,'r') as file:
        n = 0
        for line in file:
            if line[:4].strip() == 'TER':
                n += 1
    return n
def print_ter(filename):
    with open (filename,'r') as file:
        n = 0
        lines = file.readlines()
        length = len(lines)
        for i in range(0,length):
            if lines[i][:4].strip() == 'TER':
                print lines[i-1]
                print lines[i]
                print lines[i+1]

if __name__ == '__main__':
    filename = '/Users/xg666/Desktop/getTER/usefuldata/cleaned4_loop.pdb'
    number = statics_ter(filename)
    print number
    #print_ter(filename)