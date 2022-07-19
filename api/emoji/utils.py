# To keep things DRY
model_error_messages = {
    "uuid": {"unique": "The uuid is not unique."},
    "emoji": {
        "blank": "The emoji cannot be empty.",
        "does_not_exist": "The emoji does not exist.",
        "invalid": "Invalid value for the emoji.",
        "max_length": "The emoji should be no more than 1 character.",
        "null": "The emoji cannot be empty.",
        "required": "The emoji is required.",
        "unique": "The emoji already exists.",
    },
    "name": {
        "blank": "The name cannot be empty.",
        "invalid": "Invalid value for the name.",
        "max_length": "The name should be no more than 100 characters.",
        "null": "The name cannot be empty.",
        "required": "The name is required.",
        "unique": "The name already exists.",
    },
    "slug": {
        "does_not_exist": "The slug does not exist.",
        "invalid": "Invalid value for the slug.",
        "max_length": "The slug should be no more than 100 characters.",
        "null": "The slug cannot be empty.",
    },
}
