# Speech-Calculator

## Voice-Controlled Calculator

Welcome! This project is a simple, web-based voice-controlled calculator built using Python. It listens to your spoken mathematical expressions (like "What is 10 plus 5 multiplied by 2"), processes the voice input into text using Google's Speech Recognition API, cleans up operator words, and evaluates the final result in real-time using Streamlit.

### Prerequisites
- Python 3.8 or higher installed on your system.
- A working microphone connected to your computer.
- Required Python packages: streamlit, SpeechRecognition, and PyAudio.

### How to Run
1. Install dependencies using pip:
   pip install streamlit SpeechRecognition PyAudio

2. Run the Streamlit application:
   streamlit run calc.py

---

## Speech Calculator - Test Cases

### Basic Tests

1. Long pause / mic cutoff
   - Input: "What is 9929 divided by 98"
   - Expected: 9929/98 = 101.316...
   - Reason: Checks if pause_threshold and dynamic_energy_threshold = False stop the mic from cutting off the 98 at the end.

2. "divided by" vs "by"
   - Input: "15 by 3" and "15 divided by 3"
   - Expected: 15/3 = 5.0
   - Reason: Removing spaces after the loop instead of before it makes sure both phrases work without turning into 15divided/3 or 15//3.

3. Homophones ("to" / "to
