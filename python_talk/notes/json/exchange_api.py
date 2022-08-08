import json
from urllib.request import urlopen


with urlopen("https://open.er-api.com/v6/latest/USD") as response:
    source = response.read()


data = json.loads(source)
print(json.dumps(data, indent=2))
"""
{
  "result": "success",
  "provider": "https://www.exchangerate-api.com",
  "documentation": "https://www.exchangerate-api.com/docs/free",
  "terms_of_use": "https://www.exchangerate-api.com/terms",
  "time_last_update_unix": 1659916951,
  "time_last_update_utc": "Mon, 08 Aug 2022 00:02:31 +0000",
  "time_next_update_unix": 1660003741,
  "time_next_update_utc": "Tue, 09 Aug 2022 00:09:01 +0000",
  "time_eol_unix": 0,
  "base_code": "USD",
  "rates": {
    "USD": 1,
    "AED": 3.67,
    "AFN": 89.9,
    ...

"""

# print the number of currencies returned from the api
currency_count = len(list(data["rates"]))
print(currency_count) # 162

# print the list of countires with currencies over 500 times
for key,value in sorted(data["rates"].items(),key=lambda x: x[1]):
    if value >= 500:
        print(f"{key} : {value}")
"""
SDG : 565.34
SOS : 567.22
XAF : 644.79
XOF : 644.79
SSP : 660.67
CRC : 666.29
CLP : 901.97
MWK : 1031.56
RWF : 1054.62
KRW : 1301.16
IQD : 1456.38
LBP : 1507.5
MMK : 1832.58
CDF : 1992.34
BIF : 2033.77
TZS : 2331.32
SYP : 2516.27
MNT : 3184.32
UGX : 3878.39
KHR : 4091.3
MGA : 4109.61
COP : 4294.2
PYG : 6849.53
GNF : 8634.64
UZS : 10958.36
SLL : 13934.41
IDR : 14872.12
LAK : 17074.89
VND : 23359.04
IRR : 41931.9
"""
