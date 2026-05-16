#!/usr/bin/env python3
"""
AI Native Organization Agent - CLI工具
"""

import sys
import subprocess
from agent import AI_native_Org_Agent


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("AI Native Organization Agent - CLI")
        print()
        print("用法:")
        print("  python3 agent.py \"问题描述\"")
        print("  python3 agent.py --test")
        print()
        print("示例:")
        print("  python3 agent.py '如何评估组织AI化程度？'")
        print("  python3 agent.py '从传统组织到AI Native的转型计划'")
        print("  python3 agent.py 'AI咨询如何定价？'")
        return

    if sys.argv[1] == "--test":
        # 测试模式
        agent = AI_native_Org_Agent()
        print(agent.ask("如何评估组织AI化程度？"))
        return

    # 模式：用户问题
    question = " ".join(sys.argv[1:])
    agent = AI_native_Org_Agent()

    print("=" * 60)
    print("AI Native Organization Agent")
    print("=" * 60)
    print()
    print(f"问题: {question}")
    print()
    print("-" * 60)
    print()

    answer = agent.ask(question)
    print(answer)
    print()
    print("-" * 60)


if __name__ == "__main__":
    main()
