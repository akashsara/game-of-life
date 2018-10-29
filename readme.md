# Game of Life

An implementation of [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life). 

## tl;dr:
We have a 2-D grid. Each cell in the grid is either 'alive' or 'dead'. This is denoted by O for alive and . for dead in my code. The game happens in a number of rounds(usually infinite). These rounds imply generations of life.

Every round, each cell checks its immediate neighbors and sees how many are alive. Then,
1. Any live cell with 0 or 1 live neighbors dies due to underpopulation.
2. Any live cell with 2 or 3 live neighbors stays alive to the next generation.
3. Any live cell with more than 3 live neighbors dies due to overpopulation.
4. Any dead cell with exactly 3 live neighbors comes to life via reproduction.
5. Any other dead cell stays dead.

The only input required is the initial pattern which serves as the _seed_ for the system. This system tends to give rise to some interesting patterns.

## Install & Instructions

1. Clone or download this repository.
2. Run the file using `python game_of_life.py`

There are a few optional arguments you may pass while running the file:
`--h HEIGHT` - The height of the board.
`--w WIDTH` - The width of the board.
`--rounds ROUNDS` - The number of rounds/generations.
`--file FILE`- Path to an input file for the initial state. Giving an input file overrides the given height and width. 

## Game in Action

`game_of_life.py --file sample.txt --rounds 30`

![Game of Life](https://thumbs.gfycat.com/RaggedLastingDromedary-small.gif)

## Tests

Simply run `tests.py`. It ensures that the 5 conditions are working. If you find any issues or errors, please let me know!