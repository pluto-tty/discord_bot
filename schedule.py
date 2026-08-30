import random
import messages


def choose(pool):
    return random.choice(pool)


def get_message(day, period):
    """
    day:
        0 Monday
        1 Tuesday
        2 Wednesday
        3 Thursday
        4 Friday
        5 Saturday
        6 Sunday
    """

    # Monday - Thursday
    if 0 <= day <= 3:

        if period == "morning":
            return choose(
                messages.MORNING_MOTIVATION
                + messages.FUTURE_SELF
                + messages.PEOPLE_YOU_LOVE
                + messages.PEOPLE_AHEAD
                + messages.REGRET
            )

        if period == "midday":
            return choose(
                messages.MIDDAY_CHALLENGE
                + messages.MIDDAY_TRASH_TALK
            )

        if period == "evening":
            return choose(
                messages.EVENING_REFLECTION
                + messages.EVENING_HONESTY
            )

    # Friday
    if day == 4:

        if period == "morning":
            return choose(
                messages.FRIDAY_MORNING
                + messages.FUTURE_SELF
                + messages.REGRET
            )

        if period == "midday":
            return choose(
                messages.FRIDAY_MIDDAY
                + messages.MIDDAY_CHALLENGE
                + messages.MIDDAY_TRASH_TALK
            )

        if period == "evening":
            return choose(messages.FRIDAY_SOCIAL)

    # Saturday
    if day == 5:

        if period == "morning":
            return choose(
                messages.WEEKEND_MORNING
                + messages.WEEKEND_IMPORTANT
            )

        if period == "midday":
            return choose(
                messages.WEEKEND_IMPORTANT
                + messages.WEEKEND_WORKING
                + messages.WEEKEND_REST
                + messages.DIGITAL_DETOX
            )

        if period == "evening":
            return choose(
                messages.WEEKEND_REST
                + messages.DIGITAL_DETOX
            )

    # Sunday
    if day == 6:

        if period == "morning":
            return choose(
                messages.SUNDAY_MORNING
                + messages.WEEKEND_MORNING
                + messages.WEEKEND_IMPORTANT
            )

        if period == "midday":
            return choose(
                messages.WEEKEND_REST
                + messages.DIGITAL_DETOX
                + messages.WEEKEND_WORKING
            )

        if period == "evening":
            return choose(messages.SUNDAY_EVENING)

    return None
