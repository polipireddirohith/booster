# GitHub Activity Booster 🚀

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

**Boost your GitHub activity, test git workflows, and prepare your profile for job applications.**

This repository contains powerful scripts to generate legitimate commit activity and automate the creation of feature branches for Pull Requests. It is designed for:
- 🧪 Testing Git workflows and CI/CD pipelines.
- 📈 Maintaining an active contribution graph.
- 🚀 preparing "dummy" PRs to practice code reviews and merging.

## 📦 Features

- **Automated Commit Generation**: Specify the number of commits and days to spread them over.
- **Smart Dates**: Distributes commits randomly throughout the day during working hours.
- **Pull Request Automation**: Automatically creates conflict-free feature branches ready for merging.
- **Privacy Focused**: All generated code is local; nothing is uploaded until you push.

## 🛠️ Usage

### 1. Installation
Clone the repository:
```bash
git clone https://github.com/polipireddirohith/booster.git
cd booster
```

### 2. Generate Activity
Run the script to generate 50 commits over the last 10 days:
```bash
python activity_booster.py --commits 50 --days 10
```

### 3. Prepare Pull Requests
Create 5 separate branches to practice merging PRs:
```bash
# This creates 5 distinct branches that will not conflict!
python create_clean_prs.py
```

## 🤝 Contributing

Contributions are welcome! This project helps developers learn Git.
1. **Fork** this repository (Click the "Fork" button in the top right).
2. Create your feature branch (`git checkout -b feature/amazing-feature`).
3. Commit your changes.
4. Push to the branch.
5. Open a **Pull Request**.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
