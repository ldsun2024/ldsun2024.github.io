import { defineConfig } from 'vitepress'

export default defineConfig({
  title: '清单',
  description: '常用影视观看站点导航',
  lang: 'zh-CN',
  base: '/',
  outDir: '../dist',
  cleanUrls: true,
  themeConfig: {
    outline: { level: [2, 2], label: '页面导航' },
    docFooter: { prev: '上一页', next: '下一页' },
    darkModeSwitchLabel: '主题',
    sidebarMenuLabel: '菜单',
    returnToTopLabel: '回到顶部',
    darkModeSwitchTitle: '切换到深色模式',
    lightModeSwitchTitle: '切换到浅色模式',
    externalLinkIcon: true
  }
})
