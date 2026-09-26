# 项目记忆

累计反思 5 次

## 标签体系与 Issue 管理
- 优先检查仓库现有标签，统一使用 `invalid` 标记无效/非需求，`wontfix` 用于已知缺陷不修复
- 可建立 `placeholder`、`test`、`trivial` 等标签；`invalid` 与 `wontfix`/`enhancement` 等语义互斥，不可混用
- 占位/测试 Issue 统一规范：分类 `other` + 优先级 `low` + 标签 `invalid`（或 `placeholder`）
- 在 Issue 模板提供 `placeholder` / 测试选项，极简标题/单字 Issue 设自动过滤规则
- 定期审查 low/invalid Issue；关闭时添加标准注释（如“仅为测试占位，无实际需求”）
- 标题前缀遵守 `[type][priority]` 规范（若项目统一采用），无意义标题（如 "cs"）须重构改写

## CLI 与终端交互规范
- CLI 入口函数必须支持接收参数列表（如 `def run(argv=None)`），实现控制层与测试隔离
- 涉及非 ASCII 输出的 CLI 工具，统一采用 `try/except UnicodeEncodeError` 降级或提供 `--ascii-only` 开关，兼容 Windows GBK 等环境
- 新增 CLI 命令必须优先复用/委派现有业务模块，防止重构冗余业务逻辑
- `console_scripts` 入口模块必须使用 `if __name__ == "__main__":` 隔离防护

## 可行性判断与改动要点
- 分析前先执行 `repo_browser.search` 或 `grep` 确认目标文件实际内容与历史变更
- 特殊字符/print 输出需评估编码风险与 `if __name__ == "__main__":` 封装必要性
- 在给新手或模糊需求编写建议时，可提供“澄清菜单/选项步骤”降低沟通成本
- 修改包含顶层执行逻辑的文件时，评估其对外部 import 的影响；频繁变动模块适时启动重构

## 重复检测与交叉验证
- 结合标题、关键词、关联 PR、提交时间及作者多维度比对重复 Issue
- **依赖与锁文件联动**：修改依赖声明（如 `pyproject.toml`）必须同步更新锁文件（如 `uv.lock`）；提出依赖建议时需提示重新生成锁文件
- **多途径安装一致性**：若仓库保留 pip 与 uv 等多种依赖安装途径，需扫描多源（如 `requirements.txt` 和 `pyproject.toml`）确保一致
- 极简仓库中，复杂业务逻辑 Issue 优先按「无效/关联错误」处理