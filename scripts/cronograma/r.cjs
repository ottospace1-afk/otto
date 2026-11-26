const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async()=>{const b=await chromium.launch({args:['--ignore-certificate-errors']});const p=await b.newPage();
await p.goto('file:///home/user/otto/Cronograma-RIPARIA-GEN.html',{waitUntil:'networkidle'});await p.emulateMedia({media:'print'});
await p.pdf({path:'/home/user/otto/Cronograma-RIPARIA-GEN.pdf',format:'A4',landscape:true,printBackground:true,margin:{top:'10mm',bottom:'10mm',left:'11mm',right:'11mm'}});await b.close();})();
