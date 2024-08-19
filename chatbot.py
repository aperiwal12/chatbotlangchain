import openai
import langchain
import os
from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import ConversationChain
from flask import Flask, request, jsonify, render_template

# Load environment variables from .env file
load_dotenv()
app = Flask(__name__)


# Now you can access the variables using os.environ
openai_api_key = os.getenv('OPENAI_API_KEY')

llm = OpenAI(temperature=0.7)

# Initialize the conversation chain
conversation = ConversationChain(llm=llm)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    response = conversation.run(user_input)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
    
    
