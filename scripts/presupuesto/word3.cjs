const fs=require('fs');
const {Document,Packer,Paragraph,TextRun,Table,TableRow,TableCell,WidthType,ShadingType,AlignmentType,HeadingLevel,BorderStyle,ExternalHyperlink}=require('docx');
const data=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));const v=data.val;
const grp=s=>s.replace(/\B(?=(\d{3})+(?!\d))/g,'.');
const eur=x=>{const [e,d]=x.toFixed(2).split('.');return grp(e)+','+d+' €';};
const num=x=>Number.isInteger(x)?grp(String(x)):String(+x.toFixed(2)).replace('.',',');
const W=[4300,2100,1000,1150,1200]; const TW=W.reduce((a,b)=>a+b,0);
const bd={style:BorderStyle.SINGLE,size:4,color:"A6A6A6"}; const borders={top:bd,bottom:bd,left:bd,right:bd};
const run=(t,o={})=>new TextRun({text:t,bold:!!o.bold,size:19,font:"Arial"});
const tc=(child,w,o={})=>new TableCell({width:{size:w,type:WidthType.DXA},borders,shading:o.fill?{type:ShadingType.CLEAR,color:"auto",fill:o.fill}:undefined,margins:{top:50,bottom:50,left:90,right:90},children:[new Paragraph({alignment:o.right?AlignmentType.RIGHT:AlignmentType.LEFT,children:[child]})]});
const kids=[new Paragraph({heading:HeadingLevel.TITLE,children:[new TextRun("Presupuesto por tareas")]}),
 new Paragraph({spacing:{after:200},children:[new TextRun({text:"Proyecto RIPARIA-GEN · Conservación de la rata de agua en el río Francia (Salamanca). Precios con IVA; el nombre de cada tienda enlaza a la página del producto.",size:20,font:"Arial"})]})];
let tot=0; const res=[];
for(const t of data.tareas){
  const rows=[new TableRow({tableHeader:true,children:["Elemento","Tienda","Cantidad","Precio","Total"].map((h,i)=>tc(run(h,{bold:true}),W[i],{fill:"F2F2F2",right:i>=2}))})];
  let st=0;
  for(const it of t.items){const tt=it.q*it.p; st+=tt;
    const shop=it.url?new ExternalHyperlink({link:it.url,children:[new TextRun({text:it.shop,style:"Hyperlink",size:19,font:"Arial"})]}):run(it.shop);
    rows.push(new TableRow({cantSplit:true,children:[tc(run(it.el),W[0]),tc(shop,W[1]),tc(run(num(it.q)),W[2],{right:true}),tc(run(eur(it.p)),W[3],{right:true}),tc(run(eur(tt)),W[4],{right:true})]}));}
  rows.push(new TableRow({children:[new TableCell({columnSpan:4,width:{size:TW-W[4],type:WidthType.DXA},borders,margins:{top:50,bottom:50,left:90,right:90},children:[new Paragraph({children:[run("Total",{bold:true})]})]}),tc(run(eur(st),{bold:true}),W[4],{right:true})]}));
  const title=t.code==="Gestión"?t.name:`${t.code}. ${t.name}`;
  kids.push(new Paragraph({heading:HeadingLevel.HEADING_2,children:[new TextRun(title)]}));
  kids.push(new Table({width:{size:TW,type:WidthType.DXA},columnWidths:W,rows}));
  res.push([title,st]); tot+=st;}
const ind=tot*v[7]; const RW=[7000,2500];
const rr=(a,b,bold)=>new TableRow({children:[tc(run(a,{bold}),RW[0],{fill:bold?"F2F2F2":undefined}),tc(run(b,{bold}),RW[1],{right:true,fill:bold?"F2F2F2":undefined})]});
kids.push(new Paragraph({heading:HeadingLevel.HEADING_1,children:[new TextRun("Resumen del presupuesto")]}));
kids.push(new Table({width:{size:RW[0]+RW[1],type:WidthType.DXA},columnWidths:RW,rows:[rr("Tarea","Total",true),...res.map(([a,b])=>rr(a,eur(b),false)),rr("Total costes directos",eur(tot),true),rr(`Costes indirectos (${Math.round(v[7]*100)} %)`,eur(ind),false),rr("Presupuesto total del proyecto",eur(tot+ind),true)]}));
const doc=new Document({styles:{default:{document:{run:{font:"Arial",size:20}}},paragraphStyles:[
 {id:"Title",name:"Title",basedOn:"Normal",run:{font:"Arial",size:32,bold:true},paragraph:{spacing:{before:0,after:120}}},
 {id:"Heading1",name:"Heading 1",basedOn:"Normal",next:"Normal",quickFormat:true,run:{font:"Arial",size:26,bold:true},paragraph:{spacing:{before:360,after:140},keepNext:true,outlineLevel:0}},
 {id:"Heading2",name:"Heading 2",basedOn:"Normal",next:"Normal",quickFormat:true,run:{font:"Arial",size:22,bold:true},paragraph:{spacing:{before:280,after:100},keepNext:true,outlineLevel:1}}]},
 sections:[{properties:{page:{size:{width:11906,height:16838},margin:{top:1134,bottom:1134,left:1134,right:1134}}},children:kids}]});
Packer.toBuffer(doc).then(b=>{fs.writeFileSync(process.argv[3],b);console.log('ok',tot.toFixed(2),(tot+ind).toFixed(2));});
