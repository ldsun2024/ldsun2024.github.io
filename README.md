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
