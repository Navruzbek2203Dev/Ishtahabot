from aiogram import Bot,Dispatcher,executor,types
import logging
from googletrans import Translator 
from api import taom_qaytar
logging.basicConfig(level=logging.INFO)

bot=Bot(token="6149698150:AAGAqjPJxZDOh-c-aXKT-_0YMQGjCkydt-c")
dp=Dispatcher(bot)

@dp.message_handler(commands="start")
async def start(mess:types.Message):
    await mess.reply(f"Assalomu alaykum {mess.chat.full_name}. \n Taom hohlaysizmi ? \n/taom ni bosing !!!")

@dp.message_handler(commands="taom")
async def taom(message:types.Message):
    meals=taom_qaytar()
    nomi=meals['strMeal']
    hudud=meals['strArea']
    categoriya=meals['strCategory']
    rasm=meals['strMealThumb']
    video=meals['strYoutube']
    text=f"🍱 {nomi}\n🗺 {hudud} {categoriya} taomi\n🎞Tayyorlanish usuli ⤵️⤵️⤵️"
    tarjimon=Translator()
    textuz=tarjimon.translate(text,dest="uz").text
    await message.answer_photo(photo=rasm,caption=textuz)
    await message.answer(video)

if __name__=="__main__":
    executor.start_polling(dp,skip_updates=False)