
from gtts import gTTS
import os

mytextinput = "Its not going anywhere missy, except in the fucking bin!"\
"Come on big boy"\
"I'm a man, I'm a he, I dont get into that mentally retarded stuff"
language_accent = 'en'

myobj = gTTS(text=mytextinput, lang=language_accent, slow=False)

myobj.save("Big_Boy_1.wav")

os.system("Big_Boy_1.wav")