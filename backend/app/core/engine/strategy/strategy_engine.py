def validate_strategy(strategy):
    required_fields = ("name",)
    missing_fields = [
        field for field in required_fields if not getattr(strategy, field, None)
    ]

    return {
        "valid": not missing_fields,
        "missing_fields": missing_fields,
    }
