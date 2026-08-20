#!/usr/bin/env python3
"""Answer workbooks for Section 1 questions 6-30.

Same pattern as build_s1_answers.py, which covers questions 1-5: one workbook
per question holding the finished sheet, with the formulas live and a
FORMULATEXT column showing what was typed. The data is synthetic and small
because this section tests spreadsheet mechanics, not statistics.

Every figure in the bank's answer keys for these questions was computed before
being written down. Edit this script, not the .xlsx files it writes.

Run:  python3 practice/build_s1_extra.py
"""
import datetime as dt
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from build_s1_answers import (put, header, finish, new_book, note, save,
                              f_body, f_bold, f_form, f_note, f_head,
                              lock_fill, centre, FT)

MONEY = '"$"#,##0.00'; MONEY0 = '"$"#,##0'; PCT0 = "0%"; PCT1 = "0.0%"
ONE = "0.0"; TWO = "0.00"; INT = "#,##0"


def table(ws, r0, cols, rows, fmts=None, widths=None):
    """Write a small table and return the first and last data rows."""
    header(ws, r0, cols)
    for i, row in enumerate(rows):
        for j, v in enumerate(row):
            f = (fmts or {}).get(j)
            put(ws, r0 + 1 + i, 1 + j, v, fmt=f,
                align=centre if j and not isinstance(v, str) else None)
    return r0 + 1, r0 + len(rows)


def formula(ws, r, c, f, fmt=None, show_col=None):
    put(ws, r, c, f, fill=lock_fill, fmt=fmt, align=centre)
    if show_col:
        put(ws, r, show_col, f"={FT}({chr(64+c)}{r})", font=f_form)


def stat(ws, r, label, f, fmt=None, show=4):
    put(ws, r, 1, label, font=f_bold)
    put(ws, r, 3, f, fill=lock_fill, fmt=fmt, align=centre)
    put(ws, r, show, f"={FT}(C{r})", font=f_form)


# ---------------------------------------------------------------------------
def q6():
    wb, ws = new_book("Bin fill rates — averaging percentages",
        "Each bin's fill rate is filled bushels over capacity. The farm's overall "
        "rate comes from the two totals, not from averaging the five percentages.")
    rows = [("Bin 1",4200,3780),("Bin 2",2800,2100),("Bin 3",5500,5225),
            ("Bin 4",3100,1860),("Bin 5",4600,4370)]
    header(ws, 4, ["Bin","Capacity (bu)","Filled (bu)","Fill %","The formula in D"])
    for i,(n,c,f) in enumerate(rows):
        r = 5+i
        put(ws,r,1,n); put(ws,r,2,c,fmt=INT,align=centre); put(ws,r,3,f,fmt=INT,align=centre)
        put(ws,r,4,f"=C{r}/B{r}",fill=lock_fill,fmt=PCT0,align=centre)
        put(ws,r,5,f"={FT}(D{r})",font=f_form)
    last = 4+len(rows)
    put(ws,last+1,1,"Total",font=f_bold)
    put(ws,last+1,2,f"=SUM(B5:B{last})",font=f_bold,fill=lock_fill,fmt=INT,align=centre)
    put(ws,last+1,3,f"=SUM(C5:C{last})",font=f_bold,fill=lock_fill,fmt=INT,align=centre)
    stat(ws,last+3,"Overall fill rate (totals)",f"=C{last+1}/B{last+1}",PCT1,5)
    stat(ws,last+4,"AVERAGE of the Fill % column",f"=AVERAGE(D5:D{last})",PCT1,5)
    note(ws,last+6,
        "85.8% against 83.0%. The overall rate counts every bushel of capacity once. "
        "The average of the column counts every bin once, so the 2,800-bushel bin "
        "carries the same weight as the 5,500-bushel one.",5)
    finish(ws,[("A",14),("B",16),("C",14),("D",12),("E",26)],last+6)
    return wb


def q7():
    wb, ws = new_book("Summarising a small column",
        "MIN, MAX, AVERAGE and MEDIAN over seven plots, then what happens to the "
        "mean and the median when one value moves a long way.")
    rows=[("A",47.2),("B",61.8),("C",39.5),("D",55.1),("E",43.7),("F",58.9),("G",50.3)]
    first,last = table(ws,4,["Plot","Yield (bu/ac)"],rows,{1:ONE})
    rng=f"B{first}:B{last}"
    for k,(lab,f,fmt) in enumerate([("Minimum",f"=MIN({rng})",ONE),
            ("Maximum",f"=MAX({rng})",ONE),("Range",f"=MAX({rng})-MIN({rng})",ONE),
            ("Mean",f"=AVERAGE({rng})",TWO),("Median",f"=MEDIAN({rng})",ONE),
            ("Count",f"=COUNT({rng})",INT)]):
        stat(ws,last+2+k,lab,f,fmt)
    note(ws,last+9,
        "Change plot B to 91.8 and the mean climbs to 55.21 while the median stays "
        "at 50.3. The mean adds every value; the median only cares which value sits "
        "in the middle.",4)
    finish(ws,[("A",22),("B",14),("C",14),("D",30)],last+9)
    return wb


def q8():
    wb, ws = new_book("One rate, one cell",
        "The trucking rate lives in a single cell and every row points at it with an "
        "absolute reference, so renegotiating the rate is a one-cell edit.")
    put(ws,4,1,"Rate ($/tonne)",font=f_bold); put(ws,4,2,12.75,fill=lock_fill,fmt=MONEY,align=centre)
    rows=[("2026-09-12",28.4),("2026-09-19",31.7),("2026-09-26",26.9),
          ("2026-10-03",34.2),("2026-10-10",29.8)]
    header(ws,6,["Date","Tonnes","Trucking cost","The formula in C"])
    for i,(d,t) in enumerate(rows):
        r=7+i
        put(ws,r,1,dt.date.fromisoformat(d),fmt="DD-MMM-YY",align=centre)
        put(ws,r,2,t,fmt=ONE,align=centre)
        put(ws,r,3,f"=B{r}*$B$4",fill=lock_fill,fmt=MONEY,align=centre)
        put(ws,r,4,f"={FT}(C{r})",font=f_form)
    last=6+len(rows)
    put(ws,last+1,1,"Total",font=f_bold)
    put(ws,last+1,2,f"=SUM(B7:B{last})",font=f_bold,fill=lock_fill,fmt=ONE,align=centre)
    put(ws,last+1,3,f"=SUM(C7:C{last})",font=f_bold,fill=lock_fill,fmt=MONEY,align=centre)
    stat(ws,last+3,"Average cost per load",f"=AVERAGE(C7:C{last})",MONEY)
    stat(ws,last+4,"Total / COUNT",f"=C{last+1}/COUNT(B7:B{last})",MONEY)
    note(ws,last+6,
        "Change B4 to 11.90 and the total falls to $1,796.90. Had the rate been typed "
        "into each row, the edit would be five edits -- and missing one leaves a total "
        "that still looks plausible.",4)
    finish(ws,[("A",14),("B",12),("C",16),("D",26)],last+6)
    return wb


def q9():
    wb, ws = new_book("A threshold in a cell",
        "The moisture limit sits in one cell. The IF column and the COUNTIF both "
        "point at it, so lowering the limit reruns everything.")
    put(ws,4,1,"Dry limit (%)",font=f_bold); put(ws,4,2,14.5,fill=lock_fill,fmt=ONE,align=centre)
    rows=[("Truck 1",13.8),("Truck 2",14.6),("Truck 3",15.2),
          ("Truck 4",13.1),("Truck 5",14.9),("Truck 6",16.0)]
    header(ws,6,["Truck","Moisture (%)","Status","The formula in C"])
    for i,(n,m) in enumerate(rows):
        r=7+i
        put(ws,r,1,n); put(ws,r,2,m,fmt=ONE,align=centre)
        put(ws,r,3,f'=IF(B{r}>$B$4,"Tough","Dry")',fill=lock_fill,align=centre)
        put(ws,r,4,f"={FT}(C{r})",font=f_form)
    last=6+len(rows)
    stat(ws,last+2,"Tough loads",f'=COUNTIF(C7:C{last},"Tough")',INT)
    stat(ws,last+3,"Average moisture",f"=AVERAGE(B7:B{last})",'0.0"%"')
    stat(ws,last+4,"Fraction tough",f'=COUNTIF(C7:C{last},"Tough")/COUNT(B7:B{last})',PCT0)
    note(ws,last+6,
        "Four loads are tough at a 14.5 limit. Drop B4 to 13.5 and five are, with only "
        "Truck 4 staying dry -- nothing needed retyping, because both formulas read the "
        "limit cell rather than holding the number.",4)
    finish(ws,[("A",14),("B",14),("C",12),("D",30)],last+6)
    return wb


def q10():
    wb, ws = new_book("Rounding each value, or rounding the total",
        "Five payments, once unrounded and once through ROUND. The two totals differ "
        "because rounding five values collects five rounding errors.")
    put(ws,4,1,"Price ($/tonne)",font=f_bold); put(ws,4,2,9.87,fill=lock_fill,fmt=MONEY,align=centre)
    rows=[("Load A",22.35),("Load B",18.62),("Load C",25.19),("Load D",20.44),("Load E",24.03)]
    header(ws,6,["Load","Tonnes","Payment","ROUND to $","The formula in D"])
    for i,(n,t) in enumerate(rows):
        r=7+i
        put(ws,r,1,n); put(ws,r,2,t,fmt=TWO,align=centre)
        put(ws,r,3,f"=B{r}*$B$4",fill=lock_fill,fmt=MONEY0,align=centre)
        put(ws,r,4,f"=ROUND(B{r}*$B$4,0)",fill=lock_fill,fmt=MONEY0,align=centre)
        put(ws,r,5,f"={FT}(D{r})",font=f_form)
    last=6+len(rows)
    put(ws,last+1,1,"Total",font=f_bold)
    put(ws,last+1,3,f"=SUM(C7:C{last})",font=f_bold,fill=lock_fill,fmt=MONEY,align=centre)
    put(ws,last+1,4,f"=SUM(D7:D{last})",font=f_bold,fill=lock_fill,fmt=MONEY0,align=centre)
    stat(ws,last+3,"ROUND of the true total",f"=ROUND(C{last+1},0)",MONEY0,5)
    note(ws,last+5,
        "True total $1,091.92; the rounded column adds to $1,093; rounding the total "
        "once gives $1,092. The $1.08 gap is five rounding errors that mostly went the "
        "same way.",5)
    finish(ws,[("A",14),("B",12),("C",14),("D",14),("E",28)],last+5)
    return wb


def q11():
    wb, ws = new_book("A grid from one formula",
        "Crops down, grades across, one formula filled both ways. The crop reference "
        "locks its column, the grade factor locks its row, the price locks both.")
    put(ws,4,1,"Base price ($/bu)",font=f_bold); put(ws,4,2,14.20,fill=lock_fill,fmt=MONEY,align=centre)
    crops=[("Canola",41.2),("Wheat",58.6),("Barley",72.4)]
    grades=[("No. 1",1.00),("No. 2",0.93),("Sample",0.78)]
    put(ws,6,1,"Yield (bu/ac)",font=f_bold)
    for j,(g,f) in enumerate(grades):
        put(ws,6,3+j,g,font=f_head,align=centre); put(ws,7,3+j,f,fmt=TWO,align=centre)
    for i,(c,y) in enumerate(crops):
        r=8+i
        put(ws,r,1,c); put(ws,r,2,y,fmt=ONE,align=centre)
        for j in range(len(grades)):
            col=chr(67+j)
            put(ws,r,3+j,f"=$B{r}*$B$4*{col}$7",fill=lock_fill,fmt=MONEY0,align=centre)
    last=7+len(crops)
    put(ws,last+2,1,"The one formula",font=f_bold)
    put(ws,last+2,3,f"={FT}(C8)",font=f_form)
    stat(ws,last+4,"Best combination (MAX)",f"=MAX(C8:E{last})",MONEY0)
    note(ws,last+6,
        "$1,028 -- barley at No. 1. Lock every reference instead and all nine cells "
        "read $585, the canola No. 1 figure, because nothing moves when you fill.",5)
    finish(ws,[("A",18),("B",14),("C",12),("D",12),("E",12)],last+6)
    return wb


def q12():
    wb, ws = new_book("Blanks, text, and what the functions count",
        "COUNT sees numbers, COUNTA sees anything typed, AVERAGE skips both blanks "
        "and text. Filling the blanks with zero would change the claim being made.")
    rows=[("North",41.2),("South",None),("Creek",44.8),
          ("Home","not seeded"),("Rented",39.9),("Quarter",None)]
    header(ws,4,["Field","Yield (bu/ac)"])
    for i,(n,v) in enumerate(rows):
        r=5+i
        put(ws,r,1,n)
        put(ws,r,2,v,fmt=ONE if isinstance(v,float) else None,
            align=centre if isinstance(v,float) else None)
    last=4+len(rows)
    rng=f"B5:B{last}"
    for k,(lab,f,fmt) in enumerate([("COUNT (numbers)",f"=COUNT({rng})",INT),
            ("COUNTA (anything)",f"=COUNTA({rng})",INT),
            ("SUM",f"=SUM({rng})",ONE),("AVERAGE",f"=AVERAGE({rng})",TWO),
            ("SUM / COUNT",f"=SUM({rng})/COUNT({rng})",TWO)]):
        stat(ws,last+2+k,lab,f,fmt)
    note(ws,last+8,
        "COUNT 3, COUNTA 4 -- the difference is the words 'not seeded'. The average is "
        "41.97 over three values. Type 0 into the two blanks and it falls to 25.18, "
        "which asserts those fields yielded nothing.",4)
    finish(ws,[("A",20),("B",14),("C",14),("D",30)],last+8)
    return wb


def q13():
    wb, ws = new_book("Days between two dates",
        "Subtracting one date from another gives days, because Excel stores dates as "
        "numbers. The result cell has to be formatted as a number, not a date.")
    rows=[("North","2026-05-08","2026-09-14"),("South","2026-05-21","2026-09-18"),
          ("Creek","2026-04-29","2026-09-09"),("Home","2026-05-19","2026-10-02"),
          ("Rented","2026-05-12","2026-09-22")]
    header(ws,4,["Field","Seeded","Harvested","Days","The formula in D"])
    for i,(n,a,b) in enumerate(rows):
        r=5+i
        put(ws,r,1,n)
        put(ws,r,2,dt.date.fromisoformat(a),fmt="DD-MMM-YY",align=centre)
        put(ws,r,3,dt.date.fromisoformat(b),fmt="DD-MMM-YY",align=centre)
        put(ws,r,4,f"=C{r}-B{r}",fill=lock_fill,fmt=INT,align=centre)
        put(ws,r,5,f"={FT}(D{r})",font=f_form)
    last=4+len(rows)
    rng=f"D5:D{last}"
    for k,(lab,f,fmt) in enumerate([("Shortest",f"=MIN({rng})",INT),
            ("Longest",f"=MAX({rng})",INT),("Average",f"=AVERAGE({rng})",ONE),
            ("Range",f"=MAX({rng})-MIN({rng})",INT)]):
        stat(ws,last+2+k,lab,f,fmt,5)
    note(ws,last+7,
        "120 days at South to 136 at Home, a 16-day spread. If the Days column shows "
        "something like 04-May-1900 it has inherited the date format from the cells "
        "being subtracted; set it to Number.",5)
    finish(ws,[("A",14),("B",14),("C",14),("D",10),("E",24)],last+7)
    return wb


def q14():
    wb, ws = new_book("Change in bushels and change in percent",
        "The same gain is a different percentage depending on where it started. The "
        "average of five percentage changes is not the percentage change of the total.")
    rows=[("Canola",38.4,41.2),("Wheat",52.1,58.6),("Barley",66.8,72.4),
          ("Oats",71.3,68.9),("Peas",34.6,37.1)]
    header(ws,4,["Crop","2025","2026","Change","% change","The formula in E"])
    for i,(c,a,b) in enumerate(rows):
        r=5+i
        put(ws,r,1,c); put(ws,r,2,a,fmt=ONE,align=centre); put(ws,r,3,b,fmt=ONE,align=centre)
        put(ws,r,4,f"=C{r}-B{r}",fill=lock_fill,fmt=ONE,align=centre)
        put(ws,r,5,f"=(C{r}-B{r})/B{r}",fill=lock_fill,fmt=PCT1,align=centre)
        put(ws,r,6,f"={FT}(E{r})",font=f_form)
    last=4+len(rows)
    put(ws,last+1,1,"Total",font=f_bold)
    put(ws,last+1,2,f"=SUM(B5:B{last})",font=f_bold,fill=lock_fill,fmt=ONE,align=centre)
    put(ws,last+1,3,f"=SUM(C5:C{last})",font=f_bold,fill=lock_fill,fmt=ONE,align=centre)
    stat(ws,last+3,"AVERAGE of the % column",f"=AVERAGE(E5:E{last})",PCT1,6)
    stat(ws,last+4,"% change of the totals",f"=(C{last+1}-B{last+1})/B{last+1}",PCT1,6)
    note(ws,last+6,
        "6.4% against 5.7%. Oats is the only crop that fell and also the largest 2025 "
        "number, so weighting by bushels pulls the figure down; averaging the five "
        "percentages treats oats as one crop among five.",6)
    finish(ws,[("A",14),("B",10),("C",10),("D",10),("E",12),("F",26)],last+6)
    return wb


def q15():
    wb, ws = new_book("A blended price",
        "Total revenue over total tonnes gives the price the farm actually received. "
        "The plain average of the three grade prices treats the grades as equal.")
    rows=[("No. 1",1240,14.85),("No. 2",860,13.40),("Sample",410,10.75)]
    header(ws,4,["Grade","Tonnes","Price ($/t)","Revenue","The formula in D"])
    for i,(g,t,p) in enumerate(rows):
        r=5+i
        put(ws,r,1,g); put(ws,r,2,t,fmt=INT,align=centre); put(ws,r,3,p,fmt=MONEY,align=centre)
        put(ws,r,4,f"=B{r}*C{r}",fill=lock_fill,fmt=MONEY,align=centre)
        put(ws,r,5,f"={FT}(D{r})",font=f_form)
    last=4+len(rows)
    put(ws,last+1,1,"Total",font=f_bold)
    put(ws,last+1,2,f"=SUM(B5:B{last})",font=f_bold,fill=lock_fill,fmt=INT,align=centre)
    put(ws,last+1,4,f"=SUM(D5:D{last})",font=f_bold,fill=lock_fill,fmt=MONEY,align=centre)
    stat(ws,last+3,"Blended: revenue / tonnes",f"=D{last+1}/B{last+1}",MONEY,5)
    stat(ws,last+4,"Blended: SUMPRODUCT",f"=SUMPRODUCT(B5:B{last},C5:C{last})/SUM(B5:B{last})",MONEY,5)
    stat(ws,last+5,"AVERAGE of the price column",f"=AVERAGE(C5:C{last})",MONEY,5)
    note(ws,last+7,
        "$13.68 against $13.00. The two blended routes agree, which is the check. The "
        "plain average treats Sample -- 410 of 2,510 tonnes -- as equal in weight to "
        "No. 1.",5)
    finish(ws,[("A",26),("B",12),("C",14),("D",14),("E",30)],last+7)
    return wb


def q16():
    wb, ws = new_book("Summing a range that contains its own total",
        "The second SUM reaches over the total row, so every bushel is counted twice. "
        "The giveaway is that the answer is exactly double.")
    rows=[("North",1240),("South",2180),("Creek",860),("Home",1975),("Rented",1420)]
    first,last=table(ws,4,["Field","Bushels"],rows,{1:INT})
    put(ws,last+1,1,"Total",font=f_bold)
    put(ws,last+1,2,f"=SUM(B{first}:B{last})",font=f_bold,fill=lock_fill,fmt=INT,align=centre)
    put(ws,last+1,3,f"={FT}(B{last+1})",font=f_form)
    stat(ws,last+3,"SUM including the total row",f"=SUM(B{first}:B{last+1})",INT)
    note(ws,last+5,
        "7,675 against 15,350. The total row already holds the five fields, so "
        "including it adds the whole farm a second time. Leave a blank row under a "
        "table, or look at what the range highlights before pressing Enter.",4)
    finish(ws,[("A",26),("B",14),("C",26),("D",30)],last+5)
    return wb


def q17():
    wb, ws = new_book("Two rates, both in cells",
        "Every acre carries the same two rates, so the cost per acre is just the two "
        "rates added -- the field sizes cancel out entirely.")
    put(ws,4,1,"Fuel ($/ac)",font=f_bold); put(ws,4,2,18.40,fill=lock_fill,fmt=MONEY,align=centre)
    put(ws,5,1,"Labour ($/ac)",font=f_bold); put(ws,5,2,11.25,fill=lock_fill,fmt=MONEY,align=centre)
    rows=[("North",120),("South",240),("Creek",95),("Home",310),("Rented",175)]
    header(ws,7,["Field","Acres","Cost","The formula in C"])
    for i,(n,a) in enumerate(rows):
        r=8+i
        put(ws,r,1,n); put(ws,r,2,a,fmt=INT,align=centre)
        put(ws,r,3,f"=B{r}*($B$4+$B$5)",fill=lock_fill,fmt=MONEY,align=centre)
        put(ws,r,4,f"={FT}(C{r})",font=f_form)
    last=7+len(rows)
    put(ws,last+1,1,"Total",font=f_bold)
    put(ws,last+1,2,f"=SUM(B8:B{last})",font=f_bold,fill=lock_fill,fmt=INT,align=centre)
    put(ws,last+1,3,f"=SUM(C8:C{last})",font=f_bold,fill=lock_fill,fmt=MONEY,align=centre)
    stat(ws,last+3,"Cost per acre (totals)",f"=C{last+1}/B{last+1}",MONEY)
    stat(ws,last+4,"Fuel + labour",f"=$B$4+$B$5",MONEY)
    note(ws,last+6,
        "Both give $29.65, and they must: every acre is charged the same two rates, so "
        "nothing in the calculation varies by field. Raise fuel to $21.60 and the total "
        "becomes $30,879.00.",4)
    finish(ws,[("A",22),("B",12),("C",14),("D",26)],last+6)
    return wb


def q18():
    wb, ws = new_book("Comparing each row against one cell",
        "The average lives in a cell and the IF column points at it with an absolute "
        "reference. Without the $ the comparison walks off the end of the data.")
    rows=[("North",41.2),("South",38.6),("Creek",44.8),("Home",36.1),("Rented",39.9)]
    put(ws,4,1,"Farm average",font=f_bold)
    put(ws,4,2,"=AVERAGE(B7:B11)",fill=lock_fill,fmt=TWO,align=centre)
    header(ws,6,["Field","Yield (bu/ac)","Vs average","The formula in C"])
    for i,(n,y) in enumerate(rows):
        r=7+i
        put(ws,r,1,n); put(ws,r,2,y,fmt=ONE,align=centre)
        put(ws,r,3,f'=IF(B{r}>$B$4,"Above","Below")',fill=lock_fill,align=centre)
        put(ws,r,4,f"={FT}(C{r})",font=f_form)
    last=6+len(rows)
    stat(ws,last+2,"Fields above average",f'=COUNTIF(C7:C{last},"Above")',INT)
    note(ws,last+4,
        "Two of five, because Creek's 44.8 pulls the average up above three of the "
        "other four. An average is not a midpoint. Drop the $ signs and the reference "
        "slides down with the fill, so by the last row it compares against an empty "
        "cell -- which Excel reads as 0, and every yield beats 0.",4)
    finish(ws,[("A",20),("B",14),("C",12),("D",30)],last+4)
    return wb


def q19():
    wb, ws = new_book("Each field's share of the farm",
        "Bushels over the farm total, with the total locked so the formula fills. The "
        "share column answers a different question than the yield column.")
    rows=[("Aspen",164,48.3),("Bluff",287,44.1),("Coulee",103,52.6),
          ("Dugout",341,39.8),("Eastside",205,46.5)]
    header(ws,4,["Field","Acres","Yield (bu/ac)","Bushels","Share","The formula in E"])
    for i,(n,a,y) in enumerate(rows):
        r=5+i
        put(ws,r,1,n); put(ws,r,2,a,fmt=INT,align=centre); put(ws,r,3,y,fmt=ONE,align=centre)
        put(ws,r,4,f"=B{r}*C{r}",fill=lock_fill,fmt="#,##0.0",align=centre)
        put(ws,r,5,f"=D{r}/$D$10",fill=lock_fill,fmt=PCT1,align=centre)
        put(ws,r,6,f"={FT}(E{r})",font=f_form)
    last=4+len(rows)
    put(ws,last+1,1,"Total",font=f_bold)
    put(ws,last+1,2,f"=SUM(B5:B{last})",font=f_bold,fill=lock_fill,fmt=INT,align=centre)
    put(ws,last+1,4,f"=SUM(D5:D{last})",font=f_bold,fill=lock_fill,fmt="#,##0.0",align=centre)
    put(ws,last+1,5,f"=SUM(E5:E{last})",font=f_bold,fill=lock_fill,fmt=PCT1,align=centre)
    note(ws,last+3,
        "The share column has to total 100%. Dugout holds the largest share at 27.6% "
        "on the worst yield of the five; Coulee has the best yield and the smallest "
        "share. Share is about how much of the farm's production a field accounts for.",6)
    finish(ws,[("A",14),("B",10),("C",14),("D",12),("E",10),("F",24)],last+3)
    return wb


def q20():
    wb, ws = new_book("Dates are numbers wearing a format",
        "Real dates sit right-aligned and can be subtracted. Format one as General "
        "and the serial number underneath is visible.")
    rows=[("2026-08-27",51.4),("2026-09-04",46.9),("2026-09-11",58.3),
          ("2026-09-25",44.2),("2026-10-06",53.7)]
    header(ws,4,["Date","Tonnes","Days since previous","The formula in C"])
    for i,(d,t) in enumerate(rows):
        r=5+i
        put(ws,r,1,dt.date.fromisoformat(d),fmt="DD-MMM-YY",align=centre)
        put(ws,r,2,t,fmt=ONE,align=centre)
        if i:
            put(ws,r,3,f"=A{r}-A{r-1}",fill=lock_fill,fmt=INT,align=centre)
            put(ws,r,4,f"={FT}(C{r})",font=f_form)
    last=4+len(rows)
    stat(ws,last+2,"Span, first to last",f"=A{last}-A5",INT)
    stat(ws,last+3,"Total tonnes",f"=SUM(B5:B{last})",ONE)
    stat(ws,last+4,"Average load",f"=AVERAGE(B5:B{last})",ONE)
    put(ws,last+6,1,"The first date as a plain number",font=f_bold)
    put(ws,last+6,3,"=A5",fill=lock_fill,fmt=INT,align=centre)
    note(ws,last+8,
        "46,261 -- days since 30 December 1899. If the dates had arrived as text they "
        "would sit left in their cells and the Days column would return #VALUE!, "
        "because text cannot be subtracted.",4)
    finish(ws,[("A",14),("B",12),("C",20),("D",26)],last+8)
    return wb


def q21():
    wb, ws = new_book("Three scenarios from one formula",
        "Fields down, seeding rates across. The acres reference locks its column and "
        "the rate reference locks its row, so one formula fills the whole grid.")
    put(ws,4,1,"Seed price ($/lb)",font=f_bold); put(ws,4,2,1.85,fill=lock_fill,fmt=MONEY,align=centre)
    fields=[("North",120),("South",240),("Creek",95)]
    rates=[("Low",2.4),("Mid",2.9),("High",3.5)]
    put(ws,6,1,"Field",font=f_head); put(ws,6,2,"Acres",font=f_head)
    for j,(s,rt) in enumerate(rates):
        put(ws,6,3+j,s,font=f_head,align=centre); put(ws,7,3+j,rt,fmt=ONE,align=centre)
    for i,(n,a) in enumerate(fields):
        r=8+i
        put(ws,r,1,n); put(ws,r,2,a,fmt=INT,align=centre)
        for j in range(len(rates)):
            put(ws,r,3+j,f"=$B{r}*{chr(67+j)}$7",fill=lock_fill,fmt="#,##0.0",align=centre)
    last=7+len(fields)
    put(ws,last+1,1,"Total lb",font=f_bold)
    for j in range(len(rates)):
        col=chr(67+j)
        put(ws,last+1,3+j,f"=SUM({col}8:{col}{last})",font=f_bold,fill=lock_fill,fmt="#,##0.0",align=centre)
        put(ws,last+2,3+j,f"={col}{last+1}*$B$4",fill=lock_fill,fmt=MONEY,align=centre)
    put(ws,last+2,1,"Seed cost",font=f_bold)
    put(ws,last+4,1,"The one formula",font=f_bold)
    put(ws,last+4,3,f"={FT}(C8)",font=f_form)
    note(ws,last+6,
        "1,092.0 / 1,319.5 / 1,592.5 lb, costing $2,020.20 / $2,441.08 / $2,946.13. "
        "One formula covers all nine cells, so changing an acre figure or a rate "
        "updates everything at once.",6)
    finish(ws,[("A",18),("B",12),("C",12),("D",12),("E",12),("F",20)],last+6)
    return wb


def q22():
    wb, ws = new_book("A threshold the formula reads rather than holds",
        "COUNTIF can point its criterion at a cell if you join the operator on with "
        "&. Then changing the threshold is one edit, not several.")
    put(ws,4,1,"Threshold (bu/ac)",font=f_bold); put(ws,4,2,50.0,fill=lock_fill,fmt=ONE,align=centre)
    rows=[("Bin A",58.2),("Bin B",44.7),("Bin C",61.9),("Bin D",39.4),
          ("Bin E",55.0),("Bin F",47.8),("Bin G",63.1),("Bin H",41.2)]
    first,last=table(ws,6,["Bin","Yield (bu/ac)"],rows,{1:ONE})
    rng=f"B{first}:B{last}"
    stat(ws,last+2,"Count above the threshold",f'=COUNTIF({rng},">"&$B$4)',INT)
    stat(ws,last+3,"Fraction above",f'=COUNTIF({rng},">"&$B$4)/COUNT({rng})',PCT0)
    stat(ws,last+4,"Average of all bins",f"=AVERAGE({rng})",TWO)
    note(ws,last+6,
        "Four of eight at a threshold of 50, three at 55. The & is what makes it read "
        "the cell: anything inside quotation marks is treated as literal text, so "
        '">$B$4" would look for that string rather than a comparison.',4)
    finish(ws,[("A",26),("B",14),("C",14),("D",30)],last+6)
    return wb


def q23():
    wb, ws = new_book("Three columns, three formats",
        "Tonnes, a price, and a dollar amount are all plain numbers. The formatting "
        "is what tells a reader which is which.")
    rows=[("Canola",412.6,15.30),("Wheat",688.2,9.85),("Barley",524.9,7.40)]
    header(ws,4,["Crop","Tonnes","Price ($/t)","Revenue","Share","The formula in D"])
    for i,(c,t,p) in enumerate(rows):
        r=5+i
        put(ws,r,1,c); put(ws,r,2,t,fmt=ONE,align=centre); put(ws,r,3,p,fmt=MONEY,align=centre)
        put(ws,r,4,f"=B{r}*C{r}",fill=lock_fill,fmt=MONEY0,align=centre)
        put(ws,r,5,f"=D{r}/$D$8",fill=lock_fill,fmt=PCT1,align=centre)
        put(ws,r,6,f"={FT}(D{r})",font=f_form)
    last=4+len(rows)
    put(ws,last+1,1,"Total",font=f_bold)
    put(ws,last+1,2,f"=SUM(B5:B{last})",font=f_bold,fill=lock_fill,fmt=ONE,align=centre)
    put(ws,last+1,4,f"=SUM(D5:D{last})",font=f_bold,fill=lock_fill,fmt=MONEY,align=centre)
    note(ws,last+3,
        "Barley delivers 524.9 tonnes against canola's 412.6 but earns $3,884 against "
        "$6,313, because its price is less than half. One decimal for a weight, a "
        "dollar sign and two decimals for a rate, whole dollars for a total.",6)
    finish(ws,[("A",14),("B",12),("C",14),("D",14),("E",10),("F",24)],last+3)
    return wb


def q24():
    wb, ws = new_book("ROUND changes the value; formatting changes the look",
        "The same five yields shown two ways. The proof of the difference is that the "
        "two columns total differently.")
    rows=[("Plot 1",42.47),("Plot 2",38.93),("Plot 3",51.28),("Plot 4",45.61),("Plot 5",39.75)]
    header(ws,4,["Plot","Yield (stored)","Yield (formatted)","ROUND to 1 dp","The formula in D"])
    for i,(n,y) in enumerate(rows):
        r=5+i
        put(ws,r,1,n)
        put(ws,r,2,y,fmt=TWO,align=centre)
        put(ws,r,3,y,fmt=ONE,align=centre)
        put(ws,r,4,f"=ROUND(B{r},1)",fill=lock_fill,fmt=ONE,align=centre)
        put(ws,r,5,f"={FT}(D{r})",font=f_form)
    last=4+len(rows)
    put(ws,last+1,1,"Total",font=f_bold)
    for col in ("B","C","D"):
        put(ws,last+1,ord(col)-64,f"=SUM({col}5:{col}{last})",font=f_bold,
            fill=lock_fill,fmt=TWO,align=centre)
    note(ws,last+3,
        "Columns B and C hold identical values and display differently; both total "
        "218.04. Column D holds different values and totals 218.10. A formatted column "
        "shows numbers that do not add up to its own total, which reads as an error.",5)
    finish(ws,[("A",14),("B",16),("C",18),("D",14),("E",26)],last+3)
    return wb


def q25():
    wb, ws = new_book("Where the brackets go",
        "Revenue and cost are both per acre, so they have to be netted before the "
        "result is scaled by acres. Multiplication happens first unless you say otherwise.")
    put(ws,4,1,"Price ($/bu)",font=f_bold); put(ws,4,2,14.20,fill=lock_fill,fmt=MONEY,align=centre)
    put(ws,5,1,"Input cost ($/ac)",font=f_bold); put(ws,5,2,212.50,fill=lock_fill,fmt=MONEY,align=centre)
    put(ws,6,1,"Landlord share",font=f_bold); put(ws,6,2,0.25,fill=lock_fill,fmt=PCT0,align=centre)
    rows=[("North",41.2,120),("South",38.6,240),("Creek",44.8,95)]
    header(ws,8,["Field","Yield (bu/ac)","Acres","Net to farmer","Net per acre","The formula in D"])
    for i,(n,y,a) in enumerate(rows):
        r=9+i
        put(ws,r,1,n); put(ws,r,2,y,fmt=ONE,align=centre); put(ws,r,3,a,fmt=INT,align=centre)
        put(ws,r,4,f"=(B{r}*$B$4-$B$5)*C{r}*(1-$B$6)",fill=lock_fill,fmt=MONEY,align=centre)
        put(ws,r,5,f"=(B{r}*$B$4-$B$5)*(1-$B$6)",fill=lock_fill,fmt=MONEY,align=centre)
        put(ws,r,6,f"={FT}(D{r})",font=f_form)
    last=8+len(rows)
    put(ws,last+1,1,"Total",font=f_bold)
    put(ws,last+1,4,f"=SUM(D9:D{last})",font=f_bold,fill=lock_fill,fmt=MONEY,align=centre)
    put(ws,last+3,1,"The formula without brackets",font=f_bold)
    put(ws,last+3,4,"=B9*$B$4-$B$5*C9*(1-$B$6)",fill=lock_fill,fmt=MONEY,align=centre)
    put(ws,last+3,6,f"={FT}(D{last+3})",font=f_form)
    note(ws,last+5,
        "-$18,539.96 for North. Without the brackets Excel subtracts the input cost for "
        "the whole field from the revenue of a single acre. Anything that must be netted "
        "before it is scaled has to be bracketed.",6)
    finish(ws,[("A",22),("B",14),("C",10),("D",16),("E",14),("F",30)],last+5)
    return wb


def q26():
    wb, ws = new_book("Seven trucks, four usable weights",
        "Two blanks and one 'rejected' mean none of the counts equals seven. Each "
        "function answers a different question about the same column.")
    rows=[("Load 1",24.8),("Load 2",None),("Load 3",31.2),("Load 4","rejected"),
          ("Load 5",28.6),("Load 6",None),("Load 7",26.4)]
    header(ws,4,["Load","Tonnes"])
    for i,(n,v) in enumerate(rows):
        r=5+i
        put(ws,r,1,n)
        put(ws,r,2,v,fmt=ONE if isinstance(v,float) else None,
            align=centre if isinstance(v,float) else None)
    last=4+len(rows)
    rng=f"B5:B{last}"
    for k,(lab,f,fmt) in enumerate([("COUNT (numbers)",f"=COUNT({rng})",INT),
            ("COUNTA (anything)",f"=COUNTA({rng})",INT),("SUM",f"=SUM({rng})",ONE),
            ("AVERAGE",f"=AVERAGE({rng})",TWO),
            ("AVERAGE x COUNT",f"=AVERAGE({rng})*COUNT({rng})",ONE)]):
        stat(ws,last+2+k,lab,f,fmt)
    note(ws,last+8,
        "COUNT 4, COUNTA 5, SUM 111.0, AVERAGE 27.75. AVERAGE times COUNT returns the "
        "SUM, which is the check. COUNTA is the wrong tool for 'how many loads were "
        "weighed' -- it counts the word 'rejected' as an entry.",4)
    finish(ws,[("A",20),("B",14),("C",14),("D",30)],last+8)
    return wb


def q27():
    wb, ws = new_book("Percentage change against dollar change",
        "A 26-cent move on fuel is a bigger percentage than $151 off fertilizer, "
        "because percentage change measures against where the number started.")
    rows=[("Fuel",1.42,1.68),("Fertilizer",892.00,741.00),("Seed",64.50,71.20),
          ("Chemical",38.90,38.90),("Insurance",22.40,25.80)]
    header(ws,4,["Input","2025 ($)","2026 ($)","Change ($)","% change","The formula in E"])
    for i,(n,a,b) in enumerate(rows):
        r=5+i
        put(ws,r,1,n); put(ws,r,2,a,fmt=MONEY,align=centre); put(ws,r,3,b,fmt=MONEY,align=centre)
        put(ws,r,4,f"=C{r}-B{r}",fill=lock_fill,fmt=MONEY,align=centre)
        put(ws,r,5,f"=(C{r}-B{r})/B{r}",fill=lock_fill,fmt=PCT1,align=centre)
        put(ws,r,6,f"={FT}(E{r})",font=f_form)
    last=4+len(rows)
    note(ws,last+2,
        "Fuel +18.3% on 26 cents; fertilizer -16.9% on $151. Chemical returns 0.0%, "
        "which is a real answer -- the numerator is zero -- not a missing value. Use "
        "percentages when the starting values differ in size, dollars when you need to "
        "know what it costs.",6)
    finish(ws,[("A",16),("B",12),("C",12),("D",12),("E",12),("F",26)],last+2)
    return wb


def q28():
    wb, ws = new_book("A blended application rate",
        "Total pounds over total acres. The plain average of the four rates sits "
        "higher because the heaviest rates are on the smallest fields.")
    rows=[("Field 1",86,3.4),("Field 2",142,2.9),("Field 3",64,4.1),("Field 4",119,3.2)]
    header(ws,4,["Field","Acres","Rate (lb/ac)","Pounds","The formula in D"])
    for i,(n,a,rt) in enumerate(rows):
        r=5+i
        put(ws,r,1,n); put(ws,r,2,a,fmt=INT,align=centre); put(ws,r,3,rt,fmt=ONE,align=centre)
        put(ws,r,4,f"=B{r}*C{r}",fill=lock_fill,fmt="#,##0.0",align=centre)
        put(ws,r,5,f"={FT}(D{r})",font=f_form)
    last=4+len(rows)
    put(ws,last+1,1,"Total",font=f_bold)
    put(ws,last+1,2,f"=SUM(B5:B{last})",font=f_bold,fill=lock_fill,fmt=INT,align=centre)
    put(ws,last+1,4,f"=SUM(D5:D{last})",font=f_bold,fill=lock_fill,fmt="#,##0.0",align=centre)
    stat(ws,last+3,"Blended: pounds / acres",f"=D{last+1}/B{last+1}",TWO,5)
    stat(ws,last+4,"Blended: SUMPRODUCT",f"=SUMPRODUCT(B5:B{last},C5:C{last})/SUM(B5:B{last})",TWO,5)
    stat(ws,last+5,"AVERAGE of the rate column",f"=AVERAGE(C5:C{last})",TWO,5)
    note(ws,last+7,
        "3.28 lb/ac blended against a plain average of 3.40. Order on the total -- "
        "1,347.4 lb -- because that is the amount of product the farm actually needs.",5)
    finish(ws,[("A",24),("B",12),("C",14),("D",12),("E",30)],last+7)
    return wb


def q29():
    wb, ws = new_book("A delivery sheet, formatted so it reads",
        "Dates, weights and dollars are all numbers. The formats are what let a reader "
        "tell them apart without checking the headings.")
    rows=[("2026-09-03","Canola",34.6,15.30),("2026-09-11","Canola",41.2,15.30),
          ("2026-09-19","Wheat",52.8,9.85),("2026-09-28","Wheat",47.1,9.85),
          ("2026-10-05","Barley",63.4,7.40)]
    header(ws,4,["Date","Crop","Tonnes","Price ($/t)","Value","The formula in E"])
    for i,(d,c,t,p) in enumerate(rows):
        r=5+i
        put(ws,r,1,dt.date.fromisoformat(d),fmt="DD-MMM-YY",align=centre)
        put(ws,r,2,c); put(ws,r,3,t,fmt=ONE,align=centre); put(ws,r,4,p,fmt=MONEY,align=centre)
        put(ws,r,5,f"=C{r}*D{r}",fill=lock_fill,fmt=MONEY,align=centre)
        put(ws,r,6,f"={FT}(E{r})",font=f_form)
    last=4+len(rows)
    put(ws,last+1,1,"Total",font=f_bold)
    put(ws,last+1,3,f"=SUM(C5:C{last})",font=f_bold,fill=lock_fill,fmt=ONE,align=centre)
    put(ws,last+1,5,f"=SUM(E5:E{last})",font=f_bold,fill=lock_fill,fmt=MONEY,align=centre)
    stat(ws,last+3,"Canola deliveries",f'=COUNTIF(B5:B{last},"Canola")',INT,6)
    stat(ws,last+4,"Canola tonnes",f'=SUMIF(B5:B{last},"Canola",C5:C{last})',ONE,6)
    stat(ws,last+5,"Days, first to last",f"=A{last}-A5",INT,6)
    note(ws,last+7,
        "239.1 tonnes worth $2,612.92 over 32 days. All three number columns are "
        "right-aligned, which is itself the signal that Excel read them as numbers "
        "rather than text.",6)
    finish(ws,[("A",14),("B",12),("C",10),("D",14),("E",14),("F",26)],last+7)
    return wb


def q30():
    wb, ws = new_book("Four formulas, one right",
        "The same intended calculation written four ways. Only the first brackets the "
        "netting before the scaling.")
    put(ws,4,1,"Price ($/bu)",font=f_bold); put(ws,4,2,14.20,fill=lock_fill,fmt=MONEY,align=centre)
    put(ws,5,1,"Input cost ($/ac)",font=f_bold); put(ws,5,2,212.50,fill=lock_fill,fmt=MONEY,align=centre)
    header(ws,7,["Field","Yield (bu/ac)","Acres"])
    put(ws,8,1,"Creek"); put(ws,8,2,44.8,fmt=ONE,align=centre); put(ws,8,3,95,fmt=INT,align=centre)
    header(ws,10,["","Formula","Result","Right?"])
    variants=[("Correct","=($B$8*$B$4-$B$5)*$C$8",
               "Nets revenue against cost per acre, then scales by acres."),
              ("No brackets","=$B$8*$B$4-$B$5*$C$8",
               "Subtracts the whole field's cost from one acre's revenue."),
              ("Brackets misplaced","=$B$8*($B$4-$B$5)*$C$8",
               "Subtracts the cost from the price -- $14.20 less $212.50."),
              ("Cost charged twice","=($B$8*$B$4-$B$5)*$C$8-$B$5",
               "Right, except the per-acre cost is charged once more at the end.")]
    for i,(lab,f,why) in enumerate(variants):
        r=11+i
        put(ws,r,1,lab,font=f_bold if i==0 else f_body)
        put(ws,r,2,f,fill=lock_fill,fmt=MONEY,align=centre)
        put(ws,r,3,f"={FT}(B{r})",font=f_form)
        put(ws,r,4,why,font=f_note)
    note(ws,16,
        "$40,247.70 / -$19,551.34 / -$843,964.80 / $40,035.20. A net return of minus "
        "eight hundred thousand dollars on 95 acres is not a rounding problem -- check "
        "the magnitude before trusting a column of these.",4)
    finish(ws,[("A",22),("B",30),("C",30),("D",44)],16)
    return wb


BUILDERS = [(6,q6),(7,q7),(8,q8),(9,q9),(10,q10),(11,q11),(12,q12),(13,q13),
            (14,q14),(15,q15),(16,q16),(17,q17),(18,q18),(19,q19),(20,q20),
            (21,q21),(22,q22),(23,q23),(24,q24),(25,q25),(26,q26),(27,q27),
            (28,q28),(29,q29),(30,q30)]

if __name__ == "__main__":
    for n, fn in BUILDERS:
        print("   ", save(fn(), n))
