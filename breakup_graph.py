""" class of plaquette graph just defined by their type """
class plaquette_graph():
    def __init__(self,breakup_type):
        self.breakup_type = breakup_type
        #self.weight = weights.prob(sq,breakup_type,chess.Dtau,chess.Jx,chess.Jz)

    def _get_breakup_type(self):
        return self.breakup_type
   
