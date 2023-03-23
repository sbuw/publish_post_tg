import logging

logging.basicConfig(level=logging.INFO)

from pyrogram import Client, filters
from pyrogram.types import Message

m_api_id = 12345 # my.telegram.org/
m_api_hash = "1234dsfgdff5" # my.telegram.org/

m_sender_chat_id = 12345 # Where from
m_chat_id = 12345 # Where

app = Client("bot", m_api_id, m_api_hash)

@app.on_message(filters.reply & filters.command("post") & filters.chat(m_sender_chat_id))
async def post(app, msg: Message):
	await app.copy_message(m_chat_id, msg.chat.id, msg.reply_to_message_id)
	await msg.reply("Post has been sent")

app.run()