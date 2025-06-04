from fpdf import FPDF
import pandas

# ---- Generate Normal PDF File ----
# pdf = FPDF(orientation='P', unit='pt', format='A4')
# # add page
# pdf.add_page()
# # add image into page
# pdf.image('files/tiger.jpeg', w=80, h=50)
# # add text, pdf creation is base on the cell
# pdf.set_font(family='Times', style='B', size=24)
# pdf.cell(w=0, h=15, txt="Malayan Tiger", align='C', border=1, ln=1) # ln > control break line

# # content
# pdf.set_font(family='Times', style='B', size=14)
# pdf.cell(w=0, h=15, txt='Description', ln=1)

# pdf.set_font(family='Times', size=12)
# txt1 = """
#     The Malayan tiger is a tiger from a specific population of the Panthera tigris tigris subspecies that is native to Peninsular Malaysia. This population inhabits the southern and central parts of the Malay Peninsula, and has been classified as critically endangered. As of April 2014, the population was estimated at 80 120 mature individuals, with a continuing downward trend.
# """
# pdf.multi_cell(w=0, h=50, txt=txt1, ln=1)

# pdf.output('files/output.pdf')

# ---- Genaret PDF File From Excel ----
df = pandas.read_excel('files/data.xlsx')
#print(df)

for index, row in df.iterrows():
    #print(row)
    pdf = FPDF(orientation='P', unit='pt', format='A4')
    pdf.add_page()

    pdf.set_font(family='Times', style='B', size=24)
    pdf.cell(w=0, h=50, txt=row['name'], align='C',ln=1)

    for column in df.columns[1:]:
        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt=f"{column.title()}:")

        pdf.set_font(family='Times', style='B', size=14)
        pdf.cell(w=100, h=25, txt=row[column], ln=1)

    pdf.output(f"files/{row['name']}.pdf")


# ---- Extract Text from PDF ----
import fizt

with fizt.open("students.pdf") as file:
    for page in file:
        print(20*'--') # break line
        print(page.get_text())

# ---- Extract Tables from PDF ----
import tabula

table = tabula.read_pdf('weather.pdf', pages=2)

print(type(table[0])) # return DataFrame object

table[0].to_csv('output.csv') # generate csv file