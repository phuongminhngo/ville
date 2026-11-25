# Extra English strings found in the code (tour, mosaic hunt, 3D signs, small UI labels)
EXTRA = {
 "Tous":"All","Bientôt":"Soon","Ma ville":"My city","La vidéo":"The video","◉ Ouvrir":"◉ Open","Cathédrale":"Cathedral",
 "⌖ Centrer ici":"⌖ Center here","Ouvrir la page":"Open the page","Voir le projet":"See the project","nouveaux projets":"new projects",
 "cliquez pour ouvrir":"click to open","Les outils, en démo":"The tools, in demo","▭ Vue 2D (du dessus)":"▭ 2D view (from above)",
 "Chasse aux mosaïques":"Mosaic hunt","Cliquer pour ouvrir ▸":"Click to open ▸","Entrer dans le musée ▸":"Enter the museum ▸",
 "Cliquez pour visiter →":"Click to visit →","Bienvenue dans ma ville":"Welcome to my city","✨ Faire scintiller la tour":"✨ Make the tower sparkle",
 "Boîte à outils":"Toolbox","Mon CV en 1 page →":"My CV on 1 page →","Vidéo & photo · La Serre":"Video & photo · La Serre","Suivante":"Next",
 "Montre-m’en une":"Show me one","Déjà trouvée":"Already found","Mosaïque trouvée !":"Mosaic found!",
 "Chaque bâtiment rassemble des projets":"Each building gathers projects","Un clic, et tout le projet s’ouvre":"One click, and the whole project opens",
 "Soleil, pluie, neige ou nuit : à vous de choisir":"Sun, rain, snow or night: your choice","Une ville vivante, à explorer librement":"A living city, free to explore",
 "Et deux autres portfolios vous attendent":"And two more portfolios are waiting for you","Fermer":"Close","Visite guidée · 18 s":"Guided tour · 18 s",
}
# exact pieces of source code replaced in en.html (strings drawn on canvases or glued to numbers)
SRC = [
 ("'Mosaïque trouvée !':'Déjà trouvée'", "'Mosaic found!':'Already found'"),
 ('<button id="tgo">Voir le projet</button>', '<button id="tgo">See the project</button>'),
 ('<button id="tnext">Suivante</button>', '<button id="tnext">Next</button>'),
 ('<h5>Chasse aux mosaïques ${', '<h5>Mosaic hunt ${'),
 ("Dix petites mosaïques en pixels sont cachées dans les rues, en 3D comme sur le plan. Elles clignotent doucement : cliquez dessus pour découvrir une anecdote.",
  "Ten little pixel mosaics are hidden in the streets, in 3D and on the map. They blink gently: click one to discover a fun fact."),
 ("Montre-m’en une", "Show me one"),
 ("f:\"Hà Nội ⇄ Paris : entre l'Europe et l'Asie, entre stratégie et image.\"", "f:\"Hà Nội ⇄ Paris: between Europe and Asia, between strategy and image.\""),
 ("f:\"Trois écoles, deux pays, et quatre prix de recherche scientifique.\"", "f:\"Three schools, two countries, and four scientific research awards.\""),
 ("f:\"Du brief du manager au contrat signé : un recrutement standardisé et automatisé.\"", "f:\"From the manager's brief to the signed contract: a standardised, automated recruitment.\""),
 ("f:\"« trọn vẹn nghi lễ, vẹn tròn yêu thương » : mon produit 360°, conçu de zéro.\"", "f:\"“trọn vẹn nghi lễ, vẹn tròn yêu thương”: my 360° product, built from scratch.\""),
 ("f:\"Interviews, récaps d'événements et vlogs : je filme et je monte.\"", "f:\"Interviews, event recaps and vlogs: I shoot and I edit.\""),
 ("f:\"10 newsletters depuis le début de l'année et 7 e-coffees.\"", "f:\"10 newsletters since the start of the year and 7 e-coffees.\""),
 ("f:\"6 → 12 posts LinkedIn par mois : une cadence doublée et tenue.\"", "f:\"6 → 12 LinkedIn posts a month: a pace doubled and kept up.\""),
 ("f:\"Rica Lewis : heritage denim × modernité asiatique.\"", "f:\"Rica Lewis: heritage denim × Asian modernity.\""),
 ("f:\"BREAD : une identité visuelle pour du pain maison et du café.\"", "f:\"BREAD: a visual identity for homemade bread and coffee.\""),
 ("f:\"Créer, communiquer, organiser, piloter : tout est dans la boîte à outils.\"", "f:\"Create, communicate, organise, manage: it's all in the toolbox.\""),
 ("Visite guidée · 18 s</div>", "Guided tour · 18 s</div>"),
 ("Mettez la fenêtre en plein écran, lancez l’enregistrement d’écran,<br>puis cliquez n’importe où. Touche R pour rejouer à la fin.",
  "Make the window full screen, start your screen recording,<br>then click anywhere. Press R to replay at the end."),
 ("▶ Lancer</div>", "▶ Start</div>"),
 ("say('Bienvenue dans ma ville'", "say('Welcome to my city'"),
 ("say('Chaque bâtiment rassemble des projets'", "say('Each building gathers projects'"),
 ("say('Un clic, et tout le projet s’ouvre'", "say('One click, and the whole project opens'"),
 ("say('Soleil, pluie, neige ou nuit : à vous de choisir'", "say('Sun, rain, snow or night: your choice'"),
 ("say('Une ville vivante, à explorer librement'", "say('A living city, free to explore'"),
 ("say('Et deux autres portfolios vous attendent'", "say('And two more portfolios are waiting for you'"),
 ("const txt='Prochain arrêt : votre équipe !'", "const txt='Next stop: your team!'"),
 ("fillText('Ouverte aux opportunités'", "fillText('Open to opportunities'"),
 ("'Bravo, les 10 mosaïques sont trouvées !'", "'Well done, all 10 mosaics found!'"),
 ("'Glissez un bâtiment pour le déplacer'", "'Drag a building to move it'"),
 ("'Copié ! Colle-le dans la conversation.'", "'Copied! Paste it into the conversation.'"),
 ("'Flèches · ", "'Arrows · "),
 ("'Portfolio RH','8 km →'", "'HR portfolio','8 km →'"),
 ("'Portfolio PM','12 km →'", "'PM portfolio','12 km →'"),
 ("Votre navigateur ne peut pas afficher la ville en 3D. Voici l’essentiel de mon portfolio en une page.",
  "Your browser cannot show the 3D city. Here is the essence of my portfolio on one page."),
 ('Mon CV en 1 page →</a><a href="https://www.linkedin.com', 'My CV on 1 page →</a><a href="https://www.linkedin.com'),
 ('content="Galerie Phuong Ngo : un portfolio en forme de ville, avec sept lieux à visiter."', 'content="Galerie Phuong Ngo: a portfolio shaped like a city, with seven places to visit."'),
 ("'Glisser : se déplacer · pincer ou molette : zoomer · toucher un musée : l’ouvrir · ⟲ ⟳ : tourner':'Cliquez sur un musée pour voir ses projets'",
  "'Drag: move around · pinch or scroll: zoom · tap a museum: open it · ⟲ ⟳: turn':'Click a museum to see its projects'"),
]

# short labels without accents that the first pass missed
EXTRA.update({
 "Vue":"View","Jeu":"Game","Ton":"Tone","Ciel":"Sky","Rose":"Pink","Carte":"Map","Texte":"Text","Cible":"Target","Anneau":"Ring",
 "Outils":"Tools","Doigts":"Fingers","Souris":"Mouse","Nommer":"Naming","Zoomer":"Zoom","Lancer":"Start","Pincer":"Pinch",
 "Clavier":"Keyboard","Montage":"Editing","Mesurer":"Measure","Pivoter":"Rotate","Produit":"Product","Plan 2D":"2D map",
 "Visuels":"Visuals","Attirer":"Attract","1 doigt":"1 finger","Piloter":"Manage","Glisser":"Drag","Langues":"Languages",
 "Molette":"Scroll wheel","Refonte":"Redesign","Tournage":"Shooting","Primaire":"Primary","Recruter":"Recruit","Boussole":"Compass",
 "Ambiance":"Mood","Comparer":"Compare","Site web":"Website","Page web":"Web page","Formation":"Education","Principal":"Primary",
 "Discutons":"Let's talk","Clic droit":"Right click","Secondaire":"Secondary","2 doigts ↔":"2 fingers ↔","2 doigts ↕":"2 fingers ↕",
 "Couverture":"Cover","pages vues":"page views","2 semaines":"2 weeks","Entreprise":"Company","Documenter":"Document",
 "8 semaines":"8 weeks","Kit visuel":"Visual kit","Conception":"Design","Construire":"Build","▦ Mosaïques":"▦ Mosaics",
 "Communiquer":"Communicate","Rose Pastel":"Pastel Pink","Accompagner":"Support","Tour Eiffel":"Eiffel Tower","Bleu Pastel":"Pastel Blue",
 "Vert Pastel":"Pastel Green","~30 min/sem.":"~30 min/week","⌥ + 2 doigts":"⌥ + 2 fingers","Typographies":"Typefaces",
 "Rouge cerise":"Cherry Red","Publications":"Posts","Cartographier":"Map it","Maquettes web":"Web mock-ups","Page LinkedIn":"LinkedIn page",
 "Automatisation":"Automation","Cliquer dessus":"Click it","Postproduction":"Post-production","Site Cloudi-Fi":"Cloudi-Fi website",
 "Cliquer-glisser":"Click and drag","design narratif":"narrative design","Moteur… action !":"Rolling… action!","Repositionnement":"Repositioning",
 "refonte visuelle":"visual redesign","produit bilingue":"bilingual product","Tourner 2 doigts":"Turn with 2 fingers","visiteurs uniques":"unique visitors",
 "Pourquoi EasyForm":"Why EasyForm","mission freelance":"freelance assignment","2025 – aujourd'hui":"2025 – present","tourner · incliner":"turn · tilt",
 "Conception produit":"Product design","goodies · papeterie":"goodies · stationery","visites via Threads":"visits via Threads",
 "assistante stylisme":"styling assistant","Clic droit + glisser":"Right click + drag","Ambassadeurs LinkedIn":"LinkedIn ambassadors",
 "Sourcing fournisseurs":"Supplier sourcing","Programme ambassadeurs":"Ambassador programme","Organiser & automatiser":"Organise & automate",
 "1 · Attirer · Cloudi-Fi":"1 · Attract · Cloudi-Fi","2 · Recruter · Cloudi-Fi":"2 · Recruit · Cloudi-Fi","3 · Accueillir · Cloudi-Fi":"3 · Welcome · Cloudi-Fi",
 "4 · Engager · Cloudi-Fi":"4 · Engage · Cloudi-Fi","5 · Piloter · Cloudi-Fi":"5 · Manage · Cloudi-Fi",
 "(1 · Attirer · Cloudi-Fi)":"(1 · Attract · Cloudi-Fi)","(2 · Recruter · Cloudi-Fi)":"(2 · Recruit · Cloudi-Fi)","(3 · Accueillir · Cloudi-Fi)":"(3 · Welcome · Cloudi-Fi)",
 "(4 · Engager · Cloudi-Fi)":"(4 · Engage · Cloudi-Fi)","(5 · Piloter · Cloudi-Fi)":"(5 · Manage · Cloudi-Fi)",
 "EasyForm, slide 8 : Quiz":"EasyForm, slide 8: Quiz","EasyForm, slide 5 : Cible":"EasyForm, slide 5: Target","EasyForm, slide 2 : Agenda":"EasyForm, slide 2: Agenda",
 "EasyForm, slide 11 : Benchmark":"EasyForm, slide 11: Benchmark","EasyForm, slide 1 : Couverture":"EasyForm, slide 1: Cover",
 "EasyForm, slide 6 : Pourquoi EasyForm":"EasyForm, slide 6: Why EasyForm","site · LinkedIn · ambassadeurs":"website · LinkedIn · ambassadors",
 "Page entreprise · cloudi-fi.com":"Company page · cloudi-fi.com","· Page entreprise · cloudi-fi.com":"· Company page · cloudi-fi.com",
 "impressions, sept. 2025 → nov. 2026":"impressions, Sept 2025 → Nov 2026","The Chemistry : assistante stylisme":"The Chemistry: styling assistant",
 "Walenty Designer Clothing : stylisme":"Walenty Designer Clothing: styling","impressions LinkedIn, 100 % organiques":"LinkedIn impressions, 100% organic",
 "Charte graphique · hôtel en baie d'Hạ Long":"Brand guidelines · hotel in Hạ Long Bay","Texte courant : menus, fiches produit, site.":"Body text: menus, product sheets, website.",
 "Touches manuscrites : signatures, accroches.":"Handwritten touches: signatures, taglines.","Notion (bases, formulaires, automatisations)":"Notion (databases, forms, automations)",
 "Équipe d'organisation (BTC) · communication · Hà Nội":"Organising team (BTC) · communication · Hà Nội","SIRH":"HRIS","SIRH · RH":"HRIS · HR","RH & SIRH":"HR & HRIS",
 "agent IA":"AI agent","Menu":"Menu","Exemple":"Example","Formulaire":"Form",
})
import json as _j, re as _r
for _x in _j.load(open(__import__('os').path.join(__import__('os').path.dirname(__file__),'rt.json')))['data'] + _j.load(open(__import__('os').path.join(__import__('os').path.dirname(__file__),'rt.json')))['ui']:
    _t = _x.strip()
    if _r.match(r'^(RVB|CMJN) [\d ]+$', _t):
        EXTRA[_t] = _t.replace('RVB', 'RGB').replace('CMJN', 'CMYK')

# People platform card (rewritten Nov 2026)
EXTRA.update({
 "Un seul espace pour tous les sujets RH de Cloudi-Fi, avec un menu latéral et un guide sur chaque page. Chacun ne voit que ce qu'il a le droit de voir, et un agent IA tient les données à jour.":"One place for every people topic at Cloudi-Fi, with a sidebar and a guide on every page. Each person sees only what they are allowed to see, and an AI agent keeps the data up to date.",
 "Démo : l'espace manager":"Demo: the manager space","Démo : l'espace prestataire":"Demo: the contractor space","Démo guidée":"Guided demo",
 "valider les congés, suivre les soldes, les factures et les KPIs de l'équipe":"approve time off, follow the team's balances, invoices and KPIs",
 "poser un congé, suivre son solde et le calendrier partagé, envoyer une facture":"request time off, follow your balance and the shared calendar, send an invoice",
 "People handbook":"People handbook","Espace d'équipe":"Team space","Espace personnel":"Personal space","Pour les RH":"For HR","Partout":"Everywhere",
 "comment on travaille (entreprise, politiques, programmes, infos pratiques, handbooks des équipes, ressources) avec une barre de recherche ; chacun propose des ressources, validées par la direction ou les RH ; l'organigramme en bas, où chacun modifie sa propre carte":"how we work (company, policies, programmes, practical info, team handbooks, resources) with a search bar; anyone can suggest a resource, approved by leadership or HR; the org chart at the bottom, where everyone edits their own card",
 "les OKRs de chaque équipe et l'objectif de l'entreprise, les ressources de l'équipe, les KPIs par personne pour les managers, la validation des congés avec les soldes, et les factures des prestataires dès qu'elles arrivent":"every team's OKRs and the company target, the team's resources, KPIs per person for managers, time-off approvals with balances, and contractor invoices as soon as they arrive",
 "mon tableau de bord, mes tâches, mes KPIs, la gestion des congés et des factures pour les prestataires (formulaire, solde, demandes, calendrier partagé) et mes entretiens, privés ; les collègues sur PayFit ou Remote voient où faire leur demande":"my dashboard, my tasks, my KPIs, time off and invoices for contractors (form, balance, requests, shared calendar) and my reviews, kept private; colleagues on PayFit or Remote see where to ask",
 "les campagnes d'entretiens et de feedback des pairs, le Hiring Hub (postes ouverts, candidats, file d'actions, tendances), les analytics de la newsletter et des e-coffees, les réponses aux e-mails, l'onboarding et les pages LinkedIn":"review and peer feedback campaigns, the Hiring Hub (open roles, candidates, action queue, trends), newsletter and e-coffee analytics, email replies, onboarding and LinkedIn pages",
 "un guide et une démo guidée sur chaque page, une visite de toute la plateforme, un bouton commentaire, un journal de toutes les modifications, et « voir en tant que » pour les managers et les RH":"a guide and a guided demo on every page, a tour of the whole platform, a comment button, a log of every change, and “view as” for managers and HR",
 "l'agent IA envoie les e-mails de congés au salarié et au valideur, synchronise les congés avec le fichier Time Off, envoie les formulaires, relances et invitations Google Meet des campagnes, et tient les tâches d'onboarding à jour":"the AI agent sends time-off emails to the employee and the approver, syncs time off with the Time Off sheet, sends campaign forms, reminders and Google Meet invites, and keeps onboarding tasks up to date",
 ": valider les congés, suivre les soldes, les factures et les KPIs de l'équipe":": approve time off, follow the team's balances, invoices and KPIs",
 ": poser un congé, suivre son solde et le calendrier partagé, envoyer une facture":": request time off, follow your balance and the shared calendar, send an invoice",
})

EXTRA.update({
 "Le SIRH tout-en-un, tenu à jour par un agent IA":"All-in-one HRIS, kept up to date by an AI agent","Agent IA":"AI agent",
 "J'ai conçu la plateforme avec un agent IA : le People handbook, un espace d'équipe, un espace personnel et des pages réservées aux RH.":"I designed the platform with an AI agent: the People handbook, a team space, a personal space and pages for HR only.",
 "Valider les congés, suivre les soldes, les factures et les KPIs de l'équipe":"Approve time off, follow the team's balances, invoices and KPIs",
 "Poser un congé, suivre son solde et le calendrier partagé, envoyer une facture":"Request time off, follow your balance and the shared calendar, send an invoice",
})
_PP=[("People handbook","People handbook"),("Espace d'équipe","Team space"),("Espace personnel","Personal space"),("Pour les RH","For HR"),("Partout","Everywhere"),("En coulisses","Behind the scenes")]
for _fr,_en in _PP:
    for _k,_v in list(EXTRA.items()):
        pass
_bodies={k:v for k,v in EXTRA.items() if k.startswith(('comment on travaille','les OKRs de chaque','mon tableau de bord, mes tâches','les campagnes d','un guide et une démo','l\'agent IA envoie'))}
_order=['comment on travaille','les OKRs de chaque','mon tableau de bord, mes tâches','les campagnes d','un guide et une démo',"l'agent IA envoie"]
for (_fr,_en),_pre in zip(_PP,_order):
    _k=[k for k in _bodies if k.startswith(_pre)][0]
    EXTRA[_fr+' : '+_k]=_en+': '+_bodies[_k]

EXTRA.update({
 "Projet phare · 5 · Piloter · Cloudi-Fi":"Flagship project · 5 · Manage · Cloudi-Fi","(Projet phare · 5 · Piloter · Cloudi-Fi)":"(Flagship project · 5 · Manage · Cloudi-Fi)",
 "mon produit 360°":"my 360° product","(mon produit 360°)":"(my 360° product)","Projet personnel · de l'idée au produit en ligne":"Personal project · from idea to live product",
 "(Projet personnel · de l'idée au produit en ligne)":"(Personal project · from idea to live product)","Mon produit 360° : construit de zéro.":"My 360° product: built from scratch.",
})
