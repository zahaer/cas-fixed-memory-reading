# SOURCE_AUDIT

## 已确认

- CAS 论文：`papers/cas-2606.04557v1.pdf`，arXiv `2606.04557v1`。
- Cartridges：`HazyResearch/cartridges`，提交 `ef34ba97a06049c34820506e2c283746284ae5f0`。
- 截至本轮查询，GitHub API 搜索未确认 CAS 作者发布独立官方实现；这不等于断言不存在。

## 调用链和缺口

- `vendor/cartridges/cartridges/cache.py:TrainableCache` 保存每层 K/V，并把初始 cartridge 的 `seq_id` 设为 `-1`。
- `vendor/cartridges/cartridges/models/attention.py:create_block_mask_w_cache` 将 `-1` 视为所有 query 可见，不能表达每个样本可见哪些 cartridge。
- `vendor/cartridges/cartridges/models/qwen/modeling_qwen3.py:Qwen3Attention.forward` 调用 FlexAttention，但当前没有 `score_mod`。
- `vendor/cartridges/cartridges/train.py` 提供冻结基础模型、训练 cache、保存/加载和生成评测入口。
- `vendor/cartridges/examples/benchmarks/longhealth/longhealth_train.py` 是原版示例：10 位患者、Qwen3-4B 或 Llama-3.2-3B，不能直接称为 CAS 的 Qwen3-8B/20 文档复现。

本项目尚未改动底座训练器；CAS 的 mixed-visibility、cartridge identity、distractor 采样和 memory pool 管理需要后续实现。
