# Self-Learning Connect 4 AI

## Project Overview
A modular Connect 4 AI that evolves and learns opponent strategies using:
- Minimax + Alpha-Beta pruning
- Bayesian Networks for player modeling
- Genetic Algorithms for strategy optimization
- Visualization dashboard for monitoring learning

## Structure
- `game_engine/` — Phase 1, core board and game logic
- `minimax_ai/` — Phase 2, AI decision making
- `bayesian_model/` — Phase 3, opponent modeling
- `genetic_optimizer/` — Phase 4, strategy evolution
- `dashboard/` — Phase 5, visualization
- `integration/` — Phase 6, glue module for full AI
- `docs/` — documentation   

## Getting Started
1. Clone repo
2. Run Phase 1:
```bash
cd game_engine
python game.py
