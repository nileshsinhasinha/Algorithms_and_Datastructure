"""Tower Of Hanoi:- Here we have to move n discs from source to target using intermediate.
                    Rules to follow:- 1st disc is lightest it can be put on any other disc anytime
                                      Last disc is heaviest can be put on base only anytime"""
class toh:
    movements=0
    fn_calls=1
    def __init__(self,discs,source,target,intmdt):
        self.discs=discs
        self.source=source
        self.target=target
        self.intmdt=intmdt

    def tower_of_hanoi(self,discs,source,target,intmdt):
        if discs>=1:
            self.fn_calls+=1
            self.tower_of_hanoi(discs-1,source,intmdt,target)
            self.movements+=1
            target.append(source.pop())
            self.fn_calls+=1
            self.tower_of_hanoi(discs-1,intmdt,target,source)

if __name__ == "__main__":
    import random
    source=[random.randint(1,100) for _ in range(1,11)]
    source.sort(reverse=True)
    print(source)
    discs=len(source)
    target=[]
    intmdt=[]
    toh_3=toh(discs,source,target,intmdt)
    toh_3.tower_of_hanoi(toh_3.discs,toh_3.source,toh_3.target,toh_3.intmdt)

print(target,toh_3.movements,toh_3.fn_calls)


