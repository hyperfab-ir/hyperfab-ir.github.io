#!/usr/bin/env python3
"""
سازنده‌ی صفحه‌های ایستای hyperfab-ir.github.io

این سایت معرفی‌نامه‌ی هایپرفب برای موتورهای جست‌وجو و دستیارهای هوش مصنوعی است.
سایت اصلی و ثبت سفارش در https://hyperfab.ir است و همه‌ی دکمه‌ها به آنجا می‌روند.

ظاهر از قالب وردپرس هایپرفب (assets/hyperfab.css، بدون تغییر) می‌آید و همان
کلاس‌ها اینجا تکرار می‌شوند. هر چیزی که قالب نداشت در assets/site.css است.

اجرا:  python3 tools/build.py
خروجی: index.html، en/index.html و زیرپوشه‌های هر صفحه، sitemap.xml، llms.txt
"""
import json
import os
import sys
from datetime import date
from html import escape

sys.path.insert(0, os.path.dirname(__file__))
import content_fa  # noqa: E402
import content_en  # noqa: E402
from common import SITE, MAIN, CONTACT  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = date.today().isoformat()

# ---------------------------------------------------------------- icons
# همان مسیرهای hf_svc_icon در inc-services.php
ICONS = {
    'check': '<path d="M20 6L9 17l-5-5"/>',
    'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.2 2"/>',
    'layers': '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/><path d="M3 17.5l9 5 9-5"/>',
    'target': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3.2"/><path d="M12 3v5.8M12 15.2V21M3 12h5.8M15.2 12H21"/>',
    'file': '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M9 15l2 2 4-4"/>',
    'truck': '<rect x="2" y="4" width="14" height="12" rx="2"/><path d="M16 9h3l3 3v4h-6z"/><circle cx="6.5" cy="18.5" r="2"/><circle cx="17.5" cy="18.5" r="2"/>',
    'coin': '<path d="M12 1v22M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>',
    'cube': '<path d="M12 2l9 5v10l-9 5-9-5V7z"/><path d="M3.3 7L12 12l8.7-5M12 22V12"/>',
    'wrench': '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    'chart': '<path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/>',
    'shield': '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
    'sparkle': '<path d="M12 3l1.9 5.1L19 10l-5.1 1.9L12 17l-1.9-5.1L5 10l5.1-1.9z"/><path d="M19 16l.8 2.2L22 19l-2.2.8L19 22l-.8-2.2L16 19l2.2-.8z"/>',
    'bolt': '<path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/>',
    'stack': '<rect x="3" y="3" width="7" height="7" rx="1.5"/><rect x="14" y="3" width="7" height="7" rx="1.5"/><rect x="3" y="14" width="7" height="7" rx="1.5"/><rect x="14" y="14" width="7" height="7" rx="1.5"/>',
    'sheet': '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18M8 4v16"/>',
    'chat': '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    'link': '<path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/>',
    'arrow': '<path d="M19 12H5M12 19l-7-7 7-7"/>',
    'search': '<circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/>',
    'ruler': '<path d="M21.3 8.7L8.7 21.3a1 1 0 0 1-1.4 0l-4.6-4.6a1 1 0 0 1 0-1.4L15.3 2.7a1 1 0 0 1 1.4 0l4.6 4.6a1 1 0 0 1 0 1.4z"/><path d="M9 6l2 2M12 3l2 2M6 9l2 2"/>',
    'pin': '<path d="M12 21s7-5.6 7-11a7 7 0 1 0-14 0c0 5.4 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/>',
    'phone': '<path d="M6.5 3.5 9 8 7 9.8a12 12 0 0 0 7.2 7.2L16 15l4.5 2.5v3a1.5 1.5 0 0 1-1.7 1.5C10.4 20.9 3.1 13.6 2 5.2A1.5 1.5 0 0 1 3.5 3.5z"/>',
    'mail': '<rect x="3" y="5" width="18" height="14" rx="3"/><path d="m3.5 7 8.5 6 8.5-6"/>',
    'box': '<path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><path d="M3.27 6.96L12 12.01l8.73-5.05M12 22.08V12"/>',
}


def icon(name, size=22):
    return ('<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            'stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" '
            'focusable="false">%s</svg>' % (size, size, ICONS[name]))


LOGO_MARK = ('<span class="mk"><svg viewBox="0 0 300 250" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><g transform="rotate(-14 150 125)"><rect x="34" y="113" width="232" height="26" rx="13" fill="#C23A1C" stroke="#1c1c1c" stroke-width="5"/></g><rect x="100" y="58" width="100" height="132" rx="18" fill="#F2A81D" stroke="#1c1c1c" stroke-width="5"/><rect x="116" y="80" width="36" height="26" rx="7" fill="#fff" stroke="#1c1c1c" stroke-width="4"/><rect x="130" y="189" width="40" height="16" rx="5" fill="#9AA1A9" stroke="#1c1c1c" stroke-width="4"/><rect x="138" y="203" width="24" height="17" rx="5" fill="#C2C7CC" stroke="#1c1c1c" stroke-width="4"/><rect x="145" y="214" width="10" height="7" rx="2.5" fill="#1c1c1c"/></svg></span>')
WORDMARK = '<span class="wordmark" dir="ltr"><span class="hy">Hyper</span><span class="fab">Fab</span></span>'


def e(s):
    return escape(s, quote=True)


def rel(depth, path):
    """نشانی نسبی یک فایل داخل همین سایت، از صفحه‌ای در عمق depth"""
    return ('../' * depth) + path


# ---------------------------------------------------------------- schema
def org_schema(c):
    """سازمان هایپرفب؛ هر صفحه همین را با @id ثابت دارد تا موتورها یکی بشمارند."""
    return {
        '@type': ['Organization', 'LocalBusiness'],
        '@id': MAIN + '/#organization',
        'name': c['brand_name'],
        'alternateName': c['brand_alt'],
        'url': MAIN + '/',
        'logo': SITE + '/assets/img/favicon-512.png',
        'image': SITE + '/assets/img/og-default.jpg',
        'description': c['org_desc'],
        'email': CONTACT['email'],
        'telephone': CONTACT['landline_intl'],
        'address': {
            '@type': 'PostalAddress',
            'streetAddress': c['address_street'],
            'addressLocality': c['address_city'],
            'addressCountry': 'IR',
        },
        'areaServed': {'@type': 'Country', 'name': c['country']},
        'openingHoursSpecification': [
            {'@type': 'OpeningHoursSpecification',
             'dayOfWeek': ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday'],
             'opens': '09:00', 'closes': '17:00'},
            {'@type': 'OpeningHoursSpecification', 'dayOfWeek': 'Thursday',
             'opens': '09:00', 'closes': '13:00'},
        ],
        'contactPoint': [
            {'@type': 'ContactPoint', 'contactType': 'customer service',
             'telephone': CONTACT['mobile_intl'], 'email': CONTACT['email'],
             'availableLanguage': ['fa', 'en']},
        ],
        'sameAs': [MAIN + '/', SITE + '/', CONTACT['instagram'], CONTACT['instagram_pro'],
                   CONTACT['bale_channel_url'], CONTACT['bale_pro_url']],
        'knowsAbout': c['knows_about'],
    }


def faq_schema(faq):
    return {
        '@type': 'FAQPage',
        'mainEntity': [{'@type': 'Question', 'name': q,
                        'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in faq],
    }


def ld(graph):
    data = {'@context': 'https://schema.org', '@graph': graph}
    return ('<script type="application/ld+json">%s</script>'
            % json.dumps(data, ensure_ascii=False, separators=(',', ':')))


# ---------------------------------------------------------------- layout
def head(c, page, depth):
    url = SITE + page['path']
    alt = SITE + page['alt_path']
    fa_url, en_url = (url, alt) if c['lang'] == 'fa' else (alt, url)
    css = rel(depth, 'assets/')
    return f'''<!DOCTYPE html>
<html lang="{c['lang']}" dir="{c['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(page['title'])}</title>
<meta name="description" content="{e(page['desc'])}">
<meta name="keywords" content="{e(page['keywords'])}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<meta name="author" content="{e(c['brand_name'])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="fa" href="{fa_url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="x-default" href="{fa_url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(c['brand_name'])}">
<meta property="og:locale" content="{c['og_locale']}">
<meta property="og:title" content="{e(page['title'])}">
<meta property="og:description" content="{e(page['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og-default.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#171d2b">
<link rel="icon" href="{css}img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="{css}img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{css}img/apple-touch-icon.png">
<link rel="preload" href="{css}fonts/Vazirmatn-Variable.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{css}fonts.css">
<link rel="stylesheet" href="{css}hyperfab.css">
<link rel="stylesheet" href="{css}site.css">
<link rel="alternate" type="text/plain" title="llms.txt" href="{SITE}/llms.txt">
{ld(page['schema'])}
</head>
'''


def header(c, page, depth):
    home = rel(depth, c['home_rel']) or './'
    # لنگرهای صفحه‌ی اصلی (#services) از صفحه‌های دیگر به صفحه‌ی اصلی برمی‌گردند
    on_home = page['key'] == 'home'

    def href_of(h):
        if h.startswith('#'):
            return h if on_home else home + h
        return rel(depth, c['home_rel'] + h)
    nav = ''.join(
        f'<li><a href="{href_of(href)}"{" aria-current=\"page\"" if key == page["key"] else ""}>{e(label)}</a></li>'
        for key, label, href in c['nav'])
    alt_href = rel(depth, page['alt_rel']) or './'
    return f'''<body>
<a class="skip-link" href="#main">{e(c['skip'])}</a>
<header class="site-header">
	<div class="wrap">
		<a href="{home}" class="brand" aria-label="HyperFab">{LOGO_MARK}{WORDMARK}</a>
		<button class="hf-burger" id="hfBurger" aria-label="{e(c['menu'])}" aria-expanded="false" aria-controls="hfNav"><span></span><span></span><span></span></button>
		<nav class="main-nav" id="hfNav" aria-label="{e(c['menu_main'])}"><ul>{nav}</ul></nav>
		<div class="head-actions">
			<a class="order-btn" href="{MAIN}/order/">{icon('box', 17)} {e(c['order_short'])}</a>
			<a class="icon-btn lang-btn" href="{alt_href}" hreflang="{c['alt_lang']}" lang="{c['alt_lang']}" aria-label="{e(c['alt_lang_name'])}" title="{e(c['alt_lang_name'])}">{c['alt_lang_code']}</a>
		</div>
	</div>
</header>
<div class="origin-bar"><div class="wrap">{c['origin_bar']}</div></div>
<main id="main">
'''


def footer(c, depth):
    svc = ''.join(f'<li><a href="{MAIN}{s["url"]}">{e(s["title"])}</a></li>' for s in c['services'])
    svc += f'<li><a href="{rel(depth, c["est_rel"])}">{e(c["est_name"])}</a></li>'
    svc += f'<li><a href="{rel(depth, c["tek_rel"])}">{e(c["tek_name"])}</a></li>'
    links = ''.join(f'<li><a href="{MAIN}{u}">{e(t)}</a></li>' for t, u in c['foot_links'])
    soc = ''.join(
        f'<div class="hf-soc-group"><h6>{e(g["title"])}</h6><p>{e(g["desc"])}</p><div class="hf-soc-links">'
        + ''.join(f'<a href="{u}" target="_blank" rel="noopener">{e(n)} <span dir="ltr">{e(h)}</span></a>' for n, h, u in g['links'])
        + '</div></div>' for g in c['social_groups'])
    pin = '<path d="M12 21s6.5-5.2 6.5-10.2a6.5 6.5 0 1 0-13 0C5.5 15.8 12 21 12 21z"/><circle cx="12" cy="10.5" r="2.3"/>'
    tel = '<path d="M6.5 3.5 9 8 7 9.8a12 12 0 0 0 7.2 7.2L16 15l4.5 2.5v3a1.5 1.5 0 0 1-1.7 1.5C10.4 20.9 3.1 13.6 2 5.2A1.5 1.5 0 0 1 3.5 3.5z"/>'
    chat = '<path d="M21 12a8 8 0 0 1-11.5 7.2L4 20l1-4.8A8 8 0 1 1 21 12z"/>'
    clock = '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.2 2"/>'
    mail = '<rect x="3" y="5" width="18" height="14" rx="3"/><path d="m3.5 7 8.5 6 8.5-6"/>'

    def fi(p):
        return ('<svg class="fc-ico" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
                'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' + p + '</svg>')
    f = c['foot']
    return f'''</main>
<section class="bale-band">
	<div class="wrap">
		<a class="bale-cta" href="{CONTACT['bale_channel_url']}" target="_blank" rel="noopener">
			<img class="bale-logo" src="{rel(depth, 'assets/img/bale-logo.png')}" width="52" height="52" alt="{e(f['bale_alt'])}" loading="lazy" decoding="async">
			<span class="bale-text">
				<b>{e(f['bale_title'])} <span class="bale-id" dir="ltr">{CONTACT['bale_channel']}</span></b>
				<span>{e(f['bale_sub'])}</span>
			</span>
			<span class="bale-btn">{e(f['bale_btn'])}</span>
		</a>
	</div>
</section>
<footer class="site-footer" id="contact-info">
	<div class="wrap">
		<div class="foot-grid">
			<div>
				<a href="{MAIN}/" class="brand">{LOGO_MARK}{WORDMARK}</a>
				<p class="foot-tag">{e(f['tag'])}</p>
				<div class="hf-soc-groups">{soc}</div>
			</div>
			<div>
				<h5>{e(f['h_services'])}</h5>
				<ul>{svc}</ul>
			</div>
			<div>
				<h5>{e(f['h_access'])}</h5>
				<ul>{links}</ul>
			</div>
			<div>
				<h5>{e(f['h_info'])}</h5>
				<ul class="foot-contact">
					<li>{fi(pin)}<span><b>{e(f['addr_label'])}:</b> {e(f['address'])}</span></li>
					<li>{fi(tel)}<span>{e(f['tel'])}: <a class="fc-num" href="tel:{CONTACT['landline']}" dir="ltr">{f['landline_pretty']}</a></span></li>
					<li>{fi(chat)}<span>{e(f['design'])}: <a class="fc-num" href="tel:{CONTACT['mobile']}" dir="ltr">{f['mobile_pretty']}</a> <span class="foot-note">{e(f['design_note'])}</span></span></li>
					<li>{fi(chat)}<span>{e(f['service'])}: <a class="fc-num" href="tel:{CONTACT['mobile']}" dir="ltr">{f['mobile_pretty']}</a> <span class="foot-note">{e(f['service_note'])}</span></span></li>
					<li>{fi(clock)}<span>{e(f['hours_label'])}: {e(f['hours'])}</span></li>
					<li>{fi(mail)}<span>{e(f['email'])}: <a class="fc-num" href="mailto:{CONTACT['email']}" dir="ltr">{CONTACT['email']}</a></span></li>
				</ul>
			</div>
		</div>
		<div class="foot-bottom">
			<span>© {date.today().year} HyperFab — {e(f['rights'])}</span>
			<span class="mono"><a href="{MAIN}/">hyperfab.ir</a></span>
		</div>
	</div>
</footer>
<script>
(function(){{
	var b=document.getElementById('hfBurger'), n=document.getElementById('hfNav');
	if(!b||!n) return;
	var close=function(){{ n.classList.remove('open'); b.classList.remove('on'); b.setAttribute('aria-expanded','false'); }};
	b.addEventListener('click',function(ev){{ ev.stopPropagation(); var o=n.classList.toggle('open'); b.classList.toggle('on',o); b.setAttribute('aria-expanded',o?'true':'false'); }});
	n.addEventListener('click',function(ev){{ if(ev.target.closest('a')) close(); }});
	document.addEventListener('click',function(ev){{ if(!n.contains(ev.target)) close(); }});
	document.addEventListener('keydown',function(ev){{ if(ev.key==='Escape') close(); }});
}})();
</script>
</body>
</html>
'''


# ---------------------------------------------------------------- blocks
def hfs_head(kicker, title, sub='', tag='h2', anchor=''):
    a = f' id="{anchor}"' if anchor else ''
    s = f'<p>{sub}</p>' if sub else ''
    return f'<div class="hfs-head"{a}><div class="kicker">{kicker}</div><{tag}>{title}</{tag}>{s}</div>'


def why_cards(items):
    return '<div class="hfs-why">' + ''.join(
        f'<div class="hfs-why-card"><div class="hfs-why-ic">{icon(i, 28)}</div><h3>{e(t)}</h3><p>{d}</p></div>'
        for i, t, d in items) + '</div>'


def adv_cards(items):
    return '<div class="hfs-adv">' + ''.join(
        f'<div class="hfs-adv-card"><div class="ic">{icon(i, 22)}</div><h3>{e(t)}</h3><p>{d}</p></div>'
        for i, t, d in items) + '</div>'


def steps(items, num):
    return '<div class="hfs-steps">' + ''.join(
        f'<div class="hfs-step"><div class="n">{num(k)}</div><h3>{e(t)}</h3><p>{d}</p></div>'
        for k, (t, d) in enumerate(items, 1)) + '</div>'


def checks(items):
    return '<div class="hfs-dg">' + ''.join(
        f'<div class="hfs-dg-item">{icon("check", 16)}<p>{d}</p></div>' for d in items) + '</div>'


def faq_block(c, faq, sub=''):
    items = ''.join(
        f'<details{" open" if k == 0 else ""}><summary>{e(q)}</summary><div class="ans">{e(a)}</div></details>'
        for k, (q, a) in enumerate(faq))
    return (f'<section class="block section-alt" id="faq"><div class="wrap">'
            f'{hfs_head("FAQ", e(c["faq_title"]), sub)}<div class="hfs-faq">{items}</div></div></section>')


def cta_block(h, p, buttons):
    b = ''.join(f'<a class="{cls}" href="{u}"{" target=\"_blank\" rel=\"noopener\"" if u.startswith("https://ble.ir") else ""}>{e(t)}</a>'
                for cls, t, u in buttons)
    return (f'<section class="block"><div class="wrap"><div class="hfs-cta"><h2>{e(h)}</h2>'
            f'<p>{p}</p><div class="b">{b}</div></div></div></section>')


def stats_bar(items):
    return '<div class="hfs-stats"><div class="wrap">' + ''.join(
        f'<div class="hfs-stat"><div class="si">{icon(i, 21)}</div><div class="v">{e(v)} <span class="u">{e(u)}</span></div><div class="k">{e(k)}</div></div>'
        for i, v, u, k in items) + '</div></div>'


def svc_hero(c, depth, d):
    ticks = ''.join(f'<li>{icon("check", 17)}<span><b>{e(a)}</b> <span{" class=\"hfs-lat\"" if lat else ""}>{e(b)}</span></span></li>'
                    for a, b, lat in d['ticks'])
    btns = ''.join(f'<a class="{cls}" href="{u}">{(icon("box", 18) + " ") if cls == "btn-red" else ""}{e(t)}</a>' for cls, t, u in d['buttons'])
    home = rel(depth, c['home_rel']) or './'
    return f'''<section class="hfs-hero">
	<div class="wrap">
		<div>
			<div class="hfs-crumb"><a href="{home}">{e(c['brand_name'])}</a> ‹ {e(d['crumb'])}</div>
			<h1>{d['h1']}</h1>
			<p class="hfs-lead">{d['lead']}</p>
			<ul class="hfs-ticks">{ticks}</ul>
			<div class="hfs-hero-btns">{btns}</div>
		</div>
		<div class="hfs-hero-art has-pic"><picture><img src="{rel(depth, d['img'])}" alt="{e(d['img_alt'])}" width="600" height="420" loading="eager" fetchpriority="high" decoding="async"></picture></div>
	</div>
	{stats_bar(d['stats'])}
</section>
'''


def prose(paras):
    return ''.join(f'<p>{p}</p>' for p in paras)


# ---------------------------------------------------------------- pages
def page_home(c):
    depth = c['depth_home']
    h = c['home']
    cards = ''.join(
        f'<div class="proc-card"><a class="proc-illo" href="{MAIN}{s["url"]}" aria-label="{e(s["title"])}">'
        f'<picture><source srcset="{rel(depth, "assets/img/" + s["img"] + ".webp")}" type="image/webp">'
        f'<img src="{rel(depth, "assets/img/" + s["img"] + ".png")}" alt="{e(s["title"])}" width="110" height="110" loading="lazy" decoding="async"></picture></a>'
        f'<h4><a href="#{s["key"]}">{e(s["title"])}</a></h4><p>{e(s["short"])}</p></div>'
        for s in c['services'])

    details = ''
    for k, s in enumerate(c['services']):
        rows = ''.join(f'<div class="hfs-tech-row"><span class="k">{e(a)}</span><span class="v">{b}</span></div>' for a, b in s['specs'])
        details += f'''<article class="svc-detail" id="{s['key']}">
	<div class="svc-detail-pic"><picture><source srcset="{rel(depth, 'assets/img/' + s['img'] + '.webp')}" type="image/webp"><img src="{rel(depth, 'assets/img/' + s['img'] + '.png')}" alt="{e(s['title'])}" width="110" height="110" loading="lazy" decoding="async"></picture></div>
	<div class="svc-detail-body">
		<h3>{e(s['title'])}</h3>
		{prose(s['paras'])}
		<div class="svc-specs">{rows}</div>
		<div class="svc-links"><a class="btn-red" href="{MAIN}{s['url']}">{e(c['svc_more'])}</a><a class="svc-link2" href="{MAIN}/order/?m={s['m']}">{e(c['svc_order'])} {c['arrow']}</a></div>
	</div>
</article>
'''

    feat = ''
    for f in (h['est_feature'], h['tek_feature']):
        feat += f'''<section class="block{f['cls']}" id="{f['id']}">
	<div class="wrap">
		{hfs_head(f['kicker'], f['title'], f['sub'])}
		<div class="feature">
			<div class="feature-text">
				{prose(f['paras'])}
				{checks(f['points'])}
				<div class="svc-links"><a class="btn-red" href="{rel(depth, f['more_rel'])}">{e(f['more'])}</a><a class="svc-link2" href="{f['try_url']}">{e(f['try'])} {c['arrow']}</a></div>
			</div>
			<figure class="feature-pic"><img src="{rel(depth, f['img'])}" alt="{e(f['img_alt'])}" width="{f['img_w']}" height="{f['img_h']}" loading="lazy" decoding="async"><figcaption>{e(f['caption'])}</figcaption></figure>
		</div>
	</div>
</section>
'''

    stats = ''.join(f'<div><b>{e(v)}</b><span>{e(t)}</span></div>' for v, t in h['team_stats'])
    tag_svcs = '، '.join(f'<a href="#{s["key"]}">{e(s["title"])}</a>' for s in c['services']) if c['lang'] == 'fa' \
        else ', '.join(f'<a href="#{s["key"]}">{e(s["title"])}</a>' for s in c['services'])

    body = f'''<section class="hero" id="home">
	<div class="wrap">
		<div class="hero-card">
			<div class="eyebrow2">{e(h['eyebrow'])}</div>
			<h1>{e(h['h1'])}</h1>
			<p class="hero-lead">{e(h['lead'])}</p>
			<p>{h['p']}</p>
			<div class="taglist"><span class="tl-h">{e(h['tl_services'])}</span> {tag_svcs}</div>
			<div class="taglist"><span class="tl-h">{e(h['tl_tools'])}</span> <a href="#estimator">{e(c['est_name'])}</a>{c['sep']}<a href="#tekeyab">{e(c['tek_name'])}</a></div>
			<div class="taglist"><span class="tl-h">{e(h['tl_mats'])}</span> {e(h['mats'])}</div>
			<div class="hero-btns">
				<a class="btn-red" href="{MAIN}/order/">{icon('box', 18)} {e(h['btn1'])}</a>
				<a class="btn-ghost" href="{rel(depth, c['est_rel'])}">{e(h['btn2'])}</a>
			</div>
		</div>
		<div class="hero-illo"><div class="hero-illo-frame"><picture><source srcset="{rel(depth, 'assets/img/hero-parts.webp')}" type="image/webp"><img src="{rel(depth, 'assets/img/hero-parts.png')}" alt="{e(h['hero_alt'])}" width="1000" height="685" loading="eager" fetchpriority="high" decoding="async"></picture></div></div>
	</div>
</section>

<section class="block" id="summary">
	<div class="wrap">
		<div class="hf-panel about-panel summary-panel">
			<div class="sec-head"><div class="kicker">{h['sum_kicker']}</div><h2>{e(h['sum_title'])}</h2></div>
			<div class="about-body">{prose(h['sum_paras'])}</div>
		</div>
	</div>
</section>

<section class="block section-alt" id="services">
	<div class="wrap">
		<div class="shop-block">
			<div class="shop-head"><div><div class="kicker">SERVICES</div><h2>{e(h['svc_title'])}</h2><p>{e(h['svc_sub'])}</p></div>
				<a class="btn-shop" href="{MAIN}/services/">{e(h['svc_all'])} {c['arrow']}</a></div>
			<div class="proc-grid">{cards}</div>
		</div>
	</div>
</section>

{feat}
<section class="block section-alt" id="service-details">
	<div class="wrap">
		{hfs_head('IN DETAIL', e(h['det_title']), e(h['det_sub']))}
		<div class="svc-details">{details}</div>
	</div>
</section>

<section class="block" id="why">
	<div class="wrap">
		{hfs_head('WHY HYPERFAB', e(h['why_title']))}
		{why_cards(h['why'])}
	</div>
</section>

<section class="block section-alt" id="how">
	<div class="wrap">
		{hfs_head('HOW IT WORKS', e(h['how_title']), e(h['how_sub']))}
		{steps(h['how'], c['num'])}
	</div>
</section>

<section class="block about" id="about">
	<div class="wrap">
		<div class="hf-panel about-panel">
			<div class="sec-head"><div class="kicker">ABOUT</div><h2>{e(h['about_title'])}</h2></div>
			<div class="about-body">{prose(h['about_paras'])}</div>
			<div class="hf-ab-stats team-stats">{stats}</div>
			<div class="about-body">{prose(h['about_paras2'])}<p class="about-sign">{e(h['about_sign'])}</p></div>
		</div>
	</div>
</section>

<section class="block section-alt" id="academy">
	<div class="wrap">
		{hfs_head('ACADEMY', e(h['acad_title']), e(h['acad_sub']))}
		{adv_cards(h['acad'])}
		<div class="center-cta"><a class="btn-red" href="{MAIN}/academy/">{e(h['acad_btn'])}</a></div>
	</div>
</section>

{faq_block(c, h['faq'])}

<section class="block" id="contact">
	<div class="wrap">
		{hfs_head('CONTACT', e(h['contact_title']), e(h['contact_sub']))}
		<div class="hf-contact">
			{''.join(f'<div class="hf-contact-item"><span class="hf-contact-ico">{icon(i, 20)}</span><div><h4>{e(t)}</h4>{v}</div></div>' for i, t, v in h['contact_items'])}
		</div>
	</div>
</section>

{cta_block(h['cta_h'], h['cta_p'], [('w', h['btn1'], MAIN + '/order/'), ('o', c['tek_cta'], MAIN + '/tekeyab/'), ('o', c['bale_chat'], CONTACT['bale_admin_url'])])}
'''
    return depth, body


def page_tool(c, key):
    d = c[key]
    depth = d['depth']
    sections = ''
    for k, s in enumerate(d['sections']):
        alt = ' section-alt' if k % 2 == 0 else ''
        inner = hfs_head(s['kicker'], e(s['title']), s.get('sub', ''), anchor=s.get('id', ''))
        if s.get('paras'):
            inner += f'<div class="prose">{prose(s["paras"])}</div>'
        if s.get('why'):
            inner += why_cards(s['why'])
        if s.get('adv'):
            inner += adv_cards(s['adv'])
        if s.get('checks'):
            inner += checks(s['checks'])
        if s.get('steps'):
            inner += steps(s['steps'], c['num'])
        if s.get('table'):
            head_row = ''.join(f'<th>{e(x)}</th>' for x in s['table'][0])
            rows = ''.join('<tr>' + ''.join(f'<td>{x}</td>' for x in r) + '</tr>' for r in s['table'][1:])
            inner += f'<div class="hfs-tbl-wrap hfs-scroll"><table class="hfs-tbl"><thead><tr>{head_row}</tr></thead><tbody>{rows}</tbody></table></div>'
        if s.get('note'):
            inner += f'<div class="hfs-note">{s["note"]}</div>'
        if s.get('video'):
            v = s['video']
            inner += (f'<a class="video-card" href="{v["url"]}" target="_blank" rel="noopener">'
                      f'<img src="{rel(depth, v["img"])}" alt="{e(v["alt"])}" width="360" height="640" loading="lazy" decoding="async">'
                      f'<span><b>{e(v["title"])}</b>{e(v["desc"])}<em>{e(v["cta"])} {c['arrow']}</em></span></a>')
        sections += f'<section class="block{alt}"><div class="wrap">{inner}</div></section>\n'
    body = svc_hero(c, depth, d['hero']) + sections + faq_block(c, d['faq']) + cta_block(d['cta_h'], d['cta_p'], d['cta_btns'])
    return depth, body


def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full) or ROOT, exist_ok=True)
    with open(full, 'w', encoding='utf-8') as fh:
        fh.write(html)
    print('wrote', path)


def build_lang(c):
    pages = []
    depth, body = page_home(c)
    p = c['page_home']
    p['schema'] = [org_schema(c),
                   {'@type': 'WebSite', '@id': SITE + c['home_path'] + '#website', 'url': SITE + c['home_path'],
                    'name': c['site_name'], 'inLanguage': c['lang'], 'publisher': {'@id': MAIN + '/#organization'}},
                   {'@type': 'WebPage', '@id': SITE + c['home_path'], 'url': SITE + c['home_path'], 'name': p['title'],
                    'description': p['desc'], 'inLanguage': c['lang'], 'isPartOf': {'@id': SITE + c['home_path'] + '#website'},
                    'about': {'@id': MAIN + '/#organization'}, 'dateModified': TODAY},
                   {'@type': 'ItemList', 'name': c['home']['svc_title'], 'itemListElement': [
                       {'@type': 'ListItem', 'position': k, 'item': {
                           '@type': 'Service', 'name': s['title'], 'description': s['paras'][0].replace('<b>', '').replace('</b>', ''),
                           'url': MAIN + s['url'], 'serviceType': s['title'], 'provider': {'@id': MAIN + '/#organization'},
                           'areaServed': {'@type': 'Country', 'name': c['country']}}}
                       for k, s in enumerate(c['services'] + c['tools_as_services'], 1)]},
                   faq_schema(c['home']['faq'])]
    write(p['file'], head(c, p, depth) + header(c, p, depth) + body + footer(c, depth))
    pages.append(p)

    for key in ('estimator', 'tekeyab'):
        depth, body = page_tool(c, key)
        p = c['page_' + key]
        p['schema'] = [org_schema(c), *c[key]['schema'],
                       {'@type': 'BreadcrumbList', 'itemListElement': [
                           {'@type': 'ListItem', 'position': 1, 'name': c['brand_name'], 'item': SITE + c['home_path']},
                           {'@type': 'ListItem', 'position': 2, 'name': c[key]['hero']['crumb'], 'item': SITE + p['path']}]},
                       faq_schema(c[key]['faq'])]
        write(p['file'], head(c, p, depth) + header(c, p, depth) + body + footer(c, depth))
        pages.append(p)
    return pages


def sitemap(pages):
    by_path = {p['path']: p for p in pages}
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for p in pages:
        a = by_path[p['alt_path']]
        fa, en = (p, a) if p['lang'] == 'fa' else (a, p)
        out.append(f'  <url><loc>{SITE}{p["path"]}</loc><lastmod>{TODAY}</lastmod>'
                   f'<changefreq>monthly</changefreq><priority>{p["priority"]}</priority>'
                   f'<xhtml:link rel="alternate" hreflang="fa" href="{SITE}{fa["path"]}"/>'
                   f'<xhtml:link rel="alternate" hreflang="en" href="{SITE}{en["path"]}"/></url>')
    out.append('</urlset>\n')
    write('sitemap.xml', '\n'.join(out))


def main():
    pages = []
    for c in (content_fa.C, content_en.C):
        for p in ('page_home', 'page_estimator', 'page_tekeyab'):
            c[p]['lang'] = c['lang']
        pages += build_lang(c)
    sitemap(pages)


if __name__ == '__main__':
    main()
