# -*- coding: utf-8 -*-
# (elemento, tipo, cantidad, unidad, precio, tienda, url)
F,S,PE,V="Material","Servicio","Personal","Viajes y dietas"
LM="Leroy Merlin"; DEC="Decathlon"; PEND="Presupuesto pendiente"
u={
"gps":"https://www.klarna.com/es/shopping/pl/cl288/3205158795/GPS/Garmin-eTrex-SE/",
"cinta":"https://www.leroymerlin.es/productos/cinta-metrica-stanley-60-metros-13870262.html",
"flex":"https://www.leroymerlin.es/productos/flexometro-5mx19mm-82263640.html",
"clino":"https://emea.suunto.com/products/suunto-pm-5-360-pc-clinometer",
"pvc":"https://www.leroymerlin.es/productos/tubo-de-pvc-presion-de-20-mm-y-2-5-m-12400332.html",
"poste":"https://www.leroymerlin.es/productos/poste-cuadrado-de-madera-clase-iii-7-x-7-x-100-cm-natural-cerland-16368275.html",
"spray":"https://www.leroymerlin.fr/produits/bombe-de-peinture-marquage-sol-luxens-orange-mat-82991015.html",
"libreta":"https://www.alpinstore.com/es/583983-rite-in-the-rain-cuaderno-todo-tiempo-de-18-cm-amarillo.html",
"folios":"https://www.chollometro.com/ofertas/paquete-de-500-hojas-simpl-ver-las-2-fotos-del-chollo-1987221",
"lapices":"https://www.ofertitas.es/pack-12-lapices-staedtler-noris-120-hb/1164731/",
"nitrilo":"https://finditapp.es/product/250963/100-guantes-desechables-de-nitrilo-carrefour--pm---azul",
"botas":"https://www.decathlon.es/es/deportes/caza/botas-de-agua",
"botiquin":"https://www.decathlon.es/es/deportes/montana/botiquin-trekking-senderismo",
"km":"https://www.boe.es/boe/dias/2023/07/17/pdfs/BOE-A-2023-16462.pdf",
"dieta":"https://www.boe.es/buscar/act.php?id=BOE-A-2002-10337",
"contenedor":"https://www.habitissimo.es/presupuestos/retirar-escombros",
"alambre":"https://www.leroymerlin.es/productos/alambre-de-acero-de-50-m-de-longitud-y-0-7-mm-de-12165020.html",
"correos":"https://www.correos.es/es/es/particulares/enviar/envios-nacionales/burofax-cartas/carta/carta-certificada",
"tab4080":"https://www.leroymerlin.es/productos/tablero-de-contrachapado-crudo-40x80x1-cm-anchoxaltoxgrosor-10901485.html",
"arcilla":"https://www.leroymerlin.es/productos/arcilla-gris-5l-para-0-5-m2-16239615.html",
"arena":"https://www.obramat.es/productos/arena-fina-0-2-mm-25-kg-10269070.html",
"sardina":"https://www.merca2.es/2026/01/30/cena-boost-omega-3-sardinas-2347769/",
"cuerda":"https://www.leroymerlin.es/productos/cuerda-de-polipropileno-de-25-m-y-85-kg-de-carga-util-15888236.html",
"taladro":"https://www.compradiccion.com/herramientas/ofertas-herramientas-dexter-leroy-merlin-taladros-amoladoras-sierras-atornilladores-a-mejor-precio",
"serrucho":"https://www.leroymerlin.es/productos/serrucho-300-mm-bellota-213402.html",
"cam":"https://www.decathlon.es/es/electronica-deportiva/tienda-camaras",
"cable":"https://www.leroymerlin.es/productos/cable-antirrobo-con-llave-de-8-mm-de-y-1-8-m-de-longitud-13254514.html",
"sd":"https://www.pccomponentes.com/sandisk-ultra-microsdhc-32gb-uhs-i-clase-10-plus-adaptador-sd",
"pilas":"https://www.ofertitas.es/chollo-pack-pilas-alcalinas-baratas/14639/",
"jaula":"https://www.ebay.de/itm/276213381611",
"malla":"https://www.leroymerlin.es/productos/malla-metalica-electrosoldada-de-acero-decomet60-0-6x10m-12820584.html",
"tab122":"https://www.leroymerlin.es/productos/tablero-de-contrachapado-crudo-122x244x0-5-cm-anchoxaltoxgrosor-18896752.html",
"xps":"https://www.leroymerlin.es/productos/10-uds-de-aislante-de-poliestireno-extruido-xps-danosa-danopren-tl-40-1-25x0-6m-espesor-40mm-r-1-2-97179945.html",
"cuero":"https://www.leroymerlin.es/productos/guantes-juba-flor-vacuno-hps1lt-t10-85788757.html",
"linterna":"https://www.decathlon.es/es/deportes/camping/accessorios",
"lejia":"https://finditapp.es/supermercado/aldi/lejia",
"vet":"https://caser.es/documents/473773/14251649/tarifario-actos-veterinarios-plan-salud.pdf",
"ocu":"https://www.ocu.org/alimentacion/mascotas/consejos/muerte-de-mascotas",
"seguro":"https://www.ucm.es/seguro-de-accidentes",
"boli":"https://www.chollometro.com/ofertas/bic-cristal-soft-boligrafos-bolitas-punta-media-12-mm-con-tinta-easy-glide-azul-caja-de-carton-de-10-1999812",
"moo":"https://www.moo.com/es/flyers/a5",
}
def viajes(v,m,a,k):
    o=[]
    if v: o.append(("Desplazamiento Madrid – río Francia (ida y vuelta, 600 km)",V,v,"viaje","KMV","BOE (0,26 €/km)",u["km"]))
    if k: o.append(("Kilometraje en la zona de trabajo (60 km/día)",V,k,"día","KML","BOE (0,26 €/km)",u["km"]))
    if m: o.append(("Dieta de manutención",V,m,"persona-día","MAN","BOE (RD 462/2002)",u["dieta"]))
    if a: o.append(("Dieta de alojamiento",V,a,"persona-noche","ALO","BOE (RD 462/2002)",u["dieta"]))
    return o
T=[
("T1.1","Caracterización inicial y selección de tramos",[
 ("GPS de mano Garmin eTrex SE",F,1,"ud",115.00,"Powerplanetonline",u["gps"]),
 ("Cinta métrica Stanley de 60 m",F,1,"ud",31.99,LM,u["cinta"]),
 ("Flexómetro de 5 m",F,2,"ud",1.99,LM,u["flex"]),
 ("Clinómetro Suunto PM-5",F,1,"ud",135.46,"Suunto",u["clino"]),
 ("Tubo de PVC de 20 mm y 2,5 m (cuadrados de muestreo)",F,2,"ud",2.01,LM,u["pvc"]),
 ("Poste de madera tratada 7 × 7 × 100 cm (marcar tramos)",F,50,"ud",6.49,LM,u["poste"]),
 ("Spray de marcaje",F,2,"ud",9.99,LM,u["spray"]),
 ("Libreta impermeable Rite in the Rain",F,2,"ud",21.95,"Alpinstore",u["libreta"]),
 ("Paquete de 500 folios A4 (fichas de campo)",F,1,"ud",4.19,"Carrefour",u["folios"]),
 ("Pack de 12 lápices Staedtler con goma y afilador",F,1,"ud",4.99,"Amazon",u["lapices"]),
 ("Guantes de nitrilo (caja de 100)",F,1,"caja",6.99,"Carrefour",u["nitrilo"]),
 ("Botas de agua",F,3,"par",14.99,DEC,u["botas"]),
 ("Botiquín de primeros auxilios",F,1,"ud",13.99,DEC,u["botiquin"]),
]+viajes(2,20,16,10)),
("T1.2","Compra de planta autóctona",[
 ("Carrizo (Phragmites australis), en alveolo",F,500,"planta",1.56,"Floraccess (maceta 9 cm)","https://www.floraccess.com/en/product/80420/phragmites-australis/"),
 ("Junco (Juncus spp.), en alveolo",F,500,"planta",1.56,"Floraccess (maceta 9 cm)","https://www.floraccess.com/en/product/80420/phragmites-australis/"),
 ("Espadaña (Typha spp.), en alveolo",F,300,"planta",1.56,"Floraccess (maceta 9 cm)","https://www.floraccess.com/en/product/80420/phragmites-australis/"),
 ("Lirio amarillo (Iris pseudacorus), en alveolo",F,200,"planta",1.56,"Floraccess (maceta 9 cm)","https://www.floraccess.com/en/product/80420/phragmites-australis/"),
 ("Cárices (Carex spp.), en alveolo",F,500,"planta",1.56,"Floraccess (maceta 9 cm)","https://www.floraccess.com/en/product/80420/phragmites-australis/"),
]),
("T1.3","Retirada de elementos que degradan la orilla",[
 ("Empresa de restauración: peones",S,16,"jornada",160,"Tarifas Tragsa 2026 (BOE)","https://boe.es/boe/dias/2026/04/28/pdfs/BOE-A-2026-9265.pdf"),
 ("Alquiler de contenedor de escombros (5 m³, una semana)",S,1,"ud",250,"Habitissimo",u["contenedor"]),
]+viajes(1,3,2,3)),
("T1.4","Plantación de vegetación herbácea",[
 ("Empresa de restauración: plantación manual",S,2000,"planta",1.20,"Tarifas Tragsa 2026 (BOE)","https://boe.es/boe/dias/2026/04/28/pdfs/BOE-A-2026-9265.pdf"),
]+viajes(2,6,4,6)),
("T1.5","Instalación de refugios con restos leñosos",[
 ("Empresa de restauración: colocación de refugios",S,4,"jornada",160,"Tarifas Tragsa 2026 (BOE)","https://boe.es/boe/dias/2026/04/28/pdfs/BOE-A-2026-9265.pdf"),
 ("Poste de madera tratada 7 × 7 × 100 cm (fijar troncos)",F,30,"ud",6.49,LM,u["poste"]),
 ("Alambre galvanizado (50 m)",F,1,"rollo",2.29,LM,u["alambre"]),
]+viajes(1,2,1,2)),
("T1.6","Seguimiento de la vegetación y riego",[
 ("Empresa de restauración: visitas de seguimiento",S,8,"visita",150,"Tarifas Tragsa 2026 (BOE)","https://boe.es/boe/dias/2026/04/28/pdfs/BOE-A-2026-9265.pdf"),
 ("Empresa de restauración: riego de apoyo en verano",S,4,"riego",250,"Tarifas Tragsa 2026 (BOE)","https://boe.es/boe/dias/2026/04/28/pdfs/BOE-A-2026-9265.pdf"),
]+viajes(4,4,0,4)),
("T1.7","Evaluación de la restauración",[
 ("Paquete de 500 folios A4 (fichas de campo)",F,1,"ud",4.19,"Carrefour",u["folios"]),
]+viajes(2,16,12,8)),
("T1.8","Reposición de plantas perdidas",[
 ("Planta autóctona de reposición, en alveolo",F,400,"planta",1.56,"Floraccess (maceta 9 cm)","https://www.floraccess.com/en/product/80420/phragmites-australis/"),
 ("Empresa de restauración: plantación de reposición",S,400,"planta",1.20,"Tarifas Tragsa 2026 (BOE)","https://boe.es/boe/dias/2026/04/28/pdfs/BOE-A-2026-9265.pdf"),
]+viajes(1,3,2,3)),
("T2.1","Autorización de la Junta de Castilla y León y del organismo de cuenca",[
 ("Envío por carta certificada de las solicitudes",F,2,"envío",5.74,"Correos",u["correos"]),
]),
("T2.2","Localización del visón con planchas de huellas",[
 ("Tablero contrachapado 40 × 80 cm (base y tejadillo)",F,50,"ud",8.99,LM,u["tab4080"]),
 ("Arcilla gris (5 L)",F,16,"bolsa",5.39,LM,u["arcilla"]),
 ("Arena fina (25 kg)",F,2,"saco",1.10,"Obramat",u["arena"]),
 ("Poste de madera tratada 7 × 7 × 100 cm (soporte)",F,50,"ud",6.49,LM,u["poste"]),
 ("Cuerda de polipropileno (25 m)",F,4,"rollo",4.29,LM,u["cuerda"]),
 ("Sardina fresca (cebo)",F,15,"kg",4.00,"Supermercado (precio medio)",u["sardina"]),
 ("Taladro atornillador Dexter a batería",F,1,"ud",69.99,LM,u["taladro"]),
 ("Serrucho Bellota de 300 mm",F,1,"ud",16.99,LM,u["serrucho"]),
 ("Paquete de 500 folios A4 (fichas de revisión)",F,1,"ud",4.19,"Carrefour",u["folios"]),
]+viajes(7,21,18,9)),
("T2.3","Fototrampeo de localización y seguimiento",[
 ("Cámara de fototrampeo Solognac 100 SD",F,10,"ud",74.99,DEC,u["cam"]),
 ("Cable antirrobo con llave (1,8 m)",F,10,"ud",11.31,LM,u["cable"]),
 ("Tarjeta microSD SanDisk Ultra 32 GB",F,20,"ud",9.99,"PcComponentes",u["sd"]),
 ("Pilas AA alcalinas Varta (pack de 40)",F,12,"pack",8.99,"Amazon",u["pilas"]),
]),
("T2.4","Instalación y revisión diaria de trampas",[
 ("Jaula trampa de captura viva galvanizada (61 × 20 × 20 cm)",F,50,"ud",23.96,"VEVOR (eBay)",u["jaula"]),
 ("Malla electrosoldada 0,6 × 10 m (excluidores de nutria)",F,2,"rollo",19.79,LM,u["malla"]),
 ("Tablero contrachapado 122 × 244 cm (plataformas)",F,13,"ud",40.99,LM,u["tab122"]),
 ("Planchas de poliestireno extruido (pack de 10, flotadores)",F,5,"pack",65.92,LM,u["xps"]),
 ("Cuerda de polipropileno (25 m, amarres)",F,20,"rollo",4.29,LM,u["cuerda"]),
 ("Poste de madera tratada 7 × 7 × 100 cm (anclaje)",F,50,"ud",6.49,LM,u["poste"]),
 ("Sardina fresca (cebo)",F,25,"kg",4.00,"Supermercado (precio medio)",u["sardina"]),
 ("Guantes de cuero Juba",F,3,"par",2.59,LM,u["cuero"]),
 ("Guantes de nitrilo (caja de 100)",F,1,"caja",6.99,"Carrefour",u["nitrilo"]),
 ("Linterna frontal Quechua HL50",F,3,"ud",3.99,DEC,u["linterna"]),
 ("Lejía (5 L, desinfección de trampas)",F,2,"ud",1.79,"Aldi",u["lejia"]),
 ("Paquete de 500 folios A4 (estadillos)",F,1,"ud",4.19,"Carrefour",u["folios"]),
]+viajes(8,36,36,32)),
("T2.5","Eliminación de los ejemplares capturados",[
 ("Eutanasia por veterinario",S,10,"ud",20.00,"Tarifa veterinaria Caser",u["vet"]),
 ("Recogida y tratamiento de cadáveres",S,2,"servicio",60.00,"OCU",u["ocu"]),
]),
("T2.6","Seguimiento de la población de visón",[
 ("Arcilla gris (5 L)",F,16,"bolsa",5.39,LM,u["arcilla"]),
 ("Sardina fresca (cebo)",F,30,"kg",4.00,"Supermercado (precio medio)",u["sardina"]),
 ("Paquete de 500 folios A4 (fichas de revisión)",F,1,"ud",4.19,"Carrefour",u["folios"]),
]+viajes(14,32,28,16)),
("Gestión","Gestión del proyecto",[
 ("Contrato de la bióloga (Mireya Abad), jornada completa, meses 7–24",PE,18,"mes","SAL","Tabla salarial 2026 (Universidad de Valladolid)","https://investigadoc.uva.es/convocatorias/2026/Tabla%202026%20retribuciones%20-%20copia.pdf"),
 ("Seguro de accidentes para el trabajo de campo",S,3,"persona",26.16,"Seguro estudiantes UCM",u["seguro"]),
 ("Bolígrafos BIC (pack de 10)",F,1,"pack",4.35,"Amazon",u["boli"]),
 ("Paquete de 500 folios A4",F,2,"ud",4.19,"Carrefour",u["folios"]),
 ("Folletos divulgativos A5 (250 ud)",S,1,"pack",72.60,"MOO",u["moo"]),
]+viajes(1,2,0,1)),
]
