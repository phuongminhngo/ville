# Builds /home/claude/ville/en.html (English ville) from index.html plus the translation tables.
import json, re, sys
sys.path.insert(0, '.')
from t1 import T as A
from t2 import T as B
from t3 import T as C
try:
    from t4 import EXTRA, SRC
except ImportError:
    EXTRA = {}; SRC = []

import os
if os.environ.get('EXOV'):
    EXTRA = json.load(open('extra_override.json'))
todo = json.load(open('todo.json'))
M = {}
for tab in (A, B, C):
    for i, en in tab.items():
        M[todo[i]] = en
M.update(EXTRA)
M = {k: v for k, v in M.items() if k != v}

src = open('/home/claude/ville/index.html').read()
s = src

def end_of_literal(s, i):
    """i points at an opening { or [; return index just after its matching close, skipping JS strings."""
    depth = 0; q = None; k = i
    while k < len(s):
        c = s[k]
        if q:
            if c == '\\': k += 2; continue
            if c == q: q = None
        elif c in '"\'`': q = c
        elif c in '{[': depth += 1
        elif c in '}]':
            depth -= 1
            if depth == 0: return k + 1
        k += 1
    raise ValueError('unbalanced')

# translate the data objects right after they are declared
for name in ('EX', 'MUS', 'RH'):
    i = s.find('const %s=' % name)
    j = end_of_literal(s, s.find('=', i) + 1 if s[s.find('=', i) + 1] in '{[' else s.find('=', i) + 2)
    if s[j] == ';': j += 1
    s = s[:j] + '__trD(%s);' % name + s[j:]

# the 3D signs are drawn on canvases from source strings
for fr, en in [('Marque employeur · Le Palais', 'Employer brand · Le Palais'), ('Communication · La Gare', 'Communication · La Gare'),
               ('Direction artistique · L’Atelier', 'Art direction · L’Atelier'), ('Nghi le cuoi hoi · Le Pavillon', 'Nghi le cuoi hoi · Le Pavillon'),
               ('Accueil · chez Phuong', 'Home · chez Phuong'), ('Contact · La Poste', 'Contact · La Poste')]:
    s = s.replace("L2(scene,'%s'" % fr, "L2(scene,'%s'" % en)

# page metadata and links
s = s.replace('<title>Portfolio de Phuong</title>', '<title>Phuong\'s Portfolio</title>', 1)
s = s.replace('content="Phuong Ngo · Portfolio en forme de ville"', 'content="Phuong Ngo · A portfolio shaped like a city"')
s = s.replace("content=\"SIRH et communication interne : je conçois des outils RH que l'équipe adopte vraiment, et je raconte l'entreprise à ceux qui la font.\"",
              "content=\"HRIS and internal communication: I build HR tools the team actually adopts, and I tell the company's story to the people who make it.\"")
s = s.replace('<meta property="og:url" content="https://phuongminhngo.github.io/ville/">', '<meta property="og:url" content="https://phuongminhngo.github.io/ville/en.html">')
s = s.replace('<link rel="canonical" href="https://phuongminhngo.github.io/ville/">', '<link rel="canonical" href="https://phuongminhngo.github.io/ville/en.html"><link rel="alternate" hreflang="fr" href="https://phuongminhngo.github.io/ville/">')
s = s.replace('href="essentiel.html"', 'href="essential.html"')
s = s.replace('<html lang="fr"', '<html lang="en"')
for fr, en in [('} projet${', '} project${'), ('aria-label="Démo : ', 'aria-label="Demo: '), ('<i>Outils</i>', '<i>Tools</i>')]:
    assert fr in s, fr
    s = s.replace(fr, en)
# language switch: in the English page it points back to French
old = '<a class="ib ib-lang lg-lang" id="blang" href="en.html" hreflang="en" lang="en" aria-label="English version" title="English version">EN</a>'
assert old in s
s = s.replace(old, '<a class="ib ib-lang lg-lang" id="blang" href="./" hreflang="fr" lang="fr" aria-label="Version française" title="Version française">FR</a>')

for fr, en in SRC:
    if fr not in s: print('MISSING', fr[:60])
    s = s.replace(fr, en)

runtime = '''<script>
// English layer: translate the gallery data as it is declared, then any French text that still reaches the page
window.__EN=new Map(%s);
function __trD(o,seen){seen=seen||new Set();if(!o||typeof o!=='object'||seen.has(o))return o;seen.add(o);
 for(const k of Object.keys(o)){const v=o[k];if(typeof v==='string'){const t=__EN.get(v)||__EN.get(v.trim());if(t)o[k]=t;}else if(v&&typeof v==='object')__trD(v,seen);}
 for(const k of Object.keys(o)){const t=__EN.get(k);if(t&&!(t in o))o[t]=o[k];}return o;}
(function(){const A=['title','aria-label','alt','placeholder'];
 const tx=n=>{const v=n.nodeValue,t=v.trim();if(!t)return;const e=__EN.get(t);if(e&&e!==t)n.nodeValue=v.replace(t,e);};
 const el=e=>{A.forEach(a=>{const v=e.getAttribute&&e.getAttribute(a);if(v){const t=__EN.get(v.trim());if(t&&t!==v)e.setAttribute(a,t);}});};
 const walk=r=>{if(r.nodeType===3){tx(r);return;}if(r.nodeType!==1)return;if(/^(SCRIPT|STYLE)$/.test(r.nodeName))return;el(r);const w=document.createTreeWalker(r,NodeFilter.SHOW_ELEMENT|NodeFilter.SHOW_TEXT);let n;while(n=w.nextNode()){if(n.nodeType===3)tx(n);else el(n);}};
 const go=()=>{walk(document.body);new MutationObserver(ms=>ms.forEach(m=>{if(m.type==='characterData')tx(m.target);else if(m.type==='attributes')el(m.target);else m.addedNodes.forEach(walk);})).observe(document.body,{subtree:true,childList:true,characterData:true,attributes:true,attributeFilter:A});};
 if(document.body)go();else document.addEventListener('DOMContentLoaded',go);})();
</script>
''' % json.dumps(sorted(M.items(), key=lambda kv: -len(kv[0])), ensure_ascii=False).replace('</', '<\\/')

i = s.find('<script')
s = s[:i] + runtime + s[i:]
open('/home/claude/ville/en.html', 'w').write(s)
print('pairs', len(M), 'size', len(s))
