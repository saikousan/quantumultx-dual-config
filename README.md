# Quantumult X 双配置模板

这是不含私人订阅、UUID、密码和 Reality 密钥的公开模板仓库。

## 文件

- `AppleTV-Gateway.conf`：Apple TV 旁路由，优先保证局域网和 Infuse/NAS 稳定。
- `Desktop-Mobile-Full.conf`：手机和电脑使用，包含远程规则、广告重写和 AI 分流。

## 使用前必须填写

在 `[server_remote]` 中加入自己的机场订阅；在 `[server_local]` 中加入自建节点。不要把真实订阅地址提交到公开仓库。

## 远程 IPv4/IPv6 服务

`8.135.238.135`、`cg123.fun`、`deackseed.top` 被单独归入“远程连接”策略。该策略提供代理和直连两个选项，默认交给节点策略，避免因为本地 IPv6、运营商 NAT 或回源路由不同而失败。QX 会按系统 DNS 同时解析 A/AAAA；没有启用 `no-ipv6`，也没有关闭系统 DNS。

## 规则来源

配置只引用公开、可更新的规则模块；私人订阅应通过私有 NAS 地址或私有配置服务提供。
