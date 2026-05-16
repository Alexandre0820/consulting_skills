#!/bin/bash
# AI Native Organization Agent - 安装脚本

echo "=== AI Native Organization Agent 安装 ==="
echo ""

# 检查Python版本
echo "检查Python版本..."
python3 --version

# 安装依赖
echo ""
echo "安装依赖..."
pip3 install -q python-dotenv 2>/dev/null || echo "python-dotenv 已安装"

# 创建必要的目录
echo ""
echo "创建目录结构..."
mkdir -p knowledge-base/wiki
mkdir -p knowledge-base/outputs
mkdir -p knowledge-base/raw
mkdir -p tools

# 复制知识索引
echo ""
echo "复制知识索引..."
cp /Users/shengyun/lobsterai/project/alex-clone-knowledge-index.md knowledge-base/ 2>/dev/null || echo "索引文件未找到"

# 设置执行权限
chmod +x agent.py
chmod +x knowledge-retriever.sh
chmod +x tools/engine.py

# 显示目录结构
echo ""
echo "安装完成!"
echo ""
echo "项目结构:"
echo "agent.py              - Agent核心引擎"
echo "knowledge-retriever.sh - 知识检索器"
echo "tools/engine.py       - 工具集"
echo "prompts/system.md     - System Prompt"
echo ""
echo "使用方法:"
echo "  python3 agent.py --test"
echo ""
echo "或通过CLI使用:"
echo "  ./agent-cli.sh \"你的问题\""
