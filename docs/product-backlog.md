# DataMan Product Backlog

## Sources

This backlog uses these files from my repository:

- `docs/requirements.md`
- `docs/decisions/m3-backlog-triage-record.md`
- `docs/decisions/m3-product-owner-decision-record.md`

The file `docs/requirements.md` was revised after its initial submission.

## Priority Order

List every story ID from highest priority to lowest. The story blocks below must appear in this same order.

1. US-01
2. US-02
3. US-03
4. US-04

## Stories

### US-01 — Provide indicators for when an answer is correct/incorrect.

**Requirement ID:** FR-03, FR-04.

**User Story:** As a student, I want to clearly know whether or not I got an answer correct so that I can understand the results in my practice sessions better.

**Acceptance Criteria:**

- Given a student or other user is using a feature which validates answers as correct/incorrect, when an incorrect answer is inputted, notify the user their answer is incorrect. This response must be distinct/separate from the one used for correct answers.

- Given a student or other user is using a feature which validates input, when a correct answer/acceptable input is inputted, then notify the user their answer is correct. This response must be distinct/separate from the one used for incorrect answers.

**Relative Effort:** Small. Does not take as much effort as SU-03 or SU-04, and does not have any dependancies or constraints.

**Dependency / Constraint:** None

**Priority:** 1

**Readiness:** Move Forward  

**Priority Rationale:** Knowing if the answer you have entered is correct is an integral part of the DataMan toy. If there is no clear distinction between the response given for both answers, the product would not be functioning as intended. This is also one of the 'easier' requirements to fufil in comparison to the others, with no dependencies.

---

### US-02 — Display the amount attempts left.

**Requirement ID:** FR-02

**User Story:** As a student, I want indication on how many attempts I have left so that I can understand when I will be taken to the next practice problem.

**Acceptance Criteria:**

- Given a student has started a practice session , either before or when an incorrect answer is inputted, then the student is notified on how many attempts they have left.

**Relative Effort:** Small. Similar in effort to SU-01.

**Dependency / Constraint:** US-01

- Having US-01 completed would aid significantly in making it clear to the user exactly when an attempt is 'used' by inputting an incorrect answer. If this is fufilled first, a situation similar to that described in E-03 of requirements.md may happen again.

**Priority:** 2

**Readiness:** Move Forward

**Priority Rationale:** This is an integral feature for the application, and was directly shown to be a need mentioned in interviews for the prototypes of this project used in classrooms before. In terms of effort needed, it is possible that it might be 'easier' to fufil than US-01. However as mentioned under the dependencies section, it does rely on US-01 to function properly.

---

### US-03 — Save user practice progress between authenticated sessions.

**Requirement ID:** FR-01

**User Story:** As a student, I want to be able to save my practice progress so that I can continue from where I left off if I choose to stop or if my practice session is accidentally stopped.

**Acceptance Criteria:**

- Given a student has started an authenticated practice session, when the session is either intentionally or unintentionally ended, then their progress will be available when they access the application again.


**Relative Effort:** Large. Not necessarily 'hard' but would take much more  time in comparison to SU-01 and SU-02. Additionally has some details that need to be worked out.

**Dependency / Constraint:** This does rely heavily on how the sessions are authenticated, and what data is needed to be saved from the practice sessions. It could be simple to only save the users progress only for sessions that aren't 'completed', but if more data is necessary this could be more complicated.

**Priority:** 3

**Readiness:** Refine

**Priority Rationale:** Unlike US-01 and US-02, this user story would take a lot more steps to fulfill. While fulfilling this user story is required for the application to work as specified by stakeholders, the two prior stories are more 'necessary' for the application to properly function. If the students can't practice properly, what would be the point in working to have that data saved?

---

### US-04 — Multi-platform compatibility.

**Requirement ID:** NFR-02, NFR-03

**User Story:** As a teacher I would like students to be able to use the application on multiple devices so that they can still practice outside of school.

**Acceptance Criteria:**

- Given a user wants to use the application, if they are at home (or otherwise away from school, then they are able to access the application on any device capable of running the application.

**Relative Effort:** Large effort. Has the potential to be 'easier' than SU-03, but a bit more difficult than SU-01 or SU-02.

**Dependency / Constraint:** 
- Knowing what platform the project is being developed/was developed for currently would be important to know. The current acceptance criteria hinges on the phrase 'capable of running the application', which I do realize is a bit vague.
- (E-02 in requirements.md does mention how stakeholders say the application should be web-based, and E-05 mentions how it will be mainly used on Chromebooks, phones, and home computers. It would be reasonable to say that devices similar to those are the ones considered 'capable of running the application'.
- Additionally, while an application being multi-platform doesn't necessarily mean being able to save and transfer data between platforms, that is always a possibility, meaning this story could end up relying on US-03 (or potentially leading to the creation of another user story).

**Priority:** 4

**Readiness:** Defer

**Priority Rationale:** This story is based off of two non-functional requirements, and also has a quite a few complications that need to be solved before it could be worked on. It is also one of the 'larger' user stories, and depending on how the implementation for this story will work, may end up depending on the results of other stories fufillment.

## Open Questions Carried Forward


- **Q-03:** US-04 waits on this question. While we do have evidence that the application has been used/tested in a school-environment (via E-03 in requirements.md), we still have no info on what kind of system this application is being optimized for currently. It is possible to say it is being optimized for chrome books currently, but despite being partially supported (via E-05), this is still mainly an assumption.

- **Q-04** US-03 waits on this question. Knowing exactly what info should be saved will be important when it comes to fulfilling this story. It would be simple enough to just save the users practice data for them to resume, but it is possible that other data will also need to be saved. If so, the scope for US-03 might need to be increased.

## Revisions After Triage and Release Planning

State what changed in this backlog because of your triage record and your Product Owner decision record.

- US-01 and US-02 initially were going to be two parts of the same user story. But I had realized that having them separate made them a lot easier to process, especially considering the size of the other two user stories. This was not the result of any record in particular, as I began work on this backlog after completing the records for this module.


