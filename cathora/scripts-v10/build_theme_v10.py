# -*- coding: utf-8 -*-
"""CATHORA v10: clearer shopping navigation, blessings, 8 sacred lands with photos, full product page, brand pages."""
import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import build_theme as B
import v9_copy as V
from v10_copy_a import NAV, BLESS, BLESS_ORDER, HOME, PROMISES, LAND_ORDER, LAND_META, NEW_LANDS
from v10_copy_b import PDP, FAQ, BRAND, FOUNDER, CARE
from v10_copy_c import BRAND_C, FOUNDER_C
BRAND.update(BRAND_C); FOUNDER.update(FOUNDER_C)
from v10_copy_d import BRAND_D, FOUNDER_D
BRAND.update(BRAND_D); FOUNDER.update(FOUNDER_D)
from v10_copy_e import BRAND_E, FOUNDER_E, BLESS_TC, LAND_TC
BRAND.update(BRAND_E); FOUNDER.update(FOUNDER_E)
from v10_copy_g import BRAND_G
BRAND.update(BRAND_G)
for _k in BLESS: BLESS[_k]['char'] = BLESS_TC[_k]

t, url, w = B.t, B.url, B.w
ELS, EL_HANDLE, EL_COLOR, EL_CHAR = B.ELS, B.EL_HANDLE, B.EL_COLOR, B.EL_CHAR
LANGS = {'zh': 0, 'en': 1, 'ja': 2, 'ko': 3}
ROMAN = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']
NUM = {'en': ROMAN, 'zh': list('一二三四五六七八'), 'ja': list('一二三四五六七八'), 'ko': [str(i) for i in range(1, 9)]}
LK = lambda k: k.replace('-', '')  # locale key for a land
import copy_data as CD
ART = dict(CD.LINE_ART)
ART.update({
    'longmen': {'bg': '#E9E6DE', 'fg': '#4A4238', 'p1': 'M34 150 L34 66 C34 58 40 54 48 54 L232 54 C240 54 246 58 246 66 L246 150 M108 150 L108 106 C108 74 172 74 172 106 L172 150 M126 150 C126 132 154 132 154 150', 'p2': 'M18 166 C60 158 96 172 140 164 C184 156 222 170 262 162', 'cx': 140, 'cy': 112},
    'white-horse': {'bg': '#EEE7DC', 'fg': '#6E4A36', 'p1': 'M124 150 L124 124 L156 124 L156 150 M114 124 L166 124 M118 108 L162 108 M122 94 L158 94 M126 82 L154 82 M130 72 L150 72 M140 72 L140 56', 'p2': 'M24 150 L256 150 M40 150 C60 140 80 140 96 150', 'cx': 214, 'cy': 62},
    'wudang': {'bg': '#E7E7E2', 'fg': '#3A3F45', 'p1': 'M26 150 L86 82 L114 112 L156 40 L198 104 L254 150 M148 44 L164 44 M150 40 L162 40', 'p2': 'M36 126 C62 118 84 132 112 124 M168 134 C194 126 214 138 242 130', 'cx': 156, 'cy': 30},
})
PHOTO_LANDS = []  # add a land handle here once its photo (cathora-photo-<handle>.jpg) is uploaded to Files
ART_SVG = ('<svg class="v10-art" viewBox="0 0 280 200" aria-hidden="true" focusable="false"><path d="{{ la_p1 }}" fill="none" stroke="{{ la_fg }}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path>'
           '<path d="{{ la_p2 }}" fill="none" stroke="{{ la_fg }}" stroke-width="1" stroke-linecap="round" opacity="0.6"></path><circle cx="{{ la_cx }}" cy="{{ la_cy }}" r="4" fill="{{ la_fg }}"></circle></svg>')


# ------------------------------------------------------------------ locales
def pick(d, i):
    if isinstance(d, tuple):
        return d[i]
    if isinstance(d, dict):
        return {k: pick(v, i) for k, v in d.items()}
    if isinstance(d, list):
        return [pick(v, i) for v in d]
    return d


def locales():
    B.locales()  # writes v9 + cathora for 4 languages
    files = {'en': 'en.default.json', 'zh': 'zh-CN.json', 'ja': 'ja.json', 'ko': 'ko.json'}
    for lang, fn in files.items():
        i = LANGS[lang]
        p = os.path.join(B.OUT, 'locales', fn)
        d = json.load(open(p))
        lands = {}
        for n, k in enumerate(LAND_ORDER):
            src = d['v9']['lands'].get(k) or pick(NEW_LANDS[k], i)
            src = dict(src); src['num'] = NUM[lang][n]
            src.setdefault('s3', '')
            lands[LK(k)] = src
        d['v9']['lands'] = lands
        x = {'nav': pick(NAV, i), 'home': pick(HOME, i), 'pdp': pick(PDP, i), 'brand': pick(BRAND, i),
             'founder': pick(FOUNDER, i), 'care': pick(CARE, i)}
        x['bless'] = {k: dict(pick({kk: vv for kk, vv in BLESS[k].items() if kk != 'char'}, i), char=BLESS[k]['char']) for k in BLESS_ORDER}
        x['prom'] = {('p%d' % (n + 1)): {'t': pick(a, i), 'l': pick(b, i)} for n, (a, b) in enumerate(PROMISES)}
        x['faq'] = {('q%d' % (n + 1)): {'q': pick(a, i), 'a': pick(b, i)} for n, (a, b) in enumerate(FAQ)}
        d['v9']['x'] = x
        w('locales/' + fn, json.dumps(d, ensure_ascii=False, indent=2))


def X(key, **kw):
    return t('x.' + key, **kw)


# ------------------------------------------------------------------ shared liquid
def land_case(var):
    """Assign land variables (lk, la_zh, la_roman, la_file, la_el, la_cr*) from a land handle variable."""
    out = ['{%- case ' + var + ' -%}']
    for k in LAND_ORDER:
        zh, roman, handle, f, el, cr = LAND_META[k]
        a = ART[k]
        out.append("{%%- when '%s' -%%}{%%- assign lk = '%s' -%%}{%%- assign la_zh = '%s' -%%}{%%- assign la_tc = '%s' -%%}{%%- assign la_roman = '%s' -%%}{%%- assign la_file = 'cathora-photo-%s.jpg' -%%}{%%- assign has_photo = %s -%%}{%%- assign la_el = '%s' -%%}{%%- assign la_bg = '%s' -%%}{%%- assign la_fg = '%s' -%%}{%%- assign la_p1 = '%s' -%%}{%%- assign la_p2 = '%s' -%%}{%%- assign la_cx = %d -%%}{%%- assign la_cy = %d -%%}"
                   % (handle, LK(k), zh, LAND_TC[k], roman, handle, 'true' if handle in PHOTO_LANDS else 'false', el, a['bg'], a['fg'], a['p1'], a['p2'], a['cx'], a['cy']))
    out.append('{%- endcase -%}')
    return ''.join(out)


LAND_T = lambda f: "{{ 'v9.lands.' | append: lk | append: '.%s' | t }}" % f


def snippets():
    B.snippets()  # elements page, card, newsletter, localization (v9)
    import v10_reading
    ep = os.path.join(B.OUT, 'snippets/v9-elements.liquid')
    es = open(ep).read().rstrip()
    assert es.endswith('</div>')
    open(ep, 'w').write(es[:-6] + v10_reading.liquid_json() + '\n</div>')
    # photo land card (used in carousel and lists)
    w('snippets/v10-land-card.liquid', land_case('land') + '''{%- capture lnum -%}''' + LAND_T('num') + '''{%- endcapture -%}{%- assign limg = images[la_file] -%}
<a class="v10-land" href="{{ routes.collections_url }}/{{ land }}">
<span class="v10-land-img{% unless has_photo %} is-art{% endunless %}" style="background:{{ la_bg }};color:{{ la_fg }}">{% if has_photo %}{{ limg | image_url: width: 900 | image_tag: loading: 'lazy', alt: la_roman, sizes: '(min-width: 900px) 30vw, 80vw', widths: '400,600,900' }}{% else %}''' + ART_SVG + '''{% endif %}<span class="v10-land-chap">''' + "{{ 'v9.ui.chapter' | t: n: lnum }}" + '''</span><span class="v10-land-vert" aria-hidden="true">{{ la_tc }}</span></span>
<span class="v10-land-txt"><span class="v9-land-name"><span class="z">{{ la_tc }}</span><span class="r">{{ la_roman }}</span></span>
<span class="v9-land-sub">''' + LAND_T('subtitle') + '''</span>{% unless compact %}<span class="v9-land-leg">''' + LAND_T('legend') + '''</span>{% endunless %}</span>
</a>''')
    # blessing chips for a product
    bl_case = ''.join("{%% when 'blessing-%s' %%}<a class=\"v10-chip\" href=\"{{ c.url }}\"><b>%s</b>%s</a>" % (k, BLESS[k]['char'], X('bless.%s.name' % k)) for k in BLESS_ORDER)
    w('snippets/v10-bless-chips.liquid', '''{%- for c in p.collections -%}{%- case c.handle -%}''' + bl_case + '''{%- endcase -%}{%- endfor -%}''')
    # blessing tiles
    tiles = ''.join('''<a class="v10-bless" href="{{ routes.collections_url }}/blessing-%s"><span class="c" aria-hidden="true">%s</span><span class="n">%s</span><span class="l">%s</span><span class="go">%s →</span></a>'''
                    % (k, BLESS[k]['char'], X('bless.%s.name' % k), X('bless.%s.line' % k), X('home.shopNow')) for k in BLESS_ORDER)
    w('snippets/v10-bless-tiles.liquid', '<div class="v10-bless-grid">' + tiles + '</div>')
    # lands carousel
    cards = ''.join("<li class=\"v10-slide\">{%% render 'v10-land-card', land: '%s' %%}</li>" % LAND_META[k][2] for k in LAND_ORDER)
    w('snippets/v10-lands-carousel.liquid', '''<div class="v10-carousel" data-v10-carousel>
<div class="v10-car-btns"><button type="button" class="v10-car-btn" data-v10-prev aria-label="''' + X('home.prev') + '''">←</button><button type="button" class="v10-car-btn" data-v10-next aria-label="''' + X('home.next') + '''">→</button></div>
<ul class="v10-track" data-v10-track>''' + cards + '''</ul></div>''')


# ------------------------------------------------------------------ header & footer
def header_footer():
    R = '{{ routes.collections_url }}/'
    shop_panel = '''<div class="v10-panel"><div class="v9-wrap v10-panel-in">
<div><p class="v10-ph">''' + X('nav.byType') + '''</p><a href="{{ routes.all_products_collection_url }}">''' + X('nav.all') + '''</a><a href="''' + R + '''bracelets">''' + X('nav.bracelets') + '''</a><a href="''' + R + '''necklaces">''' + X('nav.necklaces') + '''</a><a href="''' + R + '''charms">''' + X('nav.charms') + '''</a><a href="''' + R + '''accessories">''' + X('nav.accessories') + '''</a>
<p class="v10-ph" style="margin-top:22px">''' + X('nav.picks') + '''</p><a href="''' + R + '''everyday">''' + X('nav.everyday') + '''</a><a href="''' + R + '''gifting">''' + X('nav.gifting') + '''</a></div>
<div><p class="v10-ph">''' + X('nav.blessings') + '''</p>''' + ''.join('<a href="%sblessing-%s"><b class="v10-mini">%s</b>%s</a>' % (R, k, BLESS[k]['char'], X('bless.%s.name' % k)) for k in BLESS_ORDER) + '''</div>
<div><p class="v10-ph">''' + X('nav.byElement') + '''</p>''' + ''.join('<a href="%s%s"><b class="v10-mini" style="color:%s">%s</b>%s</a>' % (R, EL_HANDLE[k], EL_COLOR[k], EL_CHAR[k], t('el.%s.name' % k)) for k in ELS) + '''<a class="v10-more" href="''' + url('pages/five-elements') + '''">''' + X('nav.reading') + '''</a></div>
<div class="v10-feat">{%- assign fp = all_products['enduring-form'] -%}{% if fp != blank %}<a href="{{ fp.url }}"><span class="v9-square">{{ fp.featured_image | image_url: width: 500 | image_tag: loading: 'lazy', alt: fp.title }}</span><span class="v10-feat-t">{{ fp.title | escape }}</span><span class="v10-feat-p">{{ fp.price | money }}</span></a>{% endif %}</div>
</div></div>'''
    bless_panel = '''<div class="v10-panel"><div class="v9-wrap"><div class="v10-panel-bless">''' + ''.join(
        '<a href="%sblessing-%s"><span class="c">%s</span><span class="n">%s</span><span class="l">%s</span></a>' % (R, k, BLESS[k]['char'], X('bless.%s.name' % k), X('bless.%s.line' % k)) for k in BLESS_ORDER) + '''</div></div></div>'''
    land_links = ''.join("<a href=\"%s%s\">%s{%%- assign limg = images[la_file] -%%}<span class=\"v10-thumb\" style=\"background:{{ la_bg }}\">{%% if has_photo %%}{{ limg | image_url: width: 240 | image_tag: loading: 'lazy', alt: '' }}{%% else %%}%s{%% endif %%}</span><span><b>%s</b> %s</span></a>" % (R, LAND_META[k][2], land_case("'" + LAND_META[k][2] + "'"), ART_SVG, LAND_META[k][0], LAND_META[k][1]) for k in LAND_ORDER)
    lands_panel = '''<div class="v10-panel"><div class="v9-wrap"><div class="v10-panel-lands">''' + land_links + '''</div><a class="v10-more" href="{{ routes.root_url }}#lands">''' + X('nav.allLands') + '''</a></div></div>'''
    story_links = [('pages/brand', 'nav.brand'), ('pages/founder', 'nav.founder'), ('pages/care', 'nav.care'), ('pages/faq', 'nav.faq')]
    story_panel = '''<div class="v10-panel v10-panel-sm"><div class="v9-wrap v10-panel-list">''' + ''.join('<a href="%s">%s</a>' % (url(u), X(k)) for u, k in story_links) + '''</div></div>'''
    items = [('nav.shop', '{{ routes.all_products_collection_url }}', shop_panel),
             ('nav.blessings', "{{ routes.root_url }}#blessings", bless_panel),
             ('nav.lands', "{{ routes.root_url }}#lands", lands_panel),
             ('nav.elements', url('pages/five-elements'), ''),
             ('nav.story', url('pages/brand'), story_panel)]
    desk = ''.join('<div class="v10-item%s"><a class="v10-top" href="%s">%s%s</a>%s</div>' % (' has-panel' if p else '', h, X(k), ' <span aria-hidden="true" class="v10-caret">⌄</span>' if p else '', p) for k, h, p in items)
    # mobile
    mob = '<details><summary>' + X('nav.shop') + '</summary><div><a href="{{ routes.all_products_collection_url }}">' + X('nav.all') + '</a><a href="' + R + 'bracelets">' + X('nav.bracelets') + '</a><a href="' + R + 'necklaces">' + X('nav.necklaces') + '</a>' + '<a href="' + R + 'charms">' + X('nav.charms') + '</a><a href="' + R + 'accessories">' + X('nav.accessories') + '</a>' + ''.join('<a href="%s%s">%s · %s</a>' % (R, EL_HANDLE[k], X('nav.byElement'), t('el.%s.name' % k)) for k in ELS) + '</div></details>'
    mob += '<details><summary>' + X('nav.blessings') + '</summary><div>' + ''.join('<a href="%sblessing-%s">%s %s</a>' % (R, k, BLESS[k]['char'], X('bless.%s.name' % k)) for k in BLESS_ORDER) + '</div></details>'
    mob += '<details><summary>' + X('nav.lands') + '</summary><div>' + ''.join('<a href="%s%s">%s %s</a>' % (R, LAND_META[k][2], LAND_META[k][0], LAND_META[k][1]) for k in LAND_ORDER) + '</div></details>'
    mob += '<a class="v10-mlink" href="' + url('pages/five-elements') + '">' + X('nav.elements') + '</a>'
    mob += '<details><summary>' + X('nav.story') + '</summary><div>' + ''.join('<a href="%s">%s</a>' % (url(u), X(k)) for u, k in story_links) + '</div></details>'
    w('sections/v9-header.liquid', '''<header class="v9-header v9 v10-header">
<div class="v9-wrap v9-header-top">
<button class="v9-burger" type="button" data-v9-burger aria-controls="v9-mobile" aria-expanded="false" aria-label="''' + t('ui.menu') + '''">☰</button>
<span class="v9-header-note">''' + t('ui.note') + '''</span>
<a class="v9-logo" href="{{ routes.root_url }}" aria-label="CATHORA"><img src="{{ 'cathora-logo-v9.png' | asset_url }}" alt="CATHORA" width="640" height="340"></a>
<div class="v9-header-tools">{% render 'v9-localization', fid: 'v9-loc-top' %}<a class="v9-bag" href="{{ routes.cart_url }}">''' + t('ui.bag') + ''' (<span data-v9-count>{{ cart.item_count }}</span>)</a></div>
</div>
<nav class="v10-nav" aria-label="CATHORA"><div class="v9-wrap v10-nav-in">''' + desk + '''</div></nav>
<div class="v9-mobile v10-mobile" id="v9-mobile">''' + mob + '''{% render 'v9-localization', fid: 'v9-loc-mobile' %}</div>
</header>
{% schema %}{"name":"CATHORA header","settings":[]}{% endschema %}''')

    col = lambda title, links: '<nav aria-label="%s"><span>%s</span>%s</nav>' % (title, title, ''.join('<a href="%s">%s</a>' % (h, l) for h, l in links))
    w('sections/v9-footer.liquid', '''<footer class="v9-footer v9"><div class="v9-wrap">
<div class="v9-footer-grid">
<div><a href="{{ routes.root_url }}" aria-label="CATHORA"><img src="{{ 'cathora-logo-v9.png' | asset_url }}" alt="CATHORA" width="640" height="340" loading="lazy"></a><p class="v9-p" style="font-size:13px;margin:14px 0 0">''' + t('ui.note') + '''</p></div>
''' + col(X('nav.shop'), [('{{ routes.all_products_collection_url }}', X('nav.all')), (R + 'bracelets', X('nav.bracelets')), (R + 'necklaces', X('nav.necklaces')), (R + 'charms', X('nav.charms')), (R + 'accessories', X('nav.accessories')), ('{{ routes.root_url }}#blessings', X('nav.blessings'))]) + '''
''' + col(t('ui.fDiscover'), [('{{ routes.root_url }}#lands', X('nav.lands')), (url('pages/five-elements'), X('nav.elements')), (R + 'gifting', X('nav.gifting'))]) + '''
''' + col(X('nav.story'), [(url('pages/brand'), X('nav.brand')), (url('pages/founder'), X('nav.founder'))]) + '''
<nav aria-label="''' + t('ui.fHelp') + '''"><span>''' + t('ui.fHelp') + '''</span><a href="''' + url('pages/care') + '''">''' + X('nav.care') + '''</a><a href="''' + url('pages/faq') + '''">''' + X('nav.faq') + '''</a>{% if shop.shipping_policy.url != blank %}<a href="{{ shop.shipping_policy.url }}">''' + t('ui.fShipping') + '''</a>{% endif %}<a href="''' + url('pages/contact') + '''">''' + t('ui.fContact') + '''</a></nav>
</div>
<div class="v9-footer-bottom"><p>''' + t('ui.disclaimer') + '''</p><span>© {{ "now" | date: "%Y" }} {{ shop.name | escape }}{% if shop.privacy_policy.url != blank %} · <a href="{{ shop.privacy_policy.url }}" style="color:inherit">{{ shop.privacy_policy.title }}</a>{% endif %}</span></div>
</div></footer>
{% schema %}{"name":"CATHORA footer","settings":[]}{% endschema %}''')


# ------------------------------------------------------------------ home
def home():
    els = ''.join('''<a class="v9-el" href="%s#%s"><span class="o" aria-hidden="true" style="color:%s">%s</span><span class="n">%s</span><span class="l">%s</span></a>'''
                  % (url('pages/five-elements'), k, EL_COLOR[k], EL_CHAR[k], t('el.%s.name' % k), t('el.%s.line' % k)) for k in ELS)
    proms = ''.join('<div class="v9-promise"><b>%s</b><span>%s</span></div>' % (X('prom.p%d.t' % i), X('prom.p%d.l' % i)) for i in range(1, 5))
    w('sections/v9-home.liquid', '''<div class="v9">
{%- assign hero = section.settings.hero_product | default: all_products['enduring-form'] -%}
<section class="v9-wrap v9-hero" aria-labelledby="v9-hero-h"><div style="max-width:540px">
<p class="v9-eyebrow" style="margin-bottom:26px">''' + t('ui.eyebrow') + '''</p>
<h1 id="v9-hero-h" class="v9-h1 v9-pre">''' + t('ui.h1') + '''</h1>
<p class="v9-lede">''' + t('ui.lede') + '''</p>
<div class="v9-cta"><a class="v9-btn" href="{{ routes.all_products_collection_url }}">''' + X('home.heroCta1') + ''' <span aria-hidden="true">→</span></a><a class="v9-link" href="#blessings">''' + X('home.heroCta2') + '''</a></div></div>
{% if hero != blank %}<figure class="v9-figure"><a class="v9-square" href="{{ hero.url }}">{{ hero.featured_image | image_url: width: 1400 | image_tag: loading: 'eager', fetchpriority: 'high', alt: hero.title, sizes: '(min-width: 900px) 50vw, 100vw', widths: '600,900,1200,1400' }}</a>
<figcaption class="v9-figcap"><span>{{ hero.title | escape }}</span><span>{{ hero.price | money }} ↗</span></figcaption></figure>{% endif %}
</section>
<section id="blessings" class="v9-tint" aria-labelledby="v10-bless-h"><div class="v9-wrap" style="padding-top:88px;padding-bottom:96px">
<div class="v9-sec-head" style="margin-bottom:40px"><div><p class="v9-eyebrow red">''' + X('home.blessEyebrow') + '''</p><h2 id="v10-bless-h" class="v9-h2">''' + X('home.blessH') + '''</h2></div><p class="v9-p">''' + X('home.blessP') + '''</p></div>
{% render 'v10-bless-tiles' %}</div></section>
<section id="pieces" aria-labelledby="v9-pieces-h"><div class="v9-wrap v9-sec" style="padding-top:96px;padding-bottom:96px">
<div class="v9-row-head"><h2 id="v9-pieces-h" class="v9-h2">''' + X('home.bestH') + '''</h2><a class="v9-ul" href="{{ routes.all_products_collection_url }}">''' + t('ui.piecesLink') + '''</a></div>
<div class="v9-grid">{% for card_product in collections.all.products limit: 8 %}{% render 'v9-card', card_product: card_product %}{% endfor %}</div></div></section>
<section id="lands" class="v9-border-top" aria-labelledby="v10-lands-h"><div class="v9-wrap" style="padding-top:104px;padding-bottom:104px">
<div class="v9-sec-head" style="margin-bottom:44px"><div><p class="v9-eyebrow red">''' + t('ui.landsEyebrow') + '''</p><h2 id="v10-lands-h" class="v9-h2 v9-pre">''' + X('home.landsH') + '''</h2></div><p class="v9-p">''' + X('home.landsP') + '''</p></div>
{% render 'v10-lands-carousel' %}</div></section>
<section id="elements" class="v9-tint" aria-labelledby="v9-el-h"><div class="v9-wrap v9-sec"><div class="v9-two"><div style="max-width:500px">
<p class="v9-eyebrow red">''' + t('ui.elEyebrow') + '''</p><h2 id="v9-el-h" class="v9-h2 v9-pre">''' + t('ui.elH') + '''</h2><p class="v9-p" style="margin:26px 0 0">''' + t('ui.elP') + '''</p>
<a class="v9-btn" style="margin-top:34px" href="''' + url('pages/five-elements') + '''">''' + t('ui.elCta') + ''' <span aria-hidden="true">→</span></a></div>
<div class="v9-el-grid">''' + els + '''</div></div></div></section>
<section id="story" aria-labelledby="v9-story-h"><div class="v9-wrap v9-sec"><div class="v9-two" style="gap:72px">
<div class="v9-story-art"><img src="{{ 'cathora-mark.png' | asset_url }}" alt="" loading="lazy"></div>
<div style="max-width:540px"><p class="v9-eyebrow">''' + t('ui.storyEyebrow') + '''</p><h2 id="v9-story-h" class="v9-h2 v9-pre" style="font-size:clamp(32px,3.8vw,44px);line-height:1.14">''' + X('brand.teaserH') + '''</h2>
<p class="v9-serif-p" style="margin:26px 0 0">''' + X('brand.s1') + '''</p><p class="v9-serif-p" style="margin:16px 0 0">''' + X('brand.s2') + '''</p>
<div style="display:flex;flex-wrap:wrap;gap:28px;margin-top:36px"><a class="v9-ul" href="''' + url('pages/brand') + '''">''' + t('ui.storyL1') + '''</a><a class="v9-ul" href="''' + url('pages/founder') + '''">''' + t('ui.storyL2') + '''</a></div></div></div></div></section>
<section class="v9-tint v9-promises" aria-label="CATHORA"><div class="v9-wrap">''' + proms + '''</div></section>
<section class="v9-news" aria-labelledby="v9-news-h"><div class="v9-news-in"><h2 id="v9-news-h" class="v9-h2" style="font-size:36px">''' + t('ui.newsH') + '''</h2><p class="v9-p" style="margin:14px 0 0">''' + t('ui.newsP') + '''</p>{% render 'v9-newsletter', id: 'v9-news-home' %}</div></section>
</div>
{% schema %}{"name":"CATHORA home","settings":[{"type":"product","id":"hero_product","label":"Hero product / 主推商品"}],"presets":[{"name":"CATHORA home"}]}{% endschema %}''')


# ------------------------------------------------------------------ collection
def collection():
    bl_case = ''.join("{%%- when 'blessing-%s' -%%}{%%- assign bk = '%s' -%%}{%%- assign b_ch = '%s' -%%}" % (k, k, BLESS[k]['char']) for k in BLESS_ORDER)
    el_case = ''.join("{%%- when '%s' -%%}{%%- assign elk = '%s' -%%}{%%- assign el_c = '%s' -%%}{%%- assign el_ch = '%s' -%%}" % (EL_HANDLE[k], k, EL_COLOR[k], EL_CHAR[k]) for k in ELS)
    land_handles = ' '.join(LAND_META[k][2] for k in LAND_ORDER)
    others = ''.join("{%% unless collection.handle == '%s' %%}<li class=\"v10-slide\">{%% render 'v10-land-card', land: '%s', compact: true %%}</li>{%% endunless %%}" % (LAND_META[k][2], LAND_META[k][2]) for k in LAND_ORDER)
    other_bless = ''.join("{%% unless bk == '%s' %%}<a class=\"v10-chip lg\" href=\"{{ routes.collections_url }}/blessing-%s\"><b>%s</b>%s</a>{%% endunless %%}" % (k, k, BLESS[k]['char'], X('bless.%s.name' % k)) for k in BLESS_ORDER)
    crumb = lambda mid, cur: '<nav class="v9-wrap v9-crumb" aria-label="Breadcrumb"><a href="{{ routes.root_url }}">' + t('ui.crumbHome') + '</a><span aria-hidden="true">/</span>' + mid + '<span aria-current="page">' + cur + '</span></nav>'
    grid = '''{% if collection.products.size > 0 %}<div class="v9-grid w280">{% for card_product in collection.products %}{% render 'v9-card', card_product: card_product %}{% endfor %}</div>'''
    w('sections/v9-collection.liquid', '''{%- assign lk = '' -%}{%- assign bk = '' -%}{%- assign elk = '' -%}
{%- assign land_handles = "''' + land_handles + '''" | split: ' ' -%}
{%- if land_handles contains collection.handle -%}''' + land_case('collection.handle') + '''{%- endif -%}
{%- case collection.handle -%}''' + bl_case + el_case + '''{%- endcase -%}
<div class="v9">
{%- if lk != '' -%}
{%- capture lnum -%}''' + LAND_T('num') + '''{%- endcapture -%}{%- assign limg = images[la_file] -%}
''' + crumb('<a href="{{ routes.root_url }}#lands">' + t('ui.crumbLands') + '</a><span aria-hidden="true">/</span>', '{{ la_zh }} {{ la_roman }}') + '''
<figure class="v10-land-hero{% unless has_photo %} is-art{% endunless %}" style="background:{{ la_bg }};color:{{ la_fg }}">{% if has_photo %}{{ limg | image_url: width: 2400 | image_tag: loading: 'eager', fetchpriority: 'high', alt: la_roman, sizes: '100vw', widths: '800,1200,1800,2400' }}{% else %}''' + ART_SVG + '''{% endif %}<span class="v10-land-vert" aria-hidden="true">{{ la_tc }}</span></figure>
<section class="v9-wrap v9-land-title" aria-labelledby="v9-land-h"><div>
<p class="v9-eyebrow red" style="margin-bottom:20px">''' + t('ui.crumbLands') + ''' · {{ 'v9.ui.chapter' | t: n: lnum }}</p>
<h1 id="v9-land-h" class="v9-land-h"><span class="z">{{ la_tc }}</span><span class="r">{{ la_roman }}</span></h1>
<p class="v9-land-subt">''' + LAND_T('subtitle') + '''</p></div>
<dl class="v9-meta"><div><dt>''' + t('ui.mIntention') + '''</dt><dd>''' + LAND_T('intention') + '''</dd></div><div><dt>''' + t('ui.mElement') + '''</dt><dd><a href="''' + url('pages/five-elements') + '''#{{ la_el }}">''' + LAND_T('element') + '''</a></dd></div><div><dt>''' + t('ui.mKnown') + '''</dt><dd>''' + LAND_T('known') + '''</dd></div></dl>
</section>
<article class="v9-article">
<p class="a-lead">''' + LAND_T('lead') + '''</p>
{%- capture s1 -%}''' + LAND_T('s1') + '''{%- endcapture -%}{%- capture s2 -%}''' + LAND_T('s2') + '''{%- endcapture -%}{%- capture s3 -%}''' + LAND_T('s3') + '''{%- endcapture -%}
{% if s1 != blank %}<p class="a-p">{{ s1 }}</p>{% endif %}{% if s2 != blank %}<p class="a-p">{{ s2 }}</p>{% endif %}{% if s3 != blank %}<p class="a-p">{{ s3 }}</p>{% endif %}
<div class="a-rule" aria-hidden="true"></div><p class="a-close">''' + LAND_T('close') + '''</p>
</article>
<section class="v9-tint" aria-labelledby="v9-lp-h"><div class="v9-wrap" style="padding-top:96px;padding-bottom:104px">
{%- capture lname -%}{{ la_zh }} {{ la_roman }}{%- endcapture -%}
<h2 id="v9-lp-h" class="v9-h2" style="font-size:clamp(30px,3.4vw,40px);margin-bottom:40px">{{ 'v9.ui.piecesFrom' | t: land: lname }}</h2>
''' + grid + '''
{% else %}<div class="v9-empty"><p class="v9-serif-p" style="margin:0;font-size:24px;color:var(--v9-ink)">''' + t('ui.emptyH') + '''</p><p class="v9-p" style="margin:12px 0 0">''' + t('ui.emptyP') + '''</p>{% capture nl %}''' + t('ui.notify') + '''{% endcapture %}{% render 'v9-newsletter', id: 'v9-news-land', tag: collection.handle, label: nl %}<a class="v9-link" style="margin-top:20px" href="{{ routes.all_products_collection_url }}">''' + X('nav.all') + ''' →</a></div>{% endif %}
</div></section>
<section class="v9-wrap" style="padding-top:96px;padding-bottom:104px" aria-labelledby="v9-ol-h">
<div class="v9-row-head" style="margin-bottom:36px"><h2 id="v9-ol-h" class="v9-h2" style="font-size:36px">''' + t('ui.otherLands') + '''</h2><a class="v9-ul" href="{{ routes.root_url }}#lands">''' + t('ui.back') + '''</a></div>
<div class="v10-carousel" data-v10-carousel><div class="v10-car-btns"><button type="button" class="v10-car-btn" data-v10-prev aria-label="''' + X('home.prev') + '''">←</button><button type="button" class="v10-car-btn" data-v10-next aria-label="''' + X('home.next') + '''">→</button></div><ul class="v10-track" data-v10-track>''' + others + '''</ul></div></section>
{%- elsif bk != '' -%}
{%- capture bname -%}{{ 'v9.x.bless.' | append: bk | append: '.name' | t }}{%- endcapture -%}
''' + crumb('<a href="{{ routes.root_url }}#blessings">' + X('nav.blessings') + '</a><span aria-hidden="true">/</span>', '{{ bname }}') + '''
<section class="v9-wrap v10-bless-hero" aria-labelledby="v10-bh"><span class="v10-bless-ch" aria-hidden="true">{{ b_ch }}</span><div>
<p class="v9-eyebrow red">''' + X('nav.blessings') + '''</p><h1 id="v10-bh" class="v9-h1" style="font-size:clamp(44px,5.2vw,64px)">{{ bname }}</h1>
<p class="v9-land-subt" style="margin-top:12px">{{ 'v9.x.bless.' | append: bk | append: '.line' | t }}</p>
<p class="v9-p" style="max-width:620px;margin:20px 0 0">{{ 'v9.x.bless.' | append: bk | append: '.desc' | t }}</p></div></section>
<section class="v9-wrap" style="padding-top:64px;padding-bottom:88px">''' + grid + '''{% else %}<div class="v9-empty"><p class="v9-serif-p" style="margin:0;font-size:24px;color:var(--v9-ink)">''' + X('home.blessEmpty') + '''</p>{% capture nl %}''' + t('ui.notify') + '''{% endcapture %}{% render 'v9-newsletter', id: 'v9-news-bless', tag: collection.handle, label: nl %}<a class="v9-link" style="margin-top:20px" href="{{ routes.all_products_collection_url }}">''' + X('nav.all') + ''' →</a></div>{% endif %}</section>
<section class="v9-tint"><div class="v9-wrap" style="padding-top:56px;padding-bottom:64px"><p class="v9-label">''' + X('nav.allBlessings') + '''</p><div class="v10-chips">''' + other_bless + '''</div></div></section>
{%- elsif elk != '' -%}
{%- capture eln -%}{{ 'v9.el.' | append: elk | append: '.name' | t }}{%- endcapture -%}
''' + crumb('<a href="' + url('pages/five-elements') + '">' + t('ui.nav2') + '</a><span aria-hidden="true">/</span>', '{{ eln }}') + '''
<section class="v9-wrap v9-elhero" aria-labelledby="v9-elc-h"><div style="display:flex;gap:36px;align-items:center;flex-wrap:wrap"><span class="o" aria-hidden="true" style="background:{{ el_c }}">{{ el_ch }}</span>
<div><p class="v9-eyebrow red">''' + t('ui.elEyebrow') + '''</p><h1 id="v9-elc-h" class="v9-h1" style="font-size:clamp(44px,5vw,60px)">{{ eln }}</h1><p class="v9-kw" style="color:{{ el_c }};font-size:14px">{{ 'v9.el.' | append: elk | append: '.kw' | t }}</p></div></div>
<div><p class="v9-serif-p" style="margin:0">{{ 'v9.el.' | append: elk | append: '.desc' | t }}</p><p class="v9-label" style="margin:22px 0 6px">''' + t('eu.materials') + '''</p><p style="margin:0;font-size:15px">{{ 'v9.el.' | append: elk | append: '.materials' | t }}</p>
<a class="v9-btn" style="margin-top:28px" href="''' + url('pages/five-elements') + '''">''' + t('ui.elCta') + ''' <span aria-hidden="true">→</span></a></div></section>
<section class="v9-wrap" style="padding-top:80px;padding-bottom:104px"><h2 class="v9-h2" style="font-size:clamp(30px,3.4vw,40px);margin-bottom:40px">{{ 'v9.eu.piecesOf' | t: el: eln }}</h2>''' + grid + '''{% else %}<p class="v9-serif-p">''' + t('eu.emptyP') + '''</p>{% endif %}</section>
{%- else -%}
''' + crumb('', '{% if collection.handle == \'all\' %}' + X('nav.all') + '{% else %}{{ collection.title | escape }}{% endif %}') + '''
<section class="v9-wrap v9-col-head"><h1 class="v9-h1">{% if collection.handle == 'all' %}''' + X('nav.all') + '''{% else %}{{ collection.title | escape }}{% endif %}</h1>
<div class="v10-chips" style="margin-top:24px"><a class="v10-chip lg{% if collection.handle == 'all' %} on{% endif %}" href="{{ routes.all_products_collection_url }}">''' + X('nav.all') + '''</a><a class="v10-chip lg{% if collection.handle == 'bracelets' %} on{% endif %}" href="{{ routes.collections_url }}/bracelets">''' + X('nav.bracelets') + '''</a><a class="v10-chip lg{% if collection.handle == 'necklaces' %} on{% endif %}" href="{{ routes.collections_url }}/necklaces">''' + X('nav.necklaces') + '''</a><a class="v10-chip lg{% if collection.handle == 'charms' %} on{% endif %}" href="{{ routes.collections_url }}/charms">''' + X('nav.charms') + '''</a><a class="v10-chip lg{% if collection.handle == 'accessories' %} on{% endif %}" href="{{ routes.collections_url }}/accessories">''' + X('nav.accessories') + '''</a>''' + ''.join("<a class=\"v10-chip lg\" href=\"{{ routes.collections_url }}/blessing-%s\"><b>%s</b>%s</a>" % (k, BLESS[k]['char'], X('bless.%s.name' % k)) for k in BLESS_ORDER) + '''</div></section>
<section class="v9-wrap" style="padding-bottom:104px">{% paginate collection.products by 24 %}<div class="v9-grid w280">{% for card_product in collection.products %}{% render 'v9-card', card_product: card_product %}{% endfor %}</div>{% if collection.products_count == 0 %}<div class="v9-empty"><p class="v9-serif-p" style="margin:0;font-size:24px;color:var(--v9-ink)">''' + t('ui.emptyH') + '''</p><p class="v9-p" style="margin:12px 0 0">''' + t('ui.emptyP') + '''</p>{% capture nl %}''' + t('ui.notify') + '''{% endcapture %}{% render 'v9-newsletter', id: 'v9-news-col', tag: collection.handle, label: nl %}</div>{% endif %}
{% if paginate.pages > 1 %}<nav class="v9-pages" aria-label="Pagination">{% if paginate.previous %}<a class="v9-ul" href="{{ paginate.previous.url }}">←</a>{% endif %}<span>{{ paginate.current_page }} / {{ paginate.pages }}</span>{% if paginate.next %}<a class="v9-ul" href="{{ paginate.next.url }}">→</a>{% endif %}</nav>{% endif %}{% endpaginate %}</section>
{%- endif -%}
</div>
{% schema %}{"name":"CATHORA collection","settings":[]}{% endschema %}''')


# ------------------------------------------------------------------ product
def product():
    land_handles = ' '.join(LAND_META[k][2] for k in LAND_ORDER)
    el_find = ''.join("{%%- when '%s' -%%}{%%- assign pel = '%s' -%%}" % (EL_HANDLE[k], k) for k in ELS)
    ship_rows = ''.join('<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % r for r in [
        (X('pdp.shipIntl'), X('pdp.shipStd'), X('pdp.shipIstd'), 'SGD 15<br><small>' + X('pdp.shipFree') + '</small>'),
        (X('pdp.shipIntl'), X('pdp.shipExp'), X('pdp.shipIexp'), 'SGD 45')])
    faq = ''.join('<details class="v10-q"><summary>%s</summary><p>%s</p></details>' % (X('faq.q%d.q' % i), X('faq.q%d.a' % i)) for i in range(1, 5))
    acc = lambda key, body, open_=False: '<details class="v10-acc"%s><summary>%s</summary><div class="v10-acc-b">%s</div></details>' % (' open' if open_ else '', X(key), body)
    w('sections/v9-product.liquid', '''{%- assign pland = '' -%}{%- assign pel = '' -%}{%- assign is_bracelet = false -%}
{%- assign land_handles = "''' + land_handles + '''" | split: ' ' -%}
{%- for c in product.collections -%}{%- if land_handles contains c.handle and pland == '' -%}{%- assign pland = c.handle -%}{%- endif -%}{%- if c.handle == 'bracelets' -%}{%- assign is_bracelet = true -%}{%- endif -%}{%- case c.handle -%}''' + el_find + '''{%- endcase -%}{%- endfor -%}
{%- if pland != '' -%}''' + land_case('pland') + '''{%- endif -%}
{%- assign current = product.selected_or_first_available_variant -%}
{%- assign lc = request.locale.iso_code -%}{%- assign specs = product.metafields.custom.specs.value[lc] | default: product.metafields.custom.specs.value['en'] -%}
<script type="application/ld+json">{{ product | structured_data }}</script>
<div class="v9">
<nav class="v9-wrap v9-crumb" aria-label="Breadcrumb"><a href="{{ routes.root_url }}">''' + t('ui.crumbHome') + '''</a><span aria-hidden="true">/</span><a href="{{ routes.all_products_collection_url }}">''' + X('nav.shop') + '''</a><span aria-hidden="true">/</span><span aria-current="page">{{ product.title | escape }}</span></nav>
<section class="v9-wrap v9-pp" aria-labelledby="v9-pp-h">
<div class="v9-gallery" data-v9-gallery>
<div class="v9-square">{%- assign fm = product.featured_media -%}{% if fm %}{{ fm | image_url: width: 1400 | image_tag: class: 'v9-main', loading: 'eager', fetchpriority: 'high', alt: product.title, sizes: '(min-width: 900px) 50vw, 100vw', widths: '600,900,1200,1400' }}{% endif %}</div>
{% if product.media.size > 1 %}<div class="v9-thumbs">{% for m in product.media %}{% if m.media_type == 'image' %}<button type="button" data-v9-thumb data-src="{{ m | image_url: width: 1400 }}" aria-current="{% if forloop.first %}true{% else %}false{% endif %}" aria-label="''' + t('pp.image') + ''' {{ forloop.index }}">{{ m | image_url: width: 200 | image_tag: loading: 'lazy', alt: '' }}</button>{% endif %}{% endfor %}</div>{% endif %}
</div>
<div class="v10-buybox">
<div class="v9-tags">{% if pland != '' %}<a href="{{ routes.collections_url }}/{{ pland }}">''' + t('pp.land') + ''' · {{ la_zh }} {{ la_roman }}</a>{% endif %}{% if pel != '' %}<a href="{{ routes.collections_url }}/{% case pel %}''' + ''.join("{%% when '%s' %%}%s" % (k, EL_HANDLE[k]) for k in ELS) + '''{% endcase %}">{{ 'v9.pp.element' | t }} · {{ 'v9.el.' | append: pel | append: '.name' | t }}</a>{% endif %}</div>
<h1 id="v9-pp-h" class="v9-h1 v9-pp-title">{{ product.title | escape }}</h1>
<p class="v9-price" data-v9-price>{{ current.price | money }}</p>
<div class="v10-chips" style="margin-top:20px" aria-label="''' + X('pdp.blessFor') + '''">{% render 'v10-bless-chips', p: product %}</div>
{% form 'product', product, id: 'v9-buy-form', class: 'v9-buy-form' %}
<input type="hidden" name="id" value="{{ current.id }}">
{% if is_bracelet %}<label class="v9-variant">''' + X('pdp.size') + '''<select name="properties[Wrist size]"><option value="S 15cm">''' + X('pdp.sizeS') + '''</option><option value="M 16.5cm" selected>''' + X('pdp.sizeM') + '''</option><option value="L 18cm">''' + X('pdp.sizeL') + '''</option></select></label><p class="v10-help">''' + X('pdp.sizeHelp') + ''' <a class="v9-ul" style="font-size:12px" href="''' + url('pages/care') + '''">''' + t('pp.size') + '''</a></p>{% endif %}
<div class="v9-buy"><div class="v9-qty" data-v9-qty role="group" aria-label="''' + t('pp.qty') + '''"><button type="button" aria-label="−">−</button><input type="number" name="quantity" value="1" min="1" aria-label="''' + t('pp.qty') + '''"><button type="button" data-inc aria-label="+">+</button></div>
<button class="v9-btn" type="submit" data-v9-add data-label="''' + t('pp.add') + '''" data-adding="''' + t('pp.adding') + '''" data-added="''' + t('pp.added') + '''" data-sold="''' + t('pp.soldout') + '''"{% unless current.available %} disabled{% endunless %}>{% if current.available %}''' + t('pp.add') + '''{% else %}''' + t('pp.soldout') + '''{% endif %}</button></div>
{% endform %}
<ul class="v10-trust"><li>''' + X('pdp.trust1') + '''</li><li>''' + X('pdp.trust2') + '''</li><li>''' + X('pdp.trust3') + '''</li></ul>
<div class="v10-accs">
''' + acc('pdp.tabStory', '<div class="v9-desc" style="margin:0;border:0;padding:0">{{ product.description }}</div>', True) + '''
{% if specs %}''' + acc('pdp.tabSpecs', '<table class="v10-specs">{% for row in specs %}<tr><th scope="row">{{ row[0] }}</th><td>{{ row[1] }}</td></tr>{% endfor %}</table>') + '''{% endif %}
''' + acc('pdp.tabShip', '<p>' + X('pdp.shipIntro') + '</p><table class="v10-ship"><thead><tr><th>' + X('pdp.shipRegion') + '</th><th>' + X('pdp.shipMethod') + '</th><th>' + X('pdp.shipTime') + '</th><th>' + X('pdp.shipCost') + '</th></tr></thead><tbody>' + ship_rows + '</tbody></table><p class="v10-help">' + X('pdp.shipIntlList') + '</p><p class="v10-help">' + X('pdp.shipNote') + '</p>') + '''
''' + acc('pdp.tabReturns', '<p>' + X('pdp.returns') + '</p>') + '''
''' + acc('pdp.tabCare', '<ol class="v10-ol"><li>' + X('pdp.care1') + '</li><li>' + X('pdp.care2') + '</li><li>' + X('pdp.care3') + '</li><li>' + X('pdp.care4') + '</li></ol>') + '''
''' + acc('pdp.tabBox', '<p>' + X('pdp.box') + '</p>') + '''
''' + acc('pdp.tabFaq', faq) + '''
</div>
<div class="v9-pp-links">
{% if pland != '' %}{%- capture lname -%}{{ la_zh }} {{ la_roman }}{%- endcapture -%}<a class="v9-link" href="{{ routes.collections_url }}/{{ pland }}">{{ 'v9.pp.landLink' | t: land: lname }}</a>{% endif %}
<a class="v9-link" href="''' + url('pages/five-elements') + '''">''' + t('pp.readingLink') + '''</a>
</div>
</div>
</section>
{% if product.media.size > 1 %}<section class="v9-border-top v10-detail" aria-labelledby="v10-dh"><div class="v10-detail-in">
<p class="v9-eyebrow red" style="text-align:center">CATHORA</p><h2 id="v10-dh" class="v9-h2" style="text-align:center;font-size:clamp(30px,3.4vw,40px)">''' + X('pdp.detailH') + '''</h2><p class="v9-p" style="text-align:center;margin:10px 0 40px">''' + X('pdp.detailP') + '''</p>
{% for m in product.media offset: 1 %}{% if m.media_type == 'image' %}<figure class="v10-dimg">{{ m | image_url: width: 1600 | image_tag: loading: 'lazy', alt: m.alt, sizes: '(min-width: 1000px) 900px, 100vw', widths: '600,900,1200,1600' }}</figure>{% endif %}{% endfor %}
</div></section>{% endif %}
<section class="v9-border-top" aria-labelledby="v9-also-h"><div class="v9-wrap" style="padding-top:88px;padding-bottom:96px">
<h2 id="v9-also-h" class="v9-h2" style="font-size:36px;margin-bottom:36px">''' + t('pp.also') + '''</h2>
<div class="v9-grid w280">{%- assign shown = 0 -%}{%- for card_product in collections.all.products -%}{%- if card_product.id != product.id and shown < 4 -%}{%- assign shown = shown | plus: 1 -%}{% render 'v9-card', card_product: card_product %}{%- endif -%}{%- endfor -%}</div>
</div></section>
</div>
{% schema %}{"name":"CATHORA product","settings":[]}{% endschema %}''')


# ------------------------------------------------------------------ pages
def pages():
    BR = lambda k: X('brand.' + k)
    w('snippets/v10-brand.liquid', '''<div class="v9 v10-brand">
<nav class="v9-wrap v9-crumb" aria-label="Breadcrumb"><a href="{{ routes.root_url }}">''' + t('ui.crumbHome') + '''</a><span aria-hidden="true">/</span><span aria-current="page">''' + X('nav.story') + '''</span></nav>
<section class="v10-brand-hero"><div class="v9-wrap"><p class="v9-eyebrow red">''' + BR('eyebrow') + '''</p><h1 class="v9-h1">''' + BR('h1') + '''</h1><p class="v9-lede" style="max-width:640px">''' + BR('lede') + '''</p></div></section>
<section class="v9-wrap v10-name"><div><p class="v9-label">''' + BR('nameH') + '''</p><p class="v10-word">Cathay <span>+</span> ora</p></div><div class="v10-name-txt"><p class="v9-serif-p">''' + BR('n1') + '''</p><p class="v10-name-ora">''' + BR('n2') + '''</p><p class="v9-serif-p">''' + BR('n3') + '''</p></div></section>
<article class="v9-article v10-story">
<h2 class="v9-h2 v10-story-h">''' + BR('storyH') + '''</h2><p class="a-p">''' + BR('s1') + '''</p><p class="a-p">''' + BR('s2') + '''</p><p class="a-p">''' + BR('s3') + '''</p><p class="a-p">''' + BR('s4') + '''</p><p class="a-p">''' + BR('s4b') + '''</p><div class="a-rule" aria-hidden="true"></div><p class="a-close">''' + BR('s5') + '''</p></article>
<section class="v9-tint"><div class="v9-wrap v10-qi"><div><p class="v9-eyebrow red">''' + t('ui.elEyebrow') + '''</p><h2 class="v9-h2" style="font-size:clamp(32px,4vw,46px)">''' + BR('qiH') + '''</h2>
<div class="v10-wheel" aria-hidden="true">''' + ''.join('<span style="background:%s">%s</span>' % (EL_COLOR[k], EL_CHAR[k]) for k in ['water', 'wood', 'fire', 'earth', 'metal']) + '''</div></div>
<div><p class="v10-quote">''' + BR('qiQuote') + '''</p>''' + ''.join('<p class="v9-serif-p">%s</p>' % BR('qi%d' % i) for i in range(1, 8)) + '''<a class="v9-btn" style="margin-top:20px" href="''' + url('pages/five-elements') + '''">''' + BR('qiCta') + '''</a></div></div>
<div class="v9-wrap v10-elcards-wrap"><h3 class="v9-h3 v10-elcards-h">''' + BR('elCardsH') + '''</h3><div class="v10-elcards">''' + ''.join('<div class="v10-elcard"><span class="g" style="background:%s">%s</span><p class="m">%s</p><p class="a">%s</p><p class="p">%s</p></div>' % (EL_COLOR[k], EL_CHAR[k], BR('el_%s_m' % k), BR('el_%s_a' % k), BR('el_%s_p' % k)) for k in ['water', 'wood', 'fire', 'earth', 'metal']) + '''</div><div class="v10-elcta"><a class="v9-btn" href="''' + url('pages/five-elements') + '''">''' + BR('qiCta') + '''</a></div></div></section>
<section class="v9-wrap" style="padding-top:104px;padding-bottom:96px"><h2 class="v9-h2" style="font-size:clamp(30px,3.4vw,40px);margin-bottom:40px">''' + BR('princH') + '''</h2>
<div class="v10-princ">''' + ''.join('<div><span>0%d</span><h3 class="v9-h3">%s</h3><p class="v9-p">%s</p></div>' % (i, BR('pr%dt' % i), BR('pr%d' % i)) for i in (1, 2, 3)) + '''</div></section>
<section class="v9-tint v9-promises" aria-label="CATHORA"><div class="v9-wrap">''' + ''.join('<div class="v9-promise"><b>%s</b><span>%s</span></div>' % (X('prom.p%d.t' % i), X('prom.p%d.l' % i)) for i in range(1, 5)) + '''</div></section>
<section class="v9-wrap v10-founder-tease"><div><h2 class="v9-h2" style="font-size:clamp(30px,3.4vw,40px)">''' + BR('founderH') + '''</h2><p class="v9-p">''' + BR('founderP') + '''</p></div><a class="v9-link" href="''' + url('pages/founder') + '''">''' + BR('founderLink') + '''</a></section>

</div>''')
    w('snippets/v10-founder.liquid', '''<div class="v9">
<nav class="v9-wrap v9-crumb" aria-label="Breadcrumb"><a href="{{ routes.root_url }}">''' + t('ui.crumbHome') + '''</a><span aria-hidden="true">/</span><a href="''' + url('pages/brand') + '''">''' + X('nav.story') + '''</a><span aria-hidden="true">/</span><span aria-current="page">''' + X('nav.founder') + '''</span></nav>
<section class="v9-wrap v10-founder"><div class="v10-initial" aria-hidden="true">C</div><div>
<p class="v9-eyebrow red">''' + X('founder.eyebrow') + '''</p><h1 class="v9-h1 v9-pre" style="font-size:clamp(40px,5vw,60px)">''' + X('founder.h1') + '''</h1>
<div class="v10-founder-story">''' + ''.join("<p class=\"v9-serif-p\">%s</p>" % X('founder.f%d' % i) for i in range(1, 6)) + '<p class="v10-quote v10-fq">' + X('founder.fq') + '</p>' + ''.join("<p class=\"v9-serif-p\">%s</p>" % X('founder.f%d' % i) for i in range(6, 11)) + '''<p class="v10-sign">''' + X('founder.sign') + '''</p></div>
<a class="v9-link" style="margin-top:24px" href="''' + url('pages/brand') + '''">''' + X('nav.brand') + ''' →</a></div></section></div>''')
    C = lambda k: X('care.' + k)
    w('snippets/v10-care.liquid', '''<div class="v9">
<nav class="v9-wrap v9-crumb" aria-label="Breadcrumb"><a href="{{ routes.root_url }}">''' + t('ui.crumbHome') + '''</a><span aria-hidden="true">/</span><span aria-current="page">''' + C('h1') + '''</span></nav>
<section class="v9-wrap v9-col-head"><h1 class="v9-h1">''' + C('h1') + '''</h1><p class="v9-land-subt">''' + C('lead') + '''</p></section>
<section class="v9-wrap v10-care"><div><h2 class="v9-h2" style="font-size:30px">''' + C('sizeH') + '''</h2><p class="v9-p">''' + C('sizeP') + '''</p>
<table class="v10-specs"><thead><tr><th>''' + C('chartWrist') + '''</th><th>''' + C('chartSize') + '''</th></tr></thead><tbody><tr><td>13–14 cm</td><td>S · 15 cm</td></tr><tr><td>14.5–15.5 cm</td><td>M · 16.5 cm</td></tr><tr><td>16–17 cm</td><td>L · 18 cm</td></tr></tbody></table></div>
<div><h2 class="v9-h2" style="font-size:30px">''' + C('ritualH') + '''</h2><p class="v9-p">''' + X('pdp.care1') + '''</p>
<h2 class="v9-h2" style="font-size:30px;margin-top:40px">''' + C('careH') + '''</h2><ol class="v10-ol"><li>''' + X('pdp.care2') + '''</li><li>''' + X('pdp.care3') + '''</li><li>''' + X('pdp.care4') + '''</li></ol></div></section>
<section class="v9-tint"><div class="v9-wrap" style="padding-top:64px;padding-bottom:72px;max-width:900px"><h2 class="v9-h2" style="font-size:30px">''' + X('pdp.tabBox') + '''</h2><p class="v9-p">''' + X('pdp.box') + '''</p></div></section></div>''')
    faq = ''.join('<details class="v10-q"><summary>%s</summary><p>%s</p></details>' % (X('faq.q%d.q' % i), X('faq.q%d.a' % i)) for i in range(1, 5))
    w('snippets/v10-faq.liquid', '''<div class="v9">
<nav class="v9-wrap v9-crumb" aria-label="Breadcrumb"><a href="{{ routes.root_url }}">''' + t('ui.crumbHome') + '''</a><span aria-hidden="true">/</span><span aria-current="page">''' + X('nav.faq') + '''</span></nav>
<section class="v9-wrap v9-col-head"><h1 class="v9-h1">''' + X('nav.faq') + '''</h1></section>
<section class="v9-wrap" style="max-width:900px;padding-bottom:64px">''' + faq + '''
<details class="v10-q"><summary>''' + X('pdp.tabShip') + '''</summary><p>''' + X('pdp.shipIntro') + ''' ''' + X('pdp.shipNote') + '''</p></details>
<details class="v10-q"><summary>''' + X('pdp.tabReturns') + '''</summary><p>''' + X('pdp.returns') + '''</p></details>
<a class="v9-link" style="margin-top:28px" href="''' + url('pages/contact') + '''">''' + t('ui.fContact') + ''' →</a></section></div>''')
    s = open(os.path.join(B.OUT, 'sections_src/cathora-page.liquid')).read()
    s = s.replace("{% case page.handle %}", "{% case page.handle %}{% when 'five-elements' %}{% render 'v9-elements' %}{% when 'brand' %}{% render 'v10-brand' %}{% when 'founder' %}{% render 'v10-founder' %}{% when 'care' %}{% render 'v10-care' %}{% when 'faq' %}{% render 'v10-faq' %}", 1)
    s = s.replace("{% when 'brand' %}{% if request", "{% when 'brand-v8' %}{% if request").replace("{% when 'founder' %}{% if request", "{% when 'founder-v8' %}{% if request")
    w('sections/cathora-page.liquid', s)


CSS = r'''
/* ---------------- v10 ---------------- */
.v10-nav{border-top:1px solid var(--v9-line);position:relative}
.v10-nav-in{display:flex;justify-content:center;gap:4px 8px;flex-wrap:wrap}
.v10-item{position:static}
.v10-top{display:inline-flex;align-items:center;gap:6px;min-height:52px;padding:0 18px;font-size:15px}
.v10-caret{font-size:12px;color:var(--v9-muted);transform:translateY(-2px)}
.v10-panel{display:none;position:absolute;left:0;right:0;top:100%;background:var(--v9-paper);border-top:1px solid var(--v9-line);border-bottom:1px solid var(--v9-line);box-shadow:0 18px 40px rgba(39,43,36,.08);z-index:40;padding:36px 0 40px}
.v10-item.has-panel:hover .v10-panel,.v10-item.has-panel:focus-within .v10-panel{display:block}
.v10-item.has-panel:hover .v10-top{color:var(--v9-red)}
.v10-panel-in{display:grid;grid-template-columns:1fr 1fr 1fr 1.1fr;gap:40px}
.v10-panel a{display:flex;align-items:center;gap:10px;min-height:38px;font-size:15px}
.v10-ph{margin:0 0 10px;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--v9-muted)}
.v10-mini{display:inline-flex;width:28px;height:28px;border:1px solid currentColor;border-radius:50%;align-items:center;justify-content:center;font-family:var(--v9-cjk);font-weight:400;font-size:14px;color:var(--v9-red)}
.v10-more{margin-top:10px;font-size:14px;color:var(--v9-red)!important}
.v10-feat a{display:flex;flex-direction:column;align-items:stretch;gap:8px}
.v10-feat-t{font-family:var(--v9-serif);font-size:18px}.v10-feat-p{font-size:13px;color:var(--v9-muted)}
.v10-panel-bless{display:grid;grid-template-columns:repeat(6,1fr);gap:16px}
.v10-panel-bless a{display:flex;flex-direction:column;align-items:flex-start;gap:6px;padding:18px;border:1px solid var(--v9-line);min-height:0}
.v10-panel-bless .c{font-family:var(--v9-cjk);font-size:34px;line-height:1;color:var(--v9-red)}
.v10-panel-bless .n{font-family:var(--v9-serif);font-size:19px}.v10-panel-bless .l{font-size:12px;line-height:1.5;color:var(--v9-muted)}
.v10-panel-lands{display:grid;grid-template-columns:repeat(4,1fr);gap:14px 24px}
.v10-panel-lands a{gap:14px}
.v10-thumb{flex:0 0 72px;width:72px;height:54px;overflow:hidden;background:var(--v9-soft)}
.v10-thumb img{display:block;width:100%;height:100%;object-fit:cover}
.v10-panel-lands b{font-family:var(--v9-cjk);font-weight:500}
.v10-panel-sm{padding:24px 0}
.v10-panel-list{display:flex;justify-content:center;gap:40px}
.v10-mobile details{border-bottom:1px solid var(--v9-line)}
.v10-mobile summary{min-height:52px;display:flex;align-items:center;justify-content:space-between;font-size:16px;cursor:pointer;list-style:none}
.v10-mobile summary::after{content:'+';color:var(--v9-muted)}
.v10-mobile details[open] summary::after{content:'−'}
.v10-mobile details div{padding:0 0 12px 12px}
.v10-mobile details div a{min-height:42px;border:0;font-size:15px}
.v10-mobile .v10-mlink{border-bottom:1px solid var(--v9-line)}
@media (max-width:860px){.v10-nav{display:none}}
/* blessing tiles */
.v10-bless-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(180px,100%),1fr));gap:1px;background:#DDD9CF;border:1px solid #DDD9CF}
.v10-bless{display:flex;flex-direction:column;align-items:center;text-align:center;gap:12px;padding:40px 18px 34px;background:var(--v9-paper);transition:background .3s}
.v10-bless:hover{background:#fff}
.v10-bless .c{font-family:var(--v9-cjk);font-size:54px;line-height:1;color:var(--v9-ink)}
.v10-bless:hover .c{color:var(--v9-red)}
.v10-bless .n{font-family:var(--v9-serif);font-size:21px}
.v10-bless .l{font-size:13px;line-height:1.55;color:var(--v9-muted);min-height:40px}
.v10-bless .go{font-size:13px;border-bottom:1px solid var(--v9-ink);padding-bottom:2px}
/* carousel */
.v10-carousel{position:relative}
.v10-car-btns{position:absolute;right:0;top:-92px;display:flex;gap:10px}
.v10-car-btn{width:48px;height:48px;border:1px solid var(--v9-ink);border-radius:50%;background:transparent;color:var(--v9-ink);font-size:18px;cursor:pointer}
.v10-car-btn:hover{background:var(--v9-ink);color:var(--v9-paper)}
.v10-track{list-style:none;margin:0;padding:0 0 12px;display:flex;gap:20px;overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:thin;-webkit-overflow-scrolling:touch}
.v10-slide{flex:0 0 clamp(250px,27vw,340px);scroll-snap-align:start}
.v10-land{display:flex;flex-direction:column;gap:16px}
.v10-land-img{display:block;position:relative;aspect-ratio:3/4;overflow:hidden;background:var(--v9-soft)}
.v10-land-img img{display:block;width:100%;height:100%;object-fit:cover;transition:transform 1s ease}
.v10-land:hover .v10-land-img img{transform:scale(1.04)}
.v10-land-img::after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(20,22,18,.35) 0%,rgba(20,22,18,0) 40%)}
.v10-land-chap{position:absolute;z-index:1;top:16px;left:16px;font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:#FBFAF7}
.v10-land-vert{position:absolute;z-index:1;top:14px;right:14px;writing-mode:vertical-rl;font-family:var(--v9-cjk);font-size:20px;letter-spacing:.4em;color:#FBFAF7}
.v10-land-txt{display:flex;flex-direction:column;gap:6px}
@media (max-width:860px){.v10-car-btns{position:static;justify-content:flex-end;margin-bottom:14px}.v10-slide{flex-basis:76vw}}
/* land hero photo */
.v10-land-hero{position:relative;margin:0;height:clamp(340px,52vw,640px);overflow:hidden;background:var(--v9-soft)}
.v10-land-hero img{display:block;width:100%;height:100%;object-fit:cover}
.v10-land-hero .v10-land-vert{top:36px;right:44px;font-size:30px;letter-spacing:.5em;text-shadow:0 1px 12px rgba(0,0,0,.25)}
.v10-credit{position:absolute;right:14px;bottom:10px;font-size:11px;color:rgba(251,250,247,.85);text-shadow:0 1px 4px rgba(0,0,0,.5)}
.v10-credit a{color:inherit!important;text-decoration:underline}
/* chips */
.v10-chips{display:flex;flex-wrap:wrap;gap:8px}
.v10-chip{display:inline-flex;align-items:center;gap:8px;min-height:34px;padding:0 14px 0 6px;border:1px solid var(--v9-line);border-radius:20px;font-size:13px;background:var(--v9-paper)}
.v10-chip b{display:inline-flex;width:24px;height:24px;border-radius:50%;background:var(--v9-red);color:var(--v9-paper);align-items:center;justify-content:center;font-family:var(--v9-cjk);font-weight:400;font-size:13px}
.v10-chip.lg{min-height:42px;font-size:14px;padding:0 18px}
.v10-chip.lg b{margin-left:-10px}
.v10-chip.on{background:var(--v9-ink);color:var(--v9-paper)!important;border-color:var(--v9-ink)}
/* blessing hero */
.v10-bless-hero{display:flex;gap:48px;align-items:center;flex-wrap:wrap;padding-top:56px;padding-bottom:64px;border-bottom:1px solid var(--v9-line)}
.v10-bless-ch{display:flex;flex:0 0 auto;width:clamp(140px,18vw,200px);height:clamp(140px,18vw,200px);border-radius:50%;background:var(--v9-red);color:var(--v9-paper);align-items:center;justify-content:center;font-family:var(--v9-cjk);font-size:clamp(64px,8vw,92px)}
/* product */
.v10-buybox{max-width:560px}
.v10-help{margin:8px 0 0;font-size:12px;line-height:1.6;color:var(--v9-muted)}
.v10-trust{list-style:none;margin:26px 0 0;padding:18px 0 0;border-top:1px solid var(--v9-line);display:flex;flex-direction:column;gap:10px;font-size:13px;color:var(--v9-body)}
.v10-trust li::before{content:'✓';color:var(--v9-red);margin-right:10px}
.v10-accs{margin-top:34px;border-top:1px solid var(--v9-ink)}
.v10-acc{border-bottom:1px solid var(--v9-line)}
.v10-acc summary{display:flex;justify-content:space-between;align-items:center;min-height:60px;cursor:pointer;list-style:none;font-family:var(--v9-serif);font-size:21px}
.v10-acc summary::-webkit-details-marker,.v10-q summary::-webkit-details-marker,.v10-mobile summary::-webkit-details-marker{display:none}
.v10-acc summary::after{content:'+';font-family:var(--v9-sans);font-size:20px;color:var(--v9-muted)}
.v10-acc[open] summary::after{content:'−'}
.v10-acc-b{padding:0 0 24px;font-size:15px;line-height:1.8;color:var(--v9-body)}
.v10-acc-b p{margin:0 0 12px}
.v10-specs,.v10-ship{width:100%;border-collapse:collapse;font-size:14px}
.v10-specs th,.v10-specs td,.v10-ship th,.v10-ship td{text-align:left;padding:11px 12px 11px 0;border-bottom:1px solid var(--v9-line);vertical-align:top}
.v10-specs th{width:34%;font-weight:400;color:var(--v9-muted)}
.v10-ship thead th{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--v9-muted);font-weight:400}
.v10-ol{margin:0;padding-left:20px}.v10-ol li{margin-bottom:10px}
.v10-q{border-bottom:1px solid var(--v9-line)}
.v10-q summary{min-height:54px;display:flex;align-items:center;justify-content:space-between;gap:16px;cursor:pointer;list-style:none;font-size:15px;color:var(--v9-ink)}
.v10-q summary::after{content:'+';color:var(--v9-muted)}
.v10-q[open] summary::after{content:'−'}
.v10-q p{margin:0 0 18px;font-size:14px;line-height:1.75;color:var(--v9-body)}
.v10-detail{background:#fff}
.v10-detail-in{max-width:900px;margin:0 auto;padding:88px 20px 96px}
.v10-dimg{margin:0 0 16px}.v10-dimg img{display:block;width:100%;height:auto}
.v9-gallery{top:20px}
@media (max-width:899px){.v9-gallery{position:static!important}}
/* brand */
.v10-brand-hero{padding:72px 0 64px;border-bottom:1px solid var(--v9-line)}
.v10-brand-hero .v9-h1{font-size:clamp(48px,7vw,92px);line-height:1.02}
.v10-name{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(320px,100%),1fr));gap:56px;padding-top:80px;padding-bottom:80px;align-items:center}
.v10-word{margin:0;font-family:'EB Garamond',serif;font-size:clamp(48px,6vw,80px);line-height:1}
.v10-word span{color:var(--v9-red)}
.v10-story .a-p{font-size:20px}
.v10-story-h{font-size:clamp(30px,3.6vw,42px);margin:0 0 36px}
.v10-name-txt .v9-serif-p{margin:0 0 18px}
.v10-name-ora{margin:0 0 18px;font-family:var(--v9-serif);font-style:italic;font-size:28px;color:var(--v9-red)}
.v10-quote{margin:0 0 24px;font-family:var(--v9-serif);font-style:italic;font-size:24px;line-height:1.5;color:var(--v9-ink);border-left:2px solid var(--v9-red);padding-left:20px}
.v10-land-img.is-art::after{display:none}
.v10-land-img.is-art .v10-art{position:absolute;left:0;right:0;bottom:16%;width:100%;height:auto;transition:transform .6s ease}
.v10-land:hover .v10-land-img.is-art .v10-art{transform:translateY(-4px)}
.v10-land-img.is-art .v10-land-chap,.v10-land-img.is-art .v10-land-vert{color:inherit;text-shadow:none}
.v10-land-hero.is-art{display:flex;align-items:center;justify-content:center}
.v10-land-hero.is-art .v10-art{width:min(760px,80%);height:auto}
.v10-land-hero.is-art .v10-land-vert{color:inherit;text-shadow:none}
.v10-thumb .v10-art{display:block;width:100%;height:100%}
.v10-qi{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(320px,100%),1fr));gap:64px;padding-top:96px;padding-bottom:96px;align-items:start}
.v10-elcards-wrap{padding-bottom:96px}.v10-elcards-h{margin:0 0 28px}
.v10-elcards{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:1px;background:var(--v9-line,#DDD9D0);border:1px solid var(--v9-line,#DDD9D0)}
.v10-elcard{background:var(--v9-paper,#FBFAF7);padding:28px 22px 30px}
.v10-elcard .g{display:flex;width:52px;height:52px;border-radius:50%;color:#FBFAF7;align-items:center;justify-content:center;font-family:var(--v9-cjk);font-size:24px;margin-bottom:18px}
.v10-elcard .m{margin:0 0 4px;font-family:var(--v9-serif);font-size:20px}.v10-elcta{margin-top:40px;text-align:center}.v10-elcard .a{margin:0 0 14px;font-size:12px;letter-spacing:.06em;color:var(--v9-red)}
.v10-elcard .p{margin:0;font-size:14px;line-height:1.75;color:var(--v9-muted)}
.v10-fq{margin:36px 0 36px;font-size:clamp(22px,2.4vw,28px)}
@media (max-width:1000px){.v10-elcards{grid-template-columns:repeat(2,minmax(0,1fr))}.v10-elcard:last-child{grid-column:1/-1}}@media (max-width:560px){.v10-elcards{grid-template-columns:1fr}}
.v10-wheel{display:flex;gap:10px;margin-top:32px;flex-wrap:wrap}
.v10-wheel span{display:flex;width:56px;height:56px;border-radius:50%;color:var(--v9-paper);align-items:center;justify-content:center;font-family:var(--v9-cjk);font-size:24px}
.v10-princ{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(260px,100%),1fr));gap:40px}
.v10-princ div{border-top:1px solid var(--v9-ink);padding-top:20px}
.v10-princ span{font-size:12px;letter-spacing:.18em;color:var(--v9-red)}
.v10-princ .v9-h3{font-size:24px;margin:10px 0 10px}
.v10-founder-tease{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:end;gap:24px;padding-top:88px;padding-bottom:88px}
.v10-credits{padding-top:48px;padding-bottom:56px}
.v10-credits ul{margin:12px 0 0;padding:0;list-style:none;display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:6px 24px;font-size:12px;color:var(--v9-muted)}
.v10-credits a{color:var(--v9-muted)!important;text-decoration:underline}
.v10-founder{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2fr);gap:64px;padding-top:56px;padding-bottom:104px;align-items:start}
.v10-initial{aspect-ratio:3/4;background:var(--v9-soft);display:flex;align-items:center;justify-content:center;font-family:'EB Garamond',serif;font-size:160px;color:#C9C5BB}
.v10-founder-story{margin-top:32px}.v10-founder-story .v9-serif-p{margin:0 0 20px}
.v10-sign{margin:28px 0 0;font-family:var(--v9-serif);font-style:italic;font-size:18px;color:var(--v9-muted)}
.v10-care{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(360px,100%),1fr));gap:64px;padding-bottom:88px}
@media (max-width:760px){.v10-founder{grid-template-columns:1fr}.v10-initial{max-width:260px}}
'''

JS = r'''
/* v10 carousel */
(function(){document.querySelectorAll('[data-v10-carousel]').forEach(function(c){var tr=c.querySelector('[data-v10-track]');if(!tr)return;var step=function(d){var s=tr.querySelector('.v10-slide');var wdt=s?s.getBoundingClientRect().width+20:300;tr.scrollBy({left:d*wdt,behavior:'smooth'});};var p=c.querySelector('[data-v10-prev]'),n=c.querySelector('[data-v10-next]');if(p)p.addEventListener('click',function(){step(-1)});if(n)n.addEventListener('click',function(){step(1)});});})();
'''


def assets():
    p = os.path.join(B.OUT, 'assets/cathora-v9.css')
    s = open(p).read().split('/* ---------------- v10 ---------------- */')[0]
    open(p, 'w').write(s + CSS)
    p = os.path.join(B.OUT, 'assets/cathora-v9.js')
    s = open(p).read().split('/* v10 carousel */')[0]
    import v10_reading
    if 'window.v10Fav' not in s:
        s = s.replace('function render(r) {', 'function render(r) { if (window.v10Fav) window.v10Fav(r);', 1)
        s = s.replace('    var recs = [];', "    h += (window.v10Reading ? window.v10Reading(r, T) : '');\n    var recs = [];", 1)
    if 'window.v10Render' not in s:
        s = s.replace('function render(r) { if (window.v10Fav) window.v10Fav(r);', "function render(r) { if (window.v10Fav) window.v10Fav(r); if (window.v10Render) { var hx = window.v10Render(r, T, P); if (hx) { out.innerHTML = hx; out.hidden = false; selectTab(r.favorable[0]); out.scrollIntoView({ behavior: 'smooth', block: 'start' }); return; } }", 1)
    assert 'window.v10Render' in s
    open(p, 'w').write(s + JS + v10_reading.JS)
    p = os.path.join(B.OUT, 'assets/cathora-v9.css')
    open(p, 'a').write(v10_reading.CSS)


if __name__ == '__main__':
    locales(); snippets(); header_footer(); home(); collection(); product(); pages(); assets()
    B.templates(); B.layout()
    for f in ['snippets/v9-land-card.liquid']:
        fp = os.path.join(B.OUT, f)
        if os.path.exists(fp): os.remove(fp)
    print('ok')
