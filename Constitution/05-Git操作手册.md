# Git 操作手册

本站日常 Git 操作速查 —— 拉代码、提交流、推送部署。

---

## 一、基础配置

```bash
# 配置用户信息（首次使用 Git 时）
git config --global user.name "你的名字"
git config --global user.email "你的邮箱@example.com"

# 查看当前配置
git config --list
```

---

## 二、拉取代码（Pull）

### 2.1 首次克隆

```bash
git clone git@github.com:ldsun2024/ldsun2024.github.io.git
cd ldsun2024.github.io
```

### 2.2 拉取最新代码

```bash
# 从远程拉取最新变更，并合并到当前分支
git pull

# 完整写法（当前分支关联了远程分支时效果一样）
git pull origin main
```

### 2.3 拉取但不合并（fetch）

```bash
# 只拉取远程最新记录，不自动合并
git fetch

# 拉取后查看差异，再决定如何合并
git fetch
git log main..origin/main --oneline   # 查看本地落后了哪些提交
git diff main origin/main             # 查看具体差异
git merge origin/main                 # 确认无误后合并
```

---

## 三、提交代码（Commit）

### 3.1 查看当前状态

```bash
git status
```

### 3.2 添加文件到暂存区

```bash
# 添加单个文件
git add 文件路径

# 添加所有变更（新增、修改、删除）
git add -A

# 交互式添加（逐个确认）
git add -p
```

### 3.3 提交到本地仓库

```bash
# 提交（会打开编辑器写提交信息）
git commit

# 提交（直接写信息，适合简单修改）
git commit -m "feat: 新增文章 XXX"
```

### 3.4 常用提交信息格式

```
feat: 新增文章/功能
fix: 修复问题
docs: 文档变更
refactor: 重构
style: 格式调整（不影响功能）
```

---

## 四、推送代码（Push）

### 4.1 推送到远程

```bash
# 推送到 origin（默认远程仓库）的 main 分支
git push origin main

# 如果当前分支已关联远程分支，可以简写
git push
```

### 4.2 推送后自动部署

推送到 `main` 分支后，GitHub Actions 会自动执行：

1. `hugo --verbose` 构建站点
2. 将 `public/` 目录部署到 GitHub Pages
3. 约 1-2 分钟后线上生效

---

## 五、完整工作流

### 日常写文章

```bash
# 1. 拉取最新代码（避免冲突）
git pull

# 2. 新建 .md 文件并写文章
#    content/posts/<分类>/<文件名>.md

# 3. 本地预览
hugo server -D
# 浏览器打开 http://localhost:1313

# 4. 确认无误后提交
git status                     # 查看变更
git add -A                     # 添加所有变更
git commit -m "feat: 新增文章《xxx》"

# 5. 推送上线
git push
```

### 修改已有文章

```bash
git pull
# 编辑文章 .md 文件
hugo server -D                 # 本地预览
git add -A
git commit -m "docs: 更新文章《xxx》"
git push
```

---

## 六、常见场景

### 6.1 撤销未提交的修改

```bash
# 撤销工作区的修改（未 git add 的）
git restore 文件名

# 撤销暂存区的修改（已 git add 的）
git restore --staged 文件名

# 撤销所有未提交的修改
git restore .
git restore --staged .
```

### 6.2 修改上一次提交信息

```bash
git commit --amend -m "新的提交信息"
```

### 6.3 查看提交历史

```bash
# 简洁查看
git log --oneline

# 图形化查看
git log --oneline --graph --all

# 查看最近 N 条
git log -5
```

### 6.4 解决冲突

拉取代码时如果提示冲突：

```bash
git pull
# 提示：CONFLICT（冲突）
#
# 1. 打开冲突文件，搜索 <<<<<<< 标记
# 2. 手动保留正确的内容，删除冲突标记
# 3. 保存文件

git add 文件名          # 标记冲突已解决
git commit -m "fix: 解决合并冲突"
```

### 6.5 查看远程仓库信息

```bash
# 查看远程仓库
git remote -v

# 查看本地分支与远程的关联关系
git branch -vv
```

---

## 七、命令速查表

| 操作 | 命令 |
|------|------|
| 拉取最新代码 | `git pull` |
| 拉取但不合并 | `git fetch` |
| 查看状态 | `git status` |
| 添加所有变更 | `git add -A` |
| 提交 | `git commit -m "信息"` |
| 推送 | `git push` |
| 查看提交历史 | `git log --oneline` |
| 撤销工作区修改 | `git restore 文件名` |
| 撤销暂存区 | `git restore --staged 文件名` |
| 修改上次提交 | `git commit --amend -m "新信息"` |
| 查看差异 | `git diff` |
