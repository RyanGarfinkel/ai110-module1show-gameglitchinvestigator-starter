# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - When I first ran the app, I was able to see the settings on the sidepanel and was able to type in the guess box, press submit, and see the go lower message.
- List at least two concrete bugs you noticed at the start  
  - When I submitted a guess, the go lower and go higher messages were reversed.
  - When typing a number in the guess box, a message said to press enter to apply, but it didn't. I had to press the submit button.
  - The history in the developer debug info collapsable did not immediately update with my latest guess.
  - The history in the developer debug info collapsable did not clear when I pressed new game. Attempts field did reset.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - I used the Gemini 3.1 Pro Preview modek using GitHub Copiolot and Claude Code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - Claude Code was able to fix the Go Higher/Lower text when the user guessed correctly without any additional propmpts or manual fixes.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - When updating the code to clear the history when the game resets, Claude modified the UI to have the developer debug info collapsable at the bottom despite my instruction to not modify the UI.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I first reviewed the proposed changes, if I agreed and didn't have questions I accepted the changes. Then I refreshed the UI and tested the updated code, making sure it behavied as expected.
- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
  - In addition to the pytests, I would guess lower and higher numbers to make sure the correct hint was being displayed. It showed that the if statements were correctly updated to give the right advice when comparing the guess and actual number.  
- Did AI help you design or understand any tests? How?
  - I asked Claude Code to generate new tests based on the bugs I discovered. One prompt for each and it made one new test function for each.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  - When the user interacts with the webpage (clicking a button, filling in values in input, etc), the app.py script reruns each time. Variables reset each time the user interacs with the page with Streamlit. To fix this sessions help persist the data even when the user interacts with the page. They are stored and retrieved each time that way data isn't lost.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  - For future labs/projects, I want to keep the auto apply edits off. I rather control and verify the code changes one at a time to ensure the changes are reliable.
- What is one thing you would do differently next time you work with AI on a coding task?
  - I would work to create a plan that outlines the changes and the way I would go about fixing it. I have different code styles.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  - AI generated code is produced fast, but often has small effects on other parts of the code. You need to ask why when these changes become noticable and be specific when asking it to modify code.