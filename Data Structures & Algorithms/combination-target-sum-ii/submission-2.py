class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        subset = []

        def backtrack(i, remaining):
            if remaining == 0:
                result.append(subset.copy())
                return

            if remaining < 0:
                return

            for j in range(i, len(candidates)):
                # Skip duplicates at the same recursion level
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                # Candidates are sorted, so larger values won't work
                if candidates[j] > remaining:
                    break

                subset.append(candidates[j])
                backtrack(j + 1, remaining - candidates[j])
                subset.pop()

        backtrack(0, target)
        return result