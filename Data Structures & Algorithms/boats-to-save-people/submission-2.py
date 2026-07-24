class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        people = people[::-1]

        counter = Counter(people)
        res = 0
        for p in people:
            if counter[p] <= 0:
                continue
            if p == limit:
                counter[p] -= 1
                print(f"{p} == {limit}")
                res += 1
            else:
                found = False
                for candidate in range(limit-p, 0, -1):
                    if candidate == p:
                        if counter[p] > 1:
                            counter[p] -= 2
                            res += 1
                            print(f"same {p} and {candidate}")
                            found = True
                            break
                    else:
                        if counter[candidate] > 0:
                            counter[p] -= 1
                            counter[candidate] -= 1
                            res += 1
                            print(f"{p} and {candidate}")
                            found = True
                            break
                if not found:
                    print(f"{p}")
                    counter[p] -= 1
                    res += 1
        return res


        