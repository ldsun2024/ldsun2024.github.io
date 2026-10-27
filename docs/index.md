---
layout: page
---

<script setup>
const res = [
  { name: '新视觉 6080', url: 'https://m.xinshijue-6080.hl.cn/', domain: 'xinshijue-6080.hl.cn' },
  { name: '6080 影视', url: 'https://www.6080film.cc/', domain: '6080film.cc' },
  { name: 'hellorlgzf7sn', url: 'https://www.hellorlgzf7sn.com/', domain: 'hellorlgzf7sn.com' },
  { name: 'rentbus', url: 'https://www.rentbus.cn/', domain: 'rentbus.cn' },
  { name: 'hr0592', url: 'http://m.hr0592.cn/', domain: 'hr0592.cn' },
  { name: 'rrsp', url: 'https://d.rrsp.com.cn/', domain: 'rrsp.com.cn' },
  { name: '追剧网', url: 'https://www.zhuijuwang.cc/', domain: 'zhuijuwang.cc' },
  { name: 'Silidm', url: 'https://silidm.com/', domain: 'silidm.com' },
  { name: 'VCinema', url: 'https://v.vcinema.cn/filtrate', domain: 'vcinema.cn' },
  { name: 'Guobayu', url: 'https://www.guobayu.com/', domain: 'guobayu.com' },
  { name: 'Duse0', url: 'https://www.duse0.com/', domain: 'duse0.com' },
  { name: 'YMCK', url: 'https://www.ymck.pro/', domain: 'ymck.pro' },
  { name: 'X8kb9k8', url: 'https://www.x8kb9k8.com/', domain: 'x8kb9k8.com' },
  { name: '茶杯狐', url: 'https://cupfox.love/', domain: 'cupfox.love' },
  { name: 'NO视频', url: 'https://www.novipnoad.net/', domain: 'novipnoad.net' },
  { name: '微视TV', url: 'https://weishitv.xyz/', domain: 'weishitv.xyz' },
  { name: 'Trex', url: 'https://trex.tzfile.com/', domain: 'trex.tzfile.com' }
]
</script>

<div class="tv-page">
<header class="tv-hero">
<p class="tv-kicker">Index</p>
<h1>免费观看网站清单</h1>
<p class="tv-sub">{{ res.length }} 个入口 · 点击直达</p>
</header>
<div class="tv-list">
<a v-for="(s, i) in res" :key="s.url" class="tv-row" :style="{ '--i': i }" :href="s.url" target="_blank" rel="noopener noreferrer">
<span class="tv-idx">{{ String(i + 1).padStart(2, '0') }}</span>
<span class="tv-name">{{ s.name }}</span>
<span class="tv-domain">{{ s.domain }}</span>
<span class="tv-arrow">→</span>
</a>
</div>
<footer class="tv-foot">链接清单 · 不存储任何影视资源</footer>
</div>

<style>
:root {
  --tv-paper: #ffffff;
  --tv-ink: #000000;
  --tv-ink-2: #3d3d3d;
  --tv-ink-3: #767676;
  --tv-ink-4: #a0a0a0;
  --tv-line: #e6e6e6;
  --vp-c-bg: var(--tv-paper);
  --vp-c-bg-alt: var(--tv-paper);
  --vp-c-bg-soft: #fafafa;
  --vp-c-text-1: var(--tv-ink);
  --vp-c-text-2: var(--tv-ink-2);
  --vp-c-text-3: var(--tv-ink-3);
  --vp-c-divider: var(--tv-line);
  --vp-c-brand-1: var(--tv-ink);
  --vp-c-brand-2: var(--tv-ink);
  --vp-c-brand-3: var(--tv-ink);
}

html.dark {
  --tv-paper: #000000;
  --tv-ink: #ffffff;
  --tv-ink-2: #c7c7c7;
  --tv-ink-3: #8c8c8c;
  --tv-ink-4: #5a5a5a;
  --tv-line: #1f1f1f;
  --vp-c-bg: var(--tv-paper);
  --vp-c-bg-alt: var(--tv-paper);
  --vp-c-bg-soft: #0a0a0a;
  --vp-c-text-1: var(--tv-ink);
  --vp-c-text-2: var(--tv-ink-2);
  --vp-c-text-3: var(--tv-ink-3);
  --vp-c-divider: var(--tv-line);
  --vp-c-brand-1: var(--tv-ink);
  --vp-c-brand-2: var(--tv-ink);
  --vp-c-brand-3: var(--tv-ink);
}

.tv-page {
  --font-sans: "PingFang SC", "HarmonyOS Sans SC", "Noto Sans SC", "Microsoft YaHei", sans-serif;
  --font-mono: "JetBrains Mono", ui-monospace, "SFMono-Regular", Menlo, Consolas, monospace;
  max-width: 720px;
  margin: 0 auto;
  padding: 120px 24px 140px;
  font-family: var(--font-sans);
  color: var(--tv-ink);
}

.tv-hero {
  margin-bottom: 68px;
}

.tv-kicker {
  margin: 0 0 34px;
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 400;
  letter-spacing: 0.34em;
  text-transform: uppercase;
  color: var(--tv-ink-3);
}

.tv-hero h1 {
  margin: 0;
  padding: 0;
  border: none;
  font-size: clamp(30px, 5.6vw, 62px);
  font-weight: 800;
  line-height: 1.12;
  letter-spacing: -0.02em;
  white-space: nowrap;
  color: var(--tv-ink);
}

.tv-sub {
  margin: 30px 0 0;
  font-size: 13px;
  font-weight: 400;
  letter-spacing: 0.04em;
  color: var(--tv-ink-2);
}

.tv-list {
  border-top: 1px solid var(--tv-line);
}

.tv-row {
  position: relative;
  display: grid;
  grid-template-columns: 42px 1fr auto 26px;
  align-items: baseline;
  gap: 16px;
  padding: 23px 0;
  border-bottom: 1px solid var(--tv-line);
  text-decoration: none;
  opacity: 0;
  animation: tv-in 0.42s ease forwards;
  animation-delay: calc(var(--i, 0) * 45ms);
}

.tv-row:hover {
  text-decoration: none;
}

.tv-row::before {
  content: "";
  position: absolute;
  left: -14px;
  top: 0;
  width: 2px;
  height: 0;
  background: var(--tv-ink);
  transition: height 0.24s ease;
}

.tv-row:hover::before {
  height: 100%;
}

.tv-idx {
  font-family: var(--font-mono);
  font-size: 13px;
  letter-spacing: 0.1em;
  color: var(--tv-ink-3);
  transition: color 0.2s ease;
}

.tv-name {
  font-size: 19px;
  font-weight: 500;
  letter-spacing: 0.01em;
  color: var(--tv-ink-2);
  transition: color 0.2s ease;
}

.tv-domain {
  font-family: var(--font-mono);
  font-size: 13px;
  letter-spacing: 0.06em;
  color: var(--tv-ink-3);
  transition: color 0.2s ease;
}

.tv-arrow {
  font-size: 18px;
  line-height: 1;
  text-align: right;
  color: var(--tv-ink-3);
  transition: color 0.2s ease, transform 0.24s ease;
}

.tv-row:hover .tv-idx {
  color: var(--tv-ink-2);
}

.tv-row:hover .tv-name {
  color: var(--tv-ink);
}

.tv-row:hover .tv-domain {
  color: var(--tv-ink-2);
}

.tv-row:hover .tv-arrow {
  color: var(--tv-ink);
  transform: translateX(4px);
}

.tv-foot {
  margin-top: 88px;
  font-family: var(--font-mono);
  font-size: 10.5px;
  letter-spacing: 0.18em;
  color: var(--tv-ink-4);
}

@keyframes tv-in {
  to {
    opacity: 1;
  }
}

@media (max-width: 640px) {
  .tv-page {
    padding: 72px 20px 96px;
  }

  .tv-hero {
    margin-bottom: 44px;
  }

  .tv-row {
    grid-template-columns: 30px 1fr 20px;
    gap: 12px;
    padding: 19px 0;
  }

  .tv-domain {
    display: none;
  }

  .tv-name {
    font-size: 18px;
  }
}
</style>
