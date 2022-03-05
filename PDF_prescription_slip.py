from fpdf import FPDF

# saving FPDF() class into a variable pdf
pdf = FPDF()

# Adding page
pdf.add_page()

# setting style and size of font in the pdf
pdf.set_font("Arial", size = 15)

# hospital brand name
pdf.set_fill_color(153, 255, 255)
pdf.cell(0, 10, txt = "PANDA'S MEDICARE SOLUTIONS", border = 1, ln=1, align='C', fill = True)

# company tagline
pdf.set_fill_color(200, 200, 200)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 10, txt = '"Healing and empowering people through technology."', border = 1, ln=1, align='C', fill = True)

pdf.cell(0, 10, txt = " ", ln=2, align='C')

pdf.cell(0, 10, txt = "Dr. Rishabh Panda, M.B.B.S., M.S.(Ortho.)", ln=2, align='C')

pdf.cell(0, 10, txt = "Hyderabad, India (500032)", ln=2, align='R')
pdf.cell(0, 10, txt = "Ph: (+91)7981927240", ln=2, align='R')
pdf.cell(0, 10, txt = "FAX:(207) 808 2015 2202", ln=2, align='R')

pdf.cell(0, 10, txt = " ", ln=2, align='C')

pdf.cell(0, 10, txt = "PRESCRIPTION (Rx)", ln=2, align='L')
pdf.cell(0, 10, txt = "_________________", ln=2, align='L')

pdf.cell(0, 10, txt = MyText, ln=2, align='L')

# save the pdf with name.pdf
pdf.output("DrPanda_presc.pdf")
