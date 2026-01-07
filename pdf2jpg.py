# pip install pymupdf pillow

import fitz
from pathlib import Path
import os

SCRIPT_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = SCRIPT_DIR / "output"


def pdf_to_jpg(output_dir="output_images", zoom=2):
    pdf_name = input("Enter PDF name: ")
    pdf_path = SCRIPT_DIR / pdf_name

    OUTPUT_DIR.mkdir(exist_ok=True)

    doc = fitz.open(pdf_path)

    for i, page in enumerate(doc, start=1):
        pix = page.get_pixmap(matrix=fitz.Matrix(3, 3))
        pix.save(OUTPUT_DIR / f"{pdf_name}_page_{i}.jpg")
        print(f"Saved page {i}")

    doc.close()
    print("✅ Done")

if __name__ == "__main__":
    pdf_to_jpg()
