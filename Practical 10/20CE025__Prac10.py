import canvas
from reportlab.pdfgen.canvas import Canvas

canvas = Canvas("UniResult_Sem3.pdf")
canvas.drawString(50, 830, "Sem 3 Result of DHOLAKIA HARSHIL 20CE025")
canvas.drawString(50, 800, "CE244 SOFTWARE GROUP PROJECT-1   PRACTICAL : AA")
canvas.drawString(50, 780, "CE251 JAVA PROGRAMMING PRACTICAL :AB THEORY: AA")
canvas.drawString(50, 760, "CE252 DIGITAL ELECTRONICS PRACTICAL :BC THEORY: BB")
canvas.drawString(50, 740, "CE257 DATA COMMUNICATION & NETWORKING PRACTICAL :BC THEORY: BB")
canvas.drawString(50, 720, "INTRODUCTION TO WEB DESIGNING PRACTICAL :AA ")
canvas.drawString(50, 700, "HS123.02 A CREATIVITY, PROBLEM SOLVING AND INNOVATION PRACTICAL : BB")
canvas.drawString(50, 680, "MA253 DISTINCT MATHEMATICS AND ALGEBRA THEORY: AB")
canvas.drawString(50, 660, "CGPA : 8.66")
canvas.drawString(50, 640, "SGPA : 8.75")
canvas.save()


# ---------------------
# Setting the Page Size
# ---------------------

from reportlab.lib.units import inch, cm  # noqa

print(cm)
print(inch)

canvas = Canvas("UniResult_Sem3.pdf", pagesize=(8.5 * inch, 11 * inch))

from reportlab.lib.pagesizes import LETTER  # noqa

canvas = Canvas("UniResult_Sem3.pdf", pagesize=LETTER)
print(LETTER)


# -----------------------
# Setting Font Properties
# -----------------------

canvas = Canvas("font-example.pdf", pagesize=LETTER)
canvas.setFont("Times-Roman", 18)
canvas.drawString(1 * inch, 10 * inch, "Times New Roman (18 pt)")
canvas.save()

# The code below creates a PDF with blue text
from reportlab.lib.colors import blue  # noqa
from reportlab.lib.pagesizes import LETTER  # noqa
from reportlab.lib.units import inch  # noqa
from reportlab.pdfgen.canvas import Canvas  # noqa

canvas = Canvas("font-colors.pdf", pagesize=LETTER)

# Set font to Times New Roman with 12-point size
canvas.setFont("Times-Roman", 12)

# Draw blue text one inch from the left and ten
# inches from the bottom
canvas.setFillColor(blue)
canvas.drawString(1 * inch, 10 * inch, "Blue text")

# Save the PDF file
canvas.save()
