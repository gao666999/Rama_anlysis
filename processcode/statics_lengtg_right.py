def number(filenam,filename_saved):
    with open (filename,'r') as file:
        with open (filename_saved,'a+') as f:
            lines = file.readlines()
            length = len(lines)
            number = 0
            list_number = []
            #flaga = lines[0][22:26].strip()
            flaga = 'gao'
            #print flaga
            #print 'HHH'
            for i in range(0,length):
                if lines[i][:4].strip() == 'ATOM':
                    flagb = lines[i][22:26].strip()
                    #print "---"+flaga+"-------"+flagb+"----"+str(number)+"--"
                    if (flaga != flagb) :
                        number += 1
                        flaga = flagb
                    else:
                        continue
                elif lines[i][:4].strip() =='TER':
                    list_number.append(number)
                    '''
                    if number == 406:
                        print lines[i]
                        print "1488888888"
                    if number == 0:
                        #print >> f,lines[i]
                        #print '0000000000000'
                        '''
                    number = 0
                    flaga = 'gao'
                else:
                    continue
    return list_number

if __name__ == '__main__':
    #filename = '/Users/xg666/Desktop/getTER/usefuldata/cleaned4_loop.pdb'
    filename = '/Users/xg666/Desktop/getTER/statics/ter.pdb'
    #filename = '/Users/xg666/Desktop/getTER/pdbfile/pdb1hr0.ent'
    result_saved ='/Users/xg666/Desktop/getTER/result/number.txt'
    filename_saved ='/Users/xg666/Desktop/getTER/result/abnormal_filename.txt'
    with open (result_saved,'w+') as file:
        list_number = number(filename,filename_saved)
        #print list_number
        length = len(list_number)
            #print list_number
        print >>file,list_number
        print length
