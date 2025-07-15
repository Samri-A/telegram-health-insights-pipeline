from logging import getLogger
import os
from telethon.sync import TelegramClient
from telethon.tl.types import MessageMediaPhoto
from telethon.errors import FloodWaitError
from dotenv import load_dotenv
import json



load_dotenv()
logger = getLogger()

class data_extract:
    def __init__(self):
        self.session_name = os.getenv("session_name")
        self.api_id = int(os.getenv("api_id"))
        self.api_hash= os.getenv("api_hash")
        


    async def connect(self):
        self.client = TelegramClient(self.session_name ,  self.api_id , self.api_hash)
        await self.client.start()


    async def scraping_messages( self,chat_name , limit):
        try:
            chat_info = await self.client.get_entity(chat_name)           
            messages = await self.client.get_messages(entity=chat_info ,limit= limit)
            value = ({"message": messages , "Channel_info": chat_info })
            logger.info(f"Scraping messages from {chat_name}")
            msg_result = [ msg.to_dict() for msg in value["message"]]
            outputpath = f"../data/raw/telegram_messages/{chat_name}.json"
            with open ( outputpath , "w" , encoding="utf-8") as file:
                json.dump(msg_result, file, default=str, ensure_ascii=False)
            print(f"Saved messages to: {outputpath}")
        except FloatingPointError as e:
            logger.warning(f"Rate limit hit while scraping {chat_name}. Wait {e.seconds} seconds.")
        except Exception as e:
            logger.exception(f"Error scraping {chat_name}: {str(e)}")

    async def download_images(self , chat_name, limit):
        save_dir=f"../data/raw/images/{chat_name}"
        os.makedirs(save_dir, exist_ok=True)
        chat = await self.client.get_entity(chat_name)
        messages = await self.client.get_messages(chat, limit=limit)
        image_count = 0
        for msg in messages:
            if msg.media and isinstance(msg.media, MessageMediaPhoto):
                file_path = os.path.join(save_dir, f"{chat.username}_{msg.id}.jpg")
                await self.client.download_media(msg, file_path)
                image_count += 1
    
        print( f"{image_count} images downloaded from {chat.username} to {save_dir}/")
    
