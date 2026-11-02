
"""
Signal two: Stylometric analysis.

Measures writing structure without understanding meaning.

Features:
1. Sentence length variation
2. Vocabulary diversity
3. Punctuation density

Returns a score between 0 and 1.
Higher scores indicate more AI-like writing patterns.

Important:
These are heuristic indicators, not verified probabilities
of AI authorship.
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split text into sentences."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Extract lowercase words."""
    return re.findall(r"[a-z0-9']+", text.lower())


def clamp(value: float) -> float:
    """Keep a score between 0 and 1."""
    return max(0.0, min(1.0, value))


# --------------------------------------------------
# Feature 1: Sentence Length Spread
# --------------------------------------------------

def sentence_length_spread(text: str) -> float:
    """
    Calculate coefficient of variation of sentence lengths.

    Higher values mean more variation.
    Lower values mean more uniform sentence lengths.
    """

    lengths = [
        len(words(sentence))
        for sentence in sentences(text)
    ]

    lengths = [length for length in lengths if length > 0]

    if len(lengths) < 2:
        return 0.0

    mean_length = statistics.mean(lengths)

    if mean_length == 0:
        return 0.0

    std_dev = statistics.stdev(lengths)

    return std_dev / mean_length


# --------------------------------------------------
# Feature 2: Type Token Ratio
# --------------------------------------------------

def type_token_ratio(text: str) -> float:
    """
    Calculate unique words / total words.

    Higher means more vocabulary diversity.
    """

    tokens = words(text)

    if not tokens:
        return 0.0

    unique_words = len(set(tokens))

    return unique_words / len(tokens)


# --------------------------------------------------
# Feature 3: Punctuation Density
# --------------------------------------------------

def punctuation_density(text: str) -> float:
    """
    Calculate punctuation marks per character.

    Includes commas, periods, semicolons,
    colons, question marks, exclamation marks,
    and dashes.
    """

    if not text:
        return 0.0

    punctuation = re.findall(r"[.,;:!?—–-]", text)

    return len(punctuation) / len(text)


# --------------------------------------------------
# Combine Features Into Style Signal
# --------------------------------------------------

def style_signal(text: str) -> float:
    """
    Return an AI-like style score between 0 and 1.

    Higher = more AI-like patterns.

    This is a heuristic score, not an AI probability.
    """

    tokens = words(text)

    if not tokens:
        return 0.5

    # Very short samples have unreliable style statistics.
    if len(tokens) < 30 or len(sentences(text)) < 3:
        return 0.5

    spread = sentence_length_spread(text)
    diversity = type_token_ratio(text)
    punctuation = punctuation_density(text)

    # Lower sentence variation -> more AI-like.
    spread_score = 1.0 - clamp(spread / 0.8)

    # Lower vocabulary diversity -> more AI-like.
    diversity_score = 1.0 - clamp(diversity)

    # Punctuation outside a middle range is treated
    # as less typical of conventional generated prose.
    punctuation_score = clamp(
        1.0 - abs(punctuation - 0.025) / 0.05
    )

    # Weighted combination
    raw_score = (
        0.45 * spread_score
        + 0.35 * diversity_score
        + 0.20 * punctuation_score
    )

    # Shrink toward uncertainty because stylometry
    # is weak evidence of authorship by itself.
    final_score = 0.5 + 0.5 * (raw_score - 0.5)

    return round(clamp(final_score), 4)


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. "
        "It handles most cases correctly and provides good results. "
        "Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences")
    print(f"{len(words(text))} words\n")

    print(
        "sentence_length_spread  ",
        sentence_length_spread(text)
    )

    print(
        "type_token_ratio        ",
        type_token_ratio(text)
    )

    print(
        "punctuation_density     ",
        punctuation_density(text)
    )

    print(
        "style_signal            ",
        style_signal(text),
        "(higher = more AI-like)"
    )
