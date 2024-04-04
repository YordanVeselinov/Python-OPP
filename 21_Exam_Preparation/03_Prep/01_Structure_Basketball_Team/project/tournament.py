from typing import List
from project.equipment.base_equipment import BaseEquipment
from project.equipment.elbow_pad import ElbowPad
from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam
from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam


class Tournament:
    VALID_EQUIPMENT = {
        "KneePad": KneePad,
        "ElbowPad": ElbowPad
    }

    VALID_TEAMS = {
        "OutdoorTeam": OutdoorTeam,
        "IndoorTeam": IndoorTeam
    }

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: List[BaseEquipment] = []
        self.teams: List[BaseTeam] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        try:
            equipment = self.VALID_EQUIPMENT[equipment_type]()
        except KeyError:
            raise ValueError(f"Invalid equipment type!")

        self.equipment.append(equipment)
        return f'{equipment_type} was successfully added.'

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        try:
            team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        except KeyError:
            raise ValueError(f"Invalid team type!")

        if self.capacity <= len(self.teams):
            return f'Not enough tournament capacity.'

        self.teams.append(team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team: BaseTeam = next(filter(lambda t: t.name == team_name, self.teams))
        equipment: BaseEquipment = [eq for eq in self.equipment if eq.__class__.__name__ == equipment_type][-1]

        if team.budget < equipment.price:
            raise Exception("Budget is not enough!")

        # TODO: We have to remove the last equipment from the list
        self.equipment.remove(equipment)
        team.equipment.append(equipment)
        team.budget -= equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        try:
            team: BaseTeam = next(filter(lambda t: t.name == team_name, self.teams))
        except StopIteration:
            raise Exception("No such team!")

        if team.wins:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        changed_eq_pcs = len([eq.increase_price() for eq in self.equipment if eq.TYPE_ == equipment_type])
        return f"Successfully changed {changed_eq_pcs}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team_one: BaseTeam = next(filter(lambda t: t.name == team_name1, self.teams))
        team_two: BaseTeam = next(filter(lambda t: t.name == team_name2, self.teams))

        if not team_one.TYPE_ == team_one.TYPE_:
            raise Exception(f"Game cannot start! Team types mismatch!")

        team_one_total_points = team_one.advantage + sum([eq.protection for eq in team_one.equipment])
        team_two_total_points = team_two.advantage + sum([eq.protection for eq in team_two.equipment])

        if team_one_total_points > team_two_total_points:
            team_one.win()
            return f"The winner is {team_one.name}."
        elif team_two_total_points > team_one_total_points:
            team_two.win()
            return f"The winner is {team_two.name}."
        else:
            return f"No winner in this game."

    def get_statistics(self):
        # result = f"Tournament: {self.name}\n"
        # result += f"Number of Teams: {len(self.teams)}\n"
        # result += f"Teams:\n"
        #
        # sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        #
        # result += '\n'.join(t.get_statistics() for t in sorted_teams)
        #
        # return result
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        result = [f"""Tournament: {self.name}
        Number of Teams: {len(self.teams)}
        Teams:"""]
        [result.append(t.get_statistics()) for t in sorted_teams]
        return '\n'.join(result)
