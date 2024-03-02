from typing import Dict


class Player:

    def __init__(self, name: str, hp: int, mp: int):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills: Dict[str: int] = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost) -> str:
        if skill_name in self.skills.keys():
            return f"Skill already added"

        self.skills[skill_name] = self.skills.get(skill_name, mana_cost)
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self) -> str:
        skills = "\n".join(f"==={n} - {m}" for n, m in self.skills.items())
        return f"Name: {self.name}\n" \
               f"Guild: {self.guild}\n" \
               f"HP: {self.hp}\n" \
               f"MP: {self.mp}\n" \
               f"{skills}"



