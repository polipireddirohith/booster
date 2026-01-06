# How to Boost Your GitHub Stats

You requested to increase **Stars, Network, Insights, Watch, and Pull Requests**. Here is how you can do it:

## 1. Automated (Using included script)
We have created `activity_booster.py` to help with **Contributions** and preparing **Pull Requests**.

### Increase Contribution Graph (Green Squares)
Run the script to generate commits:
```bash
python activity_booster.py --commits 50 --days 10
# This creates 50 commits spread over the last 10 days
git push origin main
```

### Increase Pull Requests
1. Run the script to create branches:
   ```bash
   python activity_booster.py --branches 5
   ```
2. Push all branches:
   ```bash
   git push --all origin
   ```
3. Go to your GitHub repository page.
4. You will see "Compare & pull request" for each branch. Click them to open PRs.
5. Merging them will increase your merged PR count.

## 2. Organic Growth (Stars, Watch, Network, Insights)
These metrics rely on other users interacting with your repository. You cannot safely script these without violating GitHub Terms of Service (fake engagement).

### Increase Stars & Watchers
* **Be Professional**: Ensure your repo has a clean `README.md`, `LICENSE`, and generic `CONTRIBUTING.md`.
* **Share**: Post your project on LinkedIn, Reddit (r/webdev, r/python), and Twitter using relevant hashtags.
* **Topics**: Add topics (tags) to your repository settings (e.g., `python`, `automation`, `machine-learning`) to make it searchable.

### Increase Network (Forks)
* **Make it useful**: Create a template or a library that others *need* to modify.
* **Call to Action**: explicitly ask users to fork the repo if they want to customize it.

### Increase Insights (Traffic/Views)
* **Backlinks**: Link to your repo from your Portfolio, LinkedIn, and Resume.
* **Documentation**: Good docs keep people reading your code longer.
