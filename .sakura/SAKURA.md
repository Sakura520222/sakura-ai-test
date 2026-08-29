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

## 5. 审查规范（新增）
- **副作用阻断规则**：若修改包含顶层执行逻辑（如 print、数据库连接）的文件，必须评估 `if __name__ == "__main__":` 封装的必要性
- **编码兼容性检查**：涉及非 ASCII 输出的 print 语句必须包含 `try/except UnicodeEncodeError` 处理，或封装为 `safe_print` 工具函数
- **截图内容强验证**：Issue 仅含截图（特别是外部平台截图）时，必须强制进行代码库关键词检索，确认是否为本项目产生
- **CI/环境敏感度**：审查涉及 I/O 操作的代码时，需考虑实际运行环境（如 Windows GBK），不能仅假设 UTF-8 环境

## 6. 关键经验教训
- Issue 分析前需通过搜索确认代码实际结构，避免误判
- 建立标签字典保持一致性（如 documentation → docs），统一使用 `invalid` 而非 `wontfix` 处理占位 Issue
- 极小改动也需评估编码、lint、CI 风险，尤其是特殊字符输出
- 重复检测需人工核对，防止误报/漏报
- 置信度需与分析结论逻辑闭环：若否定某分类，对应置信度应接近 0
- 极简仓库中，任何复杂业务逻辑 Issue 应优先按无效/关联错误处理
- 建议创建 Issue 模板和占位 Issue 处理流程，引入自动化过滤规则
- 定期审计 low/invalid Issue，保持列表清洁度

累计反思 5 次