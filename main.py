from phrase import hello, hello_null, hello_repeat, recommend_score_positive, \
    recommend_main, hangup_wrong_time, hangup_negative, hangup_positive, recommend_score_negative
import speech_recognition as sr
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(2, 3))
classifier_probability = LogisticRegression()
classifier = LinearSVC()


hello()


def record_volume():
    r = sr.Recognizer()
    with sr.Microphone(device_index = 1) as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print('Говорите...')
        audio = r.record(source, duration=4)
    try:
        query = r.recognize_google(audio, language = 'ru-RU')
        global request
        request = query.lower()
    except sr.UnknownValueError:
        hello_null()
record_volume()


hello_logic = {
    "intents": {
        "Да": {
            "examples": ["да", "конечно", "вполне",
                         "абсолютно", "удобно"],
        },
        "Нет": {
            "examples": ["нет", "неудобно", "занят", "не совсем",
                         "позже", "перезвонить"],
        },
        "Еще раз": {
            "examples": ["повторить",
                         "еще раз", "плохо слышно"],
        },
        "Null": {
            "examples": [" ",
                         " ", ""],
        },
    },
}

main_logic = {
    "intents": {
        "0-8": {
            "examples": ["0", "1", "2", "3", "4", "5", "6", "7", "8"],
        },
        "9-10": {
            "examples": ["9", "10"],
        },
        "Нет": {
            "examples": ["нет",
                         "ни в коем случае", "никогда"],
        },
        "Да": {
            "examples": ["да", "конечно", "с радостью",
                         "вполне", "готов"],
        },
        "Null": {
            "examples": [" ",
                         " ", ""],
        },
    },
}


def prepare_corpus1():
    corpus = []
    target_vector = []
    for intent_name, intent_data in hello_logic["intents"].items():
        for example in intent_data["examples"]:
            corpus.append(example)
            target_vector.append(intent_name)

    training_vector = vectorizer.fit_transform(corpus)
    classifier_probability.fit(training_vector, target_vector)
    classifier.fit(training_vector, target_vector)

prepare_corpus1()

def get_intent1():
    global best_intent
    best_intent = classifier.predict(vectorizer.transform([request]))[0]

    index_of_best_intent = list(classifier_probability.classes_).index(best_intent)
    probabilities = classifier_probability.predict_proba(vectorizer.transform([request]))[0]

    best_intent_probability = probabilities[index_of_best_intent]

    if best_intent_probability > 0.57:
        return best_intent

get_intent1()


if best_intent == 'Нет':
    hangup_wrong_time()
elif best_intent == 'Еще раз':
    hello_repeat()

elif best_intent == 'Да':
    recommend_main()

    def record_volume1():
        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            print('Говорите...')
            audio = r.record(source, duration=4)
        try:
            query = r.recognize_google(audio, language='ru-RU')
            global request1
            request1 = query.lower()
        except sr.UnknownValueError:
            hello_null()

    record_volume1()


    def prepare_corpus2():
        corpus1 = []
        target_vector1 = []
        for intent_name, intent_data in main_logic["intents"].items():
            for example in intent_data["examples"]:
                corpus1.append(example)
                target_vector1.append(intent_name)

    prepare_corpus2()

    def get_intent2():
        global best_intent1
        best_intent1 = classifier.predict(vectorizer.transform([request1]))[0]
        index_of_best_intent1 = list(classifier_probability.classes_).index(best_intent1)
        probabilities = classifier_probability.predict_proba(vectorizer.transform([request1]))[0]
        best_intent_probability1 = probabilities[index_of_best_intent1]
        # при добавлении новых намерений стоит уменьшать этот показатель
        if best_intent_probability1 > 0.4:
            return best_intent1

    get_intent2()


    if best_intent1 == '0-8':
        hangup_negative()
    elif best_intent1 == '9-10':
        hangup_positive()
    elif best_intent1 == 'Да':
        recommend_score_positive()
    elif best_intent1 == 'Нет':
        recommend_score_negative()

