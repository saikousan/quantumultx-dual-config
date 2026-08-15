# Quantumult X / Shadowrocket 双客户端配置模板

这是不含私人订阅、UUID、密码和 Reality 密钥的公开模板仓库。配置主体来自墨鱼配置，结合 Profiles4limbo、KOP-XIAO、blackmatrix7、AdRules 和 Sub-Store 的公开模块。

## 文件

- `AppleTV-Gateway.conf`：Apple TV 旁路由，优先保证局域网和 Infuse/NAS 稳定。
- `Desktop-Mobile-Full.conf`：手机和电脑使用，包含远程规则、广告重写和 AI 分流。
- `Shadowrocket.conf`：小飞机公开配置模板，使用 Shadowrocket 原生 `[Proxy Group]`、`[Rule]` 和远程规则集。
- `Modules/README.md`：小飞机模块来源、更新和 MITM 叠加注意事项。
- 策略组统一使用“我的”前缀，例如“我的自动优选”“我的AI优选”“我的远程连接”“我的兜底”。
- Netflix、Disney+、TikTok 使用独立的“我的影视优选”，不强制美国节点；AI 使用美国/Dubai 延迟优选。
- AI 规则进入“我的AI优选”，只筛选美国和 `Dubai` 节点，不使用策略套策略，避免 QX 报错。
- Apple TV 使用仓库内的 `resource-parser.js`；GitHub Actions 会从 KOP-XIAO 自动同步解析器，避免 TV 端依赖失效或被限速的第三方解析地址。

完整版还包括 Netflix、Disney+、TikTok、OpenAI、Bard、Claude、机场专线、毒奶广告计划、Sub-Store 以及墨鱼的开屏广告、微博、小红书、百度网盘等远程模块。Apple TV 版保留必要的分流模块，但关闭重写、任务和 UDP 丢弃，避免影响 NAS 视频吞吐。

小飞机版参考公开的 Shadowrocket 配置说明、模块规则和分组测试语法；机场订阅需要在小飞机中以“Subscribe”单独添加，再由配置中的 `use=true` 代理组筛选。配置文件本身不会安全地注册多个订阅地址。

## 使用前必须填写

在 `[server_remote]` 中加入自己的机场订阅；在 `[server_local]` 中加入自建节点。不要把真实订阅地址提交到公开仓库。
对于 Shadowrocket/AnyTLS 格式，优先使用服务商提供的 Shadowrocket 标记；如果服务商按客户端 UA 返回不同格式，应在小飞机中直接添加 Subscribe，而不是把该 URL 当普通规则资源。

截图中的“资源解析器”开关对应 `opt-parser=true`。Apple TV 没有该 UI 开关时，不能靠全局地址强制所有手动添加的资源开启解析；应把机场放入 `[server_remote]`，配置会自动启用解析。手动在 TV 的“资源-节点”页面添加资源时，仍可能需要设备端支持该开关。

## 远程 IPv4/IPv6 服务

个人远程服务应在私有版本中加入“我的远程连接”策略。该策略提供代理和直连两个选项；公开模板不包含任何个人 IP、域名或 NAS 地址。QX 会按系统 DNS 同时解析 A/AAAA；没有启用 `no-ipv6`，也没有关闭系统 DNS。

## 规则来源

配置按“局域网/中国/Apple 直连 → 广告拦截 → AI/流媒体/国际服务 → 广义代理 → GEOIP 中国直连 → 兜底”的顺序组织，避免广义代理规则抢先匹配国内服务。

主要规则来源：

- [blackmatrix7/ios_rule_script](https://github.com/blackmatrix7/ios_rule_script)：China、Lan、Apple、BiliBili、YouTube、Telegram、Google、Microsoft、GitHub、Proxy 和各媒体/AI分类，按 24 小时更新。
- [墨鱼 ddgksf2013](https://github.com/ddgksf2013)：规则修正、广告、AI、媒体和重写模块。
- [Cats-Team AdRules](https://github.com/Cats-Team/AdRules)：广告拦截。
- [毒奶 Profiles4limbo](https://github.com/limbopro/Profiles4limbo)：AI 和流媒体补充规则。

所有远程规则都保留 `update-interval`，QX 会自动更新；Shadowrocket 的 `RULE-SET` 会由客户端按规则资源机制更新。公开仓库只引用规则地址，不包含私人订阅。

## 自动更新

QX 会按照配置中的 `update-interval` 自动拉取墨鱼、毒奶、blackmatrix7、AdRules 等模块。GitHub Actions 每 6 小时检查一次公开模块并更新 [`UPSTREAM_STATUS.md`](UPSTREAM_STATUS.md)，这样可以看到上游是否可访问或发生变化；不会把私人订阅同步到公开仓库。
