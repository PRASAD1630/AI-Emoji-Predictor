import re
from emoji_data import emoji_dict


def predict_emoji(text):
    """
    Predict emojis from user input.
    Returns:
        emojis (list)
        detected_keywords (list)
    """

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # Split into words
    words = text.split()

    emojis = []
    detected_keywords = []

    # Search for keywords
    for word in words:

        if word in emoji_dict:

            detected_keywords.append(word)

            for emoji in emoji_dict[word]:

                if emoji not in emojis:
                    emojis.append(emoji)

    # Default emoji
    if len(emojis) == 0:
        emojis = ["🤔"]

    return emojis, detected_keywords