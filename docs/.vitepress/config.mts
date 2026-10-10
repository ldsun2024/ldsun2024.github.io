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

interface Cat {
  dir: string
  label: string
  count: number
  link: string
}

// 目录名保持精简（同时是 URL 路径），站点显示沿用原来的完整名称
const DISPLAY_NAMES: Record<string, string> = {
  '05-大盘多空': '大盘多空分析',
  '06-期权': '期权课',
  '07-火箭': '火箭课',
  '08-黄金': '黄金课'
}

function scanCats(): Cat[] {
  if (!fs.existsSync(notesDir)) return []
  return fs
    .readdirSync(notesDir, { withFileTypes: true })
    .filter((d) => d.isDirectory())
    .map((d) => d.name)
    .sort()
    .map((dir) => {
      const files = fs
        .readdirSync(path.join(notesDir, dir))
        .filter((f) => f.endsWith('.md') && f !== 'index.md')
      return {
        dir,
        label: DISPLAY_NAMES[dir] ?? dir.replace(/^\d+-/, ''),
        count: files.length,
        link: '/笔记/' + dir + '/'
      }
    })
}

const COURSES = ['01-中级课', '02-高级课', '03-研修课',
  '05-大盘多空', '06-期权', '07-火箭', '08-黄金']
const PAGES = [
  { text: '首页', link: '/' },
  { text: '经典语录', link: '/笔记/09-经典语录/' },
  {
    text: '笔记',
    items: [] as any[]
  },
  { text: '案例分析', link: '/笔记/10-案例分析/' },
  { text: '其它', link: '/笔记/11-其它/' }
]

function buildNav() {
  const cats = scanCats()
  const courseItems = cats
    .filter((c) => COURSES.includes(c.dir))
    .map((c) => ({ text: c.label + ' · ' + c.count, link: c.link }))
  const nav = PAGES.map((p) =>
    p.text === '笔记' ? { text: p.text, items: courseItems } : p
  )
  return nav
}

const COURSE_NAMES = '(中级课|高级课|研修课|大盘多空分析|期权课|火箭课|黄金课)'

function cleanTitle(t: string): string {
  const stripDate = (s: string): string =>
    s
      .replace(/^\d{4}\s*年\s*[\d\s]*月\s*[\d\s]*日-/, '')
      .replace(/^\d{4}\.\d{2}\.\d{2}-/, '')
  let s = t.replace(/^课程理论-/, '')
  s = stripDate(s)
  s = s.replace(/^\d{2}-\d+-?/, '')
  s = s.replace(new RegExp('^' + COURSE_NAMES + '-\\d+-'), '')
  s = s.replace(new RegExp('^' + COURSE_NAMES + '[\\s-]+(?=\\S)'), '')
  s = stripDate(s)
  s = s.replace(/^\d+-/, '')
  return s.trim()
}

function listItems(c: Cat, numbered = false) {
  const dir = path.join(notesDir, c.dir)
  const files = fs
    .readdirSync(dir)
    .filter((f) => f.endsWith('.md') && f !== 'index.md')
    .sort()
  return files.map((f) => {
    const clean = cleanTitle(readTitle(path.join(dir, f)))
    const m = numbered ? f.match(/^(\d+)-/) : null
    const num = m ? String(parseInt(m[1], 10)).padStart(2, '0') : ''
    return {
      text: num ? num + '-' + clean : clean,
      link: '/笔记/' + c.dir + '/' + f.replace(/\.md$/, '')
    }
  })
}

function buildSidebar() {
  const cats = scanCats()
  const group = (c: Cat) => ({
    text: c.label,
    // 条目多的分组（如 07-火箭 108 项）默认折叠，避免侧边栏过长
    collapsed: c.count > 30,
    items: listItems(c, COURSES.includes(c.dir))
  })
  const pick = (dir: string): Cat[] => {
    const c = cats.find((x) => x.dir === dir)
    return c ? [c] : []
  }
  return {
    '/笔记/09-经典语录/': pick('09-经典语录').map(group),
    '/笔记/10-案例分析/': pick('10-案例分析').map(group),
    '/笔记/11-其它/': pick('11-其它').map(group),
    ...Object.fromEntries(
      cats
        .filter((c) => COURSES.includes(c.dir))
        .map((c) => ['/笔记/' + c.dir + '/', [group(c)]])
    )
  }
}

export default defineConfig({
  title: '8861',
  description: '股票技术分析课程笔记与实战复盘',
  lang: 'zh-CN',
  base: '/',
  outDir: '../dist',
  cleanUrls: true,
  lastUpdated: true,
  repo: 'https://github.com/ldsun2024/ldsun2024.github.io',
  themeConfig: {
    nav: buildNav(),
    sidebar: buildSidebar(),
    outline: { level: [2, 2], label: '页面导航' },
    search: { provider: 'local' },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/ldsun2024/ldsun2024.github.io' }
    ],
    editLink: {
      pattern: 'https://github.com/ldsun2024/ldsun2024.github.io/edit/main/docs/:path',
      text: '在 GitHub 上编辑此页'
    },
    docFooter: { prev: '上一页', next: '下一页' },
    lastUpdatedText: '最后更新于',
    darkModeSwitchLabel: '主题',
    sidebarMenuLabel: '菜单',
    returnToTopLabel: '回到顶部',
    darkModeSwitchTitle: '切换到深色模式',
    lightModeSwitchTitle: '切换到浅色模式',
    externalLinkIcon: true
  }
})
