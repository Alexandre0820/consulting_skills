# Multi-Agent系统决策框架：Subagents vs Agent Teams

## 知识图谱链接

### 关联文章
- **[Subagents 还是 Agent Teams？先做对 Multi-Agent 的第一层判断](file:///Users/shengyun/lobsterai/project/my-ai-consulting-kb/raw/multi-agent-subteams-judgment.md)** (2026-04-27)
- **[AI Agent生态分层框架](file:///Users/shengyun/lobsterai/project/my-ai-consulting-kb/wiki/agent-harness-architecture-framework.md)** - 架构对比
- **[Agentic营销栈框架](file:///Users/shengyun/lobsterai/project/my-ai-consulting-kb/wiki/agentic-marketing-stack-framework.md)** - 应用对比
- **[技能分层架构](file:///Users/shengyun/lobsterai/project/my-ai-consulting-kb/wiki/skill-layered-architecture.md)** - 能力层次对比

## 核心概念解析

### Subagents vs Agent Teams 对比维度

**Subagents（子代理）**：
```
├─ 单个Agent的分解任务
├─ 简单协作机制
├─ 低复杂度管理
└─ 快速部署
```

**Agent Teams（代理团队）**：
```
├─ 多个独立Agent协作
├─ 复杂协调机制
├─ 高管理能力要求
└─ 需要长期优化
```

### 第一层判断标准（基于Subagents vs Agent Teams深度分析）

#### 1. 是否应该从single agent升级到multi-agent？

**触发条件（满足任一即考虑）**:
- **上下文污染**: 主代理被支线任务拖慢，注意力被稀释
- **并行需求**: 子任务天然独立，可并行处理（如检查多个服务、并行研究）
- **专业化需求**: 单一代理需要掌握太多工具/领域，稳定性下降

**成本考量**: multi-agent消耗3-10倍token，必须确认收益>成本

#### 2. 如果multi-agent，选择subagents还是agent teams？

**一句话判断**:
- **一次性委派问题** → 用 **subagents**
- **长期协作问题** → 用 **agent teams**

**Subagents适用场景**:
1. **上下文隔离需求**: 主线程被支线拖慢（如实现支付时查认证、邮件、shared util）
2. **并行探索**: 同时排查多个模块的TypeScript错误、并行安全检查/性能检查
3. **独立reviewer**: 需要不受历史对话影响的第二视角（安全审查、边界检查、测试覆盖）
4. **轻度专业化**: security-reviewer、perf-reviewer、schema-checker等固定角色

**Agent Teams适用场景**:
1. **跨多轮持续推进**: 任务需要数天/周，成员需积累局部记忆（如代码库迁移、长周期重构）
2. **稳定ownership**: 每个成员长期负责一个服务/模块，建立上下文复利
3. **持续同步**: 协作从"结果汇总"变为"过程同步"，需要频繁交流依赖和进度

**复杂度对比**:
| 维度 | Subagents | Agent Teams |
|------|-----------|-------------|
| 生命周期 | 临时、一次性 | 持续、可重复唤醒 |
| 记忆 | 通常不留长期记忆 | 成员保留局部记忆 |
| 通信模式 | 父代理汇总结果 | 持续同步进度 |
| 复杂度 | 低-中 | 中-高 |
| 默认建议 | **先用它** | 证据明确再上 |

#### 3. 其他multi-agent模式（全景图）

除subagents/agent teams外，至少还包括：
- **Generator-verifier**: 先生成再验证（适合有明确标准的任务）
- **Orchestrator-subagent**: 协调层+子代理（常见于Claude Code）
- **Message bus**: 事件驱动工作流
- **Shared state**: 共享黑板式协作（研究型任务）

**但大多数团队的第一个分叉点**:
一次性委派（subagents） vs 长期协作（agent teams）


## 与企业应用的关系

### 企业AI转型中的Agent编排

**适用场景分析**：

| 业务场景 | Subagents推荐 | Agent Teams推荐 |
|---------|--------------|----------------|
| 简单自动化 | ✅ | ❌ |
| 复杂流程 | ⚠️ | ✅ |
| 跨部门协作 | ❌ | ✅ |
| 单一任务 | ✅ | ⚠️ |
| 多任务并行 | ❌ | ✅ |

### 组织影响

**Subagents模式**：
- **组织结构**：最小变化
- **管理复杂度**：低
- **培训成本**：低
- **ROI周期**：短

**Agent Teams模式**：
- **组织结构**：需要专门协调角色
- **管理复杂度**：高
- **培训成本**：高
- **ROI周期**：长但价值大

## 与现有知识体系的关联

### 与OpenClaw平台
```
Subagents模式 ←→ OpenClaw子代理
├─ 任务分解 ←→ 子任务分配
├─ 简单协作 ←→ 工具调用链
└─ 快速迭代 ←→ 敏捷开发

Agent Teams模式 ←→ OpenClaw多智能体
├─ 复杂协调 ←→ 工作流引擎
├─ 长期优化 ←→ 持续学习
└─ 价值创造 ←→ 端到端解决方案
```

### 与AI咨询业务
```
决策框架 ←→ 咨询服务方法论
├─ 问题诊断 ←→ 需求分析
├─ 方案选择 ←→ 产品推荐
└─ ROI评估 ←→ 价值证明
```

## 实施指南（基于完整文章）

### 核心前提：共享记忆是协作的地基

**为什么记忆不够？**
- 当前智能体记忆是"单机游戏"：Claude记住你的偏好，Cursor记住项目结构——但它们不通气
- 智能体数量增长时，问题指数爆炸：每多一个智能体，需要同步的信息通道多出好几条
- **核心洞察**: 智能体需要"可以共同推理的、结构化的共享上下文"

**Multi-Agent架构选择 = 协作架构设计**。选择subagents还是agent teams，本质是决定：
- 一次性委派 → subagents（无需长期记忆）
- 长期协作 → agent teams（需要共享记忆+局部记忆）

### 如何使用 Subagents（五步法）

1. **按上下文边界拆，不按角色拆**
   - ❌ 不要拆成 planner/developer/tester
   - ✅ 问：哪些任务可以不共享核心上下文独立完成？

2. **任务边界、返回格式、并行要求要写清楚**
   - 好例子："请用subagents并行探索：1)认证链路 2)邮件入口 3)shared util复用"
   - 关键：任务独立、明确并行、只回摘要（不要原始文件）

3. **工具和权限尽量收紧**
   - 研究型subagent → 只读权限
   - 实现型subagent → 写权限
   - 工具越聚焦，输出越稳定

4. **把验证工作单独成subagent**
   - 独立reviewer做：跑测试、检查schema、安全审查、验收review
   - 避免主代理自己实现自己审查

5. **先对话式委派，再沉淀成自定义subagent**
   - 先在对话里调用，跑顺了再固化
   - 避免过早写死半成熟流程

### 如何使用 Agent Teams（五步法）

1. **先证明subagents确实不够**
   出现这些现象再升级：
   - 同工作线跨多轮持续推进
   - 成员需要保留局部记忆（不想每次重灌背景）
   - 重复拉起subagent成本过高
   - 协作问题>上下文问题

2. **按负责范围和上下文组队，不按岗位**
   - 按服务/模块/研究方向/系统边界划分
   - 让成员长期负责同一块，积累上下文复利

3. **给每个成员稳定职责、输入、交付物**
   - 谁负责哪条线？
   - 谁可以改什么？
   - 什么信息必须同步？
   - 每轮输出什么摘要？
   - （没有护栏，团队会变成互相打断的代理）

4. **设计好协调层，不只是成员**
   协调层负责：
   - 分发任务
   - 跟踪进度
   - 处理依赖
   - 决定何时汇总
   - （不一定中心化，但要有稳定协议）

5. **一开始就补可观测性和停止条件**
   - 日志和回放
   - 轮次限制
   - 终止条件
   - 失败重试规则
   - 冲突处理规则
   - （agent teams常死于协作失控，不是能力不足）

### 推荐的升级顺序

```
Single Agent
  ↓
更好的工具使用
  ↓
Subagents
  ↓
Orchestrator-Subagent
  ↓
Agent Teams
  ↓
Message Bus / Shared State
```

**逻辑**: 先解决上下文问题，再解决协作问题；先轻后重。

**常见错误**: 架构过早复杂化（把简单问题搞复杂）

---

## 与AI咨询业务的关联

### 诊断框架：客户需要哪种Multi-Agent模式？

| 评估维度 | Subagents线索 | Agent Teams线索 |
|----------|---------------|-----------------|
| 任务性质 | 一次性/短期委派 | 长期持续（数周+） |
| 上下文需求 | 可隔离，不需记忆 | 需保留局部记忆 |
| 并行度 | 多任务独立并行 | 多任务持续协作 |
| 专业化 | 轻度（1-2个工具） | 深度（长期负责一个领域） |
| 协调成本容忍度 | 低 | 中-高 |

### 服务产品建议

#### 产品A: Multi-Agent架构诊断（5-10万）
- 评估客户任务是否需multi-agent
- 推荐subagents还是agent teams
- 给出实施路线图和成本估算

#### 产品B: Subagents实施（20-40万）
- 设计subagent角色和权限
- 配置工具和调用链
- 培训团队使用和优化
- 3个月支持

#### 产品C: Agent Teams实施（50-100万）
- 团队角色设计（长期ownership）
- 协调机制搭建（消息协议、同步规则）
- 可观测性建设（日志、追踪、停止条件）
- 6-12个月持续优化

### 与技能分层的关联

| 技能层级 | Multi-Agent应用 |
|---------|-----------------|
| 原子层 | 单一agent执行基础任务 |
| 分子层 | Subagents并行/专业化 |
| 化合物层 | Agent Teams长期协作 |

**关键洞察**: multi-agent升级本质是从原子层→分子层→化合物层的跃迁。

---

## 🔗 **知识图谱关联**

### 👉 你应同步阅读
- **AI Native组织**: [ai-native-organization-consulting-framework.md](./ai-native-organization-consulting-framework.md) — 组织层面的人机协作架构
- **技能分层**: [skill-layered-consulting-application.md](./skill-layered-consulting-application.md) — 100x杠杆与compound skills
- **Karpathy哲学**: [karpathy-ai-philosophy-strategy.md](./karpathy-ai-philosophy-strategy.md) — "理解是护城河"在multi-agent中的体现
- **Perplexity增长**: [perplexity-growth-engines.md](./perplexity-growth-engines.md) — 产品架构的简洁性哲学

### 🔄 **关联关系说明**
- **与AI Native组织**: Multi-agent架构是AI Native组织的**技术实现基础**（组织扁平化需要agent teams支撑）
- **与技能分层**: Subagents→Agent Teams对应分子层→化合物层的跃迁
- **与Karpathy**: 选择合适的multi-agent模式需要"理解"问题本质结构
- **与Perplexity**: Perplexity的产品简洁性提醒我们：**不要过早复杂化**

---

**关联RAW**: [multi-agent-subteams-judgment.md](../raw/multi-agent-subteams-judgment.md)
**来源**: AI趣实验微信公众号，2026-04-27
**关键作者**: 基于Claude官方博客和多篇论文
**核心框架**: Single Agent → Subagents → Agent Teams 升级顺序
**决策公式**: 一次性委派用subagents，长期协作用agent teams

---

## 🔄 **共享记忆：Agent Teams的地基**

### 为什么需要共享记忆？

**现状问题**: 
- 单机游戏：每个智能体有私人笔记本，但不互通
- 指数级问题：智能体数量增长，同步成本爆炸
- **本质**: 不是记忆力问题，是协作架构问题

**共享记忆的价值**: 
- **知识复利**: 一个智能体的发现，全团队受益
- **决策追溯**: 谁做了什么决策，为什么，可回溯
- **避免重复**: 新智能体继承团队知识，不走回头路

### 实现方案：上下文图谱（Context Graph）

Karpathy实践: 用LLM构建结构化维基系统
- 智能体对知识库进行编译、查询、一致性检查
- 每次对话结果回流到知识库 → 知识体量增长，质量持续提升
- 形成"个人知识操作系统"

企业级应用: 
```
企业知识库 ←→ 共享记忆图谱 ←→ AI Agent团队
     ↑                     ↑
  人工知识            团队协作上下文
     ↓                     ↓
  历史决策            实时状态同步
```

### 实施建议

1. **选择共享记忆平台**
   - 自建: Notion API + 向量数据库
   - 商用: 已有知识管理工具+AI插件
   - 开源: ResearchGraph、MemGPT等

2. **设计知识结构**
   - 分层: 战略层 → 战术层 → 执行层
   - 分类: 项目知识、客户知识、技术知识、决策日志
   - 版本: 每次重大更新保留历史，支持diff

3. **集成到Agent Teams**
   - 每次任务开始：载入相关知识片段
   - 任务完成：输出沉淀到共享记忆
   - 定期：知识质量审查（去重、合并、归档）

4. **可观测性**
   - 知识使用统计（哪些被频繁引用）
   - 冲突检测（不同智能体对同一知识的理解不同）
   - 完整性检查（知识缺口识别）

---