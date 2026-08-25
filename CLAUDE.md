# CLAUDE.md

本文件为 Claude Code (claude.ai/code) 在本代码仓库中工作时提供指导。

## 命令

以下为本仓库中常用命令：

- **运行主程序**：`python main.py`
- **安装依赖**：`pip install -r requirements.txt`（如配置了依赖文件）
- **运行测试**：`pytest`（如存在测试目录）
- **代码检查**：`pylint` 或 `flake8`（如已配置）
- **构建**：本 Python 测试仓库无需构建步骤

## 架构与结构

本仓库为 Sakura-AI 功能测试仓库。基于当前状态：

- 本仓库主要用于测试 Sakura-AI 的 Issue 分析、PR 审查、仓库扫描及 Agent 模式
- **Issue 分析**：创建新 Issue 时会自动触发，提供分类、优先级评估及修改建议
- **PR 审查**：创建或更新 PR 时自动触发，检查代码质量、风格及完整性
- **Agent 模式**：在 Issue 或 PR 评论区输入 `/agent` 即可激活基于任务的自主 Agent
- **仓库扫描**：探索代码库结构并检测代码模式

关键文件与目录：
- `main.py` — 示例主入口脚本
- `.sakura/memory/` — 存储 Issue 分析及 PR 审查记录
- `.sakura/memory/*.md` — 各个 Issue/PR 分析与反思记录
- `README.md` — 项目概述与说明
- `.git/` — 标准 Git 仓库

本项目当前设计为测试 Sakura-AI 机器人功能的沙箱环境。

## 如何在本代码库中开发与测试

1. **触发 Issue 分析**：
   - **自动触发**：在 GitHub 仓库中新建 Issue，Sakura-AI 会自动分析并输出分类、优先级评估与建议。
   - **交互处理**：在对应 Issue 评论区发送 `/agent` 启动自主 Agent 处理任务。

2. **触发 PR 审查**：
   - 创建 Pull Request 后，Sakura-AI 将自动对代码变更进行多维度审查（功能正确性、代码规范、文档完整性等）。

3. **记忆系统与沉淀**：
   - 所有 Issue/PR 的分析与反思记录会持久化保存至 `.sakura/memory/`，可作为后续开发与审查的上下文参考。