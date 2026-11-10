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
  function render(r) { if (window.v10Fav) window.v10Fav(r);
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
