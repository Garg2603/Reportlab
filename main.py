from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, PageBreak
from reportlab.platypus.tables import Table, TableStyle, colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from datetime import datetime

def my_can(c):
    c.translate(inch,inch)
    c.setFont("Helvetica", 14)
    c.setStrokeColorRGB(0.1,0.8,0.1)
    c.setFillColorRGB(0,0,1) # font colour
    c.drawImage("/home/vrsiis/Desktop/downtime/abes.jpg",-0.8*inch,9.2*inch,width=120, height=60)
    c.setFont("Helvetica", 12)
    c.drawString(4*inch, 9.3*inch, "19th KM Stone , NH-09 ")
    c.setFont("Helvetica", 12)
    c.drawString(4*inch, 9.0*inch, "GHAZIABAD(U.P) PIN 201009")
    c.setFillColorRGB(0,0,0) 
    c.line(0,8.6*inch,6.8*inch,8.6*inch)
    c.drawString(-0.8*inch,9.0*inch,'Report No :# 1234')
    from  datetime import date
    dt = date.today().strftime('%d-%b-%Y')
    c.drawString(-0.8*inch,8.8*inch,dt)
    c.setFont("Helvetica", 15)
    c.drawString(3.9*inch,9.6*inch,'ABES Engineering College')
    c.line(0,-0.7*inch,6.8*inch,-0.7*inch)
    c.setFillColorRGB(1,0,0) # font colour
    c.drawString(0, -0.9*inch, u"\u00A9"+"abes.ac.in")
    c.rotate(45) # rotate by 45 degree
    c.setFillColorCMYK(0,0,0,0.08) # font colour CYAN, MAGENTA, YELLOW and BLACK
    c.setFont("Helvetica", 100) # font style and size
    c.drawString(2.5*inch,0.5*inch,'ABESEC') # String written
    c.rotate(-45) # restore the rotation
    return c

def my_can2(c):
    c.translate(inch,inch)
    c.setFont("Helvetica", 14)
    c.setStrokeColorRGB(0.1,0.8,0.1)
    c.setFillColorRGB(0,0,1) # font colour
    c.line(0,9.7*inch,6.8*inch,9.7*inch)
    c.line(0,-0.7*inch,6.8*inch,-0.7*inch)
    c.setFillColorRGB(1,0,0) # font colour
    c.drawString(0, -0.9*inch, u"\u00A9"+"abes.ac.in")
    c.rotate(45) # rotate by 45 degree
    c.setFillColorCMYK(0,0,0,0.08) # font colour CYAN, MAGENTA, YELLOW and BLACK
    c.setFont("Helvetica", 100) # font style and size
    c.drawString(2.5*inch,0.5*inch,'ABESEC') # String written
    c.rotate(-45) # restore the rotation
    return c

def first_page_elements(input_list):
    return input_list[:28]

def other_elements(input_list):
    return input_list[28:]
    
def split_list(input_list, chunk_size=31):
    return [input_list[i:i+chunk_size] for i in range(0, len(input_list), chunk_size)]

def generate_pdf(my_data, my_dict, output_path):
    
    my_new_data=other_elements(my_data)
    my_spl_data=split_list(my_new_data)
    my_spl_data1=first_page_elements(my_data)

    y_cod = 8.25
    c = canvas.Canvas(output_path, pagesize=letter)
    c=my_can(c) 
    c.setFillColorRGB(0.0, 0.0, 0.)
    c.setFont("Helvetica", 16)
    c.drawString(2.5 * inch, y_cod * inch, 'MNL Report')

    table_style = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    c_width = [0.5 * inch, 1.0 * inch, 1.0 * inch, 1.0 * inch, 1 * inch, 1.0 * inch]

    table_style2 = TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ])
    

    ln = len(my_spl_data1)
    y_cod -= ln * 0.3 

    col=[('Dev_ID', 'Dev_Name', 'Dev_Type', 'IP_Address', 'Uptime%', 'Curr_status')]
    data=col+my_spl_data1

    t1 = Table(data, rowHeights=20, repeatRows=1, colWidths=c_width)
    t1.setStyle(table_style)

    width1 = 5.5 * inch
    height1 = 20 * ln
    x1 = 50
    y1 = y_cod * inch

    if y_cod < -0.6:  # Check if enough space is available on the current page
        c.showPage()  # Start a new page
        y_cod = 9.5 
        y_cod -= ln * 0.3 # Reset y-coordinate for the new page
        y2 = y_cod * inch
        my_can2(c)
       

    t1.wrapOn(c, width1, height1)
    t1.drawOn(c, x1, y1)

    for i in my_spl_data:

        ln = len(i)
        y_cod -= ln * 0.3

               
        t = Table(i, rowHeights=20, repeatRows=1, colWidths=c_width)
        t.setStyle(table_style2)

        width = 5.5 * inch
        height = 20 * ln
        x = 50
        y = y_cod * inch

        if y_cod < -0.6:  # Check if enough space is available on the current page
            c.showPage() 
            y_cod = 9.5 
            y_cod -= ln * 0.3
            y = y_cod * inch # Reset y-coordinate for the new page
            my_can2(c)
            
            

        t.wrapOn(c, width, height)
        t.drawOn(c, x, y)

    y_cod -= 0.5
    if y_cod < -0.6:  # Check if enough space is available on the current page
        c.showPage() 
        y_cod = 9.4# Reset y-coordinate for the new page
        my_can2(c)
    c.setFillColorRGB(0.0, 0.0, 0.0)
    c.setFont("Helvetica", 16)
    c.drawString(2.5 * inch, y_cod * inch, 'Device Events')

    for key in my_dict:
        
        ele=my_dict[key]
        y_cod -= 0.5
        if y_cod < -0.6:  # Check if enough space is available on the current page
            c.showPage() 
            y_cod = 9.4 # Reset y-coordinate for the new page
            my_can2(c)
        c.setFillColorRGB(0.0, 0.0, 0.0)
        c.setFont("Helvetica", 12)
        id=ele[0][0]
        for row_ in my_data:
            if key==id:
                ip=row_[3]
                cs=row_[5]
        id_='Device ID:'+str(id)
        ip_='IP Address:'+ip
        cs_='Current Status:'+cs
        c.drawString(0.5 * inch, y_cod * inch, id_)
        c.setFont("Helvetica", 12)
        c.drawString(2.5 * inch, y_cod * inch, ip_)
        c.setFont("Helvetica", 12)
        c.drawString(4.5 * inch, y_cod * inch, cs_)

 
        ln = len(ele)+1
        y_cod -= (ln * 0.3) + 0.2
        
        col=[('Dev_ID','Current_Status','Timestamp')]
        data=col+ele

        t2 = Table(data, rowHeights=20, repeatRows=1, colWidths=[0.5 * inch, 1.0 * inch, 1.5 * inch])
        t2.setStyle(table_style)

        width2 = 2 * inch
        height2 = 20 * ln
        x2 = 140
        y2 = y_cod * inch

        if y_cod < -0.6:  # Check if enough space is available on the current page
            c.showPage()  # Start a new page
            y_cod = 9.5 
            y_cod -= ln * 0.3 # Reset y-coordinate for the new page
            y2 = y_cod * inch
            my_can2(c)
        

        t2.wrapOn(c, width2, height2)
        t2.drawOn(c, x2, y2)

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.setFont("Helvetica", 10)
    c.setFillColorRGB(0.5, 0.5, 0.5)
    c.drawString(-0.0 * inch, -0.6 * inch, f"{timestamp}")

    y_cod -= 0.3

    c.showPage()
    c.save()


my_data = [
    (1, 'ABC1', 'A', '192.1.75', 65, 'online'),
    (2, 'ABC2', 'B', '192.1.85', 45, 'offline'),
    (3, 'ABC3', 'c', '192.1.55', 87, 'online'),

]

my_dict={
    1:[(1, 'online', '2024-04-04 14:23:46'),
       (1, 'offline', '2024-04-04 14:23:46')
       ],
    2:[(2, 'online', '2024-04-04 14:23:46'),
       (2, 'offline', '2024-04-04 14:23:46')
       ],
    3:[(3, 'online', '2024-04-04 14:23:46'),
       (3, 'offline', '2024-04-04 14:23:46')
       ]
       }

output_path = '/home/vrsiis/Desktop/downtime/mypdf.pdf'

generate_pdf(my_data, my_dict, output_path)
