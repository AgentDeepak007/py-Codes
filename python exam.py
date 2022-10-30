def readData(inputfile, outputfile, character):
    try:
        inf = open(inputfile, 'r')
        outf = open(outputfile, 'w')

        i = 0
        char_count = 0

        for line in inf:
            if i%2 == 0:
                outf.write(line)
          
            i += 1
            char_count += line.count(character)
  
        inf.close()
        outf.close()

        return char_count
    
    except FileNotFoundError:
        print(f'{inputfile} not Found')
        return 0


input_file = input('Input File name : ')
output_file = input('Output File name : ')
char = input('Character : ')
print(readData(input_file, output_file, char))
