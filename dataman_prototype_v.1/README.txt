This prototype tests the following requirements that I listed in 'docs/requirements.md':

FR-02) The application tells you how many attempts you have left.

FR-03 and FR-04) Th application distinctly tells you when you get a question right or wrong.

NFR-01) The application is self documenting. (This is more objective, but instructons are provided and each input section does tell you what options should be inputted.)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

What is this prototype missing?

1. The data layer has not been implemented, but the file is present.
2. Memory Bank and Number Guesser have not been implemented.
3. This program cannot be used on the web currently.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

What do I need to fix:

Right now, there are some things I would rather have been handled by the backend that the frontend handles.
Particularly input validation (May not be as big of a problem as I think it is).

I also want to make the logic code a bit more flexible. 
I feel like the way it is structured now might be hard to adapt to other things (Memory Bank, Number Guesser, etc.)
