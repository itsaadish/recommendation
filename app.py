
from flask import Flask, request, jsonify,render_template
import logging
from data_loader import load_data, get_article_database, get_article_urls, get_cosine_sim
from user_profile import get_user_profile, get_reading_history
from recommender import get_recommendations

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        data = request.json
        user_id = data['user_id']
        current_article = data['current_article']
        
        user_profile = get_user_profile(user_id)
        reading_history = get_reading_history(user_id)
        
        article_database = get_article_database()
        article_urls = get_article_urls()
        cosine_sim = get_cosine_sim()
        
        recommendations = get_recommendations(current_article, user_profile, reading_history, 
                                              article_database)
        
        return jsonify({'recommendations': recommendations})
    
    except Exception as e:
        logger.error(f"Error in recommend endpoint: {str(e)}")
        return jsonify({'error': 'An error occurred while processing your request'}), 500

if __name__ == '__main__':
    load_data()
    app.run(debug=True)