# custom_filters.py
from django import template

register = template.Library()

@register.filter
def filter_candidate_and_position(user_votes, candidate_position):
    candidate, position = candidate_position.split(':')
    return user_votes.filter(candidate=candidate, position=position).exists()
