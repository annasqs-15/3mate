from pathlib import Path

ROOT = Path('/home/ubuntu/3mate')
source = ROOT / 'experiment.base.html'
s = source.read_text()

css = r'''<style>
:root{
  --bg:#242321;
  --bg-deep:#1d1c1a;
  --surface:#302f2c;
  --surface-2:#3a3936;
  --surface-3:#45433f;
  --board-light:#eeeed2;
  --board-dark:#769656;
  --board-light-shadow:#dedebf;
  --accent:#f6c945;
  --accent-strong:#ffd84d;
  --accent-ink:#2b250d;
  --ink:#f5f5f4;
  --muted:#aaa9a5;
  --muted-2:#84827d;
  --good:#8bc34a;
  --good-ink:#17210c;
  --bad:#e56a5d;
  --bad-ink:#2b100d;
  --line:rgba(255,255,255,.09);
  --line-strong:rgba(255,255,255,.16);
  --shadow-soft:0 14px 32px rgba(0,0,0,.24);
  --shadow-board:0 24px 50px rgba(0,0,0,.32),0 0 0 1px rgba(255,255,255,.05);
  --radius:18px;
  --radius-sm:12px;
  --font-sans:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  --font-display:"Fredoka",Inter,ui-sans-serif,system-ui,sans-serif;
  --ease-out:cubic-bezier(.22,1,.36,1);
}
*{box-sizing:border-box}
html,body{min-height:100%;margin:0;background:var(--bg-deep)}
body{
  color:var(--ink);font-family:var(--font-sans);-webkit-font-smoothing:antialiased;
  user-select:none;overscroll-behavior:none;-webkit-tap-highlight-color:transparent;
  background:radial-gradient(900px 560px at 50% -14%,rgba(83,79,65,.36),transparent 68%),linear-gradient(180deg,#2b2a27 0%,var(--bg-deep) 72%);
}
button,input{font:inherit} button{border:0;cursor:pointer;color:inherit}
button:focus-visible,input:focus-visible{outline:3px solid rgba(246,201,69,.55);outline-offset:3px}
#app{width:min(100%,1220px);margin:0 auto;padding:18px 18px calc(34px + env(safe-area-inset-bottom))}
.topbar{display:flex;align-items:center;justify-content:space-between;gap:16px;min-height:58px;margin-bottom:18px}
.brand{display:flex;align-items:center;gap:12px;min-width:0}
.brand-mark{width:38px;height:38px;border-radius:12px;display:grid;place-items:center;background:linear-gradient(145deg,#ffe17a,#e5a82d);color:#3b2b0d;box-shadow:inset 0 1px 0 rgba(255,255,255,.55),0 8px 18px rgba(0,0,0,.2);font-family:var(--font-display);font-size:20px;font-weight:700}
.brand-name{font-family:var(--font-display);font-size:25px;line-height:1;font-weight:650;letter-spacing:-.03em}
.brand-sub{margin-top:5px;color:var(--muted);font-size:11px;letter-spacing:.1em;text-transform:uppercase;font-weight:700}
.top-actions{display:flex;align-items:center;gap:8px}.top-action{min-height:40px;padding:0 12px;border-radius:12px;background:rgba(255,255,255,.06);color:var(--muted);font-size:12px;font-weight:750;transition:background .18s,color .18s,transform .18s}
.top-action:hover{background:rgba(255,255,255,.1);color:var(--ink)}.top-action:active{transform:translateY(1px)}
.top-action.icon-only{width:40px;padding:0;display:grid;place-items:center}.top-action svg{width:18px;height:18px}
.rating-pill{display:flex;align-items:center;gap:7px;padding:8px 12px;border-radius:12px;background:linear-gradient(145deg,rgba(255,255,255,.1),rgba(255,255,255,.045));border:1px solid var(--line);box-shadow:inset 0 1px 0 rgba(255,255,255,.06)}
.rating-pill .rating-label{color:var(--muted-2);font-size:9px;letter-spacing:.1em;font-weight:800}.rating-pill strong{font-size:16px;color:var(--accent)}
.rating-delta{font-size:12px;font-weight:800;opacity:0;transform:translateY(4px);transition:.2s}.rating-delta.show{opacity:1;transform:none}.rating-delta.pos{color:var(--good)}.rating-delta.neg{color:var(--bad)}.rating-pill.pulse{animation:ratingPulse .65s var(--ease-out)}
@keyframes ratingPulse{45%{transform:scale(1.05);box-shadow:0 0 0 7px rgba(246,201,69,.08)}}
#mainArea{width:100%}.trainer-shell{display:grid;grid-template-columns:minmax(0,1fr) minmax(290px,360px);gap:22px;align-items:start}
.play-column{min-width:0}.side-column{display:flex;flex-direction:column;gap:14px}
.puzzle-head{display:flex;align-items:flex-start;justify-content:space-between;gap:12px;margin:2px 0 13px;padding:0 2px}
.puzzle-eyebrow{color:var(--accent);font-size:11px;font-weight:850;letter-spacing:.12em;text-transform:uppercase}.puzzle-title{margin-top:5px;font-family:var(--font-display);font-size:26px;line-height:1.1;letter-spacing:-.025em}.puzzle-subtitle{margin:7px 0 0;color:var(--muted);font-size:13px;line-height:1.4}
.puzzle-stage-chip,.meta-chip{padding:8px 10px;border-radius:999px;background:rgba(246,201,69,.11);border:1px solid rgba(246,201,69,.18);color:var(--accent);font-size:11px;font-weight:800;white-space:nowrap}
.board-wrap{position:relative;width:min(100%,680px);margin:0 auto;border-radius:12px;box-shadow:var(--shadow-board);transition:box-shadow .25s,transform .25s}.board{position:relative;width:100%;aspect-ratio:1;overflow:hidden;border-radius:10px;background:var(--board-dark);touch-action:none;isolation:isolate}
.squares-grid{position:absolute;inset:0;display:grid;grid-template-columns:repeat(8,1fr);grid-template-rows:repeat(8,1fr)}
.sq{position:relative;display:flex;align-items:center;justify-content:center;overflow:hidden;transition:filter .16s,box-shadow .16s}.sq.light{background:linear-gradient(145deg,var(--board-light),var(--board-light-shadow))}.sq.dark{background:linear-gradient(145deg,#7d9d5c,var(--board-dark))}
.sq.last-from,.sq.last-to{box-shadow:inset 0 0 0 999px rgba(246,201,69,.34)}.sq.flash-good{box-shadow:inset 0 0 0 999px rgba(139,195,74,.38)}.sq.sel{box-shadow:inset 0 0 0 999px rgba(246,201,69,.5)}.sq.check-glow{box-shadow:inset 0 0 0 999px rgba(229,106,93,.62)}
.coord{position:absolute;z-index:1;font-size:clamp(8px,1.5vw,12px);font-weight:800;line-height:1;text-shadow:0 1px 1px rgba(0,0,0,.12)}.coord.rank{top:5px;left:5px}.coord.file{right:5px;bottom:4px;text-transform:lowercase}.sq.light .coord{color:rgba(118,150,86,.8)}.sq.dark .coord{color:rgba(238,238,210,.72)}
#pieceLayer,#moveBadgeLayer{position:absolute;inset:0;z-index:3;pointer-events:none}.piece{position:absolute;width:12.5%;height:12.5%;display:grid;place-items:center;transition:left .28s var(--ease-out),top .28s var(--ease-out),transform .18s var(--ease-out),filter .18s;will-change:left,top;pointer-events:auto;z-index:3}.piece svg{width:91%;height:91%;display:block;filter:drop-shadow(0 5px 3px rgba(0,0,0,.3))}.piece.lifted{transform:translateY(-5%) scale(1.06);filter:drop-shadow(0 9px 4px rgba(0,0,0,.28))}.piece.dragging{transition:none;z-index:9;transform:scale(1.1);filter:drop-shadow(0 12px 8px rgba(0,0,0,.35))}.piece.pop-in{animation:pieceIn .25s var(--ease-out)}.piece.vanish{animation:pieceOut .23s var(--ease-out) forwards}.piece-ghost{opacity:.16;filter:none;z-index:2}.piece.soft-pop,.piece.tap-bounce{animation:piecePop .34s var(--ease-out)}
@keyframes pieceIn{from{opacity:0;transform:scale(.72)}to{opacity:1;transform:scale(1)}}@keyframes pieceOut{to{opacity:0;transform:scale(.6)}}@keyframes piecePop{45%{transform:scale(1.08)}}
.dot,.ring{position:absolute;z-index:4;pointer-events:none}.dot{width:22%;height:22%;border-radius:50%;background:rgba(36,35,33,.28);box-shadow:0 1px 2px rgba(0,0,0,.14)}.ring{inset:13%;border-radius:50%;border:5px solid rgba(36,35,33,.26)}
.board-shroud{position:absolute;inset:0;display:none;background:rgba(21,20,18,.44);z-index:10}.board-shroud.show{display:block}.promo-row{position:absolute;z-index:20;display:flex;gap:7px;padding:10px;border-radius:15px;background:rgba(48,47,44,.96);box-shadow:var(--shadow-soft)}.promo-choice{width:58px;height:58px;border-radius:10px;background:var(--surface-2);display:grid;place-items:center}.promo-choice:hover{background:var(--surface-3)}.promo-choice svg{width:48px;height:48px}
.move-quality-badge{position:absolute;width:18%;height:18%;z-index:8;transition:opacity .3s;pointer-events:none}.move-quality-badge svg,.move-quality-badge img{width:100%;height:100%;object-fit:contain}.move-quality-badge.brilliant{animation:badgeIn .45s var(--ease-out)}.move-quality-badge.best{animation:badgeIn .38s var(--ease-out)}.move-quality-badge.leaving{opacity:0}.board-wrap.puzzle-enter{animation:boardEnter .42s var(--ease-out)}.board-wrap.success-glow{box-shadow:0 0 0 3px rgba(139,195,74,.55),0 24px 50px rgba(0,0,0,.35)}.board-wrap.fail-glow{box-shadow:0 0 0 3px rgba(229,106,93,.55),0 24px 50px rgba(0,0,0,.35)}.board.shake{animation:shake .32s ease-out}@keyframes badgeIn{from{opacity:0;transform:scale(.4) translateY(8%)}70%{transform:scale(1.1)}to{opacity:1;transform:scale(1)}}@keyframes boardEnter{from{opacity:.35;transform:translateY(8px) scale(.985)}to{opacity:1;transform:none}}@keyframes shake{25%{transform:translateX(-6px)}50%{transform:translateX(6px)}75%{transform:translateX(-3px)}}
.status-card,.score-card,.tool-card,.result-card{border:1px solid var(--line);border-radius:var(--radius);background:linear-gradient(145deg,rgba(58,57,54,.96),rgba(45,44,41,.96));box-shadow:var(--shadow-soft)}.status-card{padding:18px}.status-row{display:flex;align-items:center;gap:9px;color:var(--muted);font-size:13px}.turn-dot{width:9px;height:9px;border-radius:50%;display:inline-block;background:var(--accent);box-shadow:0 0 0 4px rgba(246,201,69,.12)}.turn-dot.b{background:#d8d8d3;box-shadow:0 0 0 4px rgba(255,255,255,.1)}
.score-card{padding:15px 16px}.score-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.metric-label{color:var(--muted-2);font-size:10px;font-weight:800;letter-spacing:.08em;text-transform:uppercase}.metric-value{margin-top:4px;font-size:20px;font-weight:800;letter-spacing:-.03em}.metric-value.accent{color:var(--accent)}.metric-value.good{color:var(--good)}.metric-value.bad{color:var(--bad)}.metric-sub{margin-top:2px;color:var(--muted);font-size:11px}
.result-card{display:none;padding:17px}.result-card.show{display:block;animation:cardIn .3s var(--ease-out)}.result-card.success{border-color:rgba(139,195,74,.3)}.result-card.failure{border-color:rgba(229,106,93,.3)}.result-kicker{font-size:10px;font-weight:850;letter-spacing:.12em;text-transform:uppercase;color:var(--accent)}.result-title{margin-top:5px;font-family:var(--font-display);font-size:21px}.result-sub{margin-top:6px;color:var(--muted);font-size:13px;line-height:1.45}.result-delta{margin-top:14px;font-size:27px;font-weight:850;letter-spacing:-.04em}.result-delta.pos{color:var(--good)}.result-delta.neg{color:var(--bad)}@keyframes cardIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}
.controls-row{display:flex;gap:10px;flex-wrap:wrap;margin-top:2px}.btn{min-height:46px;border-radius:13px;padding:0 16px;display:inline-flex;align-items:center;justify-content:center;gap:8px;font-size:13px;font-weight:850;transition:transform .18s,filter .18s,background .18s;box-shadow:inset 0 1px 0 rgba(255,255,255,.15),0 5px 12px rgba(0,0,0,.13)}.btn:active{transform:translateY(2px);box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 2px 7px rgba(0,0,0,.15)}.btn svg{width:18px;height:18px}.btn-primary{flex:1;background:linear-gradient(180deg,var(--accent-strong),#eab735);color:var(--accent-ink)}.btn-primary:hover{filter:brightness(1.06)}.btn-ghost{background:var(--surface-2);color:var(--ink);border:1px solid var(--line)}.btn-ghost:hover{background:var(--surface-3)}.btn-reveal{background:rgba(229,106,93,.11);color:#f19b91;border:1px solid rgba(229,106,93,.2)}.btn-danger{background:rgba(229,106,93,.14);color:#f2a29a;border:1px solid rgba(229,106,93,.24)}.btn-sm{min-height:40px;padding:0 13px;font-size:12px}.btn[disabled]{opacity:.48;cursor:not-allowed}
.helper-note{min-height:20px;margin:2px 2px 0;color:var(--muted-2);font-size:12px;line-height:1.45}.side-card{padding:16px}.card-heading{display:flex;justify-content:space-between;align-items:center;gap:12px}.card-title{font-size:13px;font-weight:850}.card-kicker{color:var(--muted-2);font-size:10px;text-transform:uppercase;letter-spacing:.1em;font-weight:850}.stat-line{display:flex;justify-content:space-between;gap:10px;padding:11px 0;border-bottom:1px solid var(--line);font-size:12px}.stat-line:last-child{border-bottom:0;padding-bottom:0}.stat-line span:first-child{color:var(--muted)}.stat-line strong{font-size:13px}.streak-meter{margin-top:14px;height:7px;border-radius:99px;overflow:hidden;background:rgba(255,255,255,.1)}.streak-meter span{display:block;height:100%;width:0;border-radius:inherit;background:linear-gradient(90deg,#d99d2b,var(--accent-strong));transition:width .35s var(--ease-out)}
.footer-row{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-top:18px;color:var(--muted-2);font-size:11px}.icon-row{display:flex;gap:7px}.btn-icon{width:38px;height:38px;display:grid;place-items:center;border-radius:11px;background:rgba(255,255,255,.06);color:var(--muted);border:1px solid var(--line)}.btn-icon:hover{color:var(--ink);background:rgba(255,255,255,.1)}.btn-icon svg{width:18px;height:18px}
.onboard-overlay,.modal-overlay{position:fixed;inset:0;z-index:100;display:none;align-items:center;justify-content:center;padding:18px;background:rgba(15,14,13,.72);backdrop-filter:blur(12px)}.onboard-overlay{display:none}.onboard-card,.modal-card{width:min(100%,480px);border:1px solid var(--line-strong);border-radius:24px;padding:27px;background:linear-gradient(145deg,#3b3935,#292825);box-shadow:0 30px 80px rgba(0,0,0,.42)}.onboard-mark{width:54px;height:54px;display:grid;place-items:center;border-radius:17px;background:linear-gradient(145deg,#ffe17a,#e3a72b);color:#3b2b0d;font:700 27px var(--font-display);box-shadow:inset 0 1px 0 rgba(255,255,255,.6),0 12px 26px rgba(0,0,0,.22)}.onboard-title,.modal-title{margin-top:19px;font:650 29px/1.08 var(--font-display);letter-spacing:-.03em}.onboard-kicker{margin-top:9px;color:var(--accent);font-size:10px;letter-spacing:.14em;font-weight:850;text-transform:uppercase}.onboard-sub{margin:12px 0 20px;color:var(--muted);font-size:14px;line-height:1.5}.onboard-input{width:100%;height:62px;border-radius:15px;border:1px solid var(--line-strong);background:#242321;color:var(--ink);text-align:center;font-size:27px;font-weight:850;outline:none}.onboard-input:focus{border-color:rgba(246,201,69,.7);box-shadow:0 0 0 4px rgba(246,201,69,.1)}.onboard-presets{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:12px 0 18px}.preset-btn{min-height:36px;border-radius:10px;background:rgba(255,255,255,.06);color:var(--muted);font-size:11px;font-weight:750;border:1px solid transparent}.preset-btn:hover,.preset-btn.active{background:rgba(246,201,69,.14);border-color:rgba(246,201,69,.32);color:var(--accent)}.onboard-note{margin:15px 0 0;color:var(--muted-2);font-size:11px;line-height:1.4;text-align:center}.modal-overlay.show{display:flex}.modal-card{max-height:min(760px,calc(100vh - 36px));overflow:auto}.modal-head{display:flex;align-items:flex-start;justify-content:space-between;gap:16px}.modal-close{width:36px;height:36px;border-radius:10px;background:rgba(255,255,255,.07);color:var(--muted);font-size:22px;line-height:1}.modal-sub{color:var(--muted);font-size:13px;line-height:1.45;margin:10px 0 20px}.stats-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:9px}.stats-tile{padding:13px;border-radius:13px;background:rgba(255,255,255,.055);border:1px solid var(--line)}.stats-tile .metric-value{font-size:22px}.settings-row{display:flex;justify-content:space-between;align-items:center;gap:14px;padding:14px 0;border-bottom:1px solid var(--line);font-size:13px}.settings-row small{display:block;margin-top:4px;color:var(--muted);font-size:11px;line-height:1.35}.toggle{width:46px;height:26px;border-radius:99px;background:#57544f;padding:3px;transition:.2s}.toggle:before{content:"";display:block;width:20px;height:20px;border-radius:50%;background:#e9e8e1;transition:.2s;box-shadow:0 2px 5px rgba(0,0,0,.2)}.toggle.on{background:var(--accent)}.toggle.on:before{transform:translateX(20px);background:#3c310d}
.review-overlay{display:none!important}.daily-progress{display:none!important}.banner{display:none}.daily-hint-note{display:none}
@media (max-width:800px){#app{padding:12px 12px calc(24px + env(safe-area-inset-bottom))}.topbar{margin-bottom:12px}.brand-mark{width:34px;height:34px;border-radius:11px;font-size:18px}.brand-name{font-size:22px}.brand-sub{font-size:9px}.top-action{min-height:36px;padding:0 9px;font-size:11px}.top-action.stats-label{display:none}.rating-pill{padding:7px 9px}.rating-pill .rating-label{display:none}.trainer-shell{display:block}.side-column{margin-top:14px}.puzzle-head{margin-top:4px}.puzzle-title{font-size:22px}.status-card{padding:14px}.side-column .status-card{display:none}.score-card{padding:14px}.footer-row{margin-top:13px}}
@media (max-width:440px){.top-actions{gap:5px}.top-actions .rating-pill{display:flex}.puzzle-stage-chip{font-size:10px;padding:7px 8px}.score-grid{gap:5px}.metric-value{font-size:18px}.controls-row{gap:8px}.btn{padding:0 12px}.onboard-card,.modal-card{padding:22px}.onboard-title,.modal-title{font-size:26px}.onboard-presets{grid-template-columns:repeat(2,1fr)}}
@media (min-width:801px){.play-column{display:flex;flex-direction:column}.play-column .puzzle-head{order:0}.play-column .board-wrap{order:1}.play-column .score-card{order:2;margin:14px auto 0;width:min(100%,680px)}.play-column .controls-row{order:3;width:min(100%,680px);margin:12px auto 0}.play-column .helper-note{order:4;width:min(100%,680px);margin:8px auto 0}.side-column .result-card{order:0}.side-column .status-card{order:1}.side-column .tool-card{order:2}}
</style>'''

body = r'''<body>
<div id="onboardOverlay" class="onboard-overlay" aria-hidden="true">
  <div class="onboard-card">
    <div class="onboard-mark">3</div>
    <div class="onboard-title">Mulai latihan taktik</div>
    <div class="onboard-kicker">Puzzle tanpa batas</div>
    <p class="onboard-sub">Masukkan rating awalmu. 3mate akan menyesuaikan tingkat kesulitan puzzle dan memperbarui rating setelah setiap hasil.</p>
    <input type="number" id="onboardRatingInput" class="onboard-input" min="350" max="2400" step="10" value="1200" inputmode="numeric" aria-label="Rating puzzle awal">
    <div class="onboard-presets" id="onboardPresets">
      <button type="button" class="preset-btn" data-v="600">Pemula</button>
      <button type="button" class="preset-btn" data-v="900">Santai</button>
      <button type="button" class="preset-btn" data-v="1200">Menengah</button>
      <button type="button" class="preset-btn" data-v="1600">Klub</button>
      <button type="button" class="preset-btn" data-v="2000">Mahir</button>
      <button type="button" class="preset-btn" data-v="2200">Expert</button>
    </div>
    <button type="button" class="btn btn-primary" id="onboardStartBtn" style="width:100%">Mulai bermain</button>
    <p class="onboard-note">Rating dan progres disimpan di browser ini. Kamu dapat mengubahnya nanti dari pengaturan.</p>
  </div>
</div>
<div id="app">
  <header class="topbar">
    <div class="brand"><div class="brand-mark">3</div><div><div class="brand-name">3mate</div><div class="brand-sub">Unlimited puzzle practice</div></div></div>
    <div class="top-actions">
      <div class="rating-pill" id="ratingPill" aria-label="Puzzle Rating"><span class="rating-label">RATING</span><strong id="ratingValue">1200</strong><span class="rating-delta" id="ratingDelta"></span></div>
      <button type="button" class="top-action stats-label" id="statsBtn">Statistik</button>
      <button type="button" class="top-action icon-only" id="settingsBtn" aria-label="Pengaturan">⚙</button>
    </div>
  </header>
  <div id="mainArea"></div>
  <footer class="footer-row"><div id="puzzleCounter">Puzzle 1</div><div class="icon-row"><button class="btn-icon" id="soundBtn" title="Suara" aria-label="Toggle sound"></button><button class="btn-icon" id="flipBtn" title="Balik papan" aria-label="Flip board"></button></div></footer>
  <div class="modal-overlay" id="statsOverlay" aria-hidden="true"><section class="modal-card"><div class="modal-head"><div><div class="card-kicker">Progress</div><div class="modal-title">Statistik latihan</div></div><button class="modal-close" id="statsCloseBtn" aria-label="Tutup">×</button></div><p class="modal-sub">Ringkasan performa puzzle yang tersimpan di browser ini.</p><div class="stats-grid"><div class="stats-tile"><div class="metric-label">Rating saat ini</div><div class="metric-value accent" id="statsRating">1200</div></div><div class="stats-tile"><div class="metric-label">Rating tertinggi</div><div class="metric-value" id="statsBestRating">1200</div></div><div class="stats-tile"><div class="metric-label">Dimainkan</div><div class="metric-value" id="statsPlayed">0</div></div><div class="stats-tile"><div class="metric-label">Akurasi</div><div class="metric-value" id="statsAccuracy">—</div></div><div class="stats-tile"><div class="metric-label">Berhasil</div><div class="metric-value good" id="statsSolved">0</div></div><div class="stats-tile"><div class="metric-label">Gagal</div><div class="metric-value bad" id="statsFailed">0</div></div></div></section></div>
  <div class="modal-overlay" id="settingsOverlay" aria-hidden="true"><section class="modal-card"><div class="modal-head"><div><div class="card-kicker">Preferences</div><div class="modal-title">Pengaturan</div></div><button class="modal-close" id="settingsCloseBtn" aria-label="Tutup">×</button></div><div class="settings-row"><div><strong>Suara</strong><small>Putar efek langkah dan hasil puzzle.</small></div><button class="toggle" id="soundToggle" aria-label="Toggle sound"></button></div><div class="settings-row"><div><strong>Balik papan</strong><small>Ubah orientasi papan catur.</small></div><button class="toggle" id="flipToggle" aria-label="Flip board"></button></div><div class="settings-row"><div><strong>Reset progres</strong><small>Hapus rating dan statistik lokal.</small></div><button class="btn btn-danger btn-sm" id="resetProgressBtn">Reset</button></div></section></div>
  <div class="review-overlay" id="reviewOverlay" aria-hidden="true"><button id="reviewCloseBtn"></button><div id="reviewTabs"></div><div id="reviewBoard"></div><div id="reviewResult"></div><div id="reviewMeta"></div><button id="reviewPrevBtn"></button><button id="reviewNextMoveBtn"></button><button id="reviewNextBtn"></button><div id="reviewMoveNote"></div></div>
</div>
<script>'''

start_style = s.index('<style>')
end_style = s.index('</style>') + len('</style>')
start_body = s.index('<body>')
s = s[:start_style] + css + s[end_style:]
# body string includes opening script tag, so replace all markup between body and original script opening
start_body = s.index('<body>')
start_script = s.index('<script>', start_body)
s = s[:start_body] + body + s[start_script + len('<script>'):]

marker = '/* ---- unlimited puzzle experiment mode ----'
tail_start = s.index(marker)
script_end = s.index('</script>', tail_start)

new_tail = r'''
/* ---- unlimited puzzle trainer ----
   Endless rating-based sessions. The chess engine and puzzle dataset above remain shared.
-------------------------------------------------------------------------- */
const UNLIMITED_STORAGE_VERSION = 4;
const EXPERIMENT_LIGHT_DIRECTIONS=[
  {x:'18%',y:'18%',angle:'135deg'},{x:'50%',y:'12%',angle:'180deg'},
  {x:'82%',y:'18%',angle:'225deg'},{x:'88%',y:'50%',angle:'270deg'},
  {x:'82%',y:'82%',angle:'315deg'},{x:'50%',y:'88%',angle:'0deg'},
  {x:'18%',y:'82%',angle:'45deg'},{x:'12%',y:'50%',angle:'90deg'}
];
function chooseExperimentPieceLighting(){return EXPERIMENT_LIGHT_DIRECTIONS[Math.floor(Math.random()*EXPERIMENT_LIGHT_DIRECTIONS.length)];}
function applyExperimentPieceLighting(){return true;}
function triggerPieceBulgeAt(square){
  const pc=state.pieces.find(function(item){return item.sq===square;}), el=pc&&pieceEls.get(pc.id); if(!el) return;
  el.classList.remove('soft-pop'); void el.offsetWidth; el.classList.add('soft-pop');
  setTimeout(function(){if(el.parentNode) el.classList.remove('soft-pop');},380);
}
function ensureUnlimitedState(){
  state.stats=state.stats||{played:0,solved:0,failed:0,revealed:0,hints:0,bestRating:state.playerRating||1200,lastResult:null};
  state.stats.played=Number(state.stats.played)||0; state.stats.solved=Number(state.stats.solved)||0; state.stats.failed=Number(state.stats.failed)||0; state.stats.revealed=Number(state.stats.revealed)||0; state.stats.hints=Number(state.stats.hints)||0;
  state.stats.bestRating=Math.max(Number(state.stats.bestRating)||1200,Math.round(state.playerRating||1200));
  state.experimentPuzzleNumber=Number(state.experimentPuzzleNumber)||0;
  state.recentPuzzleIds=state.recentPuzzleIds instanceof Set?state.recentPuzzleIds:new Set(Array.isArray(state.recentPuzzleIds)?state.recentPuzzleIds.map(Number):[]);
}
function loadProgress(){
  ensureUserId(); let raw=null;
  try{if(window.storage){const res=window.storage.get('tacdchess_progress'); if(res&&typeof res.then==='function'){/* async storage is intentionally secondary */}}}catch(e){}
  raw=lsGet('tacdchess_progress'); if(!raw) return false;
  try{
    const d=JSON.parse(raw);
    const savedRating=typeof d.rating==='number'?d.rating:(typeof d.playerRating==='number'?d.playerRating:1200);
    state.playerRating=clamp(Math.round(savedRating),DAILY_MIN_RATING,DAILY_MAX_RATING);
    state.streak=Math.max(0,Math.round(Number(d.streak)||0)); state.bestStreak=Math.max(0,Math.round(Number(d.bestStreak)||0));
    state.soundOn=typeof d.soundOn==='boolean'?d.soundOn:true; state.boardFlipped=!!d.boardFlipped;
    if(typeof d.userId==='string'&&d.userId) state.userId=d.userId;
    state.experimentPuzzleNumber=Math.max(0,Math.round(Number(d.puzzleNumber)||0));
    state.recentPuzzleIds=new Set((Array.isArray(d.recentPuzzleIds)?d.recentPuzzleIds:(Array.isArray(d.playedPuzzleIds)?d.playedPuzzleIds.slice(-80):[])).map(Number).filter(Number.isFinite));
    state.playedPuzzleIds=state.recentPuzzleIds;
    state.stats={played:Math.max(0,Math.round(Number(d.stats&&d.stats.played)||0)),solved:Math.max(0,Math.round(Number(d.stats&&d.stats.solved)||0)),failed:Math.max(0,Math.round(Number(d.stats&&d.stats.failed)||0)),revealed:Math.max(0,Math.round(Number(d.stats&&d.stats.revealed)||0)),hints:Math.max(0,Math.round(Number(d.stats&&d.stats.hints)||0)),bestRating:Math.max(Number(d.stats&&d.stats.bestRating)||state.playerRating,state.playerRating),lastResult:d.stats&&d.stats.lastResult||null};
    ensureUnlimitedState(); return d.onboarded===true;
  }catch(e){ensureUnlimitedState();return false;}
}
function saveProgress(){
  ensureUnlimitedState();
  const payload=JSON.stringify({schema:UNLIMITED_STORAGE_VERSION,rating:Math.round(state.playerRating),streak:state.streak,bestStreak:state.bestStreak,soundOn:state.soundOn,boardFlipped:state.boardFlipped,onboarded:true,userId:state.userId,puzzleNumber:state.experimentPuzzleNumber,recentPuzzleIds:Array.from(state.recentPuzzleIds).slice(-180),stats:state.stats,daily:state.daily});
  try{if(window.storage&&window.storage.set) window.storage.set('tacdchess_progress',payload).catch(function(){});}catch(e){}
  lsSet('tacdchess_progress',payload);
}
function chooseExperimentPuzzle(){
  ensureUnlimitedState(); if(!PUZZLES.length) return 0;
  if(state.recentPuzzleIds.size>=Math.max(120,PUZZLES.length-1)) state.recentPuzzleIds.clear();
  const target=state.playerRating, ranges=[150,250,400]; let candidates=[];
  for(let r=0;r<ranges.length&&!candidates.length;r++){
    candidates=PUZZLES.map(function(p,i){return {i:i,d:Math.abs(p.rating-target)};}).filter(function(x){return !state.recentPuzzleIds.has(x.i)&&x.d<=ranges[r];});
  }
  if(!candidates.length) candidates=PUZZLES.map(function(p,i){return {i:i,d:Math.abs(p.rating-target)};}).filter(function(x){return !state.recentPuzzleIds.has(x.i);});
  candidates.sort(function(a,b){return a.d-b.d;}); const pool=candidates.slice(0,Math.min(24,candidates.length));
  return pool[Math.floor(Math.random()*pool.length)].i;
}
function createExperimentSession(idx){
  ensureUnlimitedState(); const p=PUZZLES[idx]; state.pieceLighting=chooseExperimentPieceLighting();
  state.daily={date:'unlimited',puzzleIds:[idx],slots:[{status:'pending',mistakes:0,hintUsed:false}],currentSlot:0,complete:false,completedAt:null,ratingBefore:state.playerRating,ratingDelta:0};
  state.currentDailySlot=0; state.currentPuzzleIndex=idx; state.currentMistakes=0; state.hintUsed=false; state.ratingDeltaToday=0; state.experimentPuzzleNumber++; state.recentPuzzleIds.add(idx); state.playedPuzzleIds=state.recentPuzzleIds; state.puzzleStartedAt=Date.now(); state.elapsedSeconds=0;
  loadPuzzleByIndex(idx,false,0); saveProgress();
}
function startExperimentPuzzle(){createExperimentSession(chooseExperimentPuzzle());}
function getExperimentRatingDelta(result){
  const p=PUZZLES[state.currentPuzzleIndex]; if(!p) return 0; let quality=0;
  if(result==='solved'){quality=state.hintUsed?0.72:1; if(state.currentMistakes>0) quality=0.5;}
  else if(result==='revealed') quality=0.25;
  else if(result==='failed') quality=0;
  const expected=1/(1+Math.pow(10,(p.rating-state.playerRating)/400));
  return clamp(Math.round(32*(quality-expected)),-40,40);
}
function completeExperimentPuzzle(result){
  if(state.status==='puzzle-complete') return; ensureUnlimitedState();
  const detail=state.daily&&state.daily.slots[0]; if(!detail) return; detail.status=result; detail.mistakes=state.currentMistakes; detail.hintUsed=state.hintUsed;
  const delta=getExperimentRatingDelta(result); state.playerRating=clamp(state.playerRating+delta,DAILY_MIN_RATING,DAILY_MAX_RATING); state.ratingDeltaToday=delta; state.daily.ratingDelta=delta; state.daily.complete=true; state.daily.completedAt=new Date().toISOString(); state.elapsedSeconds=Math.max(0,Math.round((Date.now()-(state.puzzleStartedAt||Date.now()))/1000));
  state.stats.played++; state.stats.lastResult=result; if(result==='solved') state.stats.solved++; else if(result==='failed') state.stats.failed++; else if(result==='revealed') state.stats.revealed++; if(state.hintUsed) state.stats.hints++;
  if(result==='solved'){state.streak++;state.bestStreak=Math.max(state.bestStreak,state.streak);pulseBoard('good');playSound('success');} else {state.streak=0;pulseBoard('bad');playSound('wrong');}
  state.stats.bestRating=Math.max(state.stats.bestRating,state.playerRating); state.status='puzzle-complete'; if(delta) showRatingDelta(delta); else hideRatingDelta(); saveProgress(); renderAll();
}
function completeCurrentPuzzle(result){completeExperimentPuzzle(result);}
function recordDailyMistake(){
  if(state.status!=='player-turn') return; state.currentMistakes++; showTemporaryFeedback('Langkah belum tepat'); triggerShake();
  setTimeout(function(){if(state.status==='player-turn') completeCurrentPuzzle('failed');},240); saveProgress(); renderAll();
}
function goToNextDailyPuzzle(){if(state.status==='puzzle-complete') startExperimentPuzzle();}
function retryPuzzle(){if(state.status==='player-turn') loadPuzzleByIndex(state.currentPuzzleIndex,false,0);}
function formatTimer(seconds){const m=Math.floor(seconds/60),s=String(seconds%60).padStart(2,'0');return m+':'+s;}
function updateTrainerTimer(){
  if(state.status==='player-turn'||state.status==='opponent-move'||state.status==='revealing'){state.elapsedSeconds=Math.max(0,Math.round((Date.now()-(state.puzzleStartedAt||Date.now()))/1000));const el=document.getElementById('timerValue');if(el)el.textContent=formatTimer(state.elapsedSeconds);}
}
function themeLabel(p){const key=(p.themes||[]).find(function(t){return THEME_LABELS[t]&&t!=='mate';})||((p.themes||[]).find(function(t){return THEME_LABELS[t];}));return key?THEME_LABELS[key]:'Checkmate';}
function uiIcon(name){return ICONS[name]||'';}
function buildSkeleton(){
  document.getElementById('mainArea').innerHTML='<div class="trainer-shell"><main class="play-column"><div class="puzzle-head"><div><div class="puzzle-eyebrow" id="puzzleEyebrow">YOUR MOVE</div><div class="puzzle-title" id="puzzleTitle">Find the best move</div><p class="puzzle-subtitle" id="puzzleSubtitle">Solve the position and continue the line.</p></div><div class="puzzle-stage-chip" id="difficultyChip">Rating 1200</div></div><div class="board-wrap" id="boardWrap"><div class="board" id="boardGrid"><div class="squares-grid" id="squaresGrid"></div><div id="pieceLayer"></div><div id="moveBadgeLayer"></div></div><div class="board-shroud" id="boardShroud"></div></div><section class="score-card"><div class="score-grid"><div><div class="metric-label">Puzzle</div><div class="metric-value accent" id="puzzleRating">1200</div><div class="metric-sub">difficulty</div></div><div><div class="metric-label">Time</div><div class="metric-value" id="timerValue">0:00</div><div class="metric-sub">this puzzle</div></div><div><div class="metric-label">Streak</div><div class="metric-value" id="streakMetric">0</div><div class="metric-sub">solved in a row</div></div></div></section><div class="controls-row" id="controlsRow"></div><div class="helper-note" id="dailyHintNote"></div></main><aside class="side-column"><section class="status-card"><div class="card-kicker">Position</div><div class="status-row" style="margin-top:10px"><span class="turn-dot w" id="turnDot"></span><span id="statusLabel">Your move</span></div><div class="meta-row" style="display:flex;gap:7px;flex-wrap:wrap;margin-top:14px"><span class="meta-chip" id="themeChip">Checkmate</span><span class="meta-chip" id="moveCountChip">Short line</span></div></section><section class="result-card" id="resultCard"><div class="result-kicker" id="resultKicker">RESULT</div><div class="result-title" id="resultTitle">Puzzle solved</div><div class="result-sub" id="resultSub">Ready for another puzzle.</div><div class="result-delta" id="resultDelta">+0</div><button class="btn btn-primary" style="width:100%;margin-top:15px" id="nextPuzzleBtn">Puzzle berikutnya</button></section><section class="tool-card side-card"><div class="card-heading"><div><div class="card-kicker">Practice</div><div class="card-title">Tanpa batas, sesuai rating</div></div><span style="color:var(--accent);font-size:19px">∞</span></div><p style="margin:9px 0 0;color:var(--muted);font-size:12px;line-height:1.45">Puzzle berikutnya dipilih dari ratingmu. Selesaikan tanpa bantuan untuk kenaikan rating penuh.</p><div class="streak-meter"><span id="streakMeter"></span></div></section></aside></div>';
  const board=document.getElementById('boardGrid'); board.addEventListener('pointerdown',boardPointerDown);board.addEventListener('pointermove',boardPointerMove);board.addEventListener('pointerup',boardPointerUp);board.addEventListener('pointercancel',boardPointerUp);
  document.getElementById('soundBtn').addEventListener('click',toggleSound); document.getElementById('flipBtn').addEventListener('click',function(){state.boardFlipped=!state.boardFlipped;renderSquares();renderBoard();saveProgress();});
  document.getElementById('statsBtn').addEventListener('click',openStats);document.getElementById('settingsBtn').addEventListener('click',openSettings);document.getElementById('statsCloseBtn').addEventListener('click',closeStats);document.getElementById('settingsCloseBtn').addEventListener('click',closeSettings);
  document.getElementById('soundToggle').addEventListener('click',toggleSound);document.getElementById('flipToggle').addEventListener('click',function(){state.boardFlipped=!state.boardFlipped;renderSquares();renderBoard();syncSettings();saveProgress();});document.getElementById('resetProgressBtn').addEventListener('click',resetProgress);
  document.getElementById('nextPuzzleBtn').addEventListener('click',goToNextDailyPuzzle);installKeyboardShortcuts();
}
function showOnboarding(){return new Promise(function(resolve){const overlay=document.getElementById('onboardOverlay'),input=document.getElementById('onboardRatingInput'),presets=document.getElementById('onboardPresets');overlay.style.display='flex';overlay.setAttribute('aria-hidden','false');ensureUserId();presets.querySelectorAll('.preset-btn').forEach(function(btn){btn.addEventListener('click',function(){input.value=btn.dataset.v;presets.querySelectorAll('.preset-btn').forEach(function(b){b.classList.remove('active')});btn.classList.add('active');});});input.addEventListener('input',function(){presets.querySelectorAll('.preset-btn').forEach(function(b){b.classList.toggle('active',b.dataset.v===input.value);});});document.getElementById('onboardStartBtn').addEventListener('click',function(){let v=parseInt(input.value,10);if(!Number.isFinite(v))v=1200;state.playerRating=clamp(v,DAILY_MIN_RATING,DAILY_MAX_RATING);state.stats={played:0,solved:0,failed:0,revealed:0,hints:0,bestRating:state.playerRating,lastResult:null};ensureUnlimitedState();overlay.style.display='none';overlay.setAttribute('aria-hidden','true');saveProgress();resolve();});});}
function renderStats(){ensureUnlimitedState();const total=state.stats.played,accuracy=total?Math.round(state.stats.solved/total*100)+'%':'—';const map={statsRating:Math.round(state.playerRating),statsBestRating:Math.round(state.stats.bestRating),statsPlayed:total,statsAccuracy:accuracy,statsSolved:state.stats.solved,statsFailed:state.stats.failed};Object.keys(map).forEach(function(id){const el=document.getElementById(id);if(el)el.textContent=map[id];});}
function openStats(){renderStats();const el=document.getElementById('statsOverlay');el.classList.add('show');el.setAttribute('aria-hidden','false');}function closeStats(){const el=document.getElementById('statsOverlay');el.classList.remove('show');el.setAttribute('aria-hidden','true');}
function syncSettings(){document.getElementById('soundToggle').classList.toggle('on',state.soundOn);document.getElementById('flipToggle').classList.toggle('on',state.boardFlipped);}
function openSettings(){syncSettings();const el=document.getElementById('settingsOverlay');el.classList.add('show');el.setAttribute('aria-hidden','false');}function closeSettings(){const el=document.getElementById('settingsOverlay');el.classList.remove('show');el.setAttribute('aria-hidden','true');}
function resetProgress(){if(!window.confirm('Hapus rating dan seluruh statistik lokal?'))return;try{localStorage.removeItem('tacdchess_progress');}catch(e){}location.reload();}
function renderAll(){
  ensureUnlimitedState();const p=PUZZLES[state.currentPuzzleIndex];const ratingEl=document.getElementById('ratingValue');if(ratingEl)ratingEl.textContent=Math.round(state.playerRating);const ratingMetric=document.getElementById('puzzleRating');if(ratingMetric&&p)ratingMetric.textContent=p.rating;const chip=document.getElementById('difficultyChip');if(chip&&p)chip.textContent='Rating '+p.rating;const theme=document.getElementById('themeChip');if(theme&&p)theme.textContent=themeLabel(p);const turn=document.getElementById('turnDot');if(turn&&state.chess)turn.className='turn-dot '+state.chess.turn;const turnLabel=document.getElementById('statusLabel');const title=document.getElementById('puzzleTitle');const sub=document.getElementById('puzzleSubtitle');const eyebrow=document.getElementById('puzzleEyebrow');const moveChip=document.getElementById('moveCountChip');
  if(p&&moveChip)moveChip.textContent=(p.moves.length<=1?'Mate in 1':p.moves.length<=3?'Short line':p.moves.length<=5?'Medium line':'Long line');
  if(state.status==='player-turn'){if(eyebrow)eyebrow.textContent='YOUR MOVE';if(title)title.textContent='Find the best move';if(sub)sub.textContent=state.feedback||'Solve the position and continue the line.';if(turnLabel)turnLabel.textContent=state.feedback||'Your move';}
  else if(state.status==='opponent-move'){if(eyebrow)eyebrow.textContent='FOLLOW THE LINE';if(title)title.textContent='Opponent responds';if(sub)sub.textContent='Look for the next move in the combination.';if(turnLabel)turnLabel.textContent='Opponent responds…';}
  else if(state.status==='revealing'){if(eyebrow)eyebrow.textContent='SOLUTION';if(title)title.textContent='Showing the line';if(sub)sub.textContent='Review the best continuation.';if(turnLabel)turnLabel.textContent='Solution shown';}
  else {const result=state.daily&&state.daily.slots[0]?state.daily.slots[0].status:'solved';if(eyebrow)eyebrow.textContent=result==='solved'?'PUZZLE COMPLETE':'RESULT';if(title)title.textContent=result==='solved'?'Puzzle solved':result==='revealed'?'Solution revealed':'Puzzle missed';if(sub)sub.textContent=result==='solved'?'Nice work. Your rating has been updated.':result==='revealed'?'This puzzle was assisted and has limited rating credit.':'The next puzzle will be calibrated from your updated rating.';if(turnLabel)turnLabel.textContent=result==='solved'?'Solved':result==='revealed'?'Revealed':'Missed';}
  const streak=document.getElementById('streakMetric');if(streak)streak.textContent=state.streak;const meter=document.getElementById('streakMeter');if(meter)meter.style.width=Math.min(100,state.streak*12.5)+'%';const counter=document.getElementById('puzzleCounter');if(counter)counter.textContent='Puzzle '+(state.experimentPuzzleNumber||1);
  const resultCard=document.getElementById('resultCard');const controls=document.getElementById('controlsRow');const note=document.getElementById('dailyHintNote');const result=state.daily&&state.daily.slots[0]?state.daily.slots[0].status:null;
  if(state.status==='puzzle-complete'){
    resultCard.className='result-card show '+(result==='solved'?'success':'failure');document.getElementById('resultKicker').textContent=result==='solved'?'SUCCESS':result==='revealed'?'ASSISTED':'TRY AGAIN';document.getElementById('resultTitle').textContent=result==='solved'?'Puzzle solved':result==='revealed'?'Solution revealed':'Puzzle missed';const delta=state.ratingDeltaToday;const deltaText=delta>0?'+'+delta:delta<0?String(delta):'±0';document.getElementById('resultDelta').textContent=deltaText;document.getElementById('resultDelta').className='result-delta '+(delta>0?'pos':delta<0?'neg':'');document.getElementById('resultSub').textContent=result==='solved'?(state.hintUsed?'Solved with a hint · smaller rating gain':'Solved cleanly · full rating gain'):result==='revealed'?'Rating credit is limited for a revealed line':'One mistake ends the puzzle · try a new position';controls.innerHTML='';controls.hidden=true;note.textContent='Rating '+Math.round(state.playerRating)+' · choose the next puzzle when ready.';
  }else{resultCard.className='result-card';controls.hidden=false;if(state.status==='player-turn'){controls.innerHTML='<button class="btn btn-ghost" id="hintBtn">'+uiIcon('bulb')+' Hint</button><button class="btn btn-reveal" id="revealBtn">'+uiIcon('eye')+' Reveal</button><button class="btn btn-primary" id="skipBtn">Skip '+uiIcon('arrowRight')+'</button>';document.getElementById('hintBtn').addEventListener('click',useHint);document.getElementById('revealBtn').addEventListener('click',revealSolution);document.getElementById('skipBtn').addEventListener('click',function(){completeCurrentPuzzle('failed');});note.textContent=state.hintUsed?'Hint used · rating gain is reduced.':'One wrong move ends this puzzle. Use hint when you need a nudge.';}else{controls.innerHTML='<button class="btn btn-ghost" disabled>Opponent is thinking…</button>';note.textContent='';}}
  updateTrainerTimer();syncSettings();renderBoard();
}
function experimentInit(){ensureUserId();buildSkeleton();ensureUnlimitedState();const onboarded=loadProgress();if(!onboarded){showOnboarding().then(function(){startExperimentPuzzle();});}else{startExperimentPuzzle();}document.getElementById('soundBtn').innerHTML=state.soundOn?ICONS.soundOn:ICONS.soundOff;document.getElementById('flipBtn').innerHTML=ICONS.flip;setInterval(updateTrainerTimer,1000);setInterval(saveProgress,12000);}
function init(){experimentInit();}
init();
'''
s = s[:tail_start] + new_tail + s[script_end:]

# Make index.html the active entry point while keeping experiment.html synchronized.
(ROOT / 'experiment.html').write_text(s)
(ROOT / 'index.html').write_text(s)

# Update the minimal README.
(ROOT / 'README.md').write_text('3mate Unlimited Puzzle Trainer\n\nAdaptive, rating-based chess mate puzzles built with HTML, CSS, and vanilla JavaScript.\n')
print('updated', len(s), 'characters')
