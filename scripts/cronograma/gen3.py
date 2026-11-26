# -*- coding: utf-8 -*-
import html as H
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
R=lambda a,b:list(range(a,b+1))
blocks=[
 ("Objetivo 1 · Restaurar el hábitat ribereño","548235","dcefe2",[
  ("T1.1 Caracterización inicial y selección de tramos","Otto","Mireya",R(7,8)),
  ("T1.2 Compra de planta autóctona (encargo al vivero)","Mireya","Vivero",[9]),
  ("T1.3 Retirada de elementos que degradan la orilla","Mireya","Empresa",[10]),
  ("T1.4 Plantación de vegetación herbácea","Mireya","Empresa",R(10,11)),
  ("T1.5 Instalación de refugios con restos leñosos","Mireya","Empresa",[11]),
  ("T1.6 Seguimiento de la vegetación y riego","Mireya","Empresa",R(14,21)),
  ("T1.7 Evaluación de la restauración (indicios de rata)","Otto","Mireya",R(20,21)),
  ("T1.8 Reposición de plantas perdidas","Mireya","Empresa",R(22,23))]),
 ("Objetivo 2 · Eliminar el visón americano","C55A11","f6e5db",[
  ("T2.1 Autorización (Junta CyL y organismo de cuenca)","Mario","Otto",R(1,3)),
  ("T2.2 Localización del visón (planchas de huellas)","Mario","Otto, Mireya",R(9,10)),
  ("T2.3 Fototrampeo (localización y seguimiento)","Otto","Mireya",R(9,13)+R(21,22)),
  ("T2.4 Instalación y revisión diaria de trampas","Mario","Otto, Mireya",R(10,11)),
  ("T2.5 Eliminación de los ejemplares capturados","Mario","Veterinario autorizado",[11]),
  ("T2.6 Seguimiento de la población de visón","Otto","Mario",R(12,13)+R(21,22))]),
 ("Gestión del proyecto","2F5597","e1eaf2",[
  ("Contrato de la bióloga (Mireya Abad, jornada completa)","Mario","—",R(7,24)),
  ("Reuniones de coordinación (trimestrales)","Mario","Mireya, Otto",[3,6,9,12,15,18,21,24]),
  ("Análisis de datos y de resultados","Otto","Mario",R(22,23)),
  ("Informe final y difusión de resultados","Otto","Mario, Mireya",R(23,24))]),
]
notas=[
 "Mes 1 = enero de 2027. Coordinan 6 tareas cada uno: Mario (autorización, trampeo, gestión), Mireya (trabajos de restauración que ejecuta la empresa) y Otto (caracterización, fototrampeo, seguimiento, análisis e informe). La revisión diaria de las trampas se hace por turnos entre los tres.",
 "Mireya Abad está contratada como bióloga de julio de 2027 a diciembre de 2028 (meses 7–24), el periodo en el que tiene tareas de campo de forma continua. Las tareas manuales de la restauración y el seguimiento de la vegetación los hace una empresa de restauración.",
 "La rata de agua cría aprox. de febrero a octubre. La caracterización (jul–ago) solo recorre las orillas; los trabajos en la orilla (oct–nov) y el trampeo (nov) se hacen al final de la cría, con el suelo húmedo tras las primeras lluvias y antes de las heladas de invierno.",
 "El visón se localiza en septiembre–octubre, cuando los jóvenes se dispersan, y el seguimiento sigue de forma consecutiva al trampeo, como pide la Estrategia nacional; se repite un año después (sep–oct de 2028) para comprobar que no ha vuelto. El análisis empieza al terminar la toma de datos.",
]
MES=["E","F","M","A","M","J","J","A","S","O","N","D"]
# ---------------- Excel ----------------
wb=Workbook(); ws=wb.active; ws.title="Cronograma"
A=lambda **k:Font(name="Arial",**k)
thin=Side(style="thin",color="BFBFBF"); B=Border(left=thin,right=thin,top=thin,bottom=thin)
FM=4; last=FM+23
ws["A1"]="Cronograma del proyecto RIPARIA-GEN"; ws["A1"].font=A(size=14,bold=True)
ws["A2"]="Conservación de la rata de agua (Arvicola sapidus) en el río Francia (Salamanca) · 24 meses (enero 2027 – diciembre 2028)"; ws["A2"].font=A(size=9,italic=True,color="595959")
for c,t in [(1,"Tarea"),(2,"Coordina"),(3,"Participa")]:
    ws.cell(4,c,t); ws.merge_cells(start_row=4,start_column=c,end_row=6,end_column=c)
ws.merge_cells(start_row=4,start_column=FM,end_row=4,end_column=FM+11); ws.cell(4,FM,"Año 1 · 2027")
ws.merge_cells(start_row=4,start_column=FM+12,end_row=4,end_column=last); ws.cell(4,FM+12,"Año 2 · 2028")
for m in range(1,25):
    ws.cell(5,FM+m-1,MES[(m-1)%12]); ws.cell(6,FM+m-1,m)
for r in (4,5,6):
    for c in range(1,last+1):
        cell=ws.cell(r,c); cell.border=B
        cell.font=A(bold=True,size=9 if r!=6 else 8,color="FFFFFF" if (r==4 and c>=FM) else "000000")
        cell.alignment=Alignment(horizontal="center" if c>1 else "left",vertical="center",wrap_text=True)
        cell.fill=PatternFill("solid",fgColor="1F4E5A" if (r==4 and c>=FM) else "D9E1E2")
r=7
for title,dark,light,rows in blocks:
    ws.cell(r,1,title)
    for c in range(1,last+1):
        cell=ws.cell(r,c); cell.fill=PatternFill("solid",fgColor=dark); cell.font=A(bold=True,size=9,color="FFFFFF"); cell.border=B
    r+=1
    for lab,co,pa,ms in rows:
        ws.cell(r,1,lab); ws.cell(r,2,co); ws.cell(r,3,pa)
        for c in range(1,last+1):
            cell=ws.cell(r,c); cell.border=B; cell.font=A(size=9)
            cell.alignment=Alignment(horizontal="left" if c==1 else "center",vertical="center",wrap_text=(c==3))
            if c>=FM and (c-FM+1) in ms: cell.fill=PatternFill("solid",fgColor=dark)
        r+=1
ws.column_dimensions["A"].width=50; ws.column_dimensions["B"].width=10; ws.column_dimensions["C"].width=22
for m in range(24): ws.column_dimensions[L(FM+m)].width=3.6
r+=1
for n in notas:
    ws.cell(r,1,n).font=A(size=8,italic=True,color="404040"); r+=1
ws.sheet_view.showGridLines=False; ws.freeze_panes=ws.cell(7,FM)
ws.page_setup.paperSize=ws.PAPERSIZE_A4; ws.page_setup.orientation="landscape"
ws.page_setup.fitToWidth=1; ws.page_setup.fitToHeight=1; ws.sheet_properties.pageSetUpPr.fitToPage=True
ws.print_area=f"A1:{L(last)}{r}"
ws.page_margins.left=ws.page_margins.right=0.4; ws.page_margins.top=ws.page_margins.bottom=0.4
wb.save("/home/user/otto/Cronograma-RIPARIA-GEN.xlsx")
# ---------------- HTML/PDF ----------------
h=['<tr><th class="tl" rowspan="3">Tarea</th><th class="co" rowspan="3">Coordina</th><th class="pa" rowspan="3">Participa</th><th colspan="12" class="yr">Año 1 · 2027</th><th colspan="12" class="yr">Año 2 · 2028</th></tr>']
h.append('<tr>'+''.join(f'<th class="m{" sep" if i==13 else ""}">{MES[(i-1)%12]}</th>' for i in range(1,25))+'</tr>')
h.append('<tr>'+''.join(f'<th class="n{" sep" if i==13 else ""}">{i}</th>' for i in range(1,25))+'</tr>')
for title,dark,light,rows in blocks:
    h.append(f'<tr class="hdr"><td colspan="27" style="background:#{dark}">{H.escape(title)}</td></tr>')
    for lab,co,pa,ms in rows:
        cells=''.join(f'<td class="c{" sep" if m==13 else ""}" style="{"background:#"+dark if m in ms else ""}"></td>' for m in range(1,25))
        h.append(f'<tr><td class="lab" style="background:#{light}">{H.escape(lab)}</td><td class="p">{H.escape(co)}</td><td class="p">{H.escape(pa)}</td>{cells}</tr>')
nh=''.join(f'<li>{H.escape(n)}</li>' for n in notas)
doc=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Cronograma RIPARIA-GEN</title><style>
@import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700;900&display=swap');
@page{{size:A4 landscape;margin:9mm 10mm}}
body{{font-family:Lato,Arial,sans-serif;color:#1d2b2e;margin:0;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
h1{{font-size:18pt;margin:0;color:#132a28;font-weight:900}} .sub{{color:#5d6b68;font-size:9pt;margin:2px 0 8px}}
table{{border-collapse:collapse;width:100%;table-layout:fixed}} th,td{{border:1px solid #d5dcdc;font-size:8pt}}
th.tl{{width:30%;text-align:left;padding:3px 6px;background:#f1f4f4}} th.co{{width:6%;background:#f1f4f4}} th.pa{{width:12%;background:#f1f4f4}}
th.yr{{background:#24434a;color:#fff;padding:3px;font-size:8.5pt}} th.m{{background:#f1f4f4;padding:1px 0;font-weight:700}} th.n{{background:#f1f4f4;font-size:6pt;color:#7a8787;font-weight:400;padding:0}}
td.lab{{padding:3px 6px;line-height:1.15}} td.p{{padding:2px 4px;text-align:center;font-size:7.4pt;line-height:1.1}} td.c{{height:17px}}
.sep{{border-left:2px solid #24434a}} tr.hdr td{{color:#fff;font-weight:900;padding:3px 6px;font-size:8.6pt}}
ul{{margin:7px 0 0;padding-left:15px;font-size:7.6pt;color:#3b4744;line-height:1.3}} li{{margin:1px 0}}
</style></head><body><h1>Cronograma del proyecto</h1>
<p class="sub">Proyecto RIPARIA-GEN · Conservación de la rata de agua (<i>Arvicola sapidus</i>) en el río Francia (Salamanca) · 24 meses (enero 2027 – diciembre 2028)</p>
<table>{"".join(h)}</table><ul>{nh}</ul></body></html>'''
open('/home/user/otto/Cronograma-RIPARIA-GEN.html','w',encoding='utf-8').write(doc)
print('ok')
