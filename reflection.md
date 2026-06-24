# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The first time I ran the game, it looked functional on the surface but broke almost immediately during play. The hints were completely backwards guessing a low number like 5 told me to go lower, and guessing a high number like 95 told me to go higher. The attempt counter wasn't updating correctly either.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  The hints aren't working
  The number of attempts isn't changing
  The the new game button wasn't working

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
Guessof5| "go higher" hint.  "go lower"         "none"
Guessof95 "go lower" hint.   "go higher".       "none"
showhintbutton| it will show the hint| nothing happens| none

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? 
I used Claude as my primary AI tool throughout this project.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
One suggestion that was correct was when Claude identified that the check_guess function had its return messages swapped. It pointed me exactly to the lines where "Go HIGHER" and "Go LOWER" were reversed and explained why the logic was wrong. I verified this by running the game manually after the fix and confirming that a low guess now correctly showed "Go HIGHER.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). One example was when the AI was suggesting I chnage the hard mode from 1-200 to 1-500 after I already fixed it. But that was unnessary. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? I decided a bug was really fixed when it passed both a pytest test and a manual playthrough.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code. I tested that my hints were running correctly by making sure my hints were correct when it says go higher or go lower.
- Did AI help you design or understand any tests? How?
Claude helped me design the pytest structure by suggesting what inputs and assertions would actually target the specific bug rather than just testing that the function runs at all.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? 
Streamlit basically reruns the entire Python script every single time a user clicks a button or changes an input so, it's not like a normal app that sits and waits for events. Session state is how you basically save the information across those reruns, kind of like a notepad or reminder that Streamlit keeps on the side and doesn't erase between runs. Without session state, the secret number would regenerate on every click, making the game unplayable

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? 
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  One habit I want to continue is adding # FIXME comments when I see a bug before touching any code, which made my prompts much more specific and useful when asking the ai for help.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code. 
This showed me how useful AI and how it can help you learn while working on your code. But it also showed me that AI can write code that looks completely reasonable and still be a little wrong in ways that only show up when you actually play the game. So its always important to double check.
