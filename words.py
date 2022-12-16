from database import Post, Comment

unwanted_words = [
    "this",
    "is",
    "nut"
]

filter_targets = {
    "post" : ['full_name', 'title', 'content'],
    "comment" : ['nickname', 'value'],
}

map_to_class = {
    'post': Post,
    'comment': Comment
}