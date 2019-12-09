import random

from sr_api.http import HTTPClient
from sr_api.image import Image
from sr_api.pokedex import Pokedex
from sr_api.minecraft import Minecraft
from sr_api.lyrics import Lyrics
from sr_api.meme import Meme

class InputError(Exception):
    pass

class Client:

    # SR API BASE PATH
    SR_API_BASE = "https://some-random-api.ml/"

    def __init__(self):
        self._http_client = HTTPClient()

    def srapi_url(self, path):
        return self.SR_API_BASE + path

    async def get_image(self, name=None):
        options = ["cat", "dog"]
        if not name in options and name != None:
            raise InputError(name + " is not a valid option!")

        if name == None:
            response = await self._http_client.get(self.srapi_url("img/" + random.choice(options)))
            url = response.get("link")

        else:
            response = await self._http_client.get(self.srapi_url("img/" + name))
            url = response.get("link")

        return Image(self._http_client, url)
    
    async def get_pokemon(self, name):
        response = await self._http_client.get(self.srapi_url("pokedex?pokemon=" + name))
        return Pokedex(response)
    
    async def get_fact(self, name):
        response = await self._http_client.get(self.srapi_url("facts/" + name))
        fact = response.get("fact")
        
        return fact
    
    async def bot_token(self):
        response = await self._http_client.get(self.srapi_url("bottoken"))
        token = response.get("token")
                                                              
        return token
    
    async def get_gif(self, name):
        options = ["wink", "pat", "hug"]
        if not name in options and name != None:
            raise InputError(name + " is not a valid option!")

        response = await self._http_client.get(self.srapi_url("animu/" + name))
        url = response.get("link")

        return Image(self._http_client, url)
    
    async def chatbot(self, text):
        response = await self._http_client.get(self.srapi_url("chatbot?message=" + text.replace(" ", "+")))
        res = response.get("response")
        
        return res
        
    async def mc_user(self, name):
        response = await self._http_client.get(self.srapi_url("mc?username=" + name))
        
        return Minecraft(response)
    
    async def get_lyrics(self, title):
        response = await self._http_client.get(self.srapi_url("lyrics?title=" + title.replace(" ", "+")))
        
        return Lyrics(response)
    
    async def get_pikachu(self):
        response = await self._http_client.get(self.srapi_url("pikachuimg"))
        pika = response.get("link")
        
        return pika
    
    async def encode_binary(self, text):
        response = await self._http_client.get(self.srapi_url("binary?text=" + text.replace(" ", "+")))
        res = response.get("binary")
        
        return res
    
    async def decode_binary(self, text):
        response = await self._http_client.get(self.srapi_url("binary?decode=" + text.replace(" ", "+")))
        res = response.get("text")
        
        return res
    
    async def encode_base64(self, text):
        response = await self._http_client.get(self.srapi_url("base64?encode=" + text.replace(" ", "+")))
        res = response.get("base64")
        
        return res
    
    async def decode_base64(self, text):
        response = await self._http_client.get(self.srapi_url("base64?decode=" + text.replace(" ", "+")))
        res = response.get("text")
        
        return res
    
    async def get_meme(self):
        response = await self._http_client.get(self.srapi_url("meme"))
        
        return Meme(self._http_client, response)

    async def close(self):
        await self._http_client.close()
