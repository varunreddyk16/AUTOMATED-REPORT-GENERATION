import csv
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle

# Function to read data from a CSV file
def read_csv(file_path):
    data = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

# Function to generate a PDF report
def generate_pdf_report(data, output_file):
    doc = SimpleDocTemplate(output_file, pagesize=letter)
    
    content = []
    
    # title
    styles = getSampleStyleSheet()
    title = Paragraph("Employee Data Report", styles['Title'])
    content.append(title)
    
    # table data
    table_data = [["Name", "Age", "City", "Salary"]]  # Header row
    for row in data:
        table_data.append([row['Name'], row['Age'], row['City'], row['Salary']])
    
    # TO Create a table
    table = Table(table_data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'), 
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), 
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12), 
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige), 
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]))
    content.append(table)    
    doc.build(content)
    print(f"PDF report generated: {output_file}")

# Main function
def main():
    # File paths
    input_file = 'data.csv'  
    output_file = 'employee_report.pdf' 
    
    # Read data from the CSV file
    data = read_csv(r"C:\Users\sowmya\OneDrive\Documents\CODE_TECH\task_2_folder\data(2-1).csv")
    
    # Generate PDF report
    generate_pdf_report(data, output_file)

if __name__ == "__main__":
    main()
