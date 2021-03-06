import requests
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


def send_request(wabn=None):
    if wabn:
        response = requests.get(
            url="http://localhost:8000/order/",
            params={
                "wabn": wabn,
            },
            headers={
                "Authorization": "Token b5b034a6922bb2aa61b70c526545cd9ccf07d94a",
            }, )
    # print response.json()
        resp = response.json()
        data = resp.get('results')[0]
        return data
    return {}

@app.route('/pdf')
def pdf():
    data = send_request("688775458968")
    name = "Name:- {}".format(data.get('pickup')['name'])
    phone = "Phone:- {}".format(data.get('pickup')['phone'])
    email = "Email:- {}".format(data.get('pickup')['email'])
    country = "Country:- {}".format(data.get('country'))
    state = "State:- {}".format(data.get('state'))
    city = "City:- {}".format(data.get('city'))
    locality = "Locality:- {}".format(data.get('locality'))
    sublocality = "Sub-locality:- {}".format(data.get('sublocality'))
    orderid = "Order Id:- {}".format(data.get('orderid'))
    pin = "Pin:- {}".format(data.get('pin'))
    lat = "Lat:- {}".format(data.get('lat'))
    lng = "Lng:- {}".format(data.get('lng'))
    time = "Time:- {}".format(data.get('time'))
    before = "Before:- {}".format(data.get('before'))
    after = "After:- {}".format(data.get('after'))
    instructions = "Instructions:- {}".format(data.get('instructions'))


    name = "Name:- {}".format(data.get('drop')['name'])
    phone = "Phone:- {}".format(data.get('drop')['phone'])
    email = "Email:- {}".format(data.get('drop')['email'])
    country = "Country:- {}".format(data.get('country'))
    state = "State:- {}".format(data.get('state'))
    city = "City:- {}".format(data.get('city'))
    locality = "Locality:- {}".format(data.get('locality'))
    sublocality = "Sub-locality:- {}".format(data.get('sublocality'))
    pin = "Pin:- {}".format(data.get('pin'))
    lat = "Lat:- {}".format(data.get('lat'))
    lng = "Lng:- {}".format(data.get('lng'))
    time = "Time:- {}".format(data.get('time'))
    before = "Before:- {}".format(data.get('before'))
    after = "After:- {}".format(data.get('after'))
    instructions = "Instructions:- {}".format(data.get('instructions'))
    payment_type = "Payment Type:- {}".format(data.get('payment')['payment_type'])
    amount = "Amount:- {}".format(data.get('payment')['amount'])
    collectible_amount = "Collectible Amount:- {}".format(data.get('payment')['collectible_amount'])
    order_id = "Order Id:- {}".format(data.get('orderid'))
    description = "Description:- {}".format(data.get('description'))
    billable_weight = "Billable Weight:- {}".format(data.get('billable_weight'))
    dimensions = "Dimensions:- {}".format(data.get('dimensions'))
    volumetric = "Volumetric:- {}".format(data.get('volumetric'))
    weight = "Weight:- {}".format(data.get('weight'))
    product_quantity = "product_quantity:- {}".format(data.get('product_quantity'))
    seller_invoice_no = "Seller_Invoice_No:- {}".format(data.get('seller_invoice_no'))
    seller_invoice_date = "Seller_Invoice_Date:- {}".format(data.get('seller_invoice_date'))
    seller_name = "Seller Name:- {}".format(data.get('seller_name'))
    seller_cst = "Seller_cst:- {}".format(data.get('seller_cst'))
    seller_tin = "Seller_tin:- {}".format(data.get('seller_tin'))
    commodity_value = "Commodity Value:- {}".format(data.get('commodity_value'))
    tax_value = "Tax Value:- {}".format(data.get('tax_value'))
    sales_tax_form_ack_no = "sales_tax_form_ack_no:- {}".format(data.get('sales_tax_form_ack_no'))
    category_of_goods = "category_of_goods:- {}".format(data.get('category_of_goods'))


    import cStringIO
    output = cStringIO.StringIO()
    p = canvas.Canvas(output)
    p.setPageSize(landscape(letter))
    logo = ImageReader('http://www.endeavor.org/content/uploads/2015/07/Fetchr-180x180.png')
    p.drawImage(logo, 10, 480, mask='auto')
    barcode = code128.Code128("123456789", barHeight=.4 * inch, barWidth=1.5)
    barcode.drawOn(p, 200 * mm, 200 * mm)
    p.setFont("Helvetica-Bold", 12)
    p.drawString(200, 582, 'AIR WAYBILL')
    p.setFont("Courier-Bold", 8)
    p.drawString(283, 582.10, 'Track your shipment online on')
    p.setFont("Courier-Bold", 9)
    p.drawString(428, 582.10, 'FETCHR.US')
    p.grid([0.100 * inch, 5.40 * inch, 10.90 * inch],[4.05 * inch, 4.30 * inch, 4.75 * inch, 5.0 * inch, 5.25 * inch, 5.50 * inch, 5.75 * inch, 6.50 * inch,6.75 * inch, 7.0 * inch])
    p.setStrokeColor(black)
    p.drawString(2.5 * inch, 3.5 * inch, "")
    p.setFont("Courier-BoldOblique", 10.20)
    # p.setFillColor(blue)
    # p.setFillColor(HexColor(0xff8100))
    p.drawString(10, 510, '1-Pickup(Sender):')
    p.setFont("Courier-BoldOblique", 9.50)
    p.drawString(10, 490, name)
    p.drawString(10, 475, phone)
    p.drawString(210, 475, email)
    p.drawString(10, 460, 'Address:-')
    p.drawString(10, 405, country)
    p.drawString(215, 405, state)
    p.drawString(10, 385, city)
    p.drawString(215, 385, locality)
    p.drawString(10, 365, sublocality)
    p.drawString(215, 365, pin)
    p.drawString(10, 348, lat)
    p.drawString(215, 348, lng)
    p.drawString(10, 332, time)
    p.drawString(215, 332, before)
    p.drawString(10, 315, after)
    p.drawString(10, 300, instructions)
    p.setFont("Courier-BoldOblique", 10.20)
    p.drawString(390, 510, '2-Shipments(Receiver):')
    p.setFont("Courier-BoldOblique", 9.50)
    # p.drawString(300, 730, 'Drop:-')
    p.drawString(392, 490, name)
    # p.setFont("Helvetica", 8.50)
    p.drawString(392, 475, phone)
    p.drawString(595, 475, email)
    p.drawString(392, 460, 'Address:-')
    p.drawString(392, 405, country)
    p.drawString(595, 405, state)
    p.drawString(392, 385, city)
    p.drawString(595, 385, locality)
    p.drawString(392, 365, sublocality)
    p.drawString(595, 365, pin)
    p.drawString(392, 348, lat)
    p.drawString(595, 348, lng)
    p.drawString(392, 332, time)
    p.drawString(595, 332, before)
    p.drawString(392, 315, after)
    p.drawString(392, 300, instructions)

    p.grid([0.100 * inch, 5.40 * inch, 8.40 * inch], [2.00 * inch, 3.00 * inch, 3.50 * inch, 3.75 * inch])
    p.setStrokeColor(black)
    p.setFont("Courier-BoldOblique", 10.20)
    p.drawString(10, 275, '3-Shipment Details:')
    p.setFont("Courier-BoldOblique", 9.50)
    p.drawString(10, 258, order_id)
    p.drawString(10, 240, description)
    p.setFont("Courier-BoldOblique", 9.50)
    p.drawString(10, 200, billable_weight)
    p.drawString(185, 200, dimensions)
    p.drawString(10, 158, volumetric)
    p.drawString(185, 158, weight)
    p.drawString(392, 258, product_quantity)
    p.drawString(392, 240, seller_invoice_no)
    p.drawString(392, 205, seller_invoice_date)
    p.drawString(392, 160, seller_name)

    p.grid([0.100 * inch, 8.40 * inch], [1.50 * inch, 2.00 * inch])
    p.setStrokeColor(black)
    p.setFont("Courier-BoldOblique", 9.50)
    p.drawString(10, 130, 'Seller Address:-')
    p.grid([0.100 * inch, 4.40 * inch, 8.40 * inch], [1 * inch, 1.25 * inch, 1.50 * inch])
    p.setStrokeColor(black)
    p.setFont("Courier-BoldOblique", 9.50)
    p.drawString(10, 95, seller_cst)
    p.drawString(320, 95, seller_tin)
    p.drawString(10, 77, commodity_value)
    p.drawString(320, 78, tax_value)
    p.grid([0.100 * inch, 8.40 * inch], [0.50 * inch, 0.75 * inch, 1 * inch])
    p.setStrokeColor(black)
    p.setFont("Courier-BoldOblique", 9.50)
    p.drawString(10, 60, sales_tax_form_ack_no)
    p.drawString(10, 42, category_of_goods)

    p.grid([8.40 * inch, 10.90 * inch], [0.50 * inch, 1.50 * inch, 2.75 * inch, 3.75 * inch])
    p.setStrokeColor(black)
    p.setFont("Courier-BoldOblique", 10.20)
    p.drawString(610, 275, '4-Method of Payment:')
    p.setFont("Courier-BoldOblique", 9.50)
    p.drawString(610, 260, payment_type)
    p.drawString(610, 190, amount)
    p.drawString(610, 95, collectible_amount)

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
    app.run(port=5001 , debug=True)
