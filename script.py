import pdfplumber
import pandas as pd

def pdf_to_csv(pdf_file, csv_file):
    # Open the PDF file
    with pdfplumber.open(pdf_file) as pdf:
        data = []
        # Loop through each page in the PDF
        for page in pdf.pages:
            # Extract text from the page
            table = page.extract_table()
            if table:
                data.extend(table)  # Append table data

    # Convert the extracted data into a DataFrame
    df = pd.DataFrame(data[1:], columns=data[0])

    # Save the DataFrame as a CSV file
    df.to_csv(csv_file, index=False)
    print(f"Data successfully saved to {csv_file}")

# Usage example
pdf_to_csv("Thong_tin_ung_ho_qua_TSK_VCB_0011001932418_tu_01.09_den_10.09.2024.pdf", "output.csv")
