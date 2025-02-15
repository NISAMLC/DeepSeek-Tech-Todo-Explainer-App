import streamlit as st
import ollama

# Initialize the Ollama client
client = ollama.Client()

# Define the model
model = "deepseek-r1"  # Replace with your model name

# Streamlit app
def main():
    st.title("TechTodoMate")
    
    # Input for the task
    task = st.text_input("Enter your task: 💻")
    
    if st.button("Get How-To"):
        if task:
            # Generate a response from the model
            prompt = f"How to {task}?"
            response = client.generate(model=model, prompt=prompt)
            
            # Display the response
            st.write("**How to do it:**")
            st.write(response.response)
        else:
            st.warning("Please enter a task.")

if __name__ == "__main__":
    main()


