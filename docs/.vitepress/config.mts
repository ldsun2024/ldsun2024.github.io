import { defineConfig } from 'vitepress'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const here = fileURLToPath(new URL('.', import.meta.url))
const notesDir = path.resolve(here, '../笔记')

function readTitle(file: string): string {
  const raw = fs.readFileSync(file, 'utf8')
  const fm = raw.match(/^---\r?\n([\s\S]*?)\r?\n---/)
  if (fm) {
    const t = fm[1].match(/^title:\s*"?(.+?)"?\s*$/m)
    if (t) return t[1].trim()
  }
  return path.basename(file, '.md')
}

function buildSidebar() {
  if (!fs.existsSync(notesDir)) return []
  const cats = fs
    .readdirSync(notesDir, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => d.name)
    .sort()
  return cats.map((cat) => {
    const dir = path.join(notesDir, cat)
    const files = fs
      .readdirSync(dir)
      .filter((f) => f.endsWith('.md') && f !== 'index.md')
      .sort()
    return {
      text: cat.replace(/^\d+-/, ''),
      link: '/笔记/' + cat + '/',
      collapsed: true,
      items: files.map((f) => ({
        text: readTitle(path.join(dir, f)).replace(/^课程理论-/, ''),
        link: '/笔记/' + cat + '/' + f.replace(/\.md$/, '')
      }))
    }
  })
}

export default defineConfig({
  title: '8861 投资笔记',
  description: '股票技术分析课程笔记与实战复盘',
  lang: 'zh-CN',
  base: '/',
  cleanUrls: true,
  lastUpdated: true,
  themeConfig: {
    nav: [
      { text: '首页', link: '/' },
      { text: '笔记', link: '/笔记/' }
    ],
    sidebar: buildSidebar(),
    outline: { level: [2, 3], label: '本页目录' },
    search: { provider: 'local' },
    docFooter: { prev: '上一篇', next: '下一篇' },
    lastUpdatedText: '最后更新',
    darkModeSwitchLabel: '主题',
    sidebarMenuLabel: '目录',
    returnToTopLabel: '回到顶部'
  }
})
