from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import random

# Loading models
with open('safety_model.pkl', 'rb') as f:
    safety_model = pickle.load(f)
with open('category_model.pkl', 'rb') as f:
    category_model = pickle.load(f)

app = FastAPI(
    title="SafeSpace Agent Prototype",
    description="An agentic AI moderator that guides children towards positive storytelling."
)

class TextReuqest(BaseModel):
    text: str

def get_suggestion(category):
    """
    This simple rule-based logic mimics an 'Agent' providing feedback.
    In a real app, this would be an LLM call.
    """
    suggestions = {
        "Violence": ["Try using words like 'helped' or 'rescued' instead.", "How can they solve this without fighting?"],
        "Scary Theme": ["Maybe the ghost is actually friendly?", "Let's make it s funny mystery instead."],
        "Bullying": ["What if they complimented each other instead?", "Friends treat each other with kindness."],
        "Sexual": ["Let's stick to stories about adventures and friends.", "That topic isn't right for this story."]
    }
    return random.choice(suggestions.get(category, ["Let's try a different topic."]))

@app.post("/analyze")
def analyze_content(request: TextReuqest):
    text = request.text

    #Predict Safety
    is_unsafe = safety_model.predict([text])[0] # 1 = Unsafe and 0 = Safe

    response = {
        "text": text,
        "is_safe": bool(is_unsafe == 0),
        "confidence_score": float(max(safety_model.predict_proba([text])[0]))
    }

    if is_unsafe:
        # Predicting why it is unsafe
        category = category_model.predict([text])[0]
        response["flagged_categoyr"] = category

        # Adding the "Agentic" suggestions
        response["agent_suggestion"] = get_suggestion(category)
        response["message"] = f"Hold on! This looks a bit too {category.lower()}. {response['agent_suggestion']}"
    else:
        response["message"] = "Great job! This story is safe and ready to go!"

    return response