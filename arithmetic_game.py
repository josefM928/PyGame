from enum import Enum
import math
import random


class Number:
    def zero(symbol, width):
        print(symbol * width)
        for i in range(width - 2):
            print(symbol + " " * (width - 2) + symbol)
        print(symbol * width)
        print()

    def one(symbol, width):
        for i in range(width):
            print(" " * (width - 1) + symbol)
        print()

    def two(symbol, width):
        print(symbol * width)
        for i in range((width - 3) // 2):
            print(" " * (width - 1) + symbol)
        print(symbol * width)
        for i in range((width - 3) // 2):
            print(symbol + " " * (width - 1))
        print(symbol * width)
        print()

    def three(symbol, width):
        print(symbol * width)
        for i in range((width - 3) // 2):
            print(" " * (width - 1) + symbol)
        print(symbol * width)
        for i in range((width - 3) // 2):
            print(" " * (width - 1) + symbol)
        print(symbol * width)
        print()

    def four(symbol, width):
        for i in range(width // 2 - 1):
            print(symbol + " " * (width - 2) + symbol)
        print(symbol * width)
        for i in range(width // 2):
            print(" " * (width - 1) + symbol)
        print()

    def five(symbol, width):
        print(symbol * width)
        for i in range((width - 3) // 2):
            print(symbol + " " * (width - 1))
        print(symbol * width)
        for i in range((width - 3) // 2):
            print(" " * (width - 1) + symbol)
        print(symbol * width)
        print()

    def six(symbol, width):
        print(symbol * width)
        for i in range((width // 2 - 1)):
            print(symbol + " " * (width - 1))
        print(symbol * width)
        for i in range(width // 2 - 1):
            print(symbol + " " * (width - 2) + symbol)
        print(symbol * width)
        print()

    def seven(symbol, width):
        print(symbol * width)
        for i in range(width - 1):
            print(" " * (width - 1) + symbol)
        print()

    def eight(symbol, width):
        print(symbol * width)
        for i in range((width - 3) // 2):
            print(symbol + " " * (width - 2) + symbol)
        print(symbol * width)
        for i in range((width - 3) // 2):
            print(symbol + " " * (width - 2) + symbol)
        print(symbol * width)
        print()

    def nine(symbol, width):
        print(symbol * width)
        for i in range(width // 2 - 1):
            print(symbol + " " * (width - 2) + symbol)
        print(symbol * width)
        for i in range((width // 2 - 1)):
            print(" " * (width - 1) + symbol)
        print(symbol * width)
        print()

    def draw(number, symbol, width):
        my_dict = {0: Number.zero, 1: Number.one, 2: Number.two, 3: Number.three, 4: Number.four,
                   5: Number.five, 6: Number.six, 7: Number.seven, 8: Number.eight, 9: Number.nine}
        my_dict.get(number)(symbol, width)


class Operator(Enum):
    PLUS = 0
    MINUS = 1
    MULTIPLY = 2
    DIVIDE = 3

    def draw_plus(symbol, width):
        for i in range((width - 1) // 2):
            print(" " * math.floor((width - 1) / 2) + symbol + " " * math.ceil((width - 1) / 2))
        print(symbol * width)
        for i in range((width - 1) // 2):
            print(" " * math.floor((width - 1) / 2) + symbol + " " * math.ceil((width - 1) / 2))
        print()

    def draw_minus(symbol, width):
        for i in range(width // 2):
            print()
        print(symbol * width)
        for i in range(width // 2):
            print()
        print()

    def draw_multiply(symbol, width):
        for i in range(width // 2):
            print(" " * i + symbol + " " * (width - 2 * i - 2) + symbol + " " * i)
        print(" " * math.floor((width - 1) / 2) + symbol + " " * math.ceil((width - 1) / 2))
        for i in reversed(range(width // 2)):
            print(" " * i + symbol + " " * (width - 2 * i - 2) + symbol + " " * i)
        print()

    def draw_divide(symbol, width):
        for i in range(width):
            print(" " * (width - i - 1) + symbol + " " * i)
        print()

    def draw(operator_to_draw, symbol, width):
        if (operator_to_draw == Operator.PLUS):
            Operator.draw_plus(symbol, width)
        elif (operator_to_draw == Operator.MINUS):
            Operator.draw_minus(symbol, width)
        elif (operator_to_draw == Operator.MULTIPLY):
            Operator.draw_multiply(symbol, width)
        elif (operator_to_draw == Operator.DIVIDE):
            Operator.draw_divide(symbol, width)
        else:
            print("Invalid operator")

class Problem:
    def __init__(self, operand_1, operand_2, operator):
        self.operand_1 = operand_1
        self.operand_2 = operand_2
        self.operator = operator
  
    def get_answer(self):
        if (self.operator == Operator.PLUS):
            return self.operand_1 + self.operand_2
        elif (self.operator == Operator.MINUS):
            return self.operand_1 - self.operand_2
        elif (self.operator == Operator.MULTIPLY):
            return self.operand_1 * self.operand_2
        elif (self.operator == Operator.DIVIDE):
            return self.operand_1 / self.operand_2
        else:
            print("Invalid operator")

    def drawProblem(self, symbol, width):
        print("\n\n")
        print("What is ...?")
        print()
        Number.draw(self.operand_1, symbol, width)
        Operator.draw(self.operator, symbol, width)
        Number.draw(self.operand_2, symbol, width)
        print(" = ", end="")
  
    def get_user_input(self):
        self.user_answer = float(input())
  
    def check_answer(self):
        if(self.user_answer == float(self.get_answer())):
            print("Correct!")
            return True
        print("Sorry, that's not correct.")
        return False


class Quiz:

    problem_types = [Operator.PLUS, Operator.MINUS,
                     Operator.MULTIPLY, Operator.DIVIDE]

    def __init__(self, num_problems, width, symbol):
        self.num_problems = num_problems
        self.symbol = symbol
        self.width = width if (width > 4 and width < 11) else 5
        self.problems = []
        for i in range(num_problems):
            operator = Quiz.problem_types[random.randint(0, len(Quiz.problem_types) - 1)]
            first_operand = random.randint(0, 9)
            second_operand = random.randint(0, 9) if operator != Operator.DIVIDE else random.randint(1, 9)
            self.problems.append(Problem(first_operand, second_operand, operator))
      
        for problem in self.problems:
            problem.drawProblem(self.symbol, self.width)
            problem.get_user_input()
            problem.check_answer()


def get_valid_num_problems():
    try:
        result = int(input("How many problems would you like to attempt? "))
        if(result >= 0):
            return result
      
        return get_valid_num_problems()
    except Exception as e:
        print("Invalid number, try again")
        return get_valid_num_problems()

def get_valid_width():
    try:
        result = int(input("How wide do you want your digits to be? 5-10: "))
        if(result > 4 and result < 11):
            return result
      
        return get_valid_width()
    except Exception as e:
        print("Invalid number, try again")
        return get_valid_width()


def main():
    num_problems = get_valid_num_problems()
    width = get_valid_width()
    q = Quiz(num_problems, width, '*')


if __name__ == "__main__":
    main()