---
layout: home
---

<div class="poster">
  <div class="poster-lines">
    <span class="poster-line poster-line-left">只有无与伦比的专注</span>
    <span class="poster-line poster-line-right">才有超乎想象的回报</span>
  </div>
</div>

<style>
@import url('https://fonts.googleapis.com/css2?family=Zhi+Mang+Xing&display=swap');

/* 布局重置：仅在包含 .poster 的首页生效，避免污染其他页面 */
.VPPage:has(.poster),
.VPContent:has(.poster),
.VPHome:has(.poster) {
  padding: 0 !important;
  margin: 0 !important;
}

.VPHome:has(.poster) {
  display: flex;
  flex-direction: column;
  min-height: calc(100vh - var(--vp-nav-height));
}
</style>

<style scoped>
.poster {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 0 24px;
}

.poster-lines {
  display: grid;
  grid-template-rows: auto auto;
  justify-items: start;
  row-gap: 0.5em;
  width: 100%;
  max-width: 1320px;
  margin: 0 auto;
}

.poster-line {
  font-family: 'Zhi Mang Xing', 'Ma Shan Zheng', 'STXingkai', 'KaiTi', 'STKaiti', '楷体', cursive, serif;
  font-size: clamp(36px, 7.6vw, 124px);
  font-weight: 400;
  line-height: 1.3;
  letter-spacing: 0.08em;
  color: var(--vp-c-text-1);
  white-space: nowrap;
}

.poster-line-right {
  justify-self: end;
}

@media (max-width: 767px) {
  .poster-lines {
    justify-items: center;
  }

  .poster-line-right {
    justify-self: auto;
  }

  .poster-line {
    /* 9字一行自适应：8.2vw 保证 320-767px 均放得下，上限 58px 与 768px 处桌面 7.6vw 无缝衔接 */
    font-size: clamp(24px, 8.2vw, 58px);
    white-space: nowrap;
  }
}
</style>
