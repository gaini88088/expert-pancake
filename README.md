# Expert Pancake - AI Collaboration System

A collaborative AI system that brings multiple AI agents together to handle email processing and secure online access management.

## Overview

This system demonstrates how multiple AI components can work together to:
- Process and manage multiple emails efficiently (up to 50 emails)
- Secure online access through authentication and authorization
- Coordinate between different AI agents for optimal task distribution

## Components

### 1. Email Handler AI (`email_handler.py`)
Processes and manages incoming emails, categorizes them, and routes them appropriately.

### 2. Security Manager AI (`security_manager.py`)
Handles authentication, authorization, and secure access management for online resources.

### 3. AI Coordinator (`ai_coordinator.py`)
Orchestrates the different AI components, ensuring they work together seamlessly.

## Installation

```bash
# Clone the repository
git clone https://github.com/gaini88088/expert-pancake.git
cd expert-pancake

# Install required dependencies
pip install -r requirements.txt
```

## Usage

```bash
# Run the AI coordination system
python ai_coordinator.py

# Process specific number of emails
python ai_coordinator.py --emails 50

# Enable security features
python ai_coordinator.py --secure-access
```

## Configuration

Edit `config.json` to customize:
- Maximum number of emails to process
- Security settings
- AI agent parameters

## License

This project is licensed under the GNU Affero General Public License v3.0 - see the LICENSE file for details.
