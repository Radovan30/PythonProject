import cv2
import mediapipe as mp
from CalculateAngle import CalculateAngle
from SquatDetector import SquatDetector


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

# Otevření videa
video = "video4.mp4"

cap = cv2.VideoCapture(video)

# Nastavení FPS a výpočtu časového intervalu
fps = int(cap.get(cv2.CAP_PROP_FPS))  # Získání FPS videa
start_time = 20  # Start v čase
end_time = 60  # Konec v čase

# Výpočet odpovídajících snímků
start_frame = start_time * fps
end_frame = end_time * fps

# Nastavení na startovací frame
cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

paused = False

squat_detector = SquatDetector()

# Nastavení MediaPipe Pose
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5, model_complexity=1) as pose:
    try:
        while True:
            if not paused:
                current_frame = int(cap.get(cv2.CAP_PROP_POS_FRAMES))

                if current_frame >= end_frame:
                    # Reset čítačů
                    squat_detector.reset()
                    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
                    continue

                ret, frame = cap.read()
                if not ret:
                    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
                    continue

                frame = cv2.resize(frame, (800, 600))
                image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                image.flags.writeable = False

                results = pose.process(image)

                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

                if results and results.pose_landmarks:
                    landmarks = results.pose_landmarks.landmark

                    # Body pro výpočet úhlů
                    hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                           landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
                    knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
                    ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                             landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

                    shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,
                                landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]

                    foot = [landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].x,
                            landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].y]


                    # Výpočet úhlů
                    torso_angle = CalculateAngle.calculate_torso_angle(shoulder, hip)          # Trup vůči podlaze
                    hip_angle = CalculateAngle.calculate_hip_angle(shoulder, hip, knee)        # Kyčelní úhel
                    knee_angle = CalculateAngle.calculate_knee_angle(hip, knee, ankle)         # Kolenní úhel
                    ankle_angle = CalculateAngle.calculate_ankle_angle(knee, ankle, foot)      # Kotníkový úhel

                    # Detekce dřepu
                    squat_status = squat_detector.detect_squat(torso_angle, hip_angle, knee_angle, ankle_angle)

                    # Barva podle správnosti úhlu
                    torso_color = (0, 255, 0) if 0 <= torso_angle <= 65 else (0, 0, 255)
                    hip_color = (0, 255, 0) if 30 <= hip_angle <= 100 else (0, 0, 255)
                    knee_color = (0, 255, 0) if 30 <= knee_angle <= 90 else (0, 0, 255)
                    ankle_color = (0, 255, 0) if 70 <= ankle_angle <= 85 else (0, 0, 255)

                    # Zobrazení úhlů na obrazovce
                    cv2.putText(image, f"{int(torso_angle)}",
                                (int(shoulder[0] * 800), int(shoulder[1] * 600)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, torso_color, 2, cv2.LINE_AA)

                    cv2.putText(image, f"{int(hip_angle)}",
                                (int(hip[0] * 800), int(hip[1] * 600)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, hip_color, 2, cv2.LINE_AA)

                    cv2.putText(image, f"{int(knee_angle)}",
                                (int(knee[0] * 800), int(knee[1] * 600)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, knee_color, 2, cv2.LINE_AA)

                    cv2.putText(image, f"{int(ankle_angle)}",
                                (int(ankle[0] * 800), int(ankle[1] * 600)),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, ankle_color, 2, cv2.LINE_AA)

                    # Výpis správného nebo špatného dřepu
                    base_x, base_y = 50, 50

                    cv2.putText(image, "Correct:", (base_x, base_y),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                    cv2.putText(image, f"{squat_detector.correct_squats}", (base_x + 150, base_y),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

                    cv2.putText(image, "Wrong:", (base_x, base_y + 40),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                    cv2.putText(image, f"{squat_detector.incorrect_squats}", (base_x + 150, base_y + 40),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)


            # Zobrazíme aktuální snímek
            cv2.imshow('Frame', image)

            # Ovládání klávesami
            key = cv2.waitKey(10) & 0xFF
            if key == ord('q') or cv2.getWindowProperty('Frame', cv2.WND_PROP_VISIBLE) < 1:
                break
            elif key == 32:  # mezerník - pauza
                paused = not paused  # Přepínání pauzy ON/OFF

    except KeyboardInterrupt:
        print("User exits the program.")

    finally:
        cap.release()
        cv2.destroyAllWindows()
