import hashlib

symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "-", "=", "[",
           "]", "{", "}", "|", ";", ":", ",", ".", "<", ">", "?", "/", "`", "~"]
           
def augment_password(password: str, symbols: list) -> str:
    augmented = ""
    for i in range(len(password)):
        augmented += password[i] + symbols[i%len(symbols)]
    return augmented

def hash_function(data):
    return hashlib.sha256(data.encode('utf-8')).digest()

def generate_key(password: str, target_length: int, bit_length: int = 3):
    large_byte_array = bytearray()
    password = augment_password(password, symbols)

    for i in range(0, len(password), bit_length):
        chunk = password[i:i+bit_length]
        chunk_hash = hash_function(chunk)
        large_byte_array.extend(chunk_hash)
        large_byte_array.extend(chunk_hash[::-1])

    while len(large_byte_array ) < target_length:
        new_byte_array = bytearray()
        for i in range(0, len(large_byte_array), bit_length):
            segment = large_byte_array[i:i+bit_length]
            new_segment = segment.decode('latin-1', errors = 'ignore')
            new_segment_hash = hash_function(new_segment)
            new_byte_array.extend(new_segment_hash)

        large_byte_array.extend(new_byte_array)
        large_byte_array.reverse()

    large_key_string = large_byte_array.decode('utf-8', errors ='ignore')
    large_key_string = large_key_string[:target_length]
    return large_key_string