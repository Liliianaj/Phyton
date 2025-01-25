import time
import multiprocessing
from PIL import Image, ImageFilter

def process_image_part(image_part):
    """Procesowanie części obrazu."""
    for _ in range(20):  # Dodanie pętli dla cięższego przetwarzania
        image_part = image_part.filter(ImageFilter.GaussianBlur(5))
    return image_part

def split_image(image, num_parts):
    """Dzielenie obrazu na części."""
    width, height = image.size
    parts = []
    rows_per_part = height // num_parts

    for i in range(num_parts):
        top = i * rows_per_part
        bottom = (i + 1) * rows_per_part if i < num_parts - 1 else height
        parts.append(image.crop((0, top, width, bottom)))
    return parts

def merge_image_parts(parts, image_size):
    """Łączenie przetworzonych części obrazu."""
    width, height = image_size
    new_image = Image.new("RGB", (width, height))
    y_offset = 0

    for part in parts:
        new_image.paste(part, (0, y_offset))
        y_offset += part.size[1]
    return new_image

def main(image_path, num_parts):
    image = Image.open(image_path)
    width, height = image.size

    # Podział obrazu na części
    parts = split_image(image, num_parts)

    # Przetwarzanie równoległe
    start_time = time.time()
    with multiprocessing.Pool(processes=num_parts) as pool:
        processed_parts = pool.map(process_image_part, parts)

    # Łączenie części obrazu
    processed_image = merge_image_parts(processed_parts, (width, height))
    total_time = time.time() - start_time

    # Zapis i wyświetlanie obrazu
    processed_image.save(f'processed_image_{num_parts}.png')

    # Zapisz czas do pliku
    with open('times_data.txt', 'a') as f:
        f.write(f"{num_parts},{total_time:.2f}\n")
    print(f"\nCzas przetwarzania całego obrazu z {num_parts} rdzeniami: {total_time:.2f} sekund")

def test(image_path):
    # Czyszczenie pliku wynikowego przed rozpoczęciem testów
    with open('times_data.txt', 'w') as f:
        f.write("num_parts,time\n")

    for num_parts in [1, 2, 3, 4]:
        print(f"\nTest dla {num_parts} rdzeni:")
        main(image_path, num_parts)

if __name__ == "__main__":
    test("zdj.png")
