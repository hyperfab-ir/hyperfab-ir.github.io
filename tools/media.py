"""رسانه‌های واقعی هایپرفب: نمونه‌کارها (از inc-portfolio.php قالب ۲۰٫۰) و ویدیوهای آپارات (از inc-videos.php).
این‌ها عکس و فیلم خود هایپرفب‌اند و زیرنویس منبع آرشیوی نمی‌گیرند."""

WORKS = [
    {'img': 'assets/img/works/flange-steel-2.jpg', 'more': ['flange-steel-3', 'flange-steel-5', 'flange-steel-6'],
     'fa': ('مجموعه‌ی آب‌بند استیل ۳۰۴، تراشکاری CNC و جوش آرگون', 'استیل ۳۰۴ · صنایع فرآیندی',
            'ساخت کامل در هایپرفب: تراشکاری و سوراخ‌کاری دقیق CNC، جوش آرگون قطعات و تست PT جوش برای اطمینان از سلامت اتصال؛ با کنترل ابعادی نهایی مطابق نقشه، برای کاربرد صنعتی تحت فشار.'),
     'en': ('AISI 304 stainless sealing assembly, CNC-turned and TIG-welded', 'AISI 304 stainless · process industry',
            'Made end to end by HyperFab: precision CNC turning and drilling, TIG welding of the parts and a PT test of the welds to confirm joint integrity, with final dimensional inspection to the drawing, for a pressurised industrial application.')},
    {'img': 'assets/img/works/ptfe-part-1.jpg', 'more': ['ptfe-part-4', 'ptfe-part-3'],
     'fa': ('قطعه و واشر تفلون (PTFE) تراشکاری‌شده با CNC', 'تفلون PTFE · صنایع شیمیایی',
            'قطعات و واشرهای تفلونی با تراشکاری دقیق CNC، به‌صورت تیراژی. تلرانس‌ها برای آب‌بندی بدون نشتی در محیط خورنده رعایت شده است.'),
     'en': ('CNC-turned PTFE parts and gaskets', 'PTFE · chemical industry',
            'PTFE parts and gaskets CNC-turned in a production run, with tolerances held for leak-free sealing in corrosive service.')},
    {'img': 'assets/img/works/alu-cone-1.jpg', 'more': [],
     'fa': ('توپی فولادی CK45 تراشکاری‌شده با CNC', 'فولاد CK45 · صنعتی',
            'توپی فولادی با تراشکاری دقیق CNC؛ شیارها و پله‌ها با تلرانس دقیق برای قطعات دوّار و یاتاقان‌بندی.'),
     'en': ('CNC-turned CK45 steel hub', 'CK45 (C45) steel · industrial',
            'A CNC-turned steel hub with grooves and steps held to tight tolerances for rotating and bearing applications.')},
    {'img': 'assets/img/works/spline-shaft-1.jpg', 'more': [],
     'fa': ('شفت فولادی ماشین‌کاری‌شده با هزارخار در دو سر', 'فولاد · مکانیک و خودرو',
            'شفت با هزارخار در هر دو انتها برای انتقال گشتاور بالا؛ ماشین‌کاری دقیق برای درگیری کامل و بدون لقی.'),
     'en': ('Machined steel shaft splined at both ends', 'Steel · mechanical and automotive',
            'A shaft with splines at both ends for high-torque transmission, machined for full, backlash-free engagement.')},
    {'img': 'assets/img/works/steel-bush-1.jpg', 'more': [],
     'fa': ('بوش استیل ۳۰۴ تراشکاری‌شده', 'استیل ۳۰۴ · صنعتی',
            'بوش استیل با پله‌ها و شیارهای دقیق و سطح پرداخت تمیز، برای یاتاقان‌بندی و مواضع نیازمند ابعاد دقیق.'),
     'en': ('Turned AISI 304 stainless steel bushing', 'AISI 304 stainless · industrial',
            'A stainless bushing with precise steps and grooves and a clean finish, for bearing seats and other precision locations.')},
    {'img': 'assets/img/works/misc-parts-1.jpg', 'more': [],
     'fa': ('قطعات دقیق خارج از محور از برنج، استیل و پلیمر', 'برنج، استیل و پلیمر · مکانیزم',
            'مجموعه‌ای از قطعات کوچک و دقیق، از جمله قطعات خارج از محور، از برنج، استیل و پلیمر در یک پروژه، با کنترل ابعادی موشکافانه.'),
     'en': ('Precision off-axis parts in brass, stainless steel and polymer', 'Brass, stainless and polymer · mechanisms',
            'A set of small precision parts, including off-axis parts, in brass, stainless steel and polymer, made in one project with meticulous dimensional inspection.')},
]

VIDEOS = [
    ('poq88kr', 'tekeyab', ('تکه‌یاب: خرید تکه‌ی کوچک متریال صنعتی', 'قیمت تکه‌ی متریال را بدون تلفن پشت تلفن بگیرید.'),
     ('Tekeyab: buying small pieces of industrial material', 'Get a price for a piece of material without calling around.')),
    ('dne9rlc', 'multicolor-1', ('پرینت سه‌بعدی چندرنگ، قسمت ۱', 'هر بار که رنگ عوض می‌شود، داخل پرینتر چه می‌گذرد؟'),
     ('Multi-colour 3D printing, part 1', 'What happens inside the printer at every colour change?')),
    ('ghz7235', 'multicolor-2', ('پرینت سه‌بعدی چندرنگ، قسمت ۲', 'چرا پرینت رنگی این‌قدر پرتی دارد؟'),
     ('Multi-colour 3D printing, part 2', 'Why does colour 3D printing waste so much material?')),
    ('rbthfo9', 'gripper', ('گریپر پرینت سه‌بعدی: از یک عکس در گوشی تا قطعه‌ی واقعی', 'یک لینک از میکرورلد و چند روز بعد، گریپر در دست.'),
     ('3D-printed gripper: from a photo on a phone to a real part', 'One link to a model online, and a few days later the gripper is in hand.')),
    ('efnzfq6', 'order-guide', ('آموزش سفارش پرینت سه‌بعدی', 'سفارش از سایت هایپرفب در سه قدم.'),
     ('How to order a 3D print', 'Ordering on the HyperFab website in three steps.')),
    ('gqyd926', 'dragon', ('اژدهای مفصلی یک‌تکه با پرینت سه‌بعدی', 'مفصل‌های تودرتو، یک‌تکه از پرینتر.'),
     ('One-piece 3D-printed articulated dragon', 'Interlocking joints, printed in one piece.')),
    ('kxxl13o', 'print-price', ('زمان، یعنی قیمت پرینت سه‌بعدی', 'چرا زمان چاپ قیمت پرینت سه‌بعدی را تعیین می‌کند.'),
     ('Time is price in 3D printing', 'Why print time sets the price of a 3D print.')),
    ('knzjkwm', 'dino-battle', ('نبرد دایناسورهای مفصلی پرینت‌شده', 'سه دایناسور مفصلی رو در روی هم؛ کدام برنده است؟'),
     ('Battle of 3D-printed articulated dinosaurs', 'Three articulated printed dinosaurs face off. Which one wins?')),
]


def video_url(code):
    return 'https://www.aparat.com/v/' + code


def video_embed(code):
    return 'https://www.aparat.com/video/video/embed/videohash/' + code + '/vt/frame'
