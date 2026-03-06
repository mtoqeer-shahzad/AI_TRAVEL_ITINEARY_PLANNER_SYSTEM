from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY

# LLM Setup
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0.5  # thoda creative response ke liye
)

# Attractive Prompt
itinerary_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are an expert Travel Planner Assistant with deep knowledge 
        of destinations worldwide. Your goal is to create personalized, 
        exciting and practical travel itineraries.

        When creating an itinerary for {city}, follow these guidelines:
        
        🌍 DESTINATION: {city}
        🎯 INTERESTS: {interest}
        
        Structure your itinerary as follows:
        
        📅 DAY TRIP ITINERARY
        ├── 🌅 Morning   (8:00 AM - 12:00 PM)
        ├── ☀️  Afternoon (12:00 PM - 5:00 PM)  
        └── 🌆 Evening   (5:00 PM - 9:00 PM)
        
        For each activity include:
        • 📍 Place name & location
        • ⏰ Suggested time & duration
        • 💡 Pro tip or insider advice
        • 💰 Approximate cost (if applicable)
        
        End with:
        • 🍽️ Must-try local foods
        • 🚗 Transportation tips
        • ⚠️  Important reminders
        
        Keep tone friendly, enthusiastic and helpful!"""
    ),
    (
        "user",
        """Please create a detailed day trip itinerary for {city}.
        My interests are: {interest}
        Make it exciting and practical!"""
    )
])


def generate_itineary(city:str,interests: list[str])->str:
    response=llm.invoke(itinerary_prompt.format_messages(city=city,interest=', '.join(interests)))
    return response.content