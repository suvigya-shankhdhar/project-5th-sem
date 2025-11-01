from dna_operations import dna_decode, dna_encode, dna_xor
import numpy as np

def decrypt_image(cipher_img: np.ndarray , segments_list: list) -> np.ndarray:
    processed_img = cipher_img.copy()
    height, width ,channels = cipher_img.shape
    index = 0
    for i in range(height):
      for j in range(width):
        for k in range(channels):
          if index < len(segments_list):
            rule = (index % 8) + 1
            key_segment = segments_list[index]
            cipher_value = processed_img[i, j, k]
            cipher_binary = format(cipher_value , '08b')

            key_dna = dna_encode(key_segment, rule)
            cipher_dna = dna_encode(cipher_binary, rule)
            xored_dna = dna_xorR(key_dna, cipher_dna)
            original_binary = dna_decode(xored_dna, rule)

            original_value = int(original_binary, 2)
            processed_img[i, j, k] = original_value
            index += 1

    processed_img = np.clip(processed_img, 0, 255).astype(np.uint8)
    return processed_img