# AI Native Organization Agent

一个**真正的智能Agent系统**，帮助你设计AI原生组织架构。

## ✨ 核心特性

- 🔍 **知识检索**：从知识大脑（165个Wiki + 155 Outputs）检索相关信息
- 📊 **智能诊断**：评估组织AI化程度，生成诊断报告
- 📋 **转型规划**：制定三阶段转型路线图，估算成本和时间
- 💰 **定价策略**：基于三层框架（Pilot/Standard/Enterprise）生成定价建议
- 📝 **引用溯源**：每个结论都标注来源，可验证
- 🌐 **远程知识库**：支持GitHub远程知识库（在线模式）

## 🎯 解决的问题

- 传统企业如何向AI原生组织转型？
- 如何评估组织当前AI化程度？
- 从传统组织到AI Native的转型计划？
- AI咨询如何定价？

## 🚀 快速安装

### 方法1：克隆仓库（推荐，Knowledge开源）

```bash
# 克隆Agent仓库
git clone https://github.com/Alexandre0820/consulting_skills

# 进入目录
cd consulting_skills

# 运行（Knowledge在GitHub上）
python3 agent.py "如何评估组织AI化程度？"
```

### 方法2：使用本地知识库

```bash
# 克隆Agent仓库
git clone https://github.com/Alexandre0820/consulting_skills

# 克隆知识库（可选）
git clone https://github.com/Alexandre0820/alex_knowledge_base

# 运行（指定知识库路径）
python3 agent.py --knowledge-path ../alex_knowledge_base "如何评估组织AI化程度？"
```

### 方法3：直接使用本地知识库

```bash
cd /Users/shengyun/lobsterai/project/skills/ai-native-org-skill
python3 agent.py "如何评估组织AI化程度？"
```

## 💬 使用方法

### CLI模式

```bash
# 远程模式（知识在GitHub）
python3 agent.py "我们公司有10人，用了一些AI工具，如何评估？"

# 本地模式（知识在本地路径）
python3 agent.py --knowledge-path /path/to/knowledge-base "如何评估？"

# 测试模式
python3 agent.py --test
```

### Python API

```python
from agent import AI_native_Org_Agent

# 远程模式（推荐）
agent = AI_native_Org_Agent(use_remote=True)

# 本地模式
agent = AI_native_Org_Agent(knowledge_dir="/path/to/knowledge-base")

# 诊断
report = agent.diagnose_organization("我们公司有10人，用了一些AI工具")
print(report)

# 转型计划
plan = agent.generate_transformation_plan("从传统组织到AI Native")
print(plan)

# 定价策略
strategy = agent.generate_pricing_strategy("Agent开发咨询")
print(strategy)

# 处理通用问题
answer = agent.ask("如何设计AI原生组织架构？")
print(answer)
```

## 📁 项目结构

```
consulting_skills/
├── agent.py                    # Agent核心引擎
├── agent-cli.py                # CLI工具
├── knowledge-retriever.sh      # 知识检索器
├── prompts/
│   └── system.md               # System Prompt
├── knowledge-base/
│   ├── KNOWLEDGE_INDEX.md      # 知识索引
│   ├── README.md               # 知识库说明
│   ├── wiki/                   # Wiki文档（165个）
│   ├── outputs/                # Outputs（155个）
│   └── raw/                    # RAW文件（88个）
├── README.md                   # 本文件
├── LICENSE
└── .gitignore
```

## 📚 知识库

### Knowledge开源

本项目的Knowledge库**完全开源**，包含：

- **165个Wiki文档**：完整的AI Native组织知识体系
- **155个Outputs**：实战案例和经验沉淀
- **88个RAW文件**：原始素材和草稿

**GitHub知识库仓库**：https://github.com/Alexandre0820/alex_knowledge_base

### 核心主题

1. **AI Native组织**
   - 五层能力金字塔
   - 三层转型路线图
   - 一人公司OPC方法论

2. **AI咨询定价**
   - 三层部署框架（Pilot/Standard/Enterprise）
   - Token经济学
   - 价值导向定价

3. **Agent系统**
   - Multi-Agent架构设计
   - Agent编排
   - Agent评估

4. **商业模式**
   - AI原生服务模式
   - 一人公司商业模式
   - SaaS定价策略

### 文件示例

**ai-native-organization.md**
- 核心定义：以AI为核心逻辑重构业务流程
- 五层能力金字塔：战略→创意→执行→处理→操作
- 转型路线图：工具化→Agent化→组织重塑

**opc-methodology.md**
- 一人公司定义：1人 + AI工具 = 传统10人团队产出
- 关键成功要素：方法论产品化 + 服务标准化
- 规模化路径：聚焦核心能力 → 设计标准流程 → 拓展服务范围

**ai-agency-pricing-strategy.md**
- 三层部署框架详解
- Token经济学分析
- 定价策略建议

## 🔧 核心框架

### 1. 五层能力金字塔

```
Layer 5: 战略判断层（人类决策）→ 核心价值
Layer 4: 创意创新层（人机协作）→ 核心价值
Layer 3: 执行编排层（Agent主导）→ 10x效率
Layer 2: 信息处理层（AI自动化）→ 成本趋零
Layer 1: 事务操作层（全自动化）→ 成本趋零
```

### 2. 三层转型路线图

- **Phase 1**：工具化（0-6个月）- 80%重复性工作自动化
- **Phase 2**：Agent化（6-12个月）- 核心流程Agent驱动
- **Phase 3**：组织重塑（12-24个月）- 人机协作成为默认

### 3. 三层部署框架

- **Tier 1 Pilot**：$15K, 2-4周, 单一场景验证
- **Tier 2 Standard**：$40K-85K, 4-8周, 生产级实现
- **Tier 3 Enterprise**：$100K-150K+, 8-16周, 业务关键系统

## 👨‍💻 作者

**Alex Lu (陆盛赟)**

- 前罗兰贝格战略咨询顾问
- 前西蒙顾和（Simon-Kucher）上海办公室负责人
- 2025年开始AI咨询创业

## 📚 知识来源

- 165个Wiki文件（完整知识库）
- 155个Outputs（实战经验）
- 88个RAW文件（原始材料）
- 罗兰贝格战略方法论
- 西蒙顾和定价框架
- 2026年AI原生组织实践案例

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

MIT License

## 🔗 相关资源

- [Alex的GitHub](https://github.com/Alexandre0820/consulting_skills)
- [知识库仓库](https://github.com/Alexandre0820/alex_knowledge_base)
- [知识库说明](https://github.com/Alexandre0820/alex_knowledge_base#readme)
- [Alex的LinkedIn](https://linkedin.com/in/alexluyun)

---

**⭐ 如果这个Agent对你有帮助，请给个Star！**

**核心差异化**：
- ✅ 不是静态文档，而是智能Agent
- ✅ 知识库开源（165个Wiki + 155个Outputs）
- ✅ 每次回答都从知识大脑检索
- ✅ 每个结论都有引用来源
- ✅ 可执行的建议和明确的行动步骤
- ✅ 支持远程和本地两种模式