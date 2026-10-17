# FINDINGS

## 已确认

1. CAS 论文报告独立 cartridge 在 Full 多块加载下退化，并以 mixed-visibility joint training 缓解；这不是本项目的新贡献。
2. Cartridges 底座把 cartridge token 标为全局共享可见，当前 attention 调用未传入 `score_mod`；简单拼接不能证明实现了 CAS 的按样本可见性。
3. 原版 LongHealth 示例不是论文表 3 的完整 Qwen3-8B/20 文档协议。

## 尚未验证

- 固定 K/V 的读取修正是否能跨未见文档、组合和 query 泛化。
- 组合退化来自分数尺度、位置约定、压缩损失，还是共同作用。
- 只有 oracle bias 有效时，它只是诊断上限，不是方法结果。
