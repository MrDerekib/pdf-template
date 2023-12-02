from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    title = row["Topic"]

    pdf.add_page()
    pdf.set_font(family="Helvetica", style="B", size=24)
    pdf.set_text_color(100, 100, 100)  # set text color to grey
    pdf.cell(0, 12, title, align="L", border=0, new_x="LMARGIN", new_y="NEXT")
    pdf.set_draw_color(100, 100, 100)
    pdf.set_line_width(1)
    pdf.line(10, 21, 200, 21)

pdf.output("output.pdf")