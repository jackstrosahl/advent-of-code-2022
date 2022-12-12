from numbers import Number


class ModNum:
    def __init__(self, num=None, divisors=None, mods=None):
        if num:
            self.mods = {
                divisor: num % divisor for divisor in divisors
            }
        else:
            self.mods = mods
    
    def do_op(self, op, other):
        if not isinstance(other, Number):
            raise NotImplementedError
        return ModNum(mods={
            divisor:(op(mod,other))%divisor for divisor, mod in self.mods.items()
        })
    
    def __mod__(self, other):
        if not isinstance(other, Number):
            raise NotImplemented
        return self.mods[other]