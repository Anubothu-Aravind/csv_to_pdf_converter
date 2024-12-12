import pandas as pd
from fpdf import FPDF

csv_file = "events.csv"
df = pd.read_csv(csv_file)

df.columns = df.columns.str.strip()

print("Columns in the CSV file:", df.columns)

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

pdf.set_font("Times", size=12)

def clean_text(text):
    if isinstance(text, str):
        text = text.replace('’', "'").replace('“', '"').replace('”', '"').replace('—', '-').replace('–', '-')
    return text

def create_event_pdf(event_name, event_category, event_date, event_description):
    event_name = clean_text(event_name)
    event_category = clean_text(event_category)
    event_date = clean_text(event_date)
    event_description = clean_text(event_description)

    pdf.set_font("Times", 'B', 12)
    pdf.cell(200, 10, txt=f"Event Name: ", ln=True, align='L')
    pdf.set_font("Times", '', 12)
    pdf.cell(200, 10, txt=event_name, ln=True, align='L')

    pdf.set_font("Times", 'B', 12)
    pdf.cell(200, 10, txt=f"Event Category: ", ln=True, align='L')
    pdf.set_font("Times", '', 12)
    pdf.cell(200, 10, txt=event_category, ln=True, align='L')

    pdf.set_font("Times", 'B', 12)
    pdf.cell(200, 10, txt=f"Event Date: ", ln=True, align='L')
    pdf.set_font("Times", '', 12)
    pdf.cell(200, 10, txt=event_date, ln=True, align='L')

    pdf.set_font("Times", 'B', 12)
    pdf.cell(200, 10, txt="Event Description: ", ln=True, align='L')
    pdf.set_font("Times", '', 12)
    pdf.multi_cell(0, 10, txt=event_description + "\n\n")

for index, row in df.iterrows():
    create_event_pdf(row["Event Name"], row["category"], row["Date"], row["Description"])

output_pdf = "event_details.pdf"
pdf.output(output_pdf)

print(f"PDF generated successfully: {output_pdf}")