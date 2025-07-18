C_Token_Reputation_Engine/token_engine.py
# token_engine.py

# ZU Token + Reputation Engine - Phase C

class Token:
    def __init__(self, token_id, behavior_score=100):
        self.token_id = token_id
        self.behavior_score = behavior_score

    def update_score(self, impact):
        self.behavior_score += impact
        self.behavior_score = max(0, min(self.behavior_score, 100))  # Keep score between 0 and 100

class ReputationEngine:
    def __init__(self):
        self.tokens = {}

    def register(self, token_id):
        if token_id not in self.tokens:
            self.tokens[token_id] = Token(token_id)
        return self.tokens[token_id]

    def report_behavior(self, token_id, impact):
        token = self.register(token_id)
        token.update_score(impact)
        return token.behavior_score
