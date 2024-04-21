from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    MINIMUM_STRENGTH_NEEDED = 100
    INITIAL_STRENGTH = 200

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_STRENGTH)

    def can_climb(self) -> bool:
        return self.strength >= self.MINIMUM_STRENGTH_NEEDED

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            self.strength -= 20 * 2
        else:
            self.strength -= 20 * 1.5

        self.conquered_peaks.append(peak.name)
