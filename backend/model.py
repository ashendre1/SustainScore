from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel
import requests
from fastapi.responses import JSONResponse

app = FastAPI()

  # Expecting product details directly in the request payload

def get_response_from_api(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "qwen2.5:0.5b",
        "prompt": prompt,
        "stream": False
    }
    
    try:
        # Send the POST request to the external model API
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            result = response.json()
            return result.get('response', 'No response')
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"An error occurred: {e}"

@app.post("/score-product")
async def score_product(input_data:str=Body(...)):
    # Construct the prompt for scoring the product's environmental friendliness
    print("here")
    prompt = (
        f"Consider the input details: {input_data}. Based on this information, just provide a score between 1 to 10 based on how enviornment friendly the product is. the response should just be a number and no explanation is needed."
        
    )

    # Get response from the chatbot model
    chatbot_response = get_response_from_api(prompt)
    
    # Return the chatbot response as JSON
    return JSONResponse(
        status_code=200,
        content={"response": chatbot_response}
    )