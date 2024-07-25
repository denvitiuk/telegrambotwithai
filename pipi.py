import os
import openai
from aiogram import Bot, Dispatcher, executor, types
from keep_alive import keep_alive
from dotenv import load_dotenv

load_dotenv()
bot = Bot(token = os.getenv('7237760891:AAFlnviTCBVQ73mvNViWXBNmIAY3YQQhvAc'))
dp = Dispatcher(bot)

openai.api_key = os.getenv('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')

keep_alive()

@dp.message_handler(commands = ['start', 'help'])
async def welcome(message: types.Message):
  await message.reply('Hello! Im GPT chat bot. Ask me something')


@dp.message_handler()
async def gpt(message: types.Message):
  response = openai.Completion.create(
    model="text-davinci-003",
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