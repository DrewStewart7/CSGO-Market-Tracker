import requests,json,colorama,time
from colorama import Fore, Back, Style
from colorama import init
from websocket import create_connection
import discord
from discord import Webhook, SyncWebhook, Embed
init()
webhookurl = ""
pwebhookurl = ""
webhook = SyncWebhook.from_url(webhookurl)
pwebhook = SyncWebhook.from_url(pwebhookurl)


# Launch the connection to the server.



ws = create_connection('wss://skinport.com/socket.io/?EIO=4&transport=websocket')
    
# Perform the handshake.

ws.send("40")




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
                btext = ""
                name = item["name"]
                price = item["salePrice"]
                sugprice = item["suggestedPrice"]
                profit = round((sugprice * .88 - price)/100,2)
                deal = round(1 - item["salePrice"]/item["suggestedPrice"],2)
                url = "https://skinport.com/item/" + item["url"] + "/" + str(item["saleId"])
                text = f"Item name: {name}\nPrice: ${round(price/100,2)}\nSuggested price: ${round(sugprice/100,2)}\nDeal %: {deal * 100}\nProfit: ${profit}\nUrl: {url}\n\n"
                if (deal >= .25 and (round(sugprice/100,2) >= 10)):
                    btext = text
                    classid = item["classid"]
                    embed = discord.Embed(title="DEAL FOUND",description=":telescope:",color=5763719)
                    embed.set_image(url = f"https://community.cloudflare.steamstatic.com/economy/image/class/730/{classid}/256x128")
                    embed.add_field(name="Listing information:",value=text)
                    try:
                        pwebhook.send(embed=embed)
                        print("Sent webhook")
                        dataz = {
                            "content":"<@&1083232035205820516>"
                        }
                        sendping = requests.post(pwebhookurl,json=dataz)     
                    except:
                        print("Webhook error")
                elif (deal >= .25):
                    print(Fore.GREEN+text)
                    if (round(sugprice/100,2) >= 10):
                        btext = text
                        classid = item["classid"]
                        embed = discord.Embed(title="DEAL FOUND",description=":telescope:",color=5763719)
                        embed.set_image(url = f"https://community.cloudflare.steamstatic.com/economy/image/class/730/{classid}/256x128")
                        embed.add_field(name="Listing information:",value=text)
                        try:
                            webhook.send(embed=embed)
                            print("Sent webhook")
                        except:
                            print("Webhook error")
                elif(deal >= .2):
                    print(Fore.LIGHTGREEN_EX+text)
                elif(deal >= 0):
                    print(Fore.YELLOW+text)
                else:
                    print(Fore.LIGHTRED_EX+text)
        
    except Exception as e:
        ws = create_connection('wss://skinport.com/socket.io/?EIO=4&transport=websocket')
        ws.send("40")
        print(e)
        
    


