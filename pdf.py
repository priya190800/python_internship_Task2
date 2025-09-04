import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

# Step 1: Read data from CSV file
file_path = "D:/vscode/weather_dashboard_project/output/forecast1.csv"  # Replace with your file
df = pd.read_csv(file_path)

# Step 2: Analyze data (example: summary statistics)
summary = df.describe(include="all").transpose()

# Step 3: Generate PDF report
pdf_file = "report_of_forecast1.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=A4)
styles = getSampleStyleSheet()
elements = []

# Title
elements.append(Paragraph("📊 Data Analysis Report", styles['Title']))
elements.append(Spacer(1, 20))

# Add dataset info
elements.append(Paragraph(f"Total Rows: {df.shape[0]}", styles['Normal']))
elements.append(Paragraph(f"Total Columns: {df.shape[1]}", styles['Normal']))
elements.append(Spacer(1, 20))

# Add table of summary statistics
table_data = [summary.reset_index().columns.tolist()] + summary.reset_index().values.tolist()
table = Table(table_data)

# Style the table
table.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.grey),
    ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
    ('ALIGN',(0,0),(-1,-1),'CENTER'),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0,0), (-1,0), 12),
    ('GRID', (0,0), (-1,-1), 0.5, colors.black),
]))
elements.append(table)

# Build PDF
doc.build(elements)

print("✅ PDF report generated:", pdf_file)
