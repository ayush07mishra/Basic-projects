# 🤖 Autonomous Agent in a 2D Grid World

This project simulates a basic autonomous agent navigating a 2D grid to reach a goal while avoiding obstacles. The agent learns its path using **Reinforcement Learning (Q-Learning)** — a core concept in autonomous systems like robotics and self-driving cars.

## 📌 Features

- ✅ 2D grid environment with start, goal, and obstacles  
- 🧠 Q-Learning based agent (no hard-coded rules)  
- 🎮 Visualized with Pygame  
- 📊 Logs rewards, steps per episode

## 📁 Project Structure

autonomous_agent/  
├── main.py            # Game loop and visualization  
├── environment.py     # Environment: grid, goal, obstacles  
├── agent.py           # Agent wrapper for decision logic  
├── qlearning.py       # Q-learning implementation  
├── README.md          # Project guide  

## 🧠 ML Technique Used

- Q-Learning (Tabular Reinforcement Learning)
- State = (x, y) position of the agent
- Actions = [0: Up, 1: Down, 2: Left, 3: Right]
- Reward Function:
  - +100 on reaching the goal
  - -1 on each move
  - Ignores invalid moves or wall collisions

## 🚀 How to Run

1. Clone the repo
git clone https://github.com/ayush07mishra/autonomous_agent.git cd autonomous_agent

2. Install dependencies
pip install pygame numpy

3. Run the project
python main.py


## 📺 Demo Preview


https://github.com/user-attachments/assets/ed4873d7-7a13-484f-b873-e487c015b2b7



Agent (blue) starts at top-left and learns to reach the goal (green), avoiding obstacles (black).  

## 📈 Sample Output

Episode 1: Steps = 85, Reward = -15  
Episode 2: Steps = 55, Reward = 45  
...  
Episode 200: Steps = 18, Reward = 82  

## 💡 Possible Improvements

- Use Deep Q-Learning (DQN) with neural networks
- Add dynamic obstacles or multiple agents
- Visualize the Q-table or policy heatmaps
- Use expert demonstration data (behavioral cloning)
- Add reset/play buttons and UI dashboard

## 🧠 Concepts Covered

- Reinforcement Learning
- Q-Learning Algorithm
- Path Planning and Obstacle Avoidance
- Pygame Visualization

## 📜 License

This project is licensed under the MIT License.  
Free to use for educational and non-commercial purposes.

## 👨‍💻 Author

**Ayush Mishra**  
GitHub: https://github.com/ayush07mishra

