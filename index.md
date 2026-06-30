---
layout: default
title: 首页
---

<div class="home-layout">
  <aside class="sidebar">
    <div class="sidebar-card">
      <div class="avatar">8861</div>
      <h3>{{ site.author }}</h3>
      <p class="bio">{{ site.bio }}</p>
      <div class="social-links">
        <a href="https://github.com/{{ site.github }}" target="_blank" title="GitHub">
          <svg height="20" width="20" viewBox="0 0 16 16" fill="#666"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>
        </a>
        <a href="mailto:{{ site.email }}" title="Email">
          <svg height="20" width="20" viewBox="0 0 24 24" fill="#666"><path d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
        </a>
      </div>
    </div>

    <div class="sidebar-card">
      <h4>📂 分类</h4>
      <div class="categories">
        {% assign cats = site.categories | sort %}
        {% for cat in cats %}
        <span class="category-tag">{{ cat[0] }}<sup>{{ cat[1] | size }}</sup></span>
        {% endfor %}
      </div>
    </div>

    <div class="sidebar-card">
      <h4>📝 近期文章</h4>
      <ul class="sidebar-posts">
        {% for post in site.posts limit:5 %}
        <li>
          <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
          <span class="post-date">{{ post.date | date: "%m-%d" }}</span>
        </li>
        {% endfor %}
      </ul>
    </div>
  </aside>

  <main class="home-main">
    <h1 class="section-title">最新文章</h1>
    {% for post in site.posts %}
    <article class="post-card">
      <div class="post-card-body">
        <div class="post-meta">
          <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%Y 年 %m 月 %d 日" }}</time>
          {% if post.categories %}
          {% for cat in post.categories %}
          <span class="cat-badge">{{ cat }}</span>
          {% endfor %}
          {% endif %}
        </div>
        <h2><a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
        <p class="post-excerpt">{{ post.excerpt | strip_html | truncate: 150 }}</p>
        <a class="read-more" href="{{ post.url | relative_url }}">阅读更多 →</a>
      </div>
    </article>
    {% endfor %}
  </main>
</div>
