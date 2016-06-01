from flask import make_response
from flask import Flask
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle


app = Flask(__name__)
@app.route('/design')


doc = SimpleDocTemplate("table.pdf", pagesize=letter)

data = [
    ['Item', 'Cost', 'Quantity'],
    ['Widget', 3.99, 26],
    ['Whatsit', 2.25, 26],
    ['Hooplah', 10.00, 26],
]

parts = []
table = Table(data, [3 * inch, 1.5 * inch, inch])
table_with_style = Table(data, [3 * inch, 1.5 * inch, inch])

table_with_style.setStyle(TableStyle([
    ('FONT', (0, 0), (-1, -1), 'Helvetica'),
    ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 8),
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
    ('BOX', (0, 0), (-1, 0), 0.25, colors.green),
    ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
]))

parts.append(table)
parts.append(Spacer(1, 0.5 * inch))
parts.append(table_with_style)
doc.build(parts)



if __name__ == '__main__':
    app.run(port=5001)