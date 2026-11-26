# -*- coding: utf-8 -*-
import re, sys, html
D=sys.argv[1]
p=D+'/word/document.xml'
x=open(p,encoding='utf-8').read()
RPR='<w:rPr><w:rFonts w:cs="Times New Roman"/><w:lang w:val="es-ES"/></w:rPr>'
def runs(t, extra=''):
    # *italic*, **bold**
    out=[]
    for part in re.split(r'(\*\*[^*]+\*\*|\*[^*]+\*)', t):
        if not part: continue
        b=i=False
        if part.startswith('**'): b=True; part=part[2:-2]
        elif part.startswith('*'): i=True; part=part[1:-1]
        r='<w:rPr><w:rFonts w:cs="Times New Roman"/>'+('<w:b/>' if b else '')+('<w:i/>' if i else '')+extra+'<w:lang w:val="es-ES"/></w:rPr>'
        out.append(f'<w:r>{r}<w:t xml:space="preserve">{html.escape(part,quote=False)}</w:t></w:r>')
    return ''.join(out)
def P(t, style='RellenarREP', jc='both', after=None):
    sp=f'<w:spacing w:after="{after}"/>' if after is not None else '<w:spacing w:after="100"/>'
    return f'<w:p><w:pPr><w:pStyle w:val="{style}"/>{sp}<w:jc w:val="{jc}"/>{RPR}</w:pPr>{runs(t)}</w:p>'
def H(t, lvl):
    return f'<w:p><w:pPr><w:pStyle w:val="Ttulo{lvl}"/>{RPR}</w:pPr>{runs(t)}</w:p>'
def B(t):  # bullet-like paragraph with hanging indent
    return f'<w:p><w:pPr><w:pStyle w:val="RellenarREP"/><w:spacing w:after="60"/><w:ind w:left="360" w:hanging="220"/><w:jc w:val="both"/>{RPR}</w:pPr>{runs("– "+t)}</w:p>'

def para_end_containing(text, start=0):
    i=x.index(text,start); return x.index('</w:p>',i)+6
def para_start_containing(text, start=0):
    i=x.index(text,start); return x.rfind('<w:p ',0,i)

def replace_between(a,b,new):
    global x
    x=x[:a]+new+x[b:]

# ---------- INTRODUCCIÓN ----------
intro=[
P("La rata de agua (*Arvicola sapidus*) es un roedor semiacuático endémico del suroeste de Europa, presente en la península ibérica y parte de Francia. Vive ligada a ríos y arroyos con abundante vegetación herbácea en las orillas, de la que se alimenta y en la que encuentra refugio, y excava sus madrigueras en orillas blandas y de poca pendiente. En España, el Atlas y Libro Rojo de los Mamíferos Terrestres de España la clasificó como Vulnerable, estimando una regresión superior al 30 %, relacionada con la pérdida de calidad del hábitat y el efecto de especies introducidas (Palomo et al., 2007)."),
P("Entre esas especies introducidas destaca el visón americano (*Neogale vison*), un mustélido semiacuático que llegó al medio natural principalmente por escapes y liberaciones desde granjas peleteras y que está incluido en el Catálogo Español de Especies Exóticas Invasoras (Real Decreto 630/2013). En la Sierra de Francia (Salamanca), un estudio de la Universidad de Salamanca realizado entre 2006 y 2010 comprobó el impacto de esta especie sobre la rata de agua y el musgaño de Cabrera, que dejaron de aparecer en el 40 % de las localidades donde estaban presentes antes de la llegada del visón (García-Díaz et al., 2013)."),
P("La Estrategia de gestión, control y erradicación del visón americano en España (MAGRAMA, 2013) recomienda el trampeo en vivo mediante cajas de malla metálica colocadas sobre plataformas flotantes. Estas plataformas pueden incorporar planchas de huellas que permiten detectar la presencia del visón y localizar los puntos donde colocar las trampas. El procedimiento se organiza en tres fases: localización, erradicación y seguimiento. Este método se ha utilizado con éxito en diferentes ríos para reducir las poblaciones de visón y proteger a especies autóctonas como la rata de agua (Harrington et al., 2009; MAGRAMA, 2013)."),
P("En el río Francia, afluente del Alagón, las poblaciones de rata de agua que quedan se encuentran aisladas. Gran parte del cauce es rocoso, con orillas duras donde no puede excavar y con poca vegetación de ribera. Además, el visón americano está avanzando desde el Alagón y supone una amenaza para las poblaciones que todavía se mantienen. Por eso planteamos un proyecto que actúe a la vez sobre las dos causas principales de su declive: la falta de hábitat adecuado y la depredación por el visón. Actuar solo sobre una de ellas no es suficiente: si no hay hábitat, la especie no se recupera aunque se elimine el visón, y si el visón sigue presente, mejorar el hábitat no frena la depredación."),
P("Además, la rata de agua forma parte de las relaciones tróficas del ecosistema, por lo que su recuperación ayudaría a mantener las cadenas alimentarias naturales. Por otro lado, el control del visón americano también puede beneficiar a otras especies autóctonas sobre las que depreda, como el desmán ibérico y otros pequeños vertebrados ligados a los ríos (MAGRAMA, 2013)."),
P("**Beneficiarios.** Los beneficiarios directos son la Junta de Castilla y León, que dispondrá de datos actualizados para gestionar la especie; la Reserva de la Biosfera de las Sierras de Béjar y Francia; y la población local, por la mejora del estado ecológico del río."),
]
a=para_end_containing('beneficiarios. Fundamentar')
b=para_start_containing('Hipótesis y Objetivos')
replace_between(a,b,''.join(intro))

# ---------- HIPÓTESIS ----------
a=para_end_containing('Hipótesis y Objetivos')
hip=H('Hipótesis',2)+P("Si eliminamos el visón americano del río Francia y restauramos el hábitat ribereño a lo largo de sus 25 km, recuperando la vegetación de orilla y las orillas degradadas, la rata de agua podrá volver a ocupar zonas donde había desaparecido. Como resultado, esperamos que aumente el número de tramos ocupados respecto al inicio del proyecto.")
replace_between(a,a,hip)

# ---------- OBJETIVO GENERAL ----------
a=para_end_containing('>Objetivo general<')
b=para_start_containing('Objetivos específicos')
replace_between(a,b,P("Reducir el riesgo de extinción local de la rata de agua (*Arvicola sapidus*) en el río Francia, restaurando su hábitat ribereño y eliminando el visón americano en los 25 km del río durante dos años."))

# ---------- OBJETIVOS ESPECÍFICOS ----------
oes=[
P("**OE1. Restaurar el hábitat ribereño en todos los tramos de los 25 km del río Francia para favorecer la recuperación de las poblaciones de rata de agua.** Lo evaluaremos mediante la superficie de vegetación plantada, el aumento de la cobertura vegetal en las orillas, la supervivencia de las plantaciones (al menos un 70 % después del primer verano) y el número de tramos ocupados por la rata de agua al final del proyecto."),
P("**OE2. Eliminar el visón americano del río Francia sin afectar a la fauna autóctona.** Lo evaluaremos con el número de visones retirados, la ausencia de huellas y capturas de visón en la fase de seguimiento y el número de capturas de especies no objetivo, que deben liberarse todas sin daño."),
]
a=para_end_containing('coherentes con la metodología')
b=para_start_containing('>Metodología<')
replace_between(a,b,''.join(oes))

# ---------- METODOLOGÍA ----------
met=[
H('Área de estudio y diseño general',3),
P("El proyecto se desarrolla en los 25 km del río Francia, hasta su confluencia con el Alagón, durante dos años (mes 1 = enero de 2027). Dividimos el río en tramos de 500 m, que son la unidad de muestreo y de actuación. Las tareas manuales de la restauración y el seguimiento de la vegetación los realiza una empresa de restauración contratada, y nosotros los coordinamos. Para fijar las fechas tenemos en cuenta que la rata de agua cría aproximadamente de febrero a octubre, que julio–septiembre es la época más seca y que en pleno invierno hay heladas y crecidas."),
H('Objetivo 1. Restaurar el hábitat ribereño (OE1)',3),
B("**Tarea 1. Caracterización inicial y selección de tramos (meses 7–8; coordina Otto, participa Mireya).** Recorremos los 25 km del río en tramos de 500 m por ambas orillas. Registramos la cobertura y la altura de la vegetación de ribera, el tipo de sustrato, la pendiente de la orilla y la presencia de indicios de rata de agua, que en verano son más fáciles de detectar. Es un recorrido a pie que no altera la orilla. Con estos datos seleccionamos los tramos prioritarios."),
B("**Tarea 2. Compra de la planta autóctona (mes 9; coordina Mireya).** Encargamos al vivero de procedencia local la planta herbácea autóctona (carrizo, juncos, espadaña, lirio amarillo y cárices) un mes antes de la plantación."),
B("**Tarea 3. Retirada de elementos que degradan la orilla (mes 10; coordina Mireya, ejecuta la empresa).** La empresa retira escombros, materiales artificiales y restos de obras de las orillas de los tramos prioritarios, sin añadir sedimento ni modificar la orilla natural."),
B("**Tarea 4. Plantación de vegetación herbácea (meses 10–11; coordina Mireya, ejecuta la empresa).** La empresa planta las especies en islas y bandas longitudinales próximas al agua, en los tramos con escasa cobertura. Plantamos en octubre y noviembre porque el suelo ya está húmedo tras las primeras lluvias de otoño, la cría de la rata de agua termina y todavía no llegan las heladas."),
B("**Tarea 5. Instalación de refugios con restos leñosos (mes 11; coordina Mireya, ejecuta la empresa).** La empresa coloca troncos y ramas junto a las islas y en tramos con escasa cobertura natural, como refugio frente a los depredadores."),
B("**Tarea 6. Seguimiento de la vegetación y riego (meses 14–21; coordina Mireya, ejecuta la empresa).** La empresa revisa la supervivencia de las plantas desde el final del invierno y riega en el verano, que es cuando se pierden más plantas."),
B("**Tarea 7. Evaluación de la restauración (meses 20–21; coordina Otto, participa Mireya).** Repetimos el registro de la tarea 1 en los tramos restaurados y en tramos sin actuación para medir la cobertura vegetal y los indicios de rata de agua."),
B("**Tarea 8. Reposición de plantas perdidas (meses 22–23; coordina Mireya, ejecuta la empresa).** La empresa repone, en la misma época que la plantación, las plantas que no han sobrevivido según la evaluación."),
H('Objetivo 2. Eliminar el visón americano (OE2)',3),
P("Seguimos la metodología de la Estrategia de gestión, control y erradicación del visón americano en España (MAGRAMA, 2013), que recomienda el trampeo en vivo con cajas de reja en tres fases consecutivas: localización, eliminación y seguimiento. Salamanca está en la zona B, donde el trampeo puede hacerse durante todo el año; lo situamos en otoño, cuando los jóvenes de visón se dispersan y ha terminado la cría de la rata de agua."),
B("**Tarea 1. Autorización (meses 1–3; coordina Mario, participa Otto).** Solicitamos la autorización de trampeo a la Junta de Castilla y León y la de los trabajos en la orilla al organismo de cuenca."),
B("**Tarea 2. Localización del visón americano (meses 9–10; coordina Mario, participan Otto y Mireya).** Instalamos 50 planchas de huellas a lo largo de los 25 km del río, una cada 500 m y alternadas entre ambas orillas. Cada plancha es una superficie de unos 40 × 40 cm recubierta de arcilla húmeda o de un film con tinta, con un cebo de pescado en el centro, colocada sobre un soporte de madera en la orilla. Las revisamos cada semana, durante seis semanas, y registramos las huellas: distinguimos el visón de la nutria y de la rata de agua por el tamaño, la forma y la disposición de los dedos, comparándolas con una guía de rastros de mustélidos. Cada plancha con huellas de visón marca un punto donde colocar las trampas de la tarea 4."),
B("**Tarea 3. Fototrampeo de localización y seguimiento (meses 9–13 y 21–22; coordina Otto, participa Mireya).** Colocamos cámaras de fototrampeo en los puntos con más huellas de visón, junto a las planchas y las trampas. Las cámaras confirman la presencia del visón de forma visual, complementan las planchas de huellas y permiten comprobar si la rata de agua y otras especies autóctonas frecuentan los tramos restaurados."),
B("**Tarea 4. Instalación y revisión diaria de trampas selectivas (meses 10–11; coordina Mario, participan Otto y Mireya).** Adquirimos cajas-trampa de reja con excluidor de nutria (abertura de 6,5–7,5 cm y umbral de activación inferior a 400 g), instaladas sobre plataformas flotantes de madera. Colocamos 50 trampas (20 por cada 10 km), ancladas a la orilla y activas durante 30 días en noviembre. Las revisamos a diario por turnos entre los tres miembros del equipo, registramos las capturas y liberamos las especies no objetivo."),
B("**Tarea 5. Eliminación de los ejemplares capturados (mes 11; coordina Mario).** Los visones capturados se sacrifican el mismo día de la captura, en la revisión diaria de las trampas, mediante un procedimiento de eutanasia autorizado, como el dispositivo de bala cautiva, realizado por personal veterinario autorizado (de la Junta de Castilla y León o contratado como servicio puntual) y conforme al protocolo establecido por la administración competente."),
B("**Tarea 6. Seguimiento de la población de visón americano (meses 12–13 y 21–22; coordina Otto, participa Mario).** Justo después del trampeo repetimos los muestreos con planchas de huellas cada 500 m, con la metodología de la tarea 2 y revisiones semanales, y con las cámaras de la tarea 3, para comprobar la ausencia de visón. Lo repetimos un año después para detectar una posible recolonización desde el Alagón."),
H('Recursos',3),
P("Ya disponemos del GPS del Grado en Biología de la UAM y de equipos informáticos para la gestión de los datos. Troncos y ramas para los refugios se obtienen en la propia zona. El material que adquirimos (planchas de huellas, cajas-trampa, cámaras de fototrampeo y planta autóctona) y los servicios que contratamos (empresa de restauración y veterinario) se detallan en el presupuesto. El vehículo es particular de un miembro del equipo y se compensa a kilometraje (0,26 €/km, según el Real Decreto 462/2002 actualizado por la Orden HFP/793/2023)."),
H('Controles y análisis',3),
P("Para la restauración usamos como referencia los datos de la caracterización inicial (tarea 1) y comparamos los tramos restaurados con tramos de características parecidas en los que no actuamos (tarea 7). Para el visón comparamos el porcentaje de planchas con huellas en la fase de localización (tarea 2) y en las de seguimiento (tarea 6), y calculamos las capturas por trampa-noche, el número de capturas no objetivo y los registros de visón de las cámaras de fototrampeo. El análisis de los datos se hace al terminar la toma de datos de campo (meses 22–23)."),
]
a=para_end_containing('Describir metodología y tareas')
b=para_start_containing('Riesgos y plan de contingencia')
replace_between(a,b,''.join(met))

# ---------- TABLA DE RIESGOS ----------
rows=[
("Recolonización del área por visones procedentes de zonas próximas (amenaza)","Alta","Alto","Mantener las planchas de huellas en la confluencia con el Alagón tras el trampeo (tarea 5) y volver a trampear si aparecen indicios. Coordinarnos con otros proyectos de control de la zona."),
("Captura accidental de especies autóctonas por la dificultad técnica de un control selectivo (amenaza y debilidad)","Media","Alto","Cajas con excluidor de nutria y umbral de activación ajustado, revisión diaria y liberación inmediata de las especies no objetivo, con registro de cada caso."),
("Crecidas, riadas y variaciones estacionales del caudal (amenaza)","Media","Medio","Trampas sobre plataformas flotantes, retirada o desactivación ante previsión de crecida y reposición de las plantas perdidas."),
("Plazo de dos años limitado e información inicial insuficiente sobre la rata de agua (debilidad)","Media","Medio","Caracterización inicial de todos los tramos (tarea 1), indicadores medibles a corto plazo (cobertura vegetal, indicios de visón) y propuesta de seguimiento posterior."),
("Falta de continuidad futura del control (amenaza)","Media","Alto","Entregar los datos y el protocolo de trampeo a la Junta de Castilla y León y a las entidades locales para que el control se mantenga tras el proyecto."),
]
t0=x.index('<w:tbl>'); t1=x.index('</w:tbl>',t0)
tbl=x[t0:t1]
trs=re.findall(r'<w:tr[ >].*?</w:tr>',tbl,re.S)
assert len(trs)==6, len(trs)
newtrs=[trs[0]]
for tr,vals in zip(trs[1:],rows):
    tcs=re.findall(r'<w:tc>.*?</w:tc>',tr,re.S); assert len(tcs)==4
    nt=tr
    for tc,v in zip(tcs,vals):
        tcpr=re.search(r'<w:tcPr>.*?</w:tcPr>',tc,re.S).group(0)
        ppr=re.search(r'<w:pPr>.*?</w:pPr>',tc,re.S)
        ppr=ppr.group(0) if ppr else '<w:pPr></w:pPr>'
        ppr=re.sub(r'<w:rPr>.*?</w:rPr>','',ppr,flags=re.S); ppr=re.sub(r'<w:cnfStyle[^>]*/>','',ppr)
        ppr=ppr.replace('</w:pPr>','<w:spacing w:before="40" w:after="40"/><w:rPr><w:rFonts w:cs="Times New Roman"/><w:b w:val="0"/><w:sz w:val="18"/></w:rPr></w:pPr>')
        r=f'<w:r><w:rPr><w:rFonts w:cs="Times New Roman"/><w:b w:val="0"/><w:bCs w:val="0"/><w:color w:val="000000"/><w:sz w:val="18"/><w:lang w:val="es-ES"/></w:rPr><w:t xml:space="preserve">{html.escape(v,quote=False)}</w:t></w:r>'
        newtc=f'<w:tc>{tcpr}<w:p>{ppr}{r}</w:p></w:tc>'
        nt=nt.replace(tc,newtc,1)
    newtrs.append(nt)
newtbl=tbl
for o,n in zip(trs,newtrs): newtbl=newtbl.replace(o,n,1)
x=x[:t0]+newtbl+x[t1:]

# ---------- EQUIPO ----------
eq=[
P("Presentamos el proyecto desde el Grado en Biología de la Universidad Autónoma de Madrid, en colaboración con el Servicio Territorial de Medio Ambiente de Salamanca (Junta de Castilla y León), que autoriza el trampeo, y con la Reserva de la Biosfera de las Sierras de Béjar y Francia. La planta la suministra un vivero de la zona, y la retirada de elementos, la plantación, los refugios, el seguimiento de la vegetación y la reposición los realiza una empresa de restauración contratada."),
P("**Recursos disponibles.** GPS de la universidad y equipos informáticos para la gestión de los datos, la cartografía y el análisis estadístico."),
P("**Composición del equipo y funciones.** El equipo lo forman tres personas, que coordinan seis tareas cada una y se turnan en la revisión diaria de las trampas. Mireya Abad está contratada como bióloga a jornada completa de julio de 2027 a diciembre de 2028 (meses 7–24), que es el periodo en el que tiene tareas de campo de forma continua."),
B("**Mario Abad – coordinador general y del control del visón.** Autorización, localización con planchas de huellas, trampeo, eliminación de los ejemplares capturados, contrato de la bióloga y reuniones trimestrales."),
B("**Mireya Abad – bióloga contratada y coordinadora de la restauración.** Compra de la planta y coordinación y supervisión de la empresa en la retirada de elementos, la plantación, los refugios, el seguimiento de la vegetación y la reposición. Participa además en la caracterización, la evaluación, las planchas, el fototrampeo y el trampeo."),
B("**Otto Pérez – coordinador del seguimiento y de los datos.** Caracterización inicial, evaluación de la restauración, fototrampeo, seguimiento del visón, análisis de los resultados e informe final."),
H('Referencias',1),
P("García-Díaz, P., Arévalo, V., Vicente, R. y Lizana, M. (2013). The impact of the American mink (*Neovison vison*) on native vertebrates in mountainous streams in Central Spain. *European Journal of Wildlife Research*, 59, 823–831.", jc='left'),
P("Harrington, L. A., Harrington, A. L., Moorhouse, T., Gelling, M., Bonesi, L. y Macdonald, D. W. (2009). American mink control on inland rivers in southern England: an experimental test of a model strategy. *Biological Conservation*, 142(4), 839–849.", jc='left'),
P("MAGRAMA (2013). *Estrategia de gestión, control y erradicación del visón americano (Neovison vison) en España*. Ministerio de Agricultura, Alimentación y Medio Ambiente, Madrid.", jc='left'),
P("Palomo, L. J., Gisbert, J. y Blanco, J. C. (eds.) (2007). *Atlas y Libro Rojo de los Mamíferos Terrestres de España*. Dirección General para la Biodiversidad – SECEM – SECEMU, Madrid.", jc='left'),
P("Real Decreto 630/2013, de 2 de agosto, por el que se regula el Catálogo español de especies exóticas invasoras. *Boletín Oficial del Estado*, 185, de 3 de agosto de 2013.", jc='left'),
]
a=para_end_containing('composición, funciones')
b=x.index('<w:sectPr',a)
# keep any trailing paragraphs? replace the empty one(s)
replace_between(a,b,''.join(eq))
open(p,'w',encoding='utf-8').write(x)
sp=D+'/word/styles.xml'; st=open(sp,encoding='utf-8').read()
st=st.replace('<w:color w:val="306F7F"/></w:rPr></w:style>','<w:color w:val="000000"/></w:rPr></w:style>')
open(sp,'w',encoding='utf-8').write(st)
print('filled')
