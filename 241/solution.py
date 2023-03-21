def diffWaysToCompute(input):
    if input.isdigit():
        return [int(input)]
    res = []
    for i in range(len(input)):
        if input[i] in ['+', '-', '*']:
            left = diffWaysToCompute(input[:i])
            right = diffWaysToCompute(input[i+1:])
            for l in left:
                for r in right:
                    if input[i] == '+':
                        res.append(l + r)
                    elif input[i] == '-':
                        res.append(l - r)
                    else:
                        res.append(l * r)
    return res