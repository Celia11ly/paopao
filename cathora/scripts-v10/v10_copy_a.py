# -*- coding: utf-8 -*-
"""v10 copy part A: navigation, blessings, home, new lands. Each value: (zh, en, ja, ko)."""

NAV = {
    'shop': ('选购', 'Shop', 'ショップ', '쇼핑'),
    'blessings': ('祈愿', 'Blessings', '祈願', '기원'),
    'lands': ('福地', 'Sacred Lands', '福地', '복지'),
    'elements': ('五行测算', 'Five Elements', '五行診断', '오행 풀이'),
    'story': ('品牌故事', 'Our Story', 'ブランドストーリー', '브랜드 스토리'),
    'byType': ('按品类', 'By type', 'カテゴリー', '종류별'),
    'byElement': ('按五行', 'By element', '五行から', '오행별'),
    'picks': ('精选', 'Edits', 'セレクト', '셀렉트'),
    'all': ('全部作品', 'All pieces', 'すべての作品', '모든 작품'),
    'bracelets': ('手串', 'Bracelets', 'ブレスレット', '팔찌'),
    'necklaces': ('项链与吊坠', 'Necklaces & pendants', 'ネックレス · ペンダント', '목걸이 · 펜던트'),
    'charms': ('幸运挂件', 'Lucky charms', 'ラッキーチャーム', '행운 참'),
    'accessories': ('其他饰品', 'Other accessories', 'その他のアクセサリー', '기타 액세서리'),
    'everyday': ('日常佩戴', 'Everyday', '毎日に', '데일리'),
    'gifting': ('心意赠礼', 'Gifts', 'ギフト', '선물'),
    'allBlessings': ('全部祈愿 →', 'All blessings →', 'すべての祈願 →', '모든 기원 →'),
    'allLands': ('全部福地 →', 'All sacred lands →', 'すべての福地 →', '모든 복지 →'),
    'brand': ('品牌故事', 'Our story', 'ブランドストーリー', '브랜드 스토리'),
    'founder': ('主理人', 'The founder', '主宰者', '디렉터'),
    'care': ('佩戴与保养', 'Ritual & care', '身につけ方とお手入れ', '착용과 관리'),
    'faq': ('常见问题', 'FAQ', 'よくある質問', '자주 묻는 질문'),
    'reading': ('测算你的五行 →', 'Read your elements →', 'あなたの五行を読む →', '나의 오행 읽기 →'),
}

BLESS_ORDER = ['health', 'career', 'wealth', 'love', 'peace', 'retrograde']
BLESS = {
    'health': {'char': '康', 'name': ('健康', 'Health', '健康', '건강'),
               'line': ('愿身体安康，气血和顺。', 'For a body at ease, and breath that flows.', '体がすこやかに、気がめぐるように。', '몸이 편안하고 기운이 고르게 흐르기를.'),
               'desc': ('古人相信，身安则心安。愿你睡得安稳，走得轻快，每一天都有余力，去爱，去做想做的事。', 'The ancients believed a body at ease brings a heart at peace. For steady sleep, a lighter step, and strength to spare for the people and things you love.', '身が安らかなら、心も安らぐと古の人は信じました。穏やかな眠りと軽やかな足どり、愛するものに向ける力が、毎日ありますように。', '몸이 편하면 마음도 편하다고 옛사람들은 믿었습니다. 편안한 잠과 가벼운 걸음, 사랑하는 것들을 위한 힘이 매일 함께하기를.')},
    'career': {'char': '业', 'name': ('事业', 'Career', '仕事運', '사업운'),
               'line': ('愿前路清明，所做皆有所成。', 'For a clear road, and work that bears fruit.', '行く道が澄み、成すことが実るように。', '앞길이 맑고 하는 일마다 결실을 맺기를.'),
               'desc': ('为面试、升职、创业，或是正要换一条路的你。愿前路清明，所做皆有所成。', 'For an interview, a promotion, a new venture or a change of road. May the way ahead be clear, and your work bear fruit.', '面接、昇進、起業、新しい道へ踏み出すあなたへ。行く道が澄み、努力が実りますように。', '면접, 승진, 창업, 혹은 새로운 길 앞에 선 당신에게. 앞길이 맑고, 노력이 결실을 맺기를.')},
    'wealth': {'char': '财', 'name': ('财运', 'Wealth', '金運', '재물운'),
               'line': ('愿财源如水，细水长流。', 'For abundance that flows like water — steady, and long.', '財が水のように、細く長く流れるように。', '재물이 물처럼 가늘고 길게 흐르기를.'),
               'desc': ('不求一夜暴富，只愿财源如水，细水长流——进得来，也留得住。', 'Not sudden riches — abundance that flows like water, steady and long, that arrives and stays.', '一夜の富ではなく、水のように細く長く流れ、訪れてとどまる豊かさを。', '하룻밤의 부가 아니라, 물처럼 가늘고 길게 흘러 들어오고 머무는 풍요를.')},
    'love': {'char': '缘', 'name': ('爱情', 'Love', '恋愛運', '연애운'),
             'line': ('愿有缘人，终会相遇。', 'For the thread that ties two people.', 'ご縁のある人と、いつか必ず。', '인연인 사람과 언젠가 꼭 만나기를.'),
             'desc': ('中国人相信「缘」——一根看不见的红线，早已系在两个人之间。给正在等待的人，也给正在珍惜的人。', 'The Chinese believe in yuan — an invisible red thread already tied between two people. For those still waiting, and those holding on.', '中国の人々は「縁」を信じています——ふたりのあいだに、もう結ばれている見えない赤い糸。待つ人にも、大切にする人にも。', '중국 사람들은 「연(緣)」을 믿습니다. 두 사람 사이에 이미 묶여 있는 보이지 않는 붉은 실. 기다리는 사람에게도, 소중히 지키는 사람에게도.')},
    'peace': {'char': '安', 'name': ('平安', 'Peace & Safety', '平安', '평안'),
              'line': ('愿出入平安，家人康泰。', 'Safety on the road, and peace at home.', '出かける時も家でも、無事であるように。', '오가는 길과 집안이 평안하기를.'),
              'desc': ('「平安」是人们在寺院里求得最多的两个字。远行、搬家、新生儿、长辈的生日——这一组作品，给你牵挂的人。',
                       'Ping\'an — peace and safety — are the two words most asked for in the temples. For a long journey, a new home, a newborn, a parent\'s birthday: pieces for the people you carry in your heart.',
                       '「平安」は、寺院でいちばん多く願われるふた文字です。遠い旅、引っ越し、赤ちゃん、親の誕生日——心にかける人へ。',
                       '「평안」은 사찰에서 가장 많이 비는 두 글자입니다. 먼 여행, 이사, 갓 태어난 아기, 부모님의 생신——마음에 품은 사람에게.')},
    'retrograde': {'char': '转', 'name': ('防水逆', 'Retrograde Protection', '水星逆行のお守り', '수성역행 액막이'),
                   'line': ('愿诸事顺遂，逆境转顺。', 'For the seasons when everything goes sideways.', 'うまくいかない時期を、穏やかに越えられるように。', '일이 꼬이는 시기를 순탄하게 넘기기를.'),
                   'desc': ('《易经》说，穷则变，变则通。当事情接二连三地不顺，愿你站稳，等一等——运会再转回来。', 'The Book of Changes says: when things reach their end, they change; when they change, they flow again. When one thing after another goes wrong, stand steady and wait — the wheel will turn back.', '『易経』は言います。窮まれば変じ、変ずれば通ず。うまくいかないことが続くときも、しっかり立って少し待って——運はまた巡ってきます。', '『주역』은 말합니다. 궁하면 변하고, 변하면 통한다. 일이 연달아 꼬일 때에도 굳게 서서 잠시 기다리세요——운은 다시 돌아옵니다.')},
}

HOME = {
    'blessEyebrow': ('按祈愿选购 · Shop by blessing', 'Shop by blessing · 祈愿', '祈願から選ぶ · Shop by blessing', '기원별 쇼핑 · Shop by blessing'),
    'blessH': ('你在祈愿什么？', 'What are you wishing for?', 'あなたは何を願っていますか。', '무엇을 기원하고 있나요?'),
    'blessP': ('从一个心愿开始，找到属于你的那一件。', 'Begin with a wish, and find the piece that answers it.', 'ひとつの願いから、あなたの一点を。', '하나의 소원에서 시작해 나만의 작품을 찾아보세요.'),
    'shopNow': ('选购', 'Shop', '見る', '쇼핑'),
    'bestH': ('热门作品', 'Most loved', '人気の作品', '인기 작품'),
    'landsH': ('八处福地，\n八段传说。', 'Eight sacred lands,\neight legends.', '八つの福地、\n八つの伝説。', '여덟 곳의 복지,\n여덟 개의 전설.'),
    'landsP': ('千百年来，人们一级一级走上这些石阶。左右滑动，进入每一处福地的故事。', 'For centuries, people have climbed these stone steps. Swipe to enter the story of each place.', '何百年も、人々はこの石段を登ってきました。スワイプして、それぞれの福地の物語へ。', '수백 년 동안 사람들은 이 돌계단을 올랐습니다. 옆으로 넘겨 각 복지의 이야기로 들어가 보세요.'),
    'prev': ('上一个', 'Previous', '前へ', '이전'),
    'next': ('下一个', 'Next', '次へ', '다음'),
    'blessEmpty': ('这个祈愿的作品正在准备中。留下邮箱，作品上线时第一时间告诉你。', 'Pieces for this blessing are on their way. Leave your email and we will tell you first.', 'この祈願の作品は、いま準備中です。メールアドレスを残していただければ、いち早くお知らせします。', '이 기원의 작품은 지금 준비 중입니다. 이메일을 남겨 주시면 가장 먼저 알려 드릴게요.'),
    'heroCta1': ('选购全部作品', 'Shop all pieces', 'すべての作品を見る', '모든 작품 보기'),
    'heroCta2': ('按祈愿挑选', 'Shop by blessing', '祈願から選ぶ', '기원별로 고르기'),
}

PROMISES = [
    (('从中国直发全球', 'Shipped worldwide from China', '中国から世界へ', '중국에서 전 세계로'),
     ('31 个国家与地区，满 SGD 200 免标准运费。', '31 countries and regions. Free standard shipping over SGD 200.', '31の国と地域へ。SGD 200以上で通常配送無料。', '31개 국가·지역. SGD 200 이상 일반 배송 무료.')),
    (('30 天退换', '30-day returns', '30日間返品可', '30일 반품'),
     ('未佩戴、包装完整，30 天内可退换；破损或错发免费补发。', 'Unworn, in original packaging, within 30 days. Damaged or wrong items replaced free.', '未使用・元の包装なら30日以内に返品可。破損・誤配送は無料で再送。', '미착용·원래 포장 시 30일 이내 반품 가능. 파손·오배송은 무료 재발송.')),
    (('每件附出处卡', 'An origin in every box', 'すべてに由来カード', '모든 작품에 유래 카드'),
     ('告诉你它从哪里来、意味着什么。', 'Where your piece comes from, and what it means.', 'どこから来て、何を意味するのか。', '어디서 왔고 무엇을 뜻하는지.')),
    (('回馈寺院', 'Returned to the temples', '寺院へ還す', '사찰에 돌려드립니다'),
     ('每一笔购买，都有一部分回到寺院。', 'Part of every purchase returns to the temple communities.', 'お買い上げのたびに、その一部が寺院へ還ります。', '구매 금액의 일부가 사찰 공동체로 돌아갑니다.')),
]

LAND_ORDER = ['putuo', 'lingyin', 'jingshan', 'tiantai', 'emei', 'longmen', 'white-horse', 'wudang']
LAND_META = {  # zh name, roman, collection handle, photo file, element key, credit
    'putuo': ('普陀', 'Putuo', 'putuo', 'cathora-land-putuo.jpg', 'water', ('Xie Jian / Unsplash', 'Unsplash License', 'https://unsplash.com/photos/the-roof-of-a-building-with-a-sky-background-lsq11kaz9Uc')),
    'lingyin': ('灵隐', 'Lingyin', 'lingyin', 'cathora-land-lingyin.jpg', 'wood', ('Yeh Xintong / Unsplash', 'Unsplash License', 'https://unsplash.com/photos/brown-and-black-signage-wmTKji77pUU')),
    'jingshan': ('径山', 'Jingshan', 'jingshan', 'cathora-land-jingshan.jpg', 'wood', ('一只猫的橘 / Unsplash', 'Unsplash License', 'https://unsplash.com/photos/traditional-houses-nestled-in-lush-green-tea-fields-Uf9fCeIaBEM')),
    'tiantai': ('天台', 'Tiantai', 'tiantai', 'cathora-land-tiantai.jpg', 'earth', ('黑揍红', 'CC BY-SA 2.5', 'https://commons.wikimedia.org/wiki/File:Guoqing_Temple_2019-11-14_2.jpg')),
    'emei': ('峨眉', 'Emei', 'emei', 'cathora-land-emei.jpg', 'metal', ('lynying Ju / Unsplash', 'Unsplash License', 'https://unsplash.com/photos/a-view-of-the-clouds-from-above-jL6idOkZ4gI')),
    'longmen': ('龙门', 'Longmen', 'longmen', 'cathora-land-longmen.jpg', 'earth', ('Zihao Chen / Unsplash', 'Unsplash License', 'https://unsplash.com/photos/a-statue-of-a-man-zJP_j-cpfug')),
    'white-horse': ('白马', 'White Horse', 'white-horse', 'cathora-land-white-horse.jpg', 'metal', ('xiquinhosilva', 'CC BY 2.0', 'https://commons.wikimedia.org/wiki/File:27467-Luoyang_(49085730123).jpg')),
    'wudang': ('武当', 'Wudang', 'wudang', 'cathora-land-wudang.JPG', 'fire', ('Gisling', 'CC BY 3.0', 'https://commons.wikimedia.org/wiki/File:%E7%B4%AB%E9%9C%84%E6%AE%BF%E7%9A%84%E6%96%97%E6%A0%B1.JPG')),
}

NEW_LANDS = {
    'longmen': {
        'subtitle': ('石上千年', 'A Thousand Years in Stone', '石に刻まれた千年', '돌에 새긴 천 년'),
        'legend': ('伊水两岸的崖壁上，十万尊佛像静静坐了一千五百年。', 'On the cliffs above the Yi River, a hundred thousand Buddhas have sat in silence for fifteen centuries.', '伊水のほとりの崖で、十万の仏が千五百年、静かに座りつづけている。', '이수 강가의 절벽에서 십만 부처가 천오백 년을 고요히 앉아 있습니다.'),
        'intention': ('坚定 · 长久', 'Endurance · Resolve', '揺るがぬ心 · 長く続くもの', '굳건함 · 오래감'),
        'element': ('土', 'Earth', '土', '토(土)'),
        'known': ('卢舍那大佛、伊河、石窟造像', 'The Vairocana Buddha, the Yi River, cave carvings', '盧舎那大仏、伊河、石窟の造像', '노사나 대불, 이하, 석굴 조상'),
        'lead': ('洛阳城南，伊河从两山之间流过。古人说，这两山对峙如阙门，于是叫它龙门。', 'South of Luoyang, the Yi River runs between two hills that face each other like the towers of a gate. The ancients called it the Dragon Gate.', '洛陽の南、伊河はふたつの山のあいだを流れます。門の楼閣のように向かい合う山を、古人は龍門と呼びました。', '뤄양 남쪽, 이하는 마주 선 두 산 사이를 흐릅니다. 성문의 누각처럼 마주 선 그 산을 옛사람들은 용문이라 불렀습니다.'),
        's1': ('从北魏到大唐，四百多年间，工匠们在石灰岩崖壁上一凿一凿，刻下了十万余尊佛像，最小的只有两厘米，最大的高十七米。', 'From the Northern Wei to the Tang, for more than four hundred years, craftsmen cut into the limestone, stroke by stroke, until more than a hundred thousand figures filled the cliffs — the smallest two centimetres high, the largest seventeen metres.', '北魏から唐まで四百年あまり、職人たちは石灰岩の崖を一打ち一打ち刻み、十万を超える仏を彫りました。小さなものは二センチ、大きなものは十七メートル。', '북위에서 당나라까지 사백여 년 동안, 장인들은 석회암 절벽을 한 땀 한 땀 쪼아 십만이 넘는 불상을 새겼습니다. 가장 작은 것은 2센티미터, 가장 큰 것은 17미터.'),
        's2': ('奉先寺的卢舍那大佛，面容据说照着一位女皇的模样雕成。她低眉含笑，望着河水，也望着每一个仰头看她的人。', 'The great Vairocana Buddha of Fengxian is said to have been carved in the likeness of an empress. Eyes lowered, half smiling, she watches the river — and everyone who looks up at her.', '奉先寺の盧舎那大仏は、ひとりの女帝の面影を写したと伝えられます。伏し目がちにほほえみ、川を、そして見上げる一人ひとりを見つめています。', '봉선사의 노사나 대불은 한 여황제의 모습을 따라 새겼다고 전해집니다. 눈을 내리깔고 미소 지으며 강물을, 그리고 올려다보는 한 사람 한 사람을 바라봅니다.'),
        's3': ('风雨一千五百年，石头记住了每一下凿痕。有些东西，就是要慢慢地、一点一点地留下来。', 'Fifteen hundred years of wind and rain, and the stone remembers every cut. Some things are meant to be made slowly, one mark at a time.', '千五百年の風雨のなかで、石はすべての鑿の跡を覚えています。ゆっくりと、ひとつずつ残していくものがある。', '천오백 년의 비바람 속에서 돌은 모든 정 자국을 기억합니다. 어떤 것은 천천히, 한 자국씩 남겨야 합니다.'),
        'close': ('这一章，献给坚持，和需要时间才能长成的事。', 'This chapter is for endurance, and for the things that take time to become.', 'この章を、続ける力と、時間をかけて育つものへ。', '이 장을, 꾸준함과 시간이 걸려야 자라는 것들에 바칩니다.'),
    },
    'white-horse': {
        'subtitle': ('东来的第一座寺', 'The First Temple', 'はじまりの寺', '처음의 절'),
        'legend': ('一匹白马驮着经卷，走了几千里，佛法从此来到中国。', 'A white horse carried the scriptures across thousands of miles, and the teaching arrived in China.', '一頭の白馬が経典を背に何千里を歩き、仏の教えは中国にたどり着いた。', '백마 한 마리가 경전을 싣고 수천 리를 걸어, 부처의 가르침이 중국에 닿았습니다.'),
        'intention': ('相遇 · 远方', 'Connection · Journeys', '出会い · 遠いところ', '만남 · 먼 곳'),
        'element': ('金', 'Metal', '金', '금(金)'),
        'known': ('中国第一古刹、齐云塔、白马驮经', 'China\'s first temple, the Qiyun Pagoda, the white horse', '中国最古の寺、斉雲塔、白馬', '중국 최초의 사찰, 제운탑, 백마'),
        'lead': ('公元六十八年，洛阳城外，中国有了第一座佛寺。', 'In the year 68, outside the walls of Luoyang, China built its first Buddhist temple.', '西暦六十八年、洛陽の城外に、中国で最初の仏教寺院が建てられました。', '서기 68년, 뤄양 성 밖에 중국 최초의 불교 사찰이 세워졌습니다.'),
        's1': ('相传汉明帝夜里梦见一位金人，周身有光，从西方飞来。他派使者西行寻访，在远方遇到两位僧人，便请他们东归。', 'The story goes that Emperor Ming dreamed one night of a golden figure, glowing, flying in from the west. He sent envoys to find it, and far away they met two monks and asked them to come east.', '漢の明帝はある夜、光をまとった金色の人が西から飛んでくる夢を見たと伝えられます。使者を西へ送ると、遠い地でふたりの僧に出会い、東へ来てくれるよう願いました。', '한나라 명제는 어느 밤, 온몸이 빛나는 금빛 사람이 서쪽에서 날아오는 꿈을 꾸었다고 합니다. 사신을 서쪽으로 보내자 먼 곳에서 두 스님을 만나 동쪽으로 와 달라고 청했습니다.'),
        's2': ('一匹白马驮着经卷和佛像，陪他们走回洛阳。为了记住这匹马，新建的寺院就叫白马寺。', 'A white horse carried the scriptures and images all the way back to Luoyang beside them. To remember it, the new temple was named for the horse.', '一頭の白馬が経典と仏像を背に、彼らとともに洛陽まで歩きました。その馬を忘れないように、新しい寺は白馬寺と名づけられました。', '백마 한 마리가 경전과 불상을 싣고 그들과 함께 뤄양까지 걸었습니다. 그 말을 기억하려고 새 절의 이름을 백마사라 지었습니다.'),
        's3': ('一个梦，一段远路，两个陌生人，一匹马。所有重要的相遇，大概都是这样开始的。', 'A dream, a long road, two strangers and a horse. Perhaps every meeting that matters begins like this.', 'ひとつの夢、長い道、ふたりの旅人、一頭の馬。大切な出会いは、たぶんみんなこうして始まる。', '하나의 꿈, 먼 길, 낯선 두 사람, 말 한 마리. 소중한 만남은 아마 모두 이렇게 시작될 것입니다.'),
        'close': ('这一章，献给远方，和那些走了很远来到你身边的人。', 'This chapter is for journeys, and for the people who travelled far to find you.', 'この章を、遠い道のりと、遠くからあなたのもとへ来た人へ。', '이 장을, 먼 길과 멀리서 당신 곁으로 온 사람들에게 바칩니다.'),
    },
    'wudang': {
        'subtitle': ('太极之山', 'Mountain of Taiji', '太極の山', '태극의 산'),
        'legend': ('云雾里的道家仙山，太极拳从这里打出第一个圆。', 'A Taoist mountain in the clouds, where Tai Chi drew its first circle.', '雲のなかの道教の仙山。太極拳が最初の円を描いた場所。', '구름 속 도교의 선산. 태극권이 첫 원을 그린 곳.'),
        'intention': ('平衡 · 护身', 'Balance · Protection', '調和 · 護身', '균형 · 호신'),
        'element': ('火', 'Fire', '火', '화(火)'),
        'known': ('金顶、紫霄宫、太极', 'The Golden Hall, the Purple Cloud Palace, Tai Chi', '金頂、紫霄宮、太極', '금정, 자소궁, 태극'),
        'lead': ('湖北的群山之中，七十二座山峰都朝向同一处——天柱峰顶那座铜铸鎏金的金殿。', 'In the mountains of Hubei, seventy-two peaks all seem to bow toward one point: the gilded bronze hall on the summit of Heaven\'s Pillar.', '湖北の山々のなか、七十二の峰がみな一点を向いています——天柱峰の頂にある金色の銅の殿へ。', '후베이의 산들 가운데 일흔두 봉우리가 모두 한 곳을 향합니다. 천주봉 꼭대기의 금빛 구리 전각으로.'),
        's1': ('道家相信，天地之间有阴有阳，一动一静，周而复始。传说一位道人看见喜鹊与蛇相斗，一柔一刚，忽然悟出了太极。', 'Taoists believe the world turns between yin and yang — stillness and motion, again and again. Legend says a hermit here once watched a magpie fight a snake, softness against strength, and in that moment understood Tai Chi.', '道教では、天地は陰と陽、静と動をくり返しめぐると考えます。ある道士がカササギと蛇の争いを見て、柔と剛のなかに太極を悟ったと伝えられます。', '도가에서는 천지가 음과 양, 고요와 움직임을 되풀이하며 돈다고 믿습니다. 전설에 따르면 한 도인이 까치와 뱀이 싸우는 것을 보고, 부드러움과 강함 속에서 태극을 깨달았다고 합니다.'),
        's2': ('六百年前，皇帝下令在山中修建宫观，金殿用铜铸成，再镀上黄金。雷雨天，闪电落在殿顶，火光如海，殿却完好如初。', 'Six hundred years ago an emperor ordered palaces built across the mountain, and the summit hall was cast in bronze and covered in gold. In summer storms lightning strikes its roof in a sea of fire — and the hall stands untouched.', '六百年前、皇帝の命で山じゅうに宮観が建てられ、頂の殿は銅で鋳造され、金で覆われました。夏の雷雨には稲妻が屋根に落ち、火の海のように光りますが、殿は今も無傷のままです。', '육백 년 전 황제의 명으로 산 곳곳에 궁관이 세워졌고, 정상의 전각은 구리로 주조해 금을 입혔습니다. 여름 뇌우에 번개가 지붕에 떨어져 불바다처럼 빛나도, 전각은 지금도 온전합니다.'),
        's3': ('柔能克刚，静能制动。真正的力量，往往是稳住自己。', 'The soft overcomes the hard; stillness masters motion. Real strength is often just staying steady.', '柔よく剛を制し、静よく動を制す。本当の強さは、自分を保つことにある。', '부드러움이 강함을 이기고, 고요함이 움직임을 다스립니다. 진정한 힘은 흔들리지 않는 데 있습니다.'),
        'close': ('这一章，献给平衡，和在风雨里依然站稳的你。', 'This chapter is for balance, and for standing steady in the storm.', 'この章を、調和と、嵐のなかでも立ちつづけるあなたへ。', '이 장을, 균형과 비바람 속에서도 굳게 서는 당신에게 바칩니다.'),
    },
}
