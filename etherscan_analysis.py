import requests
import pandas as pd

# 替换为你自己的 API KEY
API_KEY = "56KXZMNN9P7HKBEDWH1KFUVGMH5N6NWYGD"
address = "0x742d35Cc6634C0532925a3b844Bc454e4438f44e"  # 示例地址

# 构造请求 URL
url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&sort=desc&apikey={API_KEY}"

# 获取数据
response = requests.get(url)
data = response.json()
print(data)
# 提取交易列表
txs = data.get("result", [])

# 转换为 DataFrame 方便处理
df = pd.DataFrame(txs)

# 显示最近 5 条交易
print(df[["hash", "from", "to", "value"]].head())

from_address = address.lower()  # 当前分析的地址

# 1. 总交易数
total_tx = len(df)

# 2. 总接收金额（单位：ETH）
received = df[df["to"].str.lower() == from_address]["value"].astype(float).sum() / 1e18

# 3. 总转出金额（单位：ETH）
sent = df[df["from"].str.lower() == from_address]["value"].astype(float).sum() / 1e18

# 4. 活跃交易对手地址（出现最多的对方地址）
counterparties = pd.concat([
    df[df["from"].str.lower() == from_address]["to"],
    df[df["to"].str.lower() == from_address]["from"]
])

top_counterparty = counterparties.value_counts().head(1).index[0]

# 5. 单笔最大交易额（ETH）
max_value = df["value"].astype(float).max() / 1e18

# 输出画像
print("\n📍 链上地址画像")
print(f"📌 地址：{address}")
print(f"🔁 总交易次数：{total_tx}")
print(f"💰 总接收金额：{received:.4f} ETH")
print(f"💸 总转出金额：{sent:.4f} ETH")
print(f"🤝 最频繁交易对手地址：{top_counterparty}")
print(f"🚀 最大单笔交易金额：{max_value:.4f} ETH")
