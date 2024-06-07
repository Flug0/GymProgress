

class Set:
    def __init__(self, weight, w_unit, reps, order=None, RPE=None, dist=None, d_unit=None, seconds=None, notes=None, workout_notes=None) -> None:
        self.weight = weight
        self.reps = reps

        self.one_rep_max = self.calculate_one_rep_max()

        self.w_unit = w_unit
        self.order = order
        self.RPE = RPE
        self.dist = dist
        self.d_unit = d_unit
        self.seconds = seconds
        self.notes = notes
        self.workout_notes = workout_notes

    def __str__(self) -> str:
        return f"Weight: {self.weight} {self.w_unit}, Reps: {self.reps}, 1RM: {self.one_rep_max}"
    
    def calculate_one_rep_max(self):
        return self.weight * (36/(37-self.reps))