import requests
import os
from twilio.rest import Client
from newsapi import NewsApiClient

STOCK_NAME = 'AMZN'
COMPANY_NAME = 'Amazon.com Inc'
DAYS = 2
COEFFICIENT = 0.001

STOCK_EP = 'https://www.alphavantage.co/query'

# Сomparison of market closes for the last days
def compare_stock_rate(daily_list) -> bool:
    last_days_data = list(daily_list.values())[:DAYS]
    today_close = float(last_days_data[0]['4. close'])
    yesterday_close = float(last_days_data[-1]['4. close'])

    percent = abs((today_close - yesterday_close) / yesterday_close)
    if percent > COEFFICIENT:
        return True

    return False

# Create message with last news about the company
def get_news_message(daily_list, news_num=3):
    last_days_range = list(daily_list.keys())[:DAYS]

    news_api_key = os.getenv('NEWS_API_KEY')
    newsapi = NewsApiClient(api_key=news_api_key)
    newsapi_data = newsapi.get_everything(q=COMPANY_NAME,
                                          from_param=last_days_range[0],
                                          to=last_days_range[-1],
                                          language='en',
                                          sort_by='relevancy',
                                          page=1,
                                          page_size=news_num)

    #1 for article in newsapi_data['articles']:
    #1     message += f"{article['title']}: {article['url']}\n"
    message_list = [f"Title: {article['title']}, Link: {article['url']}" for article in newsapi_data['articles']]
    return ''.join(message_list)

# Sending SMS using twilio
def send_sms(message):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    caller_phone = os.environ['TWILIO_PHONE_NUMBER']
    target_phone = os.environ['TARGET_PHONE_NUMBER']
    client = Client(account_sid, auth_token)

    client.messages.create(
        body=message,
        from_=caller_phone,
        to=target_phone
    )


def main():
    api_key = os.getenv('STOCK_API_KEY')

    parameters = {
        'function': 'TIME_SERIES_DAILY_ADJUSTED',
        'symbol': STOCK_NAME,
        'outputsize': 'compact',
        'apikey': api_key
    }

    r = requests.get(url=STOCK_EP, params=parameters)

    daily_list = r.json()['Time Series (Daily)']

    if compare_stock_rate(daily_list):
        print('Sending message...')
        # send_sms(f"Hello, We have significant changes with {COMPANY_NAME} stocks. Brief News feed:\n{get_news_message(daily_list)}")
        print('Message sent!')


if __name__ == '__main__':
    main()

