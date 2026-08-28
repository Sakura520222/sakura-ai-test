# 项目概述文档 - sakura-ai-test

## 1. 项目简介
专门为测试和演示 Sakura-AI 智能代理能力而创建的实验性项目，验证 AI 在不同场景下的表现、功能实现和交互流程。支持双语文档，目前处于早期阶段，已建立基础的 Issue 测试流程。

## 2. 技术栈
- **主要语言**：Python
- **测试框架**：pytest
- **核心文件**：main.py（当前仅包含简单打印输出）、requirements.txt

## 3. 项目结构
- `/src`：核心业务逻辑代码（规划中）
- `/tests`：测试用例目录（已配置 pytest）
- `README.md`：项目说明文档（中英双语）
- `requirements.txt`：依赖列表（仅含 pytest）
- `.sakura/`：项目知识库与反思记录

## 4. 开发约定
- **Issue 管理**：建立标签体系（invalid、documentation、enhancement），对占位类 Issue 使用 `invalid` 快速关闭
- **标题规范**：建议采用 `[type][priority] 描述` 格式，提升可读性
- **重复检测**：对低信息量 Issue 使用关键词匹配，如 "测试"、"占位"、"test"
- **编码规范**：涉及特殊字符输出需确保 UTF-8 编码，注意 lint 检查

## 5. 关键经验教训
- Issue 分析前需通过搜索确认代码实际结构，避免误判
- 建立标签字典保持一致性（如 documentation → docs）
- 极小改动也需评估编码、lint、CI 风险
- 重复检测需人工核对，防止误报/漏报
- 建议创建 Issue 模板和占位 Issue 处理流程，提升效率

累计反思 5 次