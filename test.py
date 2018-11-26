import os

def convertFile(inFile, outFile):
    inputFile = open(inFile, 'r')
    outputFile = open(outFile, 'w')
    header1 = 0
    header2 = 1
    count2 = 1
    out= ''
    lastdot = 1
    for line in inputFile:
         if line[0] == '*':
             length = len(line) 
             star = len(line.lstrip('*'))
             nos = length - star
             if nos == 1:
                 header1 += 1
                 out = out + str(header1) + '.' + line.lstrip('*')
             elif nos == 2:
                 out = out +  str(header1) + '.' + str(header2) + line.lstrip('*')
                 count1 = header2
                 header2 = header2 + 1
             elif nos == 3:
                 out = out + str(header1) + '.' + str(count1) + '.' + str(count2)+ line.lstrip('*')
                 count2 = count1
                 count1 = count1 + 1
             elif nos == 4:
                 out = out + str(header1) + '.' + str(count2) + '.' + str(count2) + '.' + str(count2) + line.lstrip('*')    
         elif line[0] == '.':
             length = len(line) 
             dot = len(line.lstrip('.'))
             nod = length - dot

             if nod == 1:
                 out = out + ' +' + line.lstrip('.')
             elif lastdot < nod:
                 out = out + ' +' + line.lstrip('.')
             else:
                 out = out + ' -' + line.lstrip('.')
             lastdot = nod
             
    print(out)
    outputFile.write(out)
    outputFile.close()
    inputFile.close()

if __name__ == "__main__":
    import sys
    convertFile(sys.argv[1], sys.argv[2])