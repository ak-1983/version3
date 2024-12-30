import tempfile
from fpdf import FPDF
import qrcode
import csv
from PyPDF2 import PdfMerger
import os

def generate_answer_sheets(csv_path, n, output_combined_pdf):
    """
    Generates answer sheets with QR codes for each UID in the CSV file.
    Each answer sheet will have `n` pages, and all sheets will be combined into a single PDF.
    
    Parameters:
    csv_path (str): Path to the CSV file containing UIDs.
    n (int): Number of pages per answer sheet.
    output_combined_pdf (str): Name of the final combined PDF file.
    """
    uids = []
    try:
        with open(csv_path, mode="r") as file:
            csv_reader = csv.reader(file)
            headers = next(csv_reader)
            for row in csv_reader:
                print((row[0], row[1]))
                uids.append((row[0], row[1]))
    except FileNotFoundError:
        print(f"Error: CSV file '{csv_path}' not found")
        return
    except IndexError:
        print("Error: CSV file doesn't have the expected format. Need at least 2 columns.")
        return

    pdf_files = []
    temp_files = []

    try:
        for name, uid in uids:
            # Create a QR Code for the UID
            qr = qrcode.QRCode(version=1, box_size=7, border=4)
            qr.add_data(uid)
            qr.make(fit=True)
            qr_img = qr.make_image(fill="black", back_color="white")

            with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmpfile:
                qr_img.save(tmpfile.name)
                temp_files.append(tmpfile.name)

                pdf = FPDF()
                for _ in range(n):
                    pdf.add_page()
                    pdf.image(tmpfile.name, x=10, y=12, w=40, h=40)
                    pdf.set_font("Arial", size=12)
                    pdf.cell(200, 10, txt=f"Student: {name}", ln=True)

                with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as pdf_tmpfile:
                    pdf.output(pdf_tmpfile.name)
                    pdf_files.append(pdf_tmpfile.name)
                    temp_files.append(pdf_tmpfile.name)

        merger = PdfMerger()
        for pdf_file in pdf_files:
            merger.append(pdf_file)
        merger.write(output_combined_pdf)
        merger.close()
        print(f"Combined PDF saved as {output_combined_pdf}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        for temp_file in temp_files:
            try:
                os.remove(temp_file)
            except OSError:
                pass

if __name__ == "__main__":
    csv_path = "A_students.csv"
    generate_answer_sheets(csv_path, n=6, output_combined_pdf="final_answer_sheets.pdf")