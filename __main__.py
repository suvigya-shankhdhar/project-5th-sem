import large_key_generation
import key_scrambling
import dna_operations
import image_decryption
import image_encryption

from PIL import Image
import numpy as np
from pathlib import Path

password = "secure_password"

test_folder = Path('test images')

cipher_img_folder = Path('processed images')
cipher_img_folder.mkdir(exist_ok = True)

original_img_folder = Path('original images')
original_img_folder.mkdir(exist_ok=True)

for file_path in test_folder.iterdir():
    try:
        img = Image.open(file_path)
        img = img.convert('RGB')
        img_matrix = np.asarray(img)
        height, width, channels = img_matrix.shape       

        total_pixels = height * width * channels
        target_length = (total_pixels // 3 ) + 1000

        large_key_string = large_key_generation.generate_key(password, target_length, 3)
        segments_list = key_scrambling.scramble(large_key_string)

        cipher_img_matrix = image_encryption.encrypt_image(segments_list, img_matrix)
        cipher_img = Image.fromarray(cipher_img_matrix)

        file_name = file_path.name
        new_file_name = f"encrypted_{file_name}"
        file_path = cipher_img_folder / new_file_name
        
        difference = np.sum(img_matrix != cipher_img)
        encryption_percentage = (difference /(height*width*channels)) * 100

        print(f"\n\nPixels changed: {difference}/{height*width*channels} ({encryption_percentage:.2f}%)")

        cipher_img.save(file_path)
        # cipher_img.show()

    except IOError:
        print("Error")

for file_path in cipher_img_folder.iterdir():
    try:
        img = Image.open(file_path)
        img = img.convert('RGB')
        img_matrix = np.asarray(img)
        height, width, channels = img_matrix.shape       

        total_pixels = height * width * channels
        target_length = (total_pixels // 3 ) + 1000

        large_key_string = large_key_generation.generate_key(password, target_length, 3)
        segments_list = key_scrambling.scramble(large_key_string)

        original_img_matrix = image_decryption.decrypt_image(segments_list, img_matrix)
        original_img = Image.fromarray(original_img_matrix)

        file_name = file_path.name.replace('encrypted_', '')
        new_file_name = f"original_{file_name}"
        
        file_path = original_img_folder/new_file_name
      
        original_img.save(file_path)
        # original_img.show()

    except IOError:
        print("Error")

        