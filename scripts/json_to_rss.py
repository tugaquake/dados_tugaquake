#!/usr/bin/env python3
import sys, json, datetime
from xml.sax.saxutils import escape

input_file, output_file = sys.argv[1], sys.argv[2]

with open(input_file, 'r', encoding='utf-8') as f:
    alerts = json.load(f)

now_dt = datetime.datetime.now(datetime.timezone.utc)
now = now_dt.strftime('%a, %d %b %Y %H:%M:%S GMT')

items = []

if not alerts:
    # Não existem alertas ativos
    items.append(f"""  <item>
    <title>🟩 - Nenhum alerta ativo</title>
    <description>Última atualização: {now}</description>
    <pubDate>{now}</pubDate>
    <category>estado</category>
  </item>
""")

else:
    # Existem alertas
    for a in alerts:
        pub_dt = datetime.datetime.fromisoformat(a['hora'])
        pub = pub_dt.strftime('%a, %d %b %Y %H:%M:%S GMT')

        title = escape(a['titulo'])
        desc = escape(a['mensagem'])
        cat = escape(a.get('canal', ''))
        zone = escape(a.get('zona', ''))

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
  <link>https://tugaquake0.wordpress.com/alertas/</link>
  <description>Feed de alertas TugaQuake</description>
  <lastBuildDate>{now}</lastBuildDate>
{''.join(items)}
</channel>
</rss>
"""

with open(output_file, 'w', encoding='utf-8') as f:
    f.write(rss)
