/* CATHORA v9 */
(function () {
  'use strict';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  // mobile menu
  $$('[data-v9-burger]').forEach(function (b) {
    b.addEventListener('click', function () {
      var m = $('#v9-mobile'); if (!m) return;
      var open = m.hasAttribute('data-open');
      if (open) m.removeAttribute('data-open'); else m.setAttribute('data-open', '');
      b.setAttribute('aria-expanded', open ? 'false' : 'true');
    });
  });

  // localization selects submit on change
  $$('.v9-loc select').forEach(function (s) {
    s.addEventListener('change', function () { s.form.submit(); });
  });

  // product gallery
  $$('[data-v9-gallery]').forEach(function (g) {
    var main = $('.v9-main', g);
    $$('[data-v9-thumb]', g).forEach(function (t) {
      t.addEventListener('click', function () {
        main.src = t.getAttribute('data-src');
        main.removeAttribute('srcset');
        $$('[data-v9-thumb]', g).forEach(function (x) { x.setAttribute('aria-current', x === t ? 'true' : 'false'); });
      });
    });
  });

  // quantity
  $$('[data-v9-qty]').forEach(function (q) {
    var input = $('input', q);
    $$('button', q).forEach(function (b) {
      b.addEventListener('click', function () {
        var v = parseInt(input.value, 10) || 1;
        v = b.hasAttribute('data-inc') ? v + 1 : Math.max(1, v - 1);
        input.value = v;
      });
    });
  });

  // variant price update
  $$('[data-v9-variant]').forEach(function (sel) {
    var form = sel.form;
    var data = {};
    try { JSON.parse($('[data-v9-variants]', form.parentNode).textContent).forEach(function (v) { data[v.id] = v; }); } catch (e) {}
    sel.addEventListener('change', function () {
      var v = data[sel.value], btn = $('[data-v9-add]', form), price = $('[data-v9-price]');
      if (!v) return;
      if (price && sel.options[sel.selectedIndex].getAttribute('data-price')) price.textContent = sel.options[sel.selectedIndex].getAttribute('data-price');
      if (btn) { btn.disabled = !v.available; btn.textContent = v.available ? btn.getAttribute('data-label') : btn.getAttribute('data-sold'); }
    });
  });

  // ajax add to cart
  $$('form.v9-buy-form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      if (!window.fetch) return;
      e.preventDefault();
      var btn = $('[data-v9-add]', form), label = btn.getAttribute('data-label');
      btn.disabled = true; btn.textContent = btn.getAttribute('data-adding');
      var root = (window.Shopify && Shopify.routes && Shopify.routes.root) || '/';
      fetch(root + 'cart/add.js', { method: 'POST', headers: { 'Accept': 'application/json' }, body: new FormData(form) })
        .then(function (r) { if (!r.ok) throw r; return fetch(root + 'cart.js'); })
        .then(function (r) { return r.json(); })
        .then(function (cart) {
          $$('[data-v9-count]').forEach(function (c) { c.textContent = cart.item_count; });
          btn.textContent = btn.getAttribute('data-added');
          setTimeout(function () { btn.disabled = false; btn.textContent = label; }, 2400);
        })
        .catch(function () { form.classList.remove('v9-buy-form'); HTMLFormElement.prototype.submit.call(form); });
    });
  });

  // ---------- Five Elements reading ----------
// Four Pillars (BaZi) from a Gregorian birth date/time, with element balance,
// day-master strength and favourable elements. Plain ES5 so it can sit inside a DC component.
function baziCompute(y, m, d, hh, mm, tzOffsetMin) {
  var STEMS = '甲乙丙丁戊己庚辛壬癸', BR = '子丑寅卯辰巳午未申酉戌亥';
  var SE = ['wood', 'wood', 'fire', 'fire', 'earth', 'earth', 'metal', 'metal', 'water', 'water'];
  var HID = { '子': ['癸'], '丑': ['己', '癸', '辛'], '寅': ['甲', '丙', '戊'], '卯': ['乙'], '辰': ['戊', '乙', '癸'], '巳': ['丙', '戊', '庚'],
    '午': ['丁', '己'], '未': ['己', '丁', '乙'], '申': ['庚', '壬', '戊'], '酉': ['辛'], '戌': ['戊', '辛', '丁'], '亥': ['壬', '甲'] };
  var W = { 1: [1], 2: [0.7, 0.3], 3: [0.6, 0.3, 0.1] };
  var hasTime = hh !== null && hh !== undefined && !isNaN(hh);
  var H = hasTime ? hh : 12, MI = hasTime ? (mm || 0) : 0;
  // moment in UTC -> Julian Day
  var utcMs = Date.UTC(y, m - 1, d, H, MI) - (tzOffsetMin || 0) * 60000;
  var jd = utcMs / 86400000 + 2440587.5;
  var T = (jd - 2451545.0) / 36525;
  var rad = Math.PI / 180;
  var L0 = 280.46646 + 36000.76983 * T + 0.0003032 * T * T;
  var M = 357.52911 + 35999.05029 * T - 0.0001537 * T * T;
  var C = (1.914602 - 0.004817 * T - 0.000014 * T * T) * Math.sin(M * rad) + (0.019993 - 0.000101 * T) * Math.sin(2 * M * rad) + 0.000289 * Math.sin(3 * M * rad);
  var lam = L0 + C - 0.00569 - 0.00478 * Math.sin((125.04 - 1934.136 * T) * rad);
  lam = ((lam % 360) + 360) % 360;
  // year pillar (changes at Lichun, solar longitude 315)
  var yy = y;
  if (m <= 2 && lam >= 270 && lam < 315) yy = y - 1;
  var ys = ((yy - 4) % 10 + 10) % 10, yb = ((yy - 4) % 12 + 12) % 12;
  // month pillar
  var mi = Math.floor((((lam - 315) % 360) + 360) % 360 / 30); // 0 = Yin (Tiger) month
  var mb = (mi + 2) % 12, ms = ((ys % 5) * 2 + 2 + mi) % 10;
  // day pillar (civil date; 23:00 starts the next day)
  var dd = d, dm_ = m, dy = y;
  function jdn(Y, Mo, D) { var a = Math.floor((14 - Mo) / 12), y2 = Y + 4800 - a, m2 = Mo + 12 * a - 3; return D + Math.floor((153 * m2 + 2) / 5) + 365 * y2 + Math.floor(y2 / 4) - Math.floor(y2 / 100) + Math.floor(y2 / 400) - 32045; }
  var J = jdn(dy, dm_, dd) + (hasTime && hh >= 23 ? 1 : 0);
  var di = (((J - 2415021 + 10) % 60) + 60) % 60;
  var ds = di % 10, db = di % 12;
  var pillars = [{ k: 'year', s: ys, b: yb }, { k: 'month', s: ms, b: mb }, { k: 'day', s: ds, b: db }];
  if (hasTime) { var hb = Math.floor((hh + 1) / 2) % 12; pillars.push({ k: 'hour', s: ((ds % 5) * 2 + hb) % 10, b: hb }); }
  // element scores
  var score = { wood: 0, fire: 0, earth: 0, metal: 0, water: 0 };
  pillars.forEach(function (p) {
    score[SE[p.s]] += 1;
    var hs = HID[BR.charAt(p.b)], w = W[hs.length], f = p.k === 'month' ? 2 : 1;
    hs.forEach(function (h, i) { score[SE[STEMS.indexOf(h)]] += w[i] * f; });
  });
  var gen = { wood: 'fire', fire: 'earth', earth: 'metal', metal: 'water', water: 'wood' };
  var ctl = { wood: 'earth', earth: 'water', water: 'fire', fire: 'metal', metal: 'wood' };
  var dmE = SE[ds], res, off;
  for (var e in gen) { if (gen[e] === dmE) res = e; if (ctl[e] === dmE) off = e; }
  var out = gen[dmE], wea = ctl[dmE];
  var total = 0; for (var e2 in score) total += score[e2];
  var ratio = (score[dmE] + score[res]) / total;
  var level = ratio >= 0.62 ? 'strong' : ratio >= 0.5 ? 'slightlyStrong' : ratio >= 0.38 ? 'slightlyWeak' : 'weak';
  var fav;
  if (ratio >= 0.5) {
    fav = [out, wea, off].sort(function (a, b) { return score[a] - score[b]; }).slice(0, 2);
  } else {
    fav = score[res] <= score[dmE] ? [res, dmE] : [res, dmE];
  }
  var pct = {}; for (var e3 in score) pct[e3] = Math.round(score[e3] / total * 100);
  return {
    pillars: pillars.map(function (p) { return { k: p.k, stem: STEMS.charAt(p.s), branch: BR.charAt(p.b), stemEl: SE[p.s], branchEl: SE[STEMS.indexOf(HID[BR.charAt(p.b)][0])] }; }),
    dayStem: STEMS.charAt(ds), dayIndex: ds, dayEl: dmE, yang: ds % 2 === 0,
    score: score, pct: pct, ratio: Math.round(ratio * 100), level: level, favorable: fav,
    resource: res, output: out, wealth: wea, officer: off, solarLongitude: lam, hasTime: hasTime
  };
}

  var app = $('[data-v9-elements]');
  if (!app) return;
  var T = JSON.parse($('#v9-el-i18n').textContent);
  var P = JSON.parse($('#v9-el-pieces').textContent);
  var COLOR = { wood: '#56634A', fire: '#9E3B2C', earth: '#8C6A43', metal: '#6E6C66', water: '#2F3B45' };
  var CH = { wood: '木', fire: '火', earth: '土', metal: '金', water: '水' };
  var ORDER = ['wood', 'fire', 'earth', 'metal', 'water'];
  var esc = function (s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };

  function selectTab(key, scroll) {
    $$('[data-v9-tab]').forEach(function (t) {
      var on = t.getAttribute('data-v9-tab') === key, c = COLOR[t.getAttribute('data-v9-tab')];
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.style.background = on ? c : 'transparent'; t.style.color = on ? '#FBFAF7' : c; t.style.borderColor = c;
    });
    $$('[data-v9-panel]').forEach(function (p) { p.hidden = p.getAttribute('data-v9-panel') !== key; });
    if (scroll) { var s = $('#v9-explore'); if (s) s.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
  }
  $$('[data-v9-tab]').forEach(function (t) { t.addEventListener('click', function () { selectTab(t.getAttribute('data-v9-tab')); }); });
  var hash = (location.hash || '').replace('#', '');
  selectTab(COLOR[hash] ? hash : 'fire', !!COLOR[hash]);

  var form = $('#v9-calc-form'), err = $('#v9-calc-err'), out = $('#v9-result');
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var v = $('#v9-date').value, m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(v || '');
    var Y = m ? +m[1] : 0;
    if (!m || Y < 1850 || Y > 2100) { err.hidden = false; out.hidden = true; return; }
    err.hidden = true;
    var Mo = +m[2], D = +m[3], hh = null, mi = null, tm = /^(\d{2}):(\d{2})/.exec($('#v9-time').value || '');
    if (tm) { hh = +tm[1]; mi = +tm[2]; }
    var tz = -new Date(Y, Mo - 1, D, hh === null ? 12 : hh, mi || 0).getTimezoneOffset();
    render(baziCompute(Y, Mo, D, hh, mi, tz));
  });

  function dot(c, size, ch) {
    return '<span class="v9-dot" aria-hidden="true" style="width:' + size + 'px;height:' + size + 'px;background:' + c + ';font-size:' + Math.round(size * .44) + 'px">' + ch + '</span>';
  }
  function render(r) { if (window.v10Fav) window.v10Fav(r); if (window.v10Render) { var hx = window.v10Render(r, T, P); if (hx) { out.innerHTML = hx; out.hidden = false; selectTab(r.favorable[0]); out.scrollIntoView({ behavior: 'smooth', block: 'start' }); return; } }
    var labels = { year: T.pYear, month: T.pMonth, day: T.pDay, hour: T.pHour };
    var h = '<div><p class="v9-label">' + esc(T.pillarsH) + '</p><div class="v9-pillars">';
    r.pillars.forEach(function (p) {
      h += '<div class="v9-pillar"><span class="k">' + esc(labels[p.k]) + '</span><span class="g" style="color:' + COLOR[p.stemEl] + '">' + p.stem + '</span><span class="g" style="color:' + COLOR[p.branchEl] + '">' + p.branch + '</span><span class="e">' + esc(T.el[p.stemEl]) + ' · ' + esc(T.el[p.branchEl]) + '</span></div>';
    });
    if (!r.hasTime) h += '<div class="v9-pillar"><span class="k">' + esc(T.pHour) + '</span><span class="g" style="color:#B8B4AA">–</span><span class="g" style="color:#B8B4AA">–</span><span class="e">' + esc(T.noHour) + '</span></div>';
    h += '</div><div class="v9-dm">' + dot(COLOR[r.dayEl], 84, r.dayStem) + '<div><p class="v9-label" style="margin:0">' + esc(T.dmH) + '</p><p style="margin:6px 0 0;font-family:var(--v9-serif);font-size:26px">' + esc(T.dm['s' + r.dayIndex]) + '</p><p style="margin:6px 0 0;font-size:13px;line-height:1.6;color:var(--v9-muted)">' + esc(T.dmNote) + '</p></div></div>';
    h += '<div style="margin-top:32px"><div style="display:flex;justify-content:space-between;align-items:baseline;gap:12px"><p class="v9-label" style="margin:0">' + esc(T.strengthH) + '</p><p style="margin:0;font-family:var(--v9-serif);font-size:22px">' + esc(T.levels[r.level]) + '</p></div><div class="v9-bar"><span style="width:' + r.ratio + '%;background:' + COLOR[r.dayEl] + '"></span><i></i></div></div></div>';
    h += '<div><p class="v9-label">' + esc(T.balanceH) + '</p>';
    ORDER.forEach(function (k) {
      h += '<div class="v9-bal"><b>' + esc(T.el[k]) + '</b><span class="t"><span style="width:' + Math.max(2, r.pct[k]) + '%;background:' + COLOR[k] + '"></span></span><em>' + r.pct[k] + '%</em></div>';
    });
    h += '<p class="v9-label" style="margin-top:36px">' + esc(T.favH) + '</p><div class="v9-favs">';
    r.favorable.forEach(function (k, i) {
      var c = COLOR[k];
      h += '<span class="v9-fav" style="border-color:' + c + ';background:' + (i === 0 ? c : 'transparent') + ';color:' + (i === 0 ? '#FBFAF7' : c) + '"><span class="z">' + CH[k] + '</span><span class="n">' + esc(T.el[k]) + '</span><span class="r">' + esc(i === 0 ? T.favPrimary : T.favSecondary) + '</span></span>';
    });
    h += '</div><p style="margin:14px 0 0;font-size:14px;line-height:1.7;color:var(--v9-body)">' + esc(r.ratio >= 50 ? T.favStrong : T.favWeak) + '</p></div>';
    h += (window.v10Reading ? window.v10Reading(r, T) : '');
    var recs = [];
    r.favorable.forEach(function (k) { (P[k] || []).forEach(function (p) { recs.push(p); }); });
    h += '<div style="grid-column:1/-1"><p class="v9-label">' + esc(T.recH) + '</p><div class="v9-recs">';
    recs.forEach(function (p) {
      h += '<a class="v9-rec" href="' + esc(p.url) + '"><span class="v9-square"><img src="' + esc(p.img) + '" alt="' + esc(p.title) + '" loading="lazy"></span><span class="t"><b>' + esc(p.title) + '</b><span>' + esc(p.price) + '</span><span style="color:var(--v9-ink);font-size:14px">' + esc(T.see) + '</span></span></a>';
    });
    h += '</div><p class="v9-note">' + esc(T.note) + '</p></div>';
    out.innerHTML = h; out.hidden = false;
    selectTab(r.favorable[0]);
    out.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
})();























/* v10 carousel */
(function(){document.querySelectorAll('[data-v10-carousel]').forEach(function(c){var tr=c.querySelector('[data-v10-track]');if(!tr)return;var step=function(d){var s=tr.querySelector('.v10-slide');var wdt=s?s.getBoundingClientRect().width+20:300;tr.scrollBy({left:d*wdt,behavior:'smooth'});};var p=c.querySelector('[data-v10-prev]'),n=c.querySelector('[data-v10-next]');if(p)p.addEventListener('click',function(){step(-1)});if(n)n.addEventListener('click',function(){step(1)});});})();

/* v10 reading */
(function(){
  var GEN={wood:'fire',fire:'earth',earth:'metal',metal:'water',water:'wood'}, CTL={wood:'earth',earth:'water',water:'fire',fire:'metal',metal:'wood'};
  var COLOR={wood:'#56634A',fire:'#9E3B2C',earth:'#8C6A43',metal:'#6E6C66',water:'#2F3B45'}, CH={wood:'木',fire:'火',earth:'土',metal:'金',water:'水'};
  var SWATCH={wood:'#5F8A5B',fire:'#C4523A',earth:'#D2AE5A',metal:'#F3F0E8',water:'#2C4A66'};
  var NUMS={wood:[3,8],fire:[2,7],earth:[5,10],metal:[4,9],water:[1,6]};
  var SEASON={'寅':'spring','卯':'spring','辰':'spring','巳':'summer','午':'summer','未':'summer','申':'autumn','酉':'autumn','戌':'autumn','亥':'winter','子':'winter','丑':'winter'};
  var WHEEL=['fire','earth','metal','water','wood'];
  function f(s,o){return String(s).replace(/\{(\w+)\}/g,function(m,k){return o[k]!==undefined?o[k]:m;});}
  function un(s){return String(s).replace(/&#39;/g,"'").replace(/&quot;/g,'"').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&amp;/g,'&');}
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
    var L=JSON.parse(node.textContent),v=r.v10,N=function(k){return T.el[k];},NM=function(k){var ro=L.roles[r.v10.role[k]];return esc((N(k)===CH[k]?'':N(k)+' · ')+(ro[0]||ro[1]));};
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
    h+='<ul class="v10r-list">'+v.fav.map(function(k){return '<li><span class="d" style="background:'+COLOR[k]+'">'+CH[k]+'</span><div><b>'+NM(k)+'</b><p>'+esc(L.fav[v.role[k]])+'</p><small>'+esc(L.rows.mat)+esc(L.colon)+esc(un(L.mat[k]))+'</small></div></li>';}).join('')+'</ul>';
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
