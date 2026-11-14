"""Industrial production services (punching, mould making and injection moulding) — English.
Mirrors industrial_fa.py. Ordering is by phone, so buttons go to phone and Bale, not hyperfab.ir."""
from common import SITE, MAIN, CONTACT

TEL = 'tel:+989962233898'
TEL_EN = '+98 996 223 3898'

CTA_BTNS = [('w', 'Call ' + TEL_EN, TEL), ('o', 'Chat on Bale', CONTACT['bale_pro_url']),
            ('o', 'Email', 'mailto:' + CONTACT['email'])]

PRICE_NOTE = ('<b>Note:</b> the tooling cost is paid once and spread across the run; '
              'the larger the quantity, the smaller the tooling share of each part’s price.')

PUNCHING = {
    'depth': 2,
    'hero': {
        'crumb': 'Sheet & Tube Punching',
        'h1': '<em>Sheet and tube punching</em><br>From die design to production runs',
        'lead': 'Holes, slots and custom shapes in metal and polyethylene sheet and tube. HyperFab designs and builds the punching die, runs a trial sample for your approval, and carries production through to delivery with full quality control.',
        'ticks': [('Punching:', 'sheet and tube', False), ('Materials:', 'metals and polymers, including polyethylene', False),
                  ('Pricing:', 'die cost + cost per stroke, by geometry and material', False)],
        'buttons': [('btn-red', 'Call for a project consultation', TEL), ('hfs-btn-ghost', 'Chat on Bale', CONTACT['bale_pro_url'])],
        'img': 'assets/img/mat-sheet-metal.webp', 'img_alt': 'Punched metal sheet with a repeating hole pattern',
        'stats': [('target', '8,000', 'tubes', 'punched in one industrial project'), ('ruler', '125', 'mm', 'polyethylene pipe punched'),
                  ('layers', '2', 'stages', 'die making and production'), ('shield', '1', 'owner', 'from design to delivery')],
    },
    'sections': [
        {'kicker': 'WHAT IT IS', 'title': 'What punching is and what HyperFab does', 'id': 'what',
         'paras': [
             '<b>Punching</b> creates holes, slots and shaped cut-outs in sheet and tube with a press stroke and a die. For repeat quantities it is one of the fastest and most economical processes. Once the die is made, each part reaches its final shape in one or a few strokes, and every part comes out the same.',
             'HyperFab handles punching end to end. The drawing is reviewed, a punching die is designed and built for the material and thickness, and a trial sample is punched for your approval. Production and quality control then run through to delivery. The service covers both sheet and tube, in metal and in polymers such as polyethylene.',
             'Punching polymer pipe is one of the hard jobs in this field. The pipe is round, the wall deforms under the stroke, and polyethylene behaves very differently from metal. HyperFab’s team has punched kidney-shaped slots in polyethylene pipe with a 125 mm diameter, 5 mm wall and 6-bar pressure rating. In another industrial project, the team was responsible for quality control of 8,000 punched tubes.',
         ]},
        {'kicker': 'WHAT WE PUNCH', 'title': 'What we punch', 'id': 'scope',
         'adv': [
             ('sheet', 'Metal sheet punching', 'Round and square holes, slots, repeating patterns and custom shapes in mild steel, galvanised, stainless steel and aluminium sheet.'),
             ('layers', 'Metal tube and profile punching', 'Holes and slots in metal tube and profile for structures, fittings, shelving, railings and furniture.'),
             ('cube', 'Polyethylene pipe punching', 'Slots and holes in polyethylene pipe, including kidney-shaped slots, for drainage, filter and distribution pipes.'),
             ('stack', 'Polymer sheet punching', 'Polyethylene and engineering-plastic sheet for gaskets, perforated plates and flat punched parts.'),
             ('target', 'Custom shapes', 'From a simple round hole to kidney slots, perforated patterns and special forms, exactly to your drawing.'),
             ('chart', 'Repeatable production runs', 'Once the die is built, parts are produced with identical strokes and dimensions stay consistent from the first part to the last.'),
         ]},
        {'kicker': 'PRICING', 'title': 'How punching is priced', 'id': 'pricing',
         'sub': 'Each project has two cost components, quoted separately. Both depend on the part’s geometry and the material being punched.',
         'table': [
             ('Cost component', 'What it depends on'),
             ('Punching die (one-off)', 'Geometry and number of holes and slots, required accuracy, material and thickness, and whether the die is simple, progressive or tube-specific'),
             ('Per stroke (production)', 'Material and thickness, strokes needed per part, and run quantity'),
             ('Material', 'At current prices, if HyperFab supplies the sheet or tube'),
         ],
         'note': PRICE_NOTE},
        {'kicker': 'WHY HYPERFAB', 'title': 'Why trust HyperFab with a punching project', 'id': 'why',
         'why': [
             ('file', 'Engineering before the die', 'The die is the most expensive part of the project. Before it is built, the design is reviewed from the die’s point of view: hole-to-edge distance, hole-diameter-to-thickness ratio and how the material behaves under the stroke. The goal is to build the die once, and build it right.'),
             ('target', 'Real tube-punching experience', 'From quality control of 8,000 punched tubes to kidney slots in 125 mm polyethylene pipe, we know the practical problems of this work first-hand.'),
             ('shield', 'Full responsibility to delivery', 'From die design to the last stroke, the project has one owner: HyperFab. You approve a sample before production, and parts are inspected before delivery.'),
         ]},
        {'kicker': 'HOW IT WORKS', 'title': 'How a punching project runs', 'id': 'steps',
         'steps': [
             ('Send drawing and specs', 'Send the part drawing, material, thickness and quantity, or describe them by phone. A physical sample also works.'),
             ('Engineering review', 'The design is checked for die manufacturability and changes are suggested where needed.'),
             ('Quotation', 'Die cost and cost per stroke are quoted separately and clearly.'),
             ('Die and sample', 'The die is built and a trial sample is punched for your approval before production.'),
             ('Production and delivery', 'Parts are produced with dimensional quality control, packed and delivered.'),
         ]},
        {'kicker': 'APPLICATIONS', 'title': 'Applications of sheet and tube punching', 'id': 'uses',
         'checks': [
             '<b>Drainage and dewatering pipes</b> with repeating slots or holes.',
             '<b>Filter and strainer pipes</b>, and water and air distribution pipes.',
             '<b>Perforated plates</b>, meshes and ventilation grilles.',
             '<b>Flat punched parts for assembly</b> such as washers, brackets and mounting plates.',
             '<b>Housings and panels for industrial equipment</b> with fixed hole patterns.',
             '<b>Perforated profile and tube</b> for structures, shelving and furniture.',
         ]},
    ],
    'faq': [
        ('Does HyperFab punch polyethylene pipe?', 'Yes. HyperFab has punched kidney-shaped slots in polyethylene pipe with a 125 mm diameter, 5 mm wall and 6-bar pressure rating. Metal tube and sheet punching is also available.'),
        ('How is punching priced?', 'There are two parts: a one-off punching die cost and a cost per stroke in production. Both depend on the part’s geometry, meaning the number and shape of holes and slots, and on the material and thickness. Both are quoted separately after the drawing is reviewed.'),
        ('Do you make the punching die too?', 'Yes. Designing and building the punching die is part of HyperFab’s service, and a trial sample is punched for your approval before production.'),
        ('What shapes can be punched?', 'Round and square holes, straight slots, kidney-shaped slots, perforated patterns and custom forms to your drawing, in sheet and tube.'),
        ('What do I need for a punching quote?', 'A drawing or sample of the part, the material and thickness, and an approximate quantity. You can also give the details by phone.'),
        ('Punching or laser cutting — which is better?', 'For low quantities or designs that keep changing, laser cutting is cheaper because there is no die cost. For repeat quantities, once the die is built, punching makes each part faster and cheaper. HyperFab offers both and recommends the right one for your quantity and geometry.'),
        ('Do you deliver outside Tehran?', 'Yes, parts are shipped across Iran.'),
    ],
    'cta_h': 'Tell us about your punching project',
    'cta_p': 'Send a drawing or a sample part, or call. HyperFab’s industrial projects specialist answers by phone.',
    'cta_btns': CTA_BTNS,
    'schema': [{
        '@type': 'Service', 'name': 'HyperFab Sheet and Tube Punching', 'alternateName': ['Tube punching', 'Sheet punching', 'پانچ ورق و لوله'],
        'serviceType': 'Punching of metal and polyethylene sheet and tube, punching die design and manufacture, production runs',
        'url': SITE + '/en/punching/',
        'description': 'Punching of holes, slots and custom shapes in metal and polyethylene sheet and tube, including punching die design and manufacture, trial samples and production runs with quality control. Pricing is a die cost plus a cost per stroke, depending on geometry and material.',
        'provider': {'@id': MAIN + '/#organization'}, 'areaServed': {'@type': 'Country', 'name': 'Iran'},
    }],
}

INJECTION = {
    'depth': 2,
    'hero': {
        'crumb': 'Mould Making & Injection Moulding',
        'h1': '<em>Mould making and plastic injection moulding</em><br>From part design to mass production',
        'lead': 'Injection mould design and manufacture, and production runs of plastic parts in a range of materials. HyperFab carries the project from design review to delivery of finished parts, with controlled quality.',
        'ticks': [('Services:', 'mould design and manufacture, sampling, production runs', False),
                  ('Materials:', 'polyethylene, polypropylene, ABS, nylon and other thermoplastics', False),
                  ('Pricing:', 'mould cost + cost per shot', False)],
        'buttons': [('btn-red', 'Call for a project consultation', TEL), ('hfs-btn-ghost', 'Chat on Bale', CONTACT['bale_pro_url'])],
        'img': 'assets/img/arc-injection.jpg', 'img_alt': 'Plastic injection moulding machine',
        'stats': [('layers', '4', 'moulds', 'from build supervision to commissioning'), ('stack', '80,000+', 'parts', 'produced with those moulds'),
                  ('file', 'DFM', 'review', 'of mouldability before tooling'), ('shield', '1', 'owner', 'from design to delivery')],
    },
    'sections': [
        {'kicker': 'WHAT IT IS', 'title': 'Mould making and injection moulding at HyperFab', 'id': 'what',
         'paras': [
             '<b>Injection moulding</b> is the main process for mass-producing plastic parts. Molten polymer is injected under pressure into a steel mould, cools, and the part comes out with repeatable dimensions. At high quantities, no other process matches its cost per part and consistency.',
             'An injection project succeeds or fails on the mould, and HyperFab starts there. First the part design is reviewed for mouldability. Then the mould is designed and built, and sampling and correction continue until the part is approved. Production runs follow, with quality control through to delivery.',
             'HyperFab’s team has taken four polyethylene injection moulds from build supervision to commissioning, and more than 80,000 parts have been produced with them. That experience shows, before the mould is built, where a design is likely to cause trouble in production.',
         ],
         'figure': {'img': 'assets/img/arc-injection-robot.jpg', 'alt': 'Injection moulding machine with a part-removal robot', 'caption': 'Production runs of plastic parts on an injection moulding machine with a part-removal robot.'}},
        {'kicker': 'DESIGN FOR MOULDING', 'title': 'Design review before the mould is built', 'id': 'dfm',
         'sub': 'Changing a design on paper costs almost nothing; changing a steel mould is expensive. These points are reviewed before tooling.',
         'checks': [
             '<b>Sufficient draft angle</b> on walls, so the part releases without scuffing or sticking.',
             '<b>Uniform wall thickness</b>, so the part does not warp or show sink marks.',
             '<b>Proper ribs and bosses</b> instead of thick, material-heavy walls.',
             '<b>Gate location</b>, parting line and ejector pin positions.',
             '<b>Undercuts</b> and the need for slides or cores in the mould.',
             '<b>Realistic tolerances for each material</b>, allowing for polymer shrinkage.',
         ]},
        {'kicker': 'MATERIALS', 'title': 'Injection moulding materials', 'id': 'materials',
         'sub': 'The material is recommended based on load, temperature, working environment and part cost.',
         'adv': [
             ('cube', 'Polyethylene (PE)', 'Chemical- and impact-resistant; for caps, containers, fittings and industrial parts.'),
             ('layers', 'Polypropylene (PP)', 'Light and fatigue-resistant; for living hinges, packaging and consumer parts.'),
             ('sparkle', 'ABS', 'Good-looking surface and solid strength; for device housings and cosmetic parts.'),
             ('wrench', 'Nylon (PA)', 'Tough and wear-resistant; for gears, bushings and mechanical parts.'),
             ('shield', 'Engineering thermoplastics', 'Polycarbonate, acetal (POM) and other materials, depending on the part’s use.'),
             ('chat', 'Choose the material with us', 'Not sure? Describe the part’s use and a suitable material and grade will be recommended.'),
         ]},
        {'kicker': 'PRICING', 'title': 'How mould making and injection moulding are priced', 'id': 'pricing',
         'sub': 'Each project has two main cost components, quoted separately and clearly.',
         'table': [
             ('Cost component', 'What it depends on'),
             ('Mould (one-off)', 'Part size and complexity, number of cavities, undercuts and slides, surface finish and mould steel'),
             ('Per shot (production)', 'Part material and weight, cycle time and run quantity'),
             ('Material', 'Polymer type, grade and colour'),
         ],
         'note': PRICE_NOTE},
        {'kicker': 'HOW IT WORKS', 'title': 'How an injection moulding project runs', 'id': 'steps',
         'steps': [
             ('Send the design', 'Send a 3D file, drawing or sample part. If you only have an idea, part design is available too.'),
             ('Mouldability review', 'The design is checked for draft, wall thickness and parting line, and changes are suggested.'),
             ('Quotation', 'Mould cost and cost per shot are quoted separately and clearly.'),
             ('Mould and sampling', 'The mould is built, sampled and corrected until you give final approval.'),
             ('Production and delivery', 'Parts are produced with quality control and delivered.'),
         ],
         'note': '<b>Before investing in a mould:</b> you can make a prototype with <a href="../#fdm">HyperFab 3D printing</a> and check form, dimensions and assembly on a real part.'},
        {'kicker': 'WHY HYPERFAB', 'title': 'Why trust HyperFab with an injection project', 'id': 'why',
         'why': [
             ('file', 'Engineering before tooling', 'HyperFab’s engineering team comes from Iran’s top universities and has worked at the heart of industry for years. It reviews your design from a production point of view before the mould is built, so the mould is built once, and built right.'),
             ('chart', 'Real production experience', 'Four injection moulds from build supervision to commissioning and more than 80,000 parts produced; we know the road from design to mass production first-hand.'),
             ('shield', 'One owner from design to delivery', 'From the mould to the last part, full responsibility for the project lies with HyperFab. You approve samples before production and quality is checked before delivery.'),
         ]},
    ],
    'faq': [
        ('Does HyperFab make plastic injection moulds?', 'Yes. HyperFab designs and builds injection moulds and runs production of plastic parts in a range of materials. The project is with HyperFab from design review to delivery.'),
        ('How are mould making and injection moulding priced?', 'There are two main parts: a one-off mould cost and a cost per shot in production. The mould cost depends on part size and complexity, number of cavities and undercuts. The cost per shot depends on part material and weight and cycle time. Both are quoted separately after the design is reviewed.'),
        ('Which materials do you mould?', 'Polyethylene, polypropylene, ABS, nylon and other engineering thermoplastics such as polycarbonate and acetal, depending on the part’s use.'),
        ('At what quantity does injection moulding pay off?', 'It depends on the mould cost and the price per part, and it usually pays off at high quantities. For smaller runs, 3D printing or CNC machining may be cheaper. HyperFab offers all three and recommends the right process after reviewing the project.'),
        ('I don’t have a file or drawing. What can I do?', 'Send a sample part, a photo or your idea. Part design and modelling are available, and the mould is built after you approve the design.'),
        ('Will I see a sample before production?', 'Yes. Samples are taken after the mould is built and production starts after your approval. Before tooling, you can also make a prototype with 3D printing.'),
    ],
    'cta_h': 'Tell us about your injection moulding project',
    'cta_p': 'Send a design, drawing or sample part, or call. HyperFab’s industrial projects specialist answers by phone.',
    'cta_btns': CTA_BTNS,
    'schema': [{
        '@type': 'Service', 'name': 'HyperFab Mould Making and Plastic Injection Moulding', 'alternateName': ['Injection molding', 'Mold making', 'قالب‌سازی و تزریق پلاستیک'],
        'serviceType': 'Injection mould design and manufacture and production of plastic parts',
        'url': SITE + '/en/injection-molding/',
        'description': 'Injection mould design and manufacture, sampling and production runs of plastic parts in polyethylene, polypropylene, ABS, nylon and engineering thermoplastics, with mouldability review and quality control. Pricing is a mould cost plus a cost per shot.',
        'provider': {'@id': MAIN + '/#organization'}, 'areaServed': {'@type': 'Country', 'name': 'Iran'},
    }],
}

FEATURE = {
    'cls': '', 'id': 'industrial', 'kicker': 'INDUSTRIAL PRODUCTION',
    'title': 'Industrial production: punching, mould making and injection moulding',
    'sub': 'For high quantities: from die and mould design and manufacture to production runs and delivery, with one responsible engineering team.',
    'paras': [
        'When a part moves from prototype to volume, the process has to change. HyperFab offers two industrial production services: <b>sheet and tube punching</b>, in metal and polyethylene, and <b>mould making and plastic injection moulding</b>. In both, tooling design and manufacture and production runs are part of the service. One responsible engineering team carries the project from design review to delivery.',
        'HyperFab’s engineering team comes from Iran’s top universities, including Sharif University of Technology, and has worked at the heart of industry for years. It has taken four polyethylene injection moulds from build to commissioning, and more than 80,000 parts have been produced with them. Its record also includes quality control of 8,000 punched tubes and kidney slots punched in 125 mm polyethylene pipe. Each project is priced as a tooling cost plus a cost per stroke or shot, quoted after geometry and material are reviewed.',
    ],
    'points': [
        '<b>Sheet and tube punching:</b> holes, slots and custom shapes in metal and polyethylene sheet and tube; punching die design and manufacture, and production runs.',
        '<b>Mould making and injection moulding:</b> mouldability review, mould design and manufacture, sampling and production runs in polyethylene, polypropylene, ABS, nylon and other thermoplastics.',
        '<b>Clear pricing:</b> tooling cost and cost per stroke or shot are quoted separately.',
        f'<b>Phone consultation:</b> HyperFab’s industrial projects specialist answers by phone: <a href="{TEL}">{TEL_EN}</a>.',
    ],
    'more_rel': 'en/punching/', 'more': 'Sheet and tube punching',
    'try_url': 'en/injection-molding/', 'try': 'Mould making and injection moulding',
    'img': 'assets/img/about-hero.webp', 'img_alt': 'Quality control of production parts at HyperFab', 'img_w': 600, 'img_h': 413,
    'caption': 'Quality control before every delivery.',
}

PAGES = {
    'page_punching': {
        'key': 'punching', 'file': 'en/punching/index.html', 'path': '/en/punching/',
        'alt_path': '/punching/', 'alt_rel': 'punching/', 'priority': '0.8',
        'title': 'Sheet & Tube Punching | Polyethylene and Metal Pipe Punching, Punching Dies — HyperFab, Iran',
        'desc': 'Sheet and tube punching in metal and polyethylene by HyperFab, Iran: punching die design and manufacture, trial samples and production runs with quality control. Kidney slots punched in 125 mm polyethylene pipe. Phone consultation.',
        'keywords': 'tube punching Iran, pipe punching, polyethylene pipe punching, PE pipe slotting, sheet metal punching, punching die, kidney slot pipe, drainage pipe perforation, HyperFab',
    },
    'page_injection': {
        'key': 'injection', 'file': 'en/injection-molding/index.html', 'path': '/en/injection-molding/',
        'alt_path': '/injection-molding/', 'alt_rel': 'injection-molding/', 'priority': '0.8',
        'title': 'Mould Making & Plastic Injection Moulding | Injection Moulds and Production Runs — HyperFab, Iran',
        'desc': 'Mould making and plastic injection moulding by HyperFab, Iran: mouldability review, injection mould design and manufacture, sampling and production runs in PE, PP, ABS and nylon. Phone consultation.',
        'keywords': 'injection molding Iran, plastic injection moulding Tehran, mold making Iran, injection mould manufacture, plastic parts production, PE injection molding, HyperFab',
    },
}


def apply(C):
    C['punching'] = PUNCHING
    C['injection'] = INJECTION
    C.update(PAGES)
    C['home']['ind_feature'] = FEATURE
    C['nav'].insert(4, ('industrial', 'Industrial', '#industrial'))
    C['industrial_links'] = [('Sheet and tube punching', 'en/punching/'), ('Mould making and injection moulding', 'en/injection-molding/')]
    C['tools_as_services'] += [
        {'title': 'HyperFab Sheet and Tube Punching', 'paras': [PUNCHING['sections'][0]['paras'][1]], 'url': SITE + '/en/punching/'},
        {'title': 'HyperFab Mould Making and Injection Moulding', 'paras': [INJECTION['sections'][0]['paras'][1]], 'url': SITE + '/en/injection-molding/'},
    ]
    C['knows_about'] += ['sheet punching', 'tube punching', 'polyethylene pipe punching', 'punching dies', 'mould making',
                         'plastic injection moulding', 'injection mould manufacture']
    C['org_desc'] = C['org_desc'].rstrip('.') + '; and, for industrial production, sheet and tube punching and mould making and plastic injection moulding.'
