BEGIN
WHILE player one not authenticated
	ask user for player one's credentials

WHILE player two not authenticated
	ask user for player two's credentials

Round = 0
WHILE (rounds =< 5)
	Roll One = random integer from 1 to 6
	Roll Two = random integer from 1 to 6
	total =  Roll One + Roll Two
	IF ((total/2) IS INT) THEN
		total = total + 10
	IF ELSE (Roll One == Roll Two) THEN
		total = total + random integer form 1 to 6
	ELSE
		total = total - 5
	Player One Score = Player One Score + Total
	IF (Player One Score < 0) THEN
		Player One Score = 0

Round = 0
WHILE (rounds =< 5)
	Roll One = random integer from 1 to 6
	Roll Two = random integer from 1 to 6
	total =  Roll One + Roll Two
	IF ((total/2) IS INT) THEN
		total = total + 10
	IF ELSE (Roll One == Roll Two) THEN
		total = total + random integer form 1 to 6
	ELSE
		total = total - 5
	Player Two Score = Player One Score + Total
	IF (Player Two Score < 0) THEN
		Player Two Score = 0

WHILE Player One Score == Player Two Score
	Player One Score = Player One Score + random integer from 1 to 6
	Player Two Score = Player Two Score + random integer from 1 to 6

IF (Player One Score > Player Two Score) THEN
	OUTPUT "Player One has won" and the scores
ELSE
	OUTPUT "Player Two has won" and the scores