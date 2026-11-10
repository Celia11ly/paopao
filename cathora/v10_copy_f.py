# -*- coding: utf-8 -*-
"""v10.6: Five Elements as metaphysics/energy, no product references. (zh, en, ja, ko)"""

BRAND_F = {
    'qiH': ('你的五行，藏着你的运。', 'Your elements hold your fortune.', 'あなたの五行に、あなたの運が宿る。', '당신의 오행에, 당신의 운이 깃들어 있습니다.'),
    'qiQuote': ('「玄之又玄，众妙之门。」——老子', '"Mystery upon mystery — the gateway to all wonders." — Laozi', '「玄の又た玄、衆妙の門。」——老子', '「현묘하고 또 현묘하니, 모든 오묘함의 문이다.」——노자'),
    'qi1': ('「玄」字，本义是深远。中国人所说的玄学，从来不是迷信，而是对看不见之物的追问：气从哪里来，运往哪里去，人与天地之间，系着怎样一根看不见的线。老子说「玄之又玄，众妙之门」——在看得见的世界之下，还有一个看不见的世界，在静静地运转。玄学，即是哲学。',
            'The Chinese word xuan means deep, dark, far. What the Chinese call xuanxue — the study of the mysterious — was never superstition. It is a question about the things we cannot see: where breath comes from, where fortune goes, and what invisible thread runs between a person and heaven and earth. Laozi called it "mystery upon mystery, the gateway to all wonders": beneath the visible world, another world turns quietly. The mysterious, in the end, is philosophy.',
            '「玄」という字は、もともと深く遠いことを意味します。中国でいう玄学は、迷信ではありません。見えないものへの問いかけです——気はどこから来て、運はどこへ行くのか。人と天地のあいだに、どんな見えない糸があるのか。老子はそれを「玄の又た玄、衆妙の門」と呼びました。目に見える世界の下に、もうひとつの見えない世界が静かにめぐっている。玄学とは、哲学なのです。',
            '「현(玄)」이라는 글자는 본디 깊고 아득하다는 뜻입니다. 중국에서 말하는 현학은 미신이 아니라, 보이지 않는 것에 대한 물음입니다——기는 어디서 오고 운은 어디로 가는가, 사람과 천지 사이에는 어떤 보이지 않는 실이 있는가. 노자는 이를 「현묘하고 또 현묘하니, 모든 오묘함의 문」이라 했습니다. 보이는 세계 아래에서 또 하나의 보이지 않는 세계가 조용히 돌고 있습니다. 현학은 곧 철학입니다.'),
    'qi2': ('古人把这股流动的能量，叫作「气」；把气的五种状态，叫作五行——水的智慧与柔韧，木的生发，火的光明，土的承载，金的清明与守护。天地之间，五气流转，生生不息；你的身体里，也有同样的五气，随日月四时起落。',
            'The ancients called this moving energy qi, and its five states the Five Elements: the wisdom and softness of water, the growth of wood, the brightness of fire, the steadiness of earth, the clarity and protection of metal. Between heaven and earth the five energies turn without end — and within your body the same five move too, rising and falling with the sun, the moon and the seasons.',
            '古の人々は、この流れるエネルギーを「気」と呼び、その五つのありようを五行と呼びました。水の智慧としなやかさ、木の伸びゆく力、火の明るさ、土の支える力、金の澄んだ守り。天地のあいだを五つの気が絶えずめぐり、あなたの身体のなかでも同じ五つの気が、日月と四季とともに満ち引きしています。',
            '옛사람들은 이 흐르는 에너지를 「기」라 부르고, 기의 다섯 가지 상태를 오행이라 불렀습니다. 물의 지혜와 유연함, 나무의 뻗어 나가는 힘, 불의 밝음, 흙의 떠받침, 쇠의 맑은 수호. 천지 사이에서 다섯 기운이 끝없이 돌고, 당신의 몸 안에서도 같은 다섯 기운이 해와 달과 사계절을 따라 차고 기웁니다.'),
    'qi3': ('你出生的那一刻，天地之气正以某种方式排列——年、月、日、时，各落两字，合为「八字」。这便是你与生俱来的五行。有的人火旺，热烈却易燥；有的人水多，聪慧却多思；有的人缺木，做什么总差一口向上的力气。五行平衡，则身安、心定、运顺；一行过旺或不足，便容易在某处卡住——事业停滞，财来财去，心神不宁。',
            'At the moment you were born, the energies of heaven and earth stood in a particular arrangement. Year, month, day and hour each leave a pair of characters — eight in all, your bazi. This is the elemental pattern you were born with. Some people burn with fire: warm, but quick to dry out. Some are full of water: clever, but given to overthinking. Some lack wood, and always seem one push short of rising. When the five are in balance, the body is at ease, the heart is settled, and things go smoothly. When one is too strong or too weak, life tends to stick somewhere — work stalls, money comes and goes, the mind won\'t rest.',
            'あなたが生まれたその瞬間、天地の気はある形に並んでいました。年・月・日・時がそれぞれ二字を残し、合わせて「八字」。これが生まれ持った五行です。火の強い人は熱く、けれど乾きやすい。水の多い人は聡く、けれど考えこみやすい。木の足りない人は、いつもあと一押しの力が出ない。五行が釣り合えば、身は安らぎ、心は定まり、運は順調に。どれかが強すぎたり弱すぎたりすると、どこかで滞りやすくなる——仕事が止まり、お金が出ていき、心が落ち着かない。',
            '당신이 태어난 그 순간, 천지의 기운은 어떤 모양으로 놓여 있었습니다. 해·달·날·시가 저마다 두 글자를 남기니, 합쳐 「팔자」. 이것이 타고난 오행입니다. 화가 강한 사람은 뜨겁지만 쉽게 메마르고, 수가 많은 사람은 총명하지만 생각이 많습니다. 목이 부족한 사람은 늘 한 걸음 내딛을 힘이 모자랍니다. 오행이 고르면 몸이 편하고 마음이 안정되며 운이 순조롭습니다. 어느 하나가 지나치거나 모자라면 어딘가에서 막히기 쉽습니다——일이 멈추고, 재물이 새고, 마음이 쉬지 못합니다.'),
    'qi4': ('古人的智慧很简单：缺什么，就去亲近什么。缺水的人宜近水，缺木的人宜见青，缺金的人宜佩银。天然的石、木与银，各自承载着某一种五行之气。把对的那一件戴在身上，日日贴着肌肤，就像在身边放了一个小小的气场——它不替你改命，却在一呼一吸之间，帮你把气调匀。',
            'The ancients\' answer was simple: draw close to what you lack. Those short of water should live near water; those short of wood should keep green around them; those short of metal should wear silver. Natural stone, wood and silver each carry the energy of one element. Wear the right one against your skin, day after day, and it is like keeping a small field of energy beside you. It does not rewrite your fate — but breath by breath, it helps bring your qi back into balance.',
            '古の知恵は簡潔です。足りないものに近づくこと。水の足りない人は水辺に、木の足りない人は緑のそばに、金の足りない人は銀を身に。天然の石、木、銀は、それぞれひとつの五行の気を宿しています。ふさわしい一点を肌に添わせ、毎日身につければ、そばに小さな気の場を置くようなもの。運命を書き換えはしなくても、ひと呼吸ごとに、気を整える手助けをしてくれます。',
            '옛사람의 지혜는 간단합니다. 부족한 것을 가까이하라. 수가 부족하면 물가를, 목이 부족하면 초록을, 금이 부족하면 은을 가까이하라. 천연의 돌과 나무와 은은 저마다 한 오행의 기운을 품고 있습니다. 맞는 하나를 피부에 닿게 날마다 지니면, 곁에 작은 기의 장을 두는 것과 같습니다. 운명을 다시 쓰지는 않지만, 숨 한 번 한 번마다 기운을 고르게 해 줍니다.'),
    'qi5': ('所以，先认识你自己的五行吧。知道自己从哪里来，缺的是什么，该往何处补——这是一切好运的起点。心定，气顺，运自然会来。',
            'So begin by knowing your own elements. Where you come from, what you lack, and where to replenish it — that is where all good fortune starts. When the heart is settled and the qi flows, luck comes of its own accord.',
            'だからまず、自分の五行を知ることから。どこから来て、何が足りず、どこで補えばいいのか——それがすべての幸運の始まりです。心が定まり、気がめぐれば、運は自ずとやってきます。',
            '그러니 먼저 자신의 오행을 알아보세요. 어디서 왔고, 무엇이 부족하며, 어디서 채워야 하는지——그것이 모든 행운의 시작입니다. 마음이 고요하고 기운이 흐르면, 운은 저절로 찾아옵니다.'),
    'elCardsH': ('你缺的，是哪一行？', 'Which element are you missing?', 'あなたに足りないのは、どの五行？', '당신에게 부족한 것은 어느 오행인가요?'),
}

# element: (keywords, line, favours)
EL_CARD = {
    'water': (('智慧 · 流动 · 财源', '水主智，亦主财。水旺的人聪慧通达；缺水，则思虑易滞，财来难留。', '宜：黑、蓝 · 北方 · 冬'),
              ('Wisdom · Flow · Wealth', 'Water governs wisdom, and wealth. Those rich in water are quick and perceptive; those who lack it find their thoughts get stuck, and money slips away.', 'Favours: black & blue · north · winter'),
              ('智慧 · 流れ · 財', '水は智をつかさどり、財をもつかさどる。水の多い人は聡く通じ、足りない人は考えが滞り、お金も留まりにくい。', '相性：黒・青 · 北 · 冬'),
              ('지혜 · 흐름 · 재물', '물은 지혜를, 또 재물을 다스립니다. 수가 많은 사람은 총명하고 막힘이 없으며, 부족한 사람은 생각이 막히고 재물이 머물지 않습니다.', '맞는 것: 검정·파랑 · 북 · 겨울')),
    'wood': (('生发 · 成长 · 事业', '木主仁，主生长。木旺的人有冲劲、有远见；缺木，则做事难以起势，总差一口气。', '宜：青、绿 · 东方 · 春'),
             ('Growth · Rising · Career', 'Wood governs kindness and growth. Those rich in wood have drive and vision; those who lack it struggle to get things moving, always one breath short.', 'Favours: green · east · spring'),
             ('生長 · 伸展 · 仕事', '木は仁をつかさどり、成長をつかさどる。木の多い人は勢いと先見を持ち、足りない人は物事が動き出さず、いつもあと一息足りない。', '相性：青・緑 · 東 · 春'),
             ('생장 · 뻗음 · 사업', '나무는 인(仁)과 성장을 다스립니다. 목이 많은 사람은 추진력과 안목이 있고, 부족한 사람은 일이 좀처럼 시작되지 않아 늘 한 숨이 모자랍니다.', '맞는 것: 초록 · 동 · 봄')),
    'fire': (('光明 · 热情 · 名望', '火主礼，主光明。火旺的人热烈、有感染力；缺火，则容易消沉，少了被看见的机会。', '宜：红、紫 · 南方 · 夏'),
             ('Light · Warmth · Recognition', 'Fire governs courtesy and light. Those rich in fire are warm and magnetic; those who lack it sink easily into low spirits, and miss their chance to be seen.', 'Favours: red & purple · south · summer'),
             ('光 · 情熱 · 名声', '火は礼をつかさどり、光をつかさどる。火の多い人は熱く人を惹きつけ、足りない人は沈みがちで、人に見出される機会を逃しやすい。', '相性：赤・紫 · 南 · 夏'),
             ('빛 · 열정 · 명성', '불은 예(禮)와 밝음을 다스립니다. 화가 많은 사람은 뜨겁고 사람을 끌며, 부족한 사람은 쉽게 가라앉아 드러날 기회를 놓칩니다.', '맞는 것: 빨강·보라 · 남 · 여름')),
    'earth': (('承载 · 安稳 · 守成', '土主信，主厚重。土旺的人踏实可靠；缺土，则根基不稳，心中常感漂泊。', '宜：黄、棕 · 中央 · 四季之交'),
              ('Grounding · Stability · Keeping', 'Earth governs trust and substance. Those rich in earth are steady and reliable; those who lack it feel unrooted, as if always drifting.', 'Favours: yellow & brown · centre · turn of seasons'),
              ('支え · 安定 · 守り', '土は信をつかさどり、重みをつかさどる。土の多い人は堅実で頼もしく、足りない人は根が定まらず、いつも漂うような心地になる。', '相性：黄・茶 · 中央 · 季節の変わり目'),
              ('떠받침 · 안정 · 지킴', '흙은 신(信)과 무게를 다스립니다. 토가 많은 사람은 듬직하고 믿음직하며, 부족한 사람은 뿌리가 흔들려 늘 떠도는 듯합니다.', '맞는 것: 노랑·갈색 · 중앙 · 환절기')),
    'metal': (('决断 · 守护 · 贵人', '金主义，主收敛与守护。金旺的人果断清明；缺金，则易犹豫不决，也易招惹是非。', '宜：白、银 · 西方 · 秋'),
              ('Resolve · Protection · Helpful people', 'Metal governs righteousness, gathering and guarding. Those rich in metal are decisive and clear; those who lack it hesitate, and draw trouble more easily.', 'Favours: white & silver · west · autumn'),
              ('決断 · 守護 · 貴人', '金は義をつかさどり、収めて守ることをつかさどる。金の多い人は決断が早く明晰で、足りない人は迷いやすく、もめごとも招きやすい。', '相性：白・銀 · 西 · 秋'),
              ('결단 · 수호 · 귀인', '쇠는 의(義)와 거두어 지킴을 다스립니다. 금이 많은 사람은 결단이 빠르고 맑으며, 부족한 사람은 망설이기 쉽고 시비를 부르기 쉽습니다.', '맞는 것: 하양·은색 · 서 · 가을')),
}
for _k, _v in EL_CARD.items():
    BRAND_F['el_%s_m' % _k] = tuple(x[0] for x in _v)
    BRAND_F['el_%s_p' % _k] = tuple(x[1] for x in _v)
    BRAND_F['el_%s_a' % _k] = tuple(x[2] for x in _v)
