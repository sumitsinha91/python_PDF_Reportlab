from flask import make_response
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.graphics.barcode import code128
from reportlab.lib.colors import pink, black, red, blue, green, brown, HexColor
from flask import Flask


app = Flask(__name__)


@app.route('/pdf')
def pdf():
    import cStringIO
    output = cStringIO.StringIO()

    p = canvas.Canvas(output)
    p.setPageSize(landscape(letter))
    logo = ImageReader('http://www.endeavor.org/content/uploads/2015/07/Fetchr-180x180.png')
    p.drawImage(logo, 10, 480, mask='auto')
    barcode = code128.Code128("123456789",barHeight=.4*inch,barWidth = 1.5)
    barcode.drawOn(p, 200*mm, 200*mm)
    p.setFont("Courier-BoldOblique", 12)
    p.drawString(200, 582, 'AIR WAYBILL')
    p.setFont("Courier", 8)
    p.drawString(283, 582.10, 'Track your shipment online on')
    p.setFont("Courier", 10)
    p.drawString(428, 582.10, 'FETCHR.US')
    p.grid([0.100*inch, 5.40 * inch, 10.90 * inch], [4.05 * inch, 4.30 * inch, 4.75 * inch, 5.0 * inch, 5.25 * inch, 5.50 * inch, 5.75 * inch, 6.50 * inch, 6.75 * inch, 7.0 * inch])
    p.setStrokeColor(black)
    p.drawString(2.5 * inch, 3.5 * inch, "")
    p.setFont("Courier-BoldOblique", 10.20)
    # p.setFillColor(blue)
    # p.setFillColor(HexColor(0xff8100))
    p.drawString(10, 510, '1-Pickup(Sender):')
    p.setFont("Courier-BoldOblique", 9.50)
    p.drawString(10, 490, 'Name:-')
    p.drawString(10, 475, 'Phone:-')
    p.drawString(210, 475, 'Email:-')
    p.drawString(10, 460, 'Address:-')
    p.drawString(10, 405, 'Country:-')
    p.drawString(215, 405, 'State:-')
    p.drawString(10, 385, 'City:-')
    p.drawString(215, 385, 'Locality:-')
    p.drawString(10, 365,'Sub-locality:-')
    p.drawString(215, 365, 'Pin:-')
    p.drawString(10, 348, 'Lat:-')
    p.drawString(215, 348, 'Lng:-')
    p.drawString(10, 332, 'Time:-')
    p.drawString(215, 332, 'Before:-')
    p.drawString(10, 315, 'After:-')
    p.drawString(10, 300, 'Instructions:-')
    p.setFont("Courier-BoldOblique", 10.20)
    p.drawString(390, 510, '2-Shipments(Receiver):')
    p.setFont("Courier-BoldOblique", 9.50)
    # p.drawString(300, 730, 'Drop:-')
    p.drawString(392, 490, 'Name:-')
    p.drawString(392, 475, 'Phone:-')
    p.drawString(595, 475, 'Email:-')
    p.drawString(392, 460, 'Address:-')
    p.drawString(392, 405, 'Country:-')
    p.drawString(595, 405, 'State:-')
    p.drawString(392, 385, 'City:-')
    p.drawString(595, 385, 'Locality:-')
    p.drawString(392, 365, 'Sub-locality:-')
    p.drawString(595, 365, 'Pin:-')
    p.drawString(392, 348, 'Lat:-')
    p.drawString(595, 348, 'Lng:-')
    p.drawString(392, 332, 'Time:-')
    p.drawString(595, 332, 'Before:-')
    p.drawString(392, 315, 'After:-')
    p.drawString(392, 300, 'Instructions:-')
    

    p.grid([0.100 * inch, 2.50 *inch, 5.40*inch, 8.20*inch, 10.90*inch], [3.25*inch, 3.50*inch, 3.75*inch])
    p.setStrokeColor(black)
    p.setFont("Courier-BoldOblique", 10.20)
    p.drawString(10, 275, '3-Payment:')
    p.setFont("Courier-BoldOblique", 9.50)
    p.drawString(10, 260, 'Payment Type:-')
    p.drawString(182, 260, 'Amount:-')
    # p.drawString(10, 200, ':-')


    

    p.showOutline()
    p.showPage()
    p.save()

    pdf_out = output.getvalue()
    output.close()
    response = make_response(pdf_out)
    response.headers['Content-Disposition'] = "attachment; filename='wabndetails.pdf"
    response.mimetype = 'application/pdf'
    return response


if __name__ == '__main__':
    app.run(port=5001)
