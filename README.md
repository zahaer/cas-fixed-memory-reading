# CAS Fixed-Memory Reading

本项目验证一个收紧的问题：冻结已有 cartridge 的 K/V 与基础模型权重时，读取侧的可泛化修正是否能缓解多块 memory 的组合退化。当前处于源码审计和 pilot 阶段，不声称完成 CAS 忠实复现，也不预设 block bias 为正确答案。

目录：`papers/` 锁定论文，`vendor/cartridges/` 源码快照，`cas_ext/` 诊断组件，`configs/` 配置，`scripts/` smoke test，`results/` 运行记录。
