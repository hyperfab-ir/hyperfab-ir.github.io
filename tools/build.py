#!/usr/bin/env python3
"""
سازنده‌ی صفحه‌های ایستای hyperfabgroup.github.io (و نسخه‌ی قدیمی hyperfab-ir.github.io)

این سایت معرفی‌نامه‌ی هایپرفب برای موتورهای جست‌وجو و دستیارهای هوش مصنوعی است.
سایت اصلی و ثبت سفارش در https://hyperfab.ir است و همه‌ی دکمه‌ها به آنجا می‌روند.

ظاهر از قالب وردپرس هایپرفب (assets/hyperfab.css، بدون تغییر) می‌آید و همان
کلاس‌ها اینجا تکرار می‌شوند. هر چیزی که قالب نداشت در assets/site.css است.

اجرا:  python3 tools/build.py
خروجی: index.html، en/index.html و زیرپوشه‌های هر صفحه، sitemap.xml، llms.txt
"""
import copy
import json
import os
import re
import sys
from datetime import date
from html import escape, unescape

from PIL import Image

sys.path.insert(0, os.path.dirname(__file__))
import content_fa  # noqa: E402
import content_en  # noqa: E402
from common import SITE, MAIN, CONTACT  # noqa: E402
from images import IMAGE_CREDITS  # noqa: E402
from media import WORKS, VIDEOS, video_url, video_embed  # noqa: E402
from structure import HUBS, NAV_LABELS, INDUSTRIAL_KEYS  # noqa: E402
from stock import MEDIA, PAGE_TOPICS  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = date.today().isoformat()
ORG_ID = MAIN + '/#organization'
# شماره‌ها در پیوند tel: به قالب E.164 و بدون جداکننده
TEL_LANDLINE = CONTACT.get('landline_e164', '+982177527438')
TEL_MOBILE = CONTACT.get('mobile_e164', '+989962233898')
HOME_IMG = 'assets/img/hero-parts.png'
WARNINGS = []


def warn(msg):
    WARNINGS.append(msg)
    print('WARNING:', msg)

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


# ---------------------------------------------------------------- images
_SIZES = {}


def img_size(path):
    """ابعاد واقعی تصویر (path نسبت به ریشه‌ی سایت)؛ برای width/height و جلوگیری از جابه‌جایی صفحه"""
    if path not in _SIZES:
        try:
            with Image.open(os.path.join(ROOT, path)) as im:
                _SIZES[path] = im.size
        except OSError:
            warn(f'image not readable: {path}')
            _SIZES[path] = None
    return _SIZES[path]


def webp_of(path):
    """نسخه‌ی webp کنار یک jpg/png، اگر باشد"""
    base, ext = os.path.splitext(path)
    if ext.lower() in ('.jpg', '.jpeg', '.png') and os.path.exists(os.path.join(ROOT, base + '.webp')):
        return base + '.webp'
    return None


def img(depth, path, alt, cls='', eager=False, picture=False):
    """<img> با ابعاد واقعی؛ اگر webp کنارش باشد داخل <picture> با <source> می‌رود."""
    size = img_size(path)
    wh = f' width="{size[0]}" height="{size[1]}"' if size else ''
    c = f' class="{cls}"' if cls else ''
    load = ' loading="eager" fetchpriority="high"' if eager else ' loading="lazy"'
    tag = f'<img{c} src="{rel(depth, path)}" alt="{e(alt)}"{wh}{load} decoding="async">'
    w = webp_of(path)
    if w:
        return f'<picture><source type="image/webp" srcset="{rel(depth, w)}">{tag}</picture>'
    return f'<picture>{tag}</picture>' if picture else tag


def abs_url(path):
    return SITE + '/' + path.lstrip('/')


def image_object(path, caption=''):
    o = {'@type': 'ImageObject', 'url': abs_url(path), 'contentUrl': abs_url(path)}
    size = img_size(path)
    if size:
        o['width'], o['height'] = size
    if caption:
        o['caption'] = caption
    return o


FA_DIGITS = str.maketrans('۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩', '01234567890123456789')


def e164(num):
    """هر شکلی از شماره‌ی ایران را به +98… بی‌جداکننده برمی‌گرداند"""
    d = re.sub(r'[^\d+]', '', num.translate(FA_DIGITS))
    if d.startswith('00'):
        return '+' + d[2:]
    if d.startswith('0'):
        return '+98' + d[1:]
    return d if d.startswith('+') else '+' + d


def fix_tel(html):
    return re.sub(r'href="tel:([^"]*)"', lambda m: f'href="tel:{e164(m.group(1))}"', html)


# ---------------------------------------------------------------- schema
def org_schema(c):
    """سازمان هایپرفب؛ هر صفحه همین را با @id ثابت دارد تا موتورها یکی بشمارند."""
    return {
        '@type': ['Organization', 'LocalBusiness', 'ProfessionalService'],
        '@id': ORG_ID,
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
        'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': c['catalog_name'], 'itemListElement': [
            {'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': s['title'],
                                               'url': s['url'] if s['url'].startswith('http') else MAIN + s['url']}}
            for s in c['services'] + c['tools_as_services']]},
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
    og_img = abs_url(page.get('og_img', 'assets/img/og-default.jpg'))
    size = img_size(page.get('og_img', 'assets/img/og-default.jpg'))
    og_size = (f'\n<meta property="og:image:width" content="{size[0]}">'
               f'\n<meta property="og:image:height" content="{size[1]}">') if size else ''
    og_alt = f'\n<meta property="og:image:alt" content="{e(page["og_alt"])}">' if page.get('og_alt') else ''
    alt_locale = 'en_US' if c['lang'] == 'fa' else 'fa_IR'
    return f'''<!DOCTYPE html>
<html lang="{c['lang']}" dir="{c['dir']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(page['title'])}</title>
<meta name="description" content="{e(page['desc'])}">
<meta name="keywords" content="{e(page['keywords'])}">
<meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
<meta name="google-site-verification" content="fU2lqYzDNWrzfksv2M-7JnUH_YPVxpO9Hlq-vi2N9NU">
<meta name="author" content="{e(c['brand_name'])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="fa" href="{fa_url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="x-default" href="{fa_url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(c['brand_name'])}">
<meta property="og:locale" content="{c['og_locale']}">
<meta property="og:locale:alternate" content="{alt_locale}">
<meta property="og:title" content="{e(page['title'])}">
<meta property="og:description" content="{e(page['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og_img}">{og_size}{og_alt}
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="{og_img}">
<meta name="theme-color" content="#171d2b">
<link rel="icon" href="{css}img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="{css}img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{css}img/apple-touch-icon.png">
<link rel="preload" href="{css}fonts/Vazirmatn-Variable.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{css}fonts.css">
<link rel="stylesheet" href="{css}hyperfab.min.css">
<link rel="stylesheet" href="{css}site.css">
<link rel="alternate" type="text/plain" title="llms.txt" href="{SITE}/llms.txt">
<link rel="alternate" type="text/plain" title="llms-full.txt" href="{SITE}/llms-full.txt">
{ld(page['schema'])}
</head>
'''


def nav_items(c):
    """منوی اصلی: (کلید، برچسب، مسیر نسبت به ریشه‌ی زبان، زیرمنو[(کلید، برچسب، مسیر)])"""
    L = NAV_LABELS[c['lang']]
    online = [(None, L['all_services'], 'services/')] + [(None, s['title'], 'services/#' + s['key']) for s in c['services']]
    industrial = [(None, L['all_industrial'], 'industrial/')] + [
        (k, c[k]['hero']['crumb'], c['page_' + k]['path'][len(c['home_path']):]) for k in INDUSTRIAL_KEYS]
    tools = [('estimator', c['est_name'], 'price-estimator/'), ('tekeyab', c['tek_name'], 'tekeyab/')]
    return [('home', L['home'], '', []), ('services', L['services'], 'services/', online),
            ('industrial', L['industrial'], 'industrial/', industrial), ('tools', L['tools'], 'price-estimator/', tools),
            ('portfolio', L['portfolio'], 'portfolio/', []), ('about', L['about'], 'about/', []),
            ('contact', L['contact'], 'contact/', [])]


def header(c, page, depth):
    home = rel(depth, c['home_rel']) or './'
    L = NAV_LABELS[c['lang']]

    def href_of(h):
        return (rel(depth, c['home_rel'] + h) or './') if h else home
    cur = page['key']
    cur_attr = ' aria-current="page"'
    nav = ''
    for key, label, h, kids in nav_items(c):
        active = cur == key or any(k == cur for k, _, _ in kids)
        a = f'<a href="{href_of(h)}"{cur_attr if cur == key else ""}>{e(label)}</a>'
        if not kids:
            nav += f'<li class="menu-item{" current-menu-item" if active else ""}">{a}</li>'
            continue
        sub = ''.join(f'<li class="menu-item{" current-menu-item" if k and k == cur else ""}"><a href="{href_of(kh)}"'
                      f'{cur_attr if k and k == cur else ""}>{e(kl)}</a></li>' for k, kl, kh in kids)
        nav += (f'<li class="menu-item menu-item-has-children{" current-menu-ancestor" if active else ""}">{a}'
                f'<button class="hf-sub-toggle" type="button" aria-expanded="false" aria-label="{e(L["toggle_open"])}" '
                f'data-open="{e(L["toggle_open"])}" data-close="{e(L["toggle_close"])}"></button>'
                f'<ul class="sub-menu">{sub}</ul></li>')
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
    svc = ''.join(f'<li><a href="{rel(depth, c["home_rel"] + "services/")}#{s["key"]}">{e(s["title"])}</a></li>' for s in c['services'])
    svc += f'<li><a href="{rel(depth, c["est_rel"])}">{e(c["est_name"])}</a></li>'
    svc += f'<li><a href="{rel(depth, c["tek_rel"])}">{e(c["tek_name"])}</a></li>'
    for name, r in c['industrial_links']:
        svc += f'<li><a href="{rel(depth, r)}">{e(name)}</a></li>'
    links = ''.join(f'<li><a href="{rel(depth, c["home_rel"] + u)}">{e(t)}</a></li>' for t, u in NAV_LABELS[c['lang']]['site_pages'])
    links += ''.join(f'<li><a href="{MAIN}{u}">{e(t)}</a></li>' for t, u in c['foot_links'])
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
			{img(depth, 'assets/img/bale-logo.png', f['bale_alt'], 'bale-logo')}
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
					<li>{fi(tel)}<span>{e(f['tel'])}: <a class="fc-num" href="tel:{TEL_LANDLINE}" dir="ltr">{f['landline_pretty']}</a></span></li>
					<li>{fi(chat)}<span>{e(f['design'])}: <a class="fc-num" href="tel:{TEL_MOBILE}" dir="ltr">{f['mobile_pretty']}</a> <span class="foot-note">{e(f['design_note'])}</span></span></li>
					<li>{fi(chat)}<span>{e(f['service'])}: <a class="fc-num" href="tel:{TEL_MOBILE}" dir="ltr">{f['mobile_pretty']}</a> <span class="foot-note">{e(f['service_note'])}</span></span></li>
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
	var sync=function(li){{ var t=li.querySelector('.hf-sub-toggle'); if(!t) return; var o=li.classList.contains('open');
		t.setAttribute('aria-expanded',o?'true':'false'); t.setAttribute('aria-label',o?t.dataset.close:t.dataset.open); }};
	n.addEventListener('click',function(ev){{
		var t=ev.target.closest('.hf-sub-toggle');
		if(t){{ ev.preventDefault(); ev.stopPropagation(); var li=t.closest('.menu-item-has-children'), was=li.classList.contains('open');
			n.querySelectorAll('.menu-item-has-children.open').forEach(function(o){{ if(o!==li){{ o.classList.remove('open'); sync(o); }} }});
			li.classList.toggle('open',!was); sync(li); return; }}
		if(ev.target.closest('a')) close();
	}});
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
		<figure class="hfs-hero-art has-pic">{img(depth, d['img'], d['img_alt'], eager=True, picture=True)}{credit(c, d['img'], 'hero-credit')}</figure>
	</div>
	{stats_bar(d['stats'])}
</section>
'''


def credit(c, img, cls):
    """زیرنویس منبع برای تصویرهای آرشیوی؛ تصویرهای خود هایپرفب زیرنویس ندارند.
    ویکی‌مدیا: نام عکاس + مجوز. Vecteezy: پیوند ذکر منبعی که مجوز رایگانش می‌خواهد
    («<موضوع> Stock photos by Vecteezy»)، به‌علاوه‌ی نام عکاس."""
    m = IMAGE_CREDITS.get(img.split('assets/img/', 1)[-1]) or IMAGE_CREDITS.get(os.path.basename(img))
    if not m:
        return ''
    t = c['credit']
    if m.get('source') == 'vecteezy':
        return (f'<small class="{cls}">{e(t["note"])} · {e(t["photo"])}: {e(m["artist"])} · '
                f'<a href="{m["attr_url"]}" rel="noopener">{e(m["attr_text"])}</a></small>')
    return (f'<small class="{cls}">{e(t["note"])} · {e(t["photo"])}: <a href="{m["page"]}" rel="noopener">{e(m["artist"])}</a>'
            f', Wikimedia Commons · <a href="{m["licurl"]}" rel="license noopener">{e(m["lic"])}</a></small>')


def gallery(c, depth, items):
    """عکس‌های واقعی کار هایپرفب؛ برچسب «عکس واقعی» دارند تا از تصویرهای آرشیوی جدا باشند."""
    return '<div class="gallery">' + ''.join(
        f'<figure>{img(depth, src, cap)}'
        f'<figcaption><span class="real-tag">{e(c["real_label"])}</span>{e(cap)}</figcaption></figure>'
        for src, cap in items) + '</div>'


def works_block(c, depth):
    cards = ''
    for w in WORKS:
        t, meta, d = w[c['lang']]
        cards += (f'<article class="work-card">{img(depth, w["img"], t)}'
                  f'<div><span class="real-tag">{e(c["real_label"])}</span><h3>{e(t)}</h3><p class="work-meta">{e(meta)}</p><p>{e(d)}</p></div></article>')
    return cards


def videos_block(c, depth):
    out = ''
    for code, cover, fa, en in VIDEOS:
        t, d = fa if c['lang'] == 'fa' else en
        out += (f'<a class="vid-card" href="{video_url(code)}" target="_blank" rel="noopener">'
                f'{img(depth, "assets/img/videos/" + cover + ".webp", t)}'
                f'<span class="vid-play" aria-hidden="true"></span><b>{e(t)}</b><small>{e(d)}</small></a>')
    return out


def video_schema(c):
    return [{'@type': 'VideoObject', 'name': (fa if c['lang'] == 'fa' else en)[0],
             'description': (fa if c['lang'] == 'fa' else en)[1],
             'thumbnailUrl': SITE + '/assets/img/videos/' + cover + '.webp', 'embedUrl': video_embed(code),
             'url': video_url(code), 'inLanguage': 'fa', 'publisher': {'@id': MAIN + '/#organization'}}
            for code, cover, fa, en in VIDEOS]


def prose(paras):
    return ''.join(f'<p>{p}</p>' for p in paras)


# ---------------------------------------------------------------- pages
def relink(html, prefix):
    """پیوندهای نسبی متن صفحه‌ی اصلی را برای صفحه‌ای که یک سطح پایین‌تر است اصلاح می‌کند."""
    if not prefix:
        return html
    return re.sub(r'href="(?!https?:|#|mailto:|tel:|/|\.\./)', 'href="' + prefix, html)


def online_cards(c, depth, on_services=False):
    base = '' if on_services else rel(depth, c['home_rel'] + 'services/')
    return ''.join(
        f'<div class="proc-card"><a class="proc-illo" href="{base}#{s["key"]}" aria-label="{e(s["title"])}">'
        f'{img(depth, "assets/img/" + s["img"] + ".png", s["title"], picture=True)}</a>'
        f'<h4><a href="{base}#{s["key"]}">{e(s["title"])}</a></h4><p>{e(s["short"])}</p></div>'
        for s in c['services'])


def industrial_cards(c, depth):
    """کارت تصویری هر خدمت صنعتی؛ تصویر همان سربرگ صفحه‌ی خدمت است (واقعی یا آرشیوی)."""
    out = ''
    for k in INDUSTRIAL_KEYS:
        hero, page = c[k]['hero'], c['page_' + k]
        href = rel(depth, page['path'].lstrip('/'))
        out += (f'<div class="proc-card ind-card"><a class="proc-illo" href="{href}" aria-label="{e(hero["crumb"])}">'
                f'{img(depth, hero["img"], hero.get("img_alt", hero["crumb"]), picture=True)}</a>'
                f'<h4><a href="{href}">{e(hero["crumb"])}</a></h4><p>{e(page["desc"])}</p></div>')
    return out


def sec_online(c, depth, on_services=False, alt=' section-alt'):
    h, L = c['home'], NAV_LABELS[c['lang']]
    btn = '' if on_services else \
        f'<a class="btn-shop" href="{rel(depth, c["home_rel"] + "services/")}">{e(L["all_services"])} {c["arrow"]}</a>'
    return f'''<section class="block{alt}" id="services">
	<div class="wrap">
		<div class="shop-block">
			<div class="shop-head"><div><div class="kicker">SERVICES</div><h2>{e(h['svc_title'])}</h2><p>{e(h['svc_sub'])}</p></div>{btn}</div>
			<div class="proc-grid">{online_cards(c, depth, on_services)}</div>
		</div>
	</div>
</section>
'''


def sec_industrial(c, depth, on_hub=False, alt=''):
    f, L = c['home']['ind_feature'], NAV_LABELS[c['lang']]
    btn = '' if on_hub else \
        f'<a class="btn-shop" href="{rel(depth, c["home_rel"] + "industrial/")}">{e(L["industrial_btn"])} {c["arrow"]}</a>'
    return f'''<section class="block{alt}" id="industrial-services">
	<div class="wrap">
		<div class="shop-block">
			<div class="shop-head"><div><div class="kicker">INDUSTRIAL PRODUCTION</div><h2>{e(f['title'])}</h2><p>{e(f['sub'])}</p></div>{btn}</div>
			<div class="proc-grid ind-grid">{industrial_cards(c, depth)}</div>
			<p class="archive-note"><a href="{rel(depth, c['home_rel'] + 'credits/')}">{e(c['credit']['note'])}</a></p>
		</div>
	</div>
</section>
'''


def feature(c, depth, f, prefix=''):
    try_href = f['try_url'] if f['try_url'].startswith('http') else rel(depth, f['try_url'])
    return f'''<section class="block{f['cls']}" id="{f['id']}">
	<div class="wrap">
		{hfs_head(f['kicker'], f['title'], f['sub'])}
		<div class="feature">
			<div class="feature-text">
				{relink(prose(f['paras']), prefix)}
				{relink(checks(f['points']), prefix)}
				<div class="svc-links"><a class="btn-red" href="{rel(depth, f['more_rel'])}">{e(f['more'])}</a><a class="svc-link2" href="{try_href}">{e(f['try'])} {c['arrow']}</a></div>
			</div>
			<figure class="feature-pic">{img(depth, f['img'], f['img_alt'])}<figcaption>{e(f['caption'])}{credit(c, f['img'], 'inline-credit')}</figcaption></figure>
		</div>
	</div>
</section>
'''


def sec_details(c, depth, prefix='../'):
    h = c['home']
    details = ''
    for s in c['services']:
        rows = ''.join(f'<div class="hfs-tech-row"><span class="k">{e(a)}</span><span class="v">{b}</span></div>' for a, b in s['specs'])
        details += f'''<article class="svc-detail" id="{s['key']}">
	<div class="svc-detail-pic">{img(depth, 'assets/img/' + s['img'] + '.png', s['title'], picture=True)}</div>
	<div class="svc-detail-body">
		<h3>{e(s['title'])}</h3>
		{relink(prose(s['paras']), prefix)}
		<div class="svc-specs">{relink(rows, prefix)}</div>
		<div class="svc-links"><a class="btn-red" href="{MAIN}{s['url']}">{e(c['svc_more'])}</a><a class="svc-link2" href="{MAIN}/order/?m={s['m']}">{e(c['svc_order'])} {c['arrow']}</a></div>
	</div>
</article>
'''
    return f'''<section class="block section-alt" id="service-details">
	<div class="wrap">
		{hfs_head('IN DETAIL', e(h['det_title']), e(h['det_sub']))}
		<div class="svc-details">{details}</div>
	</div>
</section>
'''


def sec_simple(sid, alt, inner):
    return f'<section class="block{alt}" id="{sid}"><div class="wrap">{inner}</div></section>\n'


def sec_why(c, alt=''):
    h = c['home']
    return sec_simple('why', alt, hfs_head('WHY HYPERFAB', e(h['why_title'])) + why_cards(h['why']))


def sec_how(c, alt=' section-alt'):
    h = c['home']
    return sec_simple('how', alt, hfs_head('HOW IT WORKS', e(h['how_title']), e(h['how_sub'])) + steps(h['how'], c['num']))


def sec_works(c, depth, limit=None, alt=' section-alt'):
    L = NAV_LABELS[c['lang']]
    cards = works_block(c, depth)
    if limit:
        cards = ''.join(re.findall(r'<article class="work-card">.*?</article>', cards, re.S)[:limit])
        cards += ''
    btn = (f'<div class="center-cta"><a class="btn-red" href="{rel(depth, c["home_rel"] + "portfolio/")}">{e(L["works_btn"])}</a></div>'
           if limit else '')
    return sec_simple('works', alt, hfs_head('PORTFOLIO', e(c['works_title']), e(c['works_sub']))
                      + f'<div class="works-grid">{cards}</div>' + btn)


def sec_videos(c, depth, alt=''):
    return sec_simple('videos', alt, hfs_head('VIDEOS', e(c['videos_title']), e(c['videos_sub']))
                      + f'<div class="vid-grid">{videos_block(c, depth)}</div>')


def sec_about(c, depth, prefix=''):
    h = c['home']
    stats = ''.join(f'<div><b>{e(v)}</b><span>{e(t)}</span></div>' for v, t in h['team_stats'])
    return f'''<section class="block about" id="about">
	<div class="wrap">
		<div class="hf-panel about-panel">
			<div class="sec-head"><div class="kicker">ABOUT</div><h2>{e(h['about_title'])}</h2></div>
			<div class="about-body">{relink(prose(h['about_paras']), prefix)}</div>
			<div class="hf-ab-stats team-stats">{stats}</div>
			<div class="about-body">{relink(prose(h['about_paras2']), prefix)}<p class="about-sign">{e(h['about_sign'])}</p></div>
		</div>
	</div>
</section>
'''


def sec_academy(c, alt=' section-alt'):
    h = c['home']
    return sec_simple('academy', alt, hfs_head('ACADEMY', e(h['acad_title']), e(h['acad_sub'])) + adv_cards(h['acad'])
                      + f'<div class="center-cta"><a class="btn-red" href="{MAIN}/academy/">{e(h["acad_btn"])}</a></div>')


def sec_contact(c, alt=''):
    h = c['home']
    items = ''.join(f'<div class="hf-contact-item"><span class="hf-contact-ico">{icon(i, 20)}</span><div><h4>{e(t)}</h4>{v}</div></div>'
                    for i, t, v in h['contact_items'])
    return sec_simple('contact', alt, hfs_head('CONTACT', e(h['contact_title']), e(h['contact_sub']))
                      + f'<div class="hf-contact">{items}</div>')


def home_cta(c):
    h = c['home']
    return cta_block(h['cta_h'], h['cta_p'], [('w', h['btn1'], MAIN + '/order/'), ('o', c['tek_cta'], MAIN + '/tekeyab/'),
                                              ('o', c['bale_chat'], CONTACT['bale_admin_url'])])


def page_home(c):
    depth = c['depth_home']
    h = c['home']
    svc_base = rel(depth, c['home_rel'] + 'services/')
    sep = '، ' if c['lang'] == 'fa' else ', '
    tag_svcs = sep.join(f'<a href="{svc_base}#{s["key"]}">{e(s["title"])}</a>' for s in c['services'])
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
		<div class="hero-illo"><div class="hero-illo-frame">{img(depth, HOME_IMG, h['hero_alt'], eager=True, picture=True)}</div></div>
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
'''
    est, tek = dict(h['est_feature'], cls=''), dict(h['tek_feature'], cls=' section-alt')
    body += (sec_online(c, depth) + sec_industrial(c, depth) + feature(c, depth, est) + feature(c, depth, tek)
             + sec_works(c, depth, limit=3, alt='') + faq_block(c, h['faq']) + home_cta(c))
    return depth, body


# ---------------------------------------------------------------- hub pages
def hub_page_meta(c, key, hb):
    fa = c['lang'] == 'fa'
    other_home_path, other_rel = ('/en/', 'en/') if fa else ('/', '')
    return {'key': key, 'lang': c['lang'], 'file': c['home_rel'] + hb['slug'] + '/index.html',
            'path': c['home_path'] + hb['slug'] + '/', 'alt_path': other_home_path + hb['slug'] + '/',
            'alt_rel': other_rel + hb['slug'] + '/', 'priority': hb['priority'], 'title': hb['title'], 'desc': hb['desc'],
            'keywords': c['page_home']['keywords'], 'og_img': hb['img'], 'og_alt': hb['crumb']}


def hub_hero(c, depth, key, hb):
    home = rel(depth, c['home_rel']) or './'
    L = NAV_LABELS[c['lang']]
    if key == 'industrial':
        btns = [('btn-red', b[1], b[2]) if k == 0 else ('hfs-btn-ghost', b[1], b[2])
                for k, b in enumerate(c['punching']['cta_btns'][:2])]
    elif key == 'credits':
        btns = []
    else:
        btns = [('btn-red', c['home']['btn1'], MAIN + '/order/'),
                ('hfs-btn-ghost', L['contact'], rel(depth, c['home_rel'] + 'contact/'))]
    b = ''.join(f'<a class="{cls}" href="{u}">{(icon("box", 18) + " ") if cls == "btn-red" else ""}{e(t)}</a>' for cls, t, u in btns)
    return f'''<section class="hfs-hero">
	<div class="wrap">
		<div>
			<div class="hfs-crumb"><a href="{home}">{e(c['brand_name'])}</a> ‹ {e(hb['crumb'])}</div>
			<h1>{hb['h1']}</h1>
			<p class="hfs-lead">{e(hb['lead'])}</p>
			<div class="hfs-hero-btns">{b}</div>
		</div>
		<figure class="hfs-hero-art has-pic">{img(depth, hb['img'], hb['crumb'], eager=True, picture=True)}{credit(c, hb['img'], 'hero-credit')}</figure>
	</div>
</section>
'''


def credits_table(c, depth):
    L = NAV_LABELS[c['lang']]
    head_row = ''.join(f'<th>{e(x)}</th>' for x in L['credits_col'])
    rows = ''
    for f, m in sorted(IMAGE_CREDITS.items()):
        src = 'Vecteezy' if m.get('source') == 'vecteezy' else 'Wikimedia Commons'
        lic = (f'<a href="{m["licurl"]}" rel="license noopener">{e(m["lic"])}</a>' if m.get('licurl') else e(m.get('lic', '')))
        thumb = m.get('poster') or 'assets/img/' + f
        rows += (f'<tr><td class="cr-thumb">{img(depth, thumb, m.get("file", f))}</td>'
                 f'<td>{e(m["artist"])}</td><td>{lic}</td><td><a href="{m["page"]}" rel="noopener">{src}</a></td></tr>')
    return (f'{hfs_head("CREDITS", e(L["credits_title"]))}<div class="hfs-tbl-wrap hfs-scroll"><table class="hfs-tbl credits-tbl">'
            f'<thead><tr>{head_row}</tr></thead><tbody>{rows}</tbody></table></div>')


def page_hub(c, key, hb):
    depth = c['depth_home'] + 1
    h = c['home']
    body = hub_hero(c, depth, key, hb)
    if key == 'services':
        est = dict(h['est_feature'], cls='')
        body += sec_online(c, depth, on_services=True, alt='') + sec_details(c, depth) \
            + stock_block(c, depth, 'services', hb['crumb']) + feature(c, depth, est, '../') \
            + sec_how(c) + home_cta(c)
    elif key == 'industrial':
        ind = dict(h['ind_feature'], cls=' section-alt', id='industrial')
        body += sec_industrial(c, depth, on_hub=True) + feature(c, depth, ind, '../') + sec_why(c) \
            + cta_block(hb['cta_h'], hb['cta_p'], c['punching']['cta_btns'])
    elif key == 'portfolio':
        body += sec_works(c, depth, alt='') + sec_videos(c, depth, alt=' section-alt') + home_cta(c)
    elif key == 'about':
        body += sec_about(c, depth, '../') + sec_why(c, ' section-alt') + sec_how(c, '') + sec_academy(c) + home_cta(c)
    elif key == 'contact':
        body += sec_contact(c) + home_cta(c)
    elif key == 'credits':
        body += sec_simple('credits', '', credits_table(c, depth))
    return depth, body


def hub_schema(c, key, hb, p):
    url = SITE + p['path']
    website_id = SITE + c['home_path'] + '#website'
    ptype = {'about': 'AboutPage', 'contact': 'ContactPage', 'credits': 'WebPage'}.get(key, 'CollectionPage')
    nodes = [org_schema(c), website_node(c),
             {'@type': ptype, '@id': url, 'url': url, 'name': p['title'], 'description': p['desc'], 'inLanguage': c['lang'],
              'dateModified': TODAY, 'isPartOf': {'@id': website_id}, 'about': {'@id': ORG_ID},
              'breadcrumb': {'@id': url + '#breadcrumb'}, 'primaryImageOfPage': image_object(hb['img'], hb['crumb'])},
             {'@type': 'BreadcrumbList', '@id': url + '#breadcrumb', 'itemListElement': [
                 {'@type': 'ListItem', 'position': 1, 'name': c['brand_name'], 'item': SITE + c['home_path']},
                 {'@type': 'ListItem', 'position': 2, 'name': hb['crumb'], 'item': url}]}]
    if key == 'services':
        items = [(s['title'], url + '#' + s['key']) for s in c['services']]
    elif key == 'industrial':
        items = [(c[k]['hero']['crumb'], SITE + c['page_' + k]['path']) for k in INDUSTRIAL_KEYS]
    else:
        items = []
    if items:
        nodes.append({'@type': 'ItemList', 'name': hb['crumb'], 'itemListElement': [
            {'@type': 'ListItem', 'position': k, 'name': n, 'url': u} for k, (n, u) in enumerate(items, 1)]})
    # VideoObject عمداً نیست: ویدیوها روی آپارات‌اند و گوگل بدون uploadDate آن را خطا می‌گیرد
    return nodes


def stock_block(c, depth, page_key, title):
    """کلیپ و عکس‌های آرشیوی یک صفحه، با زیرنویس منبع برای هر کدام؛ اگر چیزی نباشد خروجی ندارد."""
    clips, photos = [], []
    for t in PAGE_TOPICS.get(page_key, []):
        m = MEDIA.get(t) or {}
        if m.get('clip'):
            clips.append(m['clip'])
        photos += m.get('photos', [])
    if not clips and not photos:
        return ''
    note = c['credit']['note']
    out = ''
    for mp4, poster in clips:
        size = img_size(poster)
        wh = f' width="{size[0]}" height="{size[1]}"' if size else ''
        out += (f'<figure class="clip"><video autoplay muted loop playsinline preload="metadata" poster="{rel(depth, poster)}"{wh}>'
                f'<source src="{rel(depth, mp4)}" type="video/mp4"></video>'
                f'<figcaption>{credit(c, mp4, "inline-credit")}</figcaption></figure>')
    if len(clips) > 1:
        out = f'<div class="clip-grid">{out}</div>'
    out += '<div class="stock-grid">' + ''.join(
        f'<figure>{img(depth, ph, title + " — " + note)}<figcaption>{credit(c, ph, "inline-credit")}</figcaption></figure>'
        for ph in photos) + '</div>'
    return (f'<section class="block section-alt" id="in-pictures"><div class="wrap">'
            f'{hfs_head("IN PICTURES", e(title + c["in_pictures"]))}{out}</div></section>\n')


def related_block(c, depth, path):
    """پیوند به همه‌ی صفحه‌های خدمت دیگر؛ هم برای کاربر و هم برای خزنده‌ها."""
    links = [(c['est_name'], c['est_rel']), (c['tek_name'], c['tek_rel'])] + c['industrial_links']
    chips = ''.join(f'<a class="rel-chip" href="{rel(depth, r)}">{e(n)}</a>'
                    for n, r in links if '/' + r != path)
    chips += f'<a class="rel-chip" href="{rel(depth, c["home_rel"] + "services/")}">{e(c["online_services"])}</a>'
    return (f'<section class="block"><div class="wrap">{hfs_head("MORE SERVICES", e(c["related_title"]))}'
            f'<div class="rel-chips">{chips}</div></div></section>\n')


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
        if s.get('gallery'):
            inner += gallery(c, depth, s['gallery'])
        if s.get('figure'):
            g = s['figure']
            inner += (f'<figure class="sec-figure">{img(depth, g["img"], g["alt"])}'
                      f'<figcaption>{e(g["caption"])}{credit(c, g["img"], "inline-credit")}</figcaption></figure>')
        if s.get('video'):
            v = s['video']
            inner += (f'<a class="video-card" href="{v["url"]}" target="_blank" rel="noopener">'
                      f'{img(depth, v["img"], v["alt"])}'
                      f'<span><b>{e(v["title"])}</b>{e(v["desc"])}<em>{e(v["cta"])} {c['arrow']}</em></span></a>')
        sections += f'<section class="block{alt}"><div class="wrap">{inner}</div></section>\n'
    body = (svc_hero(c, depth, d['hero']) + answer_block(c, d) + sections
            + stock_block(c, depth, key, d['hero']['crumb'])
            + related_block(c, depth, c['page_' + key]['path'])
            + faq_block(c, d['faq']) + cta_block(d['cta_h'], d['cta_p'], d['cta_btns']))
    return depth, body


def isolate_ltr(html):
    """شناسه‌هایی مثل @hyperfab_pro در متن راست‌چین وارونه دیده می‌شوند («hyperfab_pro@»)؛
    داخل <bdi> جهتشان جدا حساب می‌شود. فقط متن بیرون از برچسب‌ها و نه ایمیل‌ها."""
    return ''.join(part if part.startswith('<') else re.sub(r'(?<![\w.])(@[A-Za-z0-9_]+)', r'<bdi>\1</bdi>', part)
                   for part in re.split(r'(<[^>]+>)', str(html)))


def answer_block(c, d):
    """پاسخ کوتاه و چند واقعیت کلیدی، درست زیر هیرو؛ برای خواننده‌ی عجول و دستیارهای هوش مصنوعی"""
    answer, facts = d.get('answer'), d.get('key_facts')
    if not answer and not facts:
        return ''
    inner = f'<p class="answer">{isolate_ltr(answer)}</p>' if answer else ''
    if facts:
        inner += '<dl class="key-facts">' + ''.join(
            f'<div><dt>{e(str(k))}</dt><dd>{isolate_ltr(v if "<" in str(v) else e(str(v)))}</dd></div>'
            for k, v in facts) + '</dl>'
    cls = 'answer-card' + (' has-facts' if answer and facts else '')
    label = 'پاسخ کوتاه' if c['lang'] == 'fa' else 'Quick answer'
    return (f'<section class="answer-sec" aria-label="{label}"><div class="wrap">'
            f'<div class="{cls}">{inner}</div></div></section>\n')


WRITTEN = {}


def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full) or ROOT, exist_ok=True)
    if path.endswith('.html'):
        html = fix_tel(html)
        WRITTEN[path] = html
    with open(full, 'w', encoding='utf-8') as fh:
        fh.write(html)
    print('wrote', path)


# ---------------------------------------------------------------- schema enrichment
def city_country(c):
    fa = c['lang'] == 'fa'
    return [{'@type': 'City', 'name': 'تهران' if fa else 'Tehran'},
            {'@type': 'Country', 'name': 'ایران' if fa else 'Iran'}]


def types_of(node):
    t = node.get('@type', [])
    return t if isinstance(t, list) else [t]


def page_schema(c, key, p):
    """گره‌های schema.org صفحه‌ی ابزار/خدمت؛ فایل‌های محتوا دست نمی‌خورند و همه‌چیز اینجا افزوده می‌شود."""
    url = SITE + p['path']
    nodes = copy.deepcopy(c[key]['schema'])
    main_node = next((n for n in nodes if {'Service', 'WebApplication'} & set(types_of(n))), None)
    if main_node is not None:
        main_node.setdefault('@id', url + '#service')
    for n in nodes:
        if 'Service' in types_of(n):
            n['areaServed'] = city_country(c)
            n['availableChannel'] = {
                '@type': 'ServiceChannel', 'serviceUrl': url,
                'servicePhone': {'@type': 'ContactPoint', 'telephone': TEL_MOBILE},
                # inLanguage در schema.org برای Service تعریف نشده؛ زبان خدمت روی کانال آن می‌آید
                'availableLanguage': {'@type': 'Language', 'name': 'Persian' if c['lang'] == 'fa' else 'English',
                                      'alternateName': c['lang']}}
            n['offers'] = {'@type': 'Offer', 'availability': 'https://schema.org/InStock', 'seller': {'@id': ORG_ID}}
    hero = c[key]['hero']
    website_id = SITE + c['home_path'] + '#website'
    webpage = {'@type': 'WebPage', '@id': url, 'url': url, 'name': p['title'], 'description': p['desc'],
               'inLanguage': c['lang'], 'dateModified': TODAY, 'isPartOf': {'@id': website_id},
               'breadcrumb': {'@id': url + '#breadcrumb'},
               'primaryImageOfPage': image_object(hero['img'], hero.get('img_alt', ''))}
    if main_node is not None:
        webpage['about'] = {'@id': main_node['@id']}
    return [org_schema(c), website_node(c), webpage, *nodes,
            {'@type': 'BreadcrumbList', '@id': url + '#breadcrumb', 'itemListElement': [
                {'@type': 'ListItem', 'position': 1, 'name': c['brand_name'], 'item': SITE + c['home_path']},
                {'@type': 'ListItem', 'position': 2, 'name': hero['crumb'], 'item': url}]},
            faq_schema(c[key]['faq'])]


def website_node(c):
    return {'@type': 'WebSite', '@id': SITE + c['home_path'] + '#website', 'url': SITE + c['home_path'],
            'name': c['site_name'], 'inLanguage': c['lang'], 'publisher': {'@id': ORG_ID}}


def check_lengths(p):
    if len(p['title']) > 60:
        warn(f'{p["path"]}: title is {len(p["title"])} chars (> 60): {p["title"]}')
    if len(p['desc']) > 160:
        warn(f'{p["path"]}: description is {len(p["desc"])} chars (> 160)')


def build_lang(c):
    pages = []
    depth, body = page_home(c)
    p = c['page_home']
    p['og_img'], p['og_alt'] = HOME_IMG, c['home']['hero_alt']
    p['schema'] = [org_schema(c), website_node(c),
                   {'@type': 'WebPage', '@id': SITE + c['home_path'], 'url': SITE + c['home_path'], 'name': p['title'],
                    'description': p['desc'], 'inLanguage': c['lang'], 'isPartOf': {'@id': SITE + c['home_path'] + '#website'},
                    'about': {'@id': ORG_ID}, 'dateModified': TODAY,
                    'primaryImageOfPage': image_object(HOME_IMG, c['home']['hero_alt'])},
                   {'@type': 'ItemList', 'name': c['home']['svc_title'], 'itemListElement': [
                       {'@type': 'ListItem', 'position': k, 'item': {
                           '@type': 'Service', 'name': s['title'], 'description': s['paras'][0].replace('<b>', '').replace('</b>', ''),
                           'url': s['url'] if s['url'].startswith('http') else MAIN + s['url'], 'serviceType': s['title'], 'provider': {'@id': ORG_ID},
                           'areaServed': {'@type': 'Country', 'name': c['country']}}}
                       for k, s in enumerate(c['services'] + c['tools_as_services'], 1)]},
                   faq_schema(c['home']['faq'])]
    check_lengths(p)
    write(p['file'], head(c, p, depth) + header(c, p, depth) + body + footer(c, depth))
    pages.append(p)

    for key, hb in HUBS[c['lang']].items():
        p = hub_page_meta(c, key, hb)
        depth, body = page_hub(c, key, hb)
        p['schema'] = hub_schema(c, key, hb, p)
        check_lengths(p)
        write(p['file'], head(c, p, depth) + header(c, p, depth) + body + footer(c, depth))
        pages.append(p)

    for key in c['tool_keys']:
        depth, body = page_tool(c, key)
        p = c['page_' + key]
        p['og_img'], p['og_alt'] = c[key]['hero']['img'], c[key]['hero'].get('img_alt', '')
        p['schema'] = page_schema(c, key, p)
        check_lengths(p)
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


# ---------------------------------------------------------------- llms-full.txt
def text(h, br=' '):
    """HTML کوتاه محتوا → متن ساده"""
    h = re.sub(r'<br\s*/?>', br, str(h))
    h = unescape(re.sub(r'<[^>]+>', '', h))
    return re.sub(r'\s+', ' ', h).strip()


def md_section(title, level=2):
    return f'\n{"#" * level} {text(title)}\n'


def md_items(items):
    return '\n'.join(f'- {x}' for x in items if x) + '\n' if items else ''


def md_table(rows):
    def cell(x):
        return text(x).replace('|', '/')
    out = ['| ' + ' | '.join(cell(x) for x in rows[0]) + ' |', '|' + '---|' * len(rows[0])]
    out += ['| ' + ' | '.join(cell(x) for x in r) + ' |' for r in rows[1:]]
    return '\n'.join(out) + '\n'


def md_faq(faq):
    return md_section('FAQ') + ''.join(f'\n### {text(q)}\n\n{text(a)}\n' for q, a in faq)


def md_paras(paras):
    return ''.join(f'\n{text(x)}\n' for x in paras if x)


def md_home(c):
    h, p = c['home'], c['page_home']
    out = f'# {text(p["title"])}\n\nURL: {SITE}{p["path"]}\n' + md_paras([h['h1'], h['lead'], h['p']])
    out += md_section(h['sum_title']) + md_paras(h['sum_paras'])
    out += md_section(h['svc_title']) + md_paras([h['svc_sub']])
    for s in c['services']:
        out += md_section(s['title'], 3) + md_paras(s['paras'])
        out += md_items([f'{text(a)}: {text(b)}' for a, b in s['specs']])
        out += f'\nURL: {s["url"] if s["url"].startswith("http") else MAIN + s["url"]}\n'
    for f in (h['est_feature'], h['tek_feature'], h['ind_feature']):
        out += md_section(f['title']) + md_paras([f['sub']] + list(f['paras'])) + '\n' + md_items([text(x) for x in f['points']])
    out += md_section(h['why_title']) + '\n' + md_items([f'**{text(t)}**: {text(d)}' for _, t, d in h['why']])
    out += md_section(c['works_title']) + md_paras([c['works_sub']]) + '\n'
    out += md_items([f'**{text(w[c["lang"]][0])}** ({text(w[c["lang"]][1])}): {text(w[c["lang"]][2])}' for w in WORKS])
    out += md_section(h['how_title']) + md_paras([h['how_sub']]) + '\n'
    out += ''.join(f'{k}. **{text(t)}**: {text(d)}\n' for k, (t, d) in enumerate(h['how'], 1))
    out += md_section(h['about_title']) + md_paras(h['about_paras'])
    out += '\n' + md_items([f'{text(v)} {text(t)}' for v, t in h['team_stats']]) + md_paras(h['about_paras2'])
    out += md_section(h['acad_title']) + md_paras([h['acad_sub']]) + '\n' + md_items([f'**{text(t)}**: {text(d)}' for _, t, d in h['acad']])
    out += md_faq(h['faq'])
    out += md_section(h['contact_title']) + md_paras([h['contact_sub']]) + '\n'
    out += md_items([f'{text(t)}: {text(v)}' for _, t, v in h['contact_items']])
    return out


def md_tool(c, key):
    d, p = c[key], c['page_' + key]
    hero = d['hero']
    out = f'# {text(hero["h1"], " — ")}\n\nURL: {SITE}{p["path"]}\n'
    out += md_paras([d.get('answer', ''), hero['lead']])
    if d.get('key_facts'):
        out += '\n' + md_items([f'{text(k)}: {text(v)}' for k, v in d['key_facts']])
    out += '\n' + md_items([f'{text(a)} {text(b)}' for a, b, _ in hero['ticks']])
    for s in d['sections']:
        out += md_section(s['title']) + md_paras([s.get('sub', '')] + list(s.get('paras', [])))
        cards = [f'**{text(t)}**: {text(x)}' for _, t, x in (s.get('why') or []) + (s.get('adv') or [])]
        cards += [text(x) for x in s.get('checks') or []]
        if cards:
            out += '\n' + md_items(cards)
        if s.get('steps'):
            out += '\n' + ''.join(f'{k}. **{text(t)}**: {text(x)}\n' for k, (t, x) in enumerate(s['steps'], 1))
        if s.get('table'):
            out += '\n' + md_table(s['table'])
        if s.get('note'):
            out += md_paras([s['note']])
    return out + md_faq(d['faq'])


def llms_full(langs):
    out = ['# HyperFab (هایپرفب) — full site content\n\n',
           f'> Full text of every page of {SITE}/ in English and Persian, generated from the site sources on {TODAY}. '
           f'English pages come first, then Persian. Short index: {SITE}/llms.txt. '
           f'Main website and online ordering: {MAIN}/\n']
    for c in langs:
        out.append(f'\n---\n\n<!-- language: {c["lang"]} -->\n\n' + md_home(c))
        for key in c['tool_keys']:
            out.append('\n---\n\n' + md_tool(c, key))
    write('llms-full.txt', re.sub(r'\n{3,}', '\n\n', ''.join(out)))


# ---------------------------------------------------------------- CSS purge
SAFE_CLASSES = {'open', 'on', 'hf-js'}  # کلاس‌هایی که اسکریپت روشن/خاموش می‌کند
GROUP_AT = ('@media', '@supports', '@container', '@layer', '@document')


def _skip_string(s, i):
    q = s[i]
    i += 1
    while i < len(s) and s[i] != q:
        i += 2 if s[i] == '\\' else 1
    return i + 1


def _block_end(s, i):
    """اندیس آکولاد بسته‌ی متناظر با بلوکی که از i (بعد از «{») شروع شده"""
    depth = 1
    while i < len(s):
        ch = s[i]
        if ch in '"\'':
            i = _skip_string(s, i)
            continue
        if s.startswith('/*', i):
            i = s.find('*/', i + 2) + 2
            continue
        if ch == '{':
            depth += 1
        elif ch == '}':
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return i


def _strip_comments(s):
    return re.sub(r'/\*.*?\*/', '', s, flags=re.S)


def parse_css(s, i=0):
    """درخت ساده: ('stmt', prelude) | ('group', prelude, children) | ('rule', prelude, body)"""
    items = []
    n = len(s)
    while i < n:
        while i < n and (s[i].isspace() or s.startswith('/*', i)):
            i = s.find('*/', i + 2) + 2 if s.startswith('/*', i) else i + 1
        if i >= n:
            break
        if s[i] == '}':
            return items, i + 1
        start, paren = i, 0
        while i < n:
            ch = s[i]
            if ch in '"\'':
                i = _skip_string(s, i)
                continue
            if s.startswith('/*', i):
                i = s.find('*/', i + 2) + 2
                continue
            if ch == '(':
                paren += 1
            elif ch == ')':
                paren -= 1
            elif paren == 0 and (ch in '{}' or (ch == ';' and s[start] == '@')):
                break
            i += 1
        prelude = re.sub(r'\s+', ' ', _strip_comments(s[start:i])).strip()
        if i >= n:
            break
        if s[i] == ';':
            items.append(('stmt', prelude))
            i += 1
        elif s[i] == '}':
            continue
        elif prelude.lower().startswith(GROUP_AT):
            children, i = parse_css(s, i + 1)
            items.append(('group', prelude, children))
        else:
            j = _block_end(s, i + 1)
            items.append(('rule', prelude, s[i + 1:j]))
            i = j + 1
    return items, i


def _split_top(sel):
    parts, depth, cur = [], 0, ''
    for ch in sel:
        if ch in '([':
            depth += 1
        elif ch in ')]':
            depth -= 1
        if ch == ',' and depth == 0:
            parts.append(cur)
            cur = ''
        else:
            cur += ch
    return parts + [cur]


def selector_can_match(sel, classes, ids):
    s = re.sub(r'\[[^\]]*\]', '', sel)                               # صفت‌ها محدود نمی‌کنند
    s = re.sub(r'::?[\w-]+(\((?:[^()]|\([^()]*\))*\))?', '', s)       # شبه‌کلاس/عنصر و آرگومان‌هایشان
    return (all(x in classes for x in re.findall(r'\.(-?[_a-zA-Z][\w-]*)', s))
            and all(x in ids for x in re.findall(r'#(-?[_a-zA-Z][\w-]*)', s)))


def _min_body(body):
    out = []
    for k, part in enumerate(re.split(r'("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\')', body)):
        if k % 2:
            out.append(part)
            continue
        part = re.sub(r'\s+', ' ', _strip_comments(part))
        out.append(re.sub(r'\s*([;{}])\s*', r'\1', re.sub(r'\s*:\s*', ':', part) if '{' not in part else part))
    return ''.join(out).strip().rstrip(';')


def _min_sel(sel):
    return re.sub(r'\s*([,>])\s*', r'\1', sel)


def emit_css(items, classes, ids):
    out = []
    for it in items:
        if it[0] == 'stmt':
            out.append(it[1] + ';')
        elif it[0] == 'group':
            inner = emit_css(it[2], classes, ids)
            if inner:
                out.append(it[1] + '{' + inner + '}')
        else:
            pre, body = it[1], it[2]
            if pre.startswith('@') or any(selector_can_match(x, classes, ids) for x in _split_top(pre)):
                out.append(_min_sel(pre) + '{' + _min_body(body) + '}')
    return ''.join(out)


def purge_css():
    classes, ids = set(SAFE_CLASSES), set()
    for html in WRITTEN.values():
        for m in re.findall(r'\sclass="([^"]*)"', html):
            classes.update(m.split())
        ids.update(re.findall(r'\sid="([^"]*)"', html))
    src = open(os.path.join(ROOT, 'assets/hyperfab.css'), encoding='utf-8').read()
    items, _ = parse_css(src)
    css = ('/* generated by tools/build.py from hyperfab.css: only rules this site uses. Do not edit. */\n'
           + emit_css(items, classes, ids) + '\n')
    write('assets/hyperfab.min.css', css)
    print(f'CSS: hyperfab.css {len(src.encode()):,} B -> hyperfab.min.css {len(css.encode()):,} B '
          f'({100 - 100 * len(css.encode()) / len(src.encode()):.0f}% smaller)')


# ---------------------------------------------------------------- checks
def check_links():
    """هر href/src داخلی باید به فایلی موجود برسد"""
    for path, html in WRITTEN.items():
        base = os.path.dirname(path)
        for ref in re.findall(r'\s(?:href|src|srcset)="([^"]+)"', html):
            if re.match(r'^(?:[a-z]+:|//|#)', ref):
                continue
            ref = ref.split('#')[0].split('?')[0]
            target = os.path.normpath(os.path.join(ROOT, base, ref))
            if ref.endswith('/') or os.path.isdir(target):
                target = os.path.join(target, 'index.html')
            if not os.path.exists(target):
                warn(f'{path}: missing target {ref}')


def main():
    pages = []
    for c in (content_fa.C, content_en.C):
        for p in ['page_home'] + ['page_' + k for k in c['tool_keys']]:
            c[p]['lang'] = c['lang']
        pages += build_lang(c)
    sitemap(pages)
    llms_full((content_en.C, content_fa.C))
    purge_css()
    check_links()
    if WARNINGS:
        print(f'{len(WARNINGS)} warning(s)')


if __name__ == '__main__':
    main()
