import json,math,statistics
from wiki import BAHIA,CHAPE
d=json.load(open('elencos_tm.json',encoding='utf-8'))
# ordem, sigla, nome curto, cores, valor total (€ mi, Transfermarkt)
CL=[('1023','PAL','Palmeiras','#006437','#ffffff',218.58),('614','FLA','Flamengo','#c4161c','#111111',211.25),
('609','CRU','Cruzeiro','#003e94','#ffffff',185.90),('199','COR','Corinthians','#ffffff','#111111',156.95),
('978','VAS','Vasco','#111111','#ffffff',151.05),('537','BOT','Botafogo','#111111','#ffffff',129.60),
('10010','BAH','Bahia','#0055a5','#e30613',123.70),('2462','FLU','Fluminense','#7a1c32','#00613c',121.13),
('221','SAN','Santos','#ffffff','#111111',114.60),('330','CAM','Atlético-MG','#111111','#ffffff',112.40),
('679','CAP','Athletico-PR','#c8102e','#111111',109.73),('8793','RBB','Bragantino','#ffffff','#d0021b',100.45),
('585','SAO','São Paulo','#ffffff','#d0021b',83.00),('210','GRE','Grêmio','#0d80bf','#111111',77.55),
('6600','INT','Internacional','#d71920','#ffffff',72.00),('2125','VIT','Vitória','#d6001c','#111111',50.23),
('776','CFC','Coritiba','#00543c','#ffffff',49.85),('3876','MIR','Mirassol','#f5d200','#00753a',30.58),
('10997','REM','Remo','#0a1f5c','#ffffff',22.98),('17776','CHA','Chapecoense','#00843d','#ffffff',22.10)]
MAP={'Goleiro':'GOL','Zagueiro':'ZAG','Lateral Esq.':'LAT','Lateral Dir.':'LAT','Volante':'MEI','Meia Central':'MEI','Meia Ofensivo':'MEI','Meia Direita':'MEI','Meia Esquerda':'MEI','Ponta-Direita':'ATA','Ponta-Esquerda':'ATA','Centroavante':'ATA','Seg. Atacante':'ATA'}
WMAP={'G':('GOL','Goleiro'),'Z':('ZAG','Zagueiro'),'LE':('LAT','Lateral Esq.'),'LD':('LAT','Lateral Dir.'),'V':('MEI','Volante'),'M':('MEI','Meia'),'A':('ATA','Atacante')}
clubes=[];jog=[]
for ci,(tid,sig,nome,c1,c2,tot) in enumerate(CL):
    clubes.append([sig,nome,c1,c2,tot])
    if tid in d:
        for j in d[tid]['jogadores']:
            jog.append(['t%d'%j['tm'],j['nome'],MAP[j['posTM']],j['posTM'],ci,j['valor'],j['idade']])
    else:
        src=BAHIA if sig=='BAH' else CHAPE
        for k,x in enumerate(src.split('|')):
            p,n=x.split(' ',1);pos,det=WMAP[p]
            jog.append(['%s%d'%(sig.lower(),k),n,pos,det,ci,None,None])
print(len(clubes),len(jog))
ids=[j[0] for j in jog];assert len(ids)==len(set(ids))
js='const CLUBES_RAW='+json.dumps(clubes,ensure_ascii=False,separators=(',',':'))+';\nconst JOGADORES_RAW='+json.dumps(jog,ensure_ascii=False,separators=(',',':'))+';\n'
open('dados.js','w',encoding='utf-8').write(js);print(len(js),'bytes')
