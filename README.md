# 🤖 Discord Server Management Bot

A feature-rich Discord bot built using **discord.py** that helps automate server management, moderation, logging, and GitHub integration. The bot provides a modular architecture using Discord Cogs, making it easy to extend and maintain.

## ✨ Features

### 🛡️ Moderation

* User moderation commands
* Automated moderation utilities
* Message management
* Server protection features

### 📜 Logging

* Join/Leave event logging
* Moderation action logging
* Server activity tracking

### 👋 Member Management

* Welcome messages
* Leave notifications
* Member event handling

### 📂 Channel Management

* Channel administration commands
* Embedded announcements
* Automated channel utilities

### 🧹 Message Management

* Bulk message deletion
* Chat cleanup commands

### 🔗 GitHub Integration

* GitHub repository utilities
* Repository monitoring support
* Developer-focused server tools

### 🎭 Dynamic Presence

The bot automatically cycles through status messages:

* Watching over the Server
* Pushing commits to Main
* Reading README.md

---

## 🏗️ Project Structure

```text
discord-bot/
│
├── main.py
│
├── cogs/
│   └── github.py
│
├── managements/
│   ├── auto_embed.py
│   ├── automod.py
│   ├── channels.py
│   ├── clear_msg.py
│   ├── database.py
│   ├── embedded.py
│   ├── join_leave.py
│   ├── loggingg.py
│   └── moderation.py
│  
├── sevices/
│   ├── caching.py
│   ├── database.py
│   ├── github_api.py
│
├── utils/
│   ├── embeds.py
│   ├── heatmap.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* Python
* discord.py
* asyncio
* python-dotenv
* SQLite

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd discord-bot
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

Linux / macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```env
MY_TOKEN=YOUR_DISCORD_BOT_TOKEN

GITHUB_TOKEN = YOUR_PERSONAL_GITHUB_TOKEN
```

---

## ▶️ Running the Bot

```bash
python main.py
```

If everything is configured correctly, you should see:

```text
logged in as BotName , yehehe
Slash Commands activated and synced
```

---

## 🔧 Required Discord Intents

The bot uses the following intents:

```python
discord.Intents.default()
intents.message_content = True
intents.members = True
```

Make sure these intents are enabled in the Discord Developer Portal.

---

## 📌 Commands

The bot uses Discord Slash Commands:

```text
/command-name
```

Commands are automatically synchronized on startup.

---

## 🔒 Security

Never commit your `.env` file or bot token.

Add the following to `.gitignore`:

```gitignore
.env
.vscode
__pycache__
*.db
.venv
```

---

## 🌱 Future Improvements

* Ticket system
* Role management system
* Music commands
* Dashboard website
* AI-powered moderation
* GitHub webhook integration
* Server analytics

---

## 👨‍💻 Author

**Harsh Shah**

