from __future__ import annotations
from bankcraft.config import *
from bankcraft.motivation.motivation_state import *


class Motivation:

    def __init__(self, state) -> None:
        self._state = state
        self.set_state(NeutralState)
        self.critical_motivation = None
        
        #self.states = [HungerState(self), FatigueState(self), ConsumerismState(self), SocialState(self), WorkState(self)]
        self.states_rate = {HungerState(self): hunger_rate,
                            FatigueState(self): fatigue_rate,
                            ConsumerismState(self): consumerism_rate,
                            SocialState(self): social_rate,
                            WorkState(self): work_rate}


    def set_state(self, state: MotivationState):
        self._state = state
        self._state.motivation = self
        
    def set_motion(self):
        self._state.set_motion()

    def set_transaction(self):
        self._state.set_transaction()

    def __str__(self):
        return str(self._state)

    def get_critical_motivation(self):
        max_motivation, max_motivation_value = self.get_max_motivation()
        if max_motivation_value > motivation_threshold:
            return max_motivation

    def get_max_motivation(self):
        max_value = 0
        max_motivation = None
        for state_class in self.states_rate.keys():
            state = state_class
            value = state.get_value()
            if value > max_value:
                max_value = value
                max_motivation = state

        return max_motivation, max_value

    def reset_one_motivation(self, motivation):
        setattr(self, motivation, 1)

    def present_state(self):
        return self._state

    def live(self):
        for state in self.states_rate.keys():
            state.update_value(self.states_rate[state])


    def step(self):
        self.live()
        self.critical_motivation= self.get_critical_motivation()
        if self.critical_motivation is not None:
            print('The critical motivation is: ', self.critical_motivation)
            self.set_state(self.critical_motivation)  # Set the critical motivation state
            print(f"{self}")
            self.set_transaction()
            self.set_motion()
