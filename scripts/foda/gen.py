import html as H
SUB="Proyecto RIPARIA-GEN · Conservación de la rata de agua (Arvicola sapidus) en el río Francia"
FORT=["Proyecto con objetivos concretos y un área de estudio delimitada",
 "Enfoque dual que combina el control de especies invasoras con la conservación de fauna autóctona",
 "Beneficios adicionales de la restauración de la vegetación ribereña para otras especies"]
OPOR=["Marco legal favorable a la gestión de especies exóticas invasoras",
 "Disponibilidad de estudios científicos y experiencia previa sobre el visón americano",
 "Posibilidad de colaborar con entidades locales y organismos de conservación",
 "Potencial para adaptar la metodología a otros ríos y especies amenazadas"]
DEBI=["Dificultad técnica para controlar selectivamente al visón americano sin afectar a otras especies",
 "Limitaciones temporales para restaurar el hábitat y evaluar sus resultados en dos años",
 "Información insuficiente sobre la distribución y el estado poblacional actual de la rata de agua",
 "Dificultad para atribuir el declive poblacional exclusivamente a la depredación por el visón"]
AMEN=["Recolonización del área por visones procedentes de zonas próximas",
 "Riesgo de captura accidental de especies autóctonas durante las actuaciones de control",
 "Crecidas, riadas y variaciones estacionales del caudal",
 "Falta de continuidad futura del control"]
G_F=dict(hdr="#3f6b38",fill="#eef4ea",tx="#26491f"); G_O=dict(hdr="#2b8793",fill="#e4f2f4",tx="#154e57")
G_D=dict(hdr="#b0892b",fill="#f8f1db",tx="#6c5112"); G_A=dict(hdr="#b2673a",fill="#f8eae1",tx="#79441f")
Q=[("FORTALEZAS","internas · favorables",FORT,G_F),("OPORTUNIDADES","externas · favorables",OPOR,G_O),
   ("DEBILIDADES","internas · desfavorables",DEBI,G_D),("AMENAZAS","externas · desfavorables",AMEN,G_A)]
e=lambda s:H.escape(s,quote=True)
def wrap(t,m):
    o=[];c=""
    for w in t.split():
        if len(c)+len(w)+(1 if c else 0)<=m: c=(c+" "+w).strip()
        else: o.append(c); c=w
    if c:o.append(c)
    return o
ML=92;MR=50;gap=34;cw=640;W=ML+2*cw+gap+MR;hdr=46;px=22;pt=60;lh=17;bg=11;MAXC=84
allw=[[wrap(b,MAXC) for b in q[2]] for q in Q]
ch=max(pt+sum(len(l)*lh for l in w)+bg*(len(w)-1)+20 for w in allw)
col_y=120;r1=col_y+22;r2=r1+ch+gap;Hc=r2+ch+60
xs=[ML,ML+cw+gap];pos=[(xs[0],r1),(xs[1],r1),(xs[0],r2),(xs[1],r2)]
o=[f'<rect width="{W}" height="{Hc}" fill="#fff"/>'];d=[]
F='font-family="Lato, Arial, sans-serif"'
for i,((n,t,b,pl),(x,y)) in enumerate(zip(Q,pos)):
    d.append(f'<clipPath id="c{i}"><rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="11"/></clipPath>')
    o.append(f'<g clip-path="url(#c{i})"><rect x="{x}" y="{y}" width="{cw}" height="{ch}" fill="{pl["fill"]}"/><rect x="{x}" y="{y}" width="{cw}" height="{hdr}" fill="{pl["hdr"]}"/></g>')
    o.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="11" fill="none" stroke="{pl["hdr"]}" stroke-width="1.6"/>')
    o.append(f'<text x="{x+px}" y="{y+29}" {F} font-size="17" font-weight="900" letter-spacing="1" fill="#fff">{n}</text>')
    o.append(f'<text x="{x+cw-px}" y="{y+29}" text-anchor="end" {F} font-size="11.5" font-style="italic" fill="#fff">{t}</text>')
    cy=y+pt
    for l in allw[i]:
        o.append(f'<circle cx="{x+px+3}" cy="{cy-4}" r="3" fill="{pl["hdr"]}"/>')
        for k,ln in enumerate(l): o.append(f'<text x="{x+px+14}" y="{cy+k*lh}" {F} font-size="13" fill="{pl["tx"]}">{e(ln)}</text>')
        cy+=len(l)*lh+bg
o.append(f'<text x="{ML}" y="34" {F} font-size="27" font-weight="800" letter-spacing="1.5" fill="#132a28">MATRIZ FODA</text>')
o.append(f'<text x="{ML}" y="58" {F} font-size="13.5" fill="#5d6b68">{e(SUB)}</text>')
for x,t in [(xs[0],"FACTORES INTERNOS  ·  DEL PROYECTO"),(xs[1],"FACTORES EXTERNOS  ·  DEL ENTORNO")]:
    o.append(f'<text x="{x+cw/2}" y="{col_y+8}" text-anchor="middle" {F} font-size="12.5" font-weight="800" letter-spacing="2" fill="#6b7673">{t}</text>')
for yc,t,c in [(r1+ch/2,"FAVORABLES  (+)","#3f6b38"),(r2+ch/2,"DESFAVORABLES  (−)","#b2673a")]:
    o.append(f'<text x="34" y="{yc}" transform="rotate(-90 34 {yc})" text-anchor="middle" {F} font-size="12" font-weight="800" letter-spacing="2.5" fill="{c}">{t}</text>')
o.append(f'<text x="{W-MR}" y="{Hc-22}" text-anchor="end" {F} font-size="11.5" fill="#8b9693">Redacción y Ejecución de Proyectos (REP) · Grado en Biología · UAM</text>')
svg=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {Hc}" width="{W}" height="{Hc}"><defs>{"".join(d)}</defs>'+"".join(o)+'</svg>'
open('/home/user/otto/Matriz-FODA-RIPARIA-GEN.svg','w').write(svg)
open('/tmp/claude-0/-home-user-otto/d29c33c2-598e-5dc8-bce0-9a1627727064/scratchpad/foda/w.html','w').write("<!doctype html><html><head><meta charset='utf-8'><style>@import url('https://fonts.googleapis.com/css2?family=Lato:wght@400;700;800;900&display=swap');html,body{margin:0}svg{width:100%;height:auto;display:block}</style></head><body>"+svg+"</body></html>")
print(W,Hc)
