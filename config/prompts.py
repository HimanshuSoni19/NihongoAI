"""
Quiz prompts for different categories
"""

PROMPTS = {
    "Kanji Reading": {
        "icon": "📚",
        "description": "Test your ability to read basic kanji characters",
        "prompt": """Create a simple JLPT N5 kanji reading quiz with 4 questions. Make it VERY EASY for beginners.

Requirements:
1. Use only the most basic N5 kanji (本、人、日、月、火、水、木、金、土、一、二、三、四、五、六、七、八、九、十、百、千、万、円、年、学、生、先、school, student, etc.)
2. Each question shows ONE kanji in 「 」 brackets
3. Ask "What is the reading of 「X」?" in simple Japanese
4. Give 3 hiragana choices (A, B, C)
5. Use very short, simple sentences

Format (MUST follow exactly):
もんだい1: 「本」の　よみかたは　なんですか。
A) ほん
B) もと
C) ぽん

もんだい2: 「人」の　よみかたは　なんですか。
A) ひと
B) じん
C) にん

もんだい3: [similar format]
A) [choice]
B) [choice]
C) [choice]

もんだい4: [similar format]
A) [choice]
B) [choice]
C) [choice]

せいかい:
1) A
2) A
3) [letter]
4) [letter]

Write ONLY in Japanese hiragana and basic kanji. Keep it SIMPLE."""
    },
    
    "Vocabulary": {
        "icon": "💭",
        "description": "Learn and practice essential Japanese vocabulary",
        "prompt": """Create a simple JLPT N5 vocabulary quiz with 4 questions. Make it VERY EASY for beginners.

Requirements:
1. Use basic daily words (たべる、のむ、いく、くる、みる、etc.)
2. Each question has a simple sentence with one blank: ____
3. Questions should be about daily activities
4. Give 3 hiragana word choices (A, B, C)
5. Keep sentences very short (5-8 words maximum)

Format (MUST follow exactly):
もんだい1: わたしは　まいにち　がっこうに　____。
A) いきます
B) たべます
C) のみます

もんだい2: あさ　パンを　____。
A) いきます
B) たべます  
C) みます

もんだい3: [similar short sentence with ____]
A) [word]
B) [word]
C) [word]

もんだい4: [similar short sentence with ____]
A) [word]
B) [word]
C) [word]

せいかい:
1) A
2) B
3) [letter]
4) [letter]

Write ONLY in hiragana. Keep sentences SHORT and SIMPLE."""
    },
    
    "Particles": {
        "icon": "🔗",
        "description": "Master Japanese particles (は、が、を、に、で, etc.)",
        "prompt": """Create a simple JLPT N5 particle quiz with 4 questions. Make it VERY EASY for beginners.

Requirements:
1. Use only basic particles: は、が、を、に、で、と
2. Each question has ONE blank for a particle: ____
3. Very short sentences (4-6 words)
4. Give 3 particle choices (A, B, C)
5. Make it easy to understand

Format (MUST follow exactly):
もんだい1: わたし____ がくせいです。
A) は
B) を
C) に

もんだい2: ほん____ よみます。
A) は
B) が
C) を

もんだい3: [short sentence with ____]
A) [particle]
B) [particle]
C) [particle]

もんだい4: [short sentence with ____]
A) [particle]
B) [particle]
C) [particle]

せいかい:
1) A
2) C
3) [letter]
4) [letter]

Write ONLY in hiragana. Keep it VERY SIMPLE."""
    },
    
    "Verb Conjugation": {
        "icon": "🔄",
        "description": "Practice verb forms and conjugations",
        "prompt": """Create a simple JLPT N5 verb conjugation quiz with 4 questions. Make it VERY EASY for beginners.

Requirements:
1. Use basic verbs: たべる、のむ、いく、みる、する、くる
2. Ask for simple forms: ます-form, て-form, た-form, ない-form
3. Each question shows a verb and asks for its form
4. Give 3 choices (A, B, C)
5. Keep it very simple

Format (MUST follow exactly):
もんだい1: 「たべる」の　ます-form は　なんですか。
A) たべます
B) たべて
C) たべない

もんだい2: 「いく」の　て-form は　なんですか。
A) いきます
B) いって
C) いかない

もんだい3: 「みる」の　[form] は　なんですか。
A) [choice]
B) [choice]
C) [choice]

もんだい4: [verb]の　[form] は　なんですか。
A) [choice]
B) [choice]
C) [choice]

せいかい:
1) A
2) B
3) [letter]
4) [letter]

Write ONLY in hiragana. Keep it SIMPLE."""
    },
    
    "Basic Grammar": {
        "icon": "🏗️",
        "description": "Practice basic Japanese grammar patterns",
        "prompt": """Create a simple JLPT N5 grammar quiz with 4 questions. Make it VERY EASY for beginners.

Requirements:
1. Test basic patterns: です/じゃないです、ます/ません、adjectives
2. Each question is a simple sentence with a blank: ____
3. Very short, simple sentences
4. Give 3 choices (A, B, C)
5. Easy daily conversation topics

Format (MUST follow exactly):
もんだい1: これは　ペン____。
A) です
B) でした
C) じゃない

もんだい2: きのう　えいがを　____。
A) みます
B) みました
C) みません

もんだい3: [simple sentence with ____]
A) [choice]
B) [choice]
C) [choice]

もんだい4: [simple sentence with ____]
A) [choice]
B) [choice]
C) [choice]

せいかい:
1) A
2) B
3) [letter]
4) [letter]

Write ONLY in hiragana. Keep it VERY SIMPLE."""
    }
}