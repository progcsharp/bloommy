async def next_state(state, state_class):
    all_states = list(state_class.__all_states__)
    return all_states[all_states.index(state)+1]
