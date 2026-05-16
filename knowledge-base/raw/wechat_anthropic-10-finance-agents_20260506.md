# 未知标题

**来源**: 微信公众号「未知公众号」
**链接**: https://mp.weixin.qq.com/s/xWTcxsmPyxbJtOAclkpA3Q
**抓取日期**: 2026-05-06
**抓取方法**: curl模拟iPhone浏览器
**字数统计**: 5589 字符

---

华尔街最烦的10件事，Anthropic全做成了Agent
我今天早上刷到 Anthropic 这条新闻的时候，愣了一下。
他们一口气发了
10个现成的Finance Agent
——pitchbook、估值建模、月底关账、KYC筛查、财报审核……华尔街分析师每天加班最久、最烦、最想扔掉的那些活，Anthropic 全打包成了开箱即用的模板。
我原本以为这种程度的 Agent 还得自己搭。你去雇个工程师、找数据、接 Excel、写 prompt、测稳定性……一个投行 IT 团队搞定一个 Agent，大概半年。
现在 Anthropic 直接说：
不用搭了，我们发给你。
plugin 形式装在 Claude Cowork 或 Claude Code 里，下午就能跑。
我看了三遍才确定不是在说未来计划。是今天就能用。
01 先说最直观的：这10个Agent具体做什么
:::
10个Agent分两组，Anthropic一次发全
先列清单。分两大块。
Research &amp; Client Coverage（5个）——前台干的活：
① 
Pitch builder
：自动列目标客户、跑可比公司、搭pitchbook。
② 
Meeting preparer
：开会前把客户和对手方的背景、最近动态全整理好。
③ 
Earnings reviewer
：读电话会议纪要和财报，自动更新模型，标出值得关注的变化。
④ 
Model builder
：从财报、数据源、分析师输入里自己搭财务模型。
⑤ 
Market researcher
：追行业和发行人动态，合成新闻/财报/研报，推送给风险和信贷部门。
Finance &amp; Operations（5个）——中后台的脏活：
⑥ 
Valuation reviewer
：对估值做交叉核验，看可比公司、方法论、公司内部审核标准。
⑦ 
General ledger reconciler
：总账科目调节，跑NAV计算，对照account of record。
⑧ 
Month-end closer
：跑月底关账清单，准备会计分录，出关账报告。
⑨ 
Statement auditor
：检查报表的一致性、完整性、审计就绪度。
⑩ 
KYC screener
：整理实体档案，审核源文件，把升级事项打包给合规团队。
看到这清单我的第一反应是：
这不就是一个投行初级分析师一整年的活
吗？
02 三种用法，总有一款你能用
:::
每个 Agent 模板不是黑盒。Anthropic 把它定义成
reference architecture
——一个可以改、可以拆、可以重组的参考架构。
里面打包了三样东西：
• 
Skills
——任务说明和领域知识
• 
Connectors
——数据的合规接入
• 
Subagents
——主Agent在跑的时候可以调用的子模型（比如专门挑可比公司、专门检查方法论）
部署有三种方式：
① Plugin in Claude Cowork
——分析师自己桌面上的 Claude 里直接装，当助手用。你把目标公司清单丢给 Pitch Agent，它直接在你电脑里的 Excel 里生成 comps，在 PowerPoint 里画 pitchbook，顺手在 Outlook 里起草好 cover note。
② Plugin in Claude Code
——工程师版本，在 IDE 里跑。
③ Cookbook for Managed Agents
——托管版，完全跑在 Claude Platform 上，可以跑一整本 deal book 或者一个通宵的排程。支持工具级权限控制、凭证托管、完整审计日志。
翻译一下：
小打小闹用plugin，大规模跑工业生产线用managed
。
03 这事真正的信号：Agent工业化的开始
:::
分析师的pitchbook/comps/KYC/closing——这些活Anthropic打包了
我一开始看这条新闻，觉得有趣但不震撼。10个Agent嘛，各家都在发。
但多看一眼就发现——
这是Agent从手工作坊进入模板时代的信号。
过去一年，谁家想在投行跑Agent，都是自己搭。自己找数据源，自己接LSEG/FactSet/MSCI，自己写system prompt，自己调subagent的调用逻辑。
一个大行的AI团队，搞一年下来，可能只落地了2-3个Agent。
现在 Anthropic 说：
这10个最高频、最重复、最容易标准化的场景，我给你做好模板。
你拿去改，改成符合你风控规则、符合你审批流、符合你模型规范的版本。
这是一个从
customize everything
到
fork-and-modify
的迁移。
你可以把它想成：以前每家投行都在自己造轮子，现在 Anthropic 给你造了车架，你只需要换个漆、调个悬挂、装个座椅。
04 配套的是Opus 4.7——金融基准第一
:::
这10个Agent跑在哪个模型上？
Claude Opus 4.7
。
Anthropic在公告里放了一个数字：
Opus 4.7 在 Vals AI 的 Finance Agent benchmark 上拿下 64.37%，行业第一。
Vals AI 这个榜单——你可以理解成专门评测 Agent 在金融任务上端到端表现的考试。不是单纯的问答，而是
开模型、查数据、跑计算、出报告
这种完整workflow。
64.37% 听起来不高。但这是Agent级别的端到端正确率——比起LLM的单轮问答，Agent每一步都可能出错，错误会链式放大。能做到60%+已经很夸张。
更重要的是——
这个数字是Anthropic敢拿来定价的底气。
如果Agent跑不稳，你根本没法把它卖给花旗。
05 Claude进驻Excel/PPT/Word/Outlook
:::
Excel/PowerPoint/Word全都接了Claude——上下文自动在四个app之间流转
这次顺带发的另一件事，我觉得分量不输那10个Agent：
Claude现在能原生跑在Microsoft Excel、PowerPoint、Word里
（Outlook马上也要来）。
具体每个app里能干嘛：
• 
Outlook
：当你的chief of staff，筛收件箱、约会议、用你的语气起草回信
• 
Excel
：从财报和数据源自己搭模型，审计跨workbook的公式，跑敏感性分析
• 
PowerPoint
：画deck，底层数据变了deck自动更新
• 
Word
：按公司模板改credit memo
但最关键的一条是这个——
Claude在四个app之间自动继承上下文：你在Excel里搭了个模型，打开PowerPoint继续做deck的时候，不用再解释一遍。
这一条其实是大多数分析师日常最痛的事。你在Excel里炼了半天丹，换到PPT重新解释；PPT搞完换Word写memo又要再解释一遍。
现在Claude在你的桌面上
当一个有记忆的同事
，一直记得你在干什么。
06 新接入的数据源：D&amp;B / Moody's / Guidepoint...
:::
Agent本身再强，没数据就是空壳。
Anthropic这次在生态上也补了一批。新加的connector：
• 
Dun &amp; Bradstreet
——全球企业身份标识的事实标准，D-U-N-S® Number。你要做KYC，它是源头。
• 
Fiscal AI
——上市公司的实时基本面数据。
• 
Financial Modeling Prep
——股票/ETF/加密/外汇/大宗的行情+基本面+filing+transcript。
• 
Guidepoint
——
10万+合规审核过的专家访谈transcript
，附上逐字原文。
• 
IBISWorld
——细分行业营收、比率、风险评分、成本结构、预测。
• 
SS&amp;C IntraLinks
——数据室数据，用于尽调问答和交易活动追踪。
• 
Third Bridge
——一级市场专家访谈。
• 
Verisk
——保险数据（财产险、意外险）。
另外Moody's直接推了一个MCP App，把6亿+家全球公司的信用评级和数据接进Claude。
这份清单里每一家都是华尔街的
付费数据贵族
——一年license费百万美元起跳。Anthropic这次把它们打包接好，意味着一个用Claude的分析师，桌面上这些数据
ctrl+K
就能查。
07 Citadel / FIS / BNY / Walleye 都在说什么
:::
Anthropic news：Agents for financial services（May 5, 2026）
看客户quote这件事，我觉得比看产品描述更能看清一个工具到底有多深入。
Citadel
（全球对冲基金巨头）：「我们的投资专家活在数据和模型里，Claude for Excel正好在那里等着他们。分析师用它做coverage model、分离信号和噪音、压力测试自己的工作——效率阶梯式跃升。」
FIS
（全球支付基础设施巨头）说得最猛：
我们在和Anthropic一起造一个Agent，把AML反洗钱调查从几天压缩到几分钟——接下来还有信用决策、反欺诈、存款挽留。
BNY
（纽约梅隆）CIO：
我们给流程安排了一批新的digital employee，能把案子从头做到尾。
Walleye Capital
（400人的对冲基金）：
我们公司100%的员工都在用Claude Code。这个比例反映的是我们的AI-first心态：我们期待每个人都持续思考，'AI能怎么帮我做这事？'——不管你是不是技术岗。
400人全用。一个不剩。
这是我在所有quote里看到最震撼的一句。
08 从几天到几分钟：AML调查的时间折叠
:::
我想停在FIS那句话上多聊两句。
AML调查
是银行合规里最吃人的活之一。一个可疑交易预警触发，合规员要去拉转账流水、查对手方关联、检索制裁名单、写报告、报SAR……
按行业均值，一个案子从立案到结案，
3-7天
算快的。复杂的一个月都不算离谱。
FIS说他们这个Agent能把这个时间
压缩到几分钟
。
我没办法验证这个数字。但就算打个对折——从几天到几十分钟——对一家要处理数百万笔交易的支付巨头来说，这就是
人员结构
意义上的重构。
AML、信用决策、反欺诈、存款挽留——FIS一口气列了四个Agent。他们说
FIS的客户不用自己搭这套基础设施了。已经在这儿了。
——这句话翻译一下就是：数千家中小银行的合规和风控IT团队，接下来可能要重新想想自己要做什么。
09 这件事真正的商业逻辑
:::
10个Agent分两组：Research &amp; Client Coverage / Finance &amp; Operations
抛开技术不谈，我觉得这次发布真正有意思的是商业模型。
Anthropic等于是在说：
我不只卖模型，我卖workflow。
以前你付钱给Anthropic，买的是token。现在你付钱给Anthropic，买的是
一个会跑pitchbook的数字员工
。模型是载体，Agent是产品。
这是个很关键的转型。
第一，
token市场正在快速商品化
——Haiku在降价、GPT在降价、开源在变强。单纯卖推理算力的毛利在塌陷。
第二，
workflow是有粘性的
。一个投行一旦把pitchbook agent、KYC agent、month-end closer接进自己工作流、改成自己风控规则的版本，下次再搬家的成本极高。
第三，
这是金融条线的Vertical AI
。接下来法律、医疗、会计、保险——每个行业都会有类似的10-20个打包Agent模板。
我的判断是——
2026-2027年的AI公司战争，从比谁的模型强，变成比谁的Agent模板库深。
10 我自己怎么看
:::
写完前面九段，我把Anthropic的公告又翻了一遍。
有一个细节我一开始没注意——他们在公告里写了这句：
so a team can put Claude on real financial work in days rather than months.
翻译过来是：
让一个团队能在几天内让Claude上手真实金融工作，而不是几个月。
这一句是整个发布的核心。
以前搭一个金融Agent，IT团队半年。现在Anthropic告诉你——几天。
从半年到几天，是一个
50倍的时间压缩
。这种尺度的效率变化，历史上只有少数几次：PC之于手写、Excel之于计算器、SaaS之于自建。
每一次，都伴随大批量的人员再分配。
我自己不是投行的。但我现在回头想想，如果你是一个金融条线的初级员工，这一周晚上回家可能要多想想自己的路径——不是说AI要取代你，而是
你做的活，Anthropic已经打包成Agent发给了你老板。
你的价值得在别的地方。
这个"别的地方"在哪里——我不知道。但可以确定的是，
继续留在做pitchbook/做comps/跑月底关账的这条线上，价值会被快速稀释。
Anthropic把题目发出来了。下一步是每个分析师自己答。
◇ ◆ ◇
source：Anthropic News「Agents for financial services」(2026-05-05)