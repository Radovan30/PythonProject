class SquatDetector:
    def __init__(self):
        self.correct_squats = 0
        self.incorrect_squats = 0
        self.in_squat = False
        self.squat_in_good_form = False

    def reset(self):
        self.correct_squats = 0
        self.incorrect_squats = 0
        self.in_squat = False
        self.squat_in_good_form = False

    def detect_squat(self, torso_angle, hip_angle, knee_angle, ankle_angle):
        # Rozsah pro správný dřep
        in_correct_range = (
            0 <= torso_angle <= 65 and
            30 <= hip_angle <= 100 and
            30 <= knee_angle <= 90 and
            70 <= ankle_angle <= 85
        )

        # Narovnání (konec dřepu)
        in_neutral_stance = (knee_angle > 160 and hip_angle > 140)

        # debug
        #print(f"torso={torso_angle}, hip={hip_angle}, knee={knee_angle}, ankle={ankle_angle}")

        # NEJSEM ve dřepu
        if not self.in_squat:
            # Jestliže naměříme správný rozsah, začneme dřep
            if in_correct_range:
                self.in_squat = True
                self.squat_in_good_form = True

        # JSEM ve dřepu
        else:
            # MIMO správný rozsah, ale ještě nejsem narovnaný, NIC nevyhodnocujeme
            # Pokud se narovnáme, vyhodnotíme dřep
            if in_neutral_stance:
                if self.squat_in_good_form:
                    self.correct_squats += 1
                else:
                    self.incorrect_squats += 1

                # Reset pro další dřep
                self.in_squat = False
                self.squat_in_good_form = False





