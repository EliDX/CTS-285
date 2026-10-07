# DataMan Requirements Register


## Project Context
The goal of this project is to remake Dataman, an educational math toy from the 1970's. The goal is to convert it into a web-based application that will be used in classrooms to aid teachers and parents in getting children to learn math.


## Evidence Notes


- **E-01 — Source:** Stakeholder Elicitation sim.  
**Evidence:** "The primary learner is a student practicing independently, often with a teacher or parent nearby."

- **E-02 — Source:** Stakeholder Elicitation sim.  
**Evidence:** "Stakeholders say modern means the experience should work reliably in a browser, be understandable without a printed manual, and avoid making the learner navigate unnecessary screens."

- **E-03 — Source:** M2.3 Elicitation Case  
**Evidence:** Ms. Alvarez stated that students were getting frustrated. It is revealed that the learners would start the Answer Checker, get a problem wrong twice, and not understand what was happening when the device displayed the wrong answer.

- **E-04 — Source:** Stakeholder Elicitation sim.  
**Evidence:** Stakeholders (teachers) report that the students may pause their practice and come back at a later time.

- **E-05 — Source:** Stakeholder Elicitation sim.  
**Evidence:** In the simulation, it was said that students may end up using the application on a variety of devices (Chromebooks, phones, and home computers). Sessions may be terminated before the students intentionally sign out.

- **E-06 — Source:** Dataman Manual (Hints for Parents and Teachers: Fun and Positive Reinforcement).    
**Evidence:** "DataMan motivates your child positively by rewarding right answers and good scores with a dazzling 'light show.' He also reacts to incorrect answers immediately with a simple 'EEE' indication in the display, followed by a brief 'blinking light' pattern."  


## Functional Requirements


### FR-01
**Requirement:** The application must automatically save a students practice progress between/during authenticated sessions.  
**Source/Rationale:** The E-04 led to this conclusion. Students may leave and come back to the application, and some sessions may end before they are intended to. In order to make sure students do not lose their progress, the sessions progress must be saved regularly.

### FR-02
**Requirement:** The application must clearly indicate how many attempts are left (for Answer Checker/ related modes).  
**Source/Rationale:** Students were having difficulty knowing when they got something wrong (mentioned in E-03). There must be indicators that allow students to know how many attempts they have left before the answer is displayed.

### FR-03
**Requirement:** The application must clearly and unmistakably indicate when a problem is answered correctly.   
**Source/Rationale:** The original Dataman device (refer to E-06) states how the original device has a clear and unmistakable response to correct answers. 

### FR-04
**Requirement:**  The application must clearly indicate when a problem is answered incorrectly.
**Source/Rationale:** As mentioned in E-06, the device must also clearly indicate when an answer is incorrect. In E-03 Ms. Alvarez mentions how students did not fully understand when they were getting problems wrong, which exacerbated the issue many had with the unclear amount of attempts.


## Non-Functional Requirements


### NFR-01
**Requirement:** The application must have an interface which is self-documenting. (eg. no outside resource should be needed to understand and use it).  
**Source/Rationale:** Stakeholders have stated that the interface should be simple enough to understand without a printed manual. The data man device itself also mentions how it was designed to be simple enough for small children to use as well.

### NFR-02
**Requirement:** The application must be able to function on multiple devices.  
**Source/Rationale:** In E-04 stakeholders informed us that students may access the application from chrome books, phones, and home computers. The application must function on all of these.

### NFR-03
**Requirement:** The application must be able to function as a web application.  
**Source/Rationale:** Stakeholders have stated in E-02 of evidence that the application must be able to work in a browser.

## Open Questions / Assumptions


- **Q-01:** Should all of the original Datamans built in functionalities should be implemented into this web application?      
- **Q-02:** Should teachers be able to assign students specific questions to practice, similarly to Datamans "Memory Bank"?    
- **Q-03:** What are the requirements for performance? Should the application be optimized for chromebooks or should it stay as lightweight as possible in order to work on the largest variety of devices?  
- **Q-04:** Will teachers/parents be able to see progress in the application itself? Additionally, how will student progress be saved (eg. after every question answered?)  


