# -*- coding: utf-8 -*-
import json,sys
sys.path.insert(0,'/tmp/claude-0/-home-user-otto/d29c33c2-598e-5dc8-bce0-9a1627727064/scratchpad/presu')
from items3 import T,F,S,PE,V,PEND
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
A=lambda **k: Font(name="Arial",**k)
thin=Side(style="thin",color="BFBFBF"); B=Border(left=thin,right=thin,top=thin,bottom=thin)
wb=Workbook(); pp=wb.active; pp.title="Parámetros"
params=[("Distancia Madrid – río Francia, ida y vuelta (km)",600),("Indemnización por vehículo particular (€/km)",0.26),
 ("Dieta de manutención (€/persona y día)",37.40),("Dieta de alojamiento (€/persona y noche)",65.97),
 ("Km por día de campo en la zona",60),("Salario bruto anual de la bióloga (€)",24000),
 ("Cuota empresarial a la Seguridad Social",0.33),("Costes indirectos (fracción de los costes directos)",0.20)]
pp["A1"]="Parámetros"; pp["A1"].font=A(bold=True,size=12)
REF={}; val=[]
for i,(n,v) in enumerate(params):
    r=3+i; pp.cell(r,1,n).font=A(); pp.cell(r,2,v).font=A(color="0000FF"); REF[i]=f"Parámetros!$B${r}"; val.append(v)
pp.column_dimensions["A"].width=50
PF={"KMV":(f"={REF[0]}*{REF[1]}",val[0]*val[1]),"KML":(f"={REF[4]}*{REF[1]}",val[4]*val[1]),"MAN":(f"={REF[2]}",val[2]),"ALO":(f"={REF[3]}",val[3]),"SAL":(f"={REF[5]}/12*(1+{REF[6]})",val[5]/12*(1+val[6]))}
ws=wb.create_sheet("Presupuesto por tareas")
for i,h in enumerate(["Elemento","Tienda","Cantidad","Precio unitario (€)","Total (€)","Enlace"],1):
    c=ws.cell(1,i,h); c.font=A(bold=True); c.fill=PatternFill("solid",fgColor="EDEDED"); c.border=B
r=2; subs=[]; out=[]
for code,name,items in T:
    ws.cell(r,1,f"{code} {name}" if code!="Gestión" else name).font=A(bold=True); r+=1; first=r; jl=[]
    for el,tipo,q,un,pr,shop,url in items:
        f,pv=PF[pr] if isinstance(pr,str) else (pr,pr)
        ws.cell(r,1,el); ws.cell(r,2,shop); ws.cell(r,3,q); ws.cell(r,4,f); ws.cell(r,5,f"=C{r}*D{r}")
        if url: c=ws.cell(r,6,url); c.hyperlink=url; c.font=A(size=9,color="0563C1",underline="single")
        for cc in range(1,6): ws.cell(r,cc).font=A(size=10)
        for cc in range(1,7): ws.cell(r,cc).border=B
        ws.cell(r,4).number_format=ws.cell(r,5).number_format='#,##0.00'
        if shop==PEND:
            for cc in (2,4,5): ws.cell(r,cc).fill=PatternFill("solid",fgColor="FFF2CC")
        jl.append({"el":el,"tipo":tipo,"q":q,"u":un,"p":pv,"shop":shop,"url":url}); r+=1
    ws.cell(r,1,"Total").font=A(bold=True); ws.cell(r,5,f"=SUM(E{first}:E{r-1})").font=A(bold=True); ws.cell(r,5).number_format='#,##0.00'
    subs.append((f"{code} {name}" if code!="Gestión" else name,r)); out.append({"code":code,"name":name,"items":jl}); r+=2
last=r
for col,w in zip("ABCDEF",[58,26,10,16,12,60]): ws.column_dimensions[col].width=w
rs=wb.create_sheet("Resumen",0); rs["A1"]="Resumen del presupuesto"; rs["A1"].font=A(bold=True,size=12)
rr=3
for t,row in subs:
    rs.cell(rr,1,t); rs.cell(rr,2,f"='Presupuesto por tareas'!E{row}").number_format='#,##0.00'; rr+=1
rs.cell(rr,1,"Total costes directos").font=A(bold=True); rs.cell(rr,2,f"=SUM(B3:B{rr-1})").number_format='#,##0.00'; td=rr; rr+=1
rs.cell(rr,1,"Costes indirectos (20 %)"); rs.cell(rr,2,f"=B{td}*{REF[7]}").number_format='#,##0.00'; ci=rr; rr+=1
rs.cell(rr,1,"PRESUPUESTO TOTAL").font=A(bold=True); rs.cell(rr,2,f"=B{td}+B{ci}").number_format='#,##0.00 "€"'
rs.column_dimensions["A"].width=70; rs.column_dimensions["B"].width=16
wb.save('/home/user/otto/Presupuesto-RIPARIA-GEN.xlsx')
json.dump({"tareas":out,"val":val},open('/tmp/claude-0/-home-user-otto/d29c33c2-598e-5dc8-bce0-9a1627727064/scratchpad/presu/data3.json','w',encoding='utf-8'),ensure_ascii=False)
print('ok')
