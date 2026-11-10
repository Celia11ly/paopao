# -*- coding: utf-8 -*-
"""v10.9: Five Elements result, redesigned (hero, type + wheel, favourable / unfavourable with plain reasons)."""
import json

ELS = ['wood', 'fire', 'earth', 'metal', 'water']
R = {}

R['zh'] = {
    'title': '{sb}日出生的你', 'dm': '日主为{stem} · {dmText}',
    'types': {'strong': '身强型', 'slightlyStrong': '偏强型', 'slightlyWeak': '偏弱型', 'weak': '身弱型'},
    'typeStrong': '你的能量充沛，像一条丰水期的河——不缺力量，缺的是出口。把多余的能量引向才华、财富与事业，运势自然流转起来。',
    'typeWeak': '你的能量内敛而细腻，像一盏需要添油的灯——不缺方向，缺的是滋养。多得贵人与同伴扶持，运势便会稳稳升起。',
    'wheelH': '五行能量分布', 'dmTag': '日主', 'sheng': '生', 'ke': '克',
    'roles': {'same': ['比劫', '自我'], 'res': ['印星', '贵人'], 'out': ['食伤', '才华'], 'wea': ['财星', '财富'], 'off': ['官杀', '事业']},
    'favH': '对你有利的五行', 'favTag': '喜用', 'avoidH': '宜少接触的五行', 'avoidTag': '忌',
    'rows': {'color': '幸运颜色', 'dir': '幸运方位', 'num': '幸运数字', 'mat': '宜佩材质'},
    'fav': {'out': '释放才华：给充沛的能量一个出口，让想法变成作品与表达。', 'wea': '收获财富：把力量用在实处，化为看得见的回报。',
            'off': '成就事业：为你定方向、立规矩，让锋芒化为成就与名望。', 'res': '贵人相助：像长辈一样滋养你，带来学识、庇护与好机缘。',
            'same': '同伴扶持：同气相求，给你底气与行动力。'},
    'avoid': {'res': '能量已足，再被滋养容易想得多、做得少，固执己见。', 'same': '同类过多，容易争强好胜，人际有摩擦，钱财易散。',
              'out': '过度消耗心力，容易疲惫、焦虑、力不从心。', 'wea': '财多身弱，机会来了却难以握住，压力随之而来。',
              'off': '外界的压力与约束偏重，容易紧绷、劳累。'},
    'tipH': '小贴士',
    'summer': '你生于夏季，命局偏热——平日多亲近水、保持清凉，有助于平衡。', 'winter': '你生于冬季，命局偏寒——平日多晒太阳、亲近温暖，有助于平衡。',
    'missFav': '你的八字中缺{list}，而它正好对你有利，值得多多亲近。', 'missOther': '你的八字中缺{list}，它并非你的喜用，缺了反而无妨。',
    'sep': '、',
    'dirs': {'wood': '东', 'fire': '南', 'earth': '西南、东北', 'metal': '西', 'water': '北'},
    'colors': {'wood': '青绿', 'fire': '红紫', 'earth': '黄棕', 'metal': '白金', 'water': '黑蓝'},
}

R['en'] = {
    'title': 'Born on a {sb} day', 'dm': 'Day master {stem} · {dmText}',
    'types': {'strong': 'Strong type', 'slightlyStrong': 'Leaning strong', 'slightlyWeak': 'Leaning gentle', 'weak': 'Gentle type'},
    'typeStrong': 'Your energy runs full, like a river in flood — you don\'t lack strength, you need an outlet. Channel the surplus into talent, wealth and work, and fortune begins to move.',
    'typeWeak': 'Your energy is inward and fine, like a lamp that wants more oil — you don\'t lack direction, you need nourishment. With support from mentors and allies, your fortune rises steadily.',
    'wheelH': 'Your elemental balance', 'dmTag': 'You', 'sheng': 'feeds', 'ke': 'checks',
    'roles': {'same': ['', 'Self'], 'res': ['', 'Support'], 'out': ['', 'Talent'], 'wea': ['', 'Wealth'], 'off': ['', 'Career']},
    'favH': 'Elements that favour you', 'favTag': 'Favourable', 'avoidH': 'Elements to keep in check', 'avoidTag': 'Unfavourable',
    'rows': {'color': 'Lucky colours', 'dir': 'Lucky directions', 'num': 'Lucky numbers', 'mat': 'Materials to wear'},
    'fav': {'out': 'Release your talent: give abundant energy an outlet, so ideas become work and expression.', 'wea': 'Reap the reward: put your strength to practical use, and turn it into results you can see.',
            'off': 'Build your career: direction and structure turn your edge into achievement and standing.', 'res': 'Find support: like an elder, it nourishes you with learning, protection and good fortune.',
            'same': 'Walk with allies: kindred energy gives you confidence and the will to act.'},
    'avoid': {'res': 'Your energy is already full; more nourishment can mean overthinking, underdoing and digging in.', 'same': 'Too much of your own kind breeds rivalry and friction, and money slips away.',
              'out': 'It drains your reserves, leaving you tired, anxious and stretched thin.', 'wea': 'Opportunity outweighs your strength — it arrives but is hard to hold, and pressure follows.',
              'off': 'Outside pressure and constraint weigh heavily, leaving you tense and worn.'},
    'tipH': 'A note',
    'summer': 'Born in summer, your chart runs warm — time near water and keeping cool help you balance.', 'winter': 'Born in winter, your chart runs cold — sunlight and warmth help you balance.',
    'missFav': 'Your chart has no {list} — and it happens to favour you, so it is well worth drawing close to.', 'missOther': 'Your chart has no {list} — it isn\'t one of your favourable elements, so its absence does no harm.',
    'sep': ', ',
    'dirs': {'wood': 'East', 'fire': 'South', 'earth': 'South-west, North-east', 'metal': 'West', 'water': 'North'},
    'colors': {'wood': 'Green', 'fire': 'Red', 'earth': 'Yellow', 'metal': 'White', 'water': 'Blue'},
}

R['ja'] = {
    'title': '{sb}の日に生まれたあなた', 'dm': '日主は{stem} · {dmText}',
    'types': {'strong': '身強タイプ', 'slightlyStrong': 'やや強タイプ', 'slightlyWeak': 'やや弱タイプ', 'weak': '身弱タイプ'},
    'typeStrong': 'あなたのエネルギーは満ちあふれ、水量豊かな川のよう。力は足りている、必要なのは出口です。余る力を才能・財・仕事へ向ければ、運は自然にめぐり出します。',
    'typeWeak': 'あなたのエネルギーは内に秘めた繊細なもの、油を足したい灯のよう。方向は見えている、必要なのは滋養です。貴人や仲間の支えを得れば、運は着実に上向きます。',
    'wheelH': '五行のバランス', 'dmTag': '日主', 'sheng': '生', 'ke': '剋',
    'roles': {'same': ['比劫', '自分'], 'res': ['印星', '貴人'], 'out': ['食傷', '才能'], 'wea': ['財星', '財'], 'off': ['官殺', '仕事']},
    'favH': 'あなたを助ける五行', 'favTag': '喜用', 'avoidH': '控えたい五行', 'avoidTag': '忌',
    'rows': {'color': 'ラッキーカラー', 'dir': 'ラッキー方位', 'num': 'ラッキーナンバー', 'mat': '身につけたい素材'},
    'fav': {'out': '才能を解き放つ：満ちた力に出口を与え、思いを作品や表現に変えます。', 'wea': '実りを得る：力を実際に使い、目に見える成果に変えます。',
            'off': '仕事を成す：方向と規律を与え、鋭さを成果と名声に変えます。', 'res': '貴人の助け：目上の人のようにあなたを養い、学び・庇護・良縁をもたらします。',
            'same': '仲間の支え：同じ気が寄り添い、自信と行動力をくれます。'},
    'avoid': {'res': 'すでに力は十分。さらに養われると、考えすぎて動けず、頑なになりがちです。', 'same': '同類が多すぎると、張り合いや摩擦が生まれ、お金も散りやすくなります。',
              'out': '心身を消耗しやすく、疲れや不安、力不足を招きます。', 'wea': '財が多く身が弱い。機会が来てもつかみきれず、重圧がついてきます。',
              'off': '外からの圧力や制約が重く、緊張や疲れがたまりやすくなります。'},
    'tipH': 'ひとこと',
    'summer': '夏生まれで命式は熱に傾きがち。水に親しみ、涼やかに過ごすとバランスが整います。', 'winter': '冬生まれで命式は寒に傾きがち。日の光やぬくもりに親しむとバランスが整います。',
    'missFav': 'あなたの八字には{list}がありません。ちょうど喜用なので、積極的に近づきましょう。', 'missOther': 'あなたの八字には{list}がありません。喜用ではないので、欠けていても差し支えありません。',
    'sep': '・',
    'dirs': {'wood': '東', 'fire': '南', 'earth': '南西・北東', 'metal': '西', 'water': '北'},
    'colors': {'wood': '緑', 'fire': '赤', 'earth': '黄', 'metal': '白', 'water': '紺'},
}

R['ko'] = {
    'title': '{sb}일에 태어난 당신', 'dm': '일주 {stem} · {dmText}',
    'types': {'strong': '신강형', 'slightlyStrong': '약간 신강형', 'slightlyWeak': '약간 신약형', 'weak': '신약형'},
    'typeStrong': '당신의 에너지는 넘쳐흐르는 강물처럼 충만합니다. 힘이 부족한 것이 아니라 출구가 필요합니다. 넘치는 힘을 재능·재물·일로 이끌면 운이 자연스럽게 흐르기 시작합니다.',
    'typeWeak': '당신의 에너지는 안으로 깊고 섬세합니다. 기름을 더해야 할 등불처럼, 방향은 있으나 자양이 필요합니다. 귀인과 동료의 도움을 받으면 운이 차근차근 오릅니다.',
    'wheelH': '오행 에너지 분포', 'dmTag': '일주', 'sheng': '생', 'ke': '극',
    'roles': {'same': ['비겁', '자아'], 'res': ['인성', '귀인'], 'out': ['식상', '재능'], 'wea': ['재성', '재물'], 'off': ['관살', '일']},
    'favH': '당신을 돕는 오행', 'favTag': '희용', 'avoidH': '절제할 오행', 'avoidTag': '기신',
    'rows': {'color': '행운의 색', 'dir': '행운의 방위', 'num': '행운의 숫자', 'mat': '지니면 좋은 소재'},
    'fav': {'out': '재능을 펼치다: 넘치는 힘에 출구를 주어 생각을 작품과 표현으로 바꿉니다.', 'wea': '결실을 거두다: 힘을 실제에 써서 눈에 보이는 성과로 바꿉니다.',
            'off': '일을 이루다: 방향과 규율을 주어 날카로움을 성취와 명성으로 바꿉니다.', 'res': '귀인의 도움: 어른처럼 당신을 길러 배움·보호·좋은 인연을 가져옵니다.',
            'same': '동료의 지지: 같은 기운이 곁에서 자신감과 행동력을 줍니다.'},
    'avoid': {'res': '이미 힘이 충분한데 더 채워지면 생각만 많고 실행이 줄며 고집스러워지기 쉽습니다.', 'same': '같은 기운이 지나치면 경쟁과 마찰이 생기고 재물이 흩어지기 쉽습니다.',
              'out': '심력을 과하게 소모해 피로·불안·무력감이 오기 쉽습니다.', 'wea': '재물은 많은데 몸이 약해 기회가 와도 붙잡기 어렵고 압박이 따릅니다.',
              'off': '바깥의 압박과 제약이 무거워 긴장하고 지치기 쉽습니다.'},
    'tipH': '한마디',
    'summer': '여름에 태어나 명식이 뜨거운 편입니다. 물을 가까이하고 시원하게 지내면 균형에 도움이 됩니다.', 'winter': '겨울에 태어나 명식이 차가운 편입니다. 햇볕과 따뜻함을 가까이하면 균형에 도움이 됩니다.',
    'missFav': '당신의 팔자에 없는 오행: {list}. 마침 희용이니 적극적으로 가까이하세요.', 'missOther': '당신의 팔자에 없는 오행: {list}. 희용이 아니니 없어도 괜찮습니다.',
    'sep': '·',
    'dirs': {'wood': '동', 'fire': '남', 'earth': '남서·북동', 'metal': '서', 'water': '북'},
    'colors': {'wood': '초록', 'fire': '빨강', 'earth': '노랑', 'metal': '하양', 'water': '남색'},
}


def liquid_json():
    mats = ',"mat":{' + ','.join('"%s":{{ \'v9.el.%s.materials\' | t | json }}' % (k, k) for k in ELS) + '}'
    parts = ["{%% when '%s' %%}%s" % (loc, json.dumps(R[loc], ensure_ascii=False)[:-1] + mats + '}') for loc in ['en', 'ja', 'ko']]
    return ('<script type="application/json" id="v10-el-read">{% case request.locale.iso_code %}' + ''.join(parts)
            + '{% else %}' + json.dumps(R['zh'], ensure_ascii=False)[:-1] + mats + '}{% endcase %}</script>')


JS = r'''
/* v10 reading */
(function(){
  var GEN={wood:'fire',fire:'earth',earth:'metal',metal:'water',water:'wood'}, CTL={wood:'earth',earth:'water',water:'fire',fire:'metal',metal:'wood'};
  var COLOR={wood:'#56634A',fire:'#9E3B2C',earth:'#8C6A43',metal:'#6E6C66',water:'#2F3B45'}, CH={wood:'木',fire:'火',earth:'土',metal:'金',water:'水'};
  var SWATCH={wood:'#5F8A5B',fire:'#C4523A',earth:'#D2AE5A',metal:'#F3F0E8',water:'#2C4A66'};
  var NUMS={wood:[3,8],fire:[2,7],earth:[5,10],metal:[4,9],water:[1,6]};
  var SEASON={'寅':'spring','卯':'spring','辰':'spring','巳':'summer','午':'summer','未':'summer','申':'autumn','酉':'autumn','戌':'autumn','亥':'winter','子':'winter','丑':'winter'};
  var WHEEL=['fire','earth','metal','water','wood'];
  function f(s,o){return String(s).replace(/\{(\w+)\}/g,function(m,k){return o[k]!==undefined?o[k]:m;});}
  function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
  window.v10Fav=function(r){
    var dm=r.dayEl,res,off,out=GEN[dm],wea=CTL[dm],s=r.score;
    for(var e in GEN){if(GEN[e]===dm)res=e;if(CTL[e]===dm)off=e;}
    var strong=r.ratio>=50,fav,avoid;
    if(strong){
      var first=s[res]>s[dm]?wea:(s[off]>=s[out]?off:out);
      fav=[first].concat([out,wea,off].filter(function(k){return k!==first;}));
      avoid=[res,dm].sort(function(a,b){return s[b]-s[a];});
    }else{
      var en=[off,out,wea].sort(function(a,b){return s[b]-s[a];});
      fav=en[0]===wea?[dm,res]:[res,dm];
      avoid=en;
    }
    var role={}; role[res]='res';role[dm]='same';role[out]='out';role[wea]='wea';role[off]='off';
    r.favorable=fav.slice(0,2);
    r.v10={strong:strong,fav:fav,avoid:avoid,role:role};
  };
  function wheel(r,L,T){
    var cx=200,cy=185,R0=118,pos={};
    WHEEL.forEach(function(k,i){var a=(-90+i*72)*Math.PI/180;pos[k]={x:cx+R0*Math.cos(a),y:cy+R0*Math.sin(a),a:a};});
    var rad=function(k){return 24+Math.min(r.pct[k],80)*0.32;};
    var g='<svg class="v10r-wheel" viewBox="0 0 400 380" role="img" aria-label="'+esc(L.wheelH)+'"><defs><marker id="v10ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="#9C8E7A"/></marker></defs>';
    WHEEL.forEach(function(k,i){var t=WHEEL[(i+2)%5],a=pos[k],b=pos[t];g+='<line x1="'+a.x+'" y1="'+a.y+'" x2="'+b.x+'" y2="'+b.y+'" stroke="#D9D2C4" stroke-width="1" stroke-dasharray="3 4"/>';});
    WHEEL.forEach(function(k,i){var t=WHEEL[(i+1)%5],a=pos[k],b=pos[t],dx=b.x-a.x,dy=b.y-a.y,d=Math.sqrt(dx*dx+dy*dy),ux=dx/d,uy=dy/d,ra=rad(k)+6,rb=rad(t)+8;
      var x1=a.x+ux*ra,y1=a.y+uy*ra,x2=b.x-ux*rb,y2=b.y-uy*rb,mx=(x1+x2)/2,my=(y1+y2)/2,nx=-uy,ny=ux,ox=(mx-cx)>0?1:-1;
      var cxp=mx+nx*14*((nx*(mx-cx)+ny*(my-cy))>0?1:-1),cyp=my+ny*14*((nx*(mx-cx)+ny*(my-cy))>0?1:-1);
      g+='<path d="M'+x1.toFixed(1)+' '+y1.toFixed(1)+' Q'+cxp.toFixed(1)+' '+cyp.toFixed(1)+' '+x2.toFixed(1)+' '+y2.toFixed(1)+'" fill="none" stroke="#9C8E7A" stroke-width="1.4" marker-end="url(#v10ar)"/>';
      var lx=mx+(mx-cx)/R0*22,ly=my+(my-cy)/R0*22;g+='<text x="'+lx.toFixed(1)+'" y="'+(ly+4).toFixed(1)+'" text-anchor="middle" font-size="11" fill="#9C8E7A">'+esc(L.sheng)+'</text>';});
    WHEEL.forEach(function(k){var p=pos[k],rr=rad(k),c=COLOR[k],dm=k===r.dayEl,ro=L.roles[r.v10.role[k]];
      g+='<circle cx="'+p.x+'" cy="'+p.y+'" r="'+rr+'" fill="'+c+'" fill-opacity="'+(dm?0.95:0.1)+'" stroke="'+c+'" stroke-width="'+(dm?0:1.4)+'"/>';
      g+='<text x="'+p.x+'" y="'+(p.y-2)+'" text-anchor="middle" font-family="Noto Serif SC,serif" font-size="'+(rr>40?24:20)+'" fill="'+(dm?'#FBFAF7':c)+'">'+CH[k]+'</text>';
      g+='<text x="'+p.x+'" y="'+(p.y+16)+'" text-anchor="middle" font-size="12" fill="'+(dm?'#FBFAF7':c)+'">'+r.pct[k]+'%</text>';
      if(dm)g+='<rect x="'+(p.x-22)+'" y="'+(p.y+rr-8)+'" width="44" height="18" rx="9" fill="#1F1E1B"/><text x="'+p.x+'" y="'+(p.y+rr+5)+'" text-anchor="middle" font-size="11" fill="#FBFAF7">'+esc(L.dmTag)+'</text>';
      var ox=Math.cos(p.a),oy=Math.sin(p.a),lx=p.x+ox*(rr+30),ly=p.y+oy*(rr+22)+(oy<-0.5?-4:0),anc=Math.abs(ox)<0.3?'middle':(ox>0?'start':'end');
      if(Math.abs(ox)>=0.3)lx=p.x+ox*(rr+10);
      g+='<text x="'+lx.toFixed(1)+'" y="'+ly.toFixed(1)+'" text-anchor="'+anc+'" font-size="12" fill="'+c+'">'+(ro[0]?'<tspan font-weight="600">'+esc(ro[0])+'</tspan> ':'')+esc(ro[1])+'</text>';});
    return g+'</svg>';
  }
  window.v10Render=function(r,T,P){
    var node=document.getElementById('v10-el-read'); if(!node||!r.v10)return '';
    var L=JSON.parse(node.textContent),v=r.v10,N=function(k){return T.el[k];},NM=function(k){return N(k)===CH[k]?'':esc(N(k));};
    var day=r.pillars[2],labels={year:T.pYear,month:T.pMonth,day:T.pDay,hour:T.pHour};
    var dmText=T.dm['s'+r.dayIndex];
    var h='<div class="v10r">';
    h+='<header class="v10r-hero"><p class="v9-eyebrow red">'+esc(T.pillarsH)+'</p><h3>'+esc(f(L.title,{sb:day.stem+day.branch}))+'</h3><p class="v10r-dm">'+esc(f(L.dm,{stem:r.dayStem,dmText:dmText}))+'</p><div class="v10r-pillars">';
    r.pillars.forEach(function(p){h+='<div><span class="k">'+esc(labels[p.k])+'</span><b style="color:'+COLOR[p.stemEl]+'">'+p.stem+'</b><b style="color:'+COLOR[p.branchEl]+'">'+p.branch+'</b></div>';});
    if(!r.hasTime)h+='<div class="na"><span class="k">'+esc(T.pHour)+'</span><b>–</b><b>–</b></div>';
    h+='</div></header><div class="v10r-grid">';
    h+='<section class="v10r-card"><p class="v10r-type">【'+esc(L.types[r.level])+'】</p><p class="v10r-p">'+esc(v.strong?L.typeStrong:L.typeWeak)+'</p><p class="v9-label" style="margin:22px 0 0">'+esc(L.wheelH)+'</p>'+wheel(r,L,T);
    var season=SEASON[r.pillars[1].branch],tips=[];
    if(season==='summer')tips.push(L.summer); if(season==='winter')tips.push(L.winter);
    var miss=['wood','fire','earth','metal','water'].filter(function(k){return r.pct[k]===0;});
    var mf=miss.filter(function(k){return v.fav.indexOf(k)>-1;}),mo=miss.filter(function(k){return v.fav.indexOf(k)<0;});
    if(mf.length)tips.push(f(L.missFav,{list:mf.map(N).join(L.sep)})); if(mo.length)tips.push(f(L.missOther,{list:mo.map(N).join(L.sep)}));
    if(tips.length)h+='<div class="v10r-tip"><b>'+esc(L.tipH)+'</b>'+tips.map(function(t){return '<p>'+esc(t)+'</p>';}).join('')+'</div>';
    h+='</section><section class="v10r-card">';
    h+='<div class="v10r-head"><h4>'+esc(L.favH)+'</h4><span class="v10r-tag on">'+esc(L.favTag)+' · '+v.fav.map(function(k){return CH[k];}).join(' ')+'</span></div>';
    h+='<div class="v10r-lucky"><div><p>'+esc(L.rows.color)+'</p><div class="sw">'+v.fav.map(function(k){return '<span title="'+esc(L.colors[k])+'"><i style="background:'+SWATCH[k]+'"></i>'+esc(L.colors[k])+'</span>';}).join('')+'</div></div>';
    h+='<div><p>'+esc(L.rows.dir)+'</p><div class="pl">'+v.fav.map(function(k){return '<span>'+esc(L.dirs[k])+'</span>';}).join('')+'</div></div>';
    h+='<div><p>'+esc(L.rows.num)+'</p><div class="pl">'+v.fav.map(function(k){return NUMS[k].map(function(n){return '<span>'+n+'</span>';}).join('');}).join('')+'</div></div></div>';
    h+='<ul class="v10r-list">'+v.fav.map(function(k){return '<li><span class="d" style="background:'+COLOR[k]+'">'+CH[k]+'</span><div><b>'+NM(k)+'</b><p>'+esc(L.fav[v.role[k]])+'</p><small>'+esc(L.rows.mat)+'：'+esc(L.mat[k])+'</small></div></li>';}).join('')+'</ul>';
    h+='<div class="v10r-head" style="margin-top:30px"><h4>'+esc(L.avoidH)+'</h4><span class="v10r-tag">'+esc(L.avoidTag)+' · '+v.avoid.map(function(k){return CH[k];}).join(' ')+'</span></div>';
    h+='<ul class="v10r-list muted">'+v.avoid.map(function(k){return '<li><span class="d" style="border-color:'+COLOR[k]+';color:'+COLOR[k]+'">'+CH[k]+'</span><div><b>'+NM(k)+'</b><p>'+esc(L.avoid[v.role[k]])+'</p></div></li>';}).join('')+'</ul>';
    h+='</section></div>';
    var recs=[];v.fav.slice(0,2).forEach(function(k){(P[k]||[]).forEach(function(p){recs.push(p);});});
    if(recs.length){h+='<section class="v10r-recs"><p class="v9-label">'+esc(T.recH)+'</p><div class="v9-recs">';
      recs.forEach(function(p){h+='<a class="v9-rec" href="'+esc(p.url)+'"><span class="v9-square"><img src="'+esc(p.img)+'" alt="'+esc(p.title)+'" loading="lazy"></span><span class="t"><b>'+esc(p.title)+'</b><span>'+esc(p.price)+'</span><span style="color:var(--v9-ink);font-size:14px">'+esc(T.see)+'</span></span></a>';});
      h+='</div></section>';}
    h+='<p class="v9-note">'+esc(T.note)+'</p></div>';
    return h;
  };
})();
'''

CSS = '''
.v9-result:has(.v10r){display:block}
.v10r{display:grid;gap:22px}
.v10r-hero{text-align:center;padding:36px 20px 30px;background:var(--v9-paper);border:1px solid var(--v9-line)}
.v10r-hero h3{margin:8px 0 0;font-family:var(--v9-serif);font-weight:400;font-size:clamp(28px,3.4vw,38px)}
.v10r-dm{margin:10px 0 0;font-size:15px;color:var(--v9-muted)}
.v10r-pillars{display:flex;justify-content:center;gap:clamp(16px,4vw,40px);margin-top:24px}
.v10r-pillars div{display:flex;flex-direction:column;align-items:center;gap:2px}
.v10r-pillars .k{font-size:12px;color:var(--v9-muted);margin-bottom:4px}
.v10r-pillars b{font-family:var(--v9-cjk);font-weight:400;font-size:26px;line-height:1.15}.v10r-pillars .na b{color:#C9C3B6}
.v10r-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(380px,100%),1fr));gap:22px;align-items:start}
.v10r-card{background:var(--v9-paper);border:1px solid var(--v9-line);padding:28px clamp(20px,3vw,32px)}
.v10r-type{margin:0;font-family:var(--v9-serif);font-size:26px;color:var(--v9-red)}
.v10r-p{margin:10px 0 0;font-size:15px;line-height:1.8;color:var(--v9-body)}
.v10r-wheel{display:block;width:100%;max-width:420px;margin:6px auto 0;font-family:inherit}
.v10r-tip{margin-top:14px;padding:16px 18px;background:var(--v9-tint,#F3F0EA)}.v10r-tip b{font-size:13px;color:var(--v9-red)}.v10r-tip p{margin:6px 0 0;font-size:14px;line-height:1.7}
.v10r-head{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:center;gap:10px}
.v10r-head h4{margin:0;font-family:var(--v9-serif);font-weight:400;font-size:24px}
.v10r-tag{display:inline-flex;align-items:center;padding:5px 14px;border:1px solid var(--v9-line);border-radius:999px;font-family:var(--v9-cjk);font-size:14px;color:var(--v9-muted)}
.v10r-tag.on{background:var(--v9-ink);border-color:var(--v9-ink);color:#FBFAF7}
.v10r-lucky{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));margin:20px 0 6px;border-top:1px solid var(--v9-line);border-bottom:1px solid var(--v9-line)}
.v10r-lucky>div{padding:16px 6px;text-align:center}.v10r-lucky>div+div{border-left:1px solid var(--v9-line)}
.v10r-lucky p{margin:0 0 10px;font-size:12px;color:var(--v9-muted);letter-spacing:.04em}
.v10r-lucky .sw,.v10r-lucky .pl{display:flex;flex-wrap:wrap;justify-content:center;gap:8px}
.v10r-lucky .sw span{display:flex;flex-direction:column;align-items:center;gap:4px;font-size:11px;color:var(--v9-muted)}
.v10r-lucky .sw i{display:block;width:26px;height:26px;border-radius:50%;border:1px solid rgba(0,0,0,.08)}
.v10r-lucky .pl span{padding:3px 10px;border:1px solid #E3C9BF;color:var(--v9-red);font-size:13px;border-radius:4px;background:#FBF5F2}
.v10r-list{list-style:none;margin:16px 0 0;padding:0}
.v10r-list li{display:flex;gap:14px;align-items:flex-start;padding:14px 0;border-top:1px solid var(--v9-line)}.v10r-list li:first-child{border-top:0}
.v10r-list .d{flex:0 0 auto;display:inline-flex;width:38px;height:38px;border-radius:50%;align-items:center;justify-content:center;color:#FBFAF7;font-family:var(--v9-cjk);font-size:18px;border:1.5px solid transparent}
.v10r-list.muted .d{background:transparent}
.v10r-list b{font-family:var(--v9-serif);font-weight:400;font-size:15px}
.v10r-list p{margin:2px 0 0;font-size:14px;line-height:1.7;color:var(--v9-ink)}
.v10r-list small{display:block;margin-top:6px;font-size:12px;color:var(--v9-muted)}
.v10r-recs{margin-top:6px}
'''
