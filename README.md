# 8861 的博客

基于 [Hugo](https://gohugo.io) 构建，部署在 [GitHub Pages](https://pages.github.com)。

## 写新文章

在 `content/posts/` 下新建 `.md` 文件：

```markdown
---
title: "文章标题"
date: 2025-10-10T10:00:00+08:00
tags:
  - 标签1
  - 标签2
---

## 正文

用 Markdown 写内容...
```

## 本地预览

```bash
hugo server -D
```

打开 http://localhost:1313

## 部署

推送到 `main` 分支，GitHub Actions 自动构建并发布。

```bash
git add .
git commit -m "新文章"
git push
```

## 文件生成规范

### 文件名规则
- 只允许：`a-z`、`A-Z`、`0-9`、`-`（横线）、`.`（点号）
- 不允许：中文、空格、逗号、冒号、问号、引号等特殊符号
- 不允许中文标点（`，` `。` `？` `：` `"` `"` 等）

### 命名格式
```
{编号}-{简短关键词}.md
```

### 文章标题（front matter）
- `title` 字段可以用完整中文，不受文件名限制
- 标题与文件名无关，页面显示的是 `title` 的内容

### 生成后必做验证
1. `hugo` 构建不报错
2. 文章列表页能正常显示新文章
3. 点击新文章能正常打开内容（非404）
