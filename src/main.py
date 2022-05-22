import asyncio

import config as cfg

from flask import Flask, jsonify, request
from aiogram import Bot

app = Flask(__name__)
bot = Bot(token=cfg.TELEGRAM_TOKEN)


@app.route("/send-to-telegram", methods=["POST"])
def send_in_tg_chat():
    json = request.get_json()

    name = json.get('name', 'no data')
    description = json.get('description', 'no data')
    price = json.get('price', 'no data')
    city = json.get('city', 'no data')
    tags = ', '.join(json.get('tags', ['no data']))

    asyncio.run(bot.send_message(
        cfg.CHAT_ID,
        cfg.SAMPLE_TEXT.format(name=name, tags=tags, description=description, price=price, city=city),
        parse_mode='html'
    ))
    return jsonify({'status': 'ok'}), 200


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
