import json

def get_list(filename):
    with open (filename,'r') as file:
        number_list = []
        for line in file:
            number_list.append(json.loads(line))
        length = len(number_list)
        return number_list,length


if __name__ =='__main__':
    filename = '/Users/xg666/Desktop/loop/getTER/result/number.txt'
    or_file = '/Users/xg666/Desktop/loop/getTER/usefuldata/cleaned4_loop.pdb'
    newfile = '/Users/xg666/Desktop/loop/getTER/usefuldata/finally_marked.pdb'
    number_list,length = get_list(filename)
    print length
    '''
    with open(newfile,'w+') as newfile:
        with open(or_file,'r') as file:
            number1 = number_list[0]
            string1 = 'MARK    ' + str(number1) + '\n'
            newfile.write(string1)
            lines = file.readlines()
            length = len(lines)
            n = 0
            for i in range(0,length):
                if i < length - 1:
                    if lines[i][:4].strip() == 'TER' and lines[i+1][:4].strip() != 'END':
                        n += 1
                        print str(i)+'-------'+str(n)
                        #print number_list[114275]
                        number = number_list[n]
                        #number = 0
                        string = 'MARK    ' + str(number) +'\n'
                        newfile.write(lines[i])
                        newfile.write(string)
                        continue
                    elif lines[i][:4].strip() == 'END'and lines[i+1][:4].strip() == 'ATOM':
                        n += 1
                        number = number_list[n]
                        string = 'MARK    ' + str(number) + '\n'
                        newfile.write(lines[i])
                        newfile.write(string)
                        continue
                    else:
                        newfile.write(lines[i])
                else:
                    newfile.write(lines[i])
                    print n
    '''
