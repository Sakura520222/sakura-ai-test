# 项目概述文档 - sakura-ai-test

## 1. 项目简介
本项目是专门为测试和演示 Sakura-AI 智能代理（Sakura Agent）能力而创建的实验性项目，验证 AI 在不同场景下的表现、功能实现和交互流程。支持中英双语文档，具备 CLI 交互、游戏玩法模块及基础测试与 Issue 处理流程。

## 2. 技术栈
- **核心语言**：Python 3.x（内置标准库 `argparse`）
- **依赖与包管理**：`uv`（推荐，配置文件 `pyproject.toml` + `uv.lock`）、`pip`（`requirements.txt` 同步维持兼容）
- **代码规范与测试**：`pytest`（测试框架）、`ruff`（代码检查/格式化工具）
- **核心入口**：`main.py`、`src/cli.py`（控制台 CLI 入口）

## 3. 项目结构
- `/src`：核心业务逻辑代码（`cli.py` 控制台命令行接口，`games.py` 迷你游戏逻辑）
- `/tests`：测试用例目录（已配置 pytest，测试覆盖率良好）
- `README.md`：项目说明文档（中英双语）
- `pyproject.toml` / `uv.lock` / `requirements.txt`：包管理与依赖配置
- `.sakura/`：项目知识库与审查反思记录

## 4. 开发与命令行交互规范
- **Issue 管理**：
  - 建立标签体系（`documentation`、`enhancement`、`invalid`、`placeholder`），区分纯测试占位与真实需求。
  - 统一标题规范：`[type][priority] 描述`。
  - 自动化与重复检测：使用关键词（"测试"、"占位"、"test"）及作者/时间维进行极简 Issue 快速筛选与关单。
- **CLI 与终端交互规范**：
  - **入口可测试性**：CLI 入口函数必须支持可选参数传递（如 `def run(argv=None)`），解耦 `sys.argv`，便于高效测试。
  - **终端编码防御**：针对非 ASCII（中文/Emoji）控制台输出，封装 `_safe_print` 并提供 `try-except UnicodeEncodeError` 降级，或提供 `--ascii-only` 开关以兼容 Windows GBK/cp936 环境。
  - **入口与架构隔离**：`console_scripts` 入口模块必须包含 `if __name__ == "__main__":` 保护；CLI 接入层使用桥接/代理模式，仅作参数分发，业务逻辑全量复用或委派给对应业务模块。

## 5. 审查规范
- **副作用与入口保护**：修改包含顶层执行逻辑的文件时，必须评估 `if __name__ == "__main__":` 隔离保护。
- **依赖与锁文件联动**：修改 `pyproject.toml` 依赖声明时，必须同时运行 `uv lock` 更新 `uv.lock`，并在多依赖源（`requirements.txt`）间保持交叉同步。
- **编码与 CI 环境兼容**：评估 I/O 操作时不能假定纯 UTF-8，须对 Windows GBK 等环境做防爆破降级处理。
- **同类缺陷横向扫描**：修复/改进某一配置或工具声明时，需扫描项目中是否存在同类路径（如 pip 备用路径）漏掉更新。

## 6. 关键经验教训
- 极小变动亦需评估编码、lint、CI 风险；涉及 CLI 与输出 print 时需将编码容错列为标准 Checklist。
- 依赖及配置修改切勿导致锁文件漂移，文档推荐工具应与项目依赖版本同步维护。
- 置信度评估需与分析结论逻辑闭环；针对灰色占位 Issue，应建立条件分支机制（如超时无响应自动关单）。

累计反思 5 次