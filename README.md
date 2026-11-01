<img width="1013" height="437" alt="image" src="https://github.com/user-attachments/assets/4716ae6c-fe04-4a28-ab9b-6a6d5c167a5a" />
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

3. Homophones ("to" / "too")
   - Input: "10 multiplied by 2"
   - Expected: `10*2` = 20
   - Reason: Google sometimes hears "to" or "too" instead of "2", so this checks if the dictionary replaces them properly.

4. Divide by zero
   - Input: "50 divided by 0"
   - Expected: 50/0 = Warning message ("Can't divide a number by 0!")
   - Reason: Uses except ZeroDivisionError: so the page shows a warning instead of crashing.

### BODMAS & Decimals

5. BODMAS (3+ numbers)
   - Input: "What is 10 plus 5 multiplied by 2"
   - Expected: `10+5*2` = 20
   - Reason: Makes sure eval() follows order of operations (multiplies first to get 20, not 30).

6. Decimals
   - Input: "5 point 5 plus 2 point 25"
   - Expected: 5.5+2.25 = 7.75
   - Reason: Checks if "point": "." in OPERATOR_MAP handles decimal numbers properly.

7. Negative numbers
   - Input: "12 minus 25"
   - Expected: 12-25 = -13
   - Reason: Basic check for negative results.

### Edge Cases & Bugs Fixed

8. Dividing by a decimal starting with 0 (0.5)
   - Input: "100 divided by 0.5"
   - Expected: 100/0.5 = 200.0
   - Reason: 100/0.5 has "/0" inside /0.5, which broke the old if "/0" in lower: check. Switched to except ZeroDivisionError: to fix this.

9. Google spelling out "zero"
   - Input: "10 divided by zero"
   - Expected: 10/0 = Warning message ("Can't divide a number by 0!")
   - Reason: Sometimes Google writes the word "zero" instead of "0", which gave NameError: name 'zero' is not defined. Fixed by adding "zero": "0" to OPERATOR_MAP.

10. Numbers in the thousands (commas)
    - Input: "1,000 plus 2,000"
    - Expected: 1000+2000 = 3000
    - Reason: Google adds commas to numbers 1,000 and above, and eval() treats commas as a tuple (1, 2000, 0). Fixed with lower.replace(",", "").


11. The "2000" bug
    - Input: "6 divided by 2000"
    - Expected: 6/2000 = 0.003
    - Reason: Worked fine for 3000+, but failed on 2000 because Google got confused by "to"/"too"/"two" and wrote "two thousand" as words. Fixed by adding "two": "2" and "thousand": "000" to OPERATOR_MAP.

---

## What I Plan to Add Next
- [ ] Better UI styling and buttons in Streamlit
- [ ] Calculation history on the page so you can see previous answers
- [ ] Scientific calculator capabilities
- [ ] Voice output (Text-to-Speech) so the calculator speaks the answer back
