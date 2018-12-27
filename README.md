## Synopsis

An implementation of the [tictactoe game](http://www.exploratorium.edu/brain_explorer/tictactoe.html) using a simple strategy that hopes to make this app, which is always playing as `o`, a formidable opponent.
The strategy is as follows:
- Watch out for obvious wins if any
- Block attempts by `x` to win
- If corner positions are available, play any one of them.
- If no corner positions are available but the center is open, play center.
- Only play the edges if and only if, no corners and center are available.

## Developer Setup
- Clone the repository and change directory into the project.
```
git clone https://github.com/ianbrayoni/tictactoe.git
cd tictactoe
```
- Create a virtual env using your preferred tool. I use [pipenv](https://github.com/pypa/pipenv).
```
pipenv --three
```
- Install requirements
```
pipenv install flask-restplus
```
- Run app
```
python api.py
```
- Sample request, the app will be available at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
```
curl http://127.0.0.1:5000/tictactoe?board=+xxo++o++
```
- Sample response after the server playing, `"oxxo  o  "`
- To play directly with the [app](https://github.com/ianbrayoni/tictactoe/blob/master/tic_tac_toe.py):
```
(tictactoe-ELLgTskw) ➜  tictactoe git:(master) python
Python 3.6.5 (default, Apr 25 2018, 14:26:36)
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.39.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from tic_tac_toe import main
>>> main()
Enter the board state: oxxo  o
'Invalid board state!'
>>> main()
Enter the board state:  xxo  o
'oxxo  o  '
```
- Test
```
python -m unittest
```

## API Reference
The api only implements a `GET` method on `<url>/tictactoe?board=<query-string>`. A valid request will get a `200 OK` HTTP Status Code with the computed state after the server playing, otherwise a `400 BAD REQUEST` for an invalid request.

## Improvements
1. Implement [minimax algorithm](https://en.wikipedia.org/wiki/Minimax) with [alpha beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) to help the server play optimally and minimise computation.
2. Store state of already computed game strings and return them without having to compute again if encountered in future.
3. Check for symmetrical board patterns and return same response for both board states.




