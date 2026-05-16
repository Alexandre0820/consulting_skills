#!/bin/bash
# AI Native Organization Agent - 知识检索器
# 基于 alex-clone-rag.sh，为Agent提供结构化知识检索

WIKI_DIR="/Users/shengyun/lobsterai/project/my-ai-consulting-kb/wiki"
INDEX_FILE="/Users/shengyun/lobsterai/project/alex-clone-knowledge-index.md"

query="$1"
top_k="${2:-5}"

# 颜色
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}🔍 知识检索: ${query}${NC}"

# 1. 检索相关Wiki文件
echo ""
echo -e "${YELLOW}【相关Wiki文件】${NC}"

found_files=$(cd "$WIKI_DIR" && ls -1 *.md 2>/dev/null | grep -i "$query" | head -10)

if [ -z "$found_files" ]; then
    echo "  未找到直接匹配的文件"
    # 尝试在内容中搜索
    echo ""
    echo -e "${YELLOW}【内容片段】${NC}"
    grep -r -i -n -C 2 "$query" "$WIKI_DIR"/*.md 2>/dev/null | head -30
else
    for file in $found_files; do
        echo "  • $file"
    done
fi

# 2. 检索知识索引中的相关主题
echo ""
echo -e "${YELLOW}【知识索引匹配】${NC}"

grep -i "$query" "$INDEX_FILE" 2>/dev/null | head -10 || echo "  无索引匹配"

# 3. 返回结构化结果
echo ""
echo -e "${GREEN}检索完成${NC}"
echo "Top-K: $top_k"

# 返回JSON格式（便于Agent解析）
echo ""
echo '{"status": "success", "query": "'"$query"'", "top_k": "'$top_k'"}'