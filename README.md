# AI Native Organization Agent

一个**真正的智能Agent系统**，帮助你设计AI原生组织架构。

## ✨ 核心特性

- 🔍 **知识检索**：从知识大脑（165个Wiki + 155 Outputs）检索相关信息
- 📊 **智能诊断**：评估组织AI化程度，生成诊断报告
- 📋 **转型规划**：制定三阶段转型路线图，估算成本和时间
- 💰 **定价策略**：基于三层框架（Pilot/Standard/Enterprise）生成定价建议
- 📝 **引用溯源**：每个结论都标注来源，可验证

## 🎯 解决的问题

- 传统企业如何向AI原生组织转型？
- 如何评估组织当前AI化程度？
- 从传统组织到AI Native的转型计划？
- AI咨询如何定价？

## 🚀 快速安装

### 方法1：一键安装

```bash
cd /Users/shengyun/lobsterai/project/skills/ai-native-org-skill
./install.sh
```

### 方法2：手动安装

```bash
# 安装Python依赖
pip3 install python-dotenv

# 设置执行权限
chmod +x agent.py
chmod +x knowledge-retriever.sh

# 运行测试
python3 agent.py --test
```

## 💬 使用方法

### CLI模式

```bash
# 诊断组织AI化程度
python3 agent.py "我们有10人，用了一些AI工具，如何评估？"

# 生成转型计划
python3 agent.py "从传统组织到AI Native，我需要做什么？"

# 生成定价策略
python3 agent.py "AI咨询如何定价？"
```

### Python API

```python
from agent import AI_native_Org_Agent

# 创建Agent
agent = AI_native_Org_Agent()

# 诊断
report = agent.diagnose_organization("我们公司有10人，用了一些AI工具")
print(report)

# 生成转型计划
plan = agent.generate_transformation_plan("从传统组织到AI Native")
print(plan)

# 生成定价策略
strategy = agent.generate_pricing_strategy("Agent开发咨询")
print(strategy)

# 处理通用问题
answer = agent.ask("如何设计AI原生组织架构？")
print(answer)
```

## 📁 项目结构

```
ai-native-org-skill/
├── agent.py               # Agent核心引擎
├── agent-cli.py           # CLI工具
├── knowledge-retriever.sh # 知识检索器
├── install.sh             # 安装脚本
├── tools/
│   └── engine.py          # 工具集
├── prompts/
│   └── system.md          # System Prompt
├── knowledge-base/
│   ├── wiki-index.md      # 知识索引
│   ├── wiki/              # Wiki文件
│   ├── outputs/           # Outputs
│   └── raw/               # RAW
├── README.md
├── LICENSE
└── .gitignore
```

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

## 📖 示例输出

### 诊断报告

```
📊 AI Native组织诊断报告

诊断等级: AI工具化组织
综合得分: 18 / 50

各层分布:
----------------------------------------------------------------------
  🎯 战略: 2分
  🎨 创意: 3分
  🚀 执行: 8分
  📊 处理: 4分
  ⚙️ 操作: 1分

核心建议:
----------------------------------------------------------------------
  你公司已经从传统组织进入AI工具化阶段。建议从Layer 2 Agent化过渡，
  设计Multi-Agent工作流，将核心业务流程自动化。
```

### 转型计划

```
📋 AI Native组织转型计划

阶段 1: 工具化阶段 (0-6个月)
  聚焦: AI工具覆盖Layer 1-2
  交付物:
    - 80%重复性工作自动化
    - 建立AI工具使用标准
    - 员工培训完成
  成本估算: ¥50K-150K
  时间线: 0-6个月

阶段 2: Agent化阶段 (6-12个月)
  聚焦: Multi-Agent系统覆盖Layer 3
  交付物:
    - 核心业务流程Agent驱动
    - 人机协作模式建立
    - 知识库建设完成
  成本估算: ¥200K-500K
  时间线: 6-12个月
```

### 定价策略

```
💰 AI咨询定价策略（三层框架）

Tier 1: Pilot包
  价格: ¥15,000
  周期: 2-4周
  范围: 单一场景快速验证
  交付:
    - POC
    - 可行性判断
    - 团队培训

Tier 2: Standard包
  价格: ¥40,000-85,000
  周期: 4-8周
  范围: 生产级实现
  交付:
    - 可用系统
    - 培训
    - 文档

Tier 3: Enterprise包
  价格: ¥100,000-150,000+
  周期: 8-16周
  范围: 业务关键系统
  交付:
    - 完整系统
    - 治理体系
    - 持续优化
```

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

MIT License

## 🔗 相关资源

- [Alex的GitHub](https://github.com/Alexandre0820/consulting_skills)
- [知识库Wiki](https://github.com/Alexandre0820/my-ai-consulting-kb)

---

**⭐ 如果这个Agent对你有帮助，请给个Star！**

**核心差异化**：
- 不是静态文档，而是智能Agent
- 知识库驱动，每次回答都基于真实知识
- 每个结论都有引用来源
- 可执行的建议和明确的行动步骤