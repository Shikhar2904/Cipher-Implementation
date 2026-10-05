
BLOCK_SIZE = 16
def pad(data):
    padding_length = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    padding_byte = padding_length
    return data + [padding_byte] * padding_length


def unpad(data):
    if len(data) == 0:
        raise ValueError("Cannot unpad empty data")
    padding_length = data[-1]
    if padding_length < 1 or padding_length > BLOCK_SIZE:
        raise ValueError("Invalid padding")
    if data[-padding_length:] != [padding_length] * padding_length:
        raise ValueError("Invalid padding")
    return data[:-padding_length]



