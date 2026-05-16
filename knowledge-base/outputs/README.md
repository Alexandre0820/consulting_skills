# Outputs 目录说明

## 📂 目录结构

```
outputs/
├── README.md                 # 本文件
├── work-documents/           # 工作文档（行动计划、商业计划等）
│   ├── README.md            # 工作文档说明
│   └── *.md                 # 具体项目文档
├── archive/                  # 待观察文档（低价值，1个月后确认删除）
│   ├── README.md            # 归档说明
│   └── *.md                 # 待确认文档
└── *.md                     # 战略洞察类（核心知识资产）
```

## 🎯 文件分类标准

### ✅ 战略洞察类（保留在根目录）
- 基于特定知识的深度分析
- 提炼出可复用的框架/决策树
- 提供战略视角或新认知
- 可直接用于内容创作或客户对话

**示例**：
- `multi-agent-decision-framework.md`（Multi-Agent决策框架）
- `karpathy-ai-philosophy-strategic.md`（Karpathy AI哲学）
- `perplexity-growth-strategic.md`（Perplexity增长引擎）

### 📋 工作文档（work-documents/）
- 具体的行动计划模板
- 商业计划书
- 项目执行计划
- 无特定知识支撑的通用方案

**特征**：含"90天执行计划"、"行动计划"、"第X周"等具体schedule

**处理原则**：保留1-2个月，如未使用则删除

### ⏳ 待观察类（archive/）
- 内容单薄（<1000字）且深度不足
- 空壳文件（仅有标题框架）
- 价值不确定需进一步评估

**处理原则**：存放1个月，确认无价值后删除

---

## 🔄 维护流程

### 每月初检查
1. 查看 `work-documents/` 中文件是否被引用/使用
2. 超过2个月未使用的 → 删除
3. `archive/` 中超过1个月未移动的 → 删除

### 知识图谱关联
- 所有战略洞察类文件应在对应Wiki中建立**双向引用**
- 工作文档和待观察文件不进入知识图谱

---

**最后更新**：2026-05-03
**维护负责人**：LobsterAI Assistant + Alex