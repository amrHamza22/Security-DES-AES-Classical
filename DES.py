import numpy as np
BinaryToHex = {
  "0": "0000",
  "1": "0001",
  "2": "0010",
  "3": "0011",
  "4": "0100",
  "5": "0101",
  "6": "0110",
  "7": "0111",
  "8": "1000",
  "9": "1001",
  "A": "1010",
  "B": "1011",
  "C": "1100",
  "D": "1101",
  "E": "1110",
  "F": "1111",
}
########################################################################################################################
def Hex_to_binary(Hex):
    out=""
    for i in range(len(Hex)):
        out+=BinaryToHex[Hex[i]]
    return out
def initial_permutation(Input):
    permuatation = np.ones((8, 8))
    index = 56
    for i in range(8):
        index += 2
        if i == 4:
            index = 57
        for j in range(8):
            permuatation[i, j] = index - j * 8
    permuatation = permuatation.flatten()
    permutated = []
    for i in range(64):
        permutated.append(Input[int(permuatation[i] - 1)])
    permutated = np.array(permutated)
    return permutated
def to_48_right_half(permutated):
    permutated1= permutated[32:]
    right_half=[]
    expantion_matrix = [32, 1, 2, 3, 4, 5,
                        4, 5, 6, 7, 8, 9,
                        8, 9, 10, 11, 12,
                        13, 12, 13, 14, 15, 16, 17,
                        16, 17, 18, 19, 20, 21,
                        20, 21, 22, 23, 24, 25,
                        24, 25, 26, 27, 28, 29,
                        28, 29, 30, 31, 32, 1]
    for i in range(48):
        right_half.append(permutated1[int(expantion_matrix[i] - 1)])
    return np.array(right_half).reshape(8,6)
def S_BOX(input,input_index):
    # S boxes
    S = [
        # S1
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],

        # S2
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
        ],

        # S3
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
        ],

        # S4
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
        ],

        # S5
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
        ],

        # S6
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
        ],

        # S7
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
        ],

        # S8
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
        ]
    ]
    S=np.array(S)
    out=S[input_index,int(str(input[0])+str(input[-1]),2),int(str(input[1])+str(input[2])+str(input[3])+str(input[4]),2)]
    out= format(out,"b")
    if len(out)<4:
        out=''.join(['0']*(4-len(out)))+out
    return out
def final_permutation(Input):
    P = [
        16, 7, 20, 21,
        29, 12, 28, 17,
        1, 15, 23, 26,
        5, 18, 31, 10,
        2, 8, 24, 14,
        32, 27, 3, 9,
        19, 13, 30, 6,
        22, 11, 4, 25,
    ]
    out=[]
    for i in range(32):
        out.append(Input[int(P[i] - 1)])
    return np.array(out,dtype='int32').reshape(8, 4)
def generate_Sub_key(key,round_num):
    round_permutation=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    PC_1 = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]
    PC_2= [
        14, 17, 11, 24, 1, 5,
        3, 28, 15, 6, 21, 10,
        23, 19, 12, 4, 26, 8,
        16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32
    ]
    out1 = []
    for i in range(56):
        out1.append(key[int(PC_1[i] - 1)])
    out1=np.array(out1,dtype='int32')
    np.roll(out1,-1*round_permutation[round_num])
    out2= []
    for i in range(48):
        out2.append(out1[int(PC_2[i] - 1)])
    out2=np.array(out2,dtype='int32')
    return out2
def final_inverse_permutation(Input):
    PI_1 = [
        40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25,
    ]
    out = []
    for i in range(64):
        out.append(Input[int(PI_1[i] - 1)])
    return np.array(out, dtype='int32')
while True:
    user_input = []
    print("input:")
    for i in range(3):
        user_input.append(input())
    plain_txt = user_input[1]
    key = user_input[0]
    num_of_encryptions = user_input[2]
    permutated_plain = np.array(list(Hex_to_binary(plain_txt)), dtype='int32')
    Key = np.array(list(Hex_to_binary(key)), dtype='int32')
    for i in range(int(num_of_encryptions)):
        permutated_plain = initial_permutation(permutated_plain)
        for round in range(16):
            Right_half_48 = to_48_right_half(permutated_plain)
            sub_key = generate_Sub_key(Key, round)
            xor_out = np.bitwise_xor(Right_half_48.flatten(), sub_key)
            xor_out = xor_out.reshape((8, 6))
            S_box_out = ''
            for block_num in range(8):
                S_box_out += (S_BOX(xor_out[block_num, :], block_num))
            new_right = np.bitwise_xor(final_permutation(S_box_out).flatten(), permutated_plain[0:32])
            new_left = permutated_plain[32:]
            permutated_plain = np.concatenate((new_left, new_right))
        right = permutated_plain[32:]
        left = permutated_plain[0:32]
        permutated_plain = final_inverse_permutation(np.concatenate((right, left)))
    cipher_txt = ''
    for i in range(64):
        cipher_txt += str((permutated_plain[i]))
    cipher_txt = hex(int(cipher_txt, 2)).upper()
    print(cipher_txt)