RULES = [
    {
        "conditions": ["fever", "cough"],
        "conclusion": "flu"
    },
    {
        "conditions": ["flu", "body_pain"],
        "conclusion": "severe_flu"
    },
    {
        "conditions": ["severe_flu"],
        "conclusion": "doctor_consultation"
    }
]