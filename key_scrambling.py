def binary_transformation(large_key_string: str) -> list:
    segments_list = []
    binary_string = ""
    for i in large_key_string:
      b_i = format(ord(i), '08b')
      binary_string += b_i

    for i in range(0, len(binary_string), 8):
      segment = binary_string[i:i+8]
      segments_list.append(segment)
      reversed_segment = segment[::-1]
      segments_list.append(reversed_segment)
      mutated_segment = segment[4:8:1] + segment[0:4:1]
      segments_list.append(mutated_segment)
    return segments_list

def cross_catenation(segments_list: list) -> list:
    binary_string = "".join(segments_list)
    first_half, second_half = binary_string[:len(binary_string)//2],binary_string[len(binary_string)//2:]
    cross_catenated_string = second_half + first_half
    l = len(cross_catenated_string)
    segments_list = []

    for i in range(0, l, 8):
        segments_list.append(cross_catenated_string[i:i+8])

    return segments_list

def scramble(large_key_string: str) -> list :
    segments_list = binary_transformation(large_key_string)
    segments_list = cross_catenation(segments_list)
    return segments_list

