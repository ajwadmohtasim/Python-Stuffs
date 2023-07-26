import os
import fitz
import io
import sys
from PIL import Image

if len(sys.argv) < 3:
    print("Please provide a file path and the desired page(s) as command-line arguments.")
    sys.exit(1)

# output directory
output_dir = "extracted_images"
output_format = "png"

# Creating output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

file_path = sys.argv[1]
page_arg = sys.argv[2]
pdf_file = fitz.open(file_path)

#Method
if page_arg.lower() == "all":
    page_numbers = range(len(pdf_file))
else:
    try:
        page_num = int(page_arg) - 1
        page_numbers = [page_num]
    except ValueError:
        print("Invalid Method. Try {num} or {all}")
        sys.exit(1)

#Extraction
for page_index in page_numbers:
    page = pdf_file[page_index]
    image_list = page.get_images(full=True)
    print("Image Found") if image_list else print("Image not found")
    for image_index, img in enumerate(image_list, start=1):
        xref = img[0]
        base_image = pdf_file.extract_image(xref)
        image_bytes = base_image["image"]
        image_ext = base_image["ext"]
        image = Image.open(io.BytesIO(image_bytes))
        image.save(
            open(os.path.join(output_dir, f"image_page{page_index + 1}.{output_format}"), "wb"),
            format=output_format.upper()
        )
