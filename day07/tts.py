# file : Thread
# desc : Text TO Speech

# pip install gTTS

from gtts import gTTS
import pygame

text = input('소리로 바꿀 텍스트 입력')

speech = gTTS(text=text, lang='ko')
speech.save('./day07/tts.mp3')


