# CLAUDE.md

本文件为 Claude Code (claude.ai/code) 在本代码仓库中工作时提供指导。

## 命令

以下为本仓库中常用命令：

- **安装依赖**：`pip install -r requirements.txt`（如存在 requirements 文件）
- **运行测试**：`pytest`（如存在测试目录）
- **代码检查**：`pylint` 或 `flake8`（如已配置）
- **构建**：本 Python 测试仓库无需构建步骤
- **启动应用**：目前无主要入口点；请参阅项目 README 获取指引

## 架构与结构

本仓库为 Sakura-AI 功能测试仓库。基于当前状态：

- 本仓库主要用于测试 Sakura-AI 的 Issue 分析、PR 审查、仓库扫描及 Agent 模式
- Issue 分析可自动处理新 Issue 并提供分类、优先级评估及建议
- PR 审查可自动检查代码质量、风格及完整性
- 仓库扫描可探索代码库结构并检测模式
- 可通过 `/agent` 调用 Agent 模式以启动基于任务的 Agent

关键文件与目录：
- `.sakura/memory/` — 存储 Issue 分析及 PR 审查记录
- `.sakura/memory/*.md` — 各个 Issue/PR 分析结果
- `README.md` — 项目概述与说明
- `.git/` — 标准 Git 仓库

本项目当前源代码极少，设计为测试 Sakura-AI 机器人功能的沙箱环境。提交的 Issue 将被自动分析，创建的 PR 将被自动审查。

## 如何在本代码库中开发

1. **提交 Issue**：创建 Issue 时，系统将自动分析并提供分类、优先级评估、标签建议及标题优化。

2. **创建 PR**：PR 将自动接受质量、完整性及项目规范一致性审查。审查检查包括：
   - 功能正确性
   - 代码风格与格式
   - 文档完整性
   - 用户体验考量

3. **使用 Agent 模式**：通过在对应的Issue、PR中评论 `/agent` 调用可启动基于任务的 Agent。

4. **仓库扫描**：可扫描代码库以了解结构、检测模式，并为不熟悉的区域生成摘要。

5. **记忆系统**：历史分析结果存储于 `.sakura/memory/` 中，可供参考以获取先前 Issue 与审查的上下文。