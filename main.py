import requests
import vosk
import cv2
import json
import pyaudio

model = vosk.Model('vosk-model-ru-0.22')
model = vosk.KaldiRecognizer(model, 16000)
audio = pyaudio.PyAudio()
recording = audio.open(
    input=True
)
recording.start_stream()
data = []


def listen():
    while True:
        data = recording.read(4000, exception_on_overflow=False)
        if model.AcceptWaveform(data) and len(data) > 0:
            answer = json.loads(model.Result())
            if answer['text']:
                yield answer['text']


def save_image():
    value = requests.get('https://dog.ceo/api/breeds/image/random').json()['message']
    out = open('img.jpg', 'wb')
    out.write(requests.get(value).content)
    out.close()
    print('Psina tut')


def get_dog_image():
    value = requests.get('https://dog.ceo/api/breeds/image/random').json()['message']
    out = open('img.jpg', 'wb')
    out.write(requests.get(value).content)
    out.close()
    print('psina tut')
    image = cv2.imread('img.jpg')
    cv2.imshow('psina', image)
    cv2.waitKey(1)
    cv2.destroyAllWindows()


def name():
    value = requests.get('https://dog.ceo/api/breeds/image/random').json()['message']
    result = value.split('/')[-2]
    print('Poroda psini:', result)


def get_image_resolution():
    width, height, _ = cv2.imread('img.jpg').shape
    print(width, 'x', height)


def get_breed_description():
    results = requests.get("https://en.wikipedia.org/wiki/List_of_dog_breeds").text.split('\n')
    for line in results:
        if "<a href=\"/wiki/" in line:
            res = line.split("/wiki/")[1].split("\"")[0].replace("_", " ")
            print(res, end=', ')


for text in listen():
    text = text.lower()
    if 'показать' in text:
        get_dog_image()
    elif 'описание' in text:
        get_breed_description()
    elif 'разрешение' in text:
        get_image_resolution()
    elif 'сохранить' in text:
        save_image()
    elif 'назвать породу' in text:
        name()
    elif 'выход' in text:
        break
    else:
        print('vrun')


def listen():
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if record.AcceptWaveform(data) and len(data) > 0:
            answer = json.loads(record.Result())
            if answer['text']:
                yield answer['text']


def speak(say):
    tts.say(say)
    tts.runAndWait()


speak('starting')
print('start...')
for text in listen():
    if text == 'закрыть':
        quit()
    elif text == 'блокнот':
        os.system('notepad.exe')
    else:
        print(text)
