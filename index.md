---
layout: default
title: 首页
---

<h1 class="page-title">最新文章</h1>

<ul class="post-list">
  {% for post in site.posts %}
  <li>
    <div class="post-meta">{{ post.date | date: "%Y 年 %m 月 %d 日" }}</div>
    <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <div class="post-excerpt">{{ post.excerpt | strip_html | truncate: 200 }}</div>
  </li>
  {% endfor %}
</ul>
