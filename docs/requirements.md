# DataMan Requirements Register


## Project Context
The goal of this project is to remake Dataman, an educational math toy from the 1970's. The goal is to convert it into a web-based application that will be used in classrooms to aid teachers and parents in getting children to learn math, 

## Evidence Notes

Use at least four concise evidence statements. Label the source of each.

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


## Functional Requirements

Write at least four functional requirements. Each requirement should describe a capability or behavior the system must provide.

### FR-01
**Requirement:** The application must save student data between sessions.  
**Source/Rationale:** The 4th piece of evidence led to this conclusion. Students may leave and come back to the applicaton.

### FR-02
**Requirement:** The application must properly indicate how many attempts are left (for Answer Checker/ related modes).
**Source/Rationale:** Students were having difficulty knowing when they got something wrong (mentioned in the 3rd piece of evidence). There must be indicators that allow students to know how many attempts they have left before the answer is displayed.

### FR-03
**Requirement:** The application must be able to function on multiple devices.  
**Source/Rationale:** In the 5th piece of evidence stakeholders informed us that students may access the application from chrome books, phones, and home computers. The application must function on all of these.

### FR-04
**Requirement:** The application must be able to function as a web application.  
**Source/Rationale:** Stakeholders have stated in the 2nd piece of evidence that the application must be able to work in a browser.


## Non-Functional Requirements

Write at least three non-functional requirements. Each requirement should describe a measurable quality, constraint, or condition the system must satisfy.

### NFR-01
**Requirement:** The application must have an interface which is self-documenting. (eg. no outside resource should be needed to understand and use it).  
**Source/Rationale:** Stakeholders have stated that the interface should be simple enough to understand without a printed manual. The data man device itself also mentions how it was designed to be simple enough for small children to use as well.

### NFR-02
**Requirement:** The application must be lightweight enough to run on low-end devices.
**Source/Rationale:** It is stated that the application will need to work on many devices, namely home computers and mobile phones. Students need to be able to use the application no matter what their specifications on these devices are.

### NFR-03
**Requirement:** The application's interactive elements must be responsive and easy to scale to a variety of screen sizes.
**Source/Rationale:** The application will be used on many devices, as stated before. It needs to be able to be displayed properly on all of those different devices!

## Open Questions / Assumptions

Do not turn an unsupported idea into a confirmed requirement. Record unresolved items here until evidence supports a decision.

- **Q-01:** Should all of the original Datamans built in functionalities should be implemented into this web application?
- **Q-02:** Should teachers be able to assign students specific questions to practice, similarly to Datamans "Memory Bank"?


## Final Quality Check
(I was unsure if I should delete this portion so I added check marks to the boxes.)

Before submitting, confirm that each requirement is:

- [✅] Clear enough for another team member to interpret consistently.
- [✅] Supported by evidence, a stakeholder need, or a confirmed project constraint.
- [✅] Testable or verifiable later.
- [✅] Solution-neutral enough for this stage of the project.
- [✅] Focused on one main capability or quality.
- [✅] Classified correctly as functional or non-functional.

Also confirm:

- [✅] At least four functional requirements are included.
- [✅] At least three non-functional requirements are included.
- [✅] Every confirmed requirement has a source/rationale.
- [✅] Open questions and assumptions are separated from confirmed requirements.
- [✅] The simulation decision record is saved at `docs/decisions/m2-elicitation-decision-record.md`.
- [✅] This file is saved as `docs/requirements.md`, committed, and synced to GitHub.
