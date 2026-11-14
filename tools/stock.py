"""عکس‌ها و کلیپ‌های آرشیوی هر خدمت (Vecteezy، مجوز رایگان با ذکر منبع).

MEDIA[موضوع] = {'clip': (mp4, پوستر) یا None, 'photos': [فایل، ...]}
منبع و مجوز هر فایل در images.py ثبت است؛ زیرنویس منبع از همان‌جا ساخته می‌شود.
"""
MEDIA = {}

# صفحه‌ی هر خدمت ← موضوع(های) آرشیوی آن
PAGE_TOPICS = {
    'punching': ['punching'], 'injection': ['injection'], 'turning': ['turning'], 'extrusion': ['extrusion'],
    'welding': ['welding'], 'plating': ['plating'], 'coating': ['coating'],
    'services': ['printing3d', 'laser', 'bending'],
}
