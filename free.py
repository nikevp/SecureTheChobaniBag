##########
# Free Chobani Coupons
# Made by @swoosh_supply (twitter)  check out the new site (soleius.com)
##########

import json
import requests
from bs4 import BeautifulSoup as bs

#####################################################################
#Change these values
city = 'New York'
zipcode = '10001'
stateAbr = 'NY'
email = 'test@gmail.com'
numberOfCoupons = 5

#Enter an email you would like to use
#Use proxies if you want to request a bunch
# +aNumber formatting used
#####################################################################
#Dont touch anything below unless you are modifying the code
#####################################################################

ShitToSet = {'zipcode': zipcode, 'city': city, 'stateAbr': stateAbr, 'email':email}


headers = {
	'Host': 'banner2.promotionpod.com',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	'User-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.76 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'origin':'https://banner2.promotionpod.com'
	}


def postReq(email):
    global ShitToSet

    session = requests.Session()
    url = 'https://www.chobani.com/freeyogurt/'
    button = 'https://banner2.promotionpod.com/coupon/banner/802f84a4bdf3845e008b8f80d1468087451beb83/widget_click'
    resp = session.get(button, headers=headers)

    respURL = resp.url
    soup = bs(resp.content, 'html.parser')
    token = soup.find('input', {'name':'csrfmiddlewaretoken'}).get('value')

    params = {
    'csrfmiddlewaretoken': token,
    'banner':'9599',
    'referrer':'https://www.chobani.com/freeyogurt/',
    'custom_text_id':'',
    'gs1_serial':'',
    'source':'',
    'token_key':'',
    'eid':'',
    'nonce':'',
    'email':email,
    'zipcode':ShitToSet['zipcode'],
    'city':ShitToSet['city'],
    'state':ShitToSet['stateAbr']
    }

    response = session.post(respURL, headers=headers, data=params)


    soup = bs(response.content, 'html.parser')
    token = soup.find('input', {'name':'csrfmiddlewaretoken'}).get('value')
    uniq1 = soup.find('input', {'id':'hdnGuid'}).get('value')
    uniq2 = soup.find('input', {'id':'hdnNonce'}).get('value')

    coupon = 'https://banner2.promotionpod.com/coupon/' +uniq1+'/final_image?nonce='+uniq2+'&lang=EN'
    print('Coupon from here: ' + coupon)
    resp = requests.get(coupon, headers=headers)
    with open(email+'.jpeg', 'wb') as f:
        f.write(resp.content)


def main(ShitToSet):
    parts = ShitToSet['email'].split('@')
    part1 = parts[0]
    part2 = parts[1]
    print(parts)
    for x in range(1, numberOfCoupons+1):
        email = part1 + '+' + str(x) + '@' + part2
        postReq(email)
main(ShitToSet)
#
