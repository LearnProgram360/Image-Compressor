from PIL import Image

def compress_image(input_path, output_path, quality):
    """
    Compresses an image using the JPEG algorithm with the given quality setting.
    Saves the compressed image to the output path.
    """
    with Image.open(input_path) as img:
        img.save(output_path, "JPEG", optimize=True, quality=quality)

# Example usage: compress an image with 50% quality
compress_image("C:\\Users\\learn\Desktop\\IMG20220619174131.jpg", "C:\\Users\\learn\\Desktop\\Compress2_IMG20220619174131.jpg", 20)
