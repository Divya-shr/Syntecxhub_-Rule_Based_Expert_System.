# expert_system.py

class ExpertSystem:

    def __init__(self, rules):
        self.rules = rules
        self.log = []

    def forward_chain(self, facts):

        facts = set(facts)

        changed = True

        while changed:

            changed = False

            for rule in self.rules:

                conditions = set(rule["conditions"])

                if conditions.issubset(facts):

                    conclusion = rule["conclusion"]

                    if conclusion not in facts:

                        facts.add(conclusion)

                        self.log.append(
                            f"IF {' AND '.join(rule['conditions'])} "
                            f"THEN {conclusion}"
                        )

                        changed = True

        return facts

    def get_log(self):
        return self.log
