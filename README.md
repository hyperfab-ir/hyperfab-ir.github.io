# hyperfab-ir.github.io

صفحه‌ی معرفی رسمی **هایپرفب** (HyperFab) روی GitHub Pages، به فارسی و انگلیسی.
سایت اصلی و ثبت سفارش: https://hyperfab.ir

هدف این سایت این است که موتورهای جست‌وجو و دستیارهای هوش مصنوعی (ChatGPT، Claude، Perplexity، Gemini و …)
که به سرورهای داخل ایران دسترسی ندارند، خدمات هایپرفب را ببینند و به hyperfab.ir ارجاع دهند.

## ساختار

| مسیر | محتوا |
|---|---|
| `/` و `/en/` | صفحه‌ی اصلی: همه‌ی خدمات، تخمین‌گر قیمت، تکه‌یاب، تیم، سؤالات متداول، تماس |
| `/price-estimator/` و `/en/price-estimator/` | تخمین‌گر آنلاین قیمت |
| `/tekeyab/` و `/en/tekeyab/` | تکه‌یاب |
| `/punching/`، `/injection-molding/`، `/cnc-turning/`، `/aluminium-extrusion/`، `/welding/`، `/plating-anodizing/`، `/powder-coating/` (و نسخه‌ی `/en/` هر کدام) | خدمات تولید صنعتی و تیراژی؛ سفارش تلفنی |
| `robots.txt`، `sitemap.xml`، `llms.txt` | راهنمای خزنده‌ها و هوش مصنوعی |

## ویرایش

صفحه‌های HTML دستی ویرایش نمی‌شوند؛ از روی متن‌های `tools/` ساخته می‌شوند.

1. متن فارسی را در `tools/content_fa.py` و انگلیسی را در `tools/content_en.py` ویرایش کنید.
   خدمات صنعتی در `tools/industrial_*.py` و `tools/industrial2_*.py` هستند،
   نمونه‌کارها و ویدیوهای واقعی در `tools/media.py`، و اطلاعات تماس مشترک در `tools/common.py`.
2. اجرا کنید (پایتون ۳٫۱۲ یا بالاتر):

   ```bash
   python3 tools/build.py
   ```
3. کامیت و پوش کنید؛ GitHub Pages ظرف یکی دو دقیقه به‌روز می‌شود.

ظاهر از فایل `style.css` قالب وردپرس هایپرفب ۲۰٫۰ می‌آید (`assets/hyperfab.css`، بی‌تغییر).
افزوده‌های این سایت در `assets/site.css` است. اگر قالب سایت اصلی به‌روز شد، کافی است `style.css` تازه را
جای `assets/hyperfab.css` بگذارید.

## تصاویر

- `assets/img/works/` و `assets/img/real-*.jpg`: عکس‌های واقعی کار هایپرفب (از قالب سایت اصلی). روی سایت برچسب «عکس واقعی» دارند.
- `assets/img/videos/`: کاور ویدیوهای آپارات هایپرفب.
- `assets/img/arc-*.jpg`: تصاویر آرشیوی از Wikimedia Commons با مجوز آزاد. نام عکاس، مجوز و پیوند منبع هر کدام
  در `tools/images.py` ثبت است و زیر هر تصویر روی سایت نمایش داده می‌شود. هر وقت عکس واقعی از همان خدمت
  داشتید، جایگزینش کنید و ردیفش را از `tools/images.py` بردارید.
