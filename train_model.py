import numpy as np
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

# Load .npy files
DATA_DIR = 'quickdraw'
CLASSES = ['sun', 'hand', 'face', 'flower']
NUM_SAMPLES = 133781  # limit per class to speed up

X = []
y = []

for idx, cls in enumerate(CLASSES):
    path = os.path.join(DATA_DIR, cls + '.npy')
    data = np.load(path)
    data = data[:NUM_SAMPLES]
    X.append(data)
    # For multi-label, create 0/1 array for each class
    labels = np.zeros((len(data), len(CLASSES)))
    labels[:, idx] = 1
    y.append(labels)

# Convert to arrays
X = np.concatenate(X, axis=0)
y = np.concatenate(y, axis=0)

# Normalize pixel values
X = X / 255.0
X = X.reshape(-1, 28, 28, 1)

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dropout(0.3),
    Dense(len(CLASSES), activation='sigmoid')  # Multi-label output
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=20, batch_size=64, validation_data=(X_test, y_test))

model.save('model.h5')
print("✅ Multi-label model saved as model.h5")