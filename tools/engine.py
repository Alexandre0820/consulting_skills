#!/usr/bin/env python3
"""
AI Native Organization Agent - 工具集
"""

import subprocess
from pathlib import Path
from typing import List, Dict, Any

class AgentTools:
    """Agent工具集"""

    def __init__(self, agent_dir: str = None):
        self.agent_dir = Path(agent_dir) if agent_dir else Path(__file__).parent.parent

    def get_knowledge_retriever(self) -> subprocess.Popen:
        """启动知识检索器"""
        retriever_path = self.agent_dir / "knowledge-retriever.sh"
        return subprocess.Popen(
            ["bash", str(retriever_path)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

    def extract_relevant_knowledge(self, query: str, top_k: int = 5) -> Dict[str, Any]:
        """提取相关知识"""
        retriever = self.get_knowledge_retriever()
        result = retriever.communicate(input=query + f"\n{top_k}\n")

        return {
            "query": query,
            "output": result[0],
            "status": "success" if result[1] == "" else "error"
        }

    def diagnose_layer_breakdown(self, description: str) -> Dict[str, int]:
        """诊断各层得分"""
        scores = {
            "战略": description.count("战略") + description.count("决策"),
            "创意": description.count("创意") + description.count("创新"),
            "执行": description.count("执行") + description.count("Agent"),
            "处理": description.count("处理") + description.count("自动化"),
            "操作": description.count("操作") + description.count("手动"),
        }

        # 归一化分数（最大50分）
        total = sum(scores.values())
        max_possible = 10 * len(scores)
        normalized = {k: int(v / max_possible * 50) for k, v in scores.items()}

        return normalized

    def determine_level(self, scores: Dict[str, int]) -> tuple:
        """确定组织等级和策略"""
        total = sum(scores.values())

        if total < 5:
            return "传统组织", "建议从Layer 1工具化开始，逐步引入AI工具覆盖重复性工作。"
        elif total < 15:
            return "AI工具化组织", "建议从Layer 2 Agent化过渡，设计Multi-Agent工作流。"
        elif total < 30:
            return "AI Agent化组织", "建议进入Layer 3，建立Agent编排能力，设计人机协作模式。"
        else:
            return "AI Native组织", "你的组织已经达到AI Native水平，建议聚焦Layer 4-5，发挥人类核心价值。"

    def calculate_transformation_cost(self, phases: List[str]) -> Dict[str, Any]:
        """计算转型成本"""
        phase_costs = {
            "phase_1": {"min": 50, "max": 150, "currency": "¥"},
            "phase_2": {"min": 200, "max": 500, "currency": "¥"},
            "phase_3": {"min": 500, "max": 1500, "currency": "¥"},
        }

        return phase_costs

    def generate_success_metrics(self) -> List[str]:
        """生成成功指标"""
        return [
            "Layer 1-2: 90%自动化",
            "Layer 3: 80% Agent驱动",
            "知识复用率: 60%+",
            "人均产出提升: 3x+"
        ]

    def generate_risks(self) -> List[str]:
        """生成风险提示"""
        return [
            "技术选型风险（工具太多，选择困难）",
            "组织阻力（员工抵触变化）",
            "ROI不清晰（短期投入，长期回报）",
            "安全合规风险（数据隐私、模型漂移）"
        ]


if __name__ == "__main__":
    # 测试工具
    tools = AgentTools()

    print("测试知识检索:")
    result = tools.extract_relevant_knowledge("AI组织", 5)
    print(result["output"])

    print("\n测试诊断:")
    scores = tools.diagnose_layer_breakdown("我们公司有10人，用了一些AI工具")
    print(f"各层得分: {scores}")
    print(f"总分: {sum(scores.values())}")
    print(f"等级: {tools.determine_level(scores)[0]}")

    print("\n测试成本计算:")
    costs = tools.calculate_transformation_cost([])
    print(costs)
