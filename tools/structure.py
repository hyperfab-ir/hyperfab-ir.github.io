"""ساختار چندصفحه‌ای سایت: صفحه‌های مادر (hub)، منوی اصلی با زیرمنو، و پیوندهای پابرگ.

هر صفحه‌ی مادر چند بخش از داده‌های موجود (content_*.py و industrial*.py) را کنار هم
می‌گذارد؛ اینجا فقط عنوان، توضیح، تیتر و تصویر سربرگ هر صفحه آمده است.
"""

# صفحه‌های خدمت صنعتی، به ترتیب نمایش در کارت‌ها و زیرمنو
INDUSTRIAL_KEYS = ['punching', 'injection', 'turning', 'extrusion', 'welding', 'plating', 'coating']

HUBS = {
    'fa': {
        'services': {
            'slug': 'services', 'priority': '0.9', 'img': 'assets/img/hero-parts.png',
            'title': 'خدمات ساخت آنلاین قطعه در تهران | هایپرفب',
            'desc': 'پرینت سه‌بعدی FDM و رزینی، ماشین‌کاری CNC، برش لیزر فلزات و غیرفلزات و خم‌کاری ورق در هایپرفب تهران؛ قیمت آنلاین و ارسال به سراسر ایران.',
            'crumb': 'خدمات آنلاین',
            'h1': '<em>خدمات ساخت آنلاین قطعه</em><br>پرینت سه‌بعدی، CNC، لیزر و خم‌کاری',
            'lead': 'فایل طرح را در hyperfab.ir بارگذاری کنید؛ برای پرینت سه‌بعدی FDM و برش لیزر قیمت همان لحظه نمایش داده می‌شود و برای روش‌های دیگر پس از بررسی کارشناس. حداقل سفارش یک قطعه است و ارسال به سراسر ایران انجام می‌شود.',
        },
        'industrial': {
            'slug': 'industrial', 'priority': '0.9', 'img': 'assets/img/works/flange-steel-2.jpg',
            'title': 'تولید صنعتی و تیراژی قطعات در تهران | هایپرفب',
            'desc': 'پانچ، قالب‌سازی و تزریق پلاستیک، تراشکاری CNC تیراژی، اکسترود آلومینیوم، جوشکاری، آبکاری و رنگ کوره‌ای در هایپرفب تهران؛ مشاوره‌ی تلفنی.',
            'crumb': 'تولید صنعتی',
            'h1': '<em>تولید صنعتی و تیراژی</em><br>از قالب و تراش تا جوش، آبکاری و رنگ',
            'lead': 'وقتی قطعه از نمونه به تیراژ می‌رسد، هایپرفب زنجیره‌ی کامل ساخت را از بررسی طرح تا تحویل قطعه پیش می‌برد: هفت خدمت صنعتی با یک گروه مهندسی مسئول. سفارش و مشاوره‌ی این خدمات تلفنی است.',
            'cta_h': 'پروژه‌ی صنعتی خود را با ما در میان بگذارید',
            'cta_p': 'نقشه یا نمونه‌ی قطعه را بفرستید یا تماس بگیرید. کارشناس پروژه‌های صنعتی هایپرفب تلفنی پاسخ‌گوی شماست.',
        },
        'portfolio': {
            'slug': 'portfolio', 'priority': '0.8', 'img': 'assets/img/works/ptfe-part-1.jpg',
            'title': 'نمونه‌کارها و ویدیوهای هایپرفب | ساخت قطعه در تهران',
            'desc': 'عکس‌های واقعی قطعاتی که هایپرفب ساخته است، از تراشکاری CNC و قطعات تفلونی تیراژی تا مجموعه‌ی استیلی جوشکاری‌شده، و ویدیوهای هایپرفب در آپارات.',
            'crumb': 'نمونه‌کارها',
            'h1': '<em>نمونه‌کارهای واقعی</em> و ویدیوهای هایپرفب',
            'lead': 'عکس‌های این صفحه از کار واقعی هایپرفب است: قطعات تراشکاری CNC، قطعات و واشرهای تفلونی تیراژی، توپی CK45، شفت هزارخاری و مجموعه‌ی آب‌بند استیلی که تراش خورده، جوش داده شده و تست PT شده است.',
        },
        'about': {
            'slug': 'about', 'priority': '0.7', 'img': 'assets/img/about-hero.webp',
            'title': 'درباره‌ی هایپرفب | گروه مهندسی ساخت قطعه در تهران',
            'desc': 'هایپرفب، پلتفرم ساخت قطعه در تهران با گروه مهندسی از دانشگاه‌های برتر کشور؛ سابقه‌ی ۴ قالب تزریق، ۸۰٬۰۰۰ قطعه و ۸٬۰۰۰ لوله‌ی پانچ‌شده.',
            'crumb': 'درباره‌ی ما',
            'h1': '<em>درباره‌ی هایپرفب</em><br>ما قطعه می‌سازیم. سال‌هاست.',
            'lead': 'هایپرفب از دل کارگاه بیرون آمده، نه از دل یک اسلاید. گروه مهندسی هایپرفب پیش از روشن‌شدن دستگاه، فایل شما را از نظر ساخت‌پذیری، جنس و روش تولید بررسی می‌کند و قیمت و زمان را شفاف می‌گوید.',
        },
        'contact': {
            'slug': 'contact', 'priority': '0.7', 'img': 'assets/img/works/flange-steel-3.jpg',
            'title': 'تماس با هایپرفب | نشانی، تلفن و ساعات کاری در تهران',
            'desc': 'نشانی هایپرفب در تهران، تلفن ۰۲۱-۷۷۵۲۷۴۳۸، موبایل و بله و تلگرام ۰۹۹۶۲۲۳۳۸۹۸، ایمیل info@hyperfab.ir و ساعات کاری؛ ثبت سفارش آنلاین ۲۴ ساعته.',
            'crumb': 'تماس',
            'h1': '<em>تماس با هایپرفب</em>',
            'lead': 'برای سفارش آنلاین به hyperfab.ir بروید. برای پروژه‌های صنعتی، مشاوره و هر سؤالی پیش از سفارش، تلفنی یا در پیام‌رسان بله با هایپرفب در تماس باشید.',
        },
        'credits': {
            'slug': 'credits', 'priority': '0.3', 'img': 'assets/img/arc-tig-stainless.jpg',
            'title': 'اعتبار تصاویر | هایپرفب',
            'desc': 'منبع، عکاس و مجوز تصاویر آرشیوی سایت هایپرفب که برای روشن‌تر شدن خدمات از ویکی‌مدیا کامنز آمده‌اند.',
            'crumb': 'اعتبار تصاویر',
            'h1': '<em>اعتبار تصاویر</em>',
            'lead': 'عکس‌های برچسب‌دار «عکس واقعی» از کار خود هایپرفب‌اند. بقیه‌ی عکس‌ها تصویر آرشیوی با مجوز آزادند و فقط برای روشن‌تر شدن خدمات آمده‌اند؛ منبع و مجوز هر کدام اینجاست.',
        },
    },
    'en': {
        'services': {
            'slug': 'services', 'priority': '0.8', 'img': 'assets/img/hero-parts.png',
            'title': 'Online Manufacturing Services in Tehran, Iran | HyperFab',
            'desc': 'FDM and resin 3D printing, CNC machining, metal and non-metal laser cutting and sheet bending by HyperFab, Tehran: instant online quotes, Iran-wide shipping.',
            'crumb': 'Online services',
            'h1': '<em>Online manufacturing services</em><br>3D printing, CNC, laser cutting and bending',
            'lead': 'Upload your design on hyperfab.ir: FDM 3D printing and laser cutting are priced instantly, other processes after an engineer’s review. The minimum order is one part, and parts ship across Iran.',
        },
        'industrial': {
            'slug': 'industrial', 'priority': '0.8', 'img': 'assets/img/works/flange-steel-2.jpg',
            'title': 'Industrial & Batch Production in Tehran, Iran | HyperFab',
            'desc': 'Punching, injection moulding, batch CNC turning, aluminium extrusion, welding, plating and powder coating by HyperFab in Tehran, Iran.',
            'crumb': 'Industrial production',
            'h1': '<em>Industrial and batch production</em><br>From moulds and turning to welding, plating and coating',
            'lead': 'When a part moves from prototype to volume, HyperFab runs the whole chain from design review to delivery: seven industrial services with one responsible engineering team. These services are arranged by phone.',
            'cta_h': 'Tell us about your industrial project',
            'cta_p': 'Send a drawing or a sample part, or call. HyperFab’s industrial projects specialist answers by phone.',
        },
        'portfolio': {
            'slug': 'portfolio', 'priority': '0.7', 'img': 'assets/img/works/ptfe-part-1.jpg',
            'title': 'HyperFab Portfolio & Videos | Parts Made in Tehran',
            'desc': 'Real photos of parts made by HyperFab, from CNC turning and batch PTFE parts to a welded and PT-tested stainless assembly, plus HyperFab videos on Aparat.',
            'crumb': 'Portfolio',
            'h1': '<em>Real HyperFab work</em> and videos',
            'lead': 'The photos on this page show HyperFab’s real work: CNC-turned parts, batch PTFE parts and gaskets, a CK45 hub, a splined shaft and a stainless sealing assembly that was turned, welded and PT-tested.',
        },
        'about': {
            'slug': 'about', 'priority': '0.6', 'img': 'assets/img/about-hero.webp',
            'title': 'About HyperFab | Manufacturing Engineers in Tehran, Iran',
            'desc': 'HyperFab is a manufacturing platform in Tehran run by engineers from Iran’s top universities; 4 injection moulds, 80,000 parts and 8,000 punched tubes.',
            'crumb': 'About',
            'h1': '<em>About HyperFab</em><br>We make parts. We have for years.',
            'lead': 'HyperFab grew out of the workshop, not out of a slide deck. Before any machine starts, HyperFab’s engineers review your file for manufacturability, material and process, and give a clear price and timeline.',
        },
        'contact': {
            'slug': 'contact', 'priority': '0.6', 'img': 'assets/img/works/flange-steel-3.jpg',
            'title': 'Contact HyperFab | Address, Phone and Hours, Tehran',
            'desc': 'HyperFab’s address in Tehran, phone +98 21 7752 7438, mobile, Bale and Telegram +98 996 223 3898, email info@hyperfab.ir and hours; online ordering 24/7.',
            'crumb': 'Contact',
            'h1': '<em>Contact HyperFab</em>',
            'lead': 'Order online at hyperfab.ir. For industrial projects, advice and any question before ordering, contact HyperFab by phone or on the Bale messenger.',
        },
        'credits': {
            'slug': 'credits', 'priority': '0.2', 'img': 'assets/img/arc-tig-stainless.jpg',
            'title': 'Image Credits | HyperFab',
            'desc': 'Source, photographer and licence of the archive images on the HyperFab site, used from Wikimedia Commons to illustrate the services.',
            'crumb': 'Image credits',
            'h1': '<em>Image credits</em>',
            'lead': 'Photos labelled “Real HyperFab photo” show HyperFab’s own work. The other photos are freely licensed archive images used only to illustrate the services; their source and licence are listed here.',
        },
    },
}

NAV_LABELS = {
    'fa': {'home': 'معرفی', 'services': 'خدمات آنلاین', 'industrial': 'تولید صنعتی', 'tools': 'ابزارها',
           'portfolio': 'نمونه‌کارها', 'about': 'درباره‌ی ما', 'contact': 'تماس', 'all_services': 'همه‌ی خدمات آنلاین',
           'all_industrial': 'همه‌ی خدمات صنعتی', 'toggle_open': 'باز کردن زیرمنو', 'toggle_close': 'بستن زیرمنو',
           'industrial_btn': 'همه‌ی خدمات صنعتی', 'works_btn': 'همه‌ی نمونه‌کارها و ویدیوها',
           'credits_title': 'تصاویر آرشیوی', 'credits_col': ('تصویر', 'عکاس', 'مجوز', 'منبع'), 'used_on': 'منبع',
           'site_pages': [('خدمات آنلاین', 'services/'), ('تولید صنعتی', 'industrial/'), ('نمونه‌کارها', 'portfolio/'),
                          ('درباره‌ی ما', 'about/'), ('تماس', 'contact/'), ('اعتبار تصاویر', 'credits/')]},
    'en': {'home': 'Overview', 'services': 'Online services', 'industrial': 'Industrial', 'tools': 'Tools',
           'portfolio': 'Portfolio', 'about': 'About', 'contact': 'Contact', 'all_services': 'All online services',
           'all_industrial': 'All industrial services', 'toggle_open': 'Open submenu', 'toggle_close': 'Close submenu',
           'industrial_btn': 'All industrial services', 'works_btn': 'All work and videos',
           'credits_title': 'Archive images', 'credits_col': ('Image', 'Photographer', 'Licence', 'Source'), 'used_on': 'Source',
           'site_pages': [('Online services', 'services/'), ('Industrial production', 'industrial/'), ('Portfolio', 'portfolio/'),
                          ('About', 'about/'), ('Contact', 'contact/'), ('Image credits', 'credits/')]},
}
