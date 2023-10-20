
from django.shortcuts import render
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import QnA

def chatbot_view(request):
    user_input = request.GET.get('user_input', '')

    if not user_input:
        response = "Please enter a question."
    else:
        # Retrieve predefined questions and answers from the database
        qna_objects = QnA.objects.all()
        questions = [obj.question for obj in qna_objects]
        answers = [obj.answer for obj in qna_objects]

        # Create TF-IDF vectors for user input and predefined questions
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform([user_input] + questions)

        # Calculate cosine similarity between user input and predefined questions
        similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])

        most_similar_index = similarities.argmax()

        # Use the response as a single string
        response = answers[most_similar_index]

    return render(request, 'chatbot.html', {'user_input': user_input, 'response': response})
