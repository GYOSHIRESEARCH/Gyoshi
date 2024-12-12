import random

# Markov Chain-like Conversation Logic
class ConversationEngine:
    def __init__(self):
        self.transitions = {
            "start": ["philosophy", "technology", "humor"],
            "philosophy": ["What is consciousness?", "Is reality subjective?", "How do we define existence?"],
            "technology": ["What are the ethical implications of AI?", "How will quantum computing evolve?", "Is cybersecurity truly secure?"],
            "humor": ["Why don’t skeletons fight each other? They don’t have the guts!", "I told a joke about AI, but it didn't process.", "Knock knock! Who’s there? Artificial. Artificial who? Artificial Intelligence."]
        }
        self.current_topic = "start"
    
    def get_next_topic(self):
        return random.choice(self.transitions[self.current_topic])
    
    def switch_topic(self):
        self.current_topic = random.choice(list(self.transitions.keys()))
        return f"Switching topic to {self.current_topic}."

    def generate_response(self, user_input):
        # Use the current topic to guide response generation
        if user_input.lower() in ["switch", "change topic"]:
            return self.switch_topic()
        else:
            return f"{random.choice(self.transitions[self.current_topic])}"

# Simulate Endless Conversation
def endless_conversation():
    engine = ConversationEngine()
    print("Starting Endless Conversation. Type 'switch' to change topics or 'exit' to stop.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Ending conversation. Goodbye!")
            break
        response = engine.generate_response(user_input)
        print(f"Pepe & Jack: {response}")

if __name__ == "__main__":
    endless_conversation()
