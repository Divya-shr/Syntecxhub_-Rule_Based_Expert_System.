# main.py

from rules import RULES
from expert_system import ExpertSystem


def print_rules():

    print("\nKnowledge Base:")

    for i, rule in enumerate(RULES, start=1):

        conditions = " AND ".join(
            rule["conditions"]
        )

        conclusion = rule["conclusion"]

        print(
            f"{i}. IF {conditions} "
            f"THEN {conclusion}"
        )


def get_conclusion(final_facts):

    if "severe_flu" in final_facts:
        return (
            "Possible Disease: Severe Flu",
            "Advice: Doctor Consultation Recommended"
        )

    elif "flu" in final_facts:
        return (
            "Possible Disease: Flu",
            "Advice: Take Rest and Stay Hydrated"
        )

    else:
        return (
            "No Disease Identified",
            "Advice: Insufficient Symptoms"
        )


def main():

    print("=" * 40)
    print("      RULE BASED EXPERT SYSTEM")
    print("=" * 40)

    symptoms = input(
        "\nEnter symptoms (comma separated):\n"
    )

    facts = [
        symptom.strip().lower()
        for symptom in symptoms.split(",")
    ]

    print_rules()

    expert = ExpertSystem(RULES)

    final_facts = expert.forward_chain(facts)

    print("\n" + "-" * 40)
    print("Inference Log")
    print("-" * 40)

    for step in expert.get_log():
        print(step)

    print("\n" + "-" * 40)
    print("Final Facts")
    print("-" * 40)

    for fact in sorted(final_facts):
        print(fact)

    disease, advice = get_conclusion(
        final_facts
    )

    print("\n" + "-" * 40)
    print("Final Conclusion")
    print("-" * 40)

    print(disease)
    print(advice)


if __name__ == "__main__":
    main()
