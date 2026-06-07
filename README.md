
# Rule-Based Expert System

A simple AI-based Expert System developed in Python using **Forward Chaining**. The system accepts user symptoms as facts, applies predefined IF-THEN rules, and infers conclusions through multi-step reasoning.

## Project Objective

This project demonstrates the concepts of:

- Expert Systems
- Knowledge Base
- Facts Base
- Rule-Based Reasoning
- Forward Chaining
- Multi-Step Inference
- Explainable AI (Inference Log)

## Features

- Accepts user symptoms as input
- Stores facts in a facts base
- Uses IF-THEN rules stored in a rule base
- Implements Forward Chaining inference
- Supports multi-step rule chaining
- Displays reasoning path (Inference Log)
- Provides final diagnosis and recommendation

---

## Project Structure

```text
Rule_Based_Expert_System/
│
├── rules.py
├── expert_system.py
├── main.py
└── README.md
```

### File Description

| File | Description |
|--------|------------|
| rules.py | Contains the rule base (knowledge base) |
| expert_system.py | Implements the forward chaining inference engine |
| main.py | Takes user input and displays results |
| README.md | Project documentation |

---

## Knowledge Base

The system uses the following rules:

```text
IF fever AND cough THEN flu

IF flu AND body_pain THEN severe_flu

IF severe_flu THEN doctor_consultation
```

---

## How Forward Chaining Works

Given user symptoms:

```text
fever
cough
body_pain
```

The system infers:

```text
fever + cough
        ↓
       flu
        ↓
flu + body_pain
        ↓
   severe_flu
        ↓
doctor_consultation
```

Newly inferred facts are reused to trigger additional rules until no more conclusions can be derived.

---

## Installation

### Clone Repository

```bash
git clone (https://github.com/Divya-shr/Syntecxhub_-Rule_Based_Expert_System..git)
```

### Navigate to Project

```bash
cd Rule-Based-Expert-System
```

### Run Project

```bash
python main.py
```

---

## Example Input

```text
fever,cough,body_pain
```

---

## Example Output

```text
========================================
      RULE BASED EXPERT SYSTEM
========================================

Knowledge Base:

1. IF fever AND cough THEN flu
2. IF flu AND body_pain THEN severe_flu
3. IF severe_flu THEN doctor_consultation

----------------------------------------
Inference Log
----------------------------------------

IF fever AND cough THEN flu

IF flu AND body_pain THEN severe_flu

IF severe_flu THEN doctor_consultation

----------------------------------------
Final Facts
----------------------------------------

body_pain
cough
doctor_consultation
fever
flu
severe_flu

----------------------------------------
Final Conclusion
----------------------------------------

Possible Disease: Severe Flu
Advice: Doctor Consultation Recommended
```

---

## Algorithm

1. Accept symptoms from the user.
2. Store symptoms as facts.
3. Check all rules.
4. If rule conditions are satisfied:
   - Infer a new fact.
   - Add it to the facts base.
   - Record the inference step.
5. Repeat until no new facts can be generated.
6. Display:
   - Inference Log
   - Final Facts
   - Final Conclusion

---

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Rule-Based AI
- Forward Chaining Inference

---

## AI Concepts Demonstrated

- Expert System
- Knowledge Representation
- Rule Base
- Facts Base
- Inference Engine
- Forward Chaining
- Multi-Step Reasoning
- Explainable AI

---

## Author

Konni Divya

AI Mini Project - Rule-Based Expert System
