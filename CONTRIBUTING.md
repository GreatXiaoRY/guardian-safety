# 贡献指南

欢迎通过问题报告或补丁改进 Guardian。项目当前以中文为主要文档语言；修改时保持术语一致，并同步更新相关文档。

## 提交前

- 先阅读 `references/core/safety-principles.md`；新规则优先加入核心权威文件，场景仅引用和应用，不复制或覆盖核心规则。
- 新增场景须包含 Scope、Risk Indicators、Immediate Priorities、Response Workflow、Communication、Evidence Preservation、Legal Considerations、Tool Requirements、Fallback Procedures、Completion Criteria 十节。
- 新增法律信息须注明辖区、官方来源、核验日期和状态；禁止猜测法律、机构、号码或服务。
- 新增工具须在能力契约中定义参数、返回、权限、授权、失败、替代方案和预授权支持；默认不支持预授权。不得宣称接口已实现。
- 模板和测试示例只能使用虚构联系人、地点和事件，不提交真实个人或敏感事件资料。

## 质量检查

运行 `python scripts/check_references.py`。新增或变更安全行为时，同步更新相应测试用例；涉及延误救援、危险行动、虚假执行声明或越权分享的问题必须修复并重测。

## 补丁质量

使用 UTF-8、清晰 Markdown 和一致的 kebab-case 文件名。说明变更动机、受影响场景、能力边界和检查结果。不要引入不必要依赖、设备采集能力或未经授权的外部服务。
