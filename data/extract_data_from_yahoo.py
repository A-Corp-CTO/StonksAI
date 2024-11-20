import yfinance as yf

def extract_data(stocks,start,end):
    data = yf.download(stocks, start=start, end=end,auto_adjust=True)
    #How do we want the data to be structured ?
    #Unpivot Ticker name so that we have date, ticker, OHLC
    #Maybe need to test how the data structure affects the perf
    return data
