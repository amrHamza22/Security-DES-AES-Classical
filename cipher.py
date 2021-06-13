import os
import numpy as np
def Caesar(plain_txt,key):
    alphapet = []
    for ch in range(97, 123):
        alphapet.append(chr(ch))
    Length=len(plain_txt)
    cipher_txt=''
    for i in range(Length - 1):
        cipher_txt += alphapet[(alphapet.index(plain_txt[i]) + key) % 26]
    return cipher_txt
def PlayFair(plain_txt,key):
    key=key.replace('j','i')
    plain_txt=plain_txt.replace('j','i')
    key=''.join(sorted(set(key), key=key.index))
    alphapet = []
    for ch in range(97, 123):
        if chr(ch) not in key and chr(ch) !='j':
            alphapet.append(chr(ch))
    matrix=np.empty((5,5),dtype=object)
    for i in range(5):
        for j in range(5):
            if not len(key) ==0:
                matrix[i, j] = key[0]
                key = key[1:]
            else:
                matrix[i, j] = alphapet[0]
                alphapet = alphapet[1:]
    for i in range(0,len(plain_txt)-1,2):
        if plain_txt[i]==plain_txt[i+1]:
            plain_txt=plain_txt[:i+1]+'x'+plain_txt[i+1:]
    if not len(plain_txt) % 2 == 0:
        plain_txt = plain_txt + 'x'
    cipher_txt=''
    while len(plain_txt)!=0:
        row2,column2 = np.where(matrix == plain_txt[1])
        row1,column1 = np.where(matrix == plain_txt[0])
        plain_txt = plain_txt[2:]
        if row1 == row2 :
            if column1==4:
                row1=(row1) % 5
            cipher_txt+=matrix[row1,(column1+1)% 5]
            if column2==4:
                row2 = (row2 ) % 5
            cipher_txt+=matrix[row2,( column2 + 1) % 5]
        elif column1==column2:
            if row1==4:
                column1=(column1)%5
            cipher_txt+=matrix[(row1+1)%5,column1]
            if row2==4:
                column2=(column2)%5
            cipher_txt+=matrix[(row2+1)%5,column2]
        else:
            cipher_txt+= matrix[row1,column2] + matrix[row2, column1]
    return cipher_txt
def Hill(plain_txt,key):
    plain_txt=plain_txt.lower()
    key=np.array(key)
    alphapet = []
    cipher_txt=''
    for ch in range(97, 123):
        alphapet.append(chr(ch))
    if not len(plain_txt) % key.shape[0] == 0:
        plain_txt = plain_txt + 'x'
    while len(plain_txt) !=0:
        plain_matrix=np.ones((1,key.shape[0]))
        for i in range(key.shape[0]):
            print(plain_txt)
            plain_matrix[0, i] = alphapet.index(plain_txt[i])
        cipher_matrix=np.dot(key,plain_matrix.T) % 26
        cipher_matrix=cipher_matrix.T
        print(cipher_matrix)
        plain_txt=plain_txt[key.shape[0]:]
        for i in range(key.shape[0]):
            cipher_txt += alphapet[int(cipher_matrix[0, i])]
    return cipher_txt
def Vigenere(plain_txt,key,repeat):
    alphapet = []
    if repeat==True:
        for i in range(len(plain_txt)-len(key)):
            key+= key[i % len(key) ]
    else:
        for i in range(len(plain_txt)-len(key)):
            key+=plain_txt[i %len(plain_txt)]
    for ch in range(97, 123):
        alphapet.append(chr(ch))
    Length = len(plain_txt)
    cipher_txt = ''
    for i in range(Length):
        cipher_txt += alphapet[(alphapet.index(plain_txt[i]) + alphapet.index(key[i])) % 26]
    return cipher_txt
def Vernam(plain_txt,key):
    plain_txt=plain_txt.lower()
    key=key.lower()
    alphapet = []
    for ch in range(97, 123):
        alphapet.append(chr(ch))
    Length = len(plain_txt)
    cipher_txt = ''
    for i in range(Length):
        cipher_txt += alphapet[(alphapet.index(plain_txt[i]) + alphapet.index(key[i])) % 26]
    return cipher_txt
#print(Hill('dimtnywk',[[2,4,12],[9,1,6],[7,5,3]]))
#print(Vigenere('dimtnywk','pie',True))
#PlayFair('hidethegoldinthetreestump','rats')
#with open('plain.txt','r') as file:
 #   with open('caesar_cipher3.txt','w') as f:
  #      ...
   # with open('caesar_cipher6.txt','w') as f:
    #    ...
    #with open('caesar_cipher12.txt','w') as f:
     #   ...
    #for line in file:
     #   with open('caesar_cipher3.txt','a') as f:
      #      f.write(Caesar(line,3))
       # with open('caesar_cipher3.txt', 'a') as f:
        #    f.write(Caesar(line, 6))
       # with open('caesar_cipher3.txt','a') as f:
        #    f.write(Caesar(line,12))

#with open('plain.txt','r') as file:
 #   with open('PlayFair_rats.txt','w') as f:
  #      ...
   # with open('PlayFair_archange.txt','w') as f:
    #    ...
   # for line in file:
    #    with open('PlayFair_rats.txt','a') as f:
     #       f.write(PlayFair(line[:-1],'rartss')[0])
      #      f.write('\n')
       # with open('PlayFair_archange.txt', 'a') as f:
        #    f.write(PlayFair(line[:-1], 'archange')[0])
         #   f.write('\n')
