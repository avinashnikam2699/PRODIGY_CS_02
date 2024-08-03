from PIL import Image

def encrypt_image(input_path, output_path, key):
    # Open an image file
    with new_func(input_path) as img:
        # Convert image to RGB
        img = img.convert("RGB")
        # Get pixel data
        pixels = list(img.getdata())
        # Encrypted pixel data
        encrypted_pixels = []

        for pixel in pixels:
            encrypted_pixel = tuple((value + key) % 256 for value in pixel)
            encrypted_pixels.append(encrypted_pixel)

        # Create a new encrypted image
        encrypted_img = Image.new(img.mode, img.size)
        encrypted_img.putdata(encrypted_pixels)
        encrypted_img.save(output_path)
        print(f"Image successfully encrypted and saved to {output_path}")

def new_func(input_path):
    return Image.open(input_path)

def decrypt_image(input_path, output_path, key):
    # Open an encrypted image file
    with Image.open(input_path) as img:
        # Convert image to RGB
        img = img.convert("RGB")
        # Get pixel data
        pixels = list(img.getdata())
        # Decrypted pixel data
        decrypted_pixels = []

        for pixel in pixels:
            decrypted_pixel = tuple((value - key) % 256 for value in pixel)
            decrypted_pixels.append(decrypted_pixel)

        # Create a new decrypted image
        decrypted_img = Image.new(img.mode, img.size)
        decrypted_img.putdata(decrypted_pixels)
        decrypted_img.save(output_path)
        print(f"Image successfully decrypted and saved to {output_path}")

def main():
    print("Image Encryption and Decryption Tool")
    print("Options:")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    print("3. Exit")

    while True:
        choice = input("Choose an option: ")

        if choice == '1':
            input_path = input("Enter the path to the image to encrypt: ")
            output_path = input("Enter the output path for the encrypted image: ")
            key = int(input("Enter a key (integer) for encryption: "))
            encrypt_image(input_path, output_path, key)
        elif choice == '2':
            input_path = input("Enter the path to the image to decrypt: ")
            output_path = input("Enter the output path for the decrypted image: ")
            key = int(input("Enter the key (integer) used for encryption: "))
            decrypt_image(input_path, output_path, key)
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
