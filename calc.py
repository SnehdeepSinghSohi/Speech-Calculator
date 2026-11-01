import streamlit as st
import speech_recognition as sr
if st.button("🎤 Speak"):
    r = sr.Recognizer()                      #   Hire the "Translator" (turns sound waves into text)
    r.dynamic_energy_threshold = False       #   Stops the mic from raising the volume bar mid-sentence and ignoring your softer voice at the end!
    r.energy_threshold = 150                 #   Sets a gentle, fixed sensitivity so even a quiet "98" at the end is heard clearly.
    r.pause_threshold = 1.5                  #   to not let the last word cut off
    r.non_speaking_duration = 1.0            #   By default, it cuts off 0.5 seconds before a pause.which slices off short/soft words right before silence!
    with sr.Microphone() as source:          #   Turn on your physical mic (uses PyAudio secretly!)
        st.info("Listening... speak!")       #   (Show a friendly message on the webpage)
        audio = r.listen(source)             #   Record your voice until you stop talking
        st.audio(audio.get_wav_data())       # Puts a mini audio player on your webpage!
    command = r.recognize_google(audio)      #   Send the recording to Google and get a text string back!
    if command == '' :
        st.warning("Please input again");
    lower=command.lower();
    lower=lower.replace("what is","");
    lower=lower.strip();
    OPERATOR_MAP = {
    "divided by": "/",
    "multiplied by": "*",
    "upon": "/",
    "by": "/",
    " to ": "2",
    " too ": "2",
    "into": "*",
    "times": "*",
    "plus": "+",
    "minus": "-",
    "x": "*",
    "÷": "/",
    "point": ".",
    "zero" : "0",
    "thousand": "000",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",

    }
    for phrase, symbol in OPERATOR_MAP.items():
     lower = lower.replace(phrase, f"{symbol}")
    lower = lower.replace(" ", "")
    lower = lower.replace(",", "")
    st.write("🎤 Google heard:", command, " | 🧮 Math:", lower)

    try:
            result = eval(lower)
            st.success(f"Answer: {result}")
    except ZeroDivisionError:
            st.warning("🚫 Can't divide a number by 0!")
    except SyntaxError:
            st.error(f"⚠️ Incomplete math (`{lower}`). Please try speaking again!")

