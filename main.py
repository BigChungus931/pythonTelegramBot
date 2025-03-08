import asyncio
import logging
import sys
import requests
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7885754901:AAFp9ZvVOPSRf1Q1AZLljAgdxR0F2fLnnFA"

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message()
async def ask_ollama (message: Message) -> None:

    try:
        standard_prompt = "standard_prompt: "
        modified_prompt = "answer shortly: "
        modified_prompt_2 = "answer thoughtfully: "
        key = "*"
        key_2 = "="

        print(message.text)
        first_key = message.text[:1]
        print(first_key)

        if first_key == key:
            print(modified_prompt + message.text[1:])

        elif first_key == key_2:
            print(modified_prompt_2 + message.text[1:])

        else:
            print(standard_prompt + message.text)
        print(message.text)
        # instruction = "Please answer shortly: "
        # from_text = message.text.split()
        # print(from_text)
        # word_to_find = "short"
        # for word in from_text:
        #     print(word)
        #     if word == word_to_find:
        #         print("short answer")
        #         prompt = instruction + prompt
        #         print(prompt)
        #         break

        data = {
            "model": "mistral",
            "prompt": message.text,
            "stream": False
        }
        r = requests.post("http://localhost:11434/api/generate", json=data)

        response = r.json()
        response_text = response.get("response", "answer not received")
        print(response_text)
        await message.answer(response_text)

    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
