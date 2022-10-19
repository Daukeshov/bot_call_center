import pyttsx3


def hello():
    s = pyttsx3.init()
    data = "добрый день! Вас беспокоит компания X, мы проводим опрос удовлетворенности нашими услугами." \
           "Подскажите, вам удобно сейчас говорить?"
    s.say(data)
    s.runAndWait()


def hello_repeat():
    s = pyttsx3.init()
    data = "Это компания X  Подскажите, вам удобно сейчас говорить?"
    s.say(data)
    s.runAndWait()


def hello_null():
    s = pyttsx3.init()
    data = "Извините, вас не слышно. Вы могли бы повторить"
    s.say(data)
    s.runAndWait()


def hangup_null1():
    s = pyttsx3.init()
    data = "Вас все равно не слышно, будет лучше если я перезвоню. Всего вам доброго"
    s.say(data)
    s.runAndWait()


def recommend_main():
    s = pyttsx3.init()
    data = "Скажите, а готовы ли вы рекомендовать нашу компанию своим друзьям? " \
           "Оцените, пожалуйста, по шкале от «0» до «10», где «0» - не буду рекомендовать, «10» - обязательно порекомендую"
    s.say(data)
    s.runAndWait()


def hangup_wrong_time():
    s = pyttsx3.init()
    data = "Извините пожалуйста за беспокойство. Всего вам доброго"
    s.say(data)
    s.runAndWait()


def recommend_score_positive():
    s = pyttsx3.init()
    data = "Хорошо,  а по 10-ти бальной шкале как бы вы оценили 8-9 или может 10  ?"
    s.say(data)
    s.runAndWait()

def recommend_score_negative():
    s = pyttsx3.init()
    data = "ХНу а от 0 до 10 как бы вы оценили бы: 0, 5 или может 7 ?"
    s.say(data)
    s.runAndWait()



def hangup_negative():
    s = pyttsx3.init()
    data = "Я вас понял. В любом случае большое спасибо за уделенное время!  Всего вам доброго"
    s.say(data)
    s.runAndWait()

def hangup_positive():
    s = pyttsx3.init()
    data = "Отлично!  Большое спасибо за уделенное время! Всего вам доброго"
    s.say(data)
    s.runAndWait()

