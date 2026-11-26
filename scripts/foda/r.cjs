const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async()=>{const b=await chromium.launch({args:['--ignore-certificate-errors']});const p=await b.newPage({viewport:{width:1500,height:900},deviceScaleFactor:2});
await p.goto('file:///tmp/claude-0/-home-user-otto/d29c33c2-598e-5dc8-bce0-9a1627727064/scratchpad/foda/w.html',{waitUntil:'networkidle'});await p.waitForTimeout(400);
const el=await p.$('svg');const bb=await el.boundingBox();await el.screenshot({path:'/tmp/claude-0/-home-user-otto/d29c33c2-598e-5dc8-bce0-9a1627727064/scratchpad/foda/prev.png'});
await p.pdf({path:'/home/user/otto/Matriz-FODA-RIPARIA-GEN.pdf',printBackground:true,width:(bb.width/96).toFixed(2)+'in',height:(bb.height/96).toFixed(2)+'in',margin:{top:'0',bottom:'0',left:'0',right:'0'}});await b.close();})();
