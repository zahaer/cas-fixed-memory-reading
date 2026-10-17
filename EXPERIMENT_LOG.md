# EXPERIMENT_LOG

## 2026-10-17：源码与环境审计

- 已锁定 CAS PDF `2606.04557v1` 和 Cartridges 提交 `ef34ba97a06049c34820506e2c283746284ae5f0`。
- 已核对 `TrainableCache`、FlexAttention mask、Qwen attention、LongHealth loader 和训练入口。
- 没有运行模型训练或生成；没有下载 LongHealth；没有修改 `cyf` 父仓库。
- 阻塞：数据快照缺失、磁盘空间约 21 GB、slime 环境与 Cartridges 依赖声明有差异。

所有后续 SSH 命令显式使用 `-F C:/Users/lenovo/.ssh/config`，先 `cd /nvme3n1/ZhengTaoworks/cyf/cas-fixed-memory-reading`，失败立即停止。
