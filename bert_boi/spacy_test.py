import spacy

nlp = spacy.load("en_core_web_sm")

sentence = """Nelcome to Belgian Waffle

~ Bridg

Type : TAKE AWAY

 

Bill No.:179
Delivery Boy:
Date: 2019-19-94 22:17:54
Kots:0
Item Qty Amt
BELGIAN CHO
COLATE (MILK) 2 247.62
Total Qty: 2
SubTotal: 247.62
GST@5% 12.38
CGST @2.5 6.19
SGST @2.5 6 19
Re ee
Round Off: 0.00
Total Invoice valua 260
Payment Detail:
SS SS SS ee eee eee
Cash 260.00

le Value your feedback, write us
nfo@thebelgianwaffle co
hank you visit again!!!

Powered by - PoSist%"""
doc = nlp(sentence)

for ent in doc.ents:
    print(ent.text, ent.label_)
