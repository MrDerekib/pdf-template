from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    topic = row["Topic"]
    pages = row["Pages"]

#  Set the header
    pdf.add_page()
    pdf.set_font(family="Helvetica", style="B", size=24)
    pdf.set_text_color(100, 100, 100)  # set text color to grey
    pdf.cell(0, 12, topic, align="L", border=0, new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(100, 100, 100)
    pdf.set_line_width(1)
    pdf.line(10, 21, 200, 21)

#  Set lines
    for line in range(31, 280, 10):
        pdf.set_draw_color(180, 180, 180)  # Light grey
        pdf.set_line_width(.5)
        pdf.line(10, line, 200, line)

#  Set the footer
    pdf.set_y(-15)
    pdf.set_font(family="Helvetica", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(0, 5, topic, align="R")

    for i in range(pages - 1):
        pdf.add_page()

        #  Set lines
        for line in range(31, 280, 10):
            pdf.set_draw_color(180, 180, 180)
            pdf.set_line_width(.5)
            pdf.line(10, line, 200, line)

        #  Set the footer
        pdf.set_y(-15)
        pdf.set_font(family="Helvetica", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(0, 5, topic, align="R")


pdf.output("output_lined.pdf")
