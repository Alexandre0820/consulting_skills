# YC CEO：让 AI Agent 真正跑起来的秘密

**来源**: 微信公众号
**链接**: https://mp.weixin.qq.com/s/AA8apxnai_3-MZ3rxRsWPA
**抓取日期**: 2026-05-12
**抓取方法**: python_requests+regex
**字数统计**: 8,123字符
**质量评分**: A级（完整技术架构长文）

---

**Garry Tan (YC CEO)**

为什么我每天都写代码写到凌晨2点。

YC每年帮助成千上万的创业者。"builder"这个词对很多人来说只是梦想，对YC CEO来说是日常。

过去5个月里，AI让我重新变回builder。不是玩具项目，而是真正会复利增长的系统。

**核心架构公式**: Fat Skills + Fat Code + Thin Harness

**技术栈（全部开源）**: github.com/garrytan/gbrain
- GStack: 代码skill框架（87,000+ stars）
- GBrain: 知识基础设施
- OpenClaw / Hermes Agent: Harness

---

## Book Mirror 实战

让AI对Pema Chödrön《When Things Fall Apart》（162页，22章）做"书镜"：

**流程**: 每章运行子Agent → 总结作者思想 + 映射到真实人生

**输出**: 3万字"brain page"，两栏渲染
- 左栏：Pema说了什么
- 右栏：如何对应到我正在经历的事

**已知事实错误 → 强制跨模型评估**
- Opus 4.7 1M：精确性
- GPT-5.5：上下文完整性
- DeepSeek V4-Pro：泛化检查

**升级到GBrain深度检索**: 第三版会针对每个小节brain搜索，右栏每项引用真实brain page

**时间**: 40分钟 vs 治疗师40小时

**已处理20+本书**: Amplified / Autobiography of Bertrand Russell / Designing Your Life / Drama of the Gifted Child / Finite and Infinite Games / Gift from the Sea / Siddhartha / Steppenwolf / The Art of Doing Science and Engineering / The Dream Machine / Alan Watts / Feynman / Pema Chödrön / Ken Wilber 等

**复利**: 第二次mirror知道第一次，第二十次知道前十九次

---

## 10万页Brain结构

**三层Schema**:
1. **Compiled Truth**（顶部）：当前最佳理解
2. **Append-Only Timeline**（中部）：只增不减的时间线
3. **Raw Sidecars**（底部）：原始资料来源

**每个页面包含**:
- 遇到的人：时间线 + 当前状态 + 开放事项 + 评分
- 每场会议：文字稿 + 结构化摘要 + Entity Propagation
- 每本书：逐章Book Mirror
- 每篇文章/播客/视频：吸收 + 打标签 + 交叉引用

**Entity Propagation（实体传播）**: 每次会议后，系统遍历提到的每个人和每家公司，更新各自的brain page

**示例**: Office hours见到创始人 → 自动创建/更新个人页面 + 公司页面 + 交叉引用会议记录 + 检查是否见过 + 浮出上次讨论内容 + 检查申请资料 + 拉取最新指标 + 匹配投资组合联系人 → 下次见面前完整上下文包已准备好

**File Cabinet vs Nervous System**:
- 文件柜：只存东西
- 神经系统：连接信息、标记变化、浮现"此刻最相关的东西"

---

## 技术架构详解

### Harness（薄壳）
- OpenClaw：runtime
- 几千行路由逻辑
- 什么都不知道（不知道书籍/会议/创始人）
- 只负责路由：谁来了，该叫谁来处理

### Skills（胖技能，100+）
每个是自包含Markdown文件，针对具体任务的详细指令

**核心Skills清单**:
| Skill | 功能 |
|-------|------|
| book-mirror | 书镜：每章总结 + 人生映射 |
| meeting-prep | 会议准备：人物页面 + 立场数据库 + 演示脚本 |
| meeting-ingestion | 会议吸收：文字稿 → 摘要 → 实体传播 |
| enrich | 人物丰富：5源合并 → brain page |
| media-ingest | 媒体摄入：视频/音频/PDF/GitHub |
| perplexity-research | 脑增强研究：brain先查 → 再网络搜索 |
| email-triage | 邮件分类 |
| investor-update-ingest | 投资组合更新识别 + 指标抽取 |
| calendar-check | 日程冲突检查 |
| cross-modal-eval | 跨模型评估（三模型互评）|
| check_resolvable | 验证skill接入resolver |

**Skills可组合**: Book-mirror调用brain-ops + enrich + cross-modal-eval + pdf-generation

**改进一个skill → 所有使用它的工作流自动变好**

### Data（厚数据）
10万页结构化知识。每个人/公司/会议/书/文章/想法都被链接、可搜索、每天都在增长。

### Code（厚代码）
转写/OCR/社交媒体归档/日历同步/API集成脚本。真正产生复利的是数据。

### Models（可替换）
- Opus 4.7 1M：精确性任务
- GPT-5.5：召回和穷尽式提取
- DeepSeek V4-Pro：创意工作和第三视角
- Groq + Llama：速度优先

**由skill决定调用哪个模型。Harness不关心。**

---

## Skillify元技能

**Skillify是Meta-Skill**: 负责创造新的skills

**循环**:
```
遇到重复工作流 → "skillify this"
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

**Book-mirror就是从第一次手动尝试后被skillify出来的**
**Meeting-prep也是在发现每次开会前做同样步骤后被skillify出来的**

---

## 复利系统

**100+ cron任务24/7运行**:
- 社交媒体监控
- Slack/邮件/日历扫描
- 会议吸收自动执行
- 邮件分类每10分钟运行
- 知识图谱从每次对话自我丰富

**复利公式**:
- 每场会议 → brain增长
- 每本书 → 下一本书上下文更丰富
- 每个skill → 下一个工作流更快
- 每个人物页面 → 下一次会议准备更精准

**今天 = 两个月前的10倍**
**两个月后 = 今天的10倍**

**核心洞察**: 未来属于构建复利型AI系统的个人，而非只使用企业中心化AI工具的人。

**区别**: 写日记 vs 拥有神经系统

---

## 如何开始（Garry的路线图）

1. **选Harness**: OpenClaw / Hermes Agent / 从零写。保持薄。只部署路由逻辑。
2. **启动GBrain**: 受Karpathy LLM Wiki启发，OpenClaw里实现。97.6%召回率（LongMemEval），超过MemPalace。39个可安装skills。
3. **做一件有趣的事**: 不要一开始就规划skill架构。先做一件事，反复迭代直到足够好。
4. **运行Skillify**: 把一次性工作转化为可复利基础设施。
5. **持续使用并认真看输出**: 一开始会很一般（这正是重点）。跨模型评估发现错误 → 修复 → 写入skill → 以后所有都变好。
6. **6个月后**: 拥有任何聊天机器人都无法复制的东西。

**第一个东西很糟糕。第一百个时，已经是一个愿意信任的系统。**

---

## 开源项目

- github.com/garrytan/gbrain（完整技术栈）
- GStack（87,000+ stars）：代码skill框架
- 30+可安装skillpacks
- 支持有头/无头浏览器
