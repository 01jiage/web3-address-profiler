# Web3 Address Transaction Analyzer

这是一个用于分析链上地址交易记录的 Python 工具，目前支持以太坊和 OKC 等兼容 EVM 的链。

## 📌 项目简介

本项目通过访问区块链浏览器（如 OKLink 或 Etherscan）获取地址交易数据，并进行如下处理：

- 获取地址的最近交易记录
- 转换时间戳为可读时间
- 输出标准化的交易数据表格
- 为后续分析（如 Token 分析、地址画像等）做准备

## 🔧 技术栈

- Python 3.x
- [pandas](https://pandas.pydata.org/)
- [requests](https://docs.python-requests.org/)
- 可选：matplotlib（用于可视化扩展）

## 📥 安装依赖

```bash
pip install pandas requests
