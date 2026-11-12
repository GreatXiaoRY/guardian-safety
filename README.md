# Guardian Safety

Guardian 是面向兼容 AI Agent 的个人安全应急响应 Skill，帮助用户进行危险预防、紧急行动导航、法律信息查询和事后整理。当前版本为 **v1.0.0**，采用平台无关的文档型 Skill 结构。

## 安装

将本仓库目录放入兼容 Agent 支持的 Skills 目录，并按该 Agent 的官方说明启用。不同 Agent 的安装位置和发现机制可能不同；本项目不假定特定平台。

## 使用

在兼容 Agent 中描述实际需求，例如：

- “我正在被跟踪，附近有一家营业中的商店。”
- “帮我事先制定独自出行的安全确认计划。”
- “危险已经解除，请帮我按事实整理事件时间线。”

若有即时生命危险，请优先联系所在地紧急服务或现场专业人员，不要等待 AI 回复。

## 支持场景

Guardian 支持 PREPARE、EMERGENCY、LEGAL_SUPPORT、AFTERCARE 四种模式，覆盖：

- 独自出行等事前安全规划。
- 交通事故、人身威胁、限制自由和医疗急症。
- 逮捕、拘留和法律援助信息导航。
- 危险解除后的事实时间线、材料和后续事项整理。

项目还提供求救消息、个人安全计划和事件记录模板。

## 限制

- Skill 本身不能定位、拨号、发送消息、录音录像、上传资料或联系任何人。
- 不提供正式法律意见或医疗诊断，也不维护全球法律数据库。
- 法律、求助渠道、设备 SOS 功能和网络可用性因地区和设备而异，必须核实。
- AI 可能出错，不应替代紧急调度、专业医疗或当地律师。

## 贡献

提交变更前，请阅读[贡献指南](CONTRIBUTING.md)、[安全原则](references/core/safety-principles.md)和[集成安全要求](references/integrations/integration-safety.md)。项目结构见[架构说明](docs/ARCHITECTURE.md)，安全问题请按 [SECURITY.md](SECURITY.md) 报告。

## 许可

本项目采用 Apache-2.0 许可，详见 [LICENSE](LICENSE)。
