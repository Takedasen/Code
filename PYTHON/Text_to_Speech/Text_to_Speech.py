
from gtts import gTTS
import os

mytextinput = 'Its not going anywhere missy, except in the fucking bin!'\
    'Come on big boy'

language_accent = 'en'

myobj = gTTS(text=mytextinput, lang=language_accent, slow=False)

myobj.save("Big_Boy.wav")

os.system("Big_Boy.wav")