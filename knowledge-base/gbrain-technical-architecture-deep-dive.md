# GBrain技术架构深度解析：Fat Skills + Fat Code + Thin Harness

**来源**: Garry Tan (YC CEO) 技术长文
**整理日期**: 2026-05-12
**核心价值**: GBrain完整技术栈 + 开源实现 + Skills架构 + 复利系统设计

---

> **本文是 `gbrain-personal-knowledge-system-2026.md` 的技术架构补充篇**
> 上一篇侧重"为什么"（元元提示法/复利增长），本篇侧重"怎么做"（技术实现/开源代码）

---

## 🎯 核心架构公式

```
GBrain = Fat Skills（胖技能） + Fat Code（厚代码） + Thin Harness（薄壳）
```

**Harness很薄**：几千行路由逻辑，什么都不知道，只负责分发
**Skills很厚**：100+个自包含Markdown文件，每个专注一件事
**Code很厚**：转写/OCR/归档/集成脚本，真正产生复利的是数据
**Models可替换**：由skill决定调用哪个模型，Harness不关心

> **"模型只是引擎。其他所有东西，才是车。"**

---

## 四大核心组件

### 1. Harness（薄壳，几千行）

**OpenClaw**: 接收消息 → 判断调用哪个skill → 分发

**关键设计**: Harness不知道书籍、会议、创始人是什么。它只负责路由。

**类比**: 一辆车的底盘和引擎。底盘不关心载什么货，只管怎么跑。

**部署选项**:
- 家里闲置电脑 + Tailscale（低成本）
- Render / Railway 云平台（省心）
- 从零自己写（完全控制）

---

### 2. Skills（胖技能，100+）

每个skill是自包含的Markdown文件，包含具体任务的详细指令。

**核心Skills清单**:

| Skill | 功能描述 | 调用关系 |
|-------|---------|---------|
| `book-mirror` | 书镜：每章总结 + 人生映射 | brain-ops + enrich + cross-modal-eval + pdf-generation |
| `meeting-prep` | 会议准备：人物页面 + 立场数据库 + 演示脚本 | brain-ops + enrich |
| `meeting-ingestion` | 会议吸收：文字稿 → 摘要 → 实体传播 | brain-ops |
| `enrich` | 人物丰富：5源合并 → brain page | brain-ops |
| `media-ingest` | 媒体摄入：视频/音频/PDF/GitHub | brain-ops |
| `perplexity-research` | 脑增强研究：brain先查 → 再网络搜索 | brain-ops + perplexity |
| `email-triage` | 邮件分类 | brain-ops |
| `investor-update-ingest` | 投资组合更新识别 + 指标抽取 | brain-ops |
| `calendar-check` | 日程冲突检查 | calendar-api |
| `cross-modal-eval` | 跨模型评估：三模型互评 | opus + gpt + deepseek |
| `check_resolvable` | 验证skill接入resolver | resolver |

**Skills可组合**: 一个工作流调用多个skill，每个skill只做一件事

**改进一个skill → 所有使用它的工作流自动变好**

---

### 3. Data（厚数据，10万页）

**三层Schema**:
```
Compiled Truth（当前最佳理解）
    ↓
Append-Only Timeline（只增不减的时间线）
    ↓
Raw Sidecars（原始资料来源）
```

**实体类型**:
- **人**: 时间线 + 当前状态 + 开放事项 + 评分
- **公司**: 业务指标 + 动态 + 关联人物
- **会议**: 文字稿 + 摘要 + Entity Propagation
- **书**: 逐章Book Mirror（3万字/本）
- **文章/播客/视频**: 吸收 + 标签 + 交叉引用

**Entity Propagation（实体传播）**: 每次会议后，系统遍历提到的每个人和每家公司，更新各自的brain page

**示例流程**:
```
Office hours见到创始人
    ↓
创建/更新个人页面
    ↓
更新公司页面
    ↓
交叉引用会议记录
    ↓
检查是否见过（浮出上次讨论）
    ↓
提取申请资料
    ↓
拉取最新指标
    ↓
匹配投资组合联系人
    ↓
下次见面前 → 完整上下文包已准备好
```

---

### 4. Models（可替换零件）

**多模型路由**（由skill决定用哪个）:

| 模型 | 用途 | 优势 |
|------|------|------|
| Opus 4.7 1M | 精确性任务 | 事实精确 |
| GPT-5.5 | 召回和穷尽式提取 | 上下文完整 |
| DeepSeek V4-Pro | 创意工作和第三视角 | 泛化检查 |
| Groq + Llama | 速度优先 | 快 |

> **"当有人问'哪个AI模型最好'时，答案是：你问错问题了。模型只是引擎。"**

---

## Skillify元技能：技能造技能

**Skillify = Meta-Skill**（元技能）：负责创造新的skills

**循环**:
```
遇到将来会重复使用的工作流
    ↓
"skillify this"
    ↓
检查发生了什么
    ↓
提取可重复模式
    ↓
写成测试过的skill文件（触发条件+边界情况）
    ↓
注册到resolver
    ↓
每一次修复复利到所有未来使用
```

**递归结构**:
```
Harness → 路由 → Skills → 工作流 → 结果
                ↑
            由Skillify创建
```

**真实案例**:
- **Book-mirror**: 从第一次手动尝试后被skillify出来
- **Meeting-prep**: 从发现每次开会前做同样步骤后被skillify出来
- **跨模型评估**: 从第一次book-mirror事实错误修复后被skillify出来

---

## Book Mirror技术细节

**第一次**: 效果很糟糕
- 说父母离婚了（实际没离）
- 说在香港长大（实际加拿大出生）

**强制事实核查步骤**:
- Opus 4.7 1M：精确性
- GPT-5.5：上下文完整性
- DeepSeek V4-Pro：泛化检查

**第三版升级**: 针对每个小节brain搜索，每项引用真实brain page

**40分钟 vs 治疗师40小时**:
- 治疗师无法同时加载并交叉引用完整职业背景/阅读历史/会议记录/创始人关系图谱
- GBrain可以

**已处理20+本书**: 每本书都变得更丰富，因为brain本身也在变得更丰富

---

## 10万页Brain vs 聊天机器人

| 维度 | 文件柜（聊天机器人） | 神经系统（GBrain） |
|------|-------------------|-----------------|
| 存储 | 被动保存 | 主动更新 |
| 连接 | 孤立信息 | 信息互联 |
| 变化 | 静态 | 标记变化 |
| 浮现 | 需主动搜索 | "此刻最相关"自动浮现 |
| 复利 | 无 | 每次使用都变好 |
| 上下文 | 单次对话 | 10万页历史 |

---

## 开源技术栈

**GitHub**: github.com/garrytan/gbrain

| 项目 | 说明 | Stars |
|------|------|-------|
| GStack | 代码skill框架 | 87,000+ |
| GBrain | 知识基础设施 | - |
| OpenClaw | Harness选项1 | - |
| Hermes Agent | Harness选项2 | - |
| 30+ skillpacks | 可安装skills | - |

**LongMemEval召回率**: 97.6%（不使用LLM的检索环节超过MemPalace）

---

## 🔗 关联知识

### 直接关联
- `gbrain-personal-knowledge-system-2026.md` - GBrain主文件（元元提示法/复利增长）
- `ai-agent-paradigm-shift-backend-agents-2026.md` - Agent范式解耦（后台Agent需求）
- `ai-agent-ecosystem-stack.md` - Agent生态栈（Harness/Skills/Models分层）
- `agent-memory-sovereignty-framework.md` - Agent记忆主权（10万页brain = 数据主权）
- `openclaw-case-studies-10-examples.md` - OpenClaw案例（Harness实战）
- `skill-layered-architecture.md` - 技能分层架构（Skillify = 元技能）
- `context-engineering-framework.md` - Context工程（跨模型评估 = 质量控制）

### 关联类型
- 🎯 **架构-实施关联**: Fat Skills + Fat Code + Thin Harness → 可复制架构
- 🔬 **实证-开源关联**: 97.6%召回率 + 87K stars = 技术可信度
- 🔄 **递归-元技能关联**: Skillify创建Skills → 技能造技能的递归结构
- 💡 **复利-数据关联**: 10万页brain + 100+ cron = 复利系统

---

## 💡 对AI咨询业务的战略启示

### 产品线1：GBrain技术实施服务

**客单价**: ¥100-200K（4-6周）
**目标客户**: 知识工作者（投资人/创始人/高管/专家）

**交付内容**: 基于开源GBrain的定制化部署

1. **Harness搭建**（1周）：OpenClaw/Hermes Agent配置 + 路由逻辑
2. **Skills定制**（2-3周）：20-30个核心skills（会议备忘/人物研究/书镜/邮件分类等）
3. **Data迁移**（1周）：导入历史邮件/会议/笔记/阅读数据
4. **跨模型评估配置**（1周）：三模型互评框架部署
5. **培训交付**（1天）：使用培训 + 持续支持30天

**技术栈**: OpenClaw + GBrain + 客户自有模型API

**价格分层**:
- **基础版**: ¥80-120K（10个skills + 基础brain）
- **专业版**: ¥120-200K（30个skills + 完整跨模型评估）
- **企业版**: ¥200-400K（50+skills + 团队协作 + SLA）

---

### 产品线2：GBrain工作坊与技术培训

**形式**: 3天深度工作坊（¥30-50K/人，10-15人）
**目标**: 教会参与者自己搭建GBrain系统

**Day1: 架构原理**
- Fat Skills + Fat Code + Thin Harness设计哲学
- 10万页Brain的三层Schema
- 开源技术栈概览（GStack/GBrain/OpenClaw）

**Day2: 实战搭建**
- 从零搭建Harness（OpenClaw配置）
- 创建第一个skill（book-mirror或meeting-prep）
- 配置跨模型评估框架
- 导入第一批数据

**Day3: Skillify循环**
- 识别可复用工作流
- 运行Skillify提炼skill
- 部署到resolver
- 建立100+ cron任务自动化

**产出**: 每个学员带走一个可运行的GBrain MVP（3-5个skills）

---

### 产品线3：GBrain Skills定制开发

**客单价**: ¥10-30K/skill
**商业模式**: 按需定制skills + Skillify服务

**标准化Skills库**（¥10K/个，可直接安装）:
| Skill | 功能 | 适用场景 |
|-------|------|---------|
| 书镜标准版 | 章节摘要 + 个人映射 | 知识工作者阅读 |
| 会议备忘增强 | 人物背景 + 立场 + hooks | 创始人/投资人 |
| 邮件智能分类 | 优先级 + 摘要 + 行动项 | 所有人 |
| 投资组合监控 | 指标抽取 + 异常预警 | 投资人 |
| 内容研究助手 | 脑增强搜索 + 交叉引用 | 研究者/写作者 |

**定制开发**（¥20-30K/skill）: 针对客户特定工作流的skill开发 + Skillify提炼

---

## 📈 关键指标

| 指标 | 当前GBrain | 6个月后目标 |
|------|-----------|-----------|
| Brain页数 | 100,000页 | 300,000+页 |
| Skills数量 | 100+ | 200+ |
| Cron任务 | 100+ | 200+ |
| 书籍处理 | 20+本 | 100+本 |
| 会议准备 | 实时 | 自动化95% |
| 复利倍数 | 10x/2月 | 10x/2月（持续）|

---

## 🔗 知识关联网络

**核心关联Wiki**:
- `gbrain-personal-knowledge-system-2026.md` - GBrain主文件（必读前置）
- `ai-agent-paradigm-shift-backend-agents-2026.md` - Agent范式（Harness = 编排层）
- `ai-agent-ecosystem-stack.md` - Agent生态栈（四层架构对应）
- `agent-memory-sovereignty-framework.md` - Agent记忆主权
- `openclaw-case-studies-10-examples.md` - OpenClaw案例
- `skill-layered-architecture.md` - 技能分层（Skillify = 元技能）
- `context-engineering-framework.md` - Context工程（跨模型评估）

**关联强度**: 极强（与GBrain主文件双向引用，7个技术架构Wiki）

---

## 📊 归档统计

- **原始内容**: 8,123字符（Garry Tan GBrain技术架构长文）
- **Wiki文件**: 本文件（约7,500字节，技术架构补充）
- **关联Wiki**: 7个（全部为技术架构类）
- **关联强度**: 极强
- **商业价值**: 高（3条产品线：实施服务/工作坊/Skills定制）
- **市场时机**: 极佳（开源+87K stars，技术可信度极高）

---

**报告生成时间**: 2026-05-12 23:05 CST
**归档质量**: A级（技术细节丰富、开源可验证、架构清晰）
**建议下一步**: 立即部署GBrain MVP + 准备技术工作坊

**核心钩子**: "Fat Skills + Fat Code + Thin Harness：Garry Tan的GBrain架构如何实现10万页复利大脑"

---
