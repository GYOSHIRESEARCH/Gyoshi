# Gyoshi: Endless AI Conversations in Dynamic Environments

Gyoshi is an experimental AI project that simulates perpetual conversations between two distinct entities, **Pepe the Frog** and **Jack**, within a dynamically generated virtual environment. These entities interact with their surroundings and adapt their dialogue based on the room's context, temperature, and object states.

---

## **Table of Contents**
- [Introduction](#introduction)
- [Features](#features)
- [Architecture](#architecture)
  - [Room Simulation Infrastructure](#room-simulation-infrastructure)
  - [Conversational AI](#conversational-ai)
  - [Environment Awareness](#environment-awareness)
  - [Endless Conversation Logic](#endless-conversation-logic)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Future Enhancements](#future-enhancements)
- [License](#license)


![FvN4HR-XwAAd6WI](https://github.com/user-attachments/assets/ca9133cc-6551-4187-bf9e-4cf319800656)
---

## **Introduction**
Gyoshi combines advanced conversational AI with immersive environmental simulation. The goal is to:
1. Simulate endless, meaningful conversations.
2. Leverage a dynamic environment where entities react to changes.
3. Push the boundaries of interaction between AI and virtual worlds.

---

## **Features**
- **Dynamic Environment**: Fully customizable room settings with furniture, paintings, and temperature.
- **Distinct Personalities**: Pepe and Jack have unique conversational tones and behaviors.
- **Context-Aware Dialogue**: Conversations are influenced by the environment.
- **Endless Interactions**: Continuously generated conversations with topic switching.

---

## **Architecture**
### **Room Simulation Infrastructure**
The virtual environment is generated with dynamic metadata that entities can interact with.

#### Example: Room Metadata in JSON
```json
{
  "room_name": "Gyoshi's Living Room",
  "temperature": 22,
  "objects": [
    {"name": "Sofa", "material": "leather", "position": [1, 0, 0]},
    {"name": "Painting", "theme": "abstract", "position": [0, 2, 1]}
  ]
}
```

Technologies:
- **3D Rendering**: Unity3D/Unreal Engine
- **Environment API**: Python libraries like `pybullet`
- **Databases**: MongoDB for object state storage

---

### **Conversational AI**
We use pre-trained language models (e.g., OpenAI GPT or HuggingFace Transformers) to generate dialogue with fine-tuned personalities for Pepe and Jack.

#### Example: Generating Dialogue
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt-neo-2.7B")
model = AutoModelForCausalLM.from_pretrained("gpt-neo-2.7B")

# Generate a response
pepe_prompt = "Pepe: This room feels a bit chilly."
jack_prompt = "Jack: I agree, let me turn up the thermostat."
input_text = f"{pepe_prompt}\n{jack_prompt}\n"
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model.generate(inputs['input_ids'], max_length=50)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

### **Environment Awareness**
Entities sense and react to their environment. For example, room temperature, lighting, or object positions influence dialogue.

#### Example: Room State Access
```python
# Access room state dynamically
def get_room_state():
    return {
        "temperature": 22,
        "lighting": "dim",
        "objects": ["sofa", "table", "painting"]
    }

# Pepe reacts to room state
room_state = get_room_state()
pepe_response = f"The temperature is {room_state['temperature']}°C. Is it always this warm here?"
```

---

### **Endless Conversation Logic**
Conversations are continuous, with context retention and topic-switching mechanisms.

#### Example: Endless Dialogue Loop
```python
conversation_history = []

while True:
    # Use the last 2 exchanges as context
    input_text = " ".join(conversation_history[-2:])
    inputs = tokenizer(input_text, return_tensors="pt")
    outputs = model.generate(inputs['input_ids'], max_length=50)

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    conversation_history.append(response)
    print(response)
```

---

## **Technologies Used**
- **AI Models**: GPT-Neo, GPT-3, or HuggingFace Transformers
- **Environment Simulation**: Unity3D, Unreal Engine, or PyBullet
- **Backend**: Python, Flask
- **Databases**: MongoDB
- **Deployment**: Docker, AWS/GCP

---

## **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gyoshi.git
   cd gyoshi
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the project:
   ```bash
   python app.py
   ```

---

## **Usage**
1. Define your room settings in `room_config.json`.
2. Run the simulation:
   ```bash
   python simulate.py
   ```
3. Watch Pepe and Jack interact!

---

## **Future Enhancements**
- **Emotion Simulation**: Inject emotional tone into conversations.
- **Multilingual Support**: Enable conversations in multiple languages.
- **Visual Room Representation**: Integrate with Unity3D for a 3D view.

---

## **License**
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

### **Contributions**
We welcome contributions! Feel free to fork the repo and submit pull requests.

---

For questions or suggestions, please contact us at: gyoshiresearch@gmail.com.
