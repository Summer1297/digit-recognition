from django.shortcuts import render
import json
import base64
from PIL import Image
from io import BytesIO
from django.http import JsonResponse
from tensorflow.keras.models import load_model
import numpy as np

model = load_model('models/mnist_model.h5')

def home(request):
    return render(request, 'home.html')

def recognize_digit(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8')) 
            image_data = data['image'].split(",")[1]  
            
            image = Image.open(BytesIO(base64.b64decode(image_data))).convert('L')
            image = image.resize((28, 28))
            image = np.array(image).reshape(1, 28, 28, 1).astype('float32') / 255
            
            print("Processed Image Shape:", image.shape)  
            

            prediction = model.predict(image)
            print("Model Prediction:", prediction) 
            
            digit = np.argmax(prediction)
            return JsonResponse({'digit': int(digit)})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=400)
