# ENVIRONMENT

记录时间：2026-10-17（Asia/Shanghai）。

- Host/user: `a100` / `ruoyuzhao`。
- Remote workdir: `/nvme3n1/ZhengTaoworks/cyf/cas-fixed-memory-reading`。
- GPU: 8 x NVIDIA A100-PCIE-40GB；检查时 GPU 7 约 40,441 MiB free。
- `/nvme3n1` 可用空间约 21 GB。
- 可复用环境：`/home/ruoyuzhao/miniconda3/envs/slime/bin/python`，Python 3.12.13，torch 2.9.1+cu129，transformers 4.57.1。
- Cartridges 声明 Python >=3.12、Transformers >=4.49.0 且 <=4.55，并依赖 `pydrantic`。当前 slime 环境无 `pydrantic`，Transformers 4.57.1 超出声明上限；未修改该环境。
- Qwen3-4B 位于 `/nvme1n1/LLM/Qwen3-4B`；LongHealth `benchmark_v5.json` 未在已检查数据盘找到。

这支持后续工程 pilot，但不能作为已验证的论文复现环境。
