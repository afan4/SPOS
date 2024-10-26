#Original Code, Engineered by Afan Shaikh [git: afan4].
try:
    source= open('source.txt', 'r')
    dum = source.readline()
    print("File is read successfully.")
    source.seek(0)
except FileNotFoundError:
    print('\n\n\nsource.txt file not found.\nOpen Macroprocessor Folder in VSC[not the main folder]\n\n\n')
except IOError:
    print('The source file has an IO error')


MDT =[]
MNT =[]

def macroman(line):
    name = line.split()[1] #A concise way to get the 2nd word-> name of macro. index =1. first split and then get 2nd word
    entry = []
    entry.append(line.strip()) #append the macro definition line
    while True:
        line=source.readline().upper()
        if not line:
            print('No MEND found for: ', name)
            return
        if 'MACRO' in line:
            macroman(line)
        elif 'MEND' in line:
            global MDT, MNT
            entry.append(line.strip()) #MEND line appended too
            MNT.append([len(MNT)+1, name, len(MDT)+1]) # Eg. 1 Fibo 50
            MDT = MDT + entry
            return
        else:
            entry.append(line.strip())
        

def pass1():
    global MDT, MNT
    while True:
        line = source.readline().upper()
        if not line:break
        if 'MACRO' in line:
            macroman(line)
    print('\nMNT:')
    for a in MNT:
        print(a)
    print('\n\nMDT:')
    i=0
    for a in MDT:
        i=i+1
        print (i, ' ',a)

pass1()
#pass 2 starts here:
def inserter(sline, name):
    global MDT, MNT
    sline = ''
    for a in MNT:
        if a[1] == name:
            add = a[2] 
            break
    while True:
        if 'MEND' in MDT[add]:
            break
        sline += MDT[add] + '\n'
        add+=1
    return sline

def pass2():
    source.seek(0)
    output = open('output.txt', 'w')
    output.close()
    output = open('output.txt', 'a+')
    while True:
        sline= source.readline().upper()
        if not sline:break
        for a in MNT:
            if a[1] in sline and 'MACRO' not in sline:
                sline=inserter(sline, a[1])  
        d = sline.strip()
        if d not in MDT:
            output.write(sline)
    print('done.')


pass2()
