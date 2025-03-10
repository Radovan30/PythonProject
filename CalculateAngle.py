import numpy as np

class CalculateAngle:
    @staticmethod
    def calculate_angle(a, b, c, invert=False):
        a = np.array(a[:2])
        b = np.array(b[:2])
        c = np.array(c[:2])

        # Vektory mezi body
        ba = a - b
        bc = c - b

        # Výpočet úhlu pomocí skalárního součinu
        cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
        angle = np.degrees(np.arccos(np.clip(cosine_angle, -1.0, 1.0)))

        return 180 - angle if invert else angle

    # Vytvoření bodu nad kyčlemi pro správný výpočet trupu
    @staticmethod
    def get_vertical_reference(hip):
        return [hip[0], hip[1] + 0.1]

    # Vytvoření vodorovného bodu pro kotník
    @staticmethod
    def get_horizontal_foot(ankle):
        return [ankle[0] + 0.1, ankle[1]]

    # Vypočet úhlu trupu
    @staticmethod
    def calculate_torso_angle(shoulder, hip):
        vertical_ref = CalculateAngle.get_vertical_reference(hip)
        return CalculateAngle.calculate_angle(shoulder, hip, vertical_ref, invert=True)

    # Vypočet úhlu kyčle
    @staticmethod
    def calculate_hip_angle(shoulder, hip, knee):
        return CalculateAngle.calculate_angle(shoulder, hip, knee)

    # Vypočet úhlu kolene
    @staticmethod
    def calculate_knee_angle(hip, knee, ankle):
        return CalculateAngle.calculate_angle(hip, knee, ankle)

    # Vypočet úhlu kotníku
    @staticmethod
    def calculate_ankle_angle(knee, ankle, foot):
        foot_ref = CalculateAngle.get_horizontal_foot(ankle)
        return CalculateAngle.calculate_angle(knee, ankle, foot_ref)


