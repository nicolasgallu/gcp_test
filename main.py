import requests
from config import WPP_TOKEN,WPP_ID

print(WPP_TOKEN)
print(WPP_ID)

def enviar_mensaje(destino="543517710609",mensaje="hola"):

    url = f"https://graph.facebook.com/v22.0/{WPP_ID}/messages"

    header = {
      "Authorization":f"Bearer {WPP_TOKEN}",
      "Content-Type":"application/json"}

    texto ={
    "messaging_product": "whatsapp", 
    "recipient_type": "individual",
    "to": destino, 
    "type": "text",
       "text": { 
            "preview_url": False,
            "body": mensaje }}
    try:   
      requests.post(url,headers=header,json=texto)
    except:
       None
             

if __name__ == "__main__":
   enviar_mensaje()