# AGENTS.md

> 这是 **海外网站开发 Agent** 的项目根规范。任何 AI（Claude Code / Cursor / Aider / Gemini CLI / Devin / OpenCode）进入这个目录，请先读这份文档。

---

## 项目目标

帮助老板（OPC 创业者 / 超级个体）从零到落地、做出可对外收钱的**海外网站**。

完整工作流：**市场调研 → 选项目 → PRD → 技术文档 → 编码 → 测试 → 部署 → 运营**，全链路跑通。

---

## 启动前必读（按顺序）

1. `README.md` — 项目说明、怎么用、怎么部署
2. `工作流-完整版.md` — 7 个 Phase 的详细步骤、输入/输出/工具/风险/决策点
3. `system-prompt.md` — Agent 灵魂提示词（**直接复制**作为系统提示）
4. `SKILL.md` — 当 Skill 加载时使用

---

## 工作方式（强约束）

### 7 大阶段

| 阶段 | 名称 | 耗时 | 老板拍板点 |
|------|------|------|----------|
| Phase 1 | 市场调研 | 3-5 天 | 赛道 / 地区 / 合规 |
| Phase 2 | 项目筛选 | 1-2 天 | MSP 范围 |
| Phase 3 | PRD | 2-3 天 | PRD 范围 |
| Phase 4 | 技术文档 | 1-2 天 | 技术栈 |
| Phase 5 | 编码实现 | 5-10 天 | Logo / 主页 / 定价 |
| Phase 6 | 测试 | 2-3 天 | 上线许可 |
| Phase 7 | 部署上线 | 1-2 天 | 上线公告 |
| Phase 8 | 运营 | 持续 | 周数据 / 月复盘 |

### 每个 Phase 必须走 Gate

**绝对不能自动推进**——每个阶段结束都要给老板过"GO / NO-GO"。即使老板说"继续"，也要走 Gate 拍板。

### 老板的硬约束（不可违反）

1. **承诺必须可实现** — PRD 里写了什么，代码里必须有
2. **简化定价** — 少即是多，不造 3-5 档"伪差异化"
3. **不造假数据** — 用户数 / ARR / 证言必须真实
4. **联动解决一类问题** — 不要一个问题只修一次
5. **先验证再继续** — 每个阶段都必须有验证产物

### 工程纪律

- **每次改动 → 一个 commit**（精确 `git add <文件>`，不要 `git add .`）
- **每次改动 → 写或更新测试**，交付前全部通过
- **不 commit .next/cache / dist / build / node_modules** 等产物

---

## 默认工具链

- 前端：Next.js 14 (App Router) + Tailwind + shadcn/ui
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

## 目录结构

```
海外网站开发Agent/
├── README.md                # 项目说明（老板/外部看）
├── AGENTS.md                # 本文件：项目根规范（AI 必读）
├── SKILL.md                 # Skill 加载格式
├── system-prompt.md         # Agent 系统提示词（直接复制）
├── 工作流-完整版.md          # 完整工作流文档
├── 工作流-完整版.html        # HTML 版（浏览器好看）
├── index.html               # 聚合入口（浏览器打开）
├── build_html.py             # markdown → HTML 转换脚本
├── workspace/               # 各项目工作目录
│   └── <项目名>-<日期>/
│       ├── progress.md      # 进度记录
│       ├── 01-市场大盘.md    # Phase 1
│       ├── 02-用户画像.md    # Phase 1
│       ├── ...
│       └── 00-GO-结构化记录.md  # Gate 决策
└── README-zh.md            # 中文 README（如需要）
```

---

## 启动流程（老板初次使用）

### 步骤 1：老板说"开工"

确认：
- 目标地区（北美 / 欧盟 / 全球英文 / 其他）
- 赛道方向（老板指定 / Agent 推荐 3 个）
- 项目代号

### 步骤 2：拉起 workspace

```bash
mkdir -p ~/Desktop/AI项目/海外网站开发Agent/workspace/<项目名>-<日期>/
cd ~/Desktop/AI项目/海外网站开发Agent/workspace/<项目名>-<日期>/
```

### 步骤 3：创建 progress.md

写入当前日期、Phase 1 启动、待办事项。

### 步骤 4：开始 Phase 1 · 市场调研

按 `工作流-完整版.md` 的 Phase 1 步骤执行。

---

## 跑通后的产出标准

每个项目跑通必须产出：
1. **代码仓库**（GitHub / 本地 git 仓库，commit 历史完整）
2. **PRD + 技术文档 + 测试报告**（在 `workspace/<项目>/`）
3. **可访问 URL**（生产环境域名，老板在浏览器看）
4. **上线检查清单**（每项 ✅）

---

## 跑通后期维护

- 每个双周发一个版本（按 Phase 8 持续运营）
- 每月一份数据报告（DAU / 转化 / 留存 / NPS）
- 每季度一份策略回顾（赛道是否需要切换、是否进新市场）

---

## 不做什么

- **不做 OPC PDF 整本扫描 + OCR**（老板明确不要）
- **不做老板没要求的"伪差异化"**（3 档 / 5 档定价、加购项）
- **不绕过老板拍板**（即使老板说"继续"也要走 Gate）
- **不编造数据 / 证言 / 行业平均数**
- **不在 PRD 里承诺做不到的功能**

---

> **遇到不确定**：开发模式 "截断到最近决策点"，等老板拍板再继续。