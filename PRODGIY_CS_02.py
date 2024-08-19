from PIL import Image
import numpy as np
import random

def load_image(path):
    image = Image.open(path)
    return np.array(image)

def save_image(image_array, path):
    image = Image.fromarray(image_array)
    image.save(path)

def encrypt_decrypt_image(image, key):
    key = int(key)
    # XOR each color channel (R, G, B) with the key independently
    encrypted_image = image ^ key
    return encrypted_image

def shuffle_pixels(image):
    original_shape = image.shape
    flattened_image = image.flatten()
    indices = np.arange(flattened_image.size)
    np.random.shuffle(indices)
    
    shuffled_image = flattened_image[indices].reshape(original_shape)
    return shuffled_image, indices

def unshuffle_pixels(image, indices):
    original_shape = image.shape
    flattened_image = image.flatten()
    unshuffled_image = np.zeros_like(flattened_image)
    unshuffled_image[indices] = flattened_image
    return unshuffled_image.reshape(original_shape)

def main():
    image_path = 'encrypted_image1.png'
    image = load_image(image_path)
    
    key = 123  # Use any integer as the key
    
    # Shuffle the image pixels
    shuffled_image, indices = shuffle_pixels(image)
    
    # Encrypt the shuffled image
    encrypted_image = encrypt_decrypt_image(shuffled_image, key)
    save_image(encrypted_image, 'encrypted_image.png')
    
    # Decrypt the image (same process as encryption)
    decrypted_image = encrypt_decrypt_image(encrypted_image, key)
    
    # Unshuffle the pixels to restore the original image
    restored_image = unshuffle_pixels(decrypted_image, indices)
    save_image(restored_image, 'decrypted_image.png')
    
    print("Encryption, Decryption, and Shuffling/Unshuffling completed successfully!")

if __name__ == "__main__":
    main()

