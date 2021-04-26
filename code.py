def codenum(string, seed):
    conv = { 'a': 1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n': 14,
             'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,
             'y':25,'z':26, '1':27, '2':28, '3':29, '4':30, '5':31, '6':32, '7':33,
             '8':34, '9':35, '0':36}
    convback = dict([(value, key) for key, value in conv.items()])
   
    code = [None]*len(string)
    for i in range(len(string)):
        code[i] = conv[string[i]]
    newcode = [None]*len(string)
    for i in range(len(code)):
        newcode[i] = (code[i]+seed)%len(conv)
    for i in range(len(code)):
        newcode[i] = convback[newcode[i]]
    return code, newcode


    
def code(string, seed):
    conv = { 'a': 1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n': 14,
             'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,
             'y':25,'z':0}
    convback = dict([(value, key) for key, value in conv.items()])
   
    code = [None]*len(string)
    for i in range(len(string)):
        code[i] = conv[string[i]]
    newcode = [None]*len(string)
    for i in range(len(code)):
        newcode[i] = (code[i]+seed)%(len(conv))
   
    final = ''
    for i in range(len(code)):
        
       final = final+convback[newcode[i]]
    return  final, " ", seed
def polyalphadecode(string, key):
    #initializes converion of letters to numbers and vice versa
    conv = { 'a': 0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n': 13,
             'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,
             'y':24,'z':25}
    convback = dict([(value, key) for key, value in conv.items()])
    lenkey = len(key)

    #creates empty arrays to hold numbers after strings are converted
    numkey = [None]*len(key)
    code = [None]*len(string)
    #converts letters to numbers and stores them in the array created above
    for i in range(len(string)):
        code[i] = conv[string[i]]
    for i in range(len(key)):
        numkey[i] = conv[key[i]]

        
    newcode = [None]*len(string)
    
    for i in range(len(code)):
#creates a variable to represent the posistion in the key that is to be used
        b = i%lenkey
        
        newcode[i] = (code[i]-numkey[b])%(len(conv))
       
    final = ''
    for i in range(len(code)):
        
       final = final+convback[newcode[i]]
    return final

def Polysqdecode(string):
    square = [['a','b','c','d','e'],['f','g','h','i','j'],['k','l','m','n','o'],['p','q','r','s','t'],['u','v','w','x','y']]
    cords = [None]*(len(string)//2)
    for i in range(len(cords)):
        cords[i] = [0,0]
    n = 2
    string = [string[i:i+n] for i in range(0, len(string), n)]
    for i in range(len(cords)):
        cords[i][0] = int(string[i][0])
        cords[i][1] = int(string[i][1])
    answer = ''
   
    for i in range(len(cords)):
        answer= answer + square[cords[i][1]-1][cords[i][0]-1]
       

    return answer
def Polysqdecode2(string):
    square = [['f','g','h','i','j', 'k'],['e','x','y','z','0', 'l'],['d','w','7','8','1', 'm'],['c','v','6','9','2','n'],['b','u','5','4','3','o']
              ['a', 't', 's', 'r', 'q', 'p'] ]
    cords = [None]*(len(string)//2)
    for i in range(len(cords)):
        cords[i] = [0,0]
    n = 2
    string = [string[i:i+n] for i in range(0, len(string), n)]
    for i in range(len(cords)):
        cords[i][0] = int(string[i][0])
        cords[i][1] = int(string[i][1])
    answer = ''
   
    for i in range(len(cords)):
        answer= answer + square[cords[i][1]-1][cords[i][0]-1]
       

    return answer	
def getotp(string):
    string.replace(" ", "")
    code = ['0']*len(string)
    for i in range(len(string)):
        if (string[i] == 'a') or (string[i] == 'e') or (string[i] == 'i') or (string[i] == 'o') or (string[i] == 'y') or (string[i] == 'u'):
            code[i] = '1'
    return code
def reverXOR(encrypted, pad):
    temp = ['0']*len(encrypted)
    final = ['0']*len(encrypted)
    for i in range(len(encrypted)):
        temp[i] = encrypted[i]
    print(temp)    
    for i in range(len(encrypted)):
        if temp[i] != pad[i]:
            final[i] = '1'
    return final
    
