# GTM Repository for Claude Code：构建GTM知识脑

## 核心洞察

**来源**: GTM Strategist (2026-04-15)
**链接**: https://knowledge.gtmstrategist.com/p/the-gtm-repository-for-claude-code
**字数**: ~7000字符

**核心思想**: 用结构化markdown文件库捕获GTM制度知识，让Claude在会话开始就有上下文，任务变成单行prompt。这是一个**GTM知识的工程化组织方案**，将团队GTM能力沉淀为可复用的"GTM Brain"。

这是知识管理与AI工作流的完美结合。

---

## 五层架构

### 1. CLAUDE.md (入口文件)
- **作用**: 每次会话自动读取
- **内容**: ICP摘要、顶级信号、定位、团队、当前优先级
- **原则**: 2分钟可扫描，详细内容在其他文件

### 2. Context Files (6个核心)
1. `profile.md`: 公司概述、产品、客户画像、参考客户
2. `icp-definition.md`: 层级定义、明确标准、ICP演变日志
3. `signal-library.md`: 信号库、检测方法、分值、衰减曲线
4. `positioning.md`: 价值支柱、信息矩阵、禁忌语言
5. `competitor-radar.md`: 竞品雷达、诚实评估胜负点
6. `personas/`: 买家画像、决策角色、关注点

### 3. Skills (5个任务技能)
1. **Setup**: 自动研究公司，填充70-80%内容
2. **Account Research**: 账户情报简报、利益相关者地图
3. **Signal to Sequence**: 完整活动构建、触发逻辑、序列文案
4. **ICP Scoring**: 账户评分、层级分配
5. **Weekly Update**: 识别过时内容、起草更新

### 4. Workflows (3个流程)
1. `enrichment.md`: 数据瀑布、质量阈值、邮件送达
2. `signal-routing.md`: 信号路由决策树
3. `campaign-build.md`: 活动构建全流程

### 5. Outputs (输出存档)
- 所有输出自动存档到对应文件夹
- 形成反馈循环：输出 → 提炼 → 更新Context Files

---

## 对AI咨询业务的价值

### 知识管理+AI工作流范例

这是**将咨询方法论沉淀为可执行AI系统**的完整案例：

**传统咨询**: 顾问个人经验，难以复用
**GTM Repository**: 结构化知识库，Claude Code可执行

**你的机会**:
1. 将 AI咨询方法论 沉淀为类似Repo
2. 为每个服务线（定价、GTM、组织转型）建立Context Files
3. 用Claude Code实现自动化报告生成、方案设计

### 产品化服务后端

**服务**: "GTM智能诊断" + "定价策略生成" + "组织转型路线图"

**后端**: 基于Repository结构，客户提供基础信息 → Claude Code自动生成初稿 → 人类顾问优化

**效率**: 交付周期从4周缩短到1周，成本下降70%

---

## 实施建议

### 第一步: 为AI咨询建立Repository
- 根目录: `ai-consulting-repo/`
- `CLAUDE.md`: 咨询方法论摘要、当前客户、优先级
- `context/`:
  - `methodologies/`: 定价框架、GTM策略、组织转型模型
  - `case-studies/`: 分类案例库（失败/成功/进行中）
  - `frameworks/`: MECE、价值链、变革管理
  - `data-sources/`: 行业数据、基准指标
- `skills/`:
  - `pricing-diagnostic`
  - `gtm-assessment`
  - `org-evolution-plan`
- `workflows/`: 咨询项目全流程
- `outputs/`: 客户报告存档

### 第二步: 用Claude Code实现
- Claude Code读取Repository
- 客户输入基础信息 → 自动调用skills → 生成报告草稿
- 人类顾问审核、调整、交付

### 第三步: 持续优化
- 每次项目后提炼insights，更新Repository
- 形成"越用越聪明"的咨询知识脑

---

## 🔗 **知识图谱关联**

### 核心关联

- **B2B GTM策略**: [b2b-gtm-consulting-strategy.md](./b2b-gtm-consulting-strategy.md) — 战略框架，本Wiki为工程实现
- **AI-First战略**: [ai-first-strategy-critical-perspective.md](./ai-first-strategy-critical-perspective.md) — 真AI-First需要此类知识沉淀
- **OpenClaw案例**: [openclaw-case-studies-10-examples.md](./openclaw-case-studies-10-examples.md) — OpenClaw是Agent，Repository是给它的知识库
- **技能分层**: [skill-layered-consulting-application.md](./skill-layered-consulting-application.md) — Repository是技能分层的实现载体

### 🔄 关联解释

- **与B2B GTM**: 战略需要落地工具，Repository是GTM知识的工程化
- **与AI-First**: 真AI-First要求组织将知识沉淀为机器可执行形式
- **与OpenClaw**: OpenClaw作为AI员工，需要Repository这样高质量上下文
- **与技能分层**: Repository将原子层技能（方法论）组织为可使用形态

---

## 🎯 **6个月行动计划**

1. **搭建**: 构建AI咨询Repository（CLAUDE.md + Context Files）
2. **技能**: 开发3个核心skills（定价诊断/GTM评估/组织转型）
3. **自动化**: Claude Code实现报告自动生成（目标：50%自动化）
4. **迭代**: 完成3个项目后，提炼更新，提升质量
5. **产品化**: 将Repository作为"AI咨询知识平台"对外提供

---

**核心思想**: GTM Repository是将GTM知识体系化、工程化、AI可执行的典范。你的AI咨询业务应建立自己的Repository，将方法论沉淀为结构化的markdown知识库，用Claude Code实现半自动化交付，大幅提升人效和一致性。

---

**生成时间**: 2026-05-03
**基于RAW**: [gtmstrategist_GTM Repository for Claude Code_20260415.md](../raw/gtmstrategist_GTM Repository for Claude Code_20260415.md)
**核心框架**: 五层架构（CLAUDE.md → Context → Skills → Workflows → Outputs）
**战略定位**: AI咨询知识工程化（GTM知识脑）
**关键案例**: GTM Strategist的Repository（可直接借鉴）