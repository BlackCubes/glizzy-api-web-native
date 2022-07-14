# To keep things DRY
model_error_messages = {
    "uuid": {"unique": "The uuid is not unique."},
    "emoji": {
        "blank": "The emoji cannot be empty.",
        "max_length": "The emoji should be no more than 1 character.",
        "required": "The emoji is required.",
        "unique": "The emoji already exists.",
    },
    "name": {
        "blank": "The name cannot be empty.",
        "max_length": "The name should be no more than 100 characters.",
        "required": "The name is required.",
        "unique": "The name already exists.",
    },
    "slug": {
        "max_length": "The slug should be no more than 100 characters.",
    },
}
