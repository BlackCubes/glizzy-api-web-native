# To keep things DRY
model_error_messages = {
    "uuid": {"unique": "The uuid is not unique."},
    "reaction_count": {
        "blank": "The reaction count cannot be empty.",
        "invalid": "The reaction count needs to be a valid integer.",
        "required": "The reaction count is required.",
    },
    "emoji": {
        "blank": "The emoji cannot be empty.",
        "does_not_exist": "The emoji does not exist.",
        "invalid": "Invalid value for the emoji.",
        "null": "The emoji cannot be empty.",
        "required": "The emoji is required.",
    },
    "glizzy": {
        "blank": "The glizzy cannot be empty.",
        "does_not_exist": "The glizzy does not exist.",
        "invalid": "Invalid value for the glizzy.",
        "null": "The glizzy cannot be empty.",
        "required": "The glizzy is required.",
    },
}
