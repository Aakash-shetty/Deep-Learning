import os
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load your pre-trained Keras model
model = load_model('model.h5')

# Define a function to preprocess the image for the model
def preprocess_image(image_path):
    img = image.load_img(image_path, target_size=(300, 300))  # Assuming your model expects 224x224 images
    img = image.img_to_array(img)
    img = img / 255.0  # Normalize the pixel values to the range [0, 1]
    img = img.reshape((1, 300, 300, 3))  # Reshape for the model
    return img

@app.route('/')
def index():
    return render_template('web.html')

@app.route('/classify', methods=['POST'])
def classify_image():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    image_file = request.files['image']

    if image_file.filename == '':
        return jsonify({'error': 'No selected image file'})

    if image_file:
        # Save the uploaded image temporarily
        image_path = 'temp_image.jpg'
        image_file.save(image_path)

        # Preprocess the image
        img = preprocess_image(image_path)

        # Perform classification using the model
        prediction = model.predict(img)
        class_index = prediction.argmax()

        # Map class index to labels
        class_labels = ["Good", "Bad"]
        result = class_labels[class_index]

        # Clean up the temporary image file
        os.remove(image_path)

        # Return the classification result
        return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
