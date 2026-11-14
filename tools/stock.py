"""عکس‌ها و کلیپ‌های آرشیوی هر خدمت (Vecteezy، مجوز رایگان با ذکر منبع).

MEDIA[موضوع] = {'clip': (mp4, پوستر) یا None, 'photos': [فایل، ...]}
منبع و مجوز هر فایل در images.py ثبت است؛ زیرنویس منبع از همان‌جا ساخته می‌شود.
"""
MEDIA = {'bending': {'clip': None,
             'photos': ['assets/img/stock/bending-1.jpg', 'assets/img/stock/bending-2.jpg', 'assets/img/stock/bending-3.jpg']},
 'coating': {'clip': None, 'photos': ['assets/img/stock/coating-1.jpg', 'assets/img/stock/coating-2.jpg']},
 'extrusion': {'clip': None,
               'photos': ['assets/img/stock/extrusion-1.jpg', 'assets/img/stock/extrusion-2.jpg', 'assets/img/stock/extrusion-3.jpg']},
 'injection': {'clip': None,
               'photos': ['assets/img/stock/injection-1.jpg', 'assets/img/stock/injection-2.jpg', 'assets/img/stock/injection-3.jpg']},
 'laser': {'clip': None, 'photos': ['assets/img/stock/laser-1.jpg', 'assets/img/stock/laser-2.jpg', 'assets/img/stock/laser-3.jpg']},
 'plating': {'clip': None, 'photos': ['assets/img/stock/plating-1.jpg', 'assets/img/stock/plating-2.jpg']},
 'printing3d': {'clip': None,
                'photos': ['assets/img/stock/printing3d-1.jpg', 'assets/img/stock/printing3d-2.jpg', 'assets/img/stock/printing3d-3.jpg']},
 'punching': {'clip': None,
              'photos': ['assets/img/stock/punching-1.jpg', 'assets/img/stock/punching-2.jpg', 'assets/img/stock/punching-3.jpg']},
 'turning': {'clip': None,
             'photos': ['assets/img/stock/turning-1.jpg', 'assets/img/stock/turning-2.jpg', 'assets/img/stock/turning-3.jpg']},
 'welding': {'clip': None,
             'photos': ['assets/img/stock/welding-1.jpg', 'assets/img/stock/welding-2.jpg', 'assets/img/stock/welding-3.jpg']}}

# صفحه‌ی هر خدمت ← موضوع(های) آرشیوی آن
PAGE_TOPICS = {
    'punching': ['punching'], 'injection': ['injection'], 'turning': ['turning'], 'extrusion': ['extrusion'],
    'welding': ['welding'], 'plating': ['plating'], 'coating': ['coating'],
    'services': ['printing3d', 'laser', 'bending'],
}
