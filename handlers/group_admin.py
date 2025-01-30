from aiogram import types, Router, F

admin_router = Router()

bad_words = {"изгой", "мал", "негр"}


@admin_router.message(F.text, lambda message: any(word in message.text.lower() for word in bad_words))
async def filter_bad_words(message: types.Message, bot):
    await message.delete()
    await bot.ban_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    await message.answer(f"Пользователь {message.from_user.first_name}"
                         f" был забанен за нарушение правил!")
