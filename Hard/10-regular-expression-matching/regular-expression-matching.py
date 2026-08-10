class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        memo = {}

        def dp(i, j):
            # If we already solved this state
            if (i, j) in memo:
                return memo[(i, j)]

            # If pattern is finished
            if j == len(p):
                return i == len(s)

            # Check whether current characters match
            first_match = (
                i < len(s) and
                (s[i] == p[j] or p[j] == '.')
            )

            # Check if next character is *
            if j + 1 < len(p) and p[j + 1] == '*':

                # Option 1: Skip "character*"
                skip = dp(i, j + 2)

                # Option 2: Use * to match current character
                use = first_match and dp(i + 1, j)

                answer = skip or use

            else:
                # Normal character or '.'
                answer = first_match and dp(i + 1, j + 1)

            # Save answer
            memo[(i, j)] = answer

            return answer

        return dp(0, 0)