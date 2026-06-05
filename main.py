from rules import RULES
from expert_system import ExpertSystem


def main():

    print("=" * 40)
    print("RULE-BASED EXPERT SYSTEM")
    print("=" * 40)

    user_input = input(
        "\nEnter symptoms separated by commas:\n"
    )

    facts = [
        symptom.strip().lower()
        for symptom in user_input.split(",")
    ]

    expert = ExpertSystem(RULES)

    final_facts = expert.forward_chain(facts)

    print("\nFinal Facts:")
    for fact in sorted(final_facts):
        print("-", fact)

    print("\nInference Log:")
    for step in expert.get_log():
        print(step)


if __name__ == "__main__":
    main()