#!/usr/bin/env python3
"""
Security Manager AI - Handles authentication and secure online access
Manages access control, authentication, and security protocols

NOTE: This is a demonstration implementation. For production use:
- Use proper password hashing (bcrypt, Argon2, scrypt) instead of SHA-256
- Implement actual credential validation against a secure database
- Use real 2FA code generation and validation (TOTP/HOTP)
- Never use hardcoded passwords or bypass authentication
"""

import json
import logging
import hashlib
import secrets
from datetime import datetime, timedelta
from typing import Dict, Optional, List


class SecurityManagerAI:
    """AI component for managing security and access control"""
    
    def __init__(self, config: Dict):
        """Initialize the Security Manager AI with configuration"""
        self.config = config.get('security_manager', {})
        self.enable_2fa = self.config.get('enable_2fa', True)
        self.session_timeout = self.config.get('session_timeout', 3600)
        self.encryption_enabled = self.config.get('encryption_enabled', True)
        self.access_levels = self.config.get('access_levels', ['admin', 'user', 'guest'])
        
        self.active_sessions = {}
        self.access_logs = []
        
        logging.info(f"Security Manager AI initialized - 2FA: {self.enable_2fa}, Encryption: {self.encryption_enabled}")
    
    def generate_session_token(self) -> str:
        """Generate a secure session token"""
        return secrets.token_urlsafe(32)
    
    def generate_2fa_code(self) -> str:
        """Generate a 6-digit 2FA code"""
        return str(secrets.randbelow(1000000)).zfill(6)
    
    def hash_password(self, password: str) -> str:
        """Hash a password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def authenticate_user(self, username: str, password: str, two_fa_code: Optional[str] = None) -> Dict:
        """
        Authenticate a user with optional 2FA
        
        Args:
            username: User's username
            password: User's password
            two_fa_code: Optional 2FA code
        
        Returns:
            Authentication result dictionary
        """
        # In a real system, this would check against a database
        # For demonstration, we'll simulate authentication
        
        auth_result = {
            'username': username,
            'authenticated': False,
            'session_token': None,
            'access_level': None,
            'timestamp': datetime.now().isoformat()
        }
        
        # Simulate password verification
        password_hash = self.hash_password(password)
        
        # For demo purposes, consider authentication successful
        auth_result['authenticated'] = True
        
        # Check 2FA if enabled
        if self.enable_2fa:
            if two_fa_code is None:
                auth_result['requires_2fa'] = True
                auth_result['authenticated'] = False
                logging.info(f"2FA required for user: {username}")
                return auth_result
            else:
                # Simulate 2FA verification
                auth_result['2fa_verified'] = True
        
        # Create session
        if auth_result['authenticated']:
            session_token = self.generate_session_token()
            auth_result['session_token'] = session_token
            auth_result['access_level'] = 'user'  # Default access level
            
            self.active_sessions[session_token] = {
                'username': username,
                'created_at': datetime.now(),
                'expires_at': datetime.now() + timedelta(seconds=self.session_timeout),
                'access_level': 'user'
            }
            
            logging.info(f"User {username} authenticated successfully")
        
        self._log_access_attempt(auth_result)
        return auth_result
    
    def secure_online_access(self, session_token: str, resource: str) -> Dict:
        """
        Secure access to an online resource
        
        Args:
            session_token: User's session token
            resource: Resource being accessed
        
        Returns:
            Access result dictionary
        """
        result = {
            'resource': resource,
            'access_granted': False,
            'reason': None,
            'timestamp': datetime.now().isoformat()
        }
        
        # Verify session
        session = self.active_sessions.get(session_token)
        
        if not session:
            result['reason'] = 'Invalid session token'
            logging.warning(f"Access denied - Invalid session token for resource: {resource}")
            return result
        
        # Check if session has expired
        if datetime.now() > session['expires_at']:
            result['reason'] = 'Session expired'
            del self.active_sessions[session_token]
            logging.warning(f"Access denied - Session expired for resource: {resource}")
            return result
        
        # Grant access
        result['access_granted'] = True
        result['access_level'] = session['access_level']
        result['username'] = session['username']
        
        logging.info(f"Access granted to {session['username']} for resource: {resource}")
        self._log_access_attempt(result)
        
        return result
    
    def enable_secure_access(self, resources: List[str]) -> Dict:
        """
        Enable secure access for multiple resources
        
        Args:
            resources: List of resources to secure
        
        Returns:
            Security setup result
        """
        result = {
            'resources_secured': len(resources),
            'encryption_enabled': self.encryption_enabled,
            '2fa_enabled': self.enable_2fa,
            'timestamp': datetime.now().isoformat(),
            'resources': []
        }
        
        for resource in resources:
            resource_security = {
                'resource': resource,
                'status': 'secured',
                'encryption': self.encryption_enabled,
                'access_control': True
            }
            result['resources'].append(resource_security)
            logging.info(f"Secured resource: {resource}")
        
        return result
    
    def _log_access_attempt(self, attempt: Dict):
        """Log an access attempt for audit purposes"""
        self.access_logs.append({
            **attempt,
            'logged_at': datetime.now().isoformat()
        })
    
    def get_security_status(self) -> Dict:
        """Get current security status"""
        return {
            'active_sessions': len(self.active_sessions),
            'total_access_logs': len(self.access_logs),
            '2fa_enabled': self.enable_2fa,
            'encryption_enabled': self.encryption_enabled,
            'session_timeout': self.session_timeout
        }
    
    def cleanup_expired_sessions(self):
        """Remove expired sessions"""
        current_time = datetime.now()
        expired_tokens = [
            token for token, session in self.active_sessions.items()
            if current_time > session['expires_at']
        ]
        
        for token in expired_tokens:
            del self.active_sessions[token]
            logging.info(f"Removed expired session")
        
        return len(expired_tokens)


if __name__ == '__main__':
    # Example usage
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    security = SecurityManagerAI(config)
    
    # Authenticate user
    print("\n=== Authentication Test ===")
    auth_result = security.authenticate_user('user@example.com', 'password123', '123456')
    print(f"Authentication successful: {auth_result['authenticated']}")
    
    if auth_result['authenticated']:
        session_token = auth_result['session_token']
        
        # Secure access test
        print("\n=== Secure Access Test ===")
        access_result = security.secure_online_access(session_token, 'email_system')
        print(f"Access granted: {access_result['access_granted']}")
        
        # Enable security for multiple resources
        print("\n=== Enable Security for Resources ===")
        resources = ['email_system', 'file_storage', 'user_dashboard']
        secure_result = security.enable_secure_access(resources)
        print(f"Resources secured: {secure_result['resources_secured']}")
    
    # Display security status
    print("\n=== Security Status ===")
    status = security.get_security_status()
    for key, value in status.items():
        print(f"{key}: {value}")
