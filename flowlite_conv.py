import tensorflow as tf

# Load your best Keras model
model = tf.keras.models.load_model('best_model.h5')

# Create a converter
converter = tf.lite.TFLiteConverter.from_keras_model(model)

# Perform the conversion (no optimizations)
tflite_model = converter.convert()

# Save the final model for your Flutter app
with open('best_model1.tflite', 'wb') as f:
  f.write(tflite_model)

print("Successfully converted model to best_model1.tflite")
