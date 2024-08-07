import openai
import json
from aiogram import Bot, Dispatcher, executor, types


def load_api_key(secrets_file="secrets.json"):
  with open(secrets_file) as f:
    secrets = json.load(f)
  return secrets["OPENAI_API_KEY"]

api_key = load_api_key()
openai.api_key = api_key
"""from keep_alive import keep_alive"""
TOKEN = 'token'
bot = Bot(token = TOKEN)
dp = Dispatcher(bot)





@dp.message_handler(commands = ['start', 'help'])
async def welcome(message: types.Message):
  await message.reply('Hello! Im GPT chat bot. Ask me something')


@dp.message_handler()
async def gpt(message: types.Message):
  response = openai.Completion.create(
    model="gpt-3.5-turbo-instruct",
    prompt=message.text,
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.0
  )
  await message.reply(response.choices[0].text)


if __name__ == "__main__":
  executor.start_polling(dp)