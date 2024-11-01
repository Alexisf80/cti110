# Alexis Furmage
# 11/1/24
# P4HW1
# Assignment assess student ability to edit and enhance exiting programs



"""
BEGIN PROGRAM

    FUNCTION get_valid_score(index)
        REPEAT
            PROMPT user to enter a score with index
            TRY
                CONVERT input to float
                IF score is between 0 and 100
                    RETURN score
                ELSE
                    PRINT "INVALID Score entered!!!!"
                    PRINT "Score should be between 0 and 100. Enter score again:"
            EXCEPT ValueError
                PRINT "INVALID input. Please enter a numeric value. Enter score again:"
        UNTIL valid score is entered
    END FUNCTION

    FUNCTION calculate_average(scores)
        IF number of scores > 1
            FIND lowest score
            REMOVE lowest score from scores
            RETURN lowest score, sum of scores divided by the number of scores
        ELSE
            RETURN None, the only score
    END FUNCTION

    FUNCTION get_letter_grade(average)
        IF average >= 90
            RETURN 'A'
        ELSE IF average >= 80
            RETURN 'B'
        ELSE IF average >= 70
            RETURN 'C'
        ELSE IF average >= 60
            RETURN 'D'
        ELSE
            RETURN 'F'
    END FUNCTION

    MAIN PROGRAM
        PROMPT user to enter the number of scores
        INITIALIZE empty list for scores

        FOR each score from 1 to num_scores
            CALL get_valid_score(i) and append result to scores

        CALL calculate_average(scores) and store result in lowest_score and average
        CALL get_letter_grade(average) and store result in letter_grade

        PRINT results including lowest score, modified list, average score, and letter grade
END PROGRAM
"""

def get_valid_score(index):
    while True:
        try:
            score = float(input(f"Enter score #{index}: "))
            if 0 <= score <= 100:
                return score
            else:
                print("INVALID Score entered!!!!")
                print("Score should be between 0 and 100. Enter score again:")
        except ValueError:
            print("INVALID input. Please enter a numeric value. Enter score again:")

def calculate_average(scores):
    if len(scores) > 1:
        lowest_score = min(scores)
        scores.remove(lowest_score)
        return lowest_score, sum(scores) / len(scores)
    else:
        return None, scores[0]

def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def main():
    num_scores = int(input("How many scores do you want to enter? "))
    scores = []

    for i in range(1, num_scores + 1):
        score = get_valid_score(i)
        scores.append(score)

    lowest_score, average = calculate_average(scores)
    letter_grade = get_letter_grade(average)

    print("---------------Results----------------")
    print(f"Lowest Score: {lowest_score}")
    print(f"Modified List: {scores}")
    print(f"Scores Average: {average:.2f}")
    print(f"Grade: {letter_grade}")
    print("-----------------------------------------")

if __name__ == "__main__":
    main()
