def create_field_choices(cls):
    return [(var, var) for key, var in vars(cls).items() if not key.startswith('_')]
