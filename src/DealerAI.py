from src.Player import * 
import src.HouseRules as RULES

class DealerAI:
    def __init__(self, dealer: Player) -> None:
        self.player = dealer
    
        def getTurnDecision(self) -> str:
            if self.player.getHandValue() < 17:
                return "HIT"
            elif self.player.getHandValue() == 17 and self.player.handIsSoft() == True and RULES.DEALER_HITS_SOFT_17 == True:
                return "HIT"
            else:
                return "STAND"