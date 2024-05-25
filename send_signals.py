import requests
import pandas as pd

# 示例代码
data = {
    'Date': ['2023-01-01', '2023-02-01', '2023-03-01'],
    'Signal': [1, -1, 1]
}
df = pd.DataFrame(data)
df.to_csv('signals.csv', index=False)

# Pipedream Webhook URL
webhook_url = "https://your-pipedream-webhook-url"

# 读取信号数据并发送
data = pd.read_csv('signals.csv')
for index, row in data.iterrows():
    signal_data = {
        "Date": row['Date'],
        "Signal": row['Signal']
    }
    response = requests.post(webhook_url, json=signal_data)
    print(f"Status Code: {response.status_code}, Response Text: {response.text}")
