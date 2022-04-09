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

    #if message.content.startswith(':Бен'):
      #await voicechannelonnect()
 


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
        await message.channel.send('Хм')      
      if current_number == haha_number:
        await message.channel.send('Хахаха')


    if message.content.startswith(':Поддержка'):
      await message.channel.send('Аккаунт создателя - Idi_Domoy#5486') 
      await message.channel.send('Ссылка на донат - https://www.donationalerts.com/r/idi_domoy')
      await message.channel.send('https://discord.com/api/oauth2/authorize?client_id=838035675228012594&permissions=8&scope=bot')


    if message.content.startswith(':Пинг'):
      await message.channel.send('@everyone')

    if message.content.startswith(':Игровое общение'):
      await message.channel.send(':Монетка - Игра основанная на игре Орёл-Решка!')
      await message.channel.send(':Imp...')
      await message.channel.send(":Бен ...")
      
    if message.content.startswith(':Рулетка'):
      win_number = 1
      current_number = randint(1,6)
      if current_number != win_number:
        await message.channel.send('Ты выйграл!')
      if current_number == win_number:
        await member.kick


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

    if message.content.startswith(':Ded_Inside'):
      await message.channel.send('1000 - 7 = 993 ')
      await message.channel.send('993 - 7 = 986 ')
      await message.channel.send('986 - 7 = 979 ')
      await message.channel.send('979 - 7 = 972 ')
      await message.channel.send('972 - 7 = 965 ')
      await message.channel.send('965 - 7 = 958 ')
      await message.channel.send('958 - 7 = 951 ')
      await message.channel.send('951 - 7 = 944 ')
      await message.channel.send('944 - 7 = 937 ')
      await message.channel.send('937 - 7 = 930 ')
      await message.channel.send('930 - 7 = 923 ')
      await message.channel.send('923 - 7 = 916 ')
      await message.channel.send('916 - 7 = 909 ')
      await message.channel.send('909 - 7 = 902 ')
      await message.channel.send('902 - 7 = 895 ')
      await message.channel.send('895 - 7 = 888 ')
      await message.channel.send('888 - 7 = 881 ')
      await message.channel.send('881 - 7 = 874 ')
      await message.channel.send('874 - 7 = 867 ')
      await message.channel.send('867 - 7 = 860 ')
      await message.channel.send('860 - 7 = 853 ')
      await message.channel.send('853 - 7 = 846 ')
      await message.channel.send('846 - 7 = 839 ')
      await message.channel.send('839 - 7 = 832 ')
      await message.channel.send('832 - 7 = 825 ')
      await message.channel.send('825 - 7 = 818 ')
      await message.channel.send('818 - 7 = 811 ')
      await message.channel.send('811 - 7 = 804 ')
      await message.channel.send('804 - 7 = 797 ')
      await message.channel.send('797 - 7 = 790 ')
      await message.channel.send('790 - 7 = 783 ')
      await message.channel.send('783 - 7 = 776 ')
      await message.channel.send('776 - 7 = 769 ')
      await message.channel.send('769 - 7 = 762 ')
      await message.channel.send('762 - 7 = 755 ')
      await message.channel.send('755 - 7 = 748 ')
      await message.channel.send('748 - 7 = 741 ')
      await message.channel.send('741 - 7 = 734 ')
      await message.channel.send('734 - 7 = 727 ')
      await message.channel.send('727 - 7 = 720 ')
      await message.channel.send('720 - 7 = 713 ')
      await message.channel.send('713 - 7 = 706 ')
      await message.channel.send('706 - 7 = 699 ')
      await message.channel.send('699 - 7 = 692')
      await message.channel.send('92 - 7 = 685 ')
      await message.channel.send('685 - 7 = 678 ')
      await message.channel.send('678 - 7 = 671 ')
      await message.channel.send('671 - 7 = 664 ')
      await message.channel.send('664 - 7 = 657 ')
      await message.channel.send('657 - 7 = 650 ')
      await message.channel.send('650 - 7 = 643 ')
      await message.channel.send('643 - 7 = 636 ')
      await message.channel.send('636 - 7 = 629 ')
      await message.channel.send('629 - 7 = 622 ')
      await message.channel.send('622 - 7 = 615 ')
      await message.channel.send('622 - 7 = 615 ')
      await message.channel.send('622 - 7 = 615 ')
      await message.channel.send('622 - 7 = 615')
      await message.channel.send('615 - 7 = 608 ')
      await message.channel.send('608 - 7 = 601 ')
      await message.channel.send('601 - 7 = 594 ')
      await message.channel.send('594 - 7 = 587 ')
      await message.channel.send('587 - 7 = 580 ')
      await message.channel.send('580 - 7 = 573 ')
      await message.channel.send('573 - 7 = 566 ')
      await message.channel.send('566 - 7 = 559 ')
      await message.channel.send('59 - 7 = 552 ')
      await message.channel.send('552 - 7 = 545 ')
      await message.channel.send('545 - 7 = 538 ')
      await message.channel.send('538 - 7 = 531 ')
      await message.channel.send('531 - 7 = 524 ')
      await message.channel.send('524 - 7 = 517 ')
      await message.channel.send('517 - 7 = 510 ')
      await message.channel.send('510 - 7 = 503 ')
      await message.channel.send('503 - 7 = 496 ')
      await message.channel.send('496 - 7 = 489 ')
      await message.channel.send('489 - 7 = 482 ')
      await message.channel.send('482 - 7 = 475 ')
      await message.channel.send('475 - 7 = 468 ')
      await message.channel.send('468 - 7 = 461 ')
      await message.channel.send('461 - 7 = 454 ')
      await message.channel.send('454 - 7 = 447 ')
      await message.channel.send('447 - 7 = 440 ')
      await message.channel.send('440 - 7 = 433 ')
      await message.channel.send('433 - 7 = 426 ')
      await message.channel.send('426 - 7 = 419 ')
      await message.channel.send('419 - 7 = 412 ')
      await message.channel.send('412 - 7 = 405 ')
      await message.channel.send('405 - 7 = 398 ')
      await message.channel.send('398 - 7 = 391 ')
      await message.channel.send('391 - 7 = 384 ')
      await message.channel.send('384 - 7 = 377 ')
      await message.channel.send('377 - 7 = 370 ')
      await message.channel.send('370 - 7 = 363 ')
      await message.channel.send('363 - 7 = 356 ')
      await message.channel.send('356 - 7 = 349 ')
      await message.channel.send('349 - 7 = 342 ')
      await message.channel.send('342 - 7 = 335 ')
      await message.channel.send('335 - 7 = 328 ')
      await message.channel.send('328 - 7 = 321 ')
      await message.channel.send('321 - 7 = 314 ')
      await message.channel.send('314 - 7 = 307 ')
      await message.channel.send('307 - 7 = 300 ')
      await message.channel.send('300 - 7 = 293 ')
      await message.channel.send('293 - 7 = 286 ')
      await message.channel.send('286 - 7 = 279 ')
      await message.channel.send('279 - 7 = 272 ')
      await message.channel.send('272 - 7 = 265 ')
      await message.channel.send('265 - 7 = 258 ')
      await message.channel.send('258 - 7 = 251 ')
      await message.channel.send('251 - 7 = 244 ')
      await message.channel.send('244 - 7 = 237 ')
      await message.channel.send('237 - 7 = 230 ')
      await message.channel.send('230 - 7 = 223 ')
      await message.channel.send('223 - 7 = 216 ')
      await message.channel.send('216 - 7 = 209 ')
      await message.channel.send('209 - 7 = 202 ')
      await message.channel.send('202 - 7 = 195 ')
      await message.channel.send('195 - 7 = 188 ')
      await message.channel.send('188 - 7 = 181 ')
      await message.channel.send('181 - 7 = 174 ')
      await message.channel.send('174 - 7 = 167 ')
      await message.channel.send('167 - 7 = 160 ')
      await message.channel.send('160 - 7 = 153 ')
      await message.channel.send('153 - 7 = 146 ')
      await message.channel.send('146 - 7 = 139 ')
      await message.channel.send('139 - 7 = 132 ')
      await message.channel.send('132 - 7 = 125 ')
      await message.channel.send('125 - 7 = 118   ') 
      await message.channel.send('118 - 7 = 111 ')
      await message.channel.send('111 - 7 = 104 ')
      await message.channel.send('104 - 7 = 97 ')
      await message.channel.send('97 - 7 = 90 ')
      await message.channel.send('90 - 7 = 83 ')
      await message.channel.send('83 - 7 = 76')
      await message.channel.send('76 - 7 = 69') 
      await message.channel.send('69 - 7 = 62')

                                 
    answer = ':Пинг 10'
    if message.content.startswith(':Пинг 10'):
      for i in range(10):
        await message.channel.send('@everyone')


client.run(os.environ['TOKEN'])