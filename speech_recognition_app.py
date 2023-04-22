#!/usr/bin/env python
# coding: utf-8

# In[15]:


import streamlit as st
import speech_recognition as sr
import threading


# In[16]:


#1.Add a feature to allow the user to select the speech recognition API to use, in addition to Google Speech Recognition. Some possible APIs to consider include Microsoft Azure Speech Services, Amazon Transcribe, and IBM Watson Speech to Text.
#2.Improve the error handling in the transcribe_speech() function to provide more meaningful error messages to the user.

def transcribe_speech(api, language, pause_event):
    # Initialize recognizer class
    r = sr.Recognizer()
    
    # Set the language for speech recognition
    if api == "Google Speech Recognition":
        r.recognize_google.language = language
    elif api == "Microsoft Azure Speech Services":
        # code for Microsoft Azure Speech Services
        pass
    elif api == "Amazon Transcribe":
        # code for Amazon Transcribe
        pass
    elif api == "IBM Watson Speech to Text":
        # code for IBM Watson Speech to Text
        pass
    else:
        raise ValueError("Invalid API selection")
    
    # Reading Microphone as source
    with sr.Microphone() as source:
        st.info("Speak now...")
        
        # listen for speech and store in audio_text variable
        audio_text = None
        while True:
            if pause_event.is_set():
                st.warning("Paused")
                continue
            st.info("Transcribing...")
            audio_text = r.listen(source)
            break

        try:
            # using the selected speech recognition API
            if api == "Google Speech Recognition":
                text = r.recognize_google(audio_text)
            elif api == "Microsoft Azure Speech Services":
                # code for Microsoft Azure Speech Services
                pass
            elif api == "Amazon Transcribe":
                # code for Amazon Transcribe
                pass
            elif api == "IBM Watson Speech to Text":
                # code for IBM Watson Speech to Text
                pass
            else:
                raise ValueError("Invalid API selection")
            return text
        except sr.UnknownValueError:
            return "Sorry, I did not understand what you said."
        except sr.RequestError:
            return "Sorry, the speech recognition service is currently unavailable."
        except ValueError as e:
            return str(e)



# In[17]:


#3.Add a feature to allow the user to save the transcribed text to a file
#4.Add a feature to allow the user to choose the language they are speaking in, and configure the speech recognition API to use that language.

def main():
    st.title("Speech Recognition App")
    
    # select the speech recognition API to use
    api = st.selectbox("Select a speech recognition API", ["Google Speech Recognition", "Microsoft Azure Speech Services", "Amazon Transcribe", "IBM Watson Speech to Text"])
    
    # select the language to use for speech recognition
    language = st.selectbox("Select your language", ["en-US", "fr-FR", "es-ES", "de-DE"])
    
    st.write("Click on the microphone to start speaking:")
    
    pause_event = st.session_state.pause_event if 'pause_event' in st.session_state else threading.Event()

    # add a button to trigger speech recognition
    if st.button("Start Recording"):
        text = transcribe_speech(api, language, pause_event)
        st.write("Transcription: ", text)
        
        # add a checkbox to allow user to save the transcription to a file
        if st.checkbox("Save transcription to file"):
            filename = st.text_input("Enter a filename for the transcription", "transcription.txt")
            with open(filename, "w") as f:
                f.write(text)
            st.write("Transcription saved to file: ", filename)

    # add buttons to pause and resume speech recognition
    if st.button("Pause"):
        pause_event.set()
    if st.button("Resume"):
        pause_event.clear()

if __name__ == "__main__":
    main()
    


# In[ ]:




