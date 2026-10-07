# M2 Elicitation Decision Record

## Investigation Path
1. What does “modern” need to mean from a user perspective?
   Evidence revealed: Stakeholders say modern means the experience should work reliably in a browser, be understandable without a printed manual, and avoid making the learner navigate unnecessary screens. They do not specify a visual style or framework.
2. Who will use the system and in what setting?
   Evidence revealed: The primary learner is a student practicing independently, often with a teacher or parent nearby. Exact device and access conditions have not yet been confirmed.
3. What exactly do stakeholders mean by “students shouldn’t lose their work”?
   Evidence revealed: Teachers report that students may pause practice and return later. They want a learner’s saved practice state to remain available after leaving and returning to the application.

## Initial Position
**Supported evidence:**
The application will need to function in a browser, and be easy enough to understand without a dedicated manual. It will mainly be used by students, though parents and teachers may observe the student using the application. Students need to be able to stop working and come back with progress intact.

**Remaining uncertainty:**
What kind of info do the parents need to know about what the child is doing? Should the layout be exactly like the dataman of the past or be more "modern"?

**Likely functional requirement:**
The user should be able to save progress in-between sessions.

**Likely non-functional requirement / quality constraint:**
The user should be able to change the theme of the application (light, dark, colors).

**Assumption or proposed solution I am not treating as confirmed:**
The user's data should be saved in the devices cookies.

**Why my initial position is defensible:**
I used the information provided to me from the questions asked, and made sure that any claims I made are supported by those answers.

## Complication
Students may use DataMan on school Chromebooks, phones, tablets, and home computers. Some sessions may be interrupted before intentional sign-out.

**What this affects:**
How the framework for the assignment will work.

**What I revised, if anything:**
The requirements stay the same, but how they are implemented will need to accommodate this new info.

**Final decision and reasoning:**
I will keep my requirements. They are unaffected by the new info. The only think that will need to change is the actual implementation, which we did not go over yet.

## Next Project Action
Use this evidence to update the DataMan Requirements Register and preserve any unresolved questions as open assumptions or follow-up items.
