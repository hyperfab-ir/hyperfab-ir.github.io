"""Industrial production, part two — English: welding, batch CNC turning, aluminium extrusion,
plating and anodizing, powder coating. Mirrors industrial2_fa.py; ordering is by phone."""
from common import SITE, MAIN, CONTACT
from industrial_en import TEL, TEL_EN, CTA_BTNS
from industrial2_fa import IMG

BATCH_NOTE = ('<b>For production runs only:</b> this service is for batch production; one-off parts are accepted only rarely. '
              'A suitable quantity is recommended after reviewing the project.')


def svc(name, alt, stype, path, desc):
    return [{'@type': 'Service', 'name': name, 'alternateName': alt, 'serviceType': stype, 'url': SITE + path,
             'description': desc, 'provider': {'@id': MAIN + '/#organization'}, 'areaServed': {'@type': 'Country', 'name': 'Iran'}}]


def hero_btns():
    return [('btn-red', 'Call for a project consultation', TEL), ('hfs-btn-ghost', 'Chat on Bale', CONTACT['bale_pro_url'])]


WELDING = {
    'depth': 2,
    'hero': {
        'crumb': 'Welding & Welded Structures',
        'h1': '<em>TIG and MIG welding</em><br>Stainless steel, aluminium and welded structures',
        'lead': 'TIG and MIG welding of stainless steel and 6000-series aluminium, fabrication and assembly of welded structures for machines, and large platform structures — with VT, PT and phased-array weld testing on request, from drawing to delivery.',
        'ticks': [('Processes:', 'TIG and MIG (argon shielded)', False), ('Materials:', 'stainless steel, 6000-series aluminium', False),
                  ('Weld testing:', 'VT · PT · PAUT and other tests as required', False)],
        'buttons': hero_btns(),
        'img': IMG['welding'], 'img_alt': 'TIG welding of a HyperFab stainless steel sealing assembly',
        'stats': [('sparkle', 'TIG · MIG', 'argon', 'stainless and aluminium'), ('layers', '6000', 'series', 'aluminium'),
                  ('search', 'VT · PT · PAUT', '', 'weld testing on request'), ('shield', '1', 'owner', 'from drawing to delivery')],
    },
    'sections': [
        {'kicker': 'WHAT WE DO', 'title': 'Welding and welded fabrication at HyperFab', 'id': 'what',
         'paras': [
             'Argon-shielded welding — <b>TIG</b> (GTAW) and <b>MIG</b> (GMAW) — is the main way to join stainless steel and aluminium in machine and equipment building. TIG gives clean, precise welds on thin sheet and sensitive parts; MIG is faster for long and structural welds. HyperFab does both on <b>stainless steel</b> and <b>6000-series aluminium</b>.',
             'HyperFab’s work is not just laying welds; it is building and assembling the project from drawing to delivery. That covers cutting and preparing parts, fixturing, welding with distortion control, weld finishing and testing. HyperFab has built many units for the <b>medical</b> and <b>marine</b> industries, where weld cleanliness and corrosion resistance are critical.',
             'The experience goes beyond small parts. HyperFab has built large platform structures, including a framed chassis mounted on wheels that runs on rails — a structure where flatness, alignment and dimensional accuracy over long lengths decide everything.',
         ],
         'gallery': [('assets/img/works/flange-steel-2.jpg', 'Stainless sealing assembly: drawing, parts and assembly'),
                     ('assets/img/works/flange-steel-3.jpg', 'AISI 304 parts of the same assembly before welding'),
                     ('assets/img/real-pt-test.jpg', 'PT test of the welds on the same assembly')]},
        {'kicker': 'SERVICES', 'title': 'HyperFab welding services', 'id': 'scope',
         'adv': [
             ('sparkle', 'TIG welding of stainless steel', 'Clean, precise welds on stainless steel for medical, food and marine equipment, with heat control to preserve corrosion resistance.'),
             ('layers', '6000-series aluminium welding', 'TIG and MIG welding of 6000-series alloys such as 6061 and 6063, for chassis, frames and light structures.'),
             ('cube', 'Welded machine structures', 'Chassis, frames, housings and enclosures for many kinds of machines in stainless steel or aluminium, from cut parts to assembled structure.'),
             ('ruler', 'Large platform structures', 'Large platforms and framed chassis, including a structure mounted on wheels that runs on rails.'),
             ('shield', 'Medical and marine industries', 'Many units built for medical equipment and marine applications, meeting those industries’ cleanliness and corrosion requirements.'),
             ('search', 'Weld testing', 'Visual testing (VT), liquid penetrant (PT), phased-array ultrasonics (PAUT) and other tests on request.'),
         ],
         'figure': {'img': IMG['tig'], 'alt': 'TIG welding on a stainless steel vessel', 'caption': 'TIG welding on stainless steel.'}},
        {'kicker': 'YOUR DESIGN', 'title': 'Built to your drawings', 'id': 'design',
         'paras': [
             'For welded structures, the structural design is the client’s, and HyperFab fabricates to your approved drawings. Before work starts, the drawings are reviewed for manufacturability: welding sequence, joint access, distortion control and tolerances that can realistically be held. Anything worth flagging is discussed with you before fabrication.',
             'For large and platform structures, complete approved drawings are essential before fabrication starts. HyperFab takes responsibility for fabrication, follow-up and quality control through to delivery.',
         ]},
        {'kicker': 'WELD TESTING', 'title': 'Weld tests', 'id': 'testing',
         'sub': 'Tests are carried out on request, to suit the project’s requirements.',
         'table': [
             ('Test', 'What it checks'),
             ('VT — visual testing', 'Weld shape and size, surface cracks, undercut, spatter and visible defects'),
             ('PT — liquid penetrant', 'Surface-breaking cracks and discontinuities; suited to non-magnetic stainless steel and aluminium'),
             ('PAUT — phased-array ultrasonics', 'Internal weld defects such as lack of fusion, internal cracks and porosity, with a cross-section image of the weld'),
             ('Other tests', 'As the project and client require'),
         ],
         'figure': {'img': IMG['ndt'], 'alt': 'Ultrasonic weld testing', 'caption': 'Ultrasonic testing finds internal weld defects.'}},
        {'kicker': 'HOW IT WORKS', 'title': 'How a welding project runs', 'id': 'steps',
         'steps': [
             ('Send drawings', 'Send the structure or part drawings, material, quantity and required tests, or describe them by phone.'),
             ('Manufacturability review', 'Welding sequence, joint access and distortion control are reviewed.'),
             ('Quotation', 'Priced by material, weld length and type, structure size and requested tests.'),
             ('Fabrication and welding', 'Parts are prepared, fixtured, welded and finished as needed.'),
             ('Testing and delivery', 'Requested tests are carried out and the structure is delivered.'),
         ]},
        {'kicker': 'WHY HYPERFAB', 'title': 'Why trust HyperFab with welding', 'id': 'why',
         'why': [
             ('file', 'Engineering before welding', 'Welding sequence and fixturing are planned before work starts so the structure stays flat and true to the drawing.'),
             ('shield', 'Experience in demanding industries', 'Many units for medical and marine use, plus large platform structures on wheels and rails.'),
             ('search', 'Quality you can verify', 'VT, PT and PAUT on request: weld quality is proven by testing, not by words.'),
         ]},
    ],
    'faq': [
        ('Does HyperFab do TIG welding of stainless steel?', 'Yes. HyperFab does TIG and MIG welding of stainless steel and has built many units for the medical and marine industries. Stainless welded structures are fabricated and assembled from drawing to delivery.'),
        ('Do you weld 6061 and 6063 aluminium?', 'Yes. TIG and MIG welding of 6000-series aluminium, including 6061 and 6063, for chassis, frames and light structures.'),
        ('TIG or MIG — which is better?', 'TIG gives cleaner, more precise welds and suits thin sheet, cosmetic parts and medical and food equipment. MIG is faster and more economical for long and structural welds. The right process is recommended by material, thickness and use.'),
        ('Do you design the structure too?', 'No. Structural design is the client’s and HyperFab fabricates to the approved drawings. The drawings are reviewed for manufacturability before fabrication and any issues are discussed with you.'),
        ('Which weld tests do you offer?', 'Visual testing (VT), liquid penetrant (PT), phased-array ultrasonics (PAUT) and other tests, on request and to suit the project’s requirements.'),
        ('Do you build large structures?', 'Yes. HyperFab has built large platform structures, including a framed chassis mounted on wheels that runs on rails.'),
    ],
    'cta_h': 'Tell us about your welding project',
    'cta_p': 'Send the structure drawings or call. HyperFab’s industrial projects specialist answers by phone.',
    'cta_btns': CTA_BTNS,
    'schema': svc('HyperFab Welding and Welded Fabrication', ['TIG welding', 'MIG welding', 'جوشکاری آرگون'],
                  'TIG and MIG welding of stainless steel and aluminium and welded structure fabrication', '/en/welding/',
                  'TIG and MIG welding of stainless steel and 6000-series aluminium, fabrication and assembly of welded machine structures and large platform structures to the client’s drawings, with VT, PT and PAUT weld testing; experience in the medical and marine industries.'),
}

TURNING = {
    'depth': 2,
    'hero': {
        'crumb': 'Batch CNC Turning',
        'h1': '<em>CNC turning</em> of industrial parts<br>Production runs with proven precision',
        'lead': 'Batch production of turned parts in brass, MO40 alloy steel, CK45 steel and other metals, to drawing and with precise fit tolerances. The critical points of every part are engineered and checked before production, from the first sample to the last part of the run.',
        'ticks': [('For:', 'production runs', False), ('Materials:', 'brass, MO40 (42CrMo4), CK45 (C45) and other metals', False),
                  ('Precision:', 'fit tolerances, mating parts and gauges', False)],
        'buttons': hero_btns(),
        'img': IMG['turning'], 'img_alt': 'CNC lathe and boxes of batch-produced PTFE parts at HyperFab',
        'stats': [('wrench', 'MO40 · CK45', '', 'alloy and carbon steel'), ('target', 'CuZn', 'brass', 'mating parts'),
                  ('layers', 'PTFE · 304', '', 'PTFE and stainless'), ('file', '1st', 'article', 'approved before the run')],
    },
    'sections': [
        {'kicker': 'WHAT WE DO', 'title': 'Batch CNC turning at HyperFab', 'id': 'what',
         'paras': [
             'CNC turning is the main way to make rotational parts: shafts, bushings, pins, nuts, nozzles, fittings and parts that must fit precisely into each other. In batch production, the real challenge is not making one good part. It is making hundreds or thousands of parts that are all exactly that good part.',
             'HyperFab has produced batch turned parts for a long time. They range from <b>brass parts with fit tolerances</b> that must mate with each other to <b>gauge parts</b> in <b>MO40</b> alloy steel and <b>CK45</b> steel. They were made to high precision and approved by the customers.',
             'Behind that precision is engineering before turning. Before production starts, each part’s critical points are engineered and briefed to the machinist: fit surfaces, critical diameters, concentricity and surface finish at specific points. The machinist then knows exactly where the part needs which accuracy. HyperFab has the right turning capacity for every precision level and budget, and assigns each project to a machinist who can meet that part’s requirements — no more expensive than needed, never below requirements.',
         ],
         'note': BATCH_NOTE,
         'gallery': [('assets/img/works/ptfe-part-1.jpg', 'Batch PTFE parts packed for delivery'),
                     ('assets/img/works/alu-cone-1.jpg', 'CNC-turned CK45 steel hub'),
                     ('assets/img/works/spline-shaft-1.jpg', 'Splined steel shaft'),
                     ('assets/img/works/steel-bush-1.jpg', 'AISI 304 bushing with precise steps and grooves'),
                     ('assets/img/works/flange-steel-4.jpg', 'Turning an AISI 304 stainless part'),
                     ('assets/img/works/misc-parts-1.jpg', 'Precision brass, stainless and polymer parts')]},
        {'kicker': 'MATERIALS & PARTS', 'title': 'Materials and parts we turn', 'id': 'scope',
         'adv': [
             ('coin', 'Brass parts', 'Brass bushings, nozzles, fittings, pins and mating parts with fit tolerances and a clean finish.'),
             ('wrench', 'MO40 steel (42CrMo4)', 'Chromium-molybdenum alloy steel for loaded parts and gauges, with high strength and toughness.'),
             ('layers', 'CK45 steel (C45)', 'Medium-carbon steel for shafts, pins, machine parts and gauges.'),
             ('target', 'Gauge parts', 'Dimensional inspection gauges that are themselves the precision reference of a production line.'),
             ('ruler', 'Mating parts', 'Sliding and press fits between parts, with control of critical diameters and concentricity.'),
             ('cube', 'Other metals', 'Stainless steel, aluminium and other steels, depending on the project.'),
         ]},
        {'kicker': 'PRECISION', 'title': 'How precision is held across a run', 'id': 'precision',
         'checks': [
             '<b>Drawing engineering before production:</b> identifying fit surfaces, critical dimensions and measurement datums.',
             '<b>Technical briefing for the machinist:</b> the accuracy of each critical point, the operation sequence and the measurement method.',
             '<b>The right machinist for the project:</b> one who can meet the part’s requirements, at a price that matches the project’s importance.',
             '<b>First-article approval</b> before the production run starts.',
             '<b>Dimensional inspection</b> during production and before delivery.',
             '<b>Suitable packing</b> so precision fit surfaces are not damaged.',
         ]},
        {'kicker': 'MORE THAN TURNING', 'title': 'After turning', 'id': 'after',
         'paras': [
             'A turned part usually needs a finish or assembly too. At HyperFab you can include <a href="../plating-anodizing/">silver and gold plating, anodizing and chromate</a>, <a href="../powder-coating/">powder coating</a> and <a href="../welding/">welding</a> in the same project, and receive the finished, ready-to-use part.',
             'For one-off parts and prototypes, see <a href="https://hyperfab.ir/services/cnc/">CNC machining on the HyperFab website</a>.',
         ]},
        {'kicker': 'HOW IT WORKS', 'title': 'How a batch turning order runs', 'id': 'steps',
         'steps': [
             ('Send the drawing', 'Send a dimensioned drawing with tolerances, the material and the quantity, or describe them by phone.'),
             ('Engineering review', 'Fit surfaces and critical dimensions are identified and production notes are set.'),
             ('Quotation', 'Priced by material, complexity, tolerances and quantity.'),
             ('First article', 'The first part is made and inspected; the run starts after your approval.'),
             ('Production and delivery', 'The run is produced with dimensional inspection and delivered.'),
         ]},
    ],
    'faq': [
        ('Does HyperFab do batch CNC turning?', 'Yes. HyperFab produces batch turned parts to drawing. Examples include brass parts with fit tolerances and gauge parts in MO40 and CK45 steel, made to high precision and approved by the customers.'),
        ('Do you turn MO40 and CK45 steel?', 'Yes. MO40 (equivalent to 42CrMo4) and CK45 (equivalent to C45) are among the materials HyperFab has used for gauge parts and batch industrial parts.'),
        ('Do you make precision mating brass parts?', 'Yes. Brass parts that must fit into each other with sliding or press fits are one of HyperFab’s core experiences. Critical diameters and concentricity are engineered before production and checked during it.'),
        ('Do you turn single parts?', 'This service is for production runs. For single parts and prototypes, see CNC machining on hyperfab.ir.'),
        ('How is batch turning priced?', 'By material, part complexity, tolerances and quantity. Each project goes to a machinist who can meet its requirements, so the price matches the part’s importance and precision.'),
        ('Can you plate or coat the parts too?', 'Yes. Silver and gold plating, anodizing and chromate, and powder coating are also available at HyperFab, and the finished part is delivered.'),
    ],
    'cta_h': 'Send the drawing of your batch part',
    'cta_p': 'Send the drawing with tolerances, material and quantity, or call. HyperFab’s industrial projects specialist answers by phone.',
    'cta_btns': CTA_BTNS,
    'schema': svc('HyperFab Batch CNC Turning', ['CNC turning', 'تراشکاری CNC'], 'Batch production of CNC turned parts', '/en/cnc-turning/',
                  'Batch production of CNC turned parts in brass, MO40 (42CrMo4), CK45 (C45) and other metals, with fit tolerances, mating parts and gauges; critical points engineered before production, first-article approval and dimensional inspection.'),
}

EXTRUSION = {
    'depth': 2,
    'hero': {
        'crumb': 'Aluminium Extrusion',
        'h1': '<em>Aluminium profile extrusion</em><br>Your cross-section, with a dedicated die',
        'lead': 'Aluminium profiles in the cross-section you need. HyperFab’s engineering team advises on the section geometry, then a dedicated extrusion die is built and the profile is produced. You need the required tonnage and pay for the die; HyperFab’s engineering team handles the rest.',
        'ticks': [('Speciality:', 'aluminium extrusion only', False), ('Your part:', 'required tonnage + die cost', False),
                  ('Our part:', 'section consultation, die, production, QC and delivery', False)],
        'buttons': hero_btns(),
        'img': IMG['extrusion'], 'img_alt': 'Extruded aluminium profiles',
        'stats': [('layers', '6063 · 6061', 'alloys', 'most used for extrusion'), ('ruler', 'Custom', 'section', 'your geometry'),
                  ('wrench', 'Die', 'tooling', 'dedicated to your profile'), ('shield', '1', 'owner', 'from consultation to delivery')],
    },
    'sections': [
        {'kicker': 'WHAT IT IS', 'title': 'Aluminium extrusion at HyperFab', 'id': 'what',
         'paras': [
             '<b>Aluminium extrusion</b> pushes a hot aluminium billet under pressure through a steel die to make a long profile with a constant cross-section. Almost any section you can draw can be made with a dedicated die: solid, hollow, slotted, finned or with screw ports. That makes extrusion the most economical way to make long, uniform aluminium parts.',
             'HyperFab <b>specialises in aluminium extrusion</b>. The model is simple: you have the required tonnage and pay for the die. Section design consultation, die making, profile production, quality control and delivery are handled by HyperFab’s engineering team. The result is a profile with exactly the section you need, not the closest one available on the market.',
             'Consultation before the die matters. Extrusion dies are expensive, and a poorly designed section can lead to warped profiles, uneven surfaces or a broken die. Before the die is made, HyperFab’s engineering team reviews your section for wall thickness, symmetry, corner radii and tongue ratios and suggests changes, so the die is built once, and built right.',
         ],
         'note': '<b>Aluminium only:</b> in extrusion, HyperFab works exclusively with aluminium. Orders are by tonnage, and the right tonnage for each section is advised after consultation.'},
        {'kicker': 'WHO DOES WHAT', 'title': 'Your part and our part', 'id': 'roles',
         'table': [
             ('Step', 'Who'),
             ('Defining the use and initial section', 'You'),
             ('Consultation and final section geometry', 'HyperFab’s engineering team, with your approval'),
             ('Paying for the die', 'You'),
             ('Extrusion die design and manufacture', 'HyperFab'),
             ('Profile production at the ordered tonnage', 'HyperFab'),
             ('Quality control and delivery', 'HyperFab'),
         ]},
        {'kicker': 'PROFILES', 'title': 'Profiles we extrude', 'id': 'profiles',
         'adv': [
             ('stack', 'Industrial and T-slot profiles', 'Structural and slotted profiles for machine frames, workbenches and production lines.'),
             ('bolt', 'Heat sinks and finned profiles', 'Finned profiles for heat dissipation in power electronics, drives and LEDs.'),
             ('box', 'Housings and enclosures', 'Device housings and electronic enclosures with a section dedicated to your product.'),
             ('sparkle', 'Architectural and decorative profiles', 'Frames, edges, handles and decorative profiles.'),
             ('layers', 'Hollow and multi-cavity profiles', 'Hollow and multi-cavity sections that are both light and strong.'),
             ('ruler', 'Rails and guides', 'Rails, linear guides and light parts for equipment and transport.'),
         ]},
        {'kicker': 'DESIGN TIPS', 'title': 'Designing an extrusion section', 'id': 'design',
         'sub': 'Following these points extends die life and lowers the cost per kilo; all of them are reviewed in consultation.',
         'checks': [
             '<b>Uniform wall thickness:</b> large thickness differences unbalance metal flow and warp the profile.',
             '<b>Rounded corners:</b> give sharp corners a small radius for longer die life and a better surface.',
             '<b>Balanced section:</b> symmetric, balanced sections extrude more stably and accurately.',
             '<b>Die tongues:</b> deep, narrow slots weaken the die tongue; the depth-to-width ratio must be controlled.',
             '<b>Section size:</b> the section must fit the production range; the right size is set in consultation.',
             '<b>Tolerances:</b> keep tight tolerances for functional dimensions only.',
         ]},
        {'kicker': 'AFTER EXTRUSION', 'title': 'After extrusion', 'id': 'after',
         'paras': [
             'An extruded profile is usually not yet the finished product. At HyperFab you can add <a href="../plating-anodizing/">anodizing</a>, <a href="../powder-coating/">powder coating</a>, <a href="../cnc-turning/">machining</a>, <a href="../punching/">punching</a> and <a href="../welding/">aluminium welding</a>, and receive a part that is ready to assemble.',
         ],
         'figure': {'img': 'assets/img/arc-extrusion-coating.jpg', 'alt': 'Aluminium profiles on a powder coating line', 'caption': 'Extruded aluminium profiles on a coating line.'}},
        {'kicker': 'HOW IT WORKS', 'title': 'How an extrusion order runs', 'id': 'steps',
         'steps': [
             ('Send the section or idea', 'Send the section drawing, a DXF or even a sketch and the profile’s use, or describe it by phone.'),
             ('Section consultation', 'The engineering team reviews and optimises the section for extrusion and advises the right tonnage.'),
             ('Quotation', 'Die cost and profile price, by alloy, weight and tonnage, are quoted separately.'),
             ('Die and sample', 'The die is built and a sample profile is produced for your approval.'),
             ('Production and delivery', 'The profile is produced at the ordered tonnage, inspected and delivered.'),
         ]},
    ],
    'faq': [
        ('Does HyperFab extrude aluminium profiles?', 'Yes. HyperFab specialises in aluminium extrusion: aluminium profiles in the customer’s own cross-section, with a dedicated die. Section consultation, die making, production and delivery are handled by HyperFab’s engineering team.'),
        ('What do I need to order a custom aluminium profile?', 'The required tonnage and payment for the die. The section is finalised after consultation with HyperFab’s engineering team, and everything else, from die making to profile delivery, is handled by HyperFab.'),
        ('What is the minimum order for aluminium extrusion?', 'Orders are by tonnage. The right tonnage depends on the section’s size and weight and is advised after consultation.'),
        ('Do you design the profile section?', 'HyperFab’s engineering team advises on the section geometry and optimises it for extrusion: wall thickness, symmetry, corner radii and tongue ratios. The final section is made with your approval.'),
        ('Do you extrude materials other than aluminium?', 'No. In extrusion, HyperFab works with aluminium only.'),
        ('Can you anodize or coat the profiles?', 'Yes. Anodizing, powder coating, machining, punching and welding of profiles are also available at HyperFab.'),
    ],
    'cta_h': 'Tell us about your profile section',
    'cta_p': 'Send the section drawing or sketch, or call. HyperFab’s engineering team advises on the section, tonnage and die.',
    'cta_btns': CTA_BTNS,
    'schema': svc('HyperFab Aluminium Extrusion', ['Aluminum extrusion', 'Custom aluminium profiles', 'اکسترود آلومینیوم'],
                  'Specialised aluminium profile extrusion with custom sections and dedicated dies', '/en/aluminium-extrusion/',
                  'Specialised extrusion of aluminium profiles in the customer’s cross-section: section design consultation, dedicated extrusion die, production at the ordered tonnage, quality control and delivery. The customer has the required tonnage and pays for the die.'),
}

PLATING = {
    'depth': 2,
    'hero': {
        'crumb': 'Plating & Anodizing',
        'h1': '<em>Silver and gold plating</em>, anodizing and chromate<br>Finishing for batch metal parts',
        'lead': 'Silver and gold plating on brass and other metals, and anodizing and chromate conversion (Alodine) on aluminium — for decorative, electrical and industrial uses, with consistent quality across the run.',
        'ticks': [('Plating:', 'silver and gold on brass and other metals', False), ('Aluminium:', 'anodizing and chromate (Alodine)', False),
                  ('For:', 'production runs', False)],
        'buttons': hero_btns(),
        'img': IMG['plating'], 'img_alt': 'Gold-plated parts',
        'stats': [('sparkle', 'Ag', 'silver', 'on brass and other metals'), ('coin', 'Au', 'gold', 'on brass and other metals'),
                  ('layers', 'Al', 'anodizing', 'on aluminium'), ('shield', 'Alodine', 'chromate', 'conversion coating')],
    },
    'sections': [
        {'kicker': 'WHAT WE DO', 'title': 'Plating and anodizing at HyperFab', 'id': 'what',
         'paras': [
             'Surface finish is the last and most visible step in making a part. It sets the part’s appearance and its resistance to corrosion and wear, and its electrical behaviour. HyperFab does <b>silver and gold plating</b> on brass and other metals, and <b>anodizing</b> and <b>chromate conversion (Alodine)</b> on aluminium.',
             'The service covers both <b>decorative</b> and <b>technical</b> parts. For decorative parts, a bright, lasting appearance matters: décor items, hardware, statuettes and corporate gifts. For technical parts, conductivity, corrosion resistance and a good paint base matter: connectors, contacts and electronic and industrial parts. It is for production runs, and it pairs well with HyperFab’s <a href="../cnc-turning/">batch CNC turning</a>: a turned brass part is delivered plated and ready.',
         ],
         'note': BATCH_NOTE},
        {'kicker': 'COATINGS', 'title': 'Finishes we offer', 'id': 'coatings',
         'adv': [
             ('sparkle', 'Silver plating', 'The highest electrical conductivity of any metal; for contacts, connectors, busbars and electrical parts, and for decorative items with a bright silver look.'),
             ('coin', 'Gold plating', 'Excellent resistance to oxidation and stable contact resistance; for connectors and electronics, and for jewellery, hardware and luxury items.'),
             ('layers', 'Aluminium anodizing', 'A hard oxide layer grown on aluminium that raises corrosion and wear resistance; for housings, profiles and industrial and decorative parts.'),
             ('shield', 'Chromate (Alodine)', 'A thin conversion coating on aluminium that prevents corrosion, keeps the surface electrically conductive and makes a good paint base.'),
             ('cube', 'On brass and other metals', 'Plating on brass and other metals, from turned parts to castings and sheet parts.'),
             ('stack', 'Consistent across the run', 'The same preparation and checks for every part in a batch, so colour and appearance match from first part to last.'),
         ],
         'figure': {'img': IMG['anodizing'], 'alt': 'Colour-anodized aluminium parts', 'caption': 'Colour anodizing on aluminium parts.'}},
        {'kicker': 'COMPARE', 'title': 'Which finish suits your part', 'id': 'compare',
         'table': [
             ('Finish', 'Base metal', 'Main property', 'Typical uses'),
             ('Silver plating', 'Brass, copper and other metals', 'Highest conductivity, silver appearance', 'Contacts and connectors, busbars, RF parts, decorative items'),
             ('Gold plating', 'Brass, copper and other metals', 'Oxidation-resistant, stable contact resistance, gold appearance', 'Connectors and electronics, jewellery, luxury hardware'),
             ('Anodizing', 'Aluminium', 'Hard oxide layer, corrosion- and wear-resistant', 'Housings, profiles, industrial and decorative parts'),
             ('Chromate (Alodine)', 'Aluminium', 'Corrosion protection with a conductive surface, paint base', 'Electronic parts, enclosures, parts before painting'),
         ]},
        {'kicker': 'APPLICATIONS', 'title': 'Uses of plating and anodizing', 'id': 'uses',
         'checks': [
             '<b>Electrical and electronic parts:</b> contacts, connectors, terminals and busbars with silver or gold plating.',
             '<b>Decorative items and gifts:</b> statuettes, badges, hardware and décor with gold and silver plating.',
             '<b>Device housings and frames:</b> anodized or chromated aluminium parts.',
             '<b>Turned brass parts:</b> fittings and precision parts with protective or decorative plating.',
             '<b>Aluminium parts before painting:</b> chromate as an adhesion base.',
         ]},
    ],
    'faq': [
        ('Does HyperFab do gold and silver plating?', 'Yes. HyperFab does silver and gold plating on brass and other metals for decorative, electrical and industrial uses. The service is for production runs.'),
        ('Do you anodize aluminium?', 'Yes. Anodizing and chromate conversion (Alodine) are done on aluminium parts.'),
        ('What is chromate or Alodine?', 'Chromate is a thin conversion coating on aluminium that prevents corrosion and, unlike anodizing, keeps the surface electrically conductive. It is also a good paint base. Alodine is the well-known trade name of this kind of coating.'),
        ('Silver or gold plating — which is better?', 'Silver has the highest conductivity and costs less but tarnishes over time in air. Gold conducts less but does not oxidise, so its contact resistance stays stable. The choice depends on use, environment and budget.'),
        ('Do you plate single parts?', 'The service is for production runs; one-off work is accepted only rarely.'),
        ('Can you make the part too?', 'Yes. You can also have the part made by HyperFab through batch CNC turning, punching or injection moulding, and receive it finished.'),
    ],
    'cta_h': 'Send your parts for plating or anodizing',
    'cta_p': 'Tell us the part material, finish and quantity, or send a sample. HyperFab’s industrial projects specialist answers by phone.',
    'cta_btns': CTA_BTNS,
    'schema': svc('HyperFab Plating and Anodizing', ['Gold plating', 'Silver plating', 'Anodizing', 'Chromate conversion', 'Alodine'],
                  'Silver and gold plating, anodizing and chromate (Alodine)', '/en/plating-anodizing/',
                  'Silver and gold plating on brass and other metals, and anodizing and chromate conversion (Alodine) on aluminium, for decorative, electrical and industrial uses; for production runs.'),
}

COATING = {
    'depth': 2,
    'hero': {
        'crumb': 'Powder Coating',
        'h1': '<em>Powder coating</em> (electrostatic, oven-cured)<br>Durable finishes for batch parts',
        'lead': 'Electrostatic powder coating in pearl, hammer and textured finishes, gloss and matt, on batch metal parts — a hard, even, durable finish for machine housings, structures, industrial parts and consumer products.',
        'ticks': [('Finishes:', 'powder, pearl, hammer, texture, gloss and matt', False), ('On:', 'steel, iron, aluminium and other metals', False),
                  ('For:', 'production runs', False)],
        'buttons': hero_btns(),
        'img': IMG['coating'], 'img_alt': 'Electrostatic powder coating of a metal part',
        'stats': [('layers', 'Powder', 'coating', 'electrostatic'), ('sparkle', 'Pearl', 'finish', 'metallic and pearlescent'),
                  ('wrench', 'Hammer', 'finish', 'hides imperfections'), ('target', 'RAL', 'colours', 'standard codes')],
    },
    'sections': [
        {'kicker': 'WHAT IT IS', 'title': 'What powder coating is', 'id': 'what',
         'paras': [
             '<b>Powder coating</b> applies a dry powder to a metal part. The electrically charged powder clings to the part, which is then cured in an oven so the powder melts into a continuous, hard layer. The result is thicker, more even and more resistant to impact, scratches and corrosion than liquid paint.',
             'HyperFab powder-coats batch metal parts with high quality at a fair price: machine housings and chassis, structures, industrial parts and consumer products. If the part is also made at HyperFab — by <a href="../punching/">punching</a>, <a href="../welding/">welding</a> or <a href="../cnc-turning/">turning</a> — you receive the coated, finished part in one place.',
         ],
         'note': BATCH_NOTE},
        {'kicker': 'FINISHES', 'title': 'Powder coating finishes', 'id': 'types',
         'adv': [
             ('layers', 'Electrostatic powder', 'The most common powder coating: an even, solvent-free finish with strong adhesion and durability.'),
             ('sparkle', 'Pearl (metallic and pearlescent)', 'A metallic or pearlescent sheen for cosmetic parts, décor and premium products.'),
             ('wrench', 'Hammer finish', 'A texture like hammered metal that hides imperfections; common on machine housings, cabinets and tools.'),
             ('stack', 'Texture and wrinkle', 'A rough, matt surface that hides fingerprints and scratches; for high-touch parts.'),
             ('target', 'Gloss, satin and matt', 'The gloss level to suit the use and look of the product.'),
             ('chat', 'Wide colour range', 'A wide range of colours, including standard RAL codes.'),
         ]},
        {'kicker': 'PROCESS', 'title': 'Powder coating steps', 'id': 'process',
         'steps': [
             ('Surface preparation', 'Degreasing and cleaning, plus other preparation where needed for better adhesion.'),
             ('Powder application', 'Charged powder is sprayed evenly onto the part.'),
             ('Oven curing', 'The part is cured in an oven so the powder melts into a hard, continuous layer.'),
             ('Inspection and delivery', 'Appearance and evenness are checked and parts are packed and delivered.'),
         ]},
        {'kicker': 'APPLICATIONS', 'title': 'Uses of powder coating', 'id': 'uses',
         'checks': [
             '<b>Machine housings and chassis</b> and industrial equipment.',
             '<b>Electrical cabinets</b>, enclosures and metal boxes.',
             '<b>Metal structures, shelving and racks.</b>',
             '<b>Metal furniture</b> and décor.',
             '<b>Car and motorcycle parts</b>, wheels and body parts.',
             '<b>Home appliances</b> and metal consumer products.',
         ]},
        {'kicker': 'WHY POWDER', 'title': 'Why powder coating instead of ordinary paint', 'id': 'why',
         'why': [
             ('shield', 'More durable', 'A thicker, harder layer that lasts longer against impact, scratches and corrosion.'),
             ('layers', 'Consistent across the run', 'The same thickness and look on every part in a batch, with no runs or blotches.'),
             ('sparkle', 'Many looks', 'From matt and gloss to pearl, hammer and textured, for every taste and use.'),
         ]},
    ],
    'faq': [
        ('What is powder coating?', 'Powder coating is an electrostatically charged powder that clings to a metal part and is cured in an oven into a hard, even layer. It is more durable than liquid paint.'),
        ('Which powder coatings does HyperFab offer?', 'Electrostatic powder, pearl (metallic and pearlescent), hammer, texture and wrinkle finishes, in gloss, satin or matt and a wide range of colours.'),
        ('What is a pearl finish?', 'A powder coating with metallic or pearlescent particles that gives a metallic or pearl-like sheen; popular for cosmetic parts and premium products.'),
        ('Do you powder-coat aluminium?', 'Yes. Powder coating is done on steel, iron, aluminium and other metals. On aluminium, chromate as a base improves paint adhesion.'),
        ('Do you coat single parts?', 'The service is for production runs; one-off work is accepted only rarely.'),
        ('How is powder coating priced?', 'By part size and surface area, finish type and texture, preparation required and quantity. The price is quoted after review.'),
    ],
    'cta_h': 'Send your batch parts for powder coating',
    'cta_p': 'Tell us the part size, finish and quantity, or send a sample. HyperFab’s industrial projects specialist answers by phone.',
    'cta_btns': CTA_BTNS,
    'schema': svc('HyperFab Powder Coating', ['Electrostatic powder coating', 'Oven-cured paint', 'رنگ کوره‌ای'],
                  'Electrostatic powder coating of metal parts', '/en/powder-coating/',
                  'Electrostatic powder coating in pearl, hammer and textured finishes, gloss and matt, on batch metal parts; for machine housings, structures, industrial parts and consumer products.'),
}


def page(key, slug, title, desc, kw):
    return {'key': key, 'file': 'en/' + slug + '/index.html', 'path': '/en/' + slug + '/', 'alt_path': '/' + slug + '/',
            'alt_rel': slug + '/', 'priority': '0.8', 'title': title, 'desc': desc, 'keywords': kw}


PAGES = {
    'page_welding': page('welding', 'welding', 'TIG & MIG Welding of Stainless Steel and Aluminium | Welded Fabrication — HyperFab, Iran',
                         'TIG and MIG welding of stainless steel and 6000-series aluminium, welded machine structures and large platforms built to drawings, with VT, PT and PAUT testing; experience in medical and marine industries. HyperFab, Tehran, Iran.',
                         'TIG welding Iran, stainless steel welding Tehran, aluminium welding, 6061 welding, welded fabrication Iran, stainless frame fabrication, weld testing PT PAUT, HyperFab'),
    'page_turning': page('turning', 'cnc-turning', 'Batch CNC Turning | Brass, MO40 and CK45 Industrial Parts — HyperFab, Iran',
                         'Batch CNC turning of industrial parts by HyperFab, Tehran: brass parts with fit tolerances and gauge parts in MO40 and CK45 steel, with critical points engineered before production, first-article approval and dimensional inspection.',
                         'CNC turning Iran, batch turning Tehran, precision brass parts, 42CrMo4 turning, C45 turning, gauge manufacturing, turned parts supplier Iran, HyperFab'),
    'page_extrusion': page('extrusion', 'aluminium-extrusion', 'Custom Aluminium Extrusion Profiles | Extrusion Dies — HyperFab, Iran',
                           'Specialised aluminium profile extrusion in your own cross-section by HyperFab, Iran: section design consultation, dedicated extrusion die, production at your tonnage and delivery; industrial, heat-sink, enclosure and architectural profiles.',
                           'aluminium extrusion Iran, aluminum extrusion, custom aluminium profiles, extrusion die, T-slot profile, heat sink extrusion, aluminium profile manufacturer Iran, HyperFab'),
    'page_plating': page('plating', 'plating-anodizing', 'Gold & Silver Plating, Anodizing and Chromate (Alodine) — HyperFab, Iran',
                         'Silver and gold plating on brass and other metals, and anodizing and chromate (Alodine) on aluminium, by HyperFab, Tehran — for decorative, electrical and industrial parts in production runs.',
                         'gold plating Iran, silver plating brass, anodizing Tehran, aluminium anodizing, chromate conversion, Alodine, connector plating, HyperFab'),
    'page_coating': page('coating', 'powder-coating', 'Powder Coating | Pearl, Hammer and Textured Finishes — HyperFab, Iran',
                         'Electrostatic powder coating in pearl, hammer and textured finishes, gloss and matt, on batch metal parts by HyperFab, Tehran; durable finishes for machine housings, structures and industrial parts.',
                         'powder coating Iran, powder coating Tehran, electrostatic painting, pearl powder coat, hammer finish, RAL powder coating, HyperFab'),
}

FEATURE_PARAS = [
    'When a part moves from prototype to volume, the process has to change. For industrial and batch production, HyperFab offers a complete chain: <a href="punching/">sheet and tube punching</a>, <a href="injection-molding/">mould making and injection moulding</a>, <a href="cnc-turning/">batch CNC turning</a>, <a href="aluminium-extrusion/">aluminium extrusion</a>, <a href="welding/">welding and welded fabrication</a>, <a href="plating-anodizing/">plating and anodizing</a> and <a href="powder-coating/">powder coating</a>. A part can go from production to final finish in one place.',
    'HyperFab’s engineering team comes from Iran’s top universities, including Sharif University of Technology, and has worked in industry for years. It has taken four polyethylene injection moulds from build to commissioning, and more than 80,000 parts have been produced with them. Its record also includes quality control of 8,000 punched tubes, mating brass parts and MO40 and CK45 gauges, and stainless and aluminium structures for the medical and marine industries.',
]

FEATURE_POINTS = [
    '<b><a href="punching/">Sheet and tube punching</a>:</b> metal and polyethylene; punching die design and manufacture and production runs.',
    '<b><a href="injection-molding/">Mould making and injection moulding</a>:</b> mould making, sampling and production in PE, PP, ABS and nylon.',
    '<b><a href="cnc-turning/">Batch CNC turning</a>:</b> brass parts with fit tolerances and gauge parts in MO40 and CK45.',
    '<b><a href="aluminium-extrusion/">Aluminium extrusion</a>:</b> your section with a dedicated die; you bring tonnage and die cost, we do the rest.',
    '<b><a href="welding/">TIG and MIG welding</a>:</b> stainless steel and 6000-series aluminium, welded structures and platforms, with VT, PT and PAUT.',
    '<b><a href="plating-anodizing/">Plating and anodizing</a>:</b> silver and gold on brass and other metals, anodizing and chromate on aluminium.',
    '<b><a href="powder-coating/">Powder coating</a>:</b> powder, pearl, hammer and textured finishes.',
    f'<b>Phone consultation:</b> HyperFab’s industrial projects specialist: <a href="{TEL}">{TEL_EN}</a>.',
]

HOME_FAQ = [
    ('Does HyperFab weld stainless steel and aluminium?', 'Yes. HyperFab does TIG and MIG welding of stainless steel and 6000-series aluminium and builds welded machine structures and large platform structures to the client’s drawings. VT, PT and PAUT testing is available on request. HyperFab has built many units for the medical and marine industries.'),
    ('Does HyperFab do batch CNC turning?', 'Yes. HyperFab produces batch turned parts to drawing, including brass parts with fit tolerances and gauge parts in MO40 and CK45 steel. Each part’s critical points are engineered and checked before production.'),
    ('Does HyperFab extrude aluminium profiles?', 'Yes, as a specialisation and for aluminium only. Profiles are made in the customer’s own section with a dedicated die. The customer has the required tonnage and pays for the die, and HyperFab’s engineering team handles everything from section consultation to delivery.'),
    ('Does HyperFab do plating, anodizing and powder coating?', 'Yes, for production runs. HyperFab does silver and gold plating on brass and other metals, and anodizing and chromate (Alodine) on aluminium. Powder coating in powder, pearl, hammer and textured finishes is also available.'),
]


def apply(C):
    C.update({'welding': WELDING, 'turning': TURNING, 'plating': PLATING, 'coating': COATING, 'extrusion': EXTRUSION})
    C.update(PAGES)
    C['tool_keys'] = ['estimator', 'tekeyab', 'punching', 'injection', 'turning', 'extrusion', 'welding', 'plating', 'coating']
    f = C['home']['ind_feature']
    f.update({'title': 'Industrial and batch production: from moulds and turning to welding, plating and coating',
              'sub': 'A complete chain for batch parts, from production to final finish, with one responsible engineering team.',
              'paras': FEATURE_PARAS, 'points': FEATURE_POINTS,
              'more_rel': 'en/cnc-turning/', 'more': 'Batch CNC turning', 'try_url': 'en/welding/', 'try': 'Welding and welded fabrication'})
    C['industrial_links'] += [('Batch CNC turning', 'en/cnc-turning/'), ('Aluminium extrusion', 'en/aluminium-extrusion/'),
                              ('Welding and welded fabrication', 'en/welding/'), ('Plating and anodizing', 'en/plating-anodizing/'),
                              ('Powder coating', 'en/powder-coating/')]
    for name, d, path in (('HyperFab Batch CNC Turning', TURNING, '/en/cnc-turning/'), ('HyperFab Aluminium Extrusion', EXTRUSION, '/en/aluminium-extrusion/'),
                          ('HyperFab Welding and Welded Fabrication', WELDING, '/en/welding/'), ('HyperFab Plating and Anodizing', PLATING, '/en/plating-anodizing/'),
                          ('HyperFab Powder Coating', COATING, '/en/powder-coating/')):
        C['tools_as_services'].append({'title': name, 'paras': [d['schema'][0]['description']], 'url': SITE + path})
    C['knows_about'] += ['CNC turning', 'batch production', 'TIG welding', 'MIG welding', 'stainless steel welding', 'aluminium welding',
                         'welded fabrication', 'non-destructive weld testing', 'gold plating', 'silver plating', 'anodizing',
                         'chromate conversion coating', 'powder coating', 'aluminium extrusion', 'custom aluminium profiles']
    C['org_desc'] = C['org_desc'].rstrip('.') + ', batch CNC turning, aluminium extrusion, welding and welded fabrication, plating and anodizing, and powder coating.'
    C['home']['faq'][-1:-1] = HOME_FAQ
    cnc = next(s for s in C['services'] if s['key'] == 'cnc')
    cnc['paras'].append('CNC machining at HyperFab is not only for mould making. HyperFab makes all kinds of parts to customers’ drawings with high quality and precision, from single parts and prototypes to <a href="cnc-turning/">batch production of turned parts</a> in brass and MO40 and CK45 steel.')
    cnc['specs'].append(('Batch production', '<a href="cnc-turning/">Batch CNC turning</a>'))
