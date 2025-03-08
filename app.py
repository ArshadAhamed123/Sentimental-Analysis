import gradio as gr
from transformers import pipeline

# Load sentiment analysis model
sentiment_pipeline = pipeline("sentiment-analysis")

# Function to analyze sentiment
def analyze_sentiment(text):
    result = sentiment_pipeline(text)
    label = result[0]['label']
    confidence = result[0]['score']
    return f"Sentiment: {label} (Confidence: {confidence:.2f})"

# Create Gradio interface
iface = gr.Interface(
    fn=analyze_sentiment,
    inputs=gr.Textbox(placeholder="Enter text here..."),
    outputs="text",
    title="Sentiment Analysis",
    description="Enter text to analyze its sentiment (Positive/Negative)."
)

# Launch the app
iface.launch()
