from PIL import Image
import os

def compress_image(input_path, output_path, quality):
    """Compress an image file with given quality level"""
    with Image.open(input_path) as img:
        # Save the compressed image to the output path
        img.save(output_path, optimize=True, quality=quality)

if __name__ == '__main__':
    # Example usage:
    input_path = 'example.jpg'
    output_path = 'compressed_example.jpg'
    quality = 50  # Set the quality level between 0 (lowest) and 100 (highest)

    compress_image(input_path, output_path, quality)

    # Get the original and compressed file sizes
    original_size = os.path.getsize(input_path)
    compressed_size = os.path.getsize(output_path)

    print(f'Original size: {original_size} bytes')
    print(f'Compressed size: {compressed_size} bytes')
