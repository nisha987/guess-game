import speech_recognition as sr
sr.__version__

r=sr.Recognizer()

harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source,offset=4, duration=5)

r.recognize_google(audio)

jackhammer=sr.AudioFile('jackhammer.wav')
with jackhammer as source:
    r.adjust_for_ambient_noise(source,duration=0.5)
    audio=r.record(source)
    
r.recognize_google(audio,show_all=True)

