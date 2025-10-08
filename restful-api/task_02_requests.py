import csv
from typing import List, Dict

import requests


JSONPLACEHOLDER_POSTS_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts() -> None:
    """Fetch posts from JSONPlaceholder, print status code and all titles."""
    try:
        response = requests.get(JSONPLACEHOLDER_POSTS_URL, timeout=10)
        print(f"Status Code: {response.status_code}")
    except requests.RequestException:
        print("Status Code: 000")
        return

    if 200 <= response.status_code < 300:
        try:
            posts = response.json()
        except ValueError:
            return

        for post in posts:
            title = post.get("title", "")
            if title:
                print(title)


def fetch_and_save_posts(csv_filename: str = "posts.csv") -> None:
    """Fetch posts and save id, title, body to a CSV file.

    Args:
        csv_filename: Nombre del archivo CSV de salida.
    """
    try:
        response = requests.get(JSONPLACEHOLDER_POSTS_URL, timeout=10)
    except requests.RequestException:
        return

    if not (200 <= response.status_code < 300):
        return

    try:
        posts = response.json()
    except ValueError:
        return

    structured_posts: List[Dict[str, str]] = [
        {
            "id": post.get("id"),
            "title": post.get("title", ""),
            "body": post.get("body", ""),
        }
        for post in posts
    ]

    if not structured_posts:
        return

    fieldnames = ["id", "title", "body"]
    with open(csv_filename, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(structured_posts)


__all__ = [
    "fetch_and_print_posts",
    "fetch_and_save_posts",
]


