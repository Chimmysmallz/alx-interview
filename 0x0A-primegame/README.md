# Prime Game

This script allows you to play the Prime Game, a game where two players take turns choosing prime numbers from a set of consecutive integers and removing them along with their multiples. The player who cannot make a move loses the game. The script determines the winner of each round based on the given inputs and returns the player with the most wins.

## Requirements

- Python 3.4.3
- Ubuntu 14.04 LTS
- PEP 8 style (version 1.7.x)

## Usage

1. Clone the repository or download the prime_game.py script.
2. Make sure the script is executable:
   ```
   chmod +x prime_game.py
   ```
3. Modify the script to adjust the rounds and numbers for testing, if desired.
4. Execute the script:
   ```
   ./prime_game.py
   ```
5. The output will display the name of the player who won the most rounds, or "None" if the winner cannot be determined.

## Example

Consider the following example:

```python
rounds = 3
numbers = [4, 5, 1]
print("Winner: {}".format(isWinner(rounds, numbers)))
```

Output:
```
Winner: Ben
```

In this example, Maria and Ben play three rounds with the given numbers. Ben wins two rounds, while Maria wins one round. Therefore, the overall winner is Ben.

## Author

- Chiamaka Nwabulue
- GitHub: [Chimmysmallz](https://github.com/Chimmysmallz)
