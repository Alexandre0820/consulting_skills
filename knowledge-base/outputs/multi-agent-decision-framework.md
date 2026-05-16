# Multi-Agent决策框架：从Subagents到Agent Teams的战略选择

**直接关联Wiki**: [multi-agent-subteams-framework.md](./multi-agent-subteams-framework.md)
**直接关联RAW**: [multi-agent-subteams-judgment.md](../raw/multi-agent-subteams-judgment.md)

---

## 🎯 **核心洞察：不要过早复杂化**

**一句话总结**：
> "一次性委派问题 → 用 Subagents；长期协作问题 → 用 Agent Teams"

**升级顺序**（大多数团队应该遵循）：
```
Single Agent
  ↓
更好的工具使用
  ↓
Subagents (轻量级，默认第一层升级)
  ↓
Orchestrator-Subagent
  ↓
Agent Teams (长期协作，证据明确再上)
  ↓
Message Bus / Shared State (超复杂场景)
```

**关键数字**：
- Multi-agent比single agent消耗**3-10倍token**
- Subagents适合**上下文隔离+并行探索**
- Agent Teams适合**长期记忆+持续同步**

---

## 💡 **对AI咨询业务的战略意义**

### 1. 这是"AI实施"的重要分支

**客户痛点**：
- AI Agent在处理复杂任务时遇到瓶颈（上下文溢出、稳定性差）
- 不知道何时该从single agent升级到multi-agent
- 更不知道选择subagents还是agent teams

**你的机会**：
- 提供**诊断服务**（评估是否需要multi-agent，推荐哪种模式）
- 提供**实施服务**（subagents配置或agent teams搭建）
- 建立**护城河**：multi-agent架构设计是复合技能（100x杠杆）

### 2. 避免"架构过早复杂化"陷阱

**常见客户错误**：
- 一开始就把简单任务拆成 planner/developer/tester 链条
- 在不需要长期协作的场景硬上 agent teams
- 忽视协调成本，导致系统失控

**你的价值**：
- 用框架帮助客户**先做对第一层判断**
- 从简单方案开始，只在必要时升级
- 设计可观测性和停止条件，避免无限复杂化

---

## 💼 **你的Multi-Agent咨询产品线**

### 产品1: Multi-Agent架构诊断（5-10万）

**目标客户**：已有AI Agent应用但遇到瓶颈的企业

**交付物**：
1. **任务评估**：客户业务场景是否需multi-agent？
   - 上下文污染程度
   - 并行需求强度
   - 专业化必要性

2. **模式推荐**：subagents vs agent teams
   - 一次性委派 vs 长期协作判断
   - 成本收益分析（token消耗 vs 效果提升）

3. **实施路线图**
   - 技术选型建议
   - 团队能力准备度
   - 时间表和里程碑

4. **初步方案**：免费提供基础配置建议

**周期**: 2周
**转化**: 60% → 实施项目

### 产品2: Subagents实施（20-40万）

**目标客户**：确认需要multi-agent，适合subagents模式的客户

**交付**：
1. **角色设计**
   - 按上下文边界拆分子代理（不是按角色）
   - 明确每个subagent的职责、权限、工具集

2. **调用链配置**
   - 主代理→subagent委派机制
   - 并行执行设置
   - 结果汇总策略

3. **验证机制**
   - 独立reviewer subagent配置
   - 安全审查、schema检查、测试覆盖

4. **培训与支持**
   - 团队使用培训（2-3天）
   - 优化最佳实践
   - 3个月持续支持（问题排查、调优）

**周期**: 4-6周 + 3个月支持
**毛利率**: 70%

### 产品3: Agent Teams实施（50-100万）

**目标客户**：任务需要长期协作、稳定ownership的企业

**交付**：
1. **团队角色设计**
   - 按服务/模块/研究方向划分成员
   - 每个成员长期负责一块（积累局部记忆）
   - 明确职责、输入、交付物

2. **协调机制搭建**
   - 消息协议（同步频率、格式）
   - 依赖管理（谁依赖谁）
   - 冲突解决规则

3. **可观测性建设**
   - 日志和回放系统
   - 进度追踪仪表板
   - 轮次限制和终止条件
   - 失败重试规则

4. **长期优化**
   - 6-12个月持续迭代
   - 记忆管理优化
   - 协作模式调优

**周期**: 2-3个月部署 + 6-12个月优化
**毛利率**: 60%

---

## 📊 **与技能分层的对应关系**

| 技能层级 | Multi-Agent模式 | 你的产品定位 |
|---------|-----------------|--------------|
| **原子层** | Single Agent | 不提供（ commoditized） |
| **分子层** | Subagents | 引流产品（20-40万） |
| **化合物层** | Agent Teams | 核心产品（50-100万） |

**战略重点**：帮助客户从原子层→分子层→化合物层跃迁，这正是Karpathy"理解是护城河"的体现。

---

## 🔗 **知识网络强化**

### 核心网络
```
Multi-Agent决策框架
    ↓ 技术支撑
Single→Subagents→Agent Teams升级顺序
    ↓ 价值体现
帮客户选择正确架构（避免过早复杂化）
    ↓ 商业转化
诊断→Subagents实施→Agent Teams实施
```

### 与核心主题关系

- **与技能分层**: Subagents是分子层，Agent Teams是化合物层，对应100x杠杆
- **与Karpathy**: 选择正确模式需要"理解问题本质结构"（上下文vs协作问题）
- **与AI Native组织**: Multi-agent是AI Native组织的技术基础（组织扁平化需要agent teams支撑）
- **与Perplexity增长**: Perplexity产品简洁性提醒我们**不要过早复杂化**，与框架哲学一致
- **与YC AI服务警示**: Multi-Agent实施服务容易陷入"价值捕获困境"，必须产品化+高价值定位

---

## 🎯 **内容创作方向**

### LinkedIn
1. **"Subagents还是Agent Teams？先回答这两个问题"**
2. **"为什么大多数团队把Multi-Agent搞复杂了？"**
3. **"从Single Agent到Agent Teams：升级的5个信号"**
4. **"Multi-Agent成本3-10倍token，你准备好了吗？"**

### 微信公众号
1. **"Multi-Agent决策白皮书：何时升级，如何选择"**（6000字）
2. **"案例分析：XX公司如何用Subagents节省40% token"**
3. **"Agent Teams实战：长期协作系统的5个护栏"**

### 小红书
1. **"AI Agent架构选择：一张表帮你决定"**
2. **"我做Multi-Agent踩过的3个大坑"**

---

## 🚀 **30-60-90天行动计划**

### 30天：产品化+内容
- 完成"Multi-Agent诊断"标准化问卷（在线工具）
- 设计"Subagents vs Agent Teams"决策矩阵（一页纸）
- 发布首篇LinkedIn（决策框架解读）
- 准备2个免费诊断（试点）

### 60天：首批客户
- 筛选20个目标（已有AI Agent应用的科技公司）
- 提供免费1小时"Multi-Agent评估"
- 目标: 签约3个诊断（5-10万）

### 90天：案例沉淀
- 完成5个诊断 + 1个Subagents实施项目
- 产出完整案例（token消耗对比、效果数据）
- 发布"Multi-Agent决策白皮书"

---

## ⚠️ **风险与应对**

| 风险 | 概率 | 影响 | 应对 |
|------|------|------|------|
| 客户过早复杂化 | 高 | 高 | 用诊断产品教育，强调"先轻后重" |
| 技术快速迭代 | 中 | 中 | 保持架构中立，聚焦模式而非工具 |
| token成本超预期 | 高 | 中 | 性能监控+成本预警机制 |
| 竞争（AI实施公司） | 中 | 低 | 突出"架构决策"专业性，不是单纯实施 |
| 客户需求不明确 | 高 | 中 | 诊断产品帮助澄清，分期交付 |

---

## 🏆 **6个月成功指标**

1. **内容**: Multi-Agent系列（LinkedIn 8万+阅读，公众号1篇白皮书）
2. **诊断**: 完成15个Multi-Agent架构诊断，转化率40%
3. **实施**: 签约2个Subagents项目（平均30万）+ 1个Agent Teams项目（80万）
4. **案例**: 1个完整实施案例（含token节省数据、效果提升）
5. **方法论**: 建立"Multi-Agent决策框架"知识产权

---

**核心思想**: Multi-Agent不是"越强越好"，而是"越合适越好"。你的价值是帮客户做对第一层判断，避免过早复杂化，这正是Perplexity和YC W26共同强调的"简洁性哲学"。

---

**生成时间**: 2026-05-03
**基于RAW**: [multi-agent-subteams-judgment.md](../raw/multi-agent-subteams-judgment.md)
**核心框架**: Single Agent → Subagents → Agent Teams
**决策公式**: 一次性委派用subagents，长期协作用agent teams
**成本警告**: Multi-agent消耗3-10倍token，必须收益>成本