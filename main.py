import os
import random
import shutil

# Paths
dataset_dir = "dataset"
train_images_dir = os.path.join(dataset_dir, "train", "images")
train_labels_dir = os.path.join(dataset_dir, "train", "labels")
val_images_dir = os.path.join(dataset_dir, "val", "images")
val_labels_dir = os.path.join(dataset_dir, "val", "labels")

# Create validation directories if they don't exist
os.makedirs(val_images_dir, exist_ok=True)
os.makedirs(val_labels_dir, exist_ok=True)

# Split ratio (e.g., 20% for validation)
val_ratio = 0.2

# List all images
all_images = [f for f in os.listdir(train_images_dir) if f.endswith((".jpg", ".png"))]
num_val = int(len(all_images) * val_ratio)

# Randomly select validation images
val_images = random.sample(all_images, num_val)

# Move images and corresponding labels to val folder
for img_file in val_images:
    label_file = img_file.replace(".jpg", ".txt").replace(".png", ".txt")

    # Move image
    shutil.move(os.path.join(train_images_dir, img_file),
                os.path.join(val_images_dir, img_file))
    
    # Move label
    if os.path.exists(os.path.join(train_labels_dir, label_file)):
        shutil.move(os.path.join(train_labels_dir, label_file),
                    os.path.join(val_labels_dir, label_file))

print(f"Moved {num_val} images and labels to validation set.")
