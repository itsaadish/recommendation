from data_loader import get_user_data

def get_user_profile(user_id):
    """Get user profile from the CSV data"""
    user_data = get_user_data(user_id)
    return {
        'top_sport': user_data['top_sport'],
        'top_entity': user_data['top_entity'],
        'no_of_sports_interested': user_data['no_of_sports_interested'],
        'no_of_entity_interested': user_data['no_of_entity_interested'],
        'sports_interested': [user_data['top_sport']],  # We only have top_sport in the data
        'entities_interested': [user_data['top_entity']]  # We only have top_entity in the data
    }

def get_reading_history(user_id):
    """Get reading history from the CSV data"""
    user_data = get_user_data(user_id)
    return {
        'latest_article_read': user_data['latest_article_read'],
        'latest_sport_read': user_data['latest_sport_read'],
        'latest_entity_read': user_data['latest_entity_read'],
        'articles_read_last_30_days': user_data['articles_read_last_30_days'],
        'total_engagement': user_data['total_engagement']
    }