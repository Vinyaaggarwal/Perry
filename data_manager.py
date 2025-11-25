# data_manager.py
# User Data Persistence Manager
# Handles saving and loading all user data to/from JSON files

import json
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional
import streamlit as st

# ============================================================================
# CONFIGURATION
# ============================================================================

USER_DATA_DIR = "user_data"

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def ensure_user_data_directory():
    """Create user_data directory if it doesn't exist"""
    Path(USER_DATA_DIR).mkdir(exist_ok=True)

def get_user_data_path(email: str) -> Path:
    """Get the path to a user's data file"""
    ensure_user_data_directory()
    # Sanitize email for filename
    safe_email = email.replace('@', '_at_').replace('.', '_')
    return Path(USER_DATA_DIR) / f"{safe_email}.json"

def datetime_serializer(obj):
    """JSON serializer for datetime objects"""
    if isinstance(obj, datetime):
        return obj.strftime('%Y-%m-%d %H:%M:%S')
    raise TypeError(f"Type {type(obj)} not serializable")

def parse_datetime(date_str: str) -> datetime:
    """Parse datetime string back to datetime object"""
    try:
        return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
    except:
        return datetime.now()

# ============================================================================
# DATA STRUCTURE INITIALIZATION
# ============================================================================

def get_empty_user_data(email: str) -> Dict[str, Any]:
    """Get empty user data structure"""
    return {
        'email': email,
        'last_saved': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'emotion_history': [],
        'focus_sessions': [],
        'schedules': [],
        'notifications': [],
        'image_emotions': [],
        'preferences': {
            'dark_mode': False,
            'current_page': '🏠 Dashboard Overview'
        },
        'perry_chat_history': [],
        'perry_sentiment_logs': [],
        'analysis_count': 0,
        'blocked_sites_custom': []
    }

# ============================================================================
# SAVE USER DATA
# ============================================================================

def save_user_data(email: str) -> bool:
    """
    Save all user data from session state to JSON file
    
    Args:
        email: User's email address
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Get user data path
        data_path = get_user_data_path(email)
        
        # Collect data from session state
        user_data = {
            'email': email,
            'last_saved': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'emotion_history': [],
            'focus_sessions': [],
            'schedules': [],
            'notifications': [],
            'image_emotions': [],
            'preferences': {},
            'perry_chat_history': [],
            'perry_sentiment_logs': [],
            'analysis_count': 0,
            'blocked_sites_custom': []
        }
        
        # Save emotion history (convert datetime objects)
        if 'emotion_history' in st.session_state:
            emotion_history = []
            for entry in st.session_state.emotion_history:
                entry_copy = entry.copy()
                if 'timestamp' in entry_copy and isinstance(entry_copy['timestamp'], datetime):
                    entry_copy['timestamp'] = entry_copy['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
                emotion_history.append(entry_copy)
            user_data['emotion_history'] = emotion_history
        
        # Save focus sessions (convert datetime objects)
        if 'focus_sessions' in st.session_state:
            sessions = []
            for session in st.session_state.focus_sessions:
                session_copy = session.copy()
                if 'date' in session_copy and isinstance(session_copy['date'], datetime):
                    session_copy['date'] = session_copy['date'].strftime('%Y-%m-%d %H:%M:%S')
                if 'start_time' in session_copy and isinstance(session_copy['start_time'], datetime):
                    session_copy['start_time'] = session_copy['start_time'].strftime('%Y-%m-%d %H:%M:%S')
                if 'end_time' in session_copy and isinstance(session_copy['end_time'], datetime):
                    session_copy['end_time'] = session_copy['end_time'].strftime('%Y-%m-%d %H:%M:%S')
                sessions.append(session_copy)
            user_data['focus_sessions'] = sessions
        
        # Save schedules (convert datetime and date objects)
        if 'schedules' in st.session_state:
            schedules = []
            for schedule in st.session_state.schedules:
                schedule_copy = schedule.copy()
                # Convert date object to string
                if 'date' in schedule_copy:
                    if hasattr(schedule_copy['date'], 'strftime'):
                        schedule_copy['date'] = schedule_copy['date'].strftime('%Y-%m-%d')
                # Convert datetime objects to strings
                if 'created_at' in schedule_copy and isinstance(schedule_copy['created_at'], datetime):
                    schedule_copy['created_at'] = schedule_copy['created_at'].strftime('%Y-%m-%d %H:%M:%S')
                # Convert time objects to strings
                if 'start_time' in schedule_copy:
                    if hasattr(schedule_copy['start_time'], 'strftime'):
                        schedule_copy['start_time'] = schedule_copy['start_time'].strftime('%H:%M:%S')
                if 'end_time' in schedule_copy:
                    if hasattr(schedule_copy['end_time'], 'strftime'):
                        schedule_copy['end_time'] = schedule_copy['end_time'].strftime('%H:%M:%S')
                schedules.append(schedule_copy)
            user_data['schedules'] = schedules
        
        # Save notifications
        if 'notifications' in st.session_state:
            notifications = []
            for notif in st.session_state.notifications:
                notif_copy = notif.copy()
                if 'timestamp' in notif_copy and isinstance(notif_copy['timestamp'], datetime):
                    notif_copy['timestamp'] = notif_copy['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
                notifications.append(notif_copy)
            user_data['notifications'] = notifications
        
        # Save image emotions
        if 'image_emotions' in st.session_state:
            image_emotions = []
            for emotion in st.session_state.image_emotions:
                emotion_copy = emotion.copy()
                if 'timestamp' in emotion_copy and isinstance(emotion_copy['timestamp'], datetime):
                    emotion_copy['timestamp'] = emotion_copy['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
                image_emotions.append(emotion_copy)
            user_data['image_emotions'] = image_emotions
        
        # Save preferences
        user_data['preferences'] = {
            'dark_mode': st.session_state.get('dark_mode', False),
            'current_page': st.session_state.get('current_page', '🏠 Dashboard Overview')
        }
        
        # Save Perry chat history
        if 'perry_chat_history' in st.session_state:
            user_data['perry_chat_history'] = st.session_state.perry_chat_history
        
        # Save Perry sentiment logs
        if 'perry_sentiment_logs' in st.session_state:
            sentiment_logs = []
            for log in st.session_state.perry_sentiment_logs:
                log_copy = log.copy()
                if 'timestamp' in log_copy and isinstance(log_copy['timestamp'], datetime):
                    log_copy['timestamp'] = log_copy['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
                sentiment_logs.append(log_copy)
            user_data['perry_sentiment_logs'] = sentiment_logs
        
        # Save analysis count
        if 'analysis_count' in st.session_state:
            user_data['analysis_count'] = st.session_state.analysis_count
        
        # Save custom blocked sites
        if 'website_blocker' in st.session_state:
            blocker = st.session_state.website_blocker
            if hasattr(blocker, 'blocked_sites'):
                user_data['blocked_sites_custom'] = list(blocker.blocked_sites)
        
        # Write to JSON file
        with open(data_path, 'w', encoding='utf-8') as f:
            json.dump(user_data, f, indent=4, ensure_ascii=False, default=datetime_serializer)
        
        print(f"✅ User data saved successfully to {data_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error saving user data: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

# ============================================================================
# LOAD USER DATA
# ============================================================================

def load_user_data(email: str) -> bool:
    """
    Load user data from JSON file into session state
    
    Args:
        email: User's email address
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        data_path = get_user_data_path(email)
        
        # Check if file exists
        if not data_path.exists():
            print(f"ℹ️ No existing data file for {email}, will create new one")
            initialize_user_data(email)
            return True
        
        # Load data from file
        with open(data_path, 'r', encoding='utf-8') as f:
            user_data = json.load(f)
        
        # Load emotion history (convert timestamp strings back to datetime)
        emotion_history = []
        for entry in user_data.get('emotion_history', []):
            entry_copy = entry.copy()
            if 'timestamp' in entry_copy and isinstance(entry_copy['timestamp'], str):
                entry_copy['timestamp'] = parse_datetime(entry_copy['timestamp'])
            emotion_history.append(entry_copy)
        st.session_state.emotion_history = emotion_history
        
        # Load focus sessions (convert datetime strings back)
        focus_sessions = []
        for session in user_data.get('focus_sessions', []):
            session_copy = session.copy()
            if 'date' in session_copy and isinstance(session_copy['date'], str):
                session_copy['date'] = parse_datetime(session_copy['date'])
            if 'start_time' in session_copy and isinstance(session_copy['start_time'], str):
                session_copy['start_time'] = parse_datetime(session_copy['start_time'])
            if 'end_time' in session_copy and isinstance(session_copy['end_time'], str):
                session_copy['end_time'] = parse_datetime(session_copy['end_time'])
            focus_sessions.append(session_copy)
        st.session_state.focus_sessions = focus_sessions
        
        # Load schedules (convert date and datetime strings back)
        from datetime import date, time
        schedules = []
        for schedule in user_data.get('schedules', []):
            schedule_copy = schedule.copy()
            # Convert date string back to date object
            if 'date' in schedule_copy and isinstance(schedule_copy['date'], str):
                try:
                    schedule_copy['date'] = datetime.strptime(schedule_copy['date'], '%Y-%m-%d').date()
                except:
                    schedule_copy['date'] = datetime.now().date()
            # Convert datetime strings back
            if 'created_at' in schedule_copy and isinstance(schedule_copy['created_at'], str):
                schedule_copy['created_at'] = parse_datetime(schedule_copy['created_at'])
            # Convert time strings back to time objects
            if 'start_time' in schedule_copy and isinstance(schedule_copy['start_time'], str):
                try:
                    schedule_copy['start_time'] = datetime.strptime(schedule_copy['start_time'], '%H:%M:%S').time()
                except:
                    schedule_copy['start_time'] = datetime.now().time()
            if 'end_time' in schedule_copy and isinstance(schedule_copy['end_time'], str):
                try:
                    schedule_copy['end_time'] = datetime.strptime(schedule_copy['end_time'], '%H:%M:%S').time()
                except:
                    schedule_copy['end_time'] = datetime.now().time()
            schedules.append(schedule_copy)
        st.session_state.schedules = schedules
        
        # Load notifications
        notifications = []
        for notif in user_data.get('notifications', []):
            notif_copy = notif.copy()
            if 'timestamp' in notif_copy and isinstance(notif_copy['timestamp'], str):
                notif_copy['timestamp'] = parse_datetime(notif_copy['timestamp'])
            notifications.append(notif_copy)
        st.session_state.notifications = notifications
        
        # Load image emotions
        image_emotions = []
        for emotion in user_data.get('image_emotions', []):
            emotion_copy = emotion.copy()
            if 'timestamp' in emotion_copy and isinstance(emotion_copy['timestamp'], str):
                emotion_copy['timestamp'] = parse_datetime(emotion_copy['timestamp'])
            image_emotions.append(emotion_copy)
        st.session_state.image_emotions = image_emotions
        
        # Load preferences
        preferences = user_data.get('preferences', {})
        st.session_state.dark_mode = preferences.get('dark_mode', False)
        st.session_state.current_page = preferences.get('current_page', '🏠 Dashboard Overview')
        
        # Load Perry chat history
        st.session_state.perry_chat_history = user_data.get('perry_chat_history', [])
        
        # Load Perry sentiment logs
        sentiment_logs = []
        for log in user_data.get('perry_sentiment_logs', []):
            log_copy = log.copy()
            if 'timestamp' in log_copy and isinstance(log_copy['timestamp'], str):
                log_copy['timestamp'] = parse_datetime(log_copy['timestamp'])
            sentiment_logs.append(log_copy)
        st.session_state.perry_sentiment_logs = sentiment_logs
        
        # Load analysis count
        st.session_state.analysis_count = user_data.get('analysis_count', 0)
        
        # Load custom blocked sites
        if 'website_blocker' in st.session_state:
            blocker = st.session_state.website_blocker
            custom_sites = user_data.get('blocked_sites_custom', [])
            if hasattr(blocker, 'blocked_sites'):
                blocker.blocked_sites.update(custom_sites)
        
        print(f"✅ User data loaded successfully from {data_path}")
        print(f"   - {len(st.session_state.emotion_history)} journal entries")
        print(f"   - {len(st.session_state.focus_sessions)} focus sessions")
        print(f"   - {len(st.session_state.schedules)} schedules")
        return True
        
    except Exception as e:
        print(f"❌ Error loading user data: {str(e)}")
        import traceback
        traceback.print_exc()
        # Initialize with empty data on error
        initialize_user_data(email)
        return False

# ============================================================================
# INITIALIZE USER DATA
# ============================================================================

def initialize_user_data(email: str) -> bool:
    """
    Initialize empty user data file for a new user
    
    Args:
        email: User's email address
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        data_path = get_user_data_path(email)
        
        # Create empty data structure
        user_data = get_empty_user_data(email)
        
        # Write to file
        with open(data_path, 'w', encoding='utf-8') as f:
            json.dump(user_data, f, indent=4, ensure_ascii=False)
        
        print(f"✅ Initialized empty data file for {email}")
        return True
        
    except Exception as e:
        print(f"❌ Error initializing user data: {str(e)}")
        return False

# ============================================================================
# DATA EXPORT/IMPORT
# ============================================================================

def export_user_data_json(email: str) -> Optional[str]:
    """
    Export user data as downloadable JSON string
    
    Args:
        email: User's email address
    
    Returns:
        str: JSON string of user data, or None if error
    """
    try:
        data_path = get_user_data_path(email)
        
        if not data_path.exists():
            return None
        
        with open(data_path, 'r', encoding='utf-8') as f:
            return f.read()
            
    except Exception as e:
        print(f"❌ Error exporting user data: {str(e)}")
        return None

def delete_user_data(email: str) -> bool:
    """
    Delete user's data file (for data clearing)
    
    Args:
        email: User's email address
    
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        data_path = get_user_data_path(email)
        
        if data_path.exists():
            data_path.unlink()
            print(f"✅ Deleted user data file for {email}")
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error deleting user data: {str(e)}")
        return False
