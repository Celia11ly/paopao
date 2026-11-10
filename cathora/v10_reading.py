# -*- coding: utf-8 -*-
"""v10.8: detailed Five Elements reading (favourable / unfavourable with reasons, guide)."""
import json

ELS = ['wood', 'fire', 'earth', 'metal', 'water']

R = {}

R['zh'] = {
    'h': '你的五行详解', 's1H': '一 · 日主旺衰', 's2H': '二 · 喜用神', 's3H': '三 · 忌神', 's4H': '四 · 调候与五行缺失', 's5H': '开运指南 · 亲近你的喜用',
    'season': {'spring': '春', 'summer': '夏', 'autumn': '秋', 'winter': '冬'},
    'seasonP_same': '你的日主为{stem}{el}，生于{season}月，{sel}气当令，正得天时。',
    'seasonP_gen': '你的日主为{stem}{el}，生于{season}月，{sel}气当令；{sel}生{el}，得时令相生。',
    'seasonP_other': '你的日主为{stem}{el}，生于{season}月，{sel}气当令，日主不得时令。',
    'strongP': '命局中生扶你的力量——{res}与{same}——约占 {pct}%，属「{level}」。气盛如满溢之水，宜疏不宜堵：需要能克、能泄、能耗的五行，把过盛的能量引向成就。',
    'weakP': '命局中生扶你的力量——{res}与{same}——仅约占 {pct}%，属「{level}」。气弱如将尽之灯，宜添不宜耗：需要能生、能扶的五行，为你补足根气。',
    'roles': {'res': '「印」，生扶你的力量，象征学识、贵人与庇护', 'same': '「比劫」，与你同气，象征意志、自我与同伴',
              'out': '「食伤」，由你生发，象征才华、表达与创造', 'wea': '「财」，为你所驭，象征财富、资源与成果', 'off': '「官杀」，约束你的力量，象征规则、事业与名位'},
    'use_wea': '取{X}为用神。{X}是你的{role}。身旺能任财——以财耗身，把过盛的能量化为实实在在的收获。',
    'use_off': '取{X}为用神。{X}是你的{role}。为过旺的意志立下方圆，锋芒便能化为事业与名望。',
    'use_out': '取{X}为用神。{X}是你的{role}。泄去过盛之气，化为才华与创造，气顺则运通。',
    'use_res': '取{X}为用神。{X}是你的{role}。如母养子，为你补足根气，也化解外来的压力。',
    'use_same': '取{X}为用神。{X}是你的{role}。同气相求，并肩而行，让你担得起眼前的财富与责任。',
    'xi_gen': '以{Y}为喜神。{Y}生{X}，让用神源源不绝。',
    'xi_flow': '以{Y}为喜神。{X}生{Y}，才华得以化为收获，气有所归。',
    'xi_ally': '以{Y}为喜神。它与用神相辅相成，一同为你扶身。',
    'ji_strong': '忌{A}、{B}。二者都在生扶你的日主——本已满溢的气再被添薪加火，容易刚愎、急躁、心神难安，做事反而事倍功半。',
    'ji_weak': '忌{A}、{B}。{A}是你的{roleA}；{B}是你的{roleB}。身弱之时再被克、泄、耗，如负重远行，容易力不从心、压力倍增、财来财去。',
    'summer': '你生于夏月，天地火气正盛，命局偏于燥热。{tail}', 'summerIn': '水正在你的喜用之中，天时与命理相合，更宜多加亲近。', 'summerOut': '不妨适度亲近水，以润其燥，作为调候。',
    'winter': '你生于冬月，天地寒气凝重，命局偏于寒湿。{tail}', 'winterIn': '火正在你的喜用之中，天时与命理相合，更宜多加亲近。', 'winterOut': '不妨适度亲近火，以暖其寒，作为调候。',
    'missing': '你的八字中五行缺{list}。缺不一定是坏事：若它正是你的喜用，便是最值得补的那一行；若是忌神，缺反而是福。',
    'missingFav': '其中，{list}正是你的喜用，宜多亲近。', 'sep': '、',
    'rows': {'color': '幸运色', 'dir': '吉方位', 'num': '幸运数字', 'season': '旺运时节', 'mat': '宜佩材质', 'life': '生活与事业'},
    'chips': {'yong': '用神', 'xi': '喜神', 'ji': '忌神'},
    'guide': {
        'wood': {'color': '青、绿', 'dir': '东方', 'num': '3、8', 'season': '春季', 'life': '多亲近草木，晨间散步；宜教育、文化、设计、园艺等生长之业。'},
        'fire': {'color': '红、紫、橙', 'dir': '南方', 'num': '2、7', 'season': '夏季', 'life': '多晒太阳，保持热情与交流；宜传媒、表演、餐饮、能源等光明之业。'},
        'earth': {'color': '黄、棕、米', 'dir': '中央、东北、西南', 'num': '5、10', 'season': '四季之交', 'life': '规律作息，脚踏实地；宜地产、建筑、农业、管理等承载之业。'},
        'metal': {'color': '白、金、银', 'dir': '西方', 'num': '4、9', 'season': '秋季', 'life': '断舍离，保持整洁与秩序；宜金融、法律、科技、精密制造等决断之业。'},
        'water': {'color': '黑、蓝', 'dir': '北方', 'num': '1、6', 'season': '冬季', 'life': '多亲近水，静坐冥想；宜贸易、物流、旅行、咨询等流通之业。'},
    },
}

R['en'] = {
    'h': 'Your elements, in depth', 's1H': 'I · Day master strength', 's2H': 'II · Favourable elements', 's3H': 'III · Elements to avoid', 's4H': 'IV · Season and missing elements', 's5H': 'Bringing in good fortune',
    'season': {'spring': 'spring', 'summer': 'summer', 'autumn': 'autumn', 'winter': 'winter'},
    'seasonP_same': 'Your day master is {stem} {el}, born in {season}, when {sel} is in command — you were born in your own season.',
    'seasonP_gen': 'Your day master is {stem} {el}, born in {season}, when {sel} is in command; {sel} feeds {el}, so the season is on your side.',
    'seasonP_other': 'Your day master is {stem} {el}, born in {season}, when {sel} is in command — not your own season.',
    'strongP': 'The forces that support you — {res} and {same} — make up about {pct}% of your chart: {level}. Strong qi is like water at the brim: it should be channelled, not dammed. You need the elements that restrain, express and spend, to turn surplus energy into achievement.',
    'weakP': 'The forces that support you — {res} and {same} — make up only about {pct}% of your chart: {level}. Gentle qi is like a lamp low on oil: add to it, don\'t drain it. You need the elements that nourish and support, to strengthen your roots.',
    'roles': {'res': 'Resource — the force that nourishes you: learning, mentors and protection', 'same': 'Companion — the same breath as you: will, self and allies',
              'out': 'Expression — what flows out of you: talent, voice and creativity', 'wea': 'Wealth — what you master: money, resources and results', 'off': 'Authority — the force that shapes you: rules, career and standing'},
    'use_wea': 'Your primary favourable element is {X}. {X} is your {role}. A strong chart can carry wealth — spending energy on it turns surplus into real reward.',
    'use_off': 'Your primary favourable element is {X}. {X} is your {role}. It gives an overly strong will a shape to work within, so its edge becomes career and reputation.',
    'use_out': 'Your primary favourable element is {X}. {X} is your {role}. It lets surplus qi flow out as talent and creation; when qi flows, fortune follows.',
    'use_res': 'Your primary favourable element is {X}. {X} is your {role}. Like a mother nourishing a child, it replenishes your roots and softens pressure from outside.',
    'use_same': 'Your primary favourable element is {X}. {X} is your {role}. Kindred breath walking beside you, it gives you the strength to carry the wealth and responsibility in front of you.',
    'xi_gen': '{Y} is your supporting element: {Y} feeds {X}, keeping it strong.',
    'xi_flow': '{Y} is your supporting element: {X} feeds {Y}, so talent finds its way into reward.',
    'xi_ally': '{Y} is your supporting element: it works alongside {X} to hold you up.',
    'ji_strong': 'Avoid too much {A} and {B}. Both add to a day master that is already full — more fuel on the fire. It can make you stubborn, restless and scattered, so effort yields less.',
    'ji_weak': 'Avoid too much {A} and {B}. {A} is your {roleA}; {B} is your {roleB}. When your qi is already gentle, being restrained, drained and spent is like carrying a heavy load a long way: stretched thin, under pressure, money in and out.',
    'summer': 'You were born in summer, when the fire of heaven and earth is at its height; your chart runs hot and dry. {tail}', 'summerIn': 'Water is already among your favourable elements — season and chart agree, so draw close to it.', 'summerOut': 'It is worth keeping some water near, to cool and moisten — a seasonal adjustment.',
    'winter': 'You were born in winter, when the cold of heaven and earth runs deep; your chart runs cold and damp. {tail}', 'winterIn': 'Fire is already among your favourable elements — season and chart agree, so draw close to it.', 'winterOut': 'It is worth keeping some fire near, to warm — a seasonal adjustment.',
    'missing': 'Your chart has no {list}. Missing is not necessarily bad: if it is favourable, it is the element most worth adding; if it is one to avoid, its absence is a blessing.',
    'missingFav': 'Of these, {list} is favourable for you — draw close to it.', 'sep': ', ',
    'rows': {'color': 'Lucky colours', 'dir': 'Best direction', 'num': 'Lucky numbers', 'season': 'Strongest season', 'mat': 'Materials to wear', 'life': 'Life & work'},
    'chips': {'yong': 'Primary', 'xi': 'Supporting', 'ji': 'Avoid'},
    'guide': {
        'wood': {'color': 'Green, teal', 'dir': 'East', 'num': '3, 8', 'season': 'Spring', 'life': 'Spend time among plants and walk in the morning; suited to education, culture, design, gardening — work that grows.'},
        'fire': {'color': 'Red, purple, orange', 'dir': 'South', 'num': '2, 7', 'season': 'Summer', 'life': 'Seek sunlight, stay warm and connected; suited to media, performance, hospitality, energy — work that shines.'},
        'earth': {'color': 'Yellow, brown, cream', 'dir': 'Centre, north-east, south-west', 'num': '5, 10', 'season': 'Turn of the seasons', 'life': 'Keep a steady routine and stay grounded; suited to property, architecture, agriculture, management — work that holds.'},
        'metal': {'color': 'White, gold, silver', 'dir': 'West', 'num': '4, 9', 'season': 'Autumn', 'life': 'Declutter, keep order and clarity; suited to finance, law, technology, precision craft — work that decides.'},
        'water': {'color': 'Black, blue', 'dir': 'North', 'num': '1, 6', 'season': 'Winter', 'life': 'Be near water and sit in stillness; suited to trade, logistics, travel, consulting — work that flows.'},
    },
}

R['ja'] = {
    'h': '五行の詳しい解読', 's1H': '一 · 日主の強弱', 's2H': '二 · 喜用神', 's3H': '三 · 忌神', 's4H': '四 · 調候と欠ける五行', 's5H': '開運ガイド · 喜用に親しむ',
    'season': {'spring': '春', 'summer': '夏', 'autumn': '秋', 'winter': '冬'},
    'seasonP_same': 'あなたの日主は{stem}（{el}）。{season}に生まれ、{sel}の気が旺じる時——まさに天の時を得ています。',
    'seasonP_gen': 'あなたの日主は{stem}（{el}）。{season}に生まれ、{sel}の気が旺じる時。{sel}は{el}を生み、季節があなたを後押ししています。',
    'seasonP_other': 'あなたの日主は{stem}（{el}）。{season}に生まれ、{sel}の気が旺じる時——日主は時を得ていません。',
    'strongP': '命式のなかであなたを生み支える力——{res}と{same}——はおよそ{pct}%、「{level}」です。盛んな気は満ちあふれる水のよう。せき止めず、導くこと。剋し、洩らし、費やす五行で、余る力を成果へ向けましょう。',
    'weakP': '命式のなかであなたを生み支える力——{res}と{same}——はおよそ{pct}%にとどまり、「{level}」です。弱い気は油の尽きかけた灯のよう。費やさず、足すこと。生み、支える五行で、根の気を補いましょう。',
    'roles': {'res': '「印」——あなたを生み支える力。学び、貴人、庇護の象徴', 'same': '「比劫」——あなたと同じ気。意志、自己、仲間の象徴',
              'out': '「食傷」——あなたから生まれ出るもの。才能、表現、創造の象徴', 'wea': '「財」——あなたが御するもの。財、資源、成果の象徴', 'off': '「官殺」——あなたを律する力。規律、仕事、地位の象徴'},
    'use_wea': '{X}を用神とします。{X}はあなたの{role}。身旺は財を担える——財に力を使うことで、余る気を確かな実りに変えます。',
    'use_off': '{X}を用神とします。{X}はあなたの{role}。強すぎる意志に枠を与え、その鋭さを仕事と名声へ変えます。',
    'use_out': '{X}を用神とします。{X}はあなたの{role}。余る気を才能と創造として流し出す。気がめぐれば、運も通じます。',
    'use_res': '{X}を用神とします。{X}はあなたの{role}。母が子を養うように根の気を補い、外からの圧力もやわらげます。',
    'use_same': '{X}を用神とします。{X}はあなたの{role}。同じ気が肩を並べ、目の前の財と責任を担う力をくれます。',
    'xi_gen': '{Y}を喜神とします。{Y}は{X}を生み、用神を絶えず支えます。',
    'xi_flow': '{Y}を喜神とします。{X}が{Y}を生み、才能が実りへと流れ込みます。',
    'xi_ally': '{Y}を喜神とします。用神と助け合い、ともにあなたを支えます。',
    'ji_strong': '{A}と{B}は忌神です。どちらもすでに満ちた日主をさらに強め、火に薪をくべるようなもの。頑なになり、焦り、心が落ち着かず、努力が実りにくくなります。',
    'ji_weak': '{A}と{B}は忌神です。{A}はあなたの{roleA}、{B}はあなたの{roleB}。身弱のときに剋され、洩らされ、費やされるのは、重荷を背負って遠くへ歩くようなもの。力が足りず、重圧が増し、お金も出入りしがちです。',
    'summer': 'あなたは夏に生まれ、天地の火の気が最も盛んな時。命式は燥熱に傾いています。{tail}', 'summerIn': '水はすでにあなたの喜用。天の時と命式が一致しているので、なおさら近づきましょう。', 'summerOut': '水に適度に親しみ、燥を潤す調候とするとよいでしょう。',
    'winter': 'あなたは冬に生まれ、天地の寒気が深い時。命式は寒湿に傾いています。{tail}', 'winterIn': '火はすでにあなたの喜用。天の時と命式が一致しているので、なおさら近づきましょう。', 'winterOut': '火に適度に親しみ、寒を温める調候とするとよいでしょう。',
    'missing': 'あなたの八字には{list}が欠けています。欠けることは必ずしも悪くありません。それが喜用なら最も補う価値のある五行、忌神なら、欠けていることがむしろ福です。',
    'missingFav': 'このうち{list}はあなたの喜用。積極的に近づきましょう。', 'sep': '・',
    'rows': {'color': 'ラッキーカラー', 'dir': '吉方位', 'num': 'ラッキーナンバー', 'season': '運気の旺じる季節', 'mat': '身につけたい素材', 'life': '暮らしと仕事'},
    'chips': {'yong': '用神', 'xi': '喜神', 'ji': '忌神'},
    'guide': {
        'wood': {'color': '青・緑', 'dir': '東', 'num': '3・8', 'season': '春', 'life': '草木に親しみ、朝に散歩を。教育・文化・デザイン・園芸など、育てる仕事に。'},
        'fire': {'color': '赤・紫・橙', 'dir': '南', 'num': '2・7', 'season': '夏', 'life': '日の光を浴び、情熱と交流を大切に。メディア・表現・飲食・エネルギーなど、照らす仕事に。'},
        'earth': {'color': '黄・茶・生成り', 'dir': '中央・北東・南西', 'num': '5・10', 'season': '季節の変わり目', 'life': '規則正しく、地に足をつけて。不動産・建築・農業・マネジメントなど、支える仕事に。'},
        'metal': {'color': '白・金・銀', 'dir': '西', 'num': '4・9', 'season': '秋', 'life': '手放し、整え、秩序を保って。金融・法律・テクノロジー・精密なものづくりなど、決断する仕事に。'},
        'water': {'color': '黒・青', 'dir': '北', 'num': '1・6', 'season': '冬', 'life': '水辺に親しみ、静かに座る時間を。貿易・物流・旅・コンサルティングなど、流れる仕事に。'},
    },
}

R['ko'] = {
    'h': '오행 상세 풀이', 's1H': '一 · 일주의 강약', 's2H': '二 · 희용신', 's3H': '三 · 기신', 's4H': '四 · 조후와 부족한 오행', 's5H': '개운 가이드 · 희용신을 가까이',
    'season': {'spring': '봄', 'summer': '여름', 'autumn': '가을', 'winter': '겨울'},
    'seasonP_same': '당신의 일주는 {stem} {el}입니다. {season}에 태어나 {sel}의 기운이 왕성한 때——바로 천시를 얻었습니다.',
    'seasonP_gen': '당신의 일주는 {stem} {el}입니다. {season}에 태어나 {sel}의 기운이 왕성한 때, {sel}의 기운이 {el}의 기운을 낳으니 계절이 당신을 돕습니다.',
    'seasonP_other': '당신의 일주는 {stem} {el}입니다. {season}에 태어나 {sel}의 기운이 왕성한 때——일주는 때를 얻지 못했습니다.',
    'strongP': '명식에서 당신을 생하고 돕는 힘({res}·{same})은 약 {pct}%로 「{level}」입니다. 성한 기운은 넘치는 물과 같아 막기보다 이끌어야 합니다. 극하고, 설하고, 소모하는 오행으로 넘치는 힘을 성취로 이끄세요.',
    'weakP': '명식에서 당신을 생하고 돕는 힘({res}·{same})은 약 {pct}%에 그쳐 「{level}」입니다. 약한 기운은 기름이 다해 가는 등불과 같아 소모하기보다 더해야 합니다. 생하고 돕는 오행으로 뿌리의 기운을 채우세요.',
    'roles': {'res': '「인성」——당신을 생하고 돕는 힘, 배움·귀인·보호의 상징', 'same': '「비겁」——당신과 같은 기운, 의지·자아·동료의 상징',
              'out': '「식상」——당신에게서 나오는 것, 재능·표현·창조의 상징', 'wea': '「재성」——당신이 다스리는 것, 재물·자원·성과의 상징', 'off': '「관살」——당신을 다스리는 힘, 규율·일·지위의 상징'},
    'use_wea': '용신: {X}. 이는 당신의 {role}입니다. 신강하면 재물을 감당할 수 있으니, 재물에 힘을 써 넘치는 기운을 확실한 결실로 바꿉니다.',
    'use_off': '용신: {X}. 이는 당신의 {role}입니다. 지나치게 강한 의지에 틀을 주어, 그 날카로움을 일과 명성으로 바꿉니다.',
    'use_out': '용신: {X}. 이는 당신의 {role}입니다. 넘치는 기운을 재능과 창조로 흘려보내니, 기운이 통하면 운도 통합니다.',
    'use_res': '용신: {X}. 이는 당신의 {role}입니다. 어머니가 아이를 기르듯 뿌리의 기운을 채우고, 바깥의 압박도 누그러뜨립니다.',
    'use_same': '용신: {X}. 이는 당신의 {role}입니다. 같은 기운이 어깨를 나란히 하여, 눈앞의 재물과 책임을 감당할 힘을 줍니다.',
    'xi_gen': '희신: {Y}. {Y}의 기운이 {X}의 기운을 낳아 용신을 끊임없이 받쳐 줍니다.',
    'xi_flow': '희신: {Y}. {X}의 기운이 {Y}의 기운을 낳으니, 재능이 결실로 흘러듭니다.',
    'xi_ally': '희신: {Y}. 용신과 서로 도우며 함께 당신을 받쳐 줍니다.',
    'ji_strong': '기신: {A}·{B}. 둘 다 이미 가득 찬 일주를 더 강하게 하니 불에 장작을 더하는 격입니다. 고집스러워지고 조급해지며 마음이 쉬지 못해, 애쓴 만큼 이루기 어렵습니다.',
    'ji_weak': '기신: {A}·{B}. 앞의 것은 당신의 {roleA}, 뒤의 것은 당신의 {roleB}입니다. 신약할 때 극하고 설하고 소모당하면 무거운 짐을 지고 먼 길을 가는 것과 같아, 힘에 부치고 압박이 커지며 재물이 들고 나기 쉽습니다.',
    'summer': '당신은 여름에 태어났고, 천지의 화기가 가장 왕성한 때입니다. 명식이 조열(燥熱)에 기울어 있습니다. {tail}', 'summerIn': '수는 이미 당신의 희용신이니 천시와 명식이 맞아떨어집니다. 더욱 가까이하세요.', 'summerOut': '물을 적당히 가까이하여 메마름을 적시는 조후로 삼으면 좋습니다.',
    'winter': '당신은 겨울에 태어났고, 천지의 한기가 깊은 때입니다. 명식이 한습(寒濕)에 기울어 있습니다. {tail}', 'winterIn': '화는 이미 당신의 희용신이니 천시와 명식이 맞아떨어집니다. 더욱 가까이하세요.', 'winterOut': '불을 적당히 가까이하여 차가움을 데우는 조후로 삼으면 좋습니다.',
    'missing': '당신의 팔자에 없는 오행: {list}. 없다고 꼭 나쁜 것은 아닙니다. 그것이 희용신이라면 가장 채울 가치가 있는 오행이고, 기신이라면 없는 것이 오히려 복입니다.',
    'missingFav': '그중 희용신에 해당하는 것: {list}. 적극적으로 가까이하세요.', 'sep': '·',
    'rows': {'color': '행운의 색', 'dir': '길한 방위', 'num': '행운의 숫자', 'season': '운이 왕성한 계절', 'mat': '지니면 좋은 소재', 'life': '생활과 일'},
    'chips': {'yong': '용신', 'xi': '희신', 'ji': '기신'},
    'guide': {
        'wood': {'color': '청록·초록', 'dir': '동', 'num': '3·8', 'season': '봄', 'life': '초목을 가까이하고 아침에 산책하세요. 교육·문화·디자인·원예 등 기르는 일에.'},
        'fire': {'color': '빨강·보라·주황', 'dir': '남', 'num': '2·7', 'season': '여름', 'life': '햇볕을 쬐고 열정과 교류를 소중히. 미디어·공연·외식·에너지 등 비추는 일에.'},
        'earth': {'color': '노랑·갈색·미색', 'dir': '중앙·북동·남서', 'num': '5·10', 'season': '환절기', 'life': '규칙적으로 생활하고 땅에 발을 디디세요. 부동산·건축·농업·경영 등 받치는 일에.'},
        'metal': {'color': '하양·금색·은색', 'dir': '서', 'num': '4·9', 'season': '가을', 'life': '비우고 정돈하며 질서를 지키세요. 금융·법률·기술·정밀 제조 등 결단하는 일에.'},
        'water': {'color': '검정·파랑', 'dir': '북', 'num': '1·6', 'season': '겨울', 'life': '물가를 가까이하고 고요히 앉는 시간을. 무역·물류·여행·컨설팅 등 흐르는 일에.'},
    },
}


def liquid_json():
    mats = ',"mat":{' + ','.join('"%s":{{ \'v9.el.%s.materials\' | t | json }}' % (k, k) for k in ELS) + '}'
    parts = []
    for loc, key in [('en', 'en'), ('ja', 'ja'), ('ko', 'ko')]:
        parts.append("{%% when '%s' %%}%s" % (loc, json.dumps(R[key], ensure_ascii=False)[:-1] + mats + '}'))
    return ('<script type="application/json" id="v10-el-read">{% case request.locale.iso_code %}' + ''.join(parts)
            + '{% else %}' + json.dumps(R['zh'], ensure_ascii=False)[:-1] + mats + '}{% endcase %}</script>')


JS = r'''
/* v10 reading */
(function(){
  var GEN={wood:'fire',fire:'earth',earth:'metal',metal:'water',water:'wood'}, CTL={wood:'earth',earth:'water',water:'fire',fire:'metal',metal:'wood'};
  var COLOR={wood:'#56634A',fire:'#9E3B2C',earth:'#8C6A43',metal:'#6E6C66',water:'#2F3B45'}, CH={wood:'木',fire:'火',earth:'土',metal:'金',water:'水'};
  var SEASON={'寅':'spring','卯':'spring','辰':'spring','巳':'summer','午':'summer','未':'summer','申':'autumn','酉':'autumn','戌':'autumn','亥':'winter','子':'winter','丑':'winter'};
  var SEL={spring:'wood',summer:'fire',autumn:'metal',winter:'water'};
  function f(s,o){return String(s).replace(/\{(\w+)\}/g,function(m,k){return o[k]!==undefined?o[k]:m;});}
  function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  window.v10Fav=function(r){
    var dm=r.dayEl,res,off,out=GEN[dm],wea=CTL[dm],s=r.score;
    for(var e in GEN){if(GEN[e]===dm)res=e;if(CTL[e]===dm)off=e;}
    var strong=r.ratio>=50,yong,xi,yk,xk,ji;
    if(strong){
      if(s[res]>s[dm]){yong=wea;yk='wea';xi=out;xk='xi_gen';}
      else if(s[off]>=s[out]){yong=off;yk='off';xi=wea;xk='xi_gen';}
      else{yong=out;yk='out';xi=wea;xk='xi_flow';}
      ji=[res,dm].sort(function(a,b){return s[b]-s[a];});
    }else{
      var en=[off,out,wea].sort(function(a,b){return s[b]-s[a];});
      if(en[0]===wea){yong=dm;yk='same';xi=res;xk='xi_gen';}else{yong=res;yk='res';xi=dm;xk='xi_ally';}
      ji=en.slice(0,2);
    }
    var role={}; role[res]='res';role[dm]='same';role[out]='out';role[wea]='wea';role[off]='off';
    r.favorable=[yong,xi];
    r.v10={strong:strong,yong:yong,yk:yk,xi:xi,xk:xk,ji:ji,role:role,res:res};
  };
  window.v10Reading=function(r,T){
    var node=document.getElementById('v10-el-read'); if(!node||!r.v10)return '';
    var L=JSON.parse(node.textContent), v=r.v10, N=function(k){return T.el[k];};
    var mb=r.pillars[1].branch, season=SEASON[mb], sel=SEL[season], dm=r.dayEl;
    var sp=sel===dm?'seasonP_same':(GEN[sel]===dm?'seasonP_gen':'seasonP_other');
    var p1=f(L[sp],{stem:r.dayStem,el:N(dm),season:L.season[season],sel:N(sel)})+' '+f(L[v.strong?'strongP':'weakP'],{res:N(v.res),same:N(dm),pct:r.ratio,level:T.levels[r.level]});
    var p2a=f(L['use_'+v.yk],{X:N(v.yong),role:L.roles[v.yk]});
    var p2b=f(L[v.xk],{X:N(v.yong),Y:N(v.xi)});
    var p3=v.strong?f(L.ji_strong,{A:N(v.ji[0]),B:N(v.ji[1])}):f(L.ji_weak,{A:N(v.ji[0]),B:N(v.ji[1]),roleA:L.roles[v.role[v.ji[0]]],roleB:L.roles[v.role[v.ji[1]]]});
    var fav=[v.yong,v.xi], notes=[];
    if(season==='summer')notes.push(f(L.summer,{tail:fav.indexOf('water')>-1?L.summerIn:L.summerOut}));
    if(season==='winter')notes.push(f(L.winter,{tail:fav.indexOf('fire')>-1?L.winterIn:L.winterOut}));
    var miss=['wood','fire','earth','metal','water'].filter(function(k){return r.pct[k]===0;});
    if(miss.length){var mf=miss.filter(function(k){return fav.indexOf(k)>-1;});
      notes.push(f(L.missing,{list:miss.map(N).join(L.sep)})+(mf.length?' '+f(L.missingFav,{list:mf.map(N).join(L.sep)}):''));}
    function chip(k,lab,solid){var c=COLOR[k];return '<span class="v10-rchip" style="border-color:'+c+';background:'+(solid?c:'transparent')+';color:'+(solid?'#FBFAF7':c)+'"><b>'+CH[k]+'</b>'+(N(k)===CH[k]?'':esc(N(k)))+'<i>'+esc(lab)+'</i></span>';}
    var h='<div class="v10-read" style="grid-column:1/-1"><h3 class="v9-h3 v10-read-h">'+esc(L.h)+'</h3>';
    h+='<div class="v10-read-sec"><p class="v9-label">'+esc(L.s1H)+'</p><p class="v10-read-p">'+esc(p1)+'</p></div>';
    h+='<div class="v10-read-sec"><p class="v9-label">'+esc(L.s2H)+'</p><div class="v10-rchips">'+chip(v.yong,L.chips.yong,true)+chip(v.xi,L.chips.xi,false)+'</div><p class="v10-read-p">'+esc(p2a)+'</p><p class="v10-read-p">'+esc(p2b)+'</p></div>';
    h+='<div class="v10-read-sec"><p class="v9-label">'+esc(L.s3H)+'</p><div class="v10-rchips">'+chip(v.ji[0],L.chips.ji,false)+chip(v.ji[1],L.chips.ji,false)+'</div><p class="v10-read-p">'+esc(p3)+'</p></div>';
    if(notes.length)h+='<div class="v10-read-sec"><p class="v9-label">'+esc(L.s4H)+'</p>'+notes.map(function(n){return '<p class="v10-read-p">'+esc(n)+'</p>';}).join('')+'</div>';
    h+='<div class="v10-read-sec"><p class="v9-label">'+esc(L.s5H)+'</p><div class="v10-guide">';
    fav.forEach(function(k,i){var g=L.guide[k],c=COLOR[k];
      h+='<div class="v10-gcard" style="border-top-color:'+c+'"><p class="v10-gh"><span style="background:'+c+'">'+CH[k]+'</span>'+(N(k)===CH[k]?'':esc(N(k))+' · ')+esc(i?L.chips.xi:L.chips.yong)+'</p><dl>';
      [['color',g.color],['dir',g.dir],['num',g.num],['season',g.season],['mat',L.mat[k]],['life',g.life]].forEach(function(row){h+='<div><dt>'+esc(L.rows[row[0]])+'</dt><dd>'+esc(row[1])+'</dd></div>';});
      h+='</dl></div>';});
    h+='</div></div></div>';
    return h;
  };
})();
'''

CSS = '''
.v10-read{margin-top:8px;padding-top:40px;border-top:1px solid var(--v9-line)}
.v10-read-h{margin:0 0 28px;font-size:clamp(26px,3vw,34px)}
.v10-read-sec{margin:0 0 34px;max-width:860px}.v10-read-sec .v9-label{margin:0 0 12px}
.v10-read-p{margin:0 0 12px;font-family:var(--v9-serif);font-size:18px;line-height:1.85;color:var(--v9-ink)}
.v10-rchips{display:flex;flex-wrap:wrap;gap:10px;margin:0 0 16px}
.v10-rchip{display:inline-flex;align-items:center;gap:8px;border:1px solid;border-radius:999px;padding:6px 16px 6px 6px;font-size:14px}
.v10-rchip b{display:inline-flex;width:28px;height:28px;border-radius:50%;align-items:center;justify-content:center;font-family:var(--v9-cjk);font-weight:400;background:rgba(255,255,255,.18)}
.v10-rchip i{font-style:normal;font-size:12px;opacity:.85;letter-spacing:.06em}
.v10-guide{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(320px,100%),1fr));gap:20px}
.v10-gcard{background:var(--v9-paper);border:1px solid var(--v9-line);border-top:3px solid;padding:22px 24px}
.v10-gh{display:flex;align-items:center;gap:10px;margin:0 0 14px;font-family:var(--v9-serif);font-size:20px}
.v10-gh span{display:inline-flex;width:32px;height:32px;border-radius:50%;color:#FBFAF7;align-items:center;justify-content:center;font-family:var(--v9-cjk);font-size:15px}
.v10-gcard dl{margin:0}.v10-gcard dl div{display:grid;grid-template-columns:96px 1fr;gap:12px;padding:9px 0;border-top:1px solid var(--v9-line);font-size:14px;line-height:1.65}
.v10-gcard dt{color:var(--v9-muted)}.v10-gcard dd{margin:0;color:var(--v9-ink)}
'''
