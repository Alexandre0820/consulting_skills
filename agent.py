#!/usr/bin/env python3
"""
AI Native Organization Agent - 简洁版本
"""

import subprocess
from pathlib import Path


class AI_native_Org_Agent:
    """AI Native组织Agent"""

    def __init__(self):
        self.agent_dir = Path(__file__).parent

    def diagnose_organization(self, description: str):
        """诊断组织AI化程度"""
        print("🔬 正在诊断组织AI化程度...")

        # 检索相关知识
        print(f"🔍 检索知识: {description}")
        try:
            result = subprocess.run(
                ["bash", str(self.agent_dir / "knowledge-retriever.sh"), description, "3"],
                capture_output=True,
                text=True,
                timeout=10
            )
            print(result.stdout)
        except Exception as e:
            print(f"检索错误: {e}")

        # 评估五层金字塔
        scores = {
            "战略": description.count("战略") + description.count("决策"),
            "创意": description.count("创意") + description.count("创新"),
            "执行": description.count("执行") + description.count("Agent"),
            "处理": description.count("处理") + description.count("自动化"),
            "操作": description.count("操作") + description.count("手动"),
        }

        total = sum(scores.values())

        if total < 5:
            level = "传统组织"
            advice = "建议从Layer 1工具化开始，逐步引入AI工具覆盖重复性工作。"
        elif total < 15:
            level = "AI工具化组织"
            advice = "建议从Layer 2 Agent化过渡，设计Multi-Agent工作流。"
        elif total < 30:
            level = "AI Agent化组织"
            advice = "建议进入Layer 3，建立Agent编排能力，设计人机协作模式。"
        else:
            level = "AI Native组织"
            advice = "你的组织已经达到AI Native水平，建议聚焦Layer 4-5，发挥人类核心价值。"

        print("\n" + "=" * 60)
        print("📊 AI Native组织诊断报告")
        print("=" * 60)
        print(f"诊断等级: {level}")
        print(f"综合得分: {total} / 50")
        print("\n各层分布:")
        print("-" * 60)

        for layer, score in scores.items():
            emoji = "🔥" if layer in ["战略", "创意"] else "🎯"
            print(f"  {emoji} {layer}: {score}分")

        print("\n核心建议:")
        print("-" * 60)
        print(f"  {advice}")
        print("\n推荐行动:")
        print("-" * 60)
        print("  1. 优先将Layer 1-2工作自动化（RPA + AI工具）")
        print("  2. 设计Agent工作流覆盖Layer 3核心流程")
        print("  3. 保留Layer 4-5给人类主导（方向、创意、决策）")
        print("  4. 建立知识管理系统（RAW → Wiki → Outputs）")

        return {
            "level": level,
            "total": total,
            "scores": scores,
            "advice": advice
        }

    def generate_transformation_plan(self, target: str):
        """生成转型计划"""
        print(f"📋 生成转型计划: {target}")
        print("\n" + "=" * 60)
        print("📋 AI Native组织转型计划")
        print("=" * 60)

        phases = [
            {
                "phase": 1,
                "name": "工具化阶段 (0-6个月)",
                "focus": "AI工具覆盖Layer 1-2",
                "deliverables": ["80%重复性工作自动化", "建立AI工具使用标准", "员工培训完成"],
                "cost": "¥50K-150K",
                "timeline": "0-6个月"
            },
            {
                "phase": 2,
                "name": "Agent化阶段 (6-12个月)",
                "focus": "Multi-Agent系统覆盖Layer 3",
                "deliverables": ["核心业务流程Agent驱动", "人机协作模式建立", "知识库建设完成"],
                "cost": "¥200K-500K",
                "timeline": "6-12个月"
            },
            {
                "phase": 3,
                "name": "组织重塑阶段 (12-24个月)",
                "focus": "组织结构适配AI逻辑",
                "deliverables": ["AI Native组织架构", "持续学习机制", "创新能力提升"],
                "cost": "¥500K-1500K",
                "timeline": "12-24个月"
            }
        ]

        for p in phases:
            print(f"\n阶段 {p['phase']}: {p['name']}")
            print(f"  聚焦: {p['focus']}")
            print(f"  交付物:")
            for d in p['deliverables']:
                print(f"    - {d}")
            print(f"  成本估算: {p['cost']}")
            print(f"  时间线: {p['timeline']}")

        print("\n成功指标:")
        print("-" * 60)
        print("  • Layer 1-2: 90%自动化")
        print("  • Layer 3: 80% Agent驱动")
        print("  • 知识复用率: 60%+")
        print("  • 人均产出提升: 3x+")

        print("\n风险提示:")
        print("-" * 60)
        print("  ⚠️ 技术选型风险（工具太多，选择困难）")
        print("  ⚠️ 组织阻力（员工抵触变化）")
        print("  ⚠️ ROI不清晰（短期投入，长期回报）")

        return {"phases": phases}


if __name__ == "__main__":
    agent = AI_native_Org_Agent()

    print("=" * 60)
    print("AI Native Organization Agent - 测试模式")
    print("=" * 60)
    print()

    # 测试诊断
    print("测试1: 诊断组织AI化程度")
    print("-" * 60)
    agent.diagnose_organization("我们公司有10人，用了一些AI工具")
    print()

    # 测试转型计划
    print("\n测试2: 生成转型计划")
    print("-" * 60)
    agent.generate_transformation_plan("从传统组织到AI Native")
