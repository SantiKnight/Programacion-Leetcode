class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        robots = sorted(zip(positions, healths, directions, range(len(positions))))
        stack = []
        survivors = []
        for pos, health, direction, idx in robots:
            if direction == 'R':
                stack.append((pos, health, direction, idx))
            else:
                while stack:
                    r_pos, r_health, r_direction, r_idx = stack[-1]
                    if r_direction == 'R':
                        if r_health < health:
                            stack.pop()
                            health -= 1
                        elif r_health > health:
                            stack[-1] = (r_pos, r_health - 1, r_direction, r_idx)
                            health = 0
                            break
                        else:
                            stack.pop()
                            health = 0
                            break
                    else:
                        break
                if health > 0:
                    survivors.append((pos, health, direction, idx))
        
        survivors.extend(stack)
        survivors.sort(key=lambda x: x[3])
        return [health for _, health, _, _ in survivors]

s = Solution()
s.survivedRobotsHealths([3,5,2,6],[10,10,15,12],"LLLL")