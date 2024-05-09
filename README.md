# SoulMegal

SoulMegal is a unique application that connects users based on shared interests, preferences, and past interactions. It aims to facilitate meaningful conversations and foster connections between like-minded individuals.

## 📌 Features

- **Interests**:
  - Sports 🏀⚽️🎾
  - Music 🎵🎸🎶
  - Movies 🎥🍿🎬
  - Technology 💻📱🔧
  - Literature 📚✒️📖
  - Hobbies 📷🍳🎮🌱🎨

- **Preferences**:
  - Conversation topics 🗣️🌍🍲💻
  - Communication style 💬😄🤓
  - Interaction frequency ⏰📆

- **Demographics**:
  - Age 🎂
  - Gender ♀️♂️⚧️
  - Location 🌎📍
  - Occupation 💼👩‍💻👨‍🔬

- **Past Interaction History**:
  - Previous connections 🔗
  - Conversation duration ⏱️
  - Shared topics 💬🔁
  - User ratings ⭐👍👎

- **Personal Preferences**:
  - Privacy settings 🔒
  - Notification preferences 🔔📧📱

- **Social Media Integration**:
  - Facebook Likes 👍📘
  - Twitter Interests #️⃣🐦
  - Instagram Preferences 📷📹📸

## 🚀 Getting Started

To get started with SoulMegal, follow these steps:
1. Clone the repository.
```bash
  git clone https://github.com/KinhaNisha/Internship-project-Systemic-Altruism.git
```
2. Install dependencies.
```bash
  pip install numpy flask scikit-learn
```
3. Run the application.

```bash
  python .\app.py
```

## 📝 Usage

SoulMegal allows users to:
- Sign up and create a profile.
- Specify interests, preferences, and demographics.
- Connect with like-minded individuals based on shared characteristics.
- routes [method: post]
  ```bash
     http://localhost:5000/match  
  ```
  ```bash
     http://localhost:5000/match/k-nearest
  ```
- body
  ```bash
    {
      "id": 12,
      "name": "Alice",
      "age": 25,
      "gender": "Female",
      "location": "New York, USA",
      "occupation": "Software Engineer",
      "interests": {
          "sports": ["basketball", "tennis"],
          "music": ["pop", "rock"],
          "movies": ["comedy", "drama"],
          "technology": ["programming", "gadgets"],
          "literature": ["fiction", "mystery"],
          "hobbies": ["photography", "gaming"]
      },
      "preferences": {
          "conversation_topics": ["technology trends", "travel"],
          "communication_style": "casual",
          "interaction_frequency": "daily"
      },
      "past_interaction_history": {
          "previous_connections": [2, 3],
          "conversation_duration": "30 minutes",
          "shared_topics": ["music", "movies"],
          "user_ratings": {
          "positive": 4,
          "negative": 1
          }
      },
      "personal_preferences": {
          "privacy_settings": {
          "hide_location": false,
          "hide_age": false
          },
          "notification_preferences": "email"
      },
      "social_media_integration": {
          "facebook_likes": ["TechCrunch", "NY Times"],
          "twitter_interests": ["#programming", "#photography"],
          "instagram_preferences": ["photos", "stories"]
      }
  }
```
- Engage in meaningful conversations through video chat.
- Provide feedback on past interactions to improve matching.
