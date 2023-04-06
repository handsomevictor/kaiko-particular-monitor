import requests
import pandas as pd

import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

org = "kaiko"
token =
url = "http://34.78.245.234:8086"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

self.write_api = client.write_api(write_options=SYNCHRONOUS)

def main():
    url = 'https://www.okcoin.com/api/v5/market/trades?instId=BTC-USD'
    data = requests.get(url).json()
    data = pd.DataFrame(data['data'])
    data['ts'] = pd.to_datetime(data['ts'], unit='ms')
    return data.head(10)

def upload_to_influxdb(self, iteration_num):
    data = [
        {
            "measurement": self.measurement_name,
            "tags": {
                "product": self.product_name,
            },
            "fields": self.run(iteration_num)
        }
    ]
    self.write_api.write(self.bucket_name, org="kaiko", record=data)
    print(f'Uploaded to influxdb: latency of {self.product_name} on endpoints: {self.endpoint}')


if __name__ == '__main__':
    print(main())

