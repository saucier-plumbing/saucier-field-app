import os
H=os.path.dirname(os.path.abspath(__file__)); R=os.path.dirname(H)
import json,sys
d=json.load(open(os.path.join(H,'data.json')))
items=[{k:i[k] for k in ('sku','name','hrs','cat','list','sa','ah','hol','desc','mtl','qbo')} for i in d['items'] if i['sku']!='FEE-005']
data=json.dumps({'items':items,'fees':{k:[v[0]] for k,v in d['fees'].items()},'hol':d['hol']},separators=(',',':'))
t=open(os.path.join(H,'app_template.html')).read().replace('/*__DATA__*/null',data)
open(os.path.join(H,'demo.html'),'w').write(t.replace('/*__DEMO__*/false','true'))
i=t.index('<header class="top">')
host='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<meta name="apple-mobile-web-app-capable" content="yes">\n<link rel="apple-touch-icon" href="icon.svg">\n'+t[:i]+'<style>:root{padding-top:env(safe-area-inset-top,0px)}[hidden]{display:none!important}img{max-width:100%}</style>\n</head>\n<body>\n'+t[i:]+'\n</body>\n</html>\n'
import os; pass
open(os.path.join(R,'index.html'),'w').write(host)
open(os.path.join(R,'prices.json'),'w').write(json.dumps({'updated':'2026-10-12','items':items},indent=0))
open(os.path.join(R,'manifest.json'),'w').write(json.dumps({"name":"Saucier Field Tickets","short_name":"Saucier","start_url":"./index.html","display":"standalone","background_color":"#f3f5f7","theme_color":"#1d3347","icons":[{"src":"icon.svg","sizes":"any","type":"image/svg+xml"}]},indent=1))
open(os.path.join(R,'icon.svg'),'w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 96 96"><rect width="96" height="96" rx="18" fill="#1d3347"/><path d="M22 30h30a14 14 0 0 1 14 14v22" fill="none" stroke="#e08a4c" stroke-width="12" stroke-linecap="round"/><text x="22" y="80" font-family="Arial" font-weight="700" font-size="22" fill="#f3f6f8">S</text></svg>')
open(os.path.join(R,'sw.js'),'w').write('''const C="saucier-v1";const F=["./","./index.html","./manifest.json","./icon.svg"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(F)));self.skipWaiting()});
self.addEventListener("activate",e=>{e.waitUntil(self.clients.claim())});
self.addEventListener("fetch",e=>{const u=new URL(e.request.url);if(e.request.method!=="GET")return;
 if(u.origin===location.origin){e.respondWith(fetch(e.request).then(r=>{const c=r.clone();caches.open(C).then(x=>x.put(e.request,c));return r}).catch(()=>caches.match(e.request).then(r=>r||caches.match("./index.html"))))}});
''')
print(len(host), len(data))
