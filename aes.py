
from key_expansion import keys_expansion
# AES-128 S-box

S_BOX = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5,
    0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,

    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0,
    0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,

    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc,
    0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,

    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a,
    0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,

    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0,
    0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,

    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b,
    0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,

    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85,
    0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,

    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5,
    0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,

    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17,
    0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,

    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88,
    0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,

    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c,
    0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,

    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9,
    0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,

    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6,
    0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,

    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e,
    0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,

    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94,
    0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,

    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68,
    0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

def sub_bytes(state):
    for row in range(4):
        for col in range(4):
            state[row][col]=S_BOX[state[row][col]]
    return state
def shift_rows(state):
    for row in range(4):
        state[row]=state[row][row:]+ state[row][:row]
    return state



def xtime(byte):
    result= byte<<1
    if byte & 0x80:
        result^=0x1b
    return result & 0xff
def mul2(byte):
    return xtime(byte)
def mul3(byte):
    return xtime(byte)^byte
def mix_columns(state):
    for col in range(4):
        a=state[0][col]
        b=state[1][col]
        c=state[2][col]
        d=state[3][col]
        
        state[0][col] = (mul2(a) ^mul3(b) ^c ^d )

        state[1][col] = (a ^mul2(b) ^mul3(c)^d)

        state[2][col] = (a ^b ^mul2(c) ^mul3(d))

        state[3][col] = (mul3(a) ^b ^c ^mul2(d))

    return state

def add_round_key(state,key):
    for row in range(4):
        for col in range(4):
            state[row][col]=state[row][col]^key[row][col]
    return state

def words_to_matrix(words):

    return [
        [words[0][0], words[1][0], words[2][0], words[3][0]],
        [words[0][1], words[1][1], words[2][1], words[3][1]],
        [words[0][2], words[1][2], words[2][2], words[3][2]],
        [words[0][3], words[1][3], words[2][3], words[3][3]]
    ]

def get_round_keys(key):
    words=keys_expansion(key)
    round_key=[]
    for i in range(0,44,4):
        new_words=words_to_matrix(words[i:i+4])
        round_key.append(new_words)
    return round_key

def bytes_to_state(block):

    return [
        [block[0],  block[4],  block[8],  block[12]],
        [block[1],  block[5],  block[9],  block[13]],
        [block[2],  block[6],  block[10], block[14]],
        [block[3],  block[7],  block[11], block[15]]
    ]
def state_to_bytes(state):
    block=[]
    for col in range(4):
        for row in range(4):
            block.append(state[row][col])
    return block
def aes_encrypt_block(plaintext,key):
    if len(plaintext)!=16:
        raise ValueError("Plaintext block must be exactly 16 bytes")
    if len(key)!=16:
            raise ValueError("Key block must be exactly 16 bytes")
    round_keys=get_round_keys(key)
    state=bytes_to_state(plaintext)
    #initial round key addition
    state=add_round_key(state,round_keys[0])
    for round_number in range(1, 10):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = add_round_key(state,round_keys[round_number])

    # Final round (Round 10)
    state = sub_bytes(state)
    state = shift_rows(state)
    state = add_round_key(state,round_keys[10])
    return state_to_bytes(state)
def inv_sub_bytes(state):
    for row in range(4):
        for col in range(4):
            state[row][col] = S_BOX.index(state[row][col])

    return state
def inv_shift_rows(state):
    for row in range(4):
        state[row]=state[row][-row:]+state[row][:-row]
    return state

def gmul(a, b):
  
    result = 0
    while b!=0:
        if b & 1:
            result ^= a
        high_bit = a & 0x80
        a = (a << 1) & 0xff
        if high_bit:
            a ^= 0x1b
        b >>= 1
    return result

def inv_mix_columns(state):

    for col in range(4):
        a = state[0][col]
        b = state[1][col]
        c = state[2][col]
        d = state[3][col]
        state[0][col] = (gmul(a, 0x0e) ^gmul(b, 0x0b) ^gmul(c, 0x0d) ^gmul(d, 0x09))
        state[1][col] = (gmul(a, 0x09) ^gmul(b, 0x0e) ^gmul(c, 0x0b) ^gmul(d, 0x0d))
        state[2][col] = (gmul(a, 0x0d) ^gmul(b, 0x09) ^gmul(c, 0x0e) ^gmul(d, 0x0b))
        state[3][col] = (gmul(a, 0x0b) ^gmul(b, 0x0d) ^gmul(c, 0x09) ^gmul(d, 0x0e))
    return state

def aes_decrypt_block(ciphertext,key):
    if len(ciphertext)!=16:
        raise ValueError("Ciphertext block must be exactly 16 bytes")
    if len(key)!=16:
        raise ValueError("AES-128 key must be exactly 16 bytes")
    round_keys=get_round_keys(key)
    state=bytes_to_state(ciphertext)
    state=add_round_key(state,round_keys[10])
    state = inv_shift_rows(state)
    state = inv_sub_bytes(state)
    for round_number in range(9, 0, -1):
        state = add_round_key(state,round_keys[round_number])
        state = inv_mix_columns(state)
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)
    state = add_round_key(state, round_keys[0])
    return state_to_bytes(state)


