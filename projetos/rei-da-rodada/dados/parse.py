import re,html,json,glob,collections
liga=open('liga.html',encoding='utf-8').read()
rows=re.findall(r'<td class="hauptlink no-border-links"><a title="([^"]+)" href="/([^/]+)/startseite/verein/(\d+)/saison_id/2025">',liga)
def valor(t):
    t=t.strip()
    m=re.match(r'€\s*([\d.,]+)\s*(mi\.|mil)',t)
    if not m: return None
    n=float(m.group(1).replace('.','').replace(',','.')) if m.group(2)=='mil' else float(m.group(1).replace(',','.'))
    return n/1000 if m.group(2)=='mil' else n
out={};posset=collections.Counter()
for t,sl,i in rows:
    try: s=open(f'kader_{i}.html',encoding='utf-8').read()
    except: continue
    if 'class="items"' not in s: print('sem tabela',t); continue
    body=s[s.find('class="items"'):]; body=body[:body.find('</table>\n</div>')] if '</table>\n</div>' in body else body
    trs=re.split(r'<tr class="(?:odd|even)">',body)[1:]
    jog=[]
    for tr in trs:
        nm=re.search(r'<td class="hauptlink">\s*<a href="/[^/]+/profil/spieler/(\d+)">\s*([^<]+?)\s*</a>',tr)
        pos=re.search(r'</tr>\s*<tr>\s*<td>\s*([^<]+?)\s*</td>',tr)
        idade=re.search(r'\((\d+)\)</td>',tr)
        mv=re.search(r'marktwertverlauf/spieler/\d+">([^<]+)</a>',tr)
        if not nm: continue
        p=html.unescape(pos.group(1)) if pos else '?'
        posset[p]+=1
        jog.append({'tm':int(nm.group(1)),'nome':html.unescape(nm.group(2)),'posTM':p,'idade':int(idade.group(1)) if idade else None,'valor':valor(mv.group(1)) if mv else None})
    out[i]={'nome':t,'slug':sl,'jogadores':jog}
    print(t,len(jog),'sem valor:',sum(1 for j in jog if j['valor'] is None))
print(posset)
json.dump(out,open('elencos_tm.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
