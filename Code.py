# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""


import os

os.chdir(r"C:\Users\admin\Documents")
with open("New.xml","r") as f:
    content=f.read()


         
d=content.split("</Debts>")
v=d[0].split("</Debt>")
file1=[]
i=0
for elt in v:
    file1.append(v[i])
    i=i+1

file1[0]=file1[0].replace("<REPV>\n<Debts>\n<Debt>\n","")
del file1[-1]
j=1
while j<len(file1):
    file1[j]=file1[j].replace("\n<Debt>\n","")
    j=j+1
    
# ------------------------------------------------------------------------------------------------------   
t=d[1].split("</Eqties>")
a=t[0].split("</Eqty>")
file2=[]
i=0
for elt in a:
    file2.append(a[i])
    i=i+1

file2[0]=file2[0].replace("\n<Eqties>\n<Eqty>\n","")
del file2[-1]
j=1
while j<len(file2):
    file2[j]=file2[j].replace("\n<Eqty>\n","")
    j=j+1
    
#---------------------------------------------------------------------------------------------------------   
b=t[1].split("</CPNS>")
c=b[0].split("</CPN>")
file3=[]
i=0
for elt in c:
    file3.append(c[i])
    i=i+1
    
file3[0]=file3[0].replace("\n<CPNS>\n<CPN>\n","")
del file3[-1]
j=1
while j<len(file3):
    file3[j]=file3[j].replace("\n<CPN>\n","")
    j=j+1   

 
 #--------------------------------------------------------------------------------------------------------  
    
h=b[1].split("</RHTS>") 
e=h[0].split("</RHT>")
file4=[]
i=0
for elt in e:
    file4.append(e[i])
    i=i+1
   
file4[0]=file4[0].replace("\n<RHTS>\n<RHT>\n","")
del file4[-1]
j=1
while j<len(file4):
    file4[j]=file4[j].replace("\n<RHT>\n","")
    j=j+1    
  
    
 #----------------------------------------------------------------------------------------------------------
f=h[1].split("</MUFUNDS>") 
g=f[0].split("</MUFU>")
file5=[]
i=0
for elt in g:
   file5.append(g[i])
   i=i+1
   
file5[0]=file5[0].replace("\n<MUFUNDS>\n<MUFU>\n","")
del file5[-1]
j=1
while j<len(file5):
    file5[j]=file5[j].replace("\n<MUFU>\n","")
    j=j+1   


#-------------------------------------------------------------------------------------------------------------------------------------------
import pandas as pd
df=pd.DataFrame(columns=["INSTRID","INSTRTYPE","INSTRCTGRY","ENGPREFERREDNAME","ENGLONGNAME","ISSUERCD","ISSUECAPITAL","ISSUESIZE","ISSUEDT","MATURITYDT_L","PARVALUE","INTERESTTYPE","FORM","GUARANTEE","NEWPARVALUE","INTERESTPERIODCTY","INTERESTRATE","PRMYDTLSDUMMYDATE1","REDEMPTIONTYPE","AMORTFREQ","EXCHIND","MNEMONIQUE","AGENTID","PREFERREDNAMEREGISTRAR","PREFERREDNAMEISSUER","CouponPayDate","INSTRSTATUS"])


for j in range(len(file1)):
    tet=[]
    if "<CouponPayDates>" in file1[j]:
        X=file1[j].split("<CouponPayDates>")
        T=X[1].split("</CouponPayDates>")
        tt=X[0].split("\n")
        del (tt[-1])
        for i in tt:
            key_temp = i.split('<')[1]
            key = key_temp.split('>')[0]
            value = key_temp.split('>')[1].split('<')[0]
            tet.append(value)
        T[1]=T[1].replace("\n","")
        key_temp=T[1].split('<')[1]
        value = key_temp.split('>')[1].split('<')[0]
        tet.append(value)
        T[0]=T[0].replace("\n","")
        tot=[]
        F =  T[0].split("</CouponPayDate>")
        del(F[-1])
        for i in F:
            i=i.replace("<CouponPayDate>","")
            tot.append(i)
            CouponPayDate=tot
    else:
        file1[j]=file1[j].split("\n")
        del(file1[j][-1])
        for i in file1[j]:
            key_temp = i.split('<')[1]
            key = key_temp.split('>')[0]
            value = key_temp.split('>')[1].split('<')[0]
            tet.append(value)
        CouponPayDate=""
        tet.insert(-1,CouponPayDate)
    
    
    if CouponPayDate!="":
        for date in CouponPayDate:
            tet.insert(-1,date)
            df1=pd.DataFrame(data=[tet],columns=["INSTRID","INSTRTYPE","INSTRCTGRY","ENGPREFERREDNAME","ENGLONGNAME","ISSUERCD","ISSUECAPITAL","ISSUESIZE","ISSUEDT","MATURITYDT_L","PARVALUE","INTERESTTYPE","FORM","GUARANTEE","NEWPARVALUE","INTERESTPERIODCTY","INTERESTRATE","PRMYDTLSDUMMYDATE1","REDEMPTIONTYPE","AMORTFREQ","EXCHIND","MNEMONIQUE","AGENTID","PREFERREDNAMEREGISTRAR","PREFERREDNAMEISSUER","CouponPayDate","INSTRSTATUS"])
            df=df.append(df1)
            del(tet[-2])
    else:
        df1=pd.DataFrame(data=[tet],columns=["INSTRID","INSTRTYPE","INSTRCTGRY","ENGPREFERREDNAME","ENGLONGNAME","ISSUERCD","ISSUECAPITAL","ISSUESIZE","ISSUEDT","MATURITYDT_L","PARVALUE","INTERESTTYPE","FORM","GUARANTEE","NEWPARVALUE","INTERESTPERIODCTY","INTERESTRATE","PRMYDTLSDUMMYDATE1","REDEMPTIONTYPE","AMORTFREQ","EXCHIND","MNEMONIQUE","AGENTID","PREFERREDNAMEREGISTRAR","PREFERREDNAMEISSUER","CouponPayDate","INSTRSTATUS"])
        df=df.append(df1)
 
#-------------------------------------------------------------------------------------------------------------------------------------

dfx=pd.DataFrame(columns=["INSTRID","INSTRTYPE","INSTRCTGRY","ENGPREFERREDNAME","ENGLONGNAME","ISSUERCD","ISSUEDT","PARVALUE","ISSUESIZE","FORM","EXCHIND","MNEMONIQUE","AGENTID","PREFERREDNAMEREGISTRAR","PREFERREDNAMEISSUER","CLOSEPRICE","STREETADDRESS","MOBILENO"])


for j in range(len(file2)):
    tet=[]
    file2[j]=file2[j].replace(";","")
    tt=file2[j].split("\n")
    for i in range(len(tt)-1):
        if tt[i].startswith('<') is not True:
            tot=(tt[i-1],tt[i])
            tt[i-1]="".join(tot)
            del(tt[i])
    if tt[0]=="":
        del(tt[0])
    if tt[-1]=='':
        del(tt[-1])
    for i in tt:
        key_temp = i.split('<')[1]
        key = key_temp.split('>')[0]
        value = key_temp.split('>')[1].split('<')[0]
        tet.append(value)
    df2=pd.DataFrame(data=[tet],columns=["INSTRID","INSTRTYPE","INSTRCTGRY","ENGPREFERREDNAME","ENGLONGNAME","ISSUERCD","ISSUEDT","PARVALUE","ISSUESIZE","FORM","EXCHIND","MNEMONIQUE","AGENTID","PREFERREDNAMEREGISTRAR","PREFERREDNAMEISSUER","CLOSEPRICE","STREETADDRESS","MOBILENO"])
    dfx=dfx.append(df2)
       
#-------------------------------------------------------------------------------------------------------------------------------------------------     

dfy=pd.DataFrame(columns=["INSTRID","INSTRTYPE","INSTRCTGRY","ENGPREFERREDNAME","ENGLONGNAME","FORM","ISSUESIZE","ISSUEDT","ISSUERCD","MNEMONIQUE","AGENTID","PREFERREDNAMEREGISTRAR","PREFERREDNAMEISSUER","BASESECURITYID"])


for j in range(len(file3)):
    tet=[]
    tt=file3[j].split("\n")
    if tt[0]=="":
        del(tt[0])
    if tt[-1]=='':
        del(tt[-1])
    for i in tt:
        key_temp = i.split('<')[1]
        key = key_temp.split('>')[0]
        value = key_temp.split('>')[1].split('<')[0]
        tet.append(value)
    df3=pd.DataFrame(data=[tet],columns=["INSTRID","INSTRTYPE","INSTRCTGRY","ENGPREFERREDNAME","ENGLONGNAME","FORM","ISSUESIZE","ISSUEDT","ISSUERCD","MNEMONIQUE","AGENTID","PREFERREDNAMEREGISTRAR","PREFERREDNAMEISSUER","BASESECURITYID"])
    dfy=dfy.append(df3)



#-----------------------------------------------------------------------------------------------------------------------------------------
dfz=pd.DataFrame(columns=["INSTRID","INSTRTYPE","INSTRCTGRY","ENGPREFERREDNAME","ENGLONGNAME","FORM","ISSUESIZE","ISSUEDT","ISSUERCD","MNEMONIQUE","AGENTID","PREFERREDNAMEREGISTRAR","PREFERREDNAMEISSUER","BASEQUANTITY","DISBURSEDQUANTITY"])


for j in range(len(file4)):
    tet=[]
    tt=file4[j].split("\n")
    if tt[0]=="":
        del(tt[0])
    if tt[-1]=='':
        del(tt[-1])
    for i in tt:
        key_temp = i.split('<')[1]
        key = key_temp.split('>')[0]
        value = key_temp.split('>')[1].split('<')[0]
        tet.append(value)
    df4=pd.DataFrame(data=[tet],columns=["INSTRID","INSTRTYPE","INSTRCTGRY","ENGPREFERREDNAME","ENGLONGNAME","FORM","ISSUESIZE","ISSUEDT","ISSUERCD","MNEMONIQUE","AGENTID","PREFERREDNAMEREGISTRAR","PREFERREDNAMEISSUER","BASEQUANTITY","DISBURSEDQUANTITY"])
    dfz=dfz.append(df4)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
    
dfb=pd.DataFrame(columns=["INSTRID","INSTRTYPE","INSTRCTGRY","ENGPREFERREDNAME","ENGLONGNAME","ISSUESIZE","ISSUEDT","ISSUERCD","FUNDFAMILY","NAVCOMPFREQ","DISTRIBUTIONPOLICY","MNEMONIQUE","AGENTID","PREFERREDNAMEREGISTRAR","CLOSEPRICE","PREFERREDNAMEISSUER"])


for j in range(len(file5)):
    tet=[]
    tt=file5[j].split("\n")
    if tt[0]=="":
        del(tt[0])
    if tt[-1]=='':
        del(tt[-1])
    for i in tt:
        key_temp = i.split('<')[1]
        key = key_temp.split('>')[0]
        value = key_temp.split('>')[1].split('<')[0]
        tet.append(value)
    df5=pd.DataFrame(data=[tet],columns=["INSTRID","INSTRTYPE","INSTRCTGRY","ENGPREFERREDNAME","ENGLONGNAME","ISSUESIZE","ISSUEDT","ISSUERCD","FUNDFAMILY","NAVCOMPFREQ","DISTRIBUTIONPOLICY","MNEMONIQUE","AGENTID","PREFERREDNAMEREGISTRAR","CLOSEPRICE","PREFERREDNAMEISSUER"])
    dfb=dfb.append(df5)


#-----------------------------------------------------------------------------------------------------------------

with pd.ExcelWriter(r'C:\Users\admin\Desktop\Travail du stage.xlsx') as writer:  
     df.to_excel(writer, sheet_name='OBL_ORDN')
     dfx.to_excel(writer, sheet_name='ACT_ORD')
     dfy.to_excel(writer, sheet_name='COUP_INTR')
     dfz.to_excel(writer, sheet_name='DROIT_ATTRIB')
     dfb.to_excel(writer, sheet_name='FCP')

















