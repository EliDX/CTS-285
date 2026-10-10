# M3 Product Owner Decision Record

## Scenario
StudyTrack release planning under constrained capacity.

## Round 1 — Capacity 13
- ST-01: Create a study task (3 pts)
- ST-02: Mark a study task complete (2 pts)
- ST-03: Recover a missed task (3 pts)
- ST-04: Keyboard-accessible task entry (2 pts)

**Why this release slice was defensible:**
The intended goal is to release a product that allows for students to use the basic functionalities of the application. ST-01, ST-02, and ST-03 are all required for the application to work. Without them it wouldn't be able to function in a way that would be useful.

**One intentional deferral and why:**
I initially wasn't going to include ST-04, but in the end I realized it could be a bit help in terms of accessibility for the application. It isn't 100% necessary, but there was room in the capacity to include it without sacrificing the core features.

## Complication
Capacity dropped from 13 to 10 points. Keyboard accessibility testing revealed that task entry cannot reliably be completed with keyboard navigation, so ST-04 became release-critical.

## Revised Release Slice — Capacity 10
- ST-01: Create a study task (3 pts)
- ST-02: Mark a study task complete (2 pts)
- ST-03: Recover a missed task (3 pts)
- ST-04: Keyboard-accessible task entry (2 pts)

### Removed after complication
- None

### Added after complication
- None

**What changed and why:**
Nothing in my plan has changed, as I was already under capacity and I had included the keyboard functionality in my initial plan.

**Tradeoff accepted:**
Since I did not have to revise the project, there were no tradeoffs.

## Transfer to DataMan
Before finalizing your DataMan backlog, review whether any item is high value but not ready, depends on unresolved work, consumes disproportionate effort, or should move because it reduces risk or unlocks other work.
