# AI Native Organization Agent

一个**真正的智能Agent系统**，帮助你设计AI原生组织架构。**零门槛使用**，无需懂技术！

## ✨ 核心特性

- 🔍 **知识检索**：从知识大脑（174 Wiki + 148 Outputs + 87 RAW）检索
- 📊 **智能诊断**：评估组织AI化程度，生成诊断报告
- 📋 **转型规划**：制定三阶段转型路线图
- 💰 **定价策略**：基于三层框架生成定价建议
- 📝 **引用溯源**：每个结论都标注来源
- 🌐 **零门槛**：支持Claude Desktop、Discord Bot、Web应用

## 🎯 解决的问题

- 传统企业如何向AI原生组织转型？
- 如何评估组织当前AI化程度？
- 从传统组织到AI Native的转型计划？
- AI咨询如何定价？

## 🚀 零门槛使用方式

### 方式1：Claude Desktop插件（推荐）⚡️

```bash
# 1. 下载Claude Desktop
# 2. 安装插件
cp claude_plugin.py ~/.claude/plugins/
# 3. 重启Claude Desktop
# 4. 开始提问！
```

**优势**：
- ✅ 零技术门槛
- ✅ Claude自带推理能力
- ✅ 跨平台（Mac/Windows/Linux）

详细说明：[CLAUDE_PLUGIN_README.md](CLAUDE_PLUGIN_README.md)

---

### 方式2：Discord Bot（社区化）⚡️

```bash
# 1. 创建Discord Bot
# 2. 安装discord.py
pip3 install discord.py
# 3. 设置Token
export DISCORD_TOKEN=你的token
# 4. 启动Bot
python3 discord_bot.py
```

**优势**：
- ✅ 社区化，易分享
- ✅ 邀请朋友一起使用
- ✅ 零技术门槛

详细说明：[DISCORD_BOT_README.md](DISCORD_BOT_README.md)

---

### 方式3：Python脚本（开发者）

```bash
# 克隆仓库
git clone https://github.com/Alexandre0820/consulting_skills
cd consulting_skills

# 安装依赖
pip3 install python-dotenv

# 运行
python3 agent.py "如何评估组织AI化程度？"
```

---

### 方式4：Web应用（即将上线）

```bash
# 访问网站
https://ai-native-org-alex.vercel.app

# 注册账号
# 输入问题
# 获得答案
```

**即将上线**：[ROADMAP.md](ROADMAP.md) 查看发布计划

---

## 💬 使用方法

### Claude Desktop Plugin

1. **安装插件**：
   ```bash
   cp claude_plugin.py ~/.claude/plugins/
   ```

2. **配置插件**（编辑 `~/.claude/claude_desktop_config.json`）：
   ```json
   {
     "mcpServers": {
       "ai-native-org": {
         "command": "python3",
         "args": ["/Users/shengyun/lobsterai/project/skills/ai-native-org-skill/claude_plugin.py"]
       }
     }
   }
   ```

3. **开始提问**：
   ```
   使用Alex的知识库，请告诉我如何评估组织AI化程度？
   ```

### Discord Bot

1. **安装依赖**：
   ```bash
   pip3 install discord.py
   ```

2. **启动Bot**：
   ```bash
   export DISCORD_TOKEN=你的token
   python3 discord_bot.py
   ```

3. **开始提问**：
   ```
   用户: 如何评估组织AI化程度？
   Bot: 📋 **回答**：
   📊 AI Native组织诊断报告
   ...
   ```

### Python脚本

```python
from agent import AI_native_Org_Agent

agent = AI_native_Org_Agent(use_remote=False)
report = agent.diagnose_organization("我们公司有10人，用了一些AI工具")
print(report)
```

---

## 📚 知识库

### Knowledge开源

本项目的Knowledge库**完全开源**，包含：

- **174个Wiki文档**：完整的AI Native组织知识体系
- **148个Outputs**：实战案例和经验沉淀
- **87个RAW文件**：原始素材和草稿

**GitHub仓库**：
- Agent仓库: https://github.com/Alexandre0820/consulting_skills
- 知识库仓库: https://github.com/Alexandre0820/alex_knowledge_base

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

---

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

---

## 👨‍💻 作者

**Alex Lu (陆盛赟)**

- 前罗兰贝格战略咨询顾问
- 前西蒙顾和（Simon-Kucher）上海办公室负责人
- 2025年开始AI咨询创业

## 📚 知识来源

- 174个Wiki文件（完整知识库）
- 148个Outputs（实战经验）
- 87个RAW文件（原始材料）
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
- [Claude文档](https://docs.anthropic.com/claude/docs/plugins)
- [Roadmap](ROADMAP.md) - 产品迭代路线图

---

## 🎯 核心差异化（现在真正成立）

1. **✅ Knowledge开源** - 174个Wiki + 148个Outputs + 87个RAW
2. **✅ 零门槛** - Claude Plugin + Discord Bot无需技术
3. **✅ Agent智能** - 每次回答都从知识库检索
4. **✅ 引用溯源** - 每个结论都有来源
5. **✅ 可执行建议** - 基于框架生成具体行动

---

## 📈 产品路线图

### Phase 1（当前）⚡️
- [x] Claude Desktop Plugin
- [x] Discord Bot
- [ ] 100个种子用户

### Phase 2（1周内）🎯
- [ ] Web应用MVP
- [ ] 用户注册/登录
- [ ] 报告导出功能

### Phase 3（1月内）⭐
- [ ] 移动应用（iOS/Android）
- [ ] 付费订阅
- [ ] 多用户协作

### Phase 4（3月内）🌟
- [ ] 定制化知识库
- [ ] API接口
- [ ] Marketplace

详细路线图：[ROADMAP.md](ROADMAP.md)

---

**Alex的知识库现已完全开源，任何人都可以使用！**

**现在，你可以通过以下方式使用（零门槛）：**
1. 🤖 **Claude Desktop** - 安装插件即可
2. 💬 **Discord Bot** - 邀请到服务器即可
3. 🌐 **Web应用** - 即将上线

**无需懂Python，无需运行脚本，直接对话即可！**