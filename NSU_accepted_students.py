from PyPDF2 import PdfReader
import re

reader = PdfReader('NSU.pdf')
cse_accepted = 0
all_sub_accepted = 0
cse_choice = 0
range_count = 0

for page_number in range(0, len(reader.pages)):
    page = reader.pages[page_number]
    text = page.extract_text()  # Extracts full page
    cse_accepted += text.count("CSE ACCEPTED")
    cse_choice += text.count("CSE")
    all_line = text.split("\n")
    for line in all_line:
        if line.count("ACCEPTED") == 4:
            all_sub_accepted += 1
        numbers = re.findall(r'\d+', line)
        numbers_in_range = [int(num) for num in numbers if 1000 <= int(num) <= 9600]
        if len(numbers_in_range) == len(numbers):
            range_count += 1

print(
    f"Number of CSE accepted students: {cse_accepted} out of {cse_choice} a percentage of {round((cse_accepted / cse_choice) * 100, 2)}")
print(f"Number of ALL subject accepted students: {all_sub_accepted} out of {range_count}")
