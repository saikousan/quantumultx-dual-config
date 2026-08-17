# Clash Verge 配置说明

`Clash-Verge-Full.yaml` 是公开模板，不含节点、UUID、密码或机场订阅。导入 Clash Verge Rev 后可直接启动，但由于没有私人节点，策略组只有 `DIRECT`，用于检查结构和规则。

私人版在 iCloud Drive 的 `Clash Verge/Clash-Verge-Personal.yaml`，包含两元店、赔钱机场和 `Dubai` 节点。Mihomo 的 `url-test` 按健康检查 URL 的响应延迟选择最快节点；它不是持续下载测速，不能等同 Netflix 实际带宽。AI 策略使用美国节点优选，故障时回退 `Dubai`。

私人版已包含 Windows TUN（mixed stack、自动路由和 DNS 劫持）；首次启动若提示管理员权限请选择允许。若 Clash Verge 的 UI 覆盖了配置，以 UI 中的 TUN 开关为准。

配置采用 Mihomo 原生 `proxy-providers`、`url-test`、`fallback`、`GEOSITE` 和 `GEOIP`，规则顺序与 QX/Shadowrocket 保持一致：局域网/NAS直连、中国服务直连、AI/媒体专用策略、普通海外自动优选、最终兜底。

参考并采用的成熟方案：MetaCubeX/mihomo 官方配置示例和 `meta-rules-dat` 地理数据；ACL4SSR 的规则组织思路；blackmatrix7 的应用规则维护方式。公共模板不直接引用私人资源。
