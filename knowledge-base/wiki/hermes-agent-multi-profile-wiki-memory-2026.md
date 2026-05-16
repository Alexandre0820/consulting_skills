# Hermes Agent高级用法：多Profile协作 + Wiki共享记忆 = OPC团队

> 来源：ihuanzhao / 龙虾之心 | 2026-05-14
> 原文：https://mp.weixin.qq.com/s/sx7EoHUKaGAxplmLboByiw
> 节点：#61

---

## 一、核心框架：OPC = 多Agent协作

```
OPC（一人公司）= 一个人 + 多个Agent + 共享记忆层（Wiki）

不是一个人单打独斗
而是像管理一支小团队一样管理多个Agent
```

**三大支柱**：
1. **多Profile**：角色分工（Researcher/Writer/Builder/Coordinator）
2. **Wiki共享记忆**：长期上下文，避免每次重复粘贴
3. **分层模型策略**：主模型（复杂）+ 副模型（总结）+ 本地模型（简单）

---

## 二、四角色模型

| 角色 | 职责 | 核心能力 | 使用频率 |
|------|------|---------|---------|
| **Researcher** | 事实核查 | 查资料、数据、案例 | 高 |
| **Writer** | 表达输出 | 写文章、润色、排版 | 高 |
| **Builder** | 技术实现 | 写代码、配置、调试 | 中 |
| **Coordinator** | 统筹协调 | 分配任务、整合结果 | 中 |

**为什么需要多角色**：
- 单一Agent最大的问题：自己写、自己审、自己觉得没问题
- 多角色 = 不同视角审视同一问题 = 更容易发现漏洞

---

## 三、Wiki八层结构

### 3.1 Wiki作为"公司文档"

```
Layer 1: 基础信息层 — 公司背景/个人档案/联系方式
Layer 2: 知识资产层 — 方法论/框架/模板
Layer 3: 项目历史层 — 历史项目/复盘/经验教训
Layer 4: 客户资产层 — 客户信息/需求/交付历史
Layer 5: 人脉网络层 — 联系人/关系/合作方
Layer 6: 工作流层 — SOP/流程/检查清单
Layer 7: 灵感捕捉层 — 碎片化想法/创意/观察
Layer 8: 元信息层 — 索引/目录/使用说明
```

### 3.2 Wiki vs Profile 边界划分

| 维度 | Wiki | Profile |
|------|------|---------|
| **生命周期** | 长期（永久记忆） | 短期（会话级） |
| **内容性质** | 事实/数据/模板 | 角色设定/任务上下文 |
| **更新频率** | 低频（整理后更新） | 高频（每次对话更新） |
| **访问范围** | 所有Profile共享 | 仅所属Profile |
| **容量限制** | 无限制（按需读取） | 有Token限制 |

**核心原则**：不要让模型记住所有东西，要让模型按需读取正确的信息。

---

## 四、多Profile协作流程

### 4.1 标准工作流

```
Coordinator（统筹）
    ↓ 分配任务
Researcher（查资料）+ Writer（写初稿）并行
    ↓
Builder（实现/配置）
    ↓
Coordinator（整合+质量检查）
    ↓
Writer（最终润色）
    ↓
交付
```

### 4.2 工具分工

| 工具 | 角色 | 适用场景 |
|------|------|---------|
| **终端** | Builder/Coordinator | 搭系统、改配置、调试路径 |
| **Web UI** | 所有角色 | 日常协作、切换Profile、继续会话 |
| **Wiki** | 所有角色共享 | 长期记忆、知识资产、文档中心 |

**类比**：
- 终端 = 施工现场
- Web UI = 办公室
- Wiki = 公司文档

---

## 五、Token成本控制策略

### 5.1 成本问题

多Profile协作一定会比单Agent更耗Token，因为每个Profile都需要读取：
- 自己的身份设定
- 项目上下文
- Wiki资料

### 5.2 分层策略

| 层级 | 模型 | 用途 | 成本 |
|------|------|------|------|
| **主模型** | Claude/GPT-4 | 复杂推理/写作/分析 | 高 |
| **副模型** | Claude Sonnet/GPT-3.5 | 总结/整理/归档 | 中 |
| **本地模型** | Llama/Qwen | 简单任务/分类/提取 | 低 |
| **Wiki缓存** | 静态文件 | 长期上下文 | 极低 |

**核心策略**：不要让模型记住所有东西，要让模型按需读取正确的信息。

---

## 六、对AI咨询业务的战略启示

### 6.1 直接可用的产品线

**1. OPC团队搭建咨询** - ¥80-150K
- **交付物**：4角色模型搭建 + Wiki八层结构设计 + 工作流SOP
- **目标客户**：AI一人公司 / 小团队AI咨询
- **钩子**：用Wiki+多Profile实现"一个人管理一支Agent团队"
- **前置条件**：自身已跑通多Profile工作流

**2. Agent团队协作设计** - ¥60-120K
- **交付物**：角色分工方案 + 信息流转机制 + 质量控制节点
- **目标客户**：已部署多个Agent但协作效率低的企业
- **核心工具**：四角色模型 + Wiki边界划分框架

**3. Wiki知识架构设计** - ¥50-100K
- **交付物**：8层Wiki架构设计 + 信息分层策略 + 使用SOP
- **目标客户**：知识密集型AI应用公司
- **差异化**：Wiki vs Profile边界划分是独家框架

**4. Token成本优化咨询** - ¥30-60K
- **交付物**：分层模型策略 + 成本测算 + 优化方案
- **目标客户**：多Agent团队（Token成本已超¥5万/月）
- **钩子**：主+副+本地模型组合可降低40-60%成本

---

### 6.2 内容创作方向

**LinkedIn（4篇系列）**：

1. **《我用4个Agent搭了一个内容团队》**（实操演示）
   - Researcher/Writer/Builder/Coordinator四角色
   - 钩子：一个人 = 一支内容团队

2. **《OPC的核心不是一个人，而是一套系统》**（概念升级）
   - Wiki八层结构 + 多Profile协作
   - 钩子：一人公司≠单打独斗

3. **《多Agent协作的Token成本怎么降60%？》**（数据驱动）
   - 分层模型策略
   - 钩子：Token账单超过5万/月时的救命稻草

4. **《Wiki vs Profile：Agent记忆的边界在哪里？》**（方法论）
   - 记忆分层框架
   - 钩子：为什么你的Agent记不住关键信息

---

### 6.3 自我应用（立即可用）

**本周可做的**：
1. 在自己的知识库中应用Wiki八层结构重新组织
2. 在OpenClaw中尝试多Profile配置（Researcher/Writer/Builder/Coordinator）
3. 用分层模型策略优化自己的Token使用

---

## 七、关联知识

### 内部知识库
- [Hermes Agent深度分析](wiki/hermes-agent-analysis.md) — Hermes产品深度拆解
- [AI员工管理理论](ai-employee-management-theory.md) — Agent管理+鲁棒性维度
- [AI原生组织框架](ai-native-org-framework-v2.md) — AI原生组织形态
- [AI创业方法论](ai-entrepreneurship-methodology-2026.md) — OPC/一人公司
- [服务即软件](service-as-software-one-person-company-2026.md) — 一人公司商业模型
- [Personal Agent产品方法论](personal-agent-product-reflection-2026.md) — IM-based Agent
- [GBrain个人知识系统](gbrain-personal-knowledge-system-2026.md) — 个人知识管理
- [知识图谱索引](knowledge-graph-index.md) — 本知识库本身就是Wiki八层结构的实践

### 外部参考
- Hermes：AI Agent平台（支持多Profile + Wiki）
- OPC（One-Person Company）：一人公司概念
- OpenClaw：龙虾之心（本文作者也是OpenClaw社区成员）

---

## 七、关联知识

### 内部知识库
- **[Hermes Agent深度分析](hermes-agent-analysis.md)** — Hermes产品拆解，本文件是高级用法补充
- **[AI员工管理理论](ai-employee-management-theory.md)** — Agent管理+鲁棒性维度
- **[AI原生组织框架](ai-native-org-framework-v2.md)** — AI原生组织形态，多Agent协作的组织设计
- **[AI创业方法论](ai-entrepreneurship-methodology-2026.md)** — OPC/一人公司方法论
- **[服务即软件](service-as-software-one-person-company-2026.md)** — 一人公司商业模型
- **[Personal Agent产品方法论](personal-agent-product-reflection-2026.md)** — IM-based Agent + 隐私设计
- **[GBrain个人知识系统](gbrain-personal-knowledge-system-2026.md)** — 个人知识管理，Wiki即知识库
- **[知识图谱索引](knowledge-graph-index.md)** — 本知识库本身就是Wiki八层结构的实践

### 外部参考
- Hermes：AI Agent平台（多Profile + Wiki）
- OPC（One-Person Company）：一人公司概念
- OpenClaw：龙虾之心（本文作者也是OpenClaw社区成员）

---

## 八、待追踪

- [ ] 在自己知识库中应用Wiki八层结构并验证效果
- [ ] OpenClaw多Profile配置实验
- [ ] Hermes Agent vs OpenClaw功能对比
- [ ] Wiki八层结构在不同业务场景的适配性
- [ ] Token成本分层策略的实际节省数据
- [ ] 四角色模型在AI咨询项目中的实战验证
