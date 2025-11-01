from dna_operations import dna_decode, dna_encode, dna_xor
import numpy as np

def encrypt_image(segments_list: list, img_matrix: np.ndarray) -> np.ndarray:
    processed_img = img_matrix.copy()
    height, width, channels = img_matrix.shape
    index = 0
    for i in range(height):
        for j in range(width):
            for k in range(channels):
                if index < len(segments_list):
                    rule = (index % 8) + 1
                    key_segment = segments_list[index]
                    original_value = processed_img[i, j, k]
                    original_bin = format(original_value, '08b')

                    key_dna = dna_encode(key_segment, rule)
                    original_dna = dna_encode(original_bin, rule)
                    xored_dna = dna_xor(key_dna, original_dna)
                    decoded_bin = dna_decode(xored_dna, rule)

                    cipher_value = int(decoded_bin, 2)
                    processed_img[i, j, k] = cipher_value
                    index += 1

    processed_img = np.clip(processed_img, 0, 255).astype(np.uint8)
    return processed_img