# -*- coding: utf-8 -*-
"""v10.5: traditional decorative glyphs, deeper Five Elements + founder. (zh, en, ja, ko)"""

# decorative glyphs only (body text stays simplified for zh-CN)
BLESS_TC = {'health': '康', 'career': '業', 'wealth': '財', 'love': '緣', 'peace': '安', 'retrograde': '轉'}
LAND_TC = {'putuo': '普陀', 'lingyin': '靈隱', 'jingshan': '徑山', 'tiantai': '天台', 'emei': '峨眉',
           'longmen': '龍門', 'white-horse': '白馬', 'wudang': '武當'}

BRAND_E = {
    'qiH': ('五行，是天地的呼吸。', 'The Five Elements: the breathing of heaven and earth.', '五行は、天地の呼吸。', '오행, 천지의 호흡.'),
    'qiQuote': ('「天有五行，水火金木土，分时化育，以成万物。」——《孔子家语》',
                '"Heaven has five phases — water, fire, metal, wood, earth. Each in its season nurtures and transforms, and so all things are made." — Kongzi Jiayu',
                '「天に五行あり、水火金木土、時を分かちて化育し、以て万物を成す。」——『孔子家語』',
                '「하늘에 오행이 있으니 수·화·금·목·토라. 때를 나누어 기르고 변화시켜 만물을 이룬다.」——『공자가어』'),
    'qi1': ('五行，不是五种物质，而是五种「行」——五种运动的方式。三千年前的《尚书·洪范》写道：水曰润下，火曰炎上，木曰曲直，金曰从革，土爰稼穑。水向下滋润，火向上升腾，木屈伸生长，金顺从而变革，土承载、孕育万物。古人看的不是东西本身，而是东西在怎样变化。',
            'The Five Elements are not five substances but five xing — five ways of moving. Three thousand years ago, the Book of Documents put it like this: water soaks downward; fire flares upward; wood bends and straightens; metal yields and is reshaped; earth receives the seed and gives the harvest. The ancients were not looking at things themselves, but at how things change.',
            '五行とは五つの物質ではなく、五つの「行」——五つの動き方のことです。三千年前の『書経』洪範篇はこう記します。水は潤下し、火は炎上し、木は曲直し、金は従革し、土は稼穡す。水は下へ潤し、火は上へ燃え、木は曲がりまた伸び、金は従いながら形を変え、土は種を受けて実りを返す。古の人が見ていたのは、ものそのものではなく、ものがどう変わるか、でした。',
            '오행은 다섯 가지 물질이 아니라 다섯 가지 「행(行)」——다섯 가지 움직임의 방식입니다. 삼천 년 전 『서경』 홍범편은 이렇게 적었습니다. 물은 아래로 적시고, 불은 위로 타오르며, 나무는 굽었다 곧게 자라고, 쇠는 따르며 모양을 바꾸고, 흙은 씨를 받아 결실을 돌려준다. 옛사람들이 본 것은 사물 그 자체가 아니라, 사물이 어떻게 변하는가였습니다.'),
    'qi2': ('五行之间，相生，也相克。木生火，火生土，土生金，金生水，水生木；木克土，土克水，水克火，火克金，金克木。生是成全，克是节制。只生不克，万物会疯长而失序；只克不生，万物会枯竭而凋零。天地之所以长久，是因为每一种力量，都既被成全，也被约束。这便是「和」——不是没有冲突，而是冲突之中，自有分寸。',
            'Between the five, there is giving rise and there is holding back. Wood feeds fire, fire makes earth, earth bears metal, metal carries water, water nourishes wood. And wood parts earth, earth dams water, water quenches fire, fire melts metal, metal cuts wood. Giving rise is generosity; holding back is restraint. With only generosity, things would grow wild and lose their order; with only restraint, they would wither. Heaven and earth endure because every force is both supported and contained. This is what the Chinese call he, harmony — not the absence of conflict, but a sense of measure within it.',
            '五行のあいだには、相生があり、相剋があります。木は火を生み、火は土を生み、土は金を生み、金は水を生み、水は木を生む。木は土を剋し、土は水を剋し、水は火を剋し、火は金を剋し、金は木を剋す。生むことは成就させること、剋することは節度を与えること。生むだけなら万物は野放図に茂って秩序を失い、剋すだけなら枯れてしまう。天地が長く続くのは、どの力もが支えられ、同時に抑えられているから。これが「和」です——争いがないことではなく、争いのなかに、ほどよい分があること。',
            '오행 사이에는 상생이 있고 상극이 있습니다. 목은 화를, 화는 토를, 토는 금을, 금은 수를, 수는 목을 낳습니다. 목은 토를, 토는 수를, 수는 화를, 화는 금을, 금은 목을 누릅니다. 낳음은 이루어 줌이고, 누름은 절제입니다. 낳기만 하면 만물은 제멋대로 자라 질서를 잃고, 누르기만 하면 말라 버립니다. 천지가 오래가는 것은 모든 힘이 북돋워지는 동시에 다스려지기 때문입니다. 이것이 「화(和)」——다툼이 없는 것이 아니라, 다툼 속에 절도가 있는 것입니다.'),
    'qi3': ('古人相信「天人合一」：人身是一个小天地。肝属木，心属火，脾属土，肺属金，肾属水；春夏秋冬与长夏，东南西北与中央，也各有所属。天地之气流转，人的气也随之起落。所谓「运」，不过是你与天地节律之间的关系——顺时则通，逆时则滞。《黄帝内经》说：「春夏养阳，秋冬养阴。」顺应，本身就是一种修行。',
            'The ancients believed heaven and humankind are one: the body is a small heaven and earth. Liver is wood, heart is fire, spleen is earth, lungs are metal, kidneys are water; the seasons and the directions each belong to an element too. As the breath of the world turns, a person\'s breath rises and falls with it. What we call fortune is only the relationship between you and the rhythm of the world — move with the season and things flow; move against it and they stall. The Yellow Emperor\'s Classic advises: in spring and summer, nourish yang; in autumn and winter, nourish yin. To move in step is itself a practice.',
            '古の人々は「天人合一」を信じていました。人の身は小さな天地。肝は木、心は火、脾は土、肺は金、腎は水。四季と土用、東西南北と中央にも、それぞれの五行がある。天地の気がめぐれば、人の気もそれにつれて上下する。「運」とは、あなたと天地のリズムとの関係にすぎません——時に順えば通じ、時に逆らえば滞る。『黄帝内経』は言います。「春夏は陽を養い、秋冬は陰を養う。」順うこと、それ自体がひとつの修行なのです。',
            '옛사람들은 「천인합일」을 믿었습니다. 사람의 몸은 작은 천지입니다. 간은 목, 심장은 화, 비장은 토, 폐는 금, 신장은 수. 사계절과 늦여름, 동서남북과 중앙도 저마다 오행에 속합니다. 천지의 기가 돌면 사람의 기도 따라 오르내립니다. 「운」이란 결국 당신과 천지의 리듬 사이의 관계——때를 따르면 통하고, 거스르면 막힙니다. 『황제내경』은 말합니다. 「봄여름에는 양을 기르고, 가을겨울에는 음을 기른다.」 따르는 것, 그 자체가 하나의 수행입니다.'),
    'qi4': ('一个人出生的年、月、日、时，各对应一组天干地支，合称「八字」。八字之中，五行有多有少，有旺有弱。古人并不说这是命定，而说这是禀赋——你天生带着的那一份气。旺者宜泄，弱者宜扶。所谓调和，不是改命，而是知命：知道自己从哪里来，缺什么，又该往哪里去。',
            'The year, month, day and hour of a person\'s birth each correspond to a pair of heavenly stems and earthly branches — eight characters in all, the bazi. Among those eight, some elements are abundant and some are scarce. The ancients did not call this fate. They called it endowment: the particular breath you were born carrying. What is too strong may be eased; what is weak may be supported. Balance is not about changing your destiny. It is about knowing it — where you come from, what you lack, and where you are going.',
            '生まれた年・月・日・時には、それぞれ天干と地支の組み合わせがあり、合わせて「八字」と呼びます。八字のなかで、五行には多い少ない、強い弱いがある。古の人はこれを運命とは言わず、稟賦と呼びました——生まれながらに携えてきた、あなただけの気。強すぎるものは和らげ、弱いものは支える。調和とは命を変えることではなく、命を知ること。どこから来て、何が足りず、どこへ向かうのかを知ることです。',
            '사람이 태어난 해·달·날·시에는 각각 천간과 지지의 짝이 있고, 이를 합쳐 「팔자」라 합니다. 팔자 속 오행에는 많고 적음, 강하고 약함이 있습니다. 옛사람들은 이를 운명이라 하지 않고 품부(稟賦)라 했습니다——타고날 때 지니고 온 당신만의 기운. 지나친 것은 덜어 내고, 약한 것은 북돋웁니다. 조화란 운명을 바꾸는 것이 아니라 운명을 아는 것. 어디서 왔고, 무엇이 부족하며, 어디로 가야 하는지를 아는 일입니다.'),
    'qi5': ('所以，我们以五行为每件作品选材、定名：朝光的太阳石属火，一息的木珠属木，静潮的玉髓属水，银雪山属金，留形以山为形，属土。你可以从自己的五行出发，找一件补你所缺；也可以只是选一件，让你心安的。好运不是被抓住的，而是被迎来的：心定，气顺，它自然会来。',
            'So we choose each piece\'s material and name by its element: the sunstone of First Light is fire, the wood of Daily Pause is wood, the chalcedony of Still Tide is water, Snow Summit is metal, and Enduring Form, shaped as a mountain, is earth. You can start from your own elements and find the piece that supplies what you lack — or simply choose the one that settles your heart. Good fortune is not seized; it is welcomed. When the heart is settled and the breath is even, it comes of its own accord.',
            'だから私たちは、五行にもとづいて作品の素材と名前を決めています。朝光のサンストーンは火、一息の木珠は木、静潮のカルセドニーは水、銀雪山は金、山をかたどった留形は土。あなた自身の五行から、足りないものを補う一点を探すこともできるし、ただ心が落ち着く一点を選んでもいい。幸運はつかむものではなく、迎えるもの。心が定まり、気が整えば、自ずとやってきます。',
            '그래서 저희는 오행에 따라 작품의 소재와 이름을 정합니다. 아침빛의 선스톤은 화, 한숨의 나무 구슬은 목, 고요한 물결의 칼세도니는 수, 은설산은 금, 산을 본뜬 머문 형상은 토. 당신의 오행에서 출발해 부족한 것을 채우는 작품을 찾을 수도 있고, 그저 마음이 편안해지는 하나를 골라도 좋습니다. 행운은 붙잡는 것이 아니라 맞이하는 것. 마음이 고요하고 기운이 고르면 저절로 찾아옵니다.'),
    'elCardsH': ('五行，各有其德', 'Each element, its own virtue', '五行、それぞれの徳', '오행, 저마다의 덕'),
}

# element: (motion, season · direction · organ · virtue, line)
EL_CARD = {
    'water': (('润下', '冬 · 北 · 肾 · 智', '水善利万物而不争。它教人柔软，也教人坚持——最柔的，能穿透最坚硬的。'),
              ('Soaks downward', 'Winter · North · Kidneys · Wisdom', 'Water benefits all things and does not contend. It teaches softness, and persistence — the softest thing can wear through the hardest.'),
              ('潤下', '冬 · 北 · 腎 · 智', '水は万物を利して争わない。やわらかさと、粘り強さを教える——もっともやわらかいものが、もっとも硬いものを穿つ。'),
              ('윤하(潤下)', '겨울 · 북 · 신장 · 지(智)', '물은 만물을 이롭게 하되 다투지 않습니다. 부드러움과 끈기를 가르칩니다——가장 부드러운 것이 가장 단단한 것을 뚫습니다.')),
    'wood': (('曲直', '春 · 东 · 肝 · 仁', '木向上生长，也向下扎根。枝叶伸得多高，根就要扎得多深。'),
             ('Bends and straightens', 'Spring · East · Liver · Benevolence', 'Wood grows upward and roots downward. However high the branches reach, the roots must go as deep.'),
             ('曲直', '春 · 東 · 肝 · 仁', '木は上へ伸び、下へ根を張る。枝葉が高く伸びるほど、根も深くなければならない。'),
             ('곡직(曲直)', '봄 · 동 · 간 · 인(仁)', '나무는 위로 자라고 아래로 뿌리내립니다. 가지가 높이 뻗는 만큼 뿌리도 깊어야 합니다.')),
    'fire': (('炎上', '夏 · 南 · 心 · 礼', '火给人光与温度。它教人热烈，也教人懂得：一盏灯点亮另一盏，自己并不会少一分光。'),
             ('Flares upward', 'Summer · South · Heart · Propriety', 'Fire gives light and warmth. It teaches passion, and this: when one lamp lights another, it loses none of its own light.'),
             ('炎上', '夏 · 南 · 心 · 礼', '火は光とぬくもりを与える。情熱と、そしてこのことを教える——一つの灯がもう一つの灯をともしても、自らの光は少しも減らない。'),
             ('염상(炎上)', '여름 · 남 · 심장 · 예(禮)', '불은 빛과 온기를 줍니다. 열정과 함께 이것을 가르칩니다——등불 하나가 다른 등불을 밝혀도 제 빛은 조금도 줄지 않는다는 것.')),
    'earth': (('稼穑', '长夏 · 中 · 脾 · 信', '土承载一切，默然不语。四季轮转，它始终在那里——厚德载物。'),
              ('Sows and reaps', 'Late summer · Centre · Spleen · Trust', 'Earth carries everything and says nothing. Seasons turn; it is always there. Great virtue bears all things.'),
              ('稼穡', '土用 · 中央 · 脾 · 信', '土はすべてを載せ、黙して語らない。四季がめぐっても、いつもそこにある——厚徳、物を載す。'),
              ('가색(稼穡)', '늦여름 · 중앙 · 비장 · 신(信)', '흙은 모든 것을 싣고 말이 없습니다. 사계절이 돌아도 늘 그 자리에——두터운 덕이 만물을 싣습니다.')),
    'metal': (('从革', '秋 · 西 · 肺 · 义', '金经千锤百炼而成器。它教人果断，也教人取舍——秋天落叶，是为了来年的春。'),
              ('Yields and is reshaped', 'Autumn · West · Lungs · Righteousness', 'Metal becomes a vessel only through a thousand blows of the hammer. It teaches resolve, and letting go — autumn drops its leaves for the sake of spring.'),
              ('従革', '秋 · 西 · 肺 · 義', '金は千回の鍛錬を経て器となる。決断と、手放すことを教える——秋に葉を落とすのは、来る春のため。'),
              ('종혁(從革)', '가을 · 서 · 폐 · 의(義)', '쇠는 천 번의 담금질을 거쳐 그릇이 됩니다. 결단과 내려놓음을 가르칩니다——가을이 잎을 떨구는 것은 다가올 봄을 위해서입니다.')),
}
for _k, _v in EL_CARD.items():
    BRAND_E['el_%s_m' % _k] = tuple(x[0] for x in _v)
    BRAND_E['el_%s_a' % _k] = tuple(x[1] for x in _v)
    BRAND_E['el_%s_p' % _k] = tuple(x[2] for x in _v)

FOUNDER_E = {
    'f4': ('外婆走的那年冬天，我一个人回到那座山。石阶还是那些石阶，只是身边没有了人。我在大殿前站了很久，不知道该求什么。一位扫地的老师父走过来，问我：「来求什么？」我说，不知道。他点点头：「不知道，也好。」',
           'The winter my grandmother died, I went back to that mountain alone. The stone steps were the same steps; there was just no one beside me. I stood in front of the main hall for a long time, not knowing what to ask for. An old monk sweeping the courtyard came over and asked, "What have you come to ask for?" I said I didn\'t know. He nodded. "Not knowing is fine too."',
           '祖母が亡くなった年の冬、わたしはひとりであの山に戻りました。石段は同じ石段なのに、隣には誰もいない。本堂の前に長いあいだ立ち尽くし、何を願えばいいのかわかりませんでした。庭を掃いていた年老いた僧が近づいてきて、「何を願いに来たのですか」と尋ねました。わかりません、と答えると、僧はうなずきました。「わからないのも、いいものです。」',
           '외할머니가 돌아가신 해 겨울, 저는 혼자 그 산에 다시 갔습니다. 돌계단은 그대로였지만 곁에는 아무도 없었습니다. 대웅전 앞에 오래 서 있었지만 무엇을 빌어야 할지 몰랐습니다. 마당을 쓸던 노스님이 다가와 물었습니다. 「무엇을 빌러 왔소?」 모르겠다고 하자 스님은 고개를 끄덕였습니다. 「모르는 것도 괜찮지요.」'),
    'f5': ('他指着身后的山说：「人来这里，多半是求的。求平安，求财，求姻缘。你看这山，它什么也不求——所以什么都有。云来了，它留；云走了，它也不留。」',
           'He pointed to the mountain behind him. "Most people come here to ask for something — safety, money, love. Look at this mountain. It asks for nothing, so it has everything. When the clouds come, it holds them; when they go, it doesn\'t hold on."',
           '僧はうしろの山を指さしました。「ここへ来る人は、たいてい何かを求めに来る。無事を、お金を、良縁を。この山をごらんなさい。何も求めない、だからすべてがある。雲が来れば留め、雲が去れば引き留めない。」',
           '스님은 뒤의 산을 가리켰습니다. 「여기 오는 사람들은 대개 무언가를 구하러 오지요. 평안을, 재물을, 인연을. 이 산을 보시오. 아무것도 구하지 않으니 모든 것을 가졌소. 구름이 오면 머물게 하고, 구름이 가면 붙잡지 않지요.」'),
    'fq': ('「这山什么也不求，所以什么都有。」', '"The mountain asks for nothing, so it has everything."', '「この山は何も求めない、だからすべてがある。」', '「이 산은 아무것도 구하지 않으니, 모든 것을 가졌다.」'),
    'f6': ('下山的路上，我想起《道德经》里的一句：「为学日益，为道日损。」求知，是一天天地加；求道，是一天天地减。原来许愿，并不是为了得到更多，而是在说出心愿的那一刻，把多余的都放下——只剩下最在乎的那一件。',
           'On the way down I remembered a line from the Tao Te Ching: "In learning, one gains a little every day; in the Way, one lets go a little every day." Seeking knowledge is adding; seeking the Way is subtracting. Maybe making a wish was never about getting more. Maybe in the moment you say it, you set down everything extra — until only the one thing you truly care about remains.',
           '山を下りる道で、『道徳経』の一節を思い出しました。「学を為せば日に益し、道を為せば日に損す。」学ぶことは日々足していくこと、道を求めることは日々減らしていくこと。願いをかけるのは、もっと多くを得るためではなかったのかもしれない。願いを口にするその瞬間に、余計なものを下ろして——いちばん大切なひとつだけを残すためなのだと。',
           '산을 내려오는 길에 『도덕경』의 한 구절이 떠올랐습니다. 「배움은 날마다 더하고, 도는 날마다 덜어 낸다.」 앎을 구하는 것은 더하는 일이고, 도를 구하는 것은 덜어 내는 일입니다. 소원을 비는 것은 더 많이 얻으려는 게 아니었는지도 모릅니다. 소원을 말하는 그 순간, 군더더기를 내려놓고——가장 소중한 하나만 남기는 일이었는지도.'),
    'f7': ('佛家说「境由心生」，庄子讲「心斋」：「虚者，心斋也。」心空了，好的东西才进得来。所谓护身，护的从来是那颗心：心定了，路就清楚了；心安了，运也就顺了。',
           'The Buddhists say the world we see is born of the mind. Zhuangzi spoke of the fasting of the heart: emptiness is the fasting of the heart. Only when the heart is empty can good things come in. Whatever protects us, it is always the heart that is being protected: when the heart is settled, the road becomes clear; when the heart is at peace, fortune follows.',
           '仏教は「境は心より生ず」と言い、荘子は「心斎」を説きました——「虚なるものは、心斎なり」。心が空になってはじめて、よいものが入ってくる。身を守るとは、いつも心を守ること。心が定まれば道ははっきりし、心が安らげば運もまた整う。',
           '불가에서는 「경계는 마음에서 생긴다」고 하고, 장자는 「심재」를 말했습니다——「비움이 곧 마음의 재계다.」 마음이 비어야 좋은 것이 들어옵니다. 몸을 지킨다는 것은 언제나 마음을 지키는 일. 마음이 고요하면 길이 보이고, 마음이 편안하면 운도 순해집니다.'),
    'f8': ('中国人讲「器以载道」。一根红绳、一串珠子，本身并不神秘；神秘的，是人放进去的那一念，以及那一念在日复一日的佩戴中，慢慢养成的定力。老话说「人养玉，玉养人」。你戴着它，它也陪着你，渐渐成为你的一部分。',
           'The Chinese say that objects carry the Way. There is nothing mysterious about a thread or a string of beads. What is mysterious is the intention a person places in it — and the quiet steadiness that intention grows into, day after day, as it is worn. An old saying goes: a person nourishes the jade, and the jade nourishes the person. As you wear it, it keeps you company, and slowly becomes part of you.',
           '中国では「器を以て道を載す」と言います。糸や珠そのものに神秘はない。神秘なのは、人がそこに込めるひとつの念、そしてその念が、日々身につけるうちに育てていく静かな落ち着きです。古い言葉に「人は玉を養い、玉は人を養う」とある。あなたが身につけるあいだ、それもあなたに寄り添い、やがてあなたの一部になっていく。',
           '중국에서는 「그릇이 도를 싣는다」고 합니다. 실이나 구슬 자체에는 신비가 없습니다. 신비로운 것은 사람이 거기에 담는 한 생각, 그리고 그 생각이 날마다 착용하는 동안 길러 내는 고요한 힘입니다. 옛말에 「사람이 옥을 기르고, 옥이 사람을 기른다」고 했습니다. 당신이 지니는 동안 그것도 당신 곁에 머물며, 천천히 당신의 일부가 됩니다.'),
    'f9': ('CATHORA 想做的，就是这样的器：说得清来处，经得起近看，也留得下你自己的意义。它不替你求什么；它只是在你忙乱的时候，轻轻碰一下你的手腕，提醒你——回来。',
           'That is the kind of object CATHORA wants to make: one with an origin you can name, a form that rewards a close look, and room for meaning of your own. It doesn\'t ask for anything on your behalf. It only touches your wrist lightly when the day gets loud, and reminds you: come back.',
           'CATHORA がつくりたいのは、そんな器です。由来を語ることができ、近くで見るほどよく、あなた自身の意味を残せるもの。あなたの代わりに何かを求めることはしない。ただ、慌ただしい日に、そっと手首にふれて思い出させる——戻っておいで、と。',
           'CATHORA가 만들고 싶은 것은 그런 그릇입니다. 출처를 말할 수 있고, 가까이 볼수록 좋으며, 당신만의 의미를 남길 수 있는 것. 당신 대신 무엇을 구하지는 않습니다. 다만 하루가 소란할 때 손목을 가만히 건드려 일깨워 줍니다——돌아오라고.'),
    'f10': ('我无法替你许愿。但我希望你戴上它时，能想起某个曾经为你祈福的人；或者，成为那个为别人祈福的人。圆没有起点，也没有终点；祝福也是。',
            'I cannot make a wish for you. But I hope that when you put it on, you think of someone who once prayed for you — or become the one who prays for someone else. A circle has no beginning and no end. Neither does a blessing.',
            'あなたの代わりに願うことはできません。けれど、これを身につけたとき、かつてあなたのために祈ってくれた誰かを思い出してくれたら。あるいは、誰かのために祈る人になってくれたら。円には始まりも終わりもない。祈りもまた。',
            '당신 대신 소원을 빌 수는 없습니다. 하지만 이것을 착용할 때 언젠가 당신을 위해 기도해 준 누군가를 떠올리기를. 혹은 누군가를 위해 기도하는 사람이 되기를. 원에는 시작도 끝도 없습니다. 축복도 그렇습니다.'),
}
