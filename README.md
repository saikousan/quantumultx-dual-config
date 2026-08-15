# Quantumult X 双配置模板

这是不含私人订阅、UUID、密码和 Reality 密钥的公开模板仓库。配置主体来自墨鱼配置，结合 Profiles4limbo、KOP-XIAO、blackmatrix7、AdRules 和 Sub-Store 的公开模块。

## 文件

- `AppleTV-Gateway.conf`：Apple TV 旁路由，优先保证局域网和 Infuse/NAS 稳定。
- `Desktop-Mobile-Full.conf`：手机和电脑使用，包含远程规则、广告重写和 AI 分流。
- 策略组统一使用“我的”前缀，例如“我的自动优选”“我的AI故障切换”“我的远程连接”“我的兜底”。
- Netflix、Disney+、TikTok 使用“我的自动优选”，不再强制美国节点；只有 AI 使用美国优选。
- AI 规则进入“我的AI故障切换”，只筛选美国和 `Dubai` 节点，避免策略组互相嵌套导致 QX 报错。
- Apple TV 使用仓库内的 `resource-parser.js`；GitHub Actions 会从 KOP-XIAO 自动同步解析器，避免 TV 端依赖失效或被限速的第三方解析地址。

完整版还包括 Netflix、Disney+、TikTok、OpenAI、Bard、Claude、机场专线、毒奶广告计划、Sub-Store 以及墨鱼的开屏广告、微博、小红书、百度网盘等远程模块。Apple TV 版保留必要的分流模块，但关闭重写、任务和 UDP 丢弃，避免影响 NAS 视频吞吐。

## 使用前必须填写

在 `[server_remote]` 中加入自己的机场订阅；在 `[server_local]` 中加入自建节点。不要把真实订阅地址提交到公开仓库。
对于 Shadowrocket/AnyTLS 格式，在订阅地址后加 `#UA=1`，让解析器用 Shadowrocket UA 重试获取节点。

截图中的“资源解析器”开关对应 `opt-parser=true`。Apple TV 没有该 UI 开关时，不能靠全局地址强制所有手动添加的资源开启解析；应把机场放入 `[server_remote]`，配置会自动启用解析。手动在 TV 的“资源-节点”页面添加资源时，仍可能需要设备端支持该开关。

## 远程 IPv4/IPv6 服务

个人远程服务应在私有版本中加入“我的远程连接”策略。该策略提供代理和直连两个选项；公开模板不包含任何个人 IP、域名或 NAS 地址。QX 会按系统 DNS 同时解析 A/AAAA；没有启用 `no-ipv6`，也没有关闭系统 DNS。

## 规则来源

配置只引用公开、可更新的规则模块；私人订阅应通过私有 NAS 地址或私有配置服务提供。

## 自动更新

QX 会按照配置中的 `update-interval` 自动拉取墨鱼、毒奶、blackmatrix7、AdRules 等模块。GitHub Actions 每 6 小时检查一次公开模块并更新 [`UPSTREAM_STATUS.md`](UPSTREAM_STATUS.md)，这样可以看到上游是否可访问或发生变化；不会把私人订阅同步到公开仓库。
