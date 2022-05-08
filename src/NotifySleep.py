import requests
import argparse
import datetime
import pytz
import re

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--webhook', type=str, required=True)

    args = parser.parse_args()
    webhook: str = args.webhook

    localtime = datetime.datetime.now(pytz.timezone('Asia/Shanghai'))
    print(localtime)
    localtimestr = re.findall(r'\d+-\d+-\d+.*\d+:\d+:\d+', str(localtime))
    if (len(localtimestr) == 0):
        print("ERROR: Get time failed!")
        exit()

    content = f'现在是 { localtimestr[0] } (UTC+8)\n华清大学即将熄灯，请群友就寝，祝大家晚安！'

    requests.post(url=webhook, json={
        'msgtype': 'text',
        'text': {
            'content': content
            }
        }
    )
