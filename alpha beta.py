def alphabeta(depth, node, maximizing, values, alpha, beta):

    if depth == 2:
        return values[node]

    if maximizing:
        best = -999

        for i in range(2):
            value = alphabeta(depth + 1, node * 2 + i,
                              False, values, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)

            if alpha >= beta:
                break

        return best

    else:
        best = 999

        for i in range(2):
            value = alphabeta(depth + 1, node * 2 + i,
                              True, values, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)

            if alpha >= beta:
                break

        return best


values = [3, 5, 2, 9]

result = alphabeta(0, 0, True, values, -999, 999)

print("Best value:", result)
