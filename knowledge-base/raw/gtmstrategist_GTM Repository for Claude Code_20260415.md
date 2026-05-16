# The GTM Repository: Build Your Claude Code GTM Brain

**来源**: GTM Strategist
**抓取日期**: 2026-04-15
**原文链接**: https://knowledge.gtmstrategist.com/p/the-gtm-repository-for-claude-code

## 核心概念

### GTM Repository的价值
- **问题**: 团队每次使用AI都重新构建上下文，对话结束即消失
- **解决方案**: 结构化markdown文件库，捕获GTM制度知识
- **效果**: Claude在会话开始时已有上下文，任务变为单行prompt

### 五层架构
```
1. CLAUDE.md          ← 入口文件，自动读取，2分钟可浏览
2. Context Files      ← 6个核心文件(Profile/ICP/Signal/Positioning等)
3. Skills            ← 5个任务技能(研究/序列/评分等)
4. Workflows         ← 3个工作流程(丰富/路由/构建)
5. Outputs           ← 输出存档，形成反馈循环
```

## 核心文件结构

### CLAUDE.md (入口文件)
- **作用**: 会话开始时自动读取
- **内容**: ICP摘要、顶级信号、定位、团队、当前优先级
- **原则**: 2分钟可扫描，详细内容在引用的文件中

### Context Files (6个核心文件)
1. **context/profile.md**: 公司概述、产品、客户画像、参考客户
2. **context/icp-definition.md**: 层级定义、明确标准、ICP演变日志
3. **context/signal-library.md**: 信号库、检测方法、分值、衰减曲线
4. **context/positioning.md**: 价值支柱、信息矩阵、禁忌语言
5. **context/competitor-radar.md**: 竞品雷达、诚实评估胜负点
6. **context/personas/**: 买家画像、决策角色、关注点

### Skills (5个核心技能)
1. **Setup**: 自动研究公司，填充70-80%内容
2. **Account Research**: 账户情报简报、利益相关者地图
3. **Signal to Sequence**: 完整活动构建、触发逻辑、序列文案
4. **ICP Scoring**: 账户评分、层级分配
5. **Weekly Update**: 识别过时内容、起草更新

### Workflows (3个流程)
1. **workflows/enrichment.md**: 数据瀑布、质量阈值、邮件送达
2. **workflows/signal-routing.md**: 信号路由决策树
3. **workflows/campaign-build.md**: 活动构建全流程

### Outputs (输出存档)
- 研究简报、活动简报、序列文案
- 6个月输出与上下文对比形成反馈循环

## 信号库核心机制

### 信号定义
```
真实信号 = "Series B announced in last 60 days, detected via Crunchbase webhook into Clay, worth 30 points, decay to 15 points after 60 days, message hook: 'Series B is the inflection point where the ops layer either scales or becomes the bottleneck.'"
```

### 信号衰减
- **原理**: 150天前的融资事件与10天前的信号价值不同
- **机制**: 30点(0-60天) → 15点(60-90天) → 0点(180天)
- **价值**: 确保活跃列表反映实际紧迫性

### 信号组合
- **原理**: 两个信号组合比单独更预测性
- **示例**: Series B + 新RevOps招聘 = 80点(含组合奖励)
- **意义**: 预算存在AND有人在积极重建

## 实施路径

### 第一阶段: 设置 (1个下午)
1. 运行Setup技能，提供域名
2. Claude自动研究公司，填充70-80%内容
3. 3分钟精炼通过

### 第二阶段: 测试 (1周)
1. 对当前pipeline运行ICP Scoring
2. 对前10账户运行Account Research
3. 识别ICP定义差距

### 第三阶段: 优化 (持续)
1. 活动后更新信号库性能
2. 每周更新Current priorities
3. 季度更新ICP演变日志

## 实际应用案例

### 案例1: ICP重写
- **公司**: 开发者工具公司
- **发现**: "Platform Engineering"或"Developer Experience"团队创建信号转换率4倍
- **行动**: 添加为Tier 1组织信号
- **结果**: 完全改变外联策略

### 案例2: 竞品卡重建
- **公司**: 安全软件公司
- **问题**: 连续3次输给同一竞品
- **行动**: 结构化损失分析，发现竞品定价和能力变化
- **结果**: 更新后赢得4次竞争评估中的2次

### 案例3: 新员工入职
- **公司**: B2B SaaS公司
- **情况**: 新RevOps负责人8个月知识库经验
- **结果**: 第一天即可研究前20优先级账户，入职对话聚焦策略而非背景

## 维护机制

### 每周维护 (5分钟)
- 更新CLAUDE.md的"Current priorities"
- 保持整个仓库与当前状态一致

### 活动后 (15分钟)
- 添加结果到活动输出文件
- 回复率、会议率、信号转换数据
- 使信号库从假设文档变为学习系统

### 赢/输后 (30分钟)
- 更新竞品雷达
- 记录AE听到、竞品说法、决策关键点
- 实时更新的竞品卡价值是季度规划的10倍

### 季度维护 (1小时)
- 审查ICP定义，添加演变日志
- 记录变化内容和原因
- 一年后，演变日志比当前定义更有价值

## OpenClaw自动化

### 自动化流程
1. 定时运行OpenClaw
2. 浏览器自动化从外联工具拉取指标
3. 自动更新信号性能日志和活动结果
4. Slack通知总结和决策提示

### 人工决策点
- 是否改变ICP
- 是否削减表现不佳信号
- 竞争交易的判断

## 开源资源

### GTM Starter Kit
- **GitHub**: github.com/KarlRaf/gtm-starter-kit
- **包含**: 
  - CLAUDE.md模板
  - 6个上下文模板
  - 5个技能
  - 3个工作流程
  - 2个playbook
  - 完整示例公司(Relay)

## 核心洞察

1. **竞争优势**: 不是更多外联，而是更好上下文
2. **复合效应**: 系统化跟踪结果产生学习系统
3. **制度化知识**: 不依赖个人，不随Slack滚动消失
4. **新人效率**: 第一天即可理解ICP、信号、定位、优先级
5. **工程化思维**: 像软件工程一样管理GTM知识

---

**价值主张**: 构建一次，持续更新，让AI的GTM输出从一般到精准，从重复到智能。*