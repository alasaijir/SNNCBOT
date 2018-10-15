import vk_api, random, sys, datetime
from vk_api.longpoll import VkLongPoll, VkEventType

def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True

    return key, remember_device

def main():
    bad_words = [
        'Пидор', 'Ты пидор', 'Ти пидор',
        'Пэдро', 'Ты пэдро', 'Ти пэдро',
        'Пыдар', 'Ты пыдар', 'Ти пыдар',
        'Пидр', 'Ты пидр', 'Ти пидр',
        'Пизда', 'Ты пизда', 'Ти пизда',
        'Пидорас', 'Ты пидорас', 'Ти пидорас',
        'Тварь', 'Ты тварь', 'Ти тварь',
        'Говно', 'Ты говно', 'Ти говно',
        'Сука', 'Ты сука', 'Ти сука',
        'Член','Ты член', 'Ти член',
        'Даун', 'Ты даун', 'Ти даун',
        'Аутист', 'Ты аутист', 'Ти аутист',
        'Долбаеб', 'Ты долбаеб', 'Ти долбаеб',
        'Долбаёб', 'Ты долбаёб', 'Ти долбаёб',
        'Долбоеб', 'Ты долбоеб', 'Ти долбоеб',
        'Долбоёб', 'Ты долбоёб', 'Ти долбоёб',
        'Говноед', 'Ты говноед', 'Ти говноед',
        'Блядь', 'Ты блядь', 'Ти блядь', 'Бля',
        'Блять', 'Ты блять', 'Ти блять',
        'Пошел нахуй', 'Пошел ты нахуй', 'Иди нахуй', 'Иди на хуй', 'Пошел на хуй',
        'Хуй', 'Ты хуй', 'Ти хуй',
        'Иди в пизду', 'Пошел в пизду', 'В пизду',
        'Ебать', 'Ебал', 'Ебаный', 'Ебанный', 'Ебал в рот', 'Ебаный рот', 'Ебанный рот',
        'Ублюдок мать твою',
        'Гей', 'Ты гей', 'Ти гей',
        'Чмо', 'Ты чмо', 'Ти чмо',
        'Чьмо', 'Ты чьмо', 'Ти чьмо',
        'Лох', 'Ты лох', 'Ти лох',
    ]

    SHS = [
        'Саня хуй соси','Хуй саня соси', 'Соси хуй саня', 'Бот, скинь дз',
        'Схс', 'Cхс', 'Cxс', 'Cxc', 'Сxс', 'Cxс', 'Сxc'
    ]

    rhythm ={
        'Да': 'Борода',
        'да': 'Борода',
        'ДА': 'Борода',
    }

    commands = {
        '!Пидор': 'chooseOneGay()',
        '!пидор': 'chooseOneGay()',
        '!ПИДОР': 'chooseOneGay()',
        '!ролл': 'getRandomNumber()',
        '!Ролл': 'getRandomNumber()',
        '!РОЛЛ': 'getRandomNumber()',

    }


    login, password = 'x', 'x'
    vk_session = vk_api.VkApi(login, password, auth_handler=auth_handler)

    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    longpoll = VkLongPoll(vk_session)


    for event in longpoll.listen():
        print('New event', event.type)

        if event.type == VkEventType.MESSAGE_NEW:
            print('Новое сообщение:')

            if event.from_me:
                print('От меня для: ', end = '')
            elif event.to_me:
                print('Для меня от: ', end = '')

            if event.from_user:
                print(event.user_id)
            elif event.from_chat:
                print(event.user_id, 'в беседе', event.chat_id)
            elif event.from_group:
                print('группы', event.group_id)

            print('Текст: ', event.text)
            print()

            messageText = str(event.text)


            def chooseOneGay():
                dict_members = vk_session.get_api().messages.getConversationMembers(peer_id=2000000072, fields='id')
                a1 = []
                a2 = []
                a3 = []
                for mass in dict_members['profiles']:
                    var1 = mass.get('id')
                    a1.append(var1)
                    var2 = mass.get('first_name')
                    a2.append(var2)
                    var3 = mass.get('last_name')
                    a3.append(var3)
                print(a1)
                print(a2)
                print(a3)
                lenghtA1 = len(a1)
                randomGay = random.randint(0, lenghtA1-1)
                randomGayName = a2[randomGay]
                randomGayLastName = a3[randomGay]
                return randomGayName, randomGayLastName

            def getRandomNumber():
                randomNumber = random.randint(0, 100)
                return randomNumber


            def checBadWord():
                for i1 in bad_words:
                    if messageText == i1.lower() or messageText == i1.upper() or messageText == i1:
                        return True
            def checkSHS():
                for i2 in SHS:
                    if messageText == i2.lower() or messageText == i2.upper() or messageText == i2:
                        return True

            def chechRhythm():
                for i3 in rhythm:
                    if messageText == i3.lower() or messageText == i3.upper() or messageText == i3:
                        return True

            def checkCommands():
                for i4 in commands:
                    if messageText == i4.lower() or messageText == i4.upper() or messageText == i4:
                        return True


            if checBadWord() == True:
                if event.from_user:
                    vk_session.get_api().messages.send(user_id=int(event.user_id), message='Сам ' +str(event.text).lower()+ '\n'+'[ BOT // ' + ' ' +datetime.datetime.today().strftime("%Y-%m-%d; %H.%M.%S") +' ]')
                elif event.from_chat:
                    vk_session.get_api().messages.send(chat_id=int(event.chat_id), message='Сам ' + str(event.text).lower()+ '\n'+'[ BOT // ' + ' ' +datetime.datetime.today().strftime("%Y-%m-%d; %H.%M.%S") +' ]' )
            elif checkSHS() == True:
                if event.from_chat:
                    vk_session.get_api().messages.removeChatUser(chat_id=int(event.chat_id),user_id=int(event.user_id))
            elif chechRhythm() == True:
                if event.from_chat:
                    vk_session.get_api().messages.send(chat_id=int(event.chat_id), message=str(rhythm.get(messageText))+'\n'+'[ BOT // ' + ' ' +datetime.datetime.today().strftime("%Y-%m-%d; %H.%M.%S") +' ]')
            elif checkCommands() == True:
                if event.from_chat:
                    commandId = commands.get(messageText)
                    if commandId == 'chooseOneGay()':
                        gayName, gaySurename = chooseOneGay()
                        vk_session.get_api().messages.send(chat_id=int(event.chat_id), message='Я думаю, что пидор: \n' + str(gayName) + ' ' + str(gaySurename) +'\n'+'[ BOT // ' + ' ' +datetime.datetime.today().strftime("%Y-%m-%d; %H.%M.%S") +' ]')
                    elif commandId == 'getRandomNumber()':
                        randomNumber = getRandomNumber()
                        vk_session.get_api().messages.send(chat_id=int(event.chat_id),message=str(randomNumber)+'\n'+'[ BOT // ' + ' ' +datetime.datetime.today().strftime("%Y-%m-%d; %H.%M.%S") +' ]')



if __name__ == '__main__':
    main()  #А зачем мейн в конце? #чтобы ты спросил
    
