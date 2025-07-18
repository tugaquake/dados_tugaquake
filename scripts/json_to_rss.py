#!/usr/bin/env python3
import sys, json, datetime
from xml.sax.saxutils import escape

input_file, output_file = sys.argv[1], sys.argv[2]
with open(input_file, 'r', encoding='utf-8') as f:
    alerts = json.load(f)

now = datetime.datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
items = []
for a in alerts:
    # Filtrar só alertas completos:
    # se algum destes campos estiver vazio, ignora este alerta
    if not (a.get('hora') and a.get('titulo') and a.get('mensagem')):
        continue

    pub = datetime.datetime.fromisoformat(a['hora']).strftime('%a, %d %b %Y %H:%M:%S GMT')
    title = escape(a['titulo'])
    desc  = escape(a['mensagem'])
    cat   = escape(a.get('canal',''))
    zone  = escape(a.get('tópico',''))
    items.append(f"""  <item>
    <title>{title}</title>
    <description>{desc} – Zona: {zone}</description>
    <pubDate>{pub}</pubDate>
    <category>{cat}</category>
  </item>
""")

rss = f"""<?xml version='1.0' encoding='UTF-8'?>
<rss version='2.0'>
<channel>
  <title>Alertas TugaQuake</title>
  <link>https://tugaquake.github.io/dados_tugaquake/alertas.xml</link>
  <description>Feed de alertas TugaQuake</description>
  <lastBuildDate>{now}</lastBuildDate>
{''.join(items)}
</channel>
</rss>
"""

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(rss)
