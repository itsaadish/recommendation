import logging

logger = logging.getLogger(__name__)

def get_recommendations(current_article, user_profile, reading_history,article_database, n_recommendations=5):
    """Get recommendations based on sports and entities"""
    try:
        current_article_data = article_database[current_article]
        print("article database",article_database)
        print("current article",current_article_data)
        scored_articles = []
        for article_url, article_data in article_database.items():
            if article_url == current_article:
                continue
            
            score = 0
            
            # Prefer articles with the same sport or entity as the current article
            if article_data['sport'] == current_article_data['sport']:
                score += 0.3
            if article_data['entity'] == current_article_data['entity']:
                score += 0.3
            
            # Prefer articles matching user's top sport and entity
            if article_data['sport'] == user_profile['top_sport']:
                score += 0.2
            if article_data['entity'] == user_profile['top_entity']:
                score += 0.2
            
            # Reduce score for recently read articles
            if article_url == reading_history['latest_article_read']:
                score -= 0.5
            elif article_data['sport'] == reading_history['latest_sport_read']:
                score -= 0.1
            elif article_data['entity'] == reading_history['latest_entity_read']:
                score -= 0.1
            
            scored_articles.append((article_url, score))
        
        scored_articles.sort(key=lambda x: x[1], reverse=True)
        
        return [article[0] for article in scored_articles[:n_recommendations]]
    
    except Exception as e:
        logger.error(f"Error in get_recommendations: {str(e)}")
        return []