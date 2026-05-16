#!/usr/bin/env python3
"""
AI Native Organization Agent - 支持远程/本地知识库
"""

import sys
import subprocess
import json
from pathlib import Path
from typing import Dict, Any


class AI_native_Org_Agent:
    """AI Native组织Agent"""

    def __init__(self, knowledge_dir: str = None, use_remote: bool = False):
        """
        初始化Agent

        Args:
            knowledge_dir: 知识库路径（本地）
            use_remote: 是否使用远程知识库（在线模式）
        """
        self.agent_dir = Path(__file__).parent

        if use_remote:
            # 远程模式：知识在GitHub仓库
            self.knowledge_dir = str(self.agent_dir / "knowledge-base")
            self.use_remote = True
        else:
            # 本地模式：知识在指定路径
            self.knowledge_dir = knowledge_dir or "/Users/shengyun/lobsterai/project/my-ai-consulting-kb"
            self.use_remote = False

        self.knowledge_index = str(self.agent_dir / "knowledge-base/KNOWLEDGE_INDEX.md")

    def retrieve_knowledge(self, query: str, top_k: int = 5) -> Dict[str, Any]:
        """
        检索相关知识

        Args:
            query: 查询
            top_k: 返回数量

        Returns:
            相关知识列表
        """
        print(f"🔍 检索知识: {query}")
        print(f"知识库模式: {'远程GitHub' if self.use_remote else '本地'}")

        try:
            if self.use_remote:
                # 远程模式：从GitHub知识库检索
                result = subprocess.run(
                    ["bash", str(self.agent_dir / "knowledge-retriever.sh"), query, str(top_k)],
                    capture_output=True,
                    text=True,
                    timeout=15
                )
                print(result.stdout)
                return {
                    "query": query,
                    "output": result.stdout,
                    "status": "success" if result.returncode == 0 else "error"
                }
            else:
                # 本地模式：调用RAG检索器
                retriever_path = Path("/Users/shengyun/lobsterai/project") / "alex-clone-rag.sh"
                result = subprocess.run(
                    ["bash", str(retriever_path), query],
                    capture_output=True,
                    text=True,
                    timeout=15
                )
                print(result.stdout)
                return {
                    "query": query,
                    "output": result.stdout,
                    "status": "success" if result.returncode == 0 else "error"
                }
        except subprocess.TimeoutExpired:
            print("⚠️ 检索超时，使用本地知识库")
            return self._local_search(query)
        except Exception as e:
            print(f"❌ 检索错误: {e}")
            return self._local_search(query)

    def _local_search(self, query: str) -> Dict[str, Any]:
        """本地搜索"""
        print(f"🔍 本地搜索: {query}")

        # 从知识索引搜索
        try:
            result = subprocess.run(
                ["grep", "-i", "-n", "-C", "2", query, str(self.knowledge_index)],
                capture_output=True,
                text=True,
                timeout=10
            )
            return {
                "query": query,
                "output": result.stdout or f"未找到匹配: {query}",
                "status": "success"
            }
        except Exception as e:
            return {
                "query": query,
                "output": f"本地搜索失败: {e}",
                "status": "error"
            }

    def diagnose_organization(self, description: str) -> Dict[str, Any]:
        """诊断组织AI化程度"""
        print("🔬 正在诊断组织AI化程度...")

        # 检索相关知识
        knowledge = self.retrieve_knowledge(description, top_k=3)

        # 评估五层金字塔
        scores = {
            "战略": description.count("战略") + description.count("决策") + description.count("方向"),
            "创意": description.count("创意") + description.count("创新") + description.count("模式"),
            "执行": description.count("执行") + description.count("Agent") + description.count("业务"),
            "处理": description.count("处理") + description.count("自动化") + description.count("流程"),
            "操作": description.count("操作") + description.count("手动") + description.count("数据"),
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

        # 构建报告
        report = {
            "diagnosis": {
                "level": level,
                "total_score": total,
                "layer_breakdown": scores,
                "advice": advice
            },
            "recommendations": [
                "优先将Layer 1-2工作自动化（RPA + AI工具）",
                "设计Agent工作流覆盖Layer 3核心流程",
                "保留Layer 4-5给人类主导（方向、创意、决策）",
                "建立知识管理系统（RAW → Wiki → Outputs）"
            ],
            "next_steps": [
                "制定AI化路线图（0-6月/6-12月/12-24月）",
                "选择3-5个关键场景进行试点",
                "培训团队使用AI工具"
            ]
        }

        return report

    def generate_transformation_plan(self, target: str) -> Dict[str, Any]:
        """生成转型计划"""
        print(f"📋 生成转型计划: {target}")

        # 检索相关框架
        frameworks = self.retrieve_knowledge(target, top_k=2)

        # 生成三阶段计划
        plan = {
            "phases": [
                {
                    "phase": 1,
                    "name": "工具化阶段 (0-6个月)",
                    "focus": "AI工具覆盖Layer 1-2",
                    "deliverables": [
                        "80%重复性工作自动化",
                        "建立AI工具使用标准",
                        "员工培训完成"
                    ],
                    "cost_estimate": "¥50K-150K",
                    "timeline": "0-6个月"
                },
                {
                    "phase": 2,
                    "name": "Agent化阶段 (6-12个月)",
                    "focus": "Multi-Agent系统覆盖Layer 3",
                    "deliverables": [
                        "核心业务流程Agent驱动",
                        "人机协作模式建立",
                        "知识库建设完成"
                    ],
                    "cost_estimate": "¥200K-500K",
                    "timeline": "6-12个月"
                },
                {
                    "phase": 3,
                    "name": "组织重塑阶段 (12-24个月)",
                    "focus": "组织结构适配AI逻辑",
                    "deliverables": [
                        "AI Native组织架构",
                        "持续学习机制",
                        "创新能力提升"
                    ],
                    "cost_estimate": "¥500K-1500K",
                    "timeline": "12-24个月"
                }
            ],
            "success_metrics": [
                "Layer 1-2: 90%自动化",
                "Layer 3: 80% Agent驱动",
                "知识复用率: 60%+",
                "人均产出提升: 3x+"
            ],
            "risks": [
                "技术选型风险（工具太多，选择困难）",
                "组织阻力（员工抵触变化）",
                "ROI不清晰（短期投入，长期回报）"
            ]
        }

        return plan


if __name__ == "__main__":
    # 测试Agent
    agent = AI_native_Org_Agent(use_remote=False)

    print("=" * 60)
    print("AI Native Organization Agent - 测试模式")
    print("=" * 60)
    print()

    # 测试诊断
    print("测试1: 诊断组织AI化程度")
    print("-" * 60)
    report = agent.diagnose_organization("我们公司有10人，用了一些AI工具")
    print(report["diagnosis"]["level"])
    print()
    print(report["diagnosis"]["advice"])
    print()

    # 测试转型计划
    print("\n测试2: 生成转型计划")
    print("-" * 60)
    plan = agent.generate_transformation_plan("从传统组织到AI Native")
    print(plan["phases"][0]["name"])
    print()

    print("✓ Agent测试完成")
