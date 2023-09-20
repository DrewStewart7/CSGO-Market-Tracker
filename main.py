import requests,json,colorama,time,traceback
from colorama import Fore, Back, Style
from colorama import init
from websocket import create_connection
import discord
from discord import Webhook, SyncWebhook, Embed
import base64
import time
from collections import defaultdict
import http.cookies
import collections
time_in_seconds = time.time()
init(autoreset=True)
csrf = ""
webhookurl = ""
webhook = SyncWebhook.from_url(webhookurl)
add = "https://skinport.com/api/cart/add"
cart = "https://skinport.com/api/cart"
pmethods = "https://skinport.com/api/checkout/payment-methods"
me = "https://skinport.com/api/data"
config = {}
with open("config.json") as jsonfile:
    config = json.load(jsonfile)
auth = config["auth"]
mindeal = config["mindeal"]
minprice = config["minprice"]
maxprice = config["maxprice"]
clientId = config["clientID"]
clientSecret = config["secret"]
globprof = 0
spend = 0
s = requests.session()


cookiestring = ""
with open('cookiestring.txt', 'r') as f:
    cookiestring = f.read()
s.headers["Cookie"] = cookiestring
#s.headers["Cookie"] = f"i18n=en; _ga=GA1.2.1871016972.{time.time()}; connect.sid=s%3AVvbzEQYYOrkYZ8KE1sE-bHxDZWZk-5fs.qK4G1cLidOHz2Ht8vpeeZyBM3d38qstJX5%2F8JQ2nLMA; cf_clearance=4zopmuet9fY6i9Y4g2AWm2plhcsDrcdN_CSMD4WI0Y4-{time.time()}-0-1-8b5481fb.3e549666.dc55de1b-0.2.{time.time()}; __cf_bm=4erKIh4sXKUc.5WpKUGmpDHBU9sj8h2bnNYpnrtSdxs-1692243718-0-AamxNCz0G81kHPPmgWSWNv20lrQ6ar3lDaL0To26yZo/vikPWcHPphzccTdNa9+0O1bbSJcAW1o0omLL/8VU5ec=; _ga_JQVJ6LN9T1=GS1.2.{time.time()}.9.1.{time.time()}.19.0.0; _uetsid=7da7e8303ca311eea132f5b31d2d1a1b; _uetvid=5c650ac0e22211ed8b735da6e4e0ed13"
#s.cookies["scid"] = auth

""" while True:

    data = {
        "v":"abc2fffc7705ffdeb435",
        "t":str(time_in_seconds)
    }
    csrfreq = s.get(me,params=data)
    csrf = csrfreq.json()["csrf"]

    
    csrfreq = csrfreq.headers

    try:
        csrfcook = str(csrfreq["Set-Cookie"])
        split = csrfcook.split(", ")
        count = 0
        for cook in split:
            try:
                count += 1
                cook = cook.split("; ")[0].split("=")
                #s.cookies[cook[0]] = cook[1]
                
                if count + 1 == len(split):
                    break
            except:
                continue
        break
    except Exception as e:
        print(e) """
#print(f"CSRF token: {csrf}")
import base64
cfbm = ""
clientId = "9c45d62fb05844c59d2b3d15b34999e9"
clientSecret = ""
clientData = f"{clientId}:{clientSecret}"
encodedData = str(base64.b64encode(clientData.encode("utf-8")), "utf-8")
authorizationHeaderString = f"Basic {encodedData}"
#print(authorizationHeaderString)


ws = create_connection('wss://skinport.com/socket.io/?EIO=4&transport=websocket')
    
# Perform the handshake.

ws.send("40")
s.headers["Sec-Ch-Ua"] = '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"'
def buy(price,saleID,s):
    try:
        global cookiestring
        s.headers["Cookie"] = cookiestring
        
        #cookiestring = c
        #s = requests.session()
        data = {
            "v":"abc2fffc7705ffdeb435",
            "t":str(time_in_seconds)
        }
        #csrf = s.get(me,params=data).json()["csrf"]
        #s = requests.session()
        s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        scop = s
        s.headers["authorization"] = authorizationHeaderString
        #s.cookies["scid"] = auth
        #s.cookies["_csrf"] = csrf
        #s.cookies["cf_clearance"] = "yZOsszYe9vywF9aKsZZYBQtg4TCmob36MlzOXW3PJSk"
        #s.headers["__cf_bm"] = "fzkhjFfB344LRw0d3l9wRElVWcTbF7xdm0zmQiTIHPc"
        s.headers["Content-Type"] = "application/x-www-form-urlencoded"
        #s.headers["Content-Length"] = "100"
        s.headers["Origin"] = "https://skinport.com"
        s.headers["Referer"] = "https://skinport.com/market"
        datas = {
            "sales[0][id]":str(saleID),
            "sales[0][price]":str(price),
            "_csrf":"NzwPqnHd-e7WOSRsySz6Tq98Slv7ELaMeSbY"
        }
        print("Adding item to cart")
        addcart = s.post(add,data=datas)
        print(addcart.text)
        if("Set-Cookie" in (addcart.headers)):
            cstring = s.headers["Cookie"]
            cstring = cstring.replace(" ","")
            cdict = defaultdict(list)
            for cookie in cstring.split(";"):
                splitcook = cookie.split("=")
                cval = cookie.replace(splitcook[0]+"=","")
                cdict[splitcook[0]] = cval
            scook = addcart.headers["Set-Cookie"]
            cookie = http.cookies.SimpleCookie()
            cookie.load(scook)
            cntr = 0
            print(cookie.keys())
            for cook in cookie.keys():
                print("Updating cookie:",cook)
                print(cookie[cook].value)
                val = (cookie[cook].value)
                #s.cookies.set(cook,val,domain=".skinport.com")
                cdict[cook] = val
            cdict["_ga_JQVJ6LN9T1"] = f"GS1.2.1692587886.21.0.{time.time()}.60.0.0"
            cookiestring = ""
            for key, value in cdict.items():
                cookiestring += "%s=%s; " % (key, value)
            
        #print(cookiestring)
        #s = scop
        #print(addcart.text)
            with open('cookiestring.txt', 'w') as f:
                f.write(cookiestring)
            s.headers["Cookie"] = cookiestring
            buy(price,saleID,s)
        if(addcart.status_code == 200):
            print("Successfully added item to cart")
            
        #cook = s.headers["Cookie"]
        #s.headers = {}
        s = requests.session()
        s.headers["Cookie"] = cookiestring

        s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"
        #s.headers["Cookie"] = f"i18n=en; _ga=GA1.2.1871016972.{time.time()}; _csrf=6PbavxTvAVUSK-8AiBsqRejU; scid=eyJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiQTE5MktXIn0.xywY-UcVZvQ627funJCZuMsxZA7vuwK4d5QnlL80nHh9CZEyg78cfQ.YQQfE1q0AKjO9n8ZtAA_rw.znRi4AEl7mXGdPjmwwmXAcLbbShFT4ExSCe5fp4DG4bF4myBqa9PTCCxhkhspniSCGPgnbPM42XJH-Ydg-cd2L4zHMFszuQGSnhELY1HrU0GIk6C9hWjc0yv6m45oOsJ7X0JLghVxGYPTSczdvCSuLRsTNJ5zZT9ZxA7aSSYJ0timC6_p6nPZw-Kxh8J6VaElp2fZDvQHzL3j45HYOQKMCw-TNySDjjN9EWGkf4_C9nOsh6IKetj_lGKYYJdd6YJAAdveWDPlZx7LZCVjUeRWwH_7um60apbZ-_tg3KJJ8tP2e3jl9AWKOaQE0ciR4jKb3wnsgzyOSD37Z8pGOkujY-Q6qudCtjzvaKFbCBrK6hvz2RQqqud4b6K3cY4qq4RiONh_DWbjROyRtj6bxm79Jm2uA3Cxwnf-HOkA4IYInIKw2bZEFWiPypdMefDUIOGAR3Cg5qgMdVpJhWWoRmgduuc3kp9oi0cwap_WGfFOXej_tdxKNTiA9zFfiQ4mESK7SA1mqQlc4l2HsQMdRbqra2h4Fjip43qU_92qr0b4nNUcYKOs10PnyJLTP1VGAh35l6cG9ojwwK_nJt9QhEjJqT-tXwgniZ4_fdIOmqON0_fQT3lrvT-mECkAMB647lS3m8ADyYy1bA40Tf3rCIEC5JWoBTX-QNqOZuKMAeLJErKDeB2OhSBxSwCWIdwX7Oz.J5Wqvg92RumLfb5G6yZMzA; connect.sid=s%3AVvbzEQYYOrkYZ8KE1sE-bHxDZWZk-5fs.qK4G1cLidOHz2Ht8vpeeZyBM3d38qstJX5%2F8JQ2nLMA; cf_clearance=4zopmuet9fY6i9Y4g2AWm2plhcsDrcdN_CSMD4WI0Y4-{time.time()}-0-1-8b5481fb.3e549666.dc55de1b-0.2.{time.time()}; __cf_bm=4erKIh4sXKUc.5WpKUGmpDHBU9sj8h2bnNYpnrtSdxs-1692243718-0-AamxNCz0G81kHPPmgWSWNv20lrQ6ar3lDaL0To26yZo/vikPWcHPphzccTdNa9+0O1bbSJcAW1o0omLL/8VU5ec=; _ga_JQVJ6LN9T1=GS1.2.{time.time()}.9.1.{time.time()}.19.0.0; _uetsid=7da7e8303ca311eea132f5b31d2d1a1b; _uetvid=5c650ac0e22211ed8b735da6e4e0ed13"
        s.headers["Referer"] = "https://skinport.com/cart"

        viewcart = s.get(cart)
        if("Set-Cookie" in (viewcart.headers)):
            cstring = s.headers["Cookie"]
            cdict = defaultdict(list)
            cstring = cstring.replace(" ","")
            for cookie in cstring.split(";"):
                splitcook = cookie.split("=")
                cval = cookie.replace(splitcook[0]+"=","")
                cdict[splitcook[0]] = cval
            scook = viewcart.headers["Set-Cookie"]
            cookie = http.cookies.SimpleCookie()
            cookie.load(scook)
            for cook in cookie.keys():
                print("Updating cookie:",cook)
                #print(cookie[cook].value)
                val = (cookie[cook].value)
                #s.cookies.set(cook,val,domain=".skinport.com")
                cdict[cook] = val
            cookiestring = ""
            print(cdict.keys())
            for key, value in cdict.items():
                cookiestring += "%s=%s; " % (key, value)
            
        #print(viewcart.text)
            with open('cookiestring.txt', 'w') as f:
                f.write(cookiestring)
            s.headers["Cookie"] = cookiestring
            buy(price,saleID,s)
        if(str(saleID) in viewcart.text and len(viewcart.json()["result"]["cart"]) == 1):
            print("Only target item in cart")


    except:
        print(Fore.RED,traceback.format_exc())

buy(183787,25039103,s)
buy(183787,25039103,s)
while True:
    try:
        result = ws.recv()
        if result == "2":
            ws.send("3")   
        elif str(result) == '42["steamStatusUpdated","operational"]':
            print(Fore.LIGHTGREEN_EX + "Successfully connected to SKINPORT")
            jstr = '42["saleFeedJoin",{"appid":730,"currency":"USD","locale":"en"}]'
            ws.send(jstr)
        elif ('"saleFeed",{"eventType":"listed"') in result:
            result = result.replace("42", "", 1)
            result = json.loads(result)
            sales = result[1]["sales"]
            btext = ""
            for item in sales:
                print(Fore.WHITE + "Item Found")
                name = item["name"]
                price = item["salePrice"]
                sugprice = item["suggestedPrice"]
                deal = round(1 - item["salePrice"]/item["suggestedPrice"],2)
                if (deal >= mindeal) and price > 100*minprice and price < 100*maxprice:
                    saleId = item["saleId"]
                    profit = round((sugprice * .88 - price)/100,2)
                    if (profit > 0):
                        print(Fore.GREEN + "$" + str(profit))
                        globprof += profit
                        print("Session profit: $",globprof)
                        spend += round(price/100,2)
                        print("Session spend: $" + str(spend))
                    buy(price,saleId,s)
                
    except Exception as e:
        ws = create_connection('wss://skinport.com/socket.io/?EIO=4&transport=websocket')
        ws.send("40")
        print(e)
        
    


