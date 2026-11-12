<div align="center">
  <h1>Guardian Safety</h1>
  <p><strong>面向 AI Agent 的个人安全响应 Skill</strong></p>
  <p>在危险预防、紧急响应、法律信息导航和事后整理中，提供清晰、克制且可执行的行动支持。</p>
  <p>
    <a href="https://github.com/GreatXiaoRY/guardian-safety/releases/latest"><img alt="Release" src="https://img.shields.io/github/v/release/GreatXiaoRY/guardian-safety?display_name=tag&amp;sort=semver"></a>
    <a href="LICENSE"><img alt="License" src="https://img.shields.io/github/license/GreatXiaoRY/guardian-safety"></a>
    <a href="https://github.com/GreatXiaoRY/guardian-safety/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/GreatXiaoRY/guardian-safety?style=flat"></a>
    <a href="README.md"><img alt="Language" src="https://img.shields.io/badge/language-%E4%B8%AD%E6%96%87-dc2626"></a>
  </p>
  <p>
    <a href="#快速开始">快速开始</a> ·
    <a href="#支持场景">支持场景</a> ·
    <a href="#设计原则">设计原则</a> ·
    <a href="#项目结构">项目结构</a> ·
    <a href="#参与贡献">参与贡献</a>
  </p>
</div>

> [!IMPORTANT]
> 若存在即时生命危险，请优先联系所在地紧急服务或现场专业人员，不要等待 AI 回复。Guardian 不替代紧急调度、医疗诊断或正式法律意见。

## 项目简介

Guardian Safety 是一个平台无关的文档型 Agent Skill。它为兼容 Skills 机制的 AI Agent 提供统一的人身安全响应规则，使 Agent 能够：

- 在紧急情形中先给行动建议，再询问必要信息。
- 把生命安全置于取证、财物和流程之前。
- 区分真实工具能力、权限状态和执行结果。
- 在定位、通信或网络不可用时提供人工替代方案。
- 尊重用户选择，减少不必要的敏感信息收集。
- 按辖区核实紧急号码和法律信息，不猜测或虚构结果。

Guardian 本身不运行后端服务，不保存用户数据，也不绑定特定模型或 Agent 平台。

## 快速开始

### 1. 获取项目

```bash
git clone https://github.com/GreatXiaoRY/guardian-safety.git
```

也可以从 [Releases](https://github.com/GreatXiaoRY/guardian-safety/releases/latest) 下载最新版本。

### 2. 安装 Skill

将完整的 `guardian-safety` 目录放入目标 Agent 支持的 Skills 目录，并按照该 Agent 的官方说明启用。

安装时请保留以下内容：

- `SKILL.md`：Skill 入口、激活条件和响应规则。
- `references/`：核心安全规则、场景流程和专题边界。
- `assets/`：可复制或填写的用户模板。

不同 Agent 的目录位置和发现机制可能不同，本项目不假定具体安装路径。

### 3. 开始使用

在已启用 Guardian 的 Agent 中直接描述需求：

```text
我正在被人跟踪，附近有一家营业中的商店。
```

```text
帮我制定一个独自夜间回家的安全确认计划。
```

```text
危险已经解除，请帮我按事实整理事件时间线。
```

Agent 会根据情况选择相应模式，并优先给出用户当前可以执行的下一步。

## 工作模式

| 模式 | 适用情况 | 主要目标 |
|---|---|---|
| `PREPARE` | 出行、会面或其他活动前的安全规划 | 制定联系人、签到、失联升级和备用方案 |
| `EMERGENCY` | 威胁、事故、受困或医疗急症正在发生 | 优先降低即时伤害并连接当地救援 |
| `LEGAL_SUPPORT` | 拘留、事故责任或寻找法律援助信息 | 确认辖区并导航至可核实的官方资源 |
| `AFTERCARE` | 危险解除后的记录与后续安排 | 整理事实、原始材料和专业支持选项 |

## 支持场景

| 场景 | 说明 |
|---|---|
| [事前安全规划](references/scenarios/pre-incident-planning.md) | 联系人、签到、路线、设备 SOS 和备用方案 |
| [交通事故](references/scenarios/vehicle-accident.md) | 现场安全、伤者求助、受困报告和事后信息整理 |
| [人身威胁](references/scenarios/personal-threat.md) | 跟踪、骚扰、威胁和迫近危险 |
| [绑架与限制自由](references/scenarios/abduction-and-confinement.md) | 沟通安全、低暴露求助和最低风险行动 |
| [逮捕与拘留](references/scenarios/arrest-and-detention.md) | 避免对抗并请求律师、翻译或医疗协助 |
| [医疗紧急事件](references/scenarios/medical-emergency.md) | 紧急医疗分流和专业救援连接 |
| [事后处理](references/scenarios/post-incident.md) | 时间线、材料清单和后续支持 |

## 设计原则

Guardian 的行为由[核心安全原则](references/core/safety-principles.md)统一约束，场景文件不能覆盖这些规则。

| 原则 | 行为要求 |
|---|---|
| 生命安全优先 | 不为取证、财物或完整问答延误撤离和求助 |
| 能力诚实 | 没有可信工具回执时，不声称已经定位、拨号、发送或上传 |
| 隐私最小化 | 只询问当前行动所需信息，外部分享前取得明确授权 |
| 辖区核实 | 不根据语言、时区或模型推测紧急号码和法律规则 |
| 用户自主 | 提供选项和风险，不强迫报警、联系特定人员或披露身份 |
| 安全降级 | 工具、权限或网络不可用时，立即给出可执行的人工方案 |

更多设计说明见[安全设计](docs/SAFETY-CASE.md)和[架构说明](docs/ARCHITECTURE.md)。

## 用户模板

| 模板 | 用途 |
|---|---|
| [紧急消息模板](assets/emergency-message-template.md) | 用最少必要信息描述位置、危险和所需帮助 |
| [个人安全计划](assets/personal-safety-plan.md) | 记录联系人、签到安排、升级步骤和备用方案 |
| [事件记录模板](assets/incident-report-template.md) | 在危险解除后整理事实、时间线和原始材料 |

模板由用户自行决定是否填写、保存或分享，不代表消息已经发送或资料已经上传。

## 项目结构

```text
guardian-safety/
|-- SKILL.md                 # Skill 入口与路由
|-- references/
|   |-- core/                # 核心安全、风险、应急、能力和隐私规则
|   |-- scenarios/           # 七类场景流程
|   |-- evidence/            # 证据保全与记录边界
|   |-- legal/               # 法律信息与辖区核实
|   `-- integrations/        # 工具能力契约与集成安全
|-- assets/                  # 用户模板
|-- tests/                   # 行为测试案例
|-- scripts/                 # 项目结构检查脚本
`-- docs/                    # 架构、安全设计与路线图
```

## 能力边界

- Guardian 是指令和参考文档集合，不是救援服务或设备控制程序。
- Skill 本身不能定位、拨号、发送消息、录音录像、上传资料或联系第三方。
- 外部工具必须同时满足能力存在、权限可用、用户明确授权和可信回执四项条件。
- 法律、紧急号码、求助渠道和设备 SOS 功能因地区及设备而异，使用前必须核实。
- Guardian 不提供医疗诊断、正式法律意见或任何结果保证。

集成开发者应阅读[工具能力契约](references/integrations/tool-capability-contract.md)和[集成安全要求](references/integrations/integration-safety.md)。

## 开发

项目检查脚本仅依赖 Python 标准库：

```bash
python scripts/check_references.py
```

脚本检查必需文件、Markdown 本地链接、Skill frontmatter、场景章节和测试编号。行为测试的格式与记录方法见 [tests/README.md](tests/README.md)。

## 参与贡献

欢迎提交问题报告和改进补丁。贡献前请阅读：

- [贡献指南](CONTRIBUTING.md)
- [行为准则](CODE_OF_CONDUCT.md)
- [安全原则](references/core/safety-principles.md)

请勿在公开 Issue、讨论或补丁中提交真实身份、精确位置、医疗记录、凭据或可识别的敏感事件资料。安全问题请按照 [SECURITY.md](SECURITY.md) 提供的方式报告。

## 版本与路线图

- 当前版本：[v1.0.0](https://github.com/GreatXiaoRY/guardian-safety/releases/tag/v1.0.0)
- 版本记录：[CHANGELOG.md](CHANGELOG.md)
- 后续方向：[docs/ROADMAP.md](docs/ROADMAP.md)

## 许可证

Guardian Safety 采用 [Apache License 2.0](LICENSE) 发布。
