---

# Event Details PDF Generator

This script reads event data from a CSV file, processes it, and generates a PDF document containing the event details. The PDF includes the event name, category, date, and description for each event in the CSV file.

## Requirements

To run this script, you will need the following Python libraries:

- `pandas` - for reading and processing the CSV file.
- `fpdf` - for generating the PDF document.

You can install the required libraries using pip:

```bash
pip install pandas fpdf
```

## How to Use

1. **Prepare the CSV file**:
   - The script expects a CSV file named `events.csv` containing the following columns:
     - `Event Name` - The name of the event.
     - `category` - The category of the event.
     - `Date` - The date of the event.
     - `Description` - A brief description of the event.

   Example `events.csv`:
   ```csv
   Event Name,category,Date,Description
   "Tech Conference","Technology","2024-05-01","A conference about the latest in tech innovations."
   "Music Festival","Music","2024-06-15","An annual event showcasing top artists in the music industry."
   ```

2. **Run the Script**:
   - Place the `events.csv` file in the same directory as the script.
   - Execute the Python script:
   
   ```bash
   python script.py
   ```

3. **Generated PDF**:
   - The script will generate a PDF file named `event_details.pdf` in the same directory. This PDF will contain the event details formatted as follows:
     - **Event Name**
     - **Event Category**
     - **Event Date**
     - **Event Description**

4. **Customize the CSV File**:
   - You can modify the CSV file to include more events or edit existing ones.
   - Ensure that the column names in the CSV file match the ones specified in the script.

## Script Overview

- The script reads data from `events.csv` using `pandas`.
- It cleans and formats any special characters in the text using the `clean_text` function.
- For each event in the CSV, the script adds the event details to a PDF document using `FPDF`.
- The final PDF file, `event_details.pdf`, is saved in the same directory.

## Customization

You can easily modify the script to change:

- **Font**: The font used for the PDF can be changed by modifying the `pdf.set_font()` lines.
- **Output File Name**: The name of the output PDF can be modified by changing the `output_pdf` variable.
- **CSV Column Names**: If your CSV uses different column names, make sure to adjust the `create_event_pdf` function accordingly.
