def add_features(data):
    data['MA50'] = data['Close'].rolling(window=50).mean()  # 50-day Moving Average
    data['MA200'] = data['Close'].rolling(window=200).mean()  # 200-day Moving Average
    data['Volume_Change'] = data['Volume'].pct_change()  # Volume change percentage
    return data