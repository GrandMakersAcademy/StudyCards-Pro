# StudyCards Pro 🎓

A comprehensive flashcard application with advanced spaced repetition algorithm designed for students, educators, and lifelong learners. Built with modern Python technologies and featuring an intuitive Qt6 interface.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PySide6](https://img.shields.io/badge/PySide6-Qt6-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

## 🚀 Features

### 🧠 Intelligent Spaced Repetition
- **Adaptive Algorithm**: Automatically calculates optimal review intervals (1, 3, 7, 14+ days)
- **Performance-Based Scheduling**: Cards with correct answers get longer intervals
- **Mistake Recovery**: Incorrect answers reset the interval for reinforced learning
- **Scientific Approach**: Based on proven memory retention research

### 📚 Comprehensive Card Management
- **Rich Content Support**: Create cards with questions, answers, and detailed examples
- **Category Organization**: Group cards by subjects (Mathematics, Languages, History, etc.)
- **Deck Management**: Work with multiple study sets simultaneously
- **Import/Export**: Share decks with classmates or backup your progress

### 📊 Advanced Progress Tracking
- **Detailed Statistics**: Track studied cards, accuracy rates, and daily progress
- **Visual Analytics**: Charts and graphs showing learning trends
- **Performance Insights**: Identify strong and weak areas
- **Study Streak Tracking**: Maintain motivation with consecutive study days

### 🎨 Modern User Interface
- **Dark Theme**: Eye-friendly design for extended study sessions
- **Responsive Layout**: Adapts to different screen sizes
- **Intuitive Navigation**: Clean, distraction-free study environment
- **Customizable Settings**: Personalize your learning experience

## 🏫 Perfect for Academic Use

**StudyCards Pro** is specifically designed for educational environments:

- **University Students**: Master complex subjects with efficient review scheduling
- **High School Students**: Prepare for exams with systematic study plans
- **Language Learners**: Build vocabulary with optimized repetition intervals
- **Medical Students**: Memorize terminology and concepts effectively
- **Professional Certification**: Prepare for licensing and certification exams
- **Educators**: Create and distribute study materials to students

## 🛠️ Technical Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows 10/11, Linux, or macOS
- **RAM**: 512MB minimum (1GB recommended)
- **Storage**: 100MB for application and database

## 📦 Installation

### Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/GrandMakersAcademy/StudyCards-Pro.git
   cd StudyCards-Pro
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python main.py
   ```

### Alternative Installation Methods

#### Using Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv studycards_env

# Activate virtual environment
# Windows:
studycards_env\Scripts\activate
# Linux/macOS:
source studycards_env/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python main.py
```

#### Using pip (Direct Installation)
```bash
pip install PySide6 qdarkstyle sqlalchemy alembic python-dateutil numpy matplotlib
python main.py
```

## 🎯 How to Use

### Getting Started
1. **Launch** the application
2. **Create your first category** (e.g., "Biology", "Spanish Vocabulary")
3. **Add flashcards** with questions and answers
4. **Start studying** - the algorithm will handle the rest!

### Study Workflow
1. **Daily Review**: Check cards scheduled for today
2. **Answer Cards**: Rate your knowledge (Easy/Good/Hard/Again)
3. **Track Progress**: Monitor your learning statistics
4. **Consistent Practice**: Study regularly for best results

### Advanced Features
- **Bulk Import**: Import cards from CSV files
- **Statistics Export**: Generate progress reports
- **Custom Categories**: Organize by subject, difficulty, or priority
- **Search & Filter**: Quickly find specific cards or topics

## 📊 Study Statistics

The application provides comprehensive analytics:

- **Cards Due Today**: Never miss a scheduled review
- **Learning Progress**: Visual representation of mastery levels
- **Accuracy Rates**: Track improvement over time
- **Study Streaks**: Maintain consistent learning habits
- **Performance by Category**: Identify areas needing attention

## 🎓 Educational Benefits

### Spaced Repetition Science
- **Forgetting Curve**: Combats natural memory decay
- **Optimal Intervals**: Reviews cards just before forgetting
- **Long-term Retention**: Moves information to long-term memory
- **Efficient Learning**: Focuses time on challenging material

### Academic Applications
- **Exam Preparation**: Systematic review before tests
- **Language Learning**: Vocabulary and grammar acquisition
- **Medical Studies**: Memorize complex terminology
- **History & Dates**: Remember important events and timelines
- **Mathematics**: Practice formulas and theorems
- **Science Facts**: Retain key concepts and definitions

## 🔧 Development

### Architecture
- **Frontend**: PySide6 (Qt6) for modern GUI
- **Backend**: SQLAlchemy for database management
- **Theming**: QDarkStyle for professional appearance
- **Analytics**: Matplotlib for progress visualization

### Project Structure
```
StudyCards-Pro/
├── main.py                 # Application entry point
├── requirements.txt        # Python dependencies
├── src/
│   ├── core/              # Business logic
│   │   ├── database.py    # Database management
│   │   ├── models.py      # Data models
│   │   └── spaced_repetition.py # Algorithm
│   ├── gui/               # User interface
│   │   ├── main_window.py # Main application window
│   │   ├── dialogs/       # Dialog windows
│   │   └── widgets/       # Custom widgets
│   └── utils/             # Utility functions
├── assets/                # Images and icons
├── docs/                  # Documentation
└── tests/                 # Unit tests
```

## 🤝 Contributing

We welcome contributions from the educational and developer communities!

1. **Fork** the repository
2. **Create** a feature branch
3. **Make** your changes
4. **Add** tests if applicable
5. **Submit** a pull request

### Development Guidelines
- Follow PEP 8 coding standards
- Add docstrings to all functions
- Include unit tests for new features
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Spaced Repetition Research**: Based on work by Hermann Ebbinghaus and modern cognitive science
- **Qt Framework**: For providing excellent cross-platform GUI capabilities
- **Python Community**: For the amazing ecosystem of libraries
- **Educational Psychology**: Inspired by evidence-based learning techniques

## 📞 Support

For support, feature requests, or bug reports:

- **GitHub Issues**: [Report bugs or request features](https://github.com/GrandMakersAcademy/StudyCards-Pro/issues)
- **Documentation**: Check the `docs/` folder for detailed guides
- **Community**: Join discussions in the Issues section

## 🚀 Future Enhancements

- **Cloud Synchronization**: Sync across devices
- **Mobile App**: Companion mobile application
- **Collaborative Decks**: Share and collaborate on card collections
- **Advanced Analytics**: Machine learning insights
- **Plugin System**: Extend functionality with custom plugins
- **Multi-language Support**: Interface localization

---

**StudyCards Pro** - Empowering students worldwide with intelligent learning technology. 🌟

Made with ❤️ by [GrandMakersAcademy](https://github.com/GrandMakersAcademy)
