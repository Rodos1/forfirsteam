from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import KeyboardButton, ReplyKeyboardRemove
import asyncio
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart, StateFilter

TOKEN = "6889363787:AAHbQFXvuQFvKX50p1PQ1od5S6541pT2elo"

bot = Bot(token=TOKEN)
disp = Dispatcher()

class OPROS(StatesGroup):
    quest1 = State()
    quest2 = State()
    quest3 = State()
    quest4 = State()

@disp.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    await message.answer("Добро пожаловать в ДебатБот!")
    await message.answer("Теперь раскажите нам о себе:")
    a = message.chat.id
    await message.answer(f" ваш айди: {a}")
    await state.set_state(OPROS.quest1)
    await message.answer("Ваше имя: ")
    



#фамилия
@disp.message(StateFilter(OPROS.quest1))
async def answer_quest1(message: types.Message, state: FSMContext):
    answer1 = message.text
    await state.update_data(answer1=answer1)
    await state.set_state(OPROS.quest2)
    await message.answer("Ваша фамилия:")
 #опыт в дебатах
@disp.message(StateFilter(OPROS.quest2))
async def answer_quest1(message: types.Message, state: FSMContext):
    answer2 = message.text
    await state.update_data(answer2=answer2)
    await state.set_state(OPROS.quest3)
    await message.answer("Был ли у вас опыт в дебатах, если да, то какой:")

@disp.message(StateFilter(OPROS.quest3))
async def answer_quest1(message: types.Message, state: FSMContext):
    answer3 = message.text
    await state.update_data(answer3=answer3)

    data = await state.get_data()
    answers = f"Ваши данные:\nИмя: {data['answer1']}\nФамилия: {data['answer2']}\nОпыт в дебатах: {data['answer3']}"

    await message.answer(answers)
    await state.clear()
   

# @disp.message(Command("ave_maria"))
# async def cmd_start(message: types.Message):
#     await message.answer("deus vult!")

async def main():
    await disp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())