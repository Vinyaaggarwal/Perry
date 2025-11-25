# session_persistence.py
# Simple session persistence WITHOUT cookies - using file-based approach
# This provides persistent login and auto-save functionality

import streamlit as st
import json
from pathlib import Path
from datetime import datetime
from data_manager import load_user_data, save_user_data

# ============================================================================
# SESSION PERSISTENCE FILE
# ============================================================================

SESSION_FILE = Path("last_session.json")

def save_last_session(email):
    """Save the last logged-in user's email to file"""
    try:
        session_data = {
            'email': email,
            'timestamp': datetime.now().isoformat()
        }
        with open(SESSION_FILE, 'w') as f:
            json.dump(session_data, f)
        return True
    except Exception as e:
        print(f"Error saving session: {str(e)}")
        return False

def load_last_session():
    """Load the last session if it exists"""
    try:
        if not SESSION_FILE.exists():
            return None
        
        with open(SESSION_FILE, 'r') as f:
            session_data = json.load(f)
        
        # Return email if session exists
        return session_data.get('email')
    except Exception as e:
        print(f"Error loading session: {str(e)}")
        return None

def clear_last_session():
    """Clear the saved session"""
    try:
        if SESSION_FILE.exists():
            SESSION_FILE.unlink()
        return True
    except Exception as e:
        print(f"Error clearing session: {str(e)}")
        return False

# ============================================================================
# AUTO-RESTORE SESSION
# ============================================================================

def auto_restore_session():
    """
    Automatically restore user session if they were recently logged in
    Call this early in app2.py before showing auth page
    """
    # Don't auto-restore if already authenticated
    if st.session_state.get('authenticated', False):
        return False
    
    # Check for last session
    last_email = load_last_session()
    if not last_email:
        return False
    
    # Verify user still exists
    from auth import load_users
    users = load_users()
    if last_email not in users:
        clear_last_session()
        return False
    
    # Restore session
    try:
        st.session_state.authenticated = True
        st.session_state.user_email = last_email
        st.session_state.user_data = users[last_email]
        
        # Load user's data
        load_user_data(last_email)
        
        print(f"✅ Auto-restored session for {last_email}")
        return True
    except Exception as e:
        print(f"Error auto-restoring session: {str(e)}")
        clear_last_session()
        return False

# ============================================================================
# AUTO-SAVE FUNCTIONALITY
# ============================================================================

def setup_autosave():
    """Setup periodic auto-save (call this in sidebar or main area)"""
    if not st.session_state.get('authenticated', False):
        return
    
    # Initialize last save timestamp
    if 'last_autosave' not in st.session_state:
        st.session_state.last_autosave = datetime.now()
    
    # Auto-save every 30 seconds if data has changed
    current_time = datetime.now()
    time_since_save = (current_time - st.session_state.last_autosave).total_seconds()
    
    # Save every 30 seconds
    if time_since_save > 30:
        user_email = st.session_state.get('user_email')
        if user_email:
            try:
                if save_user_data(user_email):
                    st.session_state.last_autosave = current_time
                    # Silently auto-save in background
            except Exception as e:
                print(f"Auto-save error: {str(e)}")

def trigger_manual_save(action=""):
    """Trigger an immediate save after a user action"""
    if not st.session_state.get('authenticated', False):
        return False
    
    user_email = st.session_state.get('user_email')
    if not user_email:
        return False
    
    try:
        if save_user_data(user_email):
            st.session_state.last_autosave = datetime.now()
            if action:
                print(f"✅ Saved after: {action}")
            return True
    except Exception as e:
        print(f"Save error: {str(e)}")
    
    return False
