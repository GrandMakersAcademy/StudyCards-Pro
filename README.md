# StudyCards-Pro 🎓

**Advanced Flashcard Learning System with Intelligent Spaced Repetition**

A powerful, feature-rich desktop application designed for students, educators, and lifelong learners who want to master complex subjects through scientifically-proven spaced repetition techniques. Built with modern Python technologies and a beautiful dark-themed interface.

---

## 🌟 Why StudyCards-Pro?

StudyCards-Pro is not just another flashcard app—it's a comprehensive learning companion designed specifically for university and institute students who need to memorize large amounts of information efficiently and retain it long-term.

### Perfect For:
- 📚 **University Students**: Master formulas, theorems, definitions, and concepts across multiple subjects
- 🌍 **Language Learners**: Build vocabulary, grammar rules, and conversational phrases
- 🔬 **Science Students**: Remember chemical formulas, biological processes, physics equations
- 📅 **History Students**: Memorize dates, events, historical figures, and timelines
- 💼 **Professional Certification**: Prepare for exams and retain professional knowledge
- 🧠 **General Knowledge**: Learn anything that requires long-term retention

---

## ✨ Key Features

### 🧠 Intelligent Spaced Repetition Algorithm

Implements the **SuperMemo 2 (SM-2)** algorithm, the gold standard in spaced repetition systems:

- **Adaptive Scheduling**: Automatically calculates optimal review intervals based on your performance
- **Smart Difficulty Adjustment**: Cards you find difficult appear more frequently; easy cards less often
- **Progressive Intervals**: 1 day → 6 days → 2 weeks → 1 month → 2 months → and beyond
- **Ease Factor Tracking**: Each card maintains its own difficulty rating (1.3 to 2.5+)
- **Forgetting Curve Optimization**: Maximizes retention while minimizing study time

**How it works:**
- ✅ **Correct answer**: Interval increases exponentially (e.g., 1 → 6 → 15 → 37 days)
- ❌ **Incorrect answer**: Card resets to 1-day interval for reinforcement
- 🎯 **Quality ratings**: "Again", "Hard", "Good", "Easy" buttons fine-tune the algorithm

### 📚 Comprehensive Card Management

**Flexible Card Structure:**
- **Question/Answer Format**: Classic two-sided flashcard design
- **Rich Examples**: Add usage examples, context, or additional notes
- **Smart Tagging System**: Organize with unlimited custom tags
- **Category Organization**: Group cards by subject (Math, English, History, etc.)
- **Difficulty Levels**: Track and filter by card difficulty
- **Multimedia Support**: Text-based cards with formatting options

**Deck Organization:**
- Create unlimited decks for different subjects or topics
- Assign decks to color-coded categories
- View card count and due cards at a glance
- Search and filter across all decks
- Import/Export capabilities (CSV, JSON formats)

### 📊 Advanced Progress Tracking & Statistics

Stay motivated with detailed analytics:

- **Daily Progress Charts**: Visualize your study consistency over time
- **Success Rate Percentage**: Track improvement in retention and recall
- **Cards Due Today**: Always know what needs attention
- **Category Performance**: Compare progress across different subjects
- **Study Streak Counter**: Build consistent study habits
- **Mastery Levels**: See cards categorized as New, Learning, Young, or Mature
- **Difficulty Analysis**: Identify your most challenging cards
- **Study Time Tracking**: Monitor total time invested in learning
- **Weekly Activity Heatmap**: GitHub-style contribution graph for study sessions

### 🎨 Modern, Beautiful Interface

- **PySide6 (Qt6) Framework**: Native performance with cross-platform compatibility
- **qdarkstyle Dark Theme**: Easy on the eyes during long study sessions
- **Intuitive Navigation**: Tab-based interface (Decks, Study, Statistics)
- **Responsive Design**: Smooth animations and transitions
- **Keyboard Shortcuts**: Study efficiently without touching the mouse
- **High DPI Support**: Crisp display on modern high-resolution screens

### 🔄 Import/Export Capabilities

- **CSV Export**: Share decks or backup to spreadsheets
- **JSON Export**: Preserve all metadata and statistics
- **Bulk Import**: Quickly add hundreds of cards from external sources
- **Database Backup**: Automatic SQLite database protection

---

## 🚀 Installation & Setup

### Prerequisites

- **Python 3.8+** (Python 3.10+ recommended)
- **pip** package manager
- **Windows, macOS, or Linux**

### Step-by-Step Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GrandMakersAcademy/StudyCards-Pro.git
   cd StudyCards-Pro
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch the application:**
   ```bash
   python main.py
   ```

### First-Time Setup

When you first launch StudyCards-Pro:

1. The application creates a local SQLite database (`studycards.db`)
2. Default categories are automatically created (Mathematics, English, History, etc.)
3. Start creating decks and adding cards immediately!

---

## 📖 How to Use

### Creating Your First Deck

1. Navigate to the **Decks** tab
2. Click **"New Deck"** button
3. Enter deck name (e.g., "Calculus Formulas")
4. Select a category (e.g., "Mathematics")
5. Add optional description
6. Click **"Create"**

### Adding Flashcards

1. Select a deck from the list
2. Click **"Add Card"** button
3. Fill in the fields:
   - **Question**: What you want to learn (e.g., "Derivative of x²")
   - **Answer**: The correct response (e.g., "2x")
   - **Example** (optional): Additional context or usage example
   - **Tags** (optional): Comma-separated tags (e.g., "derivatives, calculus, basic")
4. Click **"Save Card"**

### Studying with Spaced Repetition

1. Go to the **Study** tab
2. Select a deck to study
3. Click **"Start Study Session"**
4. For each card:
   - Read the **question**
   - Try to recall the answer mentally
   - Click **"Show Answer"** to reveal
   - Rate your recall:
     - **Again (0)**: Didn't remember → Card resets to day 1
     - **Hard (3)**: Struggled to remember → Shorter interval
     - **Good (4)**: Remembered correctly → Standard interval
     - **Easy (5)**: Perfect recall → Longer interval
5. Continue until session is complete

### Keyboard Shortcuts (Study Mode)

- **Spacebar**: Show answer / Next card
- **1**: Again (forgot)
- **2**: Hard
- **3**: Good
- **4**: Easy
- **Esc**: Exit study session

### Viewing Statistics

1. Navigate to the **Statistics** tab
2. Explore various metrics:
   - Daily review chart (last 7/30 days)
   - Category distribution pie chart
   - Success rate percentage
   - Study streak
   - Mastery level breakdown
   - Most difficult cards

---

## 🏗️ Technical Architecture

### Project Structure

```
StudyCards-Pro/
├── main.py                      # Application entry point
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git exclusions
├── README.md                    # This file
├── studycards.db               # SQLite database (auto-generated)
│
├── core/                        # Core business logic
│   ├── __init__.py
│   ├── database.py             # SQLite operations and schema
│   ├── models.py               # Data models (Card, Deck, Category)
│   ├── spaced_repetition.py   # SM-2 algorithm implementation
│   └── statistics.py           # Analytics and statistics engine
│
└── gui/                         # User interface modules
    ├── __init__.py
    ├── main_window.py          # Main application window
    ├── deck_manager.py         # Deck management interface
    ├── card_editor.py          # Card creation/editing
    ├── study_mode.py           # Study session interface
    ├── statistics_panel.py     # Statistics visualization
    └── dialogs.py              # Reusable dialog components
```

### Database Schema

**Categories Table:**
- `id`, `name`, `color`, `created_at`

**Decks Table:**
- `id`, `name`, `description`, `category_id`, `created_at`

**Cards Table:**
- `id`, `deck_id`, `question`, `answer`, `example`, `tags`
- `difficulty`, `ease_factor`, `interval`, `repetitions`, `next_review`
- `created_at`, `updated_at`

**Review History Table:**
- `id`, `card_id`, `quality`, `reviewed_at`, `time_spent`

### Technologies Used

- **PySide6 (Qt6)**: Modern cross-platform GUI framework
- **qdarkstyle**: Professional dark theme styling
- **SQLite3**: Embedded relational database
- **Python 3.8+**: Core programming language

---

## 🎓 Educational Use Cases

### For Institute/University Students

**Mathematics:**
- Formulas and theorems
- Trigonometric identities
- Calculus derivatives and integrals
- Linear algebra operations

**Foreign Languages:**
- Vocabulary building (English, Spanish, French, etc.)
- Grammar rules and exceptions
- Idiomatic expressions
- Verb conjugations

**Sciences:**
- Chemical element properties
- Biological processes and cycles
- Physics equations and constants
- Medical terminology

**History:**
- Important dates and events
- Historical figures and their contributions
- Timeline of civilizations
- Document dates and significance

**Computer Science:**
- Programming syntax
- Data structure complexities
- Algorithm pseudocode
- Design patterns

---

## 🔬 The Science Behind Spaced Repetition

**Why It Works:**

Spaced repetition leverages the **spacing effect**—a cognitive phenomenon where information is better retained when study sessions are spaced out over time rather than crammed together.

**The Forgetting Curve:**

Without review, we forget approximately:
- 50% of new information within 1 hour
- 70% within 24 hours
- 90% within 1 week

Spaced repetition combats this by:
1. Reviewing just before you're about to forget
2. Strengthening memory pathways each time
3. Gradually increasing intervals as retention improves

**SuperMemo 2 Algorithm:**

Developed by Piotr Woźniak in 1988, SM-2 calculates optimal review intervals using:
- Previous interval length
- Ease factor (card-specific difficulty)
- Quality of recall (0-5 rating)

**Result:** Maximum retention with minimum study time!

---

## 🛣️ Roadmap & Future Features

- [ ] Image support in cards
- [ ] Audio pronunciation for language learning
- [ ] Collaborative deck sharing
- [ ] Mobile companion app (Android/iOS)
- [ ] Cloud synchronization
- [ ] Pre-made deck library
- [ ] Gamification elements (achievements, streaks)
- [ ] Study reminders and notifications
- [ ] Advanced statistics (retention graphs, prediction models)
- [ ] Markdown formatting in cards
- [ ] Cloze deletion card type
- [ ] Multiple-choice review mode

---

## 🤝 Contributing

Contributions are welcome! Whether you're fixing bugs, adding features, or improving documentation:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the LICENSE file for details.

---

## 🙏 Acknowledgments

- **Piotr Woźniak** - For developing the SuperMemo algorithm
- **Qt Company** - For the excellent Qt framework
- **Colin Duquesnoy** - For qdarkstyle theme
- **Open-source community** - For inspiration and support

---

## 📧 Support

If you encounter any issues or have questions:

- Open an issue on GitHub
- Check existing issues for solutions
- Contact the development team

---

## ⭐ Show Your Support

If StudyCards-Pro helps you ace your exams and master new knowledge, please consider:

- ⭐ Starring this repository
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 🔀 Contributing code improvements
- 📢 Sharing with fellow students

---

**Happy Learning! 🎓📚🚀**

*StudyCards-Pro - Master Knowledge, Retain Forever*
