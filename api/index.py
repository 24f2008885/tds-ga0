import contextlib
import io
import json
import math
import re
import traceback
from typing import List, Optional

from fastapi import FastAPI, Query, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

CLASSES = "7T 11W 3C 1P 3F 11K 8K 3B 2O 11C 2L 12V 8X 8S 7T 4M 9C 8E 3D 2G 12R 1F 9T 8R 9X 12G 7W 12A 3X 9M 3L 4I 4U 7X 6U 1W 12J 12N 2B 1W 12W 1W 8K 7S 11J 10Q 10S 9S 1N 9K 11Z 9L 10W 6D 2E 4R 8I 1M 6S 8A 8K 3N 7N 6U 12P 11W 12C 5D 2L 12R 3D 8A 8Z 3A 1R 11S 6B 11Q 9I 6K 4N 11B 5J 7A 4E 2L 1Y 9W 10G 4G 9R 7E 2S 2S 8J 5R 11O 12X 3F 10K 3N 5A 5U 3P 6S 12Z 3Z 12L 8N 8D 4P 12D 4M 2B 1A 4P 2O 11F 7Z 10V 12E 3N 6P 12T 8L 9F 12L 3V 1H 12K 9N 1W 10Y 11Q 9B 1F 5F 12Z 8B 2A 8M 12M 12Z 5Y 10G 2E 1Z 12C 1S 7P 3L 2A 7S 11G 3C 11Y 3F 6E 11V 4E 12J 3X 5F 4M 2E 3S 1J 4E 12Z 9X 11Z 5X 12W 5J 10G 5H 1Y 11D 6X 1S 6C 6N 4S 8Y 10Q 12I 5A 8K 4V 2T 1B 4O 3X 7H 10Z 8H 8F 6G 10W 12Z 1B 6O 2Z 6G 7U 7D 8Y 12X 10P 8C 1X 9D 12M 4V 1M 1X 9F 8E 9J 3C 7L 8F 7V 9I 6N 12U 8J 2X 2D 9K 11N 9O 12R 4H 3L 3Y 11F 2H 8Z 1E 10Y 6M 3K 8V 10E 10L 10K 10D 10X 4H 12V 9Q 2H 6U 7D 7J 11H 6K 11B 8P 5E 1D 1F 10G 6E 1I 7K 2P 1R 4M 1G 1R 6Q 6W 2J 2S 6E 6N 12N 8W 11K 5M 5V 11U 8D 4J 12Y 6K 1T 3E 5G 5T 5X 6M 2L 8H 6X 2T 3D 3D 9R 7R 4M 5R 8N 10R 4Z 8Y 5K 2D 8G 3R 8O 7Z 6G 12X 10C 7F 8S 7D 9G 1F 5P 3K 12L 3I 6U 3H 4B 7T 11H 10R 6B 7D 9J 9X 2K 9N 8T 4Z 8M 1N 8H 5U 5Z 7N 12H 10G 7I 8Z 7A 11K 3T 6K 8Y 4A 10R 3H 7O 5Z 1S 5Z 1I 3J 7X 5Y 10F 3Z 1M 11I 7W 5P 1Y 12O 6W 2P 1G 6V 7J 10F 8B 10W 9T 11Q 3N 9I 12P 8L 9E 10J 12H 9I 10O 11O 7O 6Y 3Q 10G 12I 2P 9U 12Q 4T 1Y 2H 12R 11V 12H 8O 7Q 11P 8B 8U 1C 4H 11T 6K 4E 5V 9B 5G 8F 8R 10Z 12S 3G 6T 9G 7A 12O 10U 9A 3P 4K 2I 5P 11M 5Q 8C 4G 8L 11V 2Q 6N 3D 12H 11I 2H 10V 11D 7H 3B 8E 6P 1D 2S 3E 6A 8Z 5N 11Y 8I 6K 4A 12M 1A 10K 4L 9F 7A 4F 3X 2S 2G 5F 11Y 5D 5D 10C 7N 3U 12I 12C 10Y 7P 11W 10Y 5D 3G 9M 11T 8Y 2V 7Z 6Q 7H 3Q 12E 6O 12O 12O 4E 3F 4U 4J 1B 9L 3D 3P 1N 11M 12F 2P 9U 7D 5N 7O 5Z 4D 1X 7N 11L 5C 7Q 3W 10L 6K 7G 6F 3R 9H 1L 11X 6M 1Y 7S 7Q 1H 11G 12Y 2E 10U 2I 4D 2E 8B 11Z 5E 12K 12Q 9T 11H 7Z 10N 8X 10A 6Y 8B 9Z 3A 11J 5J 2T 2I 9E 2J 1L 11X 4L 12B 7G 12N 9P 1R 3A 12O 8W 8I 12L 8P 10S 7P 2M 9L 9W 10F 11M 5W 1O 3H 6I 9Q 7O 12I 9D 7F 8J 3L 6D 8Z 6S 6H 5Y 5C 2C 9F 11K 1U 5E 3D 5A 12K 7F 1D 12I 9F 11E 10L 9T 9S 8I 6N 11F 10T 6X 3U 8H 12S 2G 3Q 12A 8T 8Q 1E 1X 5R 1E 11T 8J 10U 11O 10X 3S 4M 3I 9O 2O 9M 12P 10R 2Q 10A 3S 5M 4W 11X 8D 3C 4P 12X 4I 10W 9Z 4T 10G 10C 5H 8H 10P 5B 10L 1U 2S 11I 10N 1H 2X 12B 10N 10D 5E 5V 7J 12E 2K 9L 11U 9H 9F 1L 9L 11D 2F 3I 5Z 10R 2Z 1R 3N 2K 8Z 6D 9N 11E 2F 11U 5W 3H 7W 3J 6J 8K 1S 1E 10D 3F 2Y 1T 9W 6G 9J 5L 3Z 7H 12N 3R 1Y 4P 10T 3R 9Y 2P 12W 3V 10X 7B 5F 12D 1Z 11V 2M 4M 1Y 4G 9N 2R 5X 4V 10Q 11H 8G 8J 1P 12W 1Y 8S 10Y 8Z 7L 9C 11G 9G 5N 7R 7J 5Z 10M 5K 5S 3G 11I 5G 2P 9R 7P 2S 7R 9Y 1A 4Q 10N 7A 8D 5Z 2C 2Z 12D 9J 11P 2H 10T 6G 9Q 6P 2G 7O 11Q 1B 9A 1Z 10R 1T 4X 12O 8I 12B 4F 10B 5T 2L 3S 9E 3S 3T 2U 1S 4Y 10B 1K 9S 8C 11X 6C 7X 5E 7S 1T 3S 12I 7V 11R 10J 2D 6U 8S 6T 3F 12S 12D 6G 9B 2T 3M 9K 8E 10N 10Q 1E 1H 10G 12W 3Q 5U 10C 12I 10X 1A 6Q 10B 11J 4E 9Q 7D 3X 5L 11P 2N 8Q 2U 4Z 1O 5B 3D 3A 8I 9N 5V 3Q 9W 12U 12Q 10S 7Q 11R 12H 3F 6G 5E 4F 11V 8Y 1K 6M 10P 11Q 8V 7P 3T 12K 1E 6I 9Z 9N 9U 5H 8M 10D 2Q 6E 1T 4J 10Q 9V 5N 12U 4S 3J 8A 11S 11E 10L 7T 11H 6A 12J 10S 6B 1J 12K 11G 5A 7K 1A 7A 9C 11X 8U 4N 2E 5L 10G 2D 12I 10D 10G 5E 4D 5H 8E 3X 2O 4P 8L 8E 7M 1R 11Y 3C 9Z 7X 11Q 10T 9B 7Q 4J 2R 5M 10X 4V 3D 8X 3S 1K 7E 7Y 7H 11G 3A 10B 12T 7V 11C 4A 5Z 10Q 10X 12Q 11Y 1H 10P 3G 4S 4M 4Z 3O 5Y 3P 7F 7X 8Z 6H 7O 4L 10G 2U 1Z 11F 11C 11E 2O 1O 3R 4X 5I 8J 10B 3F 2G 8F 10J 4X 8A 12M 8U 1H 9U 4N 3Y 9T 7A 7T 1P 2K 6W 6G 9J 7U 12N 7C 2E 9E 2S 7X 4C 9U 1J 12L 12E 12I 12V 4B 6U 10Y 12X 4H 3U 7A 5G 1X 8A 4Q 10J 8M 5B 8F 2O 11D 9E 9O 1Z 12F 7X 11T 9R 7S 4D 1W 12H 11O 1M 1F 7U 11Z 5H 7W 10V 4M 4R 10B 4C 5N 3R 9U 11Z 9K 4A 9K 9L 8S 1D 7Z 8K 6Z 11P 1B 9T 3B 12P 7L 10C 8O 10B 3J 7A 8E 1W 4D 8E 7L 1N 9I 3A 1D 2G 7O 8F 2A 5J 11S 6H 4A 12L 4J 7C 3E 12D 7F 7M 1H 9V 9R 12A 3S 2Z 1V 6P 5Y 7Q 10K 3H 6J 1N 10L 5R 9A 9C 1V 3F 9M 4K 12A 6E 2W 8H 9E 7Q 12J 1L 1A 12H 3U 5H 11O 11H 4E 9K 6Y 12T 6J 3J 11H 7W 8D 10F 3Q 4D 12P 12H 8L 6M 1K 12X 7S 9P 7I 6I 5I 4A 11P 9Q 4I 5B 10Q 12W 8E 4D 8I 4H 11H 12T 3D 12M 6T 12J 4P 9Z 10Q 6E 11Y 8H 7Y 12W 7L 4M 5U 8R 3F 12C 5O 2B 9U 7S 8J 4K 6O 10B 4Y 9Y 8E 12U 1Q 10L 5D 5Q 2S 5M 12Z 7Y 6Z 9O 9Z 10G 11J 7M 3O 9B 10W 11L 9O 12X 2F 11N 12H 12A 7V 6H 3Z 1D 9G 11D 4Y 8A 1K 7O 5P 7S 5H 12Y 3A 10F 10U 11Q 3A 5Q 9T 10G 10I 4I 7Z 6Z 2W 9R 3J 3I 7L 7H 4B 1O 12Z 10H 6X 8L 1H 9L 2Q 11G 12Q 3J 9J 2F 6X 12V 3V 4Z 8X 1M 3I 8L 1Z 5A 7T 11A 10T 7F 7D 2G 10P 2G 3C 2N 12P 10E 4S 2W 4Z 7T 10E 8H 9I 1S 9S 8M 5S 4H 10G 5U 4C 11Q 2C 5B 5C 7T 3P 10P 1Y 10K 9D 5E 5P 2I 9L 11A 11J 1U 8I 4O 6J 9N 2N 5N 1Z 7H 7D 4V 2Y 7Z 6X 6Z 4Z 11U 5P 2C 12B 7S 8F 7G 8B 5A 6S 7H 10O 1H 5F 1K 7Z 8I 6H 6G 11A 10Y 4M 11J 11O 9X 7B 2M 1W 1C 3M 1Y 1P 7A 7G 7W 3M 9M 9C 6Z 5X 6M 11Z 12P 9J 7D 5F 9T 6Y 8H 4Q 11P 10P 4F 1W 9K 3I 8J 1G 2N 3Q 6G 11T 3X 1S 7U 9C 7D 9A 9K 12G 5S 10T 8O 4O 8O 1T 6O 1H 9H 12F 5N 2K 6O 10A 6N 3J 1N 11C 11T 10J 7G 9C 7D 11F 11A 7Q 10A 9R 3O 6Q 4U 5I 5N 4X 6E 1A 4R 12A 7M 5W 11F 8D 1W 3C 11Z 12D 9Y 5D 12C 8B 11R 3T 4E 4V 12H 9X 10G 5I 10G 3M 5R 11Y 11T 7A 9F 5M 2D 7U 8G 7E 11G 6E 2J 1R 2Q 2D 4M 1R 2F 4K 10J 5X 2I 11A 7D 6W 12D 10G 5R 10M 12N 3F 5A 9E 10T 11J 10U 9G 12M 7N 9V 12Y 6X 11W 6T 9E 4I 11Q 10U 11F 5T 2P 11Q 8P 12K 12K 4L 10B 12C 4N 8N 7C 6T 3S 12P 12K 2U 2W 7T 8V 8W 7I 7Q 3T 7J 9T 2R 8K 11P 10Q 2A 4O 9X 2A 2K 9N 4D 12X 5H 12M 6X 8N 6D 1T 2Z 12O 6U 11D 12N 4I 2T 6U 3M 8J 12A 6X 9K 5A 8T 6M 10E 8J 2X 12R 5J 12U 2L 5M 8Z 3H 8R 11J 7T 12O 7H 12M 10B 8Q 3E 11K 6N 6F 10J 4P 12K 1T 8A 1X 10O 5D 7P 1J 9Y 1B 8N 3P 10H 7M 6N 6D 12C 5K 12X 4O 12U 9P 3N 7H 10N 4G 10L 3Q 1G 12M 7Y 1G 7L 11F 6G 2M 8F 10A 11A 3X 10G 5Z 2Q 6T 6R 12U 4D 4O 4D 9L 1S 3T 10F 1N 1F 2Y 9G 6G 4G 12G 4O 1I 3W 7F 6Y 11T 3P 5O 4Y 11T 6M 12B 9V 12Y 8O 1T 11T 6F 12H 3U 10M 2F 5N 12T 10O 4K 3Q 2J 9Y 4M 5Y 4Q 9B 11L 11G 6E 7Q 11Q 11R 9G 4B 12A 12B 7U 9W 8I 2E 6E 9Z 4R 2U 8N 5N 5I 8K 7Q 7Q 8G 12D 10L 12V 3P 4J 8L 3F 10M 12S 2M 3Y 7A 5G 7B 7M 2J 12I 6H 3R 4L 9T 5V 10G 1I 2B 8J 10S 6Q 10I 7Z 5U 7O 2Y 4C 4G 7G 7T 12R 6Q 7N 12D 1X 2B 8J 4M 4O 9X 10C 8E 2Q 5Q 8C 5A 3G 6O 3L 12J 5L 11F 6N 1S 2I 2G 9J 4L 12R 2O 6V 5K 9M 6H 9K 7N 1P 5K 4T 5R 10M 5W 9C 12W 4Y 11P 4Z 11W 9J 11Y 4W 2E 3I 5Y 7T 7Y 11D 7P 7D 2E 6O 10N 10N 2Z 11U 7W 10S 9L 6X 10R 1D 12S 2X 8S 8O 4I 3B 7S 12A 7C 6K 9S 10M 8O 4W 1C 9N 11W 2A 4N 3M 4O 6D 1E 3A 10F 2S 1D 12J 11S 6O 11A 1Y 8W 12J 7H 4J 6Z 3K 10W 5Q 8K 12Q 1W 3Q 7Q 12T 3I 1E 6Q 6C 6F 9M 8T 10H 12A 6Z 4S 3P 12X 3W 3G 10W 3T 8M 2C 4W 4C 2D 11U 1D 7X 2D 7B 7T 8H 8G 3L 2J 12O 11D 11R 3P 9J 9B 4L 5E 7D 7E 10H 9X 3F 11T 4K 6M 2S 4Z 8F 3A 11Y 4E 5B 4E 2L 9G 12J 4J 2F 2Y 3P 11X 12P 1C 12H 8F 11D 2W 4E 2Y 12T 2Z 11K 7L 6X 6E 1V 9L 6U 8L 1Y 7G 2Q".split()
STUDENTS = [{"studentId": i + 1, "class": c} for i, c in enumerate(CLASSES)]
TELEMETRY = json.loads(r'''[{"region":"apac","service":"catalog","latency_ms":181.23,"uptime_pct":97.341,"timestamp":20250301},{"region":"apac","service":"analytics","latency_ms":218.6,"uptime_pct":98.936,"timestamp":20250302},{"region":"apac","service":"payments","latency_ms":112.57,"uptime_pct":98.882,"timestamp":20250303},{"region":"apac","service":"checkout","latency_ms":144.7,"uptime_pct":99.357,"timestamp":20250304},{"region":"apac","service":"analytics","latency_ms":162.65,"uptime_pct":98.135,"timestamp":20250305},{"region":"apac","service":"payments","latency_ms":212.51,"uptime_pct":98.948,"timestamp":20250306},{"region":"apac","service":"support","latency_ms":219.34,"uptime_pct":98.314,"timestamp":20250307},{"region":"apac","service":"catalog","latency_ms":116.36,"uptime_pct":99.266,"timestamp":20250308},{"region":"apac","service":"analytics","latency_ms":151.48,"uptime_pct":97.779,"timestamp":20250309},{"region":"apac","service":"analytics","latency_ms":141.85,"uptime_pct":99.447,"timestamp":20250310},{"region":"apac","service":"analytics","latency_ms":192.53,"uptime_pct":97.103,"timestamp":20250311},{"region":"apac","service":"analytics","latency_ms":117.09,"uptime_pct":98.478,"timestamp":20250312},{"region":"emea","service":"recommendations","latency_ms":164.54,"uptime_pct":98.222,"timestamp":20250301},{"region":"emea","service":"payments","latency_ms":125.49,"uptime_pct":97.209,"timestamp":20250302},{"region":"emea","service":"checkout","latency_ms":144.94,"uptime_pct":98.268,"timestamp":20250303},{"region":"emea","service":"checkout","latency_ms":131.06,"uptime_pct":98.415,"timestamp":20250304},{"region":"emea","service":"analytics","latency_ms":208.22,"uptime_pct":97.768,"timestamp":20250305},{"region":"emea","service":"payments","latency_ms":196.29,"uptime_pct":98.149,"timestamp":20250306},{"region":"emea","service":"analytics","latency_ms":191.72,"uptime_pct":98.692,"timestamp":20250307},{"region":"emea","service":"catalog","latency_ms":211.8,"uptime_pct":97.526,"timestamp":20250308},{"region":"emea","service":"support","latency_ms":215.81,"uptime_pct":97.701,"timestamp":20250309},{"region":"emea","service":"analytics","latency_ms":128.12,"uptime_pct":97.902,"timestamp":20250310},{"region":"emea","service":"payments","latency_ms":200.14,"uptime_pct":97.679,"timestamp":20250311},{"region":"emea","service":"support","latency_ms":117.84,"uptime_pct":97.11,"timestamp":20250312},{"region":"amer","service":"support","latency_ms":220.6,"uptime_pct":99.35,"timestamp":20250301},{"region":"amer","service":"analytics","latency_ms":148.87,"uptime_pct":99.002,"timestamp":20250302},{"region":"amer","service":"recommendations","latency_ms":149.76,"uptime_pct":97.134,"timestamp":20250303},{"region":"amer","service":"catalog","latency_ms":187.32,"uptime_pct":99.267,"timestamp":20250304},{"region":"amer","service":"payments","latency_ms":215.25,"uptime_pct":97.373,"timestamp":20250305},{"region":"amer","service":"checkout","latency_ms":151.86,"uptime_pct":97.21,"timestamp":20250306},{"region":"amer","service":"payments","latency_ms":200.32,"uptime_pct":97.624,"timestamp":20250307},{"region":"amer","service":"recommendations","latency_ms":219.25,"uptime_pct":98.45,"timestamp":20250308},{"region":"amer","service":"checkout","latency_ms":174.8,"uptime_pct":98.351,"timestamp":20250309},{"region":"amer","service":"payments","latency_ms":185.97,"uptime_pct":97.333,"timestamp":20250310},{"region":"amer","service":"catalog","latency_ms":124.43,"uptime_pct":98.406,"timestamp":20250311},{"region":"amer","service":"catalog","latency_ms":207.7,"uptime_pct":97.817,"timestamp":20250312}]''')


@app.get("/")
def root():
    return {"message": "TDS GA0 endpoints: /api, /sentiment, /code-interpreter, /latency"}


# Q10: serve student data, filter by ?class=
@app.get("/api")
def get_students(class_: Optional[List[str]] = Query(None, alias="class")):
    if not class_:
        return {"students": STUDENTS}
    wanted = set(class_)
    return {"students": [s for s in STUDENTS if s["class"] in wanted]}


# Q11: batch sentiment
HAPPY_WORDS = [
    "love", "joy", "happy", "happiest", "happiness", "wonderful", "amazing", "great", "excited",
    "exciting", "excitement", "thrilled", "delighted", "grateful", "fantastic", "best", "perfect",
    "perfectly", "proud", "blessed", "bliss", "beautiful", "ecstatic", "overjoyed", "smiling",
    "grinning", "celebrating", "fortunate", "spectacular", "dream come true", "cloud nine",
    "alive", "energized", "exceeded", "hoping for", "glad", "awesome", "excellent", "enjoy",
]
SAD_WORDS = [
    "sad", "sadness", "worst", "worse", "terrible", "heartbroken", "broken", "devastated",
    "regret", "disappointed", "disappointment", "lonely", "abandoned", "falling apart", "depression",
    "badly", "hopeless", "crying", "pain", "miserable", "exhausted", "traumatized", "defeated",
    "sorrow", "failure", "failed", "empty", "anxiety", "lost", "grief", "worried", "shattered",
    "betrayal", "haunted", "crushed", "burdened", "problems", "struggling", "suffering",
    "layoffs", "rejected", "passed away", "nobody", "awful", "hate", "angry", "upset", "drowning",
]


def classify(sentence: str) -> str:
    s = sentence.lower()
    sad = any(re.search(r"\b" + re.escape(w) + r"\b", s) for w in SAD_WORDS)
    happy = any(re.search(r"\b" + re.escape(w) + r"\b", s) for w in HAPPY_WORDS)
    if happy and not sad:
        return "happy"
    if sad and not happy:
        return "sad"
    if sentence.strip().endswith("!"):
        return "happy"
    if sad:
        return "sad"
    if re.search(r"\b(i|i'm|i've|my|me)\b", s):
        return "sad"
    return "neutral"


@app.post("/sentiment")
async def sentiment(request: Request):
    body = await request.json()
    sentences = body.get("sentences", [])
    return {"results": [{"sentence": s, "sentiment": classify(s)} for s in sentences]}


# Q5: code interpreter with error-line analysis
def execute_python_code(code: str) -> dict:
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            exec(code, {"__name__": "__main__"})
        return {"success": True, "output": buf.getvalue()}
    except BaseException:
        return {"success": False, "output": traceback.format_exc()}


def analyze_error(code: str, exc: BaseException) -> List[int]:
    if isinstance(exc, SyntaxError) and exc.lineno:
        return [exc.lineno]
    frames = [f for f in traceback.extract_tb(exc.__traceback__) if f.filename == "<string>"]
    if frames:
        return [frames[-1].lineno]
    return []


@app.post("/code-interpreter")
async def code_interpreter(request: Request):
    body = await request.json()
    code = body.get("code", "")
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            exec(compile(code, "<string>", "exec"), {"__name__": "__main__"})
        return {"error": [], "result": buf.getvalue()}
    except BaseException as exc:
        return {"error": analyze_error(code, exc), "result": traceback.format_exc()}


# Q25: latency analytics
def percentile(values, q):
    v = sorted(values)
    pos = (len(v) - 1) * q
    lo = math.floor(pos)
    frac = pos - lo
    if lo + 1 < len(v):
        return v[lo] + frac * (v[lo + 1] - v[lo])
    return v[lo]


@app.post("/latency")
async def latency(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold = float(body.get("threshold_ms", 180))
    out = []
    for region in regions:
        rows = [r for r in TELEMETRY if r["region"] == region]
        if not rows:
            out.append({"region": region, "avg_latency": None, "p95_latency": None, "avg_uptime": None, "breaches": 0})
            continue
        lat = [r["latency_ms"] for r in rows]
        up = [r["uptime_pct"] for r in rows]
        out.append({
            "region": region,
            "avg_latency": round(sum(lat) / len(lat), 2),
            "p95_latency": round(percentile(lat, 0.95), 2),
            "avg_uptime": round(sum(up) / len(up), 3),
            "breaches": sum(1 for x in lat if x > threshold),
        })
    return {"regions": out}
