from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Data for the web app - Fourth Grade English Lessons
unit_data = {
    "title": "Fourth Grade English Lessons",
    "version": "1.0",
    "grade_level": 4,
    "unit_number": 1,
    "unit_name": "Countries, Numbers & Chores",
    "carousels": [
        {
            "id": "carousel_1_vocabulary",
            "title": "Vocabulary Highlights",
            "icon": "🌍🔢🧺",
            "cards": [
                {
                    "id": "vocab_countries",
                    "title": "Countries and Nationalities 🌎",
                    "type": "list",
                    "items": [
                        "Great Britain",
                        "Spain",
                        "Canada",
                        "France",
                        "USA",
                        "Germany",
                        "Portugal",
                        "Egypt",
                        "Australia",
                        "Morocco",
                        "Italy",
                        "Japan"
                    ]
                },
                {
                    "id": "vocab_numbers",
                    "title": "Numbers 💯",
                    "type": "list",
                    "items": [
                        "fifty (50)",
                        "sixty (60)",
                        "seventy (70)",
                        "eighty (80)",
                        "ninety (90)",
                        "one hundred (100)",
                        "four hundred (400)",
                        "one thousand (1000)"
                    ]
                },
                {
                    "id": "vocab_chores",
                    "title": "Household Chores 🧹",
                    "type": "list",
                    "items": [
                        "👕 wash the clothes",
                        "🧽 mop the floor", 
                        "🍽️ wash the dishes",
                        "🔌 vacuum the carpet",
                        "👔 do the ironing",
                        "🪟 clean the glass",
                        "🧹 sweep the floor",
                        "🪴 water the plants"
                    ]
                }
            ]
        },
        {
            "id": "carousel_2_dialogues",
            "title": "Mini Dialogues",
            "icon": "💬",
            "cards": [
                {
                    "id": "dialogue_origin",
                    "title": "Where Are You From? ✈️",
                    "type": "dialogue",
                    "lines": [
                        {"speaker": "A", "text": "Excuse me. Are you from Japan?"},
                        {"speaker": "B", "text": "No, I'm not. I'm from Italy."},
                        {"speaker": "A", "text": "Oh, I see! My name is Emily. I'm from Great Britain."},
                        {"speaker": "B", "text": "Nice to meet you, Emily."}
                    ]
                },
                {
                    "id": "dialogue_age_name",
                    "title": "Asking About Age and Name 👧",
                    "type": "dialogue",
                    "lines": [
                        {"speaker": "A", "text": "Hi, is your name Margarita?"},
                        {"speaker": "B", "text": "Yes, it is!"},
                        {"speaker": "A", "text": "How old are you? Are you nine years old?"},
                        {"speaker": "B", "text": "No, I'm ten. How are you today?"},
                        {"speaker": "A", "text": "I'm fine, thanks!"}
                    ]
                },
                {
                    "id": "dialogue_park",
                    "title": "At the Park 🌳",
                    "type": "dialogue",
                    "lines": [
                        {"speaker": "A", "text": "Hi! Do you want to play on the swings?"},
                        {"speaker": "B", "text": "Yes! Let's go!"},
                        {"speaker": "A", "text": "After that, can we play football?"},
                        {"speaker": "B", "text": "Of course! I love football."}
                    ]
                },
                {
                    "id": "dialogue_food",
                    "title": "Favorite Food 🍕",
                    "type": "dialogue",
                    "lines": [
                        {"speaker": "A", "text": "What's your favorite food?"},
                        {"speaker": "B", "text": "I love pizza! What about you?"},
                        {"speaker": "A", "text": "I like spaghetti and ice cream."},
                        {"speaker": "B", "text": "Yum! Let's eat together sometime."}
                    ]
                }
            ]
        }
    ]
}

@app.route('/')
def index():
    return render_template('index.html', unit_data=unit_data)

@app.route('/vocabulary')
def vocabulary():
    vocab_carousel = next((carousel for carousel in unit_data['carousels'] if carousel['id'] == 'carousel_1_vocabulary'), None)
    return render_template('vocabulary.html', data=vocab_carousel, unit_data=unit_data)

@app.route('/dialogue-drills')
def dialogue_drills():
    dialogue_carousel = next((carousel for carousel in unit_data['carousels'] if carousel['id'] == 'carousel_2_dialogues'), None)
    return render_template('dialogue_drills.html', data=dialogue_carousel, unit_data=unit_data)

@app.route('/practice')
def practice():
    return render_template('practice.html', unit_data=unit_data)

@app.route('/api/unit-data')
def api_unit_data():
    return jsonify(unit_data)

if __name__ == '__main__':
    app.run(debug=False)