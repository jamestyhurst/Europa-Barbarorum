class Season:
    def __init__(self, name, quarter):
        self.name = name
        self.quarter = quarter

    def change_season(self):
        if self.quarter == 2:
            self.quarter += 1
            self.name = 'Fall'
        elif self.quarter == 3:
            self.quarter +=1
            self.name = 'Winter'
        elif self.quarter == 1:
            self.quarter +=1
            self.name = 'Summer'
        elif self.quarter == 4:
            self.quarter = self.quarter - 3
            self. name = 'Spring'