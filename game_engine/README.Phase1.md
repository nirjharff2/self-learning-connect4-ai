# Phase 1: Game Engine Module
  Author: Nirjhar Neer
  Project: Self-Learning Connect 4 AI
  Status: ✅ Completed

## Objective
Develop foundational Connect 4 engine that supports:
- Board creation and management  
- Piece placement
- Win detection (horizontal, vertical, diagonal)  
- Two-player interactive console gameplay  

This phase establishes the **core environment** that later AI modules (Minimax, Bayesian, Genetic) will interact with.

---

## Module Structure
connect4_ai/
└── game_engine/
	├── init.py
	├── board.py
	├── game.py
	└── test_game.py


---

## Components Overview

| File | Description |
|------|--------------|

**board.py - Handles board state, valid moves, piece placement, and win detection.

**game.py - Implements the main two-player console-based Connect 4 gameplay loop.

**test_game.py - Basic unit tests for horizontal and vertical win detection.

**__init__.py - Empty file marking this folder as a Python package. 

---

## ▶️ Run Instructions

### Play the Game
```bash
cd connect4_ai/game_engine
python game.py



	

