# 海外网站开发 Agent — 项目说明

> 给老板 + 给老板的朋友 / 团队 / 投资人看的。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Mavis Agent](https://img.shields.io/badge/Mavis-Agent-blue.svg)](https://mavis.minimaxi.com)

---

## 一句话简介

一个**专门帮 OPC 创业者做海外网站**的 Agent，从市场调研到部署上线，全链路 7 阶段工作流，老板总投入约 13 小时拍板，15-27 天出一个 MSP（最小可售产品）。

---

## 这个 Agent 能帮你做什么

1. **市场调研**：行业 / 竞品 / 用户 / 合规
2. **项目筛选**：决策矩阵打分 → MSP 定义
3. **PRD**：用户故事 / User Flow / IA / 验收标准
4. **技术文档**：架构 / 数据模型 / API / 部署
5. **编码实现**：全栈（Next.js + Supabase + Stripe + Vercel）
6. **测试**：单测 / E2E / 性能 / 安全
7. **部署上线**：域名 / DNS / SEO / 上线公告
8. **运营**：数据 / 迭代 / 增长

---

## 怎么用

### 方式 A：Mavis 内置（推荐）

直接在 Mavis 里调用 **webbuilder** agent（已自动创建）。老板说"开工"，Agent 拉起整个工作流。

### 方式 B：Claude Code / Cursor / Aider / Gemini CLI

把这个项目目录作为项目根，进入后 AI 会自动读 `AGENTS.md`。

```bash
cd "<这个项目路径>"
claude-code  # 或 cursor / aider
```

### 方式 C：复制 system prompt 到任意 Chat

把 `system-prompt.md` 里 ```text ... ``` 之间的内容，复制到：
- ChatGPT → Custom Instructions
- Claude.ai → Project system prompt
- 其他 → System message

---

## 文件清单

| 文件 | 用途 | 谁看 |
|------|------|------|
| `README.md` | 项目说明 | 老板 / 团队 / 投资人 |
| `AGENTS.md` | 项目根规范 | AI（Claude Code 等） |
| `SKILL.md` | Skill 加载 | 任何 Skill 平台 |
| `system-prompt.md` | Agent 系统提示词 | 复制粘贴 |
| `工作流-完整版.md` | 完整工作流 | 老板 / 老板复盘 |
| `工作流-完整版.html` | 工作流 HTML 版 | 浏览器看 |
| `index.html` | 聚合入口 | 浏览器打开 |
| `build_html.py` | md → HTML 转换 | 老板改文档后重新生成 |
| `workspace/` | 项目工作目录 | 各项目存这里 |

---

## 工作流（7 阶段 + 持续）

```
Phase 1              Phase 2            Phase 3        Phase 4            Phase 5          Phase 6         Phase 7
市场调研   →        项目筛选    →       PRD       →    技术文档   →       编码实现  →       测试验证   →    部署上线
3-5 天              1-2 天              2-3 天          1-2 天             5-10 天          2-3 天           1-2 天
                                                                       ───── 持续 ─────
总耗时：15-27 天出一个 MSP（最小可售产品）
```

每个阶段结束都有 **GO / NO-GO Gate**，老板拍板才能推进。

---

## 默认技术栈

- 前端：Next.js 14 + Tailwind + shadcn/ui
- 后端：Next.js API Routes / tRPC
- 数据库：Supabase (Postgres + Auth)
- 支付：Stripe Checkout / Creem / Lemon Squeezy
- 部署：Vercel + Cloudflare CDN
- 分析：Plausible
- 邮件：Resend
- 监控：Sentry
- E2E：Playwright
- ORM：Prisma / Drizzle

---

## 老板的硬约束（Agent 必须遵守）

1. **承诺必须可实现** — PRD 里写了什么，代码里必须有
2. **简化定价** — 少即是多，不造 3-5 档"伪差异化"
3. **不造假数据** — 用户数 / ARR / 证言必须真实
4. **联动解决一类问题** — 不要一个问题只修一次
5. **先验证再继续** — 每个阶段必须有验证产物

---

## 下一步行动

老板：
1. 在 Mavis 里启用 webbuilder agent（已创建，agent_name: webbuilder）
2. 创建第一个项目的 web 模板：`mkdir -p workspace/<项目名>-<日期>`
3. 跟 webbuilder 说"开工"，开始 Phase 1

---

## 项目位置

```
海外网站开发Agent/
├── README.md
├── AGENTS.md
├── SKILL.md
├── system-prompt.md
├── LICENSE
├── .gitignore
├── 工作流-完整版.md
├── 工作流-完整版.html
├── index.html
├── build_html.py
└── workspace/
    └── <项目名>-<日期>/
```

---

## GitHub 部署

### 快速上传（3 步）

#### 1. 在 GitHub 上创建空 repo

打开 <https://github.com/new>，填：
- **Repository name**：`webbuilder-agent`（或你想要的）
- **Description**：海外网站开发 Agent — 全链路 7 阶段
- **Public / Private**：按需（推荐 Private）
- **不要**勾选 "Add a README" / "Add .gitignore"（本地已有）

点 **Create repository**。

#### 2. 配 git 身份（一次性）

```bash
cd "<这个项目路径>"
git config user.name "你的 GitHub 用户名"
git config user.email "你的 GitHub 邮箱"
```

#### 3. 推送

```bash
git remote add origin git@github.com:<你的用户名>/webbuilder-agent.git
# 或 HTTPS：git remote add origin https://github.com/<你的用户名>/webbuilder-agent.git
git push -u origin main
```

### 用 gh CLI（更快）

```bash
brew install gh
gh auth login
gh repo create webbuilder-agent --private --source=. --remote=origin --description "海外网站开发 Agent"
git push -u origin main
```

---

## 关联项目

- Mavis 内置 agent: **webbuilder** (displayName: 海外网站开发Agent)
- 工作流文档：`工作流-完整版.md` (20KB)
- HTML 入口：`index.html`（自动转）

---

## 维护记录

- **v1.0** (2026-10-02) — 初始版本，7 阶段工作流 + Mavis agent + 跨平台兼容
  - Mavis agent `webbuilder` 已创建
  - 工作流 7 阶段 + 持续运营完整文档
  - 文档 + HTML + SKILL + System Prompt 全套交付
  - 默认 Next.js + Supabase + Stripe + Vercel 技术栈

---

> 这个 Agent 的目标：让老板 1 个人能跑通"产品 0 到 1"全链路，把钱花在刀刃上。