import streamlit as st
import random

st.set_page_config(page_title="🎯 Goal Suggestion App", layout="centered")

st.title("🎯 Goal Suggestion App")
st.write("Answer the following questions to get career suggestions based on your interests and hobbies.")

# Updated options list
category_options = [
    "",  # Blank default
    "Art", "Business", "Cooking", "Design", "Engineering", "Fashion", "Gaming",
    "Healthcare", "Investing", "Journalism", "Kindergarten Education", "Law",
    "Music", "Nature/Environment", "Online Marketing", "Psychology", "Quantum Science",
    "Research", "Sports", "Technology", "UX/UI", "Videography", "Writing",
    "XR/VR", "YouTube", "Zoology",
    "Physics", "Chemistry", "Mathematics", "Biology",
    "Coding", "Drawing", "Blogging", "Photography", "Reading", "Traveling",
    "Teaching", "Dancing", "Crafting", "Meditation", "Podcasting", "Baking",
    "None"  # Option to select nothing
]

# ✅ Working career map
career_map = {
    "Art": ["Illustrator", "Art Director", "Animator"],
    "Business": ["Business Analyst", "Entrepreneur", "Sales Manager"],
    "Cooking": ["Chef", "Food Blogger", "Nutritionist"],
    "Design": ["Graphic Designer", "Product Designer", "Interior Designer"],
    "Engineering": ["Mechanical Engineer", "Civil Engineer", "Software Engineer"],
    "Fashion": ["Fashion Designer", "Stylist", "Model"],
    "Gaming": ["Game Developer", "Game Tester", "Streamer"],
    "Healthcare": ["Doctor", "Nurse", "Physiotherapist"],
    "Investing": ["Stock Analyst", "Investment Banker", "Financial Advisor"],
    "Journalism": ["Reporter", "News Anchor", "Content Writer"],
    "Kindergarten Education": ["Preschool Teacher", "Childcare Worker"],
    "Law": ["Lawyer", "Legal Advisor", "Judge"],
    "Music": ["Musician", "Composer", "Music Teacher"],
    "Nature/Environment": ["Environmental Scientist", "Wildlife Biologist", "Conservationist"],
    "Online Marketing": ["Digital Marketer", "SEO Specialist", "Social Media Manager"],
    "Psychology": ["Psychologist", "Therapist", "Counselor"],
    "Quantum Science": ["Quantum Physicist", "Research Scientist"],
    "Research": ["Academic Researcher", "Data Scientist", "Lab Technician"],
    "Sports": ["Athlete", "Coach", "Fitness Trainer"],
    "Technology": ["Software Engineer", "IT Consultant", "AI Researcher"],
    "UX/UI": ["UX Designer", "UI Designer", "Interaction Designer"],
    "Videography": ["Videographer", "Film Editor", "Cinematographer"],
    "Writing": ["Author", "Copywriter", "Content Creator"],
    "XR/VR": ["AR/VR Developer", "Simulation Designer", "3D Modeler"],
    "YouTube": ["YouTuber", "Video Editor", "Vlogger"],
    "Zoology": ["Zoologist", "Wildlife Conservationist", "Animal Behaviorist"],
    "Physics": ["Physicist", "Astrophysicist", "Physics Professor"],
    "Chemistry": ["Chemist", "Pharmacologist", "Chemical Engineer"],
    "Mathematics": ["Mathematician", "Statistician", "Data Analyst"],
    "Biology": ["Biologist", "Geneticist", "Biotech Researcher"],
    "Coding": ["Software Developer", "Backend Engineer", "App Developer"],
    "Drawing": ["Illustrator", "Tattoo Artist", "Storyboard Artist"],
    "Blogging": ["Blogger", "Affiliate Marketer", "SEO Writer"],
    "Photography": ["Photographer", "Photojournalist", "Photo Editor"],
    "Reading": ["Editor", "Librarian", "Literature Professor"],
    "Traveling": ["Travel Blogger", "Tour Guide", "Pilot"],
    "Teaching": ["School Teacher", "Online Instructor", "Trainer"],
    "Dancing": ["Dancer", "Choreographer", "Dance Instructor"],
    "Crafting": ["Craft Artist", "DIY YouTuber", "Product Designer"],
    "Meditation": ["Mindfulness Coach", "Yoga Instructor", "Wellness Blogger"],
    "Podcasting": ["Podcaster", "Audio Engineer", "Radio Host"],
    "Baking": ["Baker", "Pastry Chef", "Food Photographer"]
}

# 20 Unique questions
questions = [
    "1. What is your favorite hobby?",
    "2. How do you usually spend your weekends?",
    "3. What subject do you enjoy the most in school?",
    "4. Which activity makes you lose track of time?",
    "5. What do your friends usually ask your help for?",
    "6. If you could master one skill instantly, what would it be?",
    "7. What kind of YouTube content do you consume the most?",
    "8. If given a choice, which workshop would you attend?",
    "9. What do you enjoy doing during your free time?",
    "10. What do you usually score highest in at school or college?",
    "11. Which club would you join at college?",
    "12. What type of books or blogs do you read?",
    "13. What role do you enjoy in a group project?",
    "14. What excites you about the future?",
    "15. If you could intern anywhere, what field would you choose?",
    "16. What is one topic you can talk about for hours?",
    "17. What type of movies or shows do you prefer?",
    "18. Which elective would you pick if there were no limits?",
    "19. What kind of problems do you like solving?",
    "20. If you had to teach a class, what would it be about?"
]

user_answers = []

for i in range(20):
    answer = st.selectbox(
        questions[i],
        options=category_options,
        key=f"q{i}"
    )
    user_answers.append(answer)

# Suggest career paths
if st.button("✨ Suggest Career Paths"):
    selected_categories = [ans for ans in user_answers if ans and ans != "None"]
    
    if not selected_categories:
        st.warning("Please select at least one meaningful interest or hobby.")
    else:
        possible_careers = []
        for category in selected_categories:
            if category in career_map:
                possible_careers.extend(career_map[category])
        
        suggested_careers = list(set(possible_careers))
        if len(suggested_careers) > 5:
            suggested_careers = random.sample(suggested_careers, 5)

        st.subheader("🚀 Top Career Suggestions for You:")
        for career in suggested_careers:
            st.success(f"• {career}")