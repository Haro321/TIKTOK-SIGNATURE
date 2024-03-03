import requests

url = 'https://c6ae-89-105-219-164.ngrok-free.app/api'

params = {
    'Params': 'mix_mode=1&username=676767&email=&mobile=&account=&password=67766767&captcha=&ts=1695929414&app_type=normal&app_language=ar&manifest_version_code=2018080102&_rticket=1695929414806&iid=7283960284813117190&channel=samsung_store&language=ar&fp=&device_type=Redmi%20Note%208%20Pro&resolution=1080*2220&openudid=827962c690ff95f8&update_version_code=2018080102&sys_region=EG&os_api=30&is_my_cn=1&timezone_name=Asia/Baghdad&dpi=440&carrier_region=IQ&ac=wifi&device_id=7046078037436450309&mcc_mnc=41805&timezone_offset=10800&os_version=11&version_code=800&carrier_region_v2=418&app_name=musical_ly&version_name=8.0.0&device_brand=Redmi&ssmix=a&build_number=8.0.0&device_platform=android&region=SA&aid=1233&as=a1b60dc1f6b48514e54355&cp=da475d6f61591945e1KkSo&mas=0121a935b1863f736ca57034b570967866acaccc2caca62c8cac1c',
    'Payload': '',
    'Cookie' : ''
}

response = requests.get(url, params=params)
if response.status_code == 200:
    print("Response Content:")
    print(response.text)
else:
    print(response.text)
    print("Error:", response.status_code)