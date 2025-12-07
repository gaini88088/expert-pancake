#!/usr/bin/env python3
"""
Email Handler AI - Processes and manages email operations
Handles email categorization, processing, and response generation
"""

import json
import logging
from datetime import datetime
from typing import List, Dict, Optional


class EmailHandlerAI:
    """AI component for handling email operations"""
    
    def __init__(self, config: Dict):
        """Initialize the Email Handler AI with configuration"""
        self.config = config.get('email_handler', {})
        self.max_emails = self.config.get('max_emails', 50)
        self.batch_size = self.config.get('batch_size', 10)
        self.categories = self.config.get('categories', ['urgent', 'important', 'normal', 'low_priority'])
        self.auto_response = self.config.get('auto_response', True)
        self.processed_emails = []
        
        logging.info(f"Email Handler AI initialized - Max emails: {self.max_emails}")
    
    def categorize_email(self, email: Dict) -> str:
        """
        Categorize an email based on its content and metadata
        
        Args:
            email: Dictionary containing email data (subject, sender, content)
        
        Returns:
            Category string
        """
        subject = email.get('subject', '').lower()
        
        # Simple rule-based categorization
        if any(keyword in subject for keyword in ['urgent', 'asap', 'critical', 'emergency']):
            return 'urgent'
        elif any(keyword in subject for keyword in ['important', 'required', 'action needed']):
            return 'important'
        elif any(keyword in subject for keyword in ['fyi', 'update', 'notification']):
            return 'normal'
        else:
            return 'low_priority'
    
    def process_emails(self, emails: List[Dict]) -> List[Dict]:
        """
        Process a batch of emails
        
        Args:
            emails: List of email dictionaries
        
        Returns:
            List of processed email results
        """
        if len(emails) > self.max_emails:
            logging.warning(f"Email count ({len(emails)}) exceeds maximum ({self.max_emails}). Processing first {self.max_emails}.")
            emails = emails[:self.max_emails]
        
        results = []
        for i, email in enumerate(emails):
            category = self.categorize_email(email)
            
            processed = {
                'id': email.get('id', f'email_{i+1}'),
                'subject': email.get('subject', 'No Subject'),
                'sender': email.get('sender', 'Unknown'),
                'category': category,
                'processed_at': datetime.now().isoformat(),
                'status': 'processed'
            }
            
            if self.auto_response and category in ['urgent', 'important']:
                processed['auto_response_sent'] = True
                processed['response'] = self._generate_auto_response(email)
            
            results.append(processed)
            self.processed_emails.append(processed)
            
            logging.info(f"Processed email {i+1}/{len(emails)}: {email.get('subject', 'No Subject')} - Category: {category}")
        
        return results
    
    def _generate_auto_response(self, email: Dict) -> str:
        """Generate an automatic response for an email"""
        return f"Thank you for your email regarding '{email.get('subject', 'your message')}'. We have received it and will respond shortly."
    
    def get_statistics(self) -> Dict:
        """Get email processing statistics"""
        stats = {
            'total_processed': len(self.processed_emails),
            'by_category': {}
        }
        
        for category in self.categories:
            count = sum(1 for e in self.processed_emails if e['category'] == category)
            stats['by_category'][category] = count
        
        return stats
    
    def open_emails(self, count: int = 50) -> List[Dict]:
        """
        Simulate opening and retrieving multiple emails
        
        Args:
            count: Number of emails to open (default 50)
        
        Returns:
            List of simulated email data
        """
        count = min(count, self.max_emails)
        
        emails = []
        for i in range(count):
            email = {
                'id': f'email_{i+1}',
                'subject': f'Email Subject {i+1}',
                'sender': f'sender{i+1}@example.com',
                'content': f'This is the content of email {i+1}',
                'received_at': datetime.now().isoformat()
            }
            emails.append(email)
        
        logging.info(f"Opened {count} emails for processing")
        return emails


if __name__ == '__main__':
    # Example usage
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    with open('config.json', 'r') as f:
        config = json.load(f)
    
    handler = EmailHandlerAI(config)
    
    # Open and process 50 emails
    emails = handler.open_emails(50)
    results = handler.process_emails(emails)
    
    # Display statistics
    stats = handler.get_statistics()
    print("\nEmail Processing Statistics:")
    print(f"Total Processed: {stats['total_processed']}")
    print("\nBy Category:")
    for category, count in stats['by_category'].items():
        print(f"  {category}: {count}")
