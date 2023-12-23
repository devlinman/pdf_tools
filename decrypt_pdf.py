import sys
import os
import fitz

def decrypt_pdf(input_path, output_path, password):
    # Check if the input PDF file exists
    if not os.path.exists(input_path):
        print(f"Error: The specified input PDF file '{input_path}' does not exist.")
        sys.exit(1)

    # Open the PDF file
    pdf_document = fitz.open(input_path)

    # Check if the PDF is encrypted
    if pdf_document.needs_pass:
        # Try to authenticate with the provided password
        if pdf_document.authenticate(password):
            # Create a new PDF writer
            pdf_writer = fitz.open()

            # Add all the pages to the new PDF
            for page_num in range(pdf_document.page_count):
                pdf_writer.insert_pdf(pdf_document, from_page=page_num, to_page=page_num)

            # Save the decrypted PDF to the output file
            pdf_writer.save(output_path)
            pdf_writer.close()

            print("PDF decrypted successfully.")
        else:
            print("Error: Incorrect password. Unable to decrypt.")
            sys.exit(1)
    else:
        print("Error: The PDF is not encrypted or already decrypted.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 3 or len(sys.argv) > 4   :
        print("Usage: \n$ python", sys.argv[0], " [input path] [output path] [password]\n")
        sys.exit(1)

    input_pdf_path = sys.argv[1]
    password = sys.argv[2]
    if len(sys.argv) != 4:
        output_pdf_path = sys.argv[1] + "_decrypted.pdf"

        original_path = sys.argv[1]
        directory, filename = os.path.split(original_path)
        name, extension = os.path.splitext(filename)

        new_filename = f"{name}_decrypted{extension}"
        output_pdf_path = os.path.join(directory, new_filename)

    else:
        output_pdf_path = sys.argv[3]
    decrypt_pdf(input_pdf_path, output_pdf_path, password)
