from aiogram.types import ReplyKeyboardMarkup,KeyboardButton, InlineKeyboardMarkup,InlineKeyboardButton




menu5=ReplyKeyboardMarkup(
    keyboard=[
        [
        KeyboardButton(text='Registraciya'),
        KeyboardButton(text='Tovarlar')

        ]
    ]
)



contact=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='contact',request_contact=True)
        ]
    ]
)





sagatlar=InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text='Rolex',callback_data='rolex'),
        InlineKeyboardButton(text='Gucci',callback_data='gucci'),
        InlineKeyboardButton(text='назад',callback_data='nazad')
        ]
    ]
)





rolex=InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text='rolex atomishine',callback_data='r1'),
        InlineKeyboardButton(text='rolex oyster',callback_data='r1'),
        InlineKeyboardButton(text='назад',callback_data='nazad')
        ]
    ]
)




gucci=InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text='gucci clasic',callback_data='g1'),
        InlineKeyboardButton(text='gold gucci',callback_data='g1'),
        InlineKeyboardButton(text='назад',callback_data='nazad')
        ]
    ]
)























