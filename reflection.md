# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

 - so my intitial UML design is to have three classes, one for the pet's information, one for assigning what tasks to do for the pet and the final one to hold the plan. 

 the interactions would be the consutrcor, which is the pet class, would have the pet ifnromatino as the child class, just to keep things organized, and since different pets have different needs. Then the plan option can either extend the infromation class or just see it's values to make a plan based on what tasks need to be done. Finally, there would be a contraints class, for th users time schedule, priorty and owner preference.

 Class: Pet -> holds pet name and breed -> constructs a new pet object 
 Class: PetInfo -> holds the ifnromaiton whether the pet needs walks, feeding, meds, enrichment, grooming, etc. -> has unique tasks, and hodls a bool to see if the pe needs it, and additional variables for the duration, intensity, qunitiy etcs. and special infromation entered by the user 
 Class: schedule -> generates the plan for the day based on the information -> can access the petInfo class, but only sees it to make a schdule. 
 Class: OwnerConstrinats -> has data points for the users schedule, references liek walk timings and priorty of tasks. The schedule class can acces this to make the schedule. 



**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
