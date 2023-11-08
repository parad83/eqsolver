import re

'''
const stringToOperator: { [key: string]: (x: number, y: number) => function } = {
  "+": function (x: number, y: number) {
    return x + y;
  },
  "-": function (x: number, y: number) {
    return x - y;
  },
  "*": function (x: number, y: number) {
    return x * y;
  },
  "/": function (x: number, y: number) {
    return x / y;
  },
  "^": function (x: number, y: number) {
    return x ** y;
  },
};

const equationSolver = (equation: string[]) =>  {
    const char = equation[0];
    // if (char === "-") {
    //   return -1 * equationSolver(equation.slice(1));
    // } else

    // final condition
    if (!equation[1]) {
      return char;
    }
    if (!char) {
      return 1;
    } else if (char.match(/\([a-z]\)/)) {   // check for independant variable
      
      return function(x, y) {
        if stringToOperator[equation[1]] {
          return Number(char) * equationSolver(equation.slice(1));
        }
      }
    } else if (typeof char.match(/d+/g)) {    // check for digit
      if (equation[1] && stringToOperator[equation[1]]) {
        return Number(char) * equationSolver(equation.slice(1));
      }
    }
   

      return stringToOperator[equation[1]](
        char,
        equationSolver(equation.slice(2))
      );
    }
    // return char;
  };
  '''


stringToOperator = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "^": lambda x, y: x ** y,
}


# def equationSolver(equation: list):
#     char = equation[0]
#     # if not char:
#     #     return 1
#     # elif char == "-":
#     #     return -1 * equationSolver(equation[1:])
#     if not equation[1]:
#         print('end')
#         return int(char)
#     return lambda x: stringToOperator[char](x, equationSolver(equation[2:]))


def equationSolver(equation: list):
    char = equation[0]
    # checks for a number
    try:
        next_char = equation[1]
    except IndexError:
        if re.search(r"[a-z]", char):
            return lambda x: x
        return int(char)
    if re.search(r"\d", char):
        if next_char in stringToOperator:
            # if the next char is an operator, then we can assume that the next number is the second operand
            return stringToOperator[next_char](int(char), equationSolver(equation[2:]))
        # if not, then we can assume that the next char is a 'bracket'
        return int(char)*equationSolver(equation[1:])
    # checks for an independant variable
    elif re.search(r"[a-z]", char):
        print('x')
        return lambda x: stringToOperator[next_char](x, equationSolver(equation[2:]))
    # if the current char is a number, then we can assume that the next char is an operator and the next number is the second operand
    # it follows the BODMAS rule, but in reverse so the first number is the last to be solved
    elif char == "(":
        second = equation.index(')')
        if second+1 < len(equation):
            if stringToOperator[equation[second+1]]:
                return stringToOperator[equation[second+1]](equationSolver(equation[1:second]), equation[second+1:])
            return equation[second+1]*equationSolver(equation[1:second])
        return equationSolver(equation[1:second])
    # return lambda x, y: stringToOperator[char](x, equationSolver(equation[2:]))


# string = ["2", "*", "3", "*", "8", "(", "2", "+", "3", ")"]
# string = ["2", "+", "-1"]
# string = ["2", "+", "1", "*", "3", "*", "8", "(", "2", "+", "3", ")"]
# string = ["2", "^", "3", "*", "4", "+", "2"]
string = ["x", "^", "2",]

x = equationSolver(string)
print(x(2))

first = 5
second = 9

# print(string[first+1:second])

#

# if re.search(r'\(|\)', "(equation)"):
#     print('found bracket')
#     first = "(equation)".index('(')
#     second = "(equation)".index(')')

# print("(equation)"[first+1:second])
