import sqlite3

#initial connection
con = sqlite3.connect('database.db')

#get cursor
cur = con.cursor()

# Execute sql
cur.execute("select * from 'ips' order by asn")

print(cur.fetchall())

res = cur.fetchall()

for row in res:
    print(row)

# ---- convert data into csv ---- 
import pandas

# using pandas to parse fetched data

df = pandas.read_sql_query("select * from 'ips' order by asn", con)

df.to_csv('database.csv', index=None)

# ---- generate PDF file ----
from fpdf import FPDF

# query table info
cur.execute('PRAGMA table_info(ips)')
columns = cur.fetchall()

# initial PDF
pdf = FPDF(orientation='P', unit='pt', format='A4')
pdf.add_page()

for column in columns:
    pdf.set_font(family='Times', style='B', size=14)
    pdf.cell(w=100, h=25, txt=column[1], border=1)

cur.execute("select * from 'ips'")

pdf.ln()

for row in rows:
    for element in row:
        pdf.set_font(family='Times', size=14)
        pdf.cell(w=100, h=30, txt=str(element), border=1)
    pdf.ln()    

pdf.output('output.pdf')

# ---- insert records into DB ----
new_rows = [
    ('100.100.100.100','a.b.c',100)
]

cur.executemany("INSERT INTO 'ips' VALUES(?, ?, ?)", new_rows)
con.commit()
