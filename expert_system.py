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
                conclusion = rule["conclusion"]

                if conditions.issubset(facts):

                    if conclusion not in facts:

                        facts.add(conclusion)

                        self.log.append(
                            f"Rule Fired: "
                            f"{' AND '.join(rule['conditions'])} "
                            f"-> {conclusion}"
                        )

                        changed = True

        return facts

    def get_log(self):
        return self.log