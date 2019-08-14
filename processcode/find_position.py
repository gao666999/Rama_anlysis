def find_position(filename):
    with open (filename,'r') as file:
        n = 0
        for line in file:
            if line[:4] == 'ATOM' and n < 6:
                n += 1
                print '---' + line[:4]+'---'
                print '0___4'
                print '---'+line[22:26]+'---'
                print '22___26'
                print '---'+line[38:46]+'---'
                print '38---46'
                print '---'+line[46:54]+'---'
                print '46---54'

if __name__ == '__main__':
    #filename = '/Users/xg666/Desktop/getTER/pdbfile/pdb1hr0.ent'
    filename = '/Users/xg666/Desktop/getTER/usefuldata/test.pdb'
    find_position(filename)