# Shadowrocket modules

The main public configuration keeps MITM and scripts disabled by default. Add only the modules you actually need in Shadowrocket. A module containing `[MITM]` must use `hostname = %APPEND% ...` so it does not overwrite another module's hostnames. This follows the public Shadowrocket documentation and examples.

Recommended public sources:

- [墨鱼 AdBlock4limbo](https://raw.githubusercontent.com/limbopro/Adblock4limbo/main/Adblock4limbo.conf)
- [黑名单/规则脚本](https://github.com/blackmatrix7/ios_rule_script/tree/master/rule/Shadowrocket)
- [小火箭去广告模块合集](https://github.com/deezertidal/shadowrocket-rules/tree/main/modules)

Do not enable multiple overlapping MITM ad modules at the same time; overlapping rewrites can cause login or playback failures.
