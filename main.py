import discord
import os
from random import randint
from time import sleep

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return













    if message.content.startswith(':Привет'):
        await message.channel.send('qq')
        await message.channel.send('Меня зовут Home_Bot, я создан для развлечения и общения! Я надеюсь я смогу помочь твоему серверу!')
        await message.channel.send('Прописав команду :Help я тебе покажу мои функции!')
        await message.channel.send('Что бы попрощаться напиши :Пока')



    if message.content.startswith(':Монетка'):
      win_number = 1
      current_number = randint(1, 4)
      if current_number == win_number:
        await message.channel.send('Опа! Ты выйграл, поздравляю!')
      else:
        await message.channel.send('Ты проиграл, сорян!')

    

    if message.content.startswith(':Help'):
      await message.channel.send('Мои категории:')
      await message.channel.send(':Игровое общение')
      await message.channel.send(':Поддержка')

    if message.content.startswith(':Бен'):
      await voicechannelonnect()
 


     if message.content.startswith(':Бен'):
      yes_number = 1
      no_number = 2
      hm_number = 3
      haha_number = 4
      current_number = randint(1, 4)
      if current_number == yes_number:
        await message.channel.send('Да')
      if current_number == no_number:
        await message.channel.send('Нет')
      if current_number == hm_number:
        await message.channel.send('Хм')       if current_number == haha_number:
        await message.channel.send('Хахаха')


     if message.content.startswith(':Поддержка'):
      await message.channel.send('Аккаунт создателя - Idi_Domoy#5486') 
      await message.channel.send('Ссылка на донат - https://www.donationalerts.com/r/idi_domoy')
      await message.channel.send('https://discord.com/api/oauth2/authorize?client_id=838035675228012594&permissions=8&scope=bot')


    if message.content.startswith(':Пинг'):
      await message.channel.send('@everyone')

    if message.content.startswith(':Игровое общение'):
      await message.channel.send(':Монетка - Игра основанная на игре Орёл-Решка!')
      await message.channel.send(':Imp - вы задаёте бота вопрос не предатель ли ...')



    if message.content.startswith(':Imp'):
      win_number = 1
      current_number = randint(1, 2)
      if current_number == win_number:
        await message.channel.send('Да!')
      else:
        await message.channel.send('Нет!')

    if message.content.startswith('@Home_Bot'):
      await message.channel.send('Иди нахуй!')


    if message.content.startswith(':Пока'):
      await message.channel.send('Пока!')


    if message.content.startswith(':Turn on crash'):
      await message.channel.send('ОК')
      await message.channel.send('Краш режим запущен')

    answer = ':Пинг 10'
    if message.content.startswith(':Пинг 10'):
      for i in range(10):
        await message.channel.send('@everyone')


client.run(os.environ['TOKEN'])