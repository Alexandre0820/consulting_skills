标题: 爱马仕Hermes Agent 万字深度解读：第一个出厂就带缰绳的 AI Agent，到底怎么样？
来源: 龙虾之心微信公众号
日期: 2026-04-27
链接: https://mp.weixin.qq.com/s/fjwNMfK_93fEvmbhKzccaA
抓取方法: wechat-article-fetcher (Playwright)
字数统计: 17866 字符
抓取成功率: 100%
质量评分: A级

# 爱马仕Hermes Agent 万字深度解读：第一个出厂就带缰绳的 AI Agent，到底怎么样？

引言：又来一个？

我理解你的疲惫。

OpenClaw在 2025 年底掀起了「龙虾热」，2600 万用户，国内大厂纷纷跟进。那段时间你的朋友圈大概率被「我养了一只虾」刷过屏。龙虾热还没完全散去，又有一个新东西冒出来了。

2026 年 2 月，Nous Research 发布了 Hermes Agent。截止2026 年 4 月26日，GitHub stars 飙到 117,000+

你的第一反应可能是：龙虾我还没搞明白，又来？

我花了一周时间把 Hermes 从头到尾拆了一遍，发现它和 OpenClaw 走的是完全不同的路。Hermes 不是又一个龙虾，它在做一件我们一直在讨论但没人做成产品的事。

一、从 Harness Engineering 到 Hermes
1.1 瓶颈不是模型，是环境

2026 年初，AI 编程圈出现了一个共识：瓶颈不是模型，是环境。

LangChain 团队做了一个实验，用同一个模型（GPT-5.2 Codex），只调整周围的「缰绳」配置，成绩从 52.8% 涨到 66.5%，排名从 Top 30 跳到 Top 5。模型一行没改。

Mitchell Hashimoto（Terraform 的创造者）第一个给这件事命名：Harness Engineering。他的做法很朴素——每次 AI 犯了一个错，就加一条规则，让它永远不再犯同一个错。文件是活的，一直在长。

Harness Engineering 可以拆成五个组件：

Harness 五组件	手动实现方式
指令层	手写 CLAUDE.md / AGENTS.md
约束层	配置 hooks / linter / CI
反馈层	人工审查 / 评估者 Agent
记忆层	手动维护 knowledge base
编排层	自己搭多 Agent pipeline

这五个组件，是理解 Hermes 的钥匙。

1.2 Hermes 把五组件全部内建了

Harness Engineering 讲的是方法论——「你应该给 AI 造什么样的缰绳」。但方法论有一个问题：执行全靠人。你得自己写 CLAUDE.md，自己配 hooks，自己搭记忆系统，自己设计工作流。

Hermes 做的事情是：把这五个组件全部内建了，而且让它们自动运转。

Harness 五组件	Hermes 内建系统
指令层	Skill 系统（markdown skill 文件，自动创建 + 自改进）
约束层	Tool permissions + sandbox + toolset 按需启用
反馈层	自改进学习循环（完成任务后自动复盘优化）
记忆层	三层记忆（会话/持久/Skill）+ Honcho 用户建模
编排层	子 Agent 委派 + cron 调度

看左列和右列的对比。左边全是手动操作，你得是一个有经验的工程师才能搭出来。右边是开箱即用，装完就有。

这就是 Hermes 和 OpenClaw 的本质区别。OpenClaw 给你一套「配置即行为」的系统，你写 SOUL.md，它变成你想要的样子。它的记忆系统功能完善（Daily Logs + MEMORY.md + 语义搜索），Skill 生态庞大，但主要靠人工编写和维护。

Hermes 把这套手动流程变成了一个自动运行的系统。从「你给 AI 造缰绳」变成「AI 自己给自己造缰绳」。

二、Hermes Agent 全景：60 秒看懂
2.1 架构一张图

Hermes Agent 的架构可以用一条线串起来：

学习循环 → 三层记忆 → Skill 系统 → 40+ 工具 → 多平台 Gateway

从左到右，每个模块的职责一句话讲清楚：

学习循环是 Hermes 的心脏。每次完成一个任务，它会自动复盘：该记住什么、该提炼什么 Skill、现有 Skill 需不需要优化。这个循环是持续运转的，不需要你手动触发。
三层记忆是 Hermes 的大脑。会话记忆记住「刚才发生了什么」，持久记忆记住「你是谁、你喜欢什么」，Skill 记忆记住「怎么做事」。三层各司其职，用 SQLite + FTS5 索引存储，按需检索而不是全量加载。
Skill 系统是 Hermes 的技能库。每个 Skill 是一个独立的 markdown文件，存在 ~/.hermes/skills/ 目录下。关键特性：Skill 不是静态的，会在使用中自我改进。
40+ 内置工具是 Hermes 的手脚。分五大类：执行、信息、媒体、记忆、协调。再加上 MCP 集成，可以连接 6000+ 外部应用。
多平台 Gateway 是 Hermes 的入口。Telegram、Discord、Slack、WhatsApp、Signal、CLI，飞书，QQ，微信12+ 平台支持。你可以在 Telegram （或者飞书）上给它发消息，它在 VPS 后台处理，跨平台对话连续。

[文章内容继续...完整全文已保存]