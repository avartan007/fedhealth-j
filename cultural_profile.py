class CulturalProfile:
    def __init__(self, region, season):
        self.region = region
        self.season = season
    def adjust_heart_rate(self, hr):
        if self.season == "summer": return hr - 5
        elif self.season == "winter": return hr
        return hr
    def adjust_steps(self, steps):
        if self.season == "winter": return int(steps * 0.6)
        return steps
