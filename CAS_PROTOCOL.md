# CAS_PROTOCOL

| 字段 | 论文原设 | 当前实现 | 状态 |
|---|---|---|---|
| 主模型 | Qwen3-8B | 尚未运行 | 待核实 |
| LongHealth 文档 | 20 位患者记录 | 数据快照未定位 | 阻塞 |
| 问题 | 400，约 20/文档 | 尚未运行 | 待核实 |
| 压缩 | 20x，约 585 tokens/cartridge | 尚未实现 | 待核实 |
| 训练 | 80 epochs；isolated 与 25% mixed，active 10/20 | 尚未实现 | 待核实 |
| 表 3 Full 核对 | isolated 26.0±3.1；joint 20 active 77.8±0.6 | 不得当作本项目结果 | 仅核对目标 |
| 表 3 Oracle 核对 | isolated 73.6±0.4；joint 20 active 79.0±1.4 | 不得当作本项目结果 | 仅核对目标 |

仓库原版 LongHealth 示例使用 10 位患者和不同模型/配置，不能替代上述协议。固定 K/V 的读取修复是本项目主问题；CAS joint training、检索、长度归一化和 block bias 都是对照或待验证探针。
