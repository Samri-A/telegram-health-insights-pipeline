import os
import pandas as pd


LABEL_DIR = 'C:/Users/HP/OneDrive/Desktop/Tenx/telegram-health-insights-pipeline/src/results/run13/labels/'
OUTPUT_CSV = 'C:/Users/HP/OneDrive/Desktop/Tenx/telegram-health-insights-pipeline/data/image_detections.csv' 


CLASS_NAMES = {
    0: 'person',
    11: 'fire extinguisher',
    26: 'handbag',
    39: 'bottle',
    56: 'chair',
    62: 'tv',
    63: 'laptop',
    65: 'remote',
    67: 'cell phone',
    73: 'book'
}

rows = []

for label_file in os.listdir(LABEL_DIR):
    if label_file.endswith('.txt'):
        message_id = os.path.splitext(label_file)[0].split('_')[-1]  # e.g., "171980"
        with open(os.path.join(LABEL_DIR, label_file), 'r') as f:
            for line in f:
                parts = line.strip().split()
                class_id = int(parts[0])
                confidence = float(parts[-1])
                rows.append({
                    'message_id': int(message_id),
                    'detected_object_class': CLASS_NAMES.get(class_id, f'class_{class_id}'),
                    'confidence_score': confidence
                })


df = pd.DataFrame(rows)
df.to_csv(OUTPUT_CSV, index=False)
print(f"Saved detections to {OUTPUT_CSV}")


